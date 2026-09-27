# Issue Boundary Evidence

- Issue: [astral-sh/uv#22006](https://github.com/astral-sh/uv/issues/22006) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/astral-sh/uv/issues/22006)): uv tool install --force --reinstall mutates the tool environment in place: concurrent readers observe missing files for tens of seconds while the install exits 0
- State at retrieval ([issue metadata](https://github.com/astral-sh/uv/issues/22006)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Runtime mentioned: Python 3.13.15.
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/22006), issue body — “5.7.3 arm64 ### Version uv 0.12.6 (7938ca5d5 2026-08-25) ### Python version Python 3.13.15”
- **fact** — Platform mentioned: macOS.
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/22006), issue body — “ble. The cost is duplicated disk per version and manual reaping. ### Platform macOS 15.7.3 arm64 ### Version uv 0.12.6 (7938ca5d5 2026-08-25) ### Python version Python 3.13.15”

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **fact** — Version mentioned: 0.12.6.
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/22006), issue body — “version and manual reaping. ### Platform macOS 15.7.3 arm64 ### Version uv 0.12.6 (7938ca5d5 2026-08-25) ### Python version Python 3.13.15”
- **fact** — Version mentioned: 3.13.15.
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/22006), issue body — “rm64 ### Version uv 0.12.6 (7938ca5d5 2026-08-25) ### Python version Python 3.13.15”
- **strong_clue** — Version or regression language: (And maybe then add an example of this mechanism.) ### Workaround I now install tools into an immutable per-version directory and flip a symlink pointer ourselves; the race becomes impossible rather…
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/22006), issue body — “(And maybe then add an example of this mechanism.) ### Workaround I now install tools into an immutable per-version directory and flip a symlink pointer ourselves; the race becomes impossible rather than detectable.”

## Related evidence

- No evidence extracted in this category.

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/22006), issue body — “### Summary ### Summary `uv tool install --force --reinstall <tool>` replaces the tool environment *in place*. A concurrent reader of that environment, such as the running tool itself, or any process importing from its site-packages, obser…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
