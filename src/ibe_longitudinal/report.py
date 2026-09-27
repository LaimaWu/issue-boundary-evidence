"""Deterministic projections; no classification, scoring, or evidence inference."""
import html
import json
import re

from .validation import DIMENSIONS, timestamp, validate


def literal(value):
    text = html.escape(str(value), quote=True)
    text = re.sub(r'([\\`*_{}\[\]()#+.!|>~\-])', r'\\\1', text)
    return text.replace('@', '&#64;').replace(':', '&#58;').replace('\n', '<br>')


def render(data, as_of=None):
    validate(data)
    cutoff = timestamp(as_of) if as_of else None
    events = [e for e in data['events'] if cutoff is None or timestamp(e['recorded_at']) <= cutoff]
    source_cutoffs = sorted({e['payload']['observed_at'] for e in events if e['kind'] == 'evidence' and e['payload']['kind'] == 'research_snapshot'})
    lines = ['# IBE longitudinal adjudication / outcome report', '',
             f"Dataset: {literal(data['dataset_id'])} · Frozen release: {literal(data['frozen_release'])}", '',
             f"Knowledge cutoff (recorded_at): {literal(as_of or (events[-1]['recorded_at'] if events else 'No research events imported'))}", '',
             f"Source study observation cutoff(s): {literal(', '.join(source_cutoffs) or 'No imported study snapshots')}", '',
             'Independent research layer. Frozen reports are immutable inputs. Issue closure does not establish a final research outcome. No accuracy score is computed.', '',
             'Pre-freeze context is shown separately from post-freeze evidence. Claim status is recorded by the researcher; validation checks structure and provenance, not the truth of a claim.', '',
             'Research snapshots retain source-assigned labels and are not upstream events. Imported summaries are secondary provenance, not freshly fetched GitHub records. source_recorded is a lossless transport state, not a success score.', '', '## Case overview', '', '| Case | Issue state | Research outcome | Review status |', '|---|---|---|---|']
    projections = []
    for case in data['cases']:
        history = [e for e in events if e['case_id'] == case['id']]
        outcomes = [e for e in history if e['kind'] == 'outcome']
        outcome = outcomes[-1] if outcomes else None
        needs_review = bool(outcome and history[-1]['id'] != outcome['id'])
        state = outcome['payload']['issue_state'] if outcome else 'unknown'
        status = outcome['payload']['status'] if outcome else 'not_adjudicated'
        review = 'new evidence/adjudication after outcome — review required' if needs_review else ('not imported' if not outcome else 'current as recorded')
        lines.append(f"| {literal(case['id'])} | {literal(state)} | {literal(status)} | {literal(review)} |")
        projections.append((case, history, outcome, needs_review))
    for case, history, outcome, needs_review in projections:
        lines += ['', f"## {literal(case['id'])}", '', f"Issue: {literal(case['issue_url'])}", '', f"Frozen at: {literal(case['frozen_at'])}", '']
        report = next(a for a in data['artifacts'] if a['id'] == case['report_artifact_id'])
        lines += [f"Frozen report: {literal(report['path'])}", '', f"SHA-256: `{report['sha256']}`", '', '### Dimension adjudication', '', '| Dimension | Frozen alignment / verdict | Source status | Source evidence basis | Record |', '|---|---|---|---|---|']
        for dimension in DIMENSIONS:
            revisions = [e for e in history if e['kind'] == 'adjudication' and e['payload']['dimension'] == dimension]
            current = revisions[-1] if revisions else None
            values = [dimension, current['payload'].get('frozen_alignment', current['payload']['verdict']) if current else 'not_assessed', current['payload'].get('source_assessment', {}).get('status', '—') if current else '—', current['payload'].get('source_assessment', {}).get('evidence_type', current['payload']['epistemic_status']) if current else 'No source adjudication imported', current['id'] if current else '—']
            lines.append('| ' + ' | '.join(literal(v) for v in values) + ' |')
        lines += ['', '### Evidence timeline', '']
        evidence = [e for e in history if e['kind'] == 'evidence']
        for scope in ('pre_freeze_context', 'post_freeze', 'research_snapshot'):
            lines += [f'#### {literal(scope)}', '']
            scoped = sorted((e for e in evidence if e['payload']['temporal_scope'] == scope), key=lambda e: (timestamp(e['payload']['occurred_at']), e['id']))
            if not scoped:
                lines += ['No evidence imported for this scope.', '']
            for event in scoped:
                p, src = event['payload'], event['payload']['source']
                lines += [f"- **{literal(p['occurred_at'])} — {literal(event['id'])}** ({literal(p.get('source_kind', p['kind']))}; {literal(p['epistemic_status'])})", f"  - Statement: {literal(p['statement'])}", f"  - Source: {literal(src['url'])}; locator: {literal(src['locator'])}; author: {literal(src['author'])} ({literal(src['author_role'])})", f"  - Excerpt ({literal(src.get('origin', 'direct'))}): {literal(src['excerpt'])}", f"  - Observed: {literal(p['observed_at'])}; recorded: {literal(event['recorded_at'])}; actor: {literal(event['actor'])}; artifact: {literal(src['artifact_id'] or 'external source only')}", '']
        snapshots = [e for e in evidence if e['payload']['kind'] == 'research_snapshot' and 'source_record' in e['payload']]
        for snapshot in snapshots:
            record = snapshot['payload']['source_record']
            alignment = record['frozen_report_adjudication']
            lines += ['### Source case research context', '', f"Study observation cutoff: {literal(snapshot['payload']['observed_at'])}", '', f"Title: {literal(record['title'])}", '', f"Freeze context: {literal(record['freeze_context'])}", '', f"Frozen-report summary: {literal(alignment['summary'])}", '', f"Supported extraction: {literal(alignment['supported_extraction'])}", '', f"Misses / noise: {literal(alignment['miss_or_noise'])}", '', f"Literal report signals: {literal(json.dumps(alignment['literal_report_signals'], ensure_ascii=False))}", '', f"Temporal conclusion: {literal(alignment['temporal_conclusion'])}", '', f"Assessment scope: {literal(alignment['scope'])}", '', f"Snapshot diff: {literal(json.dumps(record['snapshot_diff'], ensure_ascii=False))}", '', 'Linked PRs (source state at cutoff):', '']
            lines += [f"- {literal(json.dumps(pr, ensure_ascii=False))}" for pr in record['linked_prs']] or ['- None recorded.']
            lines += ['', 'Release / backport evidence:', '']
            lines += [f"- {literal(json.dumps(release, ensure_ascii=False))}" for release in record['release_and_backport']] or ['- None recorded.']
            lines += ['', f"Source: {literal(snapshot['payload']['source']['artifact_id'])} {literal(snapshot['payload']['source']['json_pointer'])}", '']
        lines += ['### Adjudication and outcome history (append order)', '']
        for event in history:
            if event['kind'] == 'evidence':
                continue
            p = event['payload']
            lines += [f"#### {literal(event['id'])} — {literal(event['kind'])}", '', f"Recorded: {literal(event['recorded_at'])}; actor: {literal(event['actor'])}; supersedes: {literal(p['supersedes'] or 'none')}", '']
            if event['kind'] == 'adjudication':
                lines += [f"Dimension: {literal(p['dimension'])}; verdict: {literal(p['verdict'])}; basis: {literal(p['epistemic_status'])}", '', f"Frozen claim / omission: {literal(p['frozen_claim'])}", '']
                if 'source_assessment' in p:
                    a = p['source_assessment']
                    lines += [f"Source dimension status: {literal(a['status'])}; source evidence basis: {literal(a['evidence_type'])}; frozen alignment: {literal(p['frozen_alignment'])}", '', f"Source evidence URLs: {literal(', '.join(a['evidence_urls']))}", '', f"Source pointer: {literal(p['source_pointer']['artifact_id'])} {literal(p['source_pointer']['pointer'])}", '']
            else:
                if 'source_disposition' in p:
                    lines += [f"Source disposition (verbatim): {literal(p['source_disposition'])}. Generic resolution remains unknown because the import does not infer a normalized resolution or finality.", '']
                lines += [f"Outcome: {literal(p['status'])}; issue: {literal(p['issue_state'])}; resolution: {literal(p['resolution'])}", '', f"Dimension records: {literal(', '.join(p['dimension_ids'].values()))}", '']
            lines += [f"Rationale: {literal(p['rationale'])}", '', f"Evidence: {literal(', '.join(p['evidence_ids']) or 'none')}", '', 'Unresolved questions:', '']
            lines += [f"- {literal(q)}" for q in p['unresolved_questions']] or ['- None recorded.']
            lines.append('')
        if not history:
            lines += ['Pending source import. No research verdicts or outcome have been inferred from the frozen report.', '']
        if needs_review:
            lines += ['**Review required:** records were appended after the latest outcome. That outcome is historical and must not be treated as a fresh final decision.', '']
    lines += ['## Source artifact registry', '', '| Artifact | Kind | Path | SHA-256 |', '|---|---|---|---|']
    for a in data['artifacts']:
        lines.append(f"| {literal(a['id'])} | {literal(a['kind'])} | {literal(a['path'])} | `{a['sha256']}` |")
    return '\n'.join(lines) + '\n'
