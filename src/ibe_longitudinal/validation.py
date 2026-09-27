"""Schema, provenance, temporal, and append-only validation (no network I/O)."""
from datetime import datetime
from hashlib import sha256
from importlib.resources import files
import json
import re
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

DIMENSIONS = ("phenomenon", "cause", "ownership", "severity", "fix_trajectory")
ZERO_HASH = "0" * 64


class ValidationError(ValueError):
    """A journal violates the storage or research contract."""


def digest(data):
    return sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")


def event_hash(event):
    return digest(canonical({k: v for k, v in event.items() if k != "hash"}))


def timestamp(value):
    try:
        require(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z", value)), "timestamp must be a UTC date-time ending in Z")
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"invalid UTC timestamp: {value}") from exc


FORMATS = FormatChecker()


@FORMATS.checks("date-time", raises=ValidationError)
def _utc_datetime(value):
    if not isinstance(value, str):
        return True  # The schema's type keyword handles non-strings.
    timestamp(value)
    return True


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def artifact_path(root, path):
    candidate = Path(path)
    require(not candidate.is_absolute() and ".." not in candidate.parts, f"unsafe artifact path: {path}")
    root = Path(root).resolve()
    target = (root / candidate).resolve()
    require(target.is_relative_to(root), f"artifact escapes root: {path}")
    return target


def resolve_pointer(document, pointer):
    """Resolve RFC 6901 pointers; reject missing nodes instead of guessing."""
    require(pointer.startswith('/'), 'source pointer must start with /')
    try:
        for token in pointer[1:].split('/'):
            token = token.replace('~1', '/').replace('~0', '~')
            document = document[int(token)] if isinstance(document, list) else document[token]
        return document
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        raise ValidationError(f'invalid source pointer: {pointer}') from exc


def _unique(items, label):
    result = {}
    for item in items:
        require(item["id"] not in result, f"duplicate {label} id: {item['id']}")
        result[item["id"]] = item
    return result


def validate(data, root=None, previous=None):
    """Validate a journal; root additionally verifies all pinned artifact bytes.

    previous protects immutable headers and historical prefixes, even against a
    rewritten hash chain. Keep previous versions in version control.
    """
    schema = json.loads(files("ibe_longitudinal").joinpath("schema.json").read_text())
    errors = sorted(Draft202012Validator(schema, format_checker=FORMATS).iter_errors(data), key=lambda e: str(list(e.path)))
    if errors:
        error = errors[0]
        raise ValidationError(f"schema {list(error.path)}: {error.message}")
    if previous is not None:
        validate(previous)
        for key in ("schema_version", "dataset_id", "frozen_release", "cases"):
            require(data[key] == previous[key], f"immutable field changed: {key}")
        for key in ("artifacts", "events"):
            require(data[key][:len(previous[key])] == previous[key], f"historical {key} changed or removed")
    artifacts = _unique(data["artifacts"], "artifact")
    require(len({a['path'] for a in data['artifacts']}) == len(artifacts), "duplicate artifact path")
    for artifact in artifacts.values():
        target = artifact_path(root or Path.cwd(), artifact["path"])
        if root is not None:
            require(target.is_file(), f"missing artifact: {artifact['path']}")
            require(digest(target.read_bytes()) == artifact["sha256"], f"artifact hash mismatch: {artifact['path']}")
    cases = _unique(data["cases"], "case")
    require(len({c['issue_url'] for c in cases.values()}) == len(cases), "duplicate issue URL")
    for case in cases.values():
        for field, kind in (("report_artifact_id", "frozen_report"), ("metadata_artifact_id", "frozen_metadata")):
            require(case[field] in artifacts and artifacts[case[field]]["kind"] == kind, f"invalid {field} in {case['id']}")
        if root is not None:
            metadata = json.loads(artifact_path(root, artifacts[case['metadata_artifact_id']]['path']).read_text())
            require(metadata.get('issue_url') == case['issue_url'], "frozen metadata issue mismatch")
            require(metadata.get('snapshot_completed_utc') == case['frozen_at'], "frozen metadata time mismatch")
    _unique(data["events"], "event")
    seen, latest = {}, {}
    prior_hash, prior_time = ZERO_HASH, None
    for event in data["events"]:
        eid, cid, kind, payload = event["id"], event["case_id"], event["kind"], event["payload"]
        require(cid in cases, f"unknown case: {cid}")
        recorded = timestamp(event["recorded_at"])
        frozen = timestamp(cases[cid]["frozen_at"])
        require(recorded >= frozen, f"record predates freeze: {eid}")
        require(prior_time is None or recorded >= prior_time, f"recording time moves backwards: {eid}")
        require(event['previous_hash'] == prior_hash and event['hash'] == event_hash(event), f"broken hash chain: {eid}")
        if kind == "evidence":
            occurred, observed = timestamp(payload["occurred_at"]), timestamp(payload["observed_at"])
            require(occurred <= observed <= recorded, f"invalid evidence chronology: {eid}")
            if payload['kind'] == 'research_snapshot':
                require(payload['temporal_scope'] == 'research_snapshot' and occurred == observed, f"invalid research snapshot time: {eid}")
            else:
                require(payload['temporal_scope'] != 'research_snapshot', f"only research snapshots use snapshot scope: {eid}")
                require((occurred > frozen) == (payload['temporal_scope'] == 'post_freeze'), f"incorrect pre/post-freeze scope: {eid}")
            source = payload['source']
            require(source['artifact_id'] is None or source['artifact_id'] in artifacts, f"unknown evidence artifact: {eid}")
            if source.get('origin') == 'research_summary':
                require(source['artifact_id'] in artifacts and 'json_pointer' in source, f"research summary needs pinned source and pointer: {eid}")
                if root is not None:
                    document = json.loads(artifact_path(root, artifacts[source['artifact_id']]['path']).read_text())
                    located = resolve_pointer(document, source['json_pointer'])
                    require(document.get('as_of_utc') == payload['observed_at'], f"source observation cutoff mismatch: {eid}")
                    if 'source_record' in payload:
                        require(payload['source_record'] == located, f"source record differs from original: {eid}")
                if 'source_record' in payload:
                    original = payload['source_record']
                    if payload['kind'] == 'research_snapshot':
                        require(original.get('issue_url') == cases[cid]['issue_url'], f"snapshot belongs to another case: {eid}")
                        require(original.get('frozen_artifact', {}).get('snapshot_completed_utc') == cases[cid]['frozen_at'], f"snapshot freeze mismatch: {eid}")
                        require(original.get('frozen_artifact', {}).get('report_sha256') == artifacts[cases[cid]['report_artifact_id']]['sha256'], f"snapshot report mismatch: {eid}")
                        require(payload['statement'] == original.get('freeze_context'), f"snapshot summary mismatch: {eid}")
                    elif 'at_utc' in original:
                        require(all(payload[key] == original[source_key] for key, source_key in (('occurred_at','at_utc'),('statement','statement'),('epistemic_status','evidence_type'),('source_kind','kind'))) and source['url'] == original['url'], f"timeline differs from source: {eid}")
                    elif payload.get('source_kind') in ('opened_utc', 'merged_utc', 'closed_utc', 'published_utc'):
                        require(original.get(payload['source_kind']) == payload['occurred_at'] and original.get('url') == source['url'], f"transition differs from source: {eid}")
            if payload['epistemic_status'] == 'maintainer_confirmed_fact':
                require(source['author_role'] == 'maintainer', f"maintainer confirmation needs maintainer provenance: {eid}")
        else:
            evidence = []
            for ref in payload['evidence_ids']:
                require(ref in seen and seen[ref]['case_id'] == cid and seen[ref]['kind'] == 'evidence', f"invalid evidence reference: {eid} -> {ref}")
                evidence.append(seen[ref])
            slot = (cid, payload['dimension'] if kind == 'adjudication' else 'outcome')
            require(payload['supersedes'] == latest.get(slot), f"supersedes must reference latest revision: {eid}")
            if kind == 'adjudication':
                if payload['verdict'] == 'source_recorded':
                    pointer = payload['source_pointer']
                    require(pointer['artifact_id'] in artifacts, f"unknown adjudication source: {eid}")
                    require(payload['epistemic_status'] == 'researcher_inference', f"frozen alignment remains researcher judgment: {eid}")
                    require(any(e['payload'].get('source_record', {}).get('dimensions', {}).get(payload['dimension']) == payload['source_assessment'] and e['payload'].get('source_record', {}).get('frozen_report_adjudication', {}).get('dimension_alignment', {}).get(payload['dimension']) == payload['frozen_alignment'] and e['payload']['source']['artifact_id'] == pointer['artifact_id'] and e['payload']['source'].get('json_pointer') == pointer['pointer'] for e in evidence), f"source adjudication differs from case snapshot: {eid}")
                require(payload['verdict'] in ('unresolved', 'not_assessed') or evidence, f"verdict needs evidence: {eid}")
                if payload['epistemic_status'] == 'maintainer_confirmed_fact':
                    require(any(e['payload']['epistemic_status'] == 'maintainer_confirmed_fact' for e in evidence), f"adjudication lacks maintainer confirmation: {eid}")
                if payload['epistemic_status'] == 'observed_fact' and evidence:
                    require(any(e['payload']['epistemic_status'] != 'researcher_inference' for e in evidence), f"observed adjudication cites inference only: {eid}")
                if payload['verdict'] == 'unresolved':
                    require(payload['unresolved_questions'], f"unresolved verdict needs questions: {eid}")
            else:
                for dimension, ref in payload['dimension_ids'].items():
                    require(latest.get((cid, dimension)) == ref, f"outcome must reference latest {dimension}: {eid}")
                if 'source_disposition' in payload:
                    snapshots = [e['payload']['source_record'] for e in evidence if e['payload']['kind'] == 'research_snapshot' and 'source_record' in e['payload']]
                    require(any(payload['source_disposition'] == c['dimensions']['fix_trajectory']['status'] and payload['rationale'] == c['dimensions']['fix_trajectory']['assessment'] and payload['issue_state'] == c['issue_state_as_of'] and payload['unresolved_questions'] == c['unresolved'] for c in snapshots), f"outcome differs from source snapshot: {eid}")
                    require(payload['status'] == 'unresolved' and payload['resolution'] == 'unknown', f"source import cannot infer finality or normalized resolution: {eid}")
                if payload['status'] == 'final':
                    require(evidence and payload['resolution'] != 'unknown', f"final outcome needs evidence and resolution: {eid}")
                    require(not payload['unresolved_questions'], f"final outcome has unresolved questions: {eid}")
                    require(all(seen[r]['payload']['verdict'] not in ('unresolved', 'not_assessed', 'source_recorded') and not seen[r]['payload']['unresolved_questions'] for r in payload['dimension_ids'].values()), f"final outcome has unresolved dimensions: {eid}")
                else:
                    require(payload['unresolved_questions'], f"unresolved outcome needs questions: {eid}")
            latest[slot] = eid
        seen[eid] = event
        prior_hash, prior_time = event['hash'], recorded
    return data
