# v0.1.1 — Precision and provenance fixes

## Fixed

- Preserve the explicit external repository owner and path for commit provenance.
- Reduce strong boundary clues from incidental imports, environment details, and test-command context.
- Suppress generic “regression test” prose from regression-history evidence.

## Validation

- Failures identified in v0.1.0 were converted into generic regression tests.
- The candidate was evaluated against a fresh 12-case holdout using authenticated GitHub snapshots and offline replay.
- The offline replay validated extraction and report behavior; it was not an end-to-end test of candidate HTTP retrieval.

## Known limitations

- Rule-like names can still resemble packages and be over-promoted.
- Issue-template or checklist wording can still trigger history clues.
- Explicit upstream responsibility can sometimes remain only in related evidence instead of boundary candidates.
- Incidental service or packaging context can still be over-promoted.
