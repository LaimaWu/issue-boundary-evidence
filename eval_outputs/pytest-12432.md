# Issue Boundary Evidence

- Issue: [pytest-dev/pytest#12432](https://github.com/pytest-dev/pytest/issues/12432) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/pytest-dev/pytest/issues/12432)): MockAwareDocTestFinder._find is stale
- State at retrieval ([issue metadata](https://github.com/pytest-dev/pytest/issues/12432)): closed
- Method: deterministic, read-only extraction from the issue and its comments

> No major boundary evidence found.

## Environment facts

- **fact** — Runtime mentioned: Python 3.10.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12432), issue body — “in the class. It appears that the tests all pass with the method removed on Python 3.10 and later.”

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **fact** — Version mentioned: 3.10.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12432), issue body — “class. It appears that the tests all pass with the method removed on Python 3.10 and later.”
- **fact** — Historical commit referenced: [a6988aa0b92c93bfd397d6b788249488b8f5d300](https://github.com/pytest-dev/pytest/commit/a6988aa0b92c93bfd397d6b788249488b8f5d300).
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12432), issue body — “the comments in the class are related. Indeed, looking at where that method was introduced (a6988aa0b92c93bfd397d6b788249488b8f5d300), it's associated with the docstring in the class. It appears that the tests all pass with the m”

## Related evidence

- **fact** — Explicit GitHub link to pytest-dev/pytest (same repository): https://github.com/pytest-dev/pytest/blob/043ff9abc657124db3504d3604e16ddebfe6e28f/src/_pytest/doctest.py#L534-L543.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12432), issue body — “The implementation of _find has no comments: https://github.com/pytest-dev/pytest/blob/043ff9abc657124db3504d3604e16ddebfe6e28f/src/_pytest/doctest.py#L534-L543 Perhaps the comments in the class are related. Indeed, looking at where that m…”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12432), issue body — “The implementation of _find has no comments: https://github.com/pytest-dev/pytest/blob/043ff9abc657124db3504d3604e16ddebfe6e28f/src/_pytest/doctest.py#L534-L543 Perhaps the comments in the class are related. Indeed, looking at where that m…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
