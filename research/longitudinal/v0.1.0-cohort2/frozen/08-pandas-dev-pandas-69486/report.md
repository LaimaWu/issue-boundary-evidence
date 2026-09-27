# Issue Boundary Evidence

- Issue: [pandas-dev/pandas#69486](https://github.com/pandas-dev/pandas/issues/69486) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/pandas-dev/pandas/issues/69486)): BUG: `Series.str.zfill` with a negative width raises "Negative buffer resize" on pyarrow-backed strings (regression on main from #66339)
- State at retrieval ([issue metadata](https://github.com/pandas-dev/pandas/issues/69486)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Runtime mentioned: python                : 3.12.2.
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/69486), issue body — “-------------- commit : eeae81b6da3c2c2b19906815bcb84bd2b19aef9f python : 3.12.2 python-bits : 64 OS : Darwin OS-release : 25.5.0 Version”

## Boundary candidates

- **strong_clue** — Investigate the wheel/ABI packaging boundary.
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/69486), issue body — “ist() ['1', '2', '03'] ``` ### Installed Versions Reproduced with the nightly wheel (`pip install --pre --extra-index-url https://pypi.anaconda.org/scientific-python-nightly-wheels/si”

## Version and regression clues

- **strong_clue** — Version or regression language: BUG: `Series.str.zfill` with a negative width raises "Negative buffer resize" on pyarrow-backed strings (regression on main from #66339)
  - Source: [issue_title](https://github.com/pandas-dev/pandas/issues/69486), issue title — “BUG: `Series.str.zfill` with a negative width raises "Negative buffer resize" on pyarrow-backed strings (regression on main from #66339)”
- **fact** — Version mentioned: 3.0.6.
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/69486), issue body — “### Issue Description This is a regression on main only: the released pandas 3.0.6 returns `['1', '2', '03']` for the example above. Since #66339, `ArrowStringArray._str_zfill` pass”
- **fact** — Version mentioned: 3.12.2.
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/69486), issue body — “: eeae81b6da3c2c2b19906815bcb84bd2b19aef9f python : 3.12.2 python-bits : 64 OS : Darwin OS-release : 25.5.0 Version”
- **fact** — Version mentioned: 3.1.0.dev0.
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/69486), issue body — “: None LOCALE : C.UTF-8 pandas : 3.1.0.dev0+2037.geeae81b6da numpy : 2.6.0.dev0+git20260922.e29186c dateutil : 2.9”
- **strong_clue** — Version or regression language: ### Reproducible Example ### Issue Description This is a regression on main only: the released pandas 3.0.6 returns `['1', '2', '03']` for the example above.
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/69486), issue body — “### Reproducible Example ### Issue Description This is a regression on main only: the released pandas 3.0.6 returns `['1', '2', '03']` for the example above.”
- **fact** — Version mentioned: 3.0.
  - Source: [issue_comment](https://github.com/pandas-dev/pandas/issues/69486#issuecomment-5856987971), comment 1 — “@jbrockmendel @jorisvandenbossche - confirmed this is a regression on main vs 3.0.x; labeling as 3.1. Not a blocker for 3.1 RC in my opinion.”
- **fact** — Version mentioned: 3.1.
  - Source: [issue_comment](https://github.com/pandas-dev/pandas/issues/69486#issuecomment-5856987971), comment 1 — “risvandenbossche - confirmed this is a regression on main vs 3.0.x; labeling as 3.1. Not a blocker for 3.1 RC in my opinion.”
  - Source: [issue_comment](https://github.com/pandas-dev/pandas/issues/69486#issuecomment-5856987971), comment 1 — “irmed this is a regression on main vs 3.0.x; labeling as 3.1. Not a blocker for 3.1 RC in my opinion.”
- **strong_clue** — Version or regression language: @jbrockmendel @jorisvandenbossche - confirmed this is a regression on main vs 3.0.x; labeling as 3.1.
  - Source: [issue_comment](https://github.com/pandas-dev/pandas/issues/69486#issuecomment-5856987971), comment 1 — “@jbrockmendel @jorisvandenbossche - confirmed this is a regression on main vs 3.0.x; labeling as 3.1.”

## Related evidence

- No evidence extracted in this category.

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/pandas-dev/pandas/issues/69486), issue body — “### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confir…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
