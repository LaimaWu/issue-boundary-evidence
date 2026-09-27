# Issue Boundary Evidence

- Issue: [scikit-learn/scikit-learn#34975](https://github.com/scikit-learn/scikit-learn/issues/34975) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/scikit-learn/scikit-learn/issues/34975)): BUG confusion_matrix_at_thresholds / roc_auc_score lose precision on plain numpy when y_score is float32 (regression from #34817)
- State at retrieval ([issue metadata](https://github.com/scikit-learn/scikit-learn/issues/34975)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- **strong_clue** — Investigate the external repository boundary with `ammar-iitm/scikit-learn`.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34975#issuecomment-5708730312), comment 3 — “ix conceptually. I've now actually implemented, tested, and pushed it: Branch: https://github.com/ammar-iitm/scikit-learn/tree/fix/confusion-matrix-at-thresholds-float32-precision Commit: https://github.com/ammar-iitm/scikit-learn/commit/6…”
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34975#issuecomment-5708730312), comment 3 — “/scikit-learn/tree/fix/confusion-matrix-at-thresholds-float32-precision Commit: https://github.com/ammar-iitm/scikit-learn/commit/63b0b6184 Fix: use `_max_precision_float_dtype(xp, device)` unconditionally for `output_dtype` in the unweig”
- **strong_clue** — Investigate the package/runtime boundary involving `numpy`.
  - Source: [issue_title](https://github.com/scikit-learn/scikit-learn/issues/34975), issue title — “BUG confusion_matrix_at_thresholds / roc_auc_score lose precision on plain numpy when y_score is float32 (regression from #34817)”
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34975#issuecomment-5708730312), comment 3 — “e`. Verified: - New non-regression test reproducing this exact scenario (plain numpy, 20M samples, float32 `y_score`) — confirmed it fails on the pre-fix code before restoring the fix.”
  - Source: [issue_body](https://github.com/scikit-learn/scikit-learn/issues/34975), issue body — “rve`, `det_curve`, `roc_auc_score`) silently loses integer precision on **plain numpy** — not just the restricted array-API devices that #34817 was fixing — whenever the caller's `y_sco”

## Version and regression clues

- **strong_clue** — Version or regression language: BUG confusion_matrix_at_thresholds / roc_auc_score lose precision on plain numpy when y_score is float32 (regression from #34817)
  - Source: [issue_title](https://github.com/scikit-learn/scikit-learn/issues/34975), issue title — “BUG confusion_matrix_at_thresholds / roc_auc_score lose precision on plain numpy when y_score is float32 (regression from #34817)”
- **strong_clue** — Version or regression language: This looks like a regression introduced this week by #34817 (merged 2026-08-31), which switched the unweighted cumulative-sum path to compute exact `int64` counts and then cast them to `output_dtype`…
  - Source: [issue_body](https://github.com/scikit-learn/scikit-learn/issues/34975), issue body — “This looks like a regression introduced this week by #34817 (merged 2026-08-31), which switched the unweighted cumulative-sum path to compute exact `int64` counts and then cast them to `output_dtype`: https://github.com/scikit-learn/scikit…”
- **strong_clue** — Version or regression language: Verified: - New non-regression test reproducing this exact scenario (plain numpy, 20M samples, float32 `y_score`) — confirmed it fails on the pre-fix code before restoring the fix.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34975#issuecomment-5708730312), comment 3 — “Verified: - New non-regression test reproducing this exact scenario (plain numpy, 20M samples, float32 `y_score`) — confirmed it fails on the pre-fix code before restoring the fix.”

## Related evidence

- **fact** — Explicit GitHub link to scikit-learn/scikit-learn (same repository): https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/metrics/_ranking.py#L1028-L1039.
  - Source: [issue_body](https://github.com/scikit-learn/scikit-learn/issues/34975), issue body — “sum path to compute exact `int64` counts and then cast them to `output_dtype`: https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/metrics/_ranking.py#L1028-L1039 ```python y_true_int = xp.astype(y_true, xp.int64) tps_int = xp.c…”
- **fact** — Explicit GitHub link to ammar-iitm/scikit-learn (external repository): https://github.com/ammar-iitm/scikit-learn/tree/fix/confusion-matrix-at-thresholds-float32-precision.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34975#issuecomment-5708730312), comment 3 — “ix conceptually. I've now actually implemented, tested, and pushed it: Branch: https://github.com/ammar-iitm/scikit-learn/tree/fix/confusion-matrix-at-thresholds-float32-precision Commit: https://github.com/ammar-iitm/scikit-learn/commit/6…”
- **fact** — Explicit GitHub link to ammar-iitm/scikit-learn (external repository): https://github.com/ammar-iitm/scikit-learn/commit/63b0b6184.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34975#issuecomment-5708730312), comment 3 — “/scikit-learn/tree/fix/confusion-matrix-at-thresholds-float32-precision Commit: https://github.com/ammar-iitm/scikit-learn/commit/63b0b6184 Fix: use `_max_precision_float_dtype(xp, device)` unconditionally for `output_dtype` in the unweig”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/scikit-learn/scikit-learn/issues/34975), issue body — “### Describe the bug `confusion_matrix_at_thresholds` (and everything built on it: `roc_curve`, `precision_recall_curve`, `det_curve`, `roc_auc_score`) silently loses integer precision on **plain numpy** — not just the restricted array-API…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
