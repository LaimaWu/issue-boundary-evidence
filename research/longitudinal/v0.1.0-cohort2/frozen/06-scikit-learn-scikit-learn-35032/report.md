# Issue Boundary Evidence

- Issue: [scikit-learn/scikit-learn#35032](https://github.com/scikit-learn/scikit-learn/issues/35032) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/scikit-learn/scikit-learn/issues/35032)): BUG: Explicit validation data does not enable HistGradientBoosting automatic early stopping
- State at retrieval ([issue metadata](https://github.com/scikit-learn/scikit-learn/issues/35032)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **fact** — Version mentioned: 1.9.0.
  - Source: [issue_body](https://github.com/scikit-learn/scikit-learn/issues/35032), issue body — “minate before `max_iter`. ### Actual Results The reported run on scikit-learn 1.9.0 produced: ```text 1.9.0 HistGradientBoostingRegressor auto False 0 HistGradientBoostingRegressor T”
- **strong_clue** — Version or regression language: A workaround is to set `early_stopping=True` explicitly when providing validation arrays.
  - Source: [issue_body](https://github.com/scikit-learn/scikit-learn/issues/35032), issue body — “A workaround is to set `early_stopping=True` explicitly when providing validation arrays.”
- **strong_clue** — Version or regression language: A regression test should cover both estimator classes with a small training set, explicit validation arrays, and `early_stopping="auto"`, and check: Keep `early_stopping=True` as a passing control.
  - Source: [issue_body](https://github.com/scikit-learn/scikit-learn/issues/35032), issue body — “A regression test should cover both estimator classes with a small training set, explicit validation arrays, and `early_stopping="auto"`, and check: Keep `early_stopping=True` as a passing control.”
- **strong_clue** — Version or regression language: I'll take a look at this and submit a PR with the fix and regression tests.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/35032#issuecomment-5845320437), comment 1 — “I'll take a look at this and submit a PR with the fix and regression tests.”
- **strong_clue** — Version or regression language: I have a tested fix on my branch, including a regression test.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/35032#issuecomment-5845559272), comment 2 — “I have a tested fix on my branch, including a regression test.”

## Related evidence

- **fact** — Explicit GitHub link to scikit-learn/scikit-learn (same repository): https://github.com/scikit-learn/scikit-learn/blob/1.9.0/sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py.
  - Source: [issue_body](https://github.com/scikit-learn/scikit-learn/issues/35032), issue body — “## Interest in fixing the bug In [`BaseHistGradientBoosting.fit` at tag 1.9.0](https://github.com/scikit-learn/scikit-learn/blob/1.9.0/sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py), the automatic-mode decision only checks…”
- **fact** — Explicit GitHub link to scikit-learn/scikit-learn (same repository): https://github.com/scikit-learn/scikit-learn/issues/18748.
  - Source: [issue_body](https://github.com/scikit-learn/scikit-learn/issues/35032), issue body — “, and preserve the existing validation-argument errors. Related work: [#18748](https://github.com/scikit-learn/scikit-learn/issues/18748) requested custom validation-set support, and [#27124](https://github.com/scikit-learn/scikit-learn”
- **fact** — Explicit GitHub link to scikit-learn/scikit-learn (same repository): https://github.com/scikit-learn/scikit-learn/pull/27124.
  - Source: [issue_body](https://github.com/scikit-learn/scikit-learn/issues/35032), issue body — “cikit-learn/issues/18748) requested custom validation-set support, and [#27124](https://github.com/scikit-learn/scikit-learn/pull/27124) introduced the explicit validation arguments. These references do not establish that no duplicate”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/scikit-learn/scikit-learn/issues/35032), issue body — “> [!WARNING] > This issue is not yet ready for a PR. If you are interested in contributing to scikit-learn, please have a look at our [contributing guidelines](https://scikit-learn.org/dev/developers/contributing.html), and in particular t…”

## Retrieved same-repository references

- **fact** — [scikit-learn/scikit-learn#18748: Support early_stopping with custom validation_set](https://github.com/scikit-learn/scikit-learn/issues/18748) (source kind: related issue metadata; structured location: title and state=open)
- **fact** — [scikit-learn/scikit-learn#27124: ENH add X_val and y_val to HGBT.fit](https://github.com/scikit-learn/scikit-learn/pull/27124) (source kind: related issue metadata; structured location: title and state=closed)

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
