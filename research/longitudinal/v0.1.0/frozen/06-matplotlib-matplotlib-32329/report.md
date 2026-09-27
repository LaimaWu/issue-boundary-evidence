# Issue Boundary Evidence

- Issue: [matplotlib/matplotlib#32329](https://github.com/matplotlib/matplotlib/issues/32329) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/matplotlib/matplotlib/issues/32329)): Behavior of `contains()` inconsistent with fill in overlapping paths
- State at retrieval ([issue metadata](https://github.com/matplotlib/matplotlib/issues/32329)): open
- Method: deterministic, read-only extraction from the issue and its comments

> No major boundary evidence found.

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- No evidence extracted in this category.

## Related evidence

- **fact** — Explicit GitHub link to matplotlib/matplotlib (same repository): https://github.com/matplotlib/matplotlib/blob/284213d3701a1112521fac0ef4891e3443c5880d/src/_path.h#L108.
  - Source: [issue_body](https://github.com/matplotlib/matplotlib/issues/32329), issue body — “fully consistent with either fill rule. The current logic (in [this function](https://github.com/matplotlib/matplotlib/blob/284213d3701a1112521fac0ef4891e3443c5880d/src/_path.h#L108)) is essentially (and possibly unintentionally) consisten…”
- **fact** — Explicit GitHub link to matplotlib/matplotlib (same repository): https://github.com/matplotlib/matplotlib/issues/32253.
  - Source: [issue_body](https://github.com/matplotlib/matplotlib/issues/32329), issue body — “tains()` should be deferred to a future PR. _Originally posted by @ayshih in https://github.com/matplotlib/matplotlib/issues/32253#issuecomment-5591178865_”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/matplotlib/matplotlib/issues/32329), issue body — “> How do the two cases behave with `contains()` and mouse checking on the various artists? I've investigated this, and amusingly enough, `contains()` is not fully consistent with either fill rule. The current logic (in [this function](http…”

## Retrieved same-repository references

- **fact** — [matplotlib/matplotlib#32253: Enable choosing the even-odd rule for filling shapes](https://github.com/matplotlib/matplotlib/pull/32253) (source kind: related issue metadata; structured location: title and state=closed)

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
