# Issue Boundary Evidence

- Issue: [astral-sh/uv#21720](https://github.com/astral-sh/uv/issues/21720) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/astral-sh/uv/issues/21720)): `uv check` and `ty check` report different errors
- State at retrieval ([issue metadata](https://github.com/astral-sh/uv/issues/21720)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Runtime mentioned: Python version

3.14.0.
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/21720), issue body — “x ### Version uv 0.12.15 (d35f1f270 2026-09-15 x86_64-unknown-linux-gnu) ### Python version 3.14.0”
- **fact** — Platform mentioned: Linux.
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/21720), issue body — “make a difference. uv version 0.12.15 ty version 0.0.81 ### Platform Arch - Linux 6.18.51-1-lts x86_64 GNU/Linux ### Version uv 0.12.15 (d35f1f270 2026-09-15 x86_64-unknown-linux-”
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/21720), issue body — “0.12.15 ty version 0.0.81 ### Platform Arch - Linux 6.18.51-1-lts x86_64 GNU/Linux ### Version uv 0.12.15 (d35f1f270 2026-09-15 x86_64-unknown-linux-gnu) ### Python version 3.14.”
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/21720), issue body — “x86_64 GNU/Linux ### Version uv 0.12.15 (d35f1f270 2026-09-15 x86_64-unknown-linux-gnu) ### Python version 3.14.0”

## Boundary candidates

- **strong_clue** — Investigate the package/runtime boundary involving `demo`.
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/21720), issue body — “y does? As a minimal example, with `pyproject.toml` ```toml [project] name = "demo" version = "0.1.0" requires-python = ">=3.12" ``` and `demo.py` in the same directory (I know the”

## Version and regression clues

- **fact** — Version mentioned: 3.12.
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/21720), issue body — “t.toml` ```toml [project] name = "demo" version = "0.1.0" requires-python = ">=3.12" ``` and `demo.py` in the same directory (I know the code itself is questionable - it's minified f”
- **fact** — Version mentioned: 0.12.15.
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/21720), issue body — “`uv check` with the same version as ty, doesn't make a difference. uv version 0.12.15 ty version 0.0.81 ### Platform Arch - Linux 6.18.51-1-lts x86_64 GNU/Linux ### Version uv 0.12.”
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/21720), issue body — “.81 ### Platform Arch - Linux 6.18.51-1-lts x86_64 GNU/Linux ### Version uv 0.12.15 (d35f1f270 2026-09-15 x86_64-unknown-linux-gnu) ### Python version 3.14.0”

## Related evidence

- No evidence extracted in this category.

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/21720), issue body — “### Summary It appears to be related to `uv check` using the version of python in `.venv` and ignoring the `requires-python` field in the pyproject.toml whereas ty does? As a minimal example, with `pyproject.toml` ```toml [project] name =…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
