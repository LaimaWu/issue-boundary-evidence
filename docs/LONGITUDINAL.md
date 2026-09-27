# Longitudinal adjudication and outcome layer

## Scope and current import status

`ibe_longitudinal` is an independent research package. It does not import the
`issue_boundary_evidence` engine and the engine does not import it. The existing
CLI, heuristics, scoring, classification, prompts and boundary extraction are
unchanged. Install the optional `longitudinal` extra to use this layer; ordinary
IBE installs keep their original zero runtime dependency contract.

The checked-in `research/longitudinal/v0.1.0/journal.json` contains ten frozen
cases and the complete supplied September 27 study import: 40 evidence/snapshot
records, 50 dimension adjudications and 10 unresolved outcomes. Three issues were
closed and seven were open at the source cutoff, `2026-09-26T23:41:39Z`. All ten
cases retain explicit research questions. Import does not infer finality.

The user supplied two DOCX transfer documents. Their bytes are preserved in
`sources/study-2026-09-27/`. The JSON embedded in the first was recovered and
parsed; the second was converted to Markdown, retaining all paragraph/table
content. The extraction audit preserves body-block locations and source/derived
hashes. Original DOCX bytes are exact; original standalone JSON/Markdown byte
identity cannot be claimed without those files. All 50 dimension assessment
texts also occur in the recovered research report.

The `history/` directory retains the pre-import journal and pending report, source
artifact registry and exact append batch. The current report is
`longitudinal-report-2026-09-27.md`. No upstream fetch was performed during import;
this is the supplied historical study, not a new observation run.

## Data contract

The packaged [JSON Schema](../src/ibe_longitudinal/schema.json) uses Draft 2020-12
and schema version `1.0.0`. Unknown fields are rejected. This layer's schema
version is independent of the frozen engine release.

```
immutable frozen case + report digest
    └── evidence events (pre-freeze context / post-freeze)
          └── adjudication revisions for each dimension
                └── unresolved / final outcome revisions
```

A journal contains:

- `schema_version`, `dataset_id`, `frozen_release`: immutable identity.
- `artifacts`: an append-only registry of relative paths, SHA-256 digests and
  artifact kinds. Original study datasets/reports and evidence snapshots belong
  here with their exact bytes preserved. Paths cannot be absolute, traverse `..`,
  or escape the dataset directory through symlinks.
- `cases`: immutable issue URLs, per-case `frozen_at`, and references to the
  original frozen report and metadata. The time is the original metadata's
  `snapshot_completed_utc`, not a date guessed from filenames.
- `events`: an append-only array with unique IDs, case, researcher/actor,
  `recorded_at`, typed payload, preceding event hash and event hash.

### Evidence

Evidence records carry three separate timestamps/concepts:

- `occurred_at`: when the upstream event happened.
- `observed_at`: when the researcher observed it.
- `recorded_at`: when the record entered this research history.

All use explicit UTC timestamps ending in `Z`. Events satisfy
`occurred_at <= observed_at <= recorded_at`; recording order never goes
backwards. Post-freeze evidence must have occurred strictly after that case's
freeze. Evidence at or before the cutoff is `pre_freeze_context`. This allows
an explanation already present at freeze to be recorded as an omission in the
frozen report without misrepresenting it as later evidence.

`epistemic_status` explicitly distinguishes `observed_fact`,
`maintainer_confirmed_fact`, and `researcher_inference`. A source includes its URL,
locator (comment ID, JSON pointer, or report section), excerpt, author, author
role and optional registered artifact ID. Maintainer confirmation requires a
maintainer source; an adjudication labelled as maintainer-confirmed must cite
such evidence. The validator checks recorded provenance, not whether a person
really is a maintainer or whether a claim is true. Human review is still needed.

Kinds cover comments, maintainer comments, closure, reopen, PR, commit, release,
backport, explicit regression/version conclusions and other observations.
Corrections to evidence are new evidence records explaining the correction;
subsequent adjudications cite the appropriate record. Earlier evidence remains.

### Five dimensions

Every adjudication addresses exactly one of:

1. `phenomenon`
2. `cause`
3. `ownership`
4. `severity`
5. `fix_trajectory`

It records the frozen claim (or explicit absence), a human-authored rationale,
evidence references, epistemic status, remaining questions, and a verdict:
`supported`, `refuted`, `mixed`, `unresolved`, `not_assessed`, `not_claimed`, or `source_recorded`.
These are research judgments supplied by the author; the software never derives
them from keywords, case identity, issue state or engine output.

For source-study imports, `verdict: source_recorded` means lossless transport of
an existing adjudication, not a normalized success judgment. `source_assessment`
retains the exact original assessment, status, epistemic type and evidence URLs;
`frozen_alignment` separately retains labels such as `not_claimed`,
`partial_pre_freeze` or `misleading_boundary`. The comparison with the frozen
report remains researcher inference. Source-assigned maintainer confirmation in
a dimension is displayed as source attribution rather than silently converted
into a newly verified fact. The complete original case is pinned in a research
snapshot, including literal signals, omissions, snapshot diff and all PR/release
records. JSON Pointers are resolved and compared against the registered source.

An explicitly reviewed `not_claimed` verdict records absence of a frozen claim;
it is neither a failure nor a forced supported/refuted judgment and does not by
itself block finality. Open questions and unresolved facts still do.

The first revision has `supersedes: null`; later revisions must supersede the
latest record for the same case/dimension. References must point backward to
existing events in the same case. Supported/refuted/mixed judgments need evidence.

### Outcome

An outcome references the latest revision of all five dimensions and its
supporting evidence. `issue_state` is independent from research `status`:
a closed issue can have an unresolved research outcome. `resolution` records
unknown/fixed/wont_fix/duplicate/invalid/withdrawn/other separately.

`final` means that the researcher explicitly considers the five-dimensional
adjudication settled: evidence and a known resolution are required, no dimension
can remain `unresolved`/`not_assessed`, and no unresolved questions can remain.
An imported `source_recorded` dimension needs an explicit, evidence-backed
review revision before it can support finality. A maintainer's `wont_fix` or merged PR does not automatically satisfy this gate.
Use `unresolved` with the known issue state/resolution while research questions
remain. Reopening or later contradictory evidence can lead to an appended
unresolved outcome that supersedes the previous final outcome.

Source imports additionally preserve the exact `source_disposition`, including
`closed_no_fix` and `main_merged_backport_unresolved`. Generic `resolution` remains
`unknown` because no normalization is inferred; the report prominently displays
the original disposition and rationale. This does not erase the known no-fix or
main-branch-merge facts. Every source case in this import has unresolved questions,
so every imported outcome is `unresolved`. Sources with no open questions require
a separately authored outcome instead of automatic promotion to final.

The report marks an outcome as needing review if any further records for that
case were appended after it. It never silently promotes old finality to current
finality. Missing outcomes are `not_adjudicated`, not inferred unresolved verdicts.

## Commands

From the repository root:

```sh
python -m pip install '.[longitudinal]'
ibe-longitudinal validate research/longitudinal/v0.1.0/journal.json
ibe-longitudinal report research/longitudinal/v0.1.0/journal.json \
  --output longitudinal-report.md
```

The equivalent module entry point is `python -m ibe_longitudinal`; when working
without installation, prefix it with `PYTHONPATH=src`.

To initialize a **new** dataset from a freeze ZIP:

```sh
ibe-longitudinal init-freeze prospective-freeze-v0.1.0-2026-09-19.zip \
  research/longitudinal/new-dataset \
  --dataset-id another-prospective-study --release v0.1.0
```

This verifies every checksum and manifest coverage before publishing the new
directory. It preserves the original ZIP bytes, copies the exact report/metadata
bytes and initializes no judgments. An existing destination is never overwritten.

### Reproducible transfer-document ingestion

```sh
ibe-longitudinal extract-docx adjudication.docx research.docx new-source-directory
ibe-longitudinal prepare-study journal.json adjudication-recovered.json \
  --source-id registered-source-id --batch-id unique-study-import-id \
  --artifacts new-source-artifacts.json --output reviewed-batch.json
```

`extract-docx` refuses an existing destination or unsupported embedded/edited
content. It writes original DOCX copies, recovered JSON, recovered Markdown and
an extraction audit. `prepare-study` supports the supplied source schema `1.0`,
checks case membership, release tag, frozen ZIP/report hashes, report paths,
per-case freeze times and dimension completeness. It validates the proposed
batch against the real pinned source files without changing the journal.

New source artifacts must be present beneath the journal directory. The artifact
registry argument is a JSON array using the journal's artifact schema. An actual
registry and batch are preserved in `history/` as working examples.
`--recorded-at` defaults to current UTC; use an explicit value only to reproduce
a preserved batch. It cannot predate source observation. Reusing a batch ID is
rejected. A later import with a new batch ID supersedes the latest dimensions and
outcome while preserving all prior events.

Research snapshots use `temporal_scope: research_snapshot`, with occurrence set
to their observation cutoff. They describe knowledge at that time, not an upstream
event. Timeline events use the supplied event timestamps, including edit times.
PR/release transitions use their explicitly supplied opened/merged/closed/published
times; other fields describe state at cutoff. No missing event time or author
login is invented. Secondary excerpts are labelled `research_summary`, and
maintainer attribution is explicitly inherited from that study.

### Importing the source study and appending later work


1. Copy the **updated** study JSON and research Markdown into a new `sources/`
   path under the dataset directory without modifying their bytes. Record each
   as a `research_dataset` or `research_report` artifact with its SHA-256 digest.
2. Read the actual source schema before mapping it. Prepare a reviewed batch
   with exactly `artifacts` and `events` arrays. Preserve source wording and
   cite JSON pointers/report sections through evidence locators and artifact
   IDs. Do not translate unassessed claims into supported/refuted verdicts.
3. Use the source's actual observation times and individual upstream event
   times. At import, use the actual import time for `recorded_at`; do not backdate
   journal entry times to the original research observation time.
4. Add evidence first, then dimension adjudications, then outcomes. Use the same
   `recorded_at` across a batch if appropriate. Omit `hash` and `previous_hash`;
   the append command fills those in. An annotated synthetic batch is available
   as [append-example.json](../tests/fixtures/longitudinal/append-example.json).
   It targets a synthetic test dataset and is **not** a judgment for a real case.
5. Save a previous journal snapshot outside the artifact registry or use a
   version-control revision. Validate and copy the printed journal digest:

```sh
ibe-longitudinal validate research/longitudinal/v0.1.0/journal.json
ibe-longitudinal append research/longitudinal/v0.1.0/journal.json reviewed-batch.json \
  --expected-sha256 <sha256-from-validate>
ibe-longitudinal validate research/longitudinal/v0.1.0/journal.json \
  --previous previous-journal.json
ibe-longitudinal report research/longitudinal/v0.1.0/journal.json \
  --output longitudinal-report-next.md
```

`append` uses an exclusive lock, optimistic file digest, full validation, fsync
and atomic file replacement. Failed validation leaves the prior journal intact.
Readers see either the old or new complete JSON file. Artifact copies must
already exist before appending references to them; orphaned new copies from a
failed append are harmless and can be reviewed separately. A crash can leave a
`.lock` directory: verify no writer remains before removing that stale lock.

The lock coordinates this CLI's writers. Filesystem editing tools do not honor
it. Hashes detect accidental corruption; they are not signatures or protection
against an adversary who can rewrite every file. Use a trusted version-control
baseline and `validate --previous` to detect truncated or recomputed histories.

### Historical reports

```sh
ibe-longitudinal report research/longitudinal/v0.1.0/journal.json \
  --as-of 2026-09-27T12:00:00Z --output report-as-of.md
```

The cutoff filters by **recorded time**, so evidence discovered later cannot leak
into earlier knowledge views. The evidence timeline is sorted by occurrence
within pre/post-freeze sections. Artifact inventory always describes the current
journal's pinned source registry. The report includes all adjudication/outcome
revisions, rationale, unresolved questions and provenance. It computes no
accuracy or success rate from these ten cases. Report output uses exclusive file
creation to prevent overwriting an original source or frozen report.

## Verification

```sh
python -m pip install '.[longitudinal]'
PYTHONPATH=src python -m unittest discover -s tests -v
```

CI runs the entire suite on Python 3.10–3.13, with the optional extra installed.
Synthetic tests exercise the contract, temporal boundaries, wrong-case and forward
references, provenance, corrections, finality, reopening, historical integrity,
file tampering, atomic append failures, report escaping and CLI operations. The
real ten-case freeze is used only to verify unchanged bytes and the original
98 checksums, never to tune extraction behavior.
