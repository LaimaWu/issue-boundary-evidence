# Issue Boundary Evidence

- Issue: [scikit-learn/scikit-learn#34977](https://github.com/scikit-learn/scikit-learn/issues/34977) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/scikit-learn/scikit-learn/issues/34977)): ⚠️ CI failed on Wheel builder (last failure: Sep 17, 2026) ⚠️
- State at retrieval ([issue metadata](https://github.com/scikit-learn/scikit-learn/issues/34977)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — ABI or wheel tag mentioned: cp314t.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5723076602), comment 2 — “[Build wheel for cp314t-win_arm64-](https://github.com/scikit-learn/scikit-learn/actions/runs/35179514326/job/105068469527#”

## Boundary candidates

- **strong_clue** — Investigate the wheel/ABI packaging boundary.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5723076602), comment 2 — “[Build wheel for cp314t-win_arm64-](https://github.com/scikit-learn/scikit-learn/actions/runs/35179514326/job/10”
- **strong_clue** — Investigate the package/runtime boundary involving `joblib`.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5723076602), comment 2 — “^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ..\venv-test\Lib\site-packages\joblib\parallel.py:2098: in __call__ return output if self.return_generator else list(output)”
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5723076602), comment 2 — “^^^^^^^^^^^^ ..\venv-test\Lib\site-packages\joblib\parallel.py:1763: in _get_outputs self._terminate_and_reset() ..\venv-test\Lib\site-pac”
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5723076602), comment 2 — “_outputs self._terminate_and_reset() ..\venv-test\Lib\site-packages\joblib\parallel.py:1430: in _terminate_and_reset self._backend.terminate() ..\venv-test\Lib\si”
- **strong_clue** — Investigate the package/runtime boundary involving `parallel`.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5723076602), comment 2 — “ble\_hist_gradient_boosting\binning.py:289: in fit non_cat_thresholds = Parallel(n_jobs=self.n_threads, backend="threading")( ..\venv-test\Lib\site-packages\sklearn\utils\paral”

## Version and regression clues

- No evidence extracted in this category.

## Related evidence

- **fact** — Explicit GitHub link to scikit-learn/scikit-learn (same repository): https://github.com/scikit-learn/scikit-learn/actions/runs/35179514326.
  - Source: [issue_body](https://github.com/scikit-learn/scikit-learn/issues/34977), issue body — “**CI failed on [Wheel builder](https://github.com/scikit-learn/scikit-learn/actions/runs/35179514326)** (Sep 17, 2026)”
- **fact** — Explicit GitHub link to scikit-learn/scikit-learn (same repository): https://github.com/scikit-learn/scikit-learn/actions/runs/35419499583.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5722880061), comment 1 — “## CI is no longer failing! ✅ [Successful run](https://github.com/scikit-learn/scikit-learn/actions/runs/35419499583) on Sep 19, 2026”
- **fact** — Explicit GitHub link to scikit-learn/scikit-learn (same repository): https://github.com/scikit-learn/scikit-learn/actions/runs/35179514326/job/105068469527#logs.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5723076602), comment 2 — “[Build wheel for cp314t-win_arm64-](https://github.com/scikit-learn/scikit-learn/actions/runs/35179514326/job/105068469527#logs) failed, because the `HistGradientBoostingRegressor` test [<code>test_X_val_in_fit</code>](https://”
- **fact** — Explicit GitHub link to scikit-learn/scikit-learn (same repository): https://github.com/scikit-learn/scikit-learn/blob/914346f574cddd99904513dec5a5d655b954dc91/sklearn/ensemble/_hist_gradient_boosting/tests/test_gradient_boosting.py#L1465.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5723076602), comment 2 — “cause the `HistGradientBoostingRegressor` test [<code>test_X_val_in_fit</code>](https://github.com/scikit-learn/scikit-learn/blob/914346f574cddd99904513dec5a5d655b954dc91/sklearn/ensemble/_hist_gradient_boosting/tests/test_gradient_boostin…”
- **fact** — Explicit GitHub link to scikit-learn/scikit-learn (same repository): https://github.com/scikit-learn/scikit-learn/actions/runs/35179514326/job/105423468025#logs.
  - Source: [issue_comment](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5723076602), comment 2 — “in the issue tracker led me to #30810. I re-ran the job, and it is now green: https://github.com/scikit-learn/scikit-learn/actions/runs/35179514326/job/105423468025#logs.”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/scikit-learn/scikit-learn/issues/34977), issue body — “**CI failed on [Wheel builder](https://github.com/scikit-learn/scikit-learn/actions/runs/35179514326)** (Sep 17, 2026)”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
