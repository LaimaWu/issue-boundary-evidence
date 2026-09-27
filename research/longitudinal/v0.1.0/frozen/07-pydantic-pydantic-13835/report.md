# Issue Boundary Evidence

- Issue: [pydantic/pydantic#13835](https://github.com/pydantic/pydantic/issues/13835) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/pydantic/pydantic/issues/13835)): pydantic.v1._hypothesis_plugin cannot be imported under pydantic 2
- State at retrieval ([issue metadata](https://github.com/pydantic/pydantic/issues/13835)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Runtime mentioned: python version: 3.13.5.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13835), issue body — “eError ``` ### Python, Pydantic & OS Version ```Text pydantic version: 2.13.5 python version: 3.13.5 platform: Windows 11 hypothesis: installed ``` --- Found while auditing installed code with a ver”
- **fact** — Platform mentioned: Windows 11.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13835), issue body — “& OS Version ```Text pydantic version: 2.13.5 python version: 3.13.5 platform: Windows 11 hypothesis: installed ``` --- Found while auditing installed code with a verification tool I am b”
- **fact** — Runtime mentioned: Python 3.13.
  - Source: [issue_comment](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5738069213), comment 1 — “the clear report. I reproduced the failure on `main` with Pydantic 2.14.0b2 and Python 3.13. Your proposed fix works, but one line is enough: -import pydantic -import pydantic.color”
- **fact** — Runtime mentioned: Python 3.13.5.
  - Source: [issue_comment](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5739788496), comment 3 — “the import block, each imported in a fresh interpreter under pydantic 2.13.5 / Python 3.13.5, then asked Hypothesis for a value of a v1 type: \| import block \| result \| \| --- \| --- \| \| as ship”

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **fact** — Version mentioned: 2.13.5.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13835), issue body — “ched by importing it directly — and that always fails. **Reproduce** (pydantic 2.13.5, hypothesis installed): ``` >>> import pydantic.v1._hypothesis_plugin AttributeError: module 'pyda”
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13835), issue body — “v1.types as _types # noqa: F401 ``` Checked with `main`'s file under pydantic 2.13.5: the current module fails to import; the fixed module imports, and Hypothesis then draws valid valu”
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13835), issue body — “ttributeError ``` ### Python, Pydantic & OS Version ```Text pydantic version: 2.13.5 python version: 3.13.5 platform: Windows 11 hypothesis: installed ``` --- Found while auditing in”
- **fact** — Version mentioned: 3.13.5.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13835), issue body — “Python, Pydantic & OS Version ```Text pydantic version: 2.13.5 python version: 3.13.5 platform: Windows 11 hypothesis: installed ``` --- Found while auditing installed code with a ver”
  - Source: [issue_comment](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5739788496), comment 3 — “port block, each imported in a fresh interpreter under pydantic 2.13.5 / Python 3.13.5, then asked Hypothesis for a value of a v1 type: \| import block \| result \| \| --- \| --- \| \| as ship”
- **fact** — Version mentioned: 2.14.0b2.
  - Source: [issue_comment](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5738069213), comment 1 — “Thanks for the clear report. I reproduced the failure on `main` with Pydantic 2.14.0b2 and Python 3.13. Your proposed fix works, but one line is enough: -import pydantic -impor”
- **fact** — Version mentioned: 3.13.
  - Source: [issue_comment](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5738069213), comment 1 — “ar report. I reproduced the failure on `main` with Pydantic 2.14.0b2 and Python 3.13. Your proposed fix works, but one line is enough: -import pydantic -import pydantic.color”
- **strong_clue** — Version or regression language: I opened #13836 with a regression test.
  - Source: [issue_comment](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5738069213), comment 1 — “I opened #13836 with a regression test.”
- **strong_clue** — Version or regression language: The fix and regression test are ready in that PR.
  - Source: [issue_comment](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5738082207), comment 2 — “The fix and regression test are ready in that PR.”

## Related evidence

- No evidence extracted in this category.

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13835), issue body — “### Initial Checks - [x] I confirm that I'm using Pydantic V2 ### Description `pydantic/v1/_hypothesis_plugin.py` cannot be imported under pydantic 2: it imports the **v2** modules and then reads v1-only names off them at import time. The…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
