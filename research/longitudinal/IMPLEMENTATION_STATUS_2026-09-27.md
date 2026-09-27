# IBE longitudinal layer implementation and completed source import

## Result

The independent layer, supplied study import, report generation and full local
verification are complete. The user supplied DOCX transfer versions of the
adjudication JSON and research report. Both original DOCX files are preserved
byte-for-byte; recovered JSON and Markdown are pinned separately with an OOXML
extraction audit. The original standalone JSON/Markdown byte identity is not
asserted, because those files were not supplied.

The data is the supplied first longitudinal observation, with source cutoff
**2026-09-26T23:41:39Z**. Import recorded at **2026-09-27T01:38:50Z**. No new GitHub
fetch, fresh upstream adjudication or engine tuning was performed during import.

## Repository and isolation

- Repository: `LaimaWu/issue-boundary-evidence`
- Worktree: `/Users/a1123/Documents/New project/ibe-longitudinal`
- Branch: `codex/longitudinal-adjudication-20260927`
- Base: `895b0fc`
- Changes remain local; no push, release or remote CI run.
- The existing engine and its command entry point are unchanged.
- No heuristic, scoring, classification, prompt or boundary extraction changes.

The optional `ibe_longitudinal` package and `ibe-longitudinal` command use the
`longitudinal` installation extra. The original engine retains its zero runtime
dependency contract and does not import this layer or jsonschema.

## Completed dataset

| Record type | Count |
|---|---:|
| Frozen cases | 10 |
| Pinned source artifacts | 27 |
| Evidence and study snapshots | 40 |
| Dimension adjudications | 50 |
| Outcomes | 10 |
| Total journal events | 100 |

Evidence records comprise 6 pre-freeze context records, 24 post-freeze records
and 10 research snapshots. These are journal records, not a count of distinct
upstream events: a PR transition may also appear in the source timeline.

All source cases, source timeline entries, linked PR/release records, snapshot
diffs, frozen-report signal/omission descriptions, dimension statuses, evidence
URLs and unresolved questions are preserved. All 50 source dimension assessment
texts also occur in the supplied research report. JSON Pointers connect imported
records to the pinned recovered source dataset.

### Research state

- Three issues closed; seven remained open at the source observation cutoff.
- All ten cases retain explicitly listed research questions, so all ten imported
  research outcomes remain `unresolved`.
- Known dispositions remain separate and verbatim: e.g. `closed_no_fix` and
  `main_merged_backport_unresolved`. They are not erased by the unresolved status.
- Generic resolution remains `unknown` because import does not infer a normalized
  resolution. The generated report shows the source disposition and its rationale.
- Source dimension status and frozen-report alignment are separate fields.
  `not_claimed`, `partial_pre_freeze`, `misleading_boundary` and other source labels
  are retained exactly. No single accuracy/pass-fail score is computed.

The wrapper `source_recorded` denotes lossless transport of a prior adjudication,
not support/refutation. The original source evidence type remains visible beside
it. Explicit later review can append a normalized adjudication and outcome.
An explicitly reviewed `not_claimed` dimension does not require inventing a claim
and does not itself block finality; unresolved facts and open questions do.

## Validation and sustainability

- Draft 2020-12 JSON Schema with strict event envelopes and typed source details.
- Per-case freeze boundaries, chronology, evidence provenance and reference checks.
- Study case membership, frozen ZIP/report hashes, paths and timestamps checked.
- Source record contents, JSON Pointers and observation cutoffs checked against
  pinned source bytes; modifications or invented source attributions rejected.
- Append-only revisions, latest-revision supersession, event hash chain and
  `validate --previous` historical-prefix protection.
- Lock, optimistic journal digest, validated atomic replacement and output
  overwrite prevention.
- Actual entry time is separate from source observation and upstream occurrence.
- Research snapshots are not represented as new upstream events. Edited comments
  retain their supplied edit timestamp; deleted text is never reconstructed.
- Source summaries are explicitly secondary provenance, not claimed raw GitHub
  quotes or fresh maintainer verification.
- Final outcomes require an explicit reviewed decision; closure does not auto-final.
- Later evidence marks the previous outcome as needing review; reopening and
  further adjudication can be appended without rewriting historical decisions.

Commands: `extract-docx`, `init-freeze`, `prepare-study`, `validate`, `append`,
`report`. The equivalent module entry point is `python -m ibe_longitudinal`.

## Frozen integrity

Original freeze ZIP SHA-256:

`f398678f387c4b37e4d08285a0637d70f653aa2aa536e032d58b06beb20ec070`

- All **98 original checksum entries** pass.
- Ten original reports and metadata files match their ZIP member bytes.
- All **28 existing engine/test/example/eval/action files** match base HEAD bytes.
- Both stored DOCX originals match the user attachments byte-for-byte.
- The pre-import journal is retained, and validation confirms its immutable header,
  case list, artifact prefix and event history are preserved.

## Tests and installation

Local Python **3.12.14**:

```text
PYTHONPATH=src .venv/bin/python -m unittest discover -s tests -v
Ran 115 tests
OK
```

Original suite: 70 tests. Added longitudinal contract/import tests: 45.

Coverage includes generic synthetic event contracts, finality/reopen behavior,
explicit absence of claims, invalid times and references, historical/file
mutation, atomic append failures, unsafe paths, report escaping and historical
views, source-study fidelity, original DOCX preservation, reproducible extraction,
source report/JSON agreement, wrong frozen identities, duplicate/backdated imports,
source-pointer/content mutation and exact replay of the reviewed batch.

Package build/install succeeded with schema included. Installed CLI validation
works outside the repository. CI retains Python 3.10–3.13 with the optional extra
installed; that remote matrix was not run locally.

## Deliverables and replay

Current machine-readable journal: `v0.1.0/journal.json`.
Generated human-readable report: `v0.1.0/longitudinal-report-2026-09-27.md`.
Source recovery and original documents: `v0.1.0/sources/study-2026-09-27/`.
Prior journal, artifact registry and exact append batch: `v0.1.0/history/`.
The old pending-import report is retained only as a historical artifact.

The delivery ZIP includes a root `journal.json`, all relative pinned artifact
paths, baseline/batch files, generated report, schema, guide and implementation
status. After extraction, `ibe-longitudinal validate journal.json --previous
history/journal-before-source-import.json` verifies the full source bundle.
The separate binary patch contains all repository changes against base `895b0fc`.

Keep a trusted Git baseline: hashes are integrity checks, not signatures or
protection against someone able to rewrite all files and history.
