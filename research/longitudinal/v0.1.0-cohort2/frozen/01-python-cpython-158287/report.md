# Issue Boundary Evidence

- Issue: [python/cpython#158287](https://github.com/python/cpython/issues/158287) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/python/cpython/issues/158287)): asyncio.subprocess blocked event loop unexpectedly on MacOS
- State at retrieval ([issue metadata](https://github.com/python/cpython/issues/158287)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Platform mentioned: MacOS.
  - Source: [issue_title](https://github.com/python/cpython/issues/158287), issue title — “asyncio.subprocess blocked event loop unexpectedly on MacOS”
  - Source: [issue_body](https://github.com/python/cpython/issues/158287), issue body — “# Bug report ### Bug description: After upgrading to 3.14.7 & macOS 27, this bug has happened. When pausing the subprocess created by `asyncio.create_subprocess_exec`”
  - Source: [issue_body](https://github.com/python/cpython/issues/158287), issue body — “ed by `asyncio.create_subprocess_exec`, it will blocked the whole event loop on MacOS. Here is a minimal test code: ```python import asyncio import psutil async def main(): proc =”
- **fact** — Platform mentioned: Windows.
  - Source: [issue_body](https://github.com/python/cpython/issues/158287), issue body — “il` because the same result was got with `kill -STOP xxxxx`. This runs well on Windows, but not on MacOS. This didn't happen on the previous version of 3.14. ### CPython versions test”
  - Source: [issue_body](https://github.com/python/cpython/issues/158287), issue body — “### CPython versions tested on: 3.14 ### Operating systems tested on: macOS, Windows”
- **fact** — Runtime mentioned: Python 3.14.
  - Source: [issue_comment](https://github.com/python/cpython/issues/158287#issuecomment-5856940502), comment 2 — “@starstreammm Do you mean that on Python 3.14.**6** it works well? or is it on **3.13** that it works well? (this is to confirm whether it's a re”
  - Source: [issue_comment](https://github.com/python/cpython/issues/158287#issuecomment-5857035743), comment 3 — “> [@starstreammm](https://github.com/starstreammm) Do you mean that on Python 3.14.**6** it works well? or is it on **3.13** that it works well? (this is to confirm whether it's a re”

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **fact** — Version mentioned: 3.14.7.
  - Source: [issue_body](https://github.com/python/cpython/issues/158287), issue body — “# Bug report ### Bug description: After upgrading to 3.14.7 & macOS 27, this bug has happened. When pausing the subprocess created by `asyncio.create_subproce”
- **fact** — Version mentioned: 3.14.
  - Source: [issue_body](https://github.com/python/cpython/issues/158287), issue body — “ll on Windows, but not on MacOS. This didn't happen on the previous version of 3.14. ### CPython versions tested on: 3.14 ### Operating systems tested on: macOS, Windows”
  - Source: [issue_comment](https://github.com/python/cpython/issues/158287#issuecomment-5856940502), comment 2 — “@starstreammm Do you mean that on Python 3.14.**6** it works well? or is it on **3.13** that it works well? (this is to confirm whether it's a re”
  - Source: [issue_comment](https://github.com/python/cpython/issues/158287#issuecomment-5857035743), comment 3 — “> [@starstreammm](https://github.com/starstreammm) Do you mean that on Python 3.14.**6** it works well? or is it on **3.13** that it works well? (this is to confirm whether it's a re”
- **strong_clue** — Version or regression language: # Bug report ### Bug description: After upgrading to 3.14.7 & macOS 27, this bug has happened.
  - Source: [issue_body](https://github.com/python/cpython/issues/158287), issue body — “# Bug report ### Bug description: After upgrading to 3.14.7 & macOS 27, this bug has happened.”
- **strong_clue** — Version or regression language: This didn't happen on the previous version of 3.14.
  - Source: [issue_body](https://github.com/python/cpython/issues/158287), issue body — “This didn't happen on the previous version of 3.14.”
- **fact** — Version mentioned: 3.13.
  - Source: [issue_comment](https://github.com/python/cpython/issues/158287#issuecomment-5856940502), comment 2 — “starstreammm Do you mean that on Python 3.14.**6** it works well? or is it on **3.13** that it works well? (this is to confirm whether it's a release blocker or not)”
  - Source: [issue_comment](https://github.com/python/cpython/issues/158287#issuecomment-5857035743), comment 3 — “tarstreammm) Do you mean that on Python 3.14.**6** it works well? or is it on **3.13** that it works well? (this is to confirm whether it's a release blocker or not) I updated my Pyth”
- **strong_clue** — Version or regression language: At least, it's a regression AFAICT.
  - Source: [issue_comment](https://github.com/python/cpython/issues/158287#issuecomment-5857160247), comment 4 — “At least, it's a regression AFAICT.”

## Related evidence

- No evidence extracted in this category.

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/python/cpython/issues/158287), issue body — “# Bug report ### Bug description: After upgrading to 3.14.7 & macOS 27, this bug has happened. When pausing the subprocess created by `asyncio.create_subprocess_exec`, it will blocked the whole event loop on MacOS. Here is a minimal test c…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
