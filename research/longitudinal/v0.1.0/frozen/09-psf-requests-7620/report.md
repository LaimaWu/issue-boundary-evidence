# Issue Boundary Evidence

- Issue: [psf/requests#7620](https://github.com/psf/requests/issues/7620) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/psf/requests/issues/7620)): PR 5410 got merged but is not in fact merged
- State at retrieval ([issue metadata](https://github.com/psf/requests/issues/7620)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **fact** — Historical commit referenced: [f1a94608814a6bdc484233f48b3051dfcb13aa36](https://github.com/psf/requests/commit/f1a94608814a6bdc484233f48b3051dfcb13aa36).
  - Source: [issue_body](https://github.com/psf/requests/issues/7620), issue body — “requests/pull/5410, which says it was merged in https://github.com/psf/requests/commit/f1a94608814a6bdc484233f48b3051dfcb13aa36 but that is not part of main any more. Was there a rebase of the main branch that happened and era”
- **strong_clue** — Version or regression language: We can look at removing it for the next release.
  - Source: [issue_comment](https://github.com/psf/requests/issues/7620#issuecomment-5626752874), comment 1 — “We can look at removing it for the next release.”

## Related evidence

- **fact** — Explicit GitHub link to psf/requests (same repository): https://github.com/psf/requests/pull/5410.
  - Source: [issue_body](https://github.com/psf/requests/issues/7620), issue body — “Hello, I was just looking at https://github.com/psf/requests/pull/5410, which says it was merged in https://github.com/psf/requests/commit/f1a94608814a6bdc484233f48b3051d”
- **fact** — Explicit GitHub link to psf/requests (same repository): https://github.com/psf/requests/commit/f1a94608814a6bdc484233f48b3051dfcb13aa36.
  - Source: [issue_body](https://github.com/psf/requests/issues/7620), issue body — “oking at https://github.com/psf/requests/pull/5410, which says it was merged in https://github.com/psf/requests/commit/f1a94608814a6bdc484233f48b3051dfcb13aa36 but that is not part of main any more. Was there a rebase of the main branch th…”
- **fact** — Explicit GitHub link to psf/requests (same repository): https://github.com/psf/requests/compare/main...hroncok:requests:pr5410?expand=1.
  - Source: [issue_comment](https://github.com/psf/requests/issues/7620#issuecomment-5713205873), comment 5 — “ack, thanks for the explanation. I have https://github.com/psf/requests/compare/main...hroncok:requests:pr5410?expand=1, but I cannot open it because PRs are restricted.”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/psf/requests/issues/7620), issue body — “Hello, I was just looking at https://github.com/psf/requests/pull/5410, which says it was merged in https://github.com/psf/requests/commit/f1a94608814a6bdc484233f48b3051dfcb13aa36 but that is not part of main any more. Was there a rebase o…”

## Retrieved same-repository references

- **fact** — [psf/requests#5410: Remove shebang from nonexecutable script](https://github.com/psf/requests/pull/5410) (source kind: related issue metadata; structured location: title and state=closed)

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
