# Issue Boundary Evidence

- Issue: [psf/requests#7630](https://github.com/psf/requests/issues/7630) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/psf/requests/issues/7630)): Incorrect type annotation for iter_lines
- State at retrieval ([issue metadata](https://github.com/psf/requests/issues/7630)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- **strong_clue** — Investigate the external repository boundary with `agustin18/requests`.
  - Source: [issue_comment](https://github.com/psf/requests/issues/7630#issuecomment-5834878579), comment 4 — “rk here: **Branch:** [`agustin18:requests:fix/iter-lines-chunk-size-type-7630`](https://github.com/agustin18/requests/tree/fix/iter-lines-chunk-size-type-7630) **Compare Diff:** [`psf/requests/compare/main...agustin18:requests:fix/iter-lin…”

## Version and regression clues

- **strong_clue** — Version or regression language: I'll submit a focused typing fix with regression coverage shortly.
  - Source: [issue_comment](https://github.com/psf/requests/issues/7630#issuecomment-5819550674), comment 1 — “I'll submit a focused typing fix with regression coverage shortly.”
- **strong_clue** — Version or regression language: Added parameterized regression tests in `tests/test_requests.py` covering `chunk_size=None` and `chunk_size=512` with both `decode_unicode=False` and `True`.
  - Source: [issue_comment](https://github.com/psf/requests/issues/7630#issuecomment-5834878579), comment 4 — “Added parameterized regression tests in `tests/test_requests.py` covering `chunk_size=None` and `chunk_size=512` with both `decode_unicode=False` and `True`.”

## Related evidence

- **fact** — Explicit GitHub link to psf/requests (same repository): https://github.com/psf/requests/compare/main...grantisu:requests:gmathews/tiny-type-fix.
  - Source: [issue_body](https://github.com/psf/requests/issues/7630), issue body — “causing valid code to fail type checks. This seems pretty trivial to fix (e.g. https://github.com/psf/requests/compare/main...grantisu:requests:gmathews/tiny-type-fix), but I'm not able to open a PR since I'm not a collaborator on the repo.”
- **fact** — Explicit GitHub link to agustin18/requests (external repository): https://github.com/agustin18/requests/tree/fix/iter-lines-chunk-size-type-7630.
  - Source: [issue_comment](https://github.com/psf/requests/issues/7630#issuecomment-5834878579), comment 4 — “rk here: **Branch:** [`agustin18:requests:fix/iter-lines-chunk-size-type-7630`](https://github.com/agustin18/requests/tree/fix/iter-lines-chunk-size-type-7630) **Compare Diff:** [`psf/requests/compare/main...agustin18:requests:fix/iter-lin…”
- **fact** — Explicit GitHub link to psf/requests (same repository): https://github.com/psf/requests/compare/main...agustin18:requests:fix/iter-lines-chunk-size-type-7630.
  - Source: [issue_comment](https://github.com/psf/requests/issues/7630#issuecomment-5834878579), comment 4 — “equests/compare/main...agustin18:requests:fix/iter-lines-chunk-size-type-7630`](https://github.com/psf/requests/compare/main...agustin18:requests:fix/iter-lines-chunk-size-type-7630) ### Changes 1. Updated `chunk_size: int \| None = ITER_CH…”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/psf/requests/issues/7630), issue body — “The type annotation for `Response.iter_lines` misses that `chunk_size` can be `None`, causing valid code to fail type checks. This seems pretty trivial to fix (e.g. https://github.com/psf/requests/compare/main...grantisu:requests:gmathews/…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
