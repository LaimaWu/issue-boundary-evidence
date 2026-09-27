# Issue Boundary Evidence

- Issue: [pytest-dev/pytest#15099](https://github.com/pytest-dev/pytest/issues/15099) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/pytest-dev/pytest/issues/15099)): monkeypatch.setattr fails to undo on objects with a custom __setattr__ (regression from #14969)
- State at retrieval ([issue metadata](https://github.com/pytest-dev/pytest/issues/15099)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Runtime mentioned: Python 3.13.5.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/15099), issue body — “back to the value from `getattr()`, as before. pytest 9.2.0.dev345+g872117358, Python 3.13.5, Windows 11.”
- **fact** — Platform mentioned: Windows 11.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/15099), issue body — “ue from `getattr()`, as before. pytest 9.2.0.dev345+g872117358, Python 3.13.5, Windows 11.”

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **strong_clue** — Version or regression language: monkeypatch.setattr fails to undo on objects with a custom __setattr__ (regression from #14969)
  - Source: [issue_title](https://github.com/pytest-dev/pytest/issues/15099), issue title — “monkeypatch.setattr fails to undo on objects with a custom __setattr__ (regression from #14969)”
- **fact** — Version mentioned: 9.2.0.dev345.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/15099), issue body — “tattr__`. Otherwise fall back to the value from `getattr()`, as before. pytest 9.2.0.dev345+g872117358, Python 3.13.5, Windows 11.”
- **fact** — Version mentioned: 3.13.5.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/15099), issue body — “the value from `getattr()`, as before. pytest 9.2.0.dev345+g872117358, Python 3.13.5, Windows 11.”
- **strong_clue** — Version or regression language: I'm opening this issue so it gets fixed before the next release.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/15099), issue body — “I'm opening this issue so it gets fixed before the next release.”

## Related evidence

- No evidence extracted in this category.

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/15099), issue body — “Since #14969 (0c601d510, not released yet), `monkeypatch.setattr` doesn't restore attributes on objects that store them somewhere other than `__dict__` through a custom `__setattr__`/`__getattr__`. Undo raises `AttributeError`, and the pat…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
