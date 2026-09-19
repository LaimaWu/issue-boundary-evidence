# Issue Boundary Evidence

- Issue: [pandas-dev/pandas#58927](https://github.com/pandas-dev/pandas/issues/58927) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/pandas-dev/pandas/issues/58927)): BUG: iterrows() on an awkward array with equal-length rows results in a ValueError
- State at retrieval ([issue metadata](https://github.com/pandas-dev/pandas/issues/58927)): closed
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Runtime mentioned: python                : 3.11.0.
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/58927), issue body — “------------ commit : d9cdd2ee5a58015ef6f4d15c7226110c9aab8140 python : 3.11.0.final.0 python-bits : 64 OS : Linux OS-release : 5.15.14”
- **fact** — Platform mentioned: Linux.
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/58927), issue body — “: 3.11.0.final.0 python-bits : 64 OS : Linux OS-release : 5.15.146.1-microsoft-standard-WSL2 Version : #1 SMP Thu Jan”

## Boundary candidates

- **strong_clue** — Investigate the external repository boundary with `intake/awkward-pandas`.
  - Source: [issue_comment](https://github.com/pandas-dev/pandas/issues/58927#issuecomment-2163519805), comment 3 — “loper of `awkward_pandas` replied to [the issue I posted on their page as well](https://github.com/intake/awkward-pandas/issues/55#issuecomment-2161580075). It seems this problem will be solved soon in a future release.”
- **strong_clue** — Investigate the package/runtime boundary involving `awkward_pandas`.
  - Source: [issue_comment](https://github.com/pandas-dev/pandas/issues/58927#issuecomment-2163519805), comment 3 — “loper of `awkward_pandas` replied to [the issue I posted on their page as well](https://github.com/intake/awkward-pandas/issues/55#issuecomment-2161580075). It seems this problem will be solved soon in a future release.”
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/58927), issue body — “andas. ### Reproducible Example ```python import awkward as ak import awkward_pandas as akpd import pandas as pd # numbers = [[1, 2, 3], [4, 5], [6]] numbers = [[1, 2, 3], [4, 5,”
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/58927), issue body — “e first. Please let me know if this is actually an issue with the `awkward` or `awkward_pandas` module. --- When calling `iterrows()` on a DataFrame which contains an awkward array as a co”

## Version and regression clues

- **fact** — Version mentioned: 3.11.0.
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/58927), issue body — “: d9cdd2ee5a58015ef6f4d15c7226110c9aab8140 python : 3.11.0.final.0 python-bits : 64 OS : Linux OS-release : 5.15.14”
- **fact** — Version mentioned: 2.2.2.
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/58927), issue body — “: C.UTF-8 LOCALE : en_US.UTF-8 pandas : 2.2.2 numpy : 1.26.4 pytz : 2024.1 dateutil : 2.9.0.post”

## Related evidence

- **fact** — Explicit GitHub link to intake/awkward-pandas (external repository): https://github.com/intake/awkward-pandas/issues/55.
  - Source: [issue_comment](https://github.com/pandas-dev/pandas/issues/58927#issuecomment-2163519805), comment 3 — “loper of `awkward_pandas` replied to [the issue I posted on their page as well](https://github.com/intake/awkward-pandas/issues/55#issuecomment-2161580075). It seems this problem will be solved soon in a future release.”

## Evidence gaps

- **fact** — Responsibility or reproduction uncertainty is explicit: ### Reproducible Example ### Issue Description I'm not really knowledgeable on the internals of Pandas and array extensions, so I'm not sure if this is the right place to report the bug, but since it…
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/58927), issue body — “### Reproducible Example ### Issue Description I'm not really knowledgeable on the internals of Pandas and array extensions, so I'm not sure if this is the right place to report the bug, but since it occurred in the Pandas core code, I cam…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
