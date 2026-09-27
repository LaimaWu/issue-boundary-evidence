# Issue Boundary Evidence

- Issue: [psf/requests#7610](https://github.com/psf/requests/issues/7610) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/psf/requests/issues/7610)): Drop the versionless `License ::` classifier now that `license` is a valid SPDX expression
- State at retrieval ([issue metadata](https://github.com/psf/requests/issues/7610)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- **strong_clue** — Investigate the package/runtime boundary involving `setuptools`.
  - Source: [issue_comment](https://github.com/psf/requests/issues/7610#issuecomment-5427534997), comment 3 — “The current setup is intended as there are still millions of daily downloads of setuptools that do not support what you're proposing. We will get to a point where we are able to remove this”

## Version and regression clues

- **strong_clue** — Version or regression language: Why make individual projects do work that doesn't help on older versions instead of fixing the broken tool?
  - Source: [issue_comment](https://github.com/psf/requests/issues/7610#issuecomment-5425702180), comment 1 — “Why make individual projects do work that doesn't help on older versions instead of fixing the broken tool?”

## Related evidence

- **fact** — Explicit GitHub link to psf/requests (same repository): https://github.com/psf/requests/blob/5460f467b02e49471c0fd6cfc9ca0adab6351f98/pyproject.toml#L9.
  - Source: [issue_comment](https://github.com/psf/requests/issues/7610#issuecomment-5425896809), comment 2 — “me). The problem is that the requests package has a single license defined here https://github.com/psf/requests/blob/5460f467b02e49471c0fd6cfc9ca0adab6351f98/pyproject.toml#L9, but reports multiple in its metadata. So having the license cl…”
- **fact** — Explicit GitHub link to psf/requests (same repository): https://github.com/psf/requests/pull/7012.
  - Source: [issue_comment](https://github.com/psf/requests/issues/7610#issuecomment-5427534997), comment 3 — “@btschwertfeger, we have discussed this [here](https://github.com/psf/requests/pull/7012#discussion_r2748329758) previously. The current setup is intended as there are still millions of da”
- **fact** — Explicit GitHub link to psf/requests (same repository): https://github.com/psf/requests/issues/7610.
  - Source: [issue_comment](https://github.com/psf/requests/issues/7610#issuecomment-5460764689), comment 6 — “work for others with no guarantee of the payoff for you As I already noted in https://github.com/psf/requests/issues/7610#issuecomment-5425896809 that the cyclonedx-bom example wasn't the best one to make this point. I sh”
- **fact** — Explicit GitHub link to psf/requests (same repository): https://github.com/psf/requests/compare/main...ShamikOfficial:fix/drop-license-classifier?quick_pull=1.
  - Source: [issue_comment](https://github.com/psf/requests/issues/7610#issuecomment-5562663490), comment 7 — “Opened a fix branch for this: https://github.com/psf/requests/compare/main...ShamikOfficial:fix/drop-license-classifier?quick_pull=1 Single-line removal of the obsolete `License :: OSI Approved :: Apache Software License` classifie”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/psf/requests/issues/7610), issue body — “> This issue is part of a larger batch of similar-scoped issues we distribute in the context of our internal vulnerability and dependency tracking activities. The batch covers multiple projects, this is only one of them. The goal is to ris…”

## Retrieved same-repository references

- **fact** — [psf/requests#7012: Migrate build system to PEP 517](https://github.com/psf/requests/pull/7012) (source kind: related issue metadata; structured location: title and state=closed)

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
