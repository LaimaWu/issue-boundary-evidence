# Issue Boundary Evidence

- Issue: [pydantic/pydantic#13869](https://github.com/pydantic/pydantic/issues/13869) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/pydantic/pydantic/issues/13869)): `model_construct` with `validation_alias=AliasPath(...)` and `extra='allow'` leaves the alias path keys in `model_extra`
- State at retrieval ([issue metadata](https://github.com/pydantic/pydantic/issues/13869)): open
- Method: deterministic, read-only extraction from the issue and its comments

> No major boundary evidence found.

## Environment facts

- **fact** — Runtime mentioned: Python 3.12.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13869), issue body — “t reproduces on the installed release `pydantic 2.13.5` (pydantic_core 2.46.5), Python 3.12. ### Example Code ```python from pydantic import AliasPath, BaseModel, ConfigDict, Field class”
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13869), issue body — “ntic/OS Version - pydantic 2.13.5 (installed release) - pydantic_core 2.46.5 - Python 3.12 The same source locations are present on `main` at `a9a0e1d1`, at the line numbers given in Root C”

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **fact** — Version mentioned: 2.13.5.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13869), issue body — “nstruct`, not a recent change. It reproduces on the installed release `pydantic 2.13.5` (pydantic_core 2.46.5), Python 3.12. ### Example Code ```python from pydantic import AliasPath,”
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13869), issue body — “as. The three branches are not equivalent. On the installed release, `pydantic 2.13.5`, in `main.py`: - lines 344-345: the `field.alias` branch — `values.pop(field.alias)`. - line 357:”
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13869), issue body — “erence only, not as the same issue. ### Python/Pydantic/OS Version - pydantic 2.13.5 (installed release) - pydantic_core 2.46.5 - Python 3.12 The same source locations are present on”
- **fact** — Version mentioned: 3.12.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13869), issue body — “duces on the installed release `pydantic 2.13.5` (pydantic_core 2.46.5), Python 3.12. ### Example Code ```python from pydantic import AliasPath, BaseModel, ConfigDict, Field class”
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13869), issue body — “Version - pydantic 2.13.5 (installed release) - pydantic_core 2.46.5 - Python 3.12 The same source locations are present on `main` at `a9a0e1d1`, at the line numbers given in Root C”

## Related evidence

- No evidence extracted in this category.

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13869), issue body — “### Description `BaseModel.model_construct` does not process `validation_alias`, which is expected — `model_construct` takes field names directly and skips validation. But when a field declares `validation_alias=AliasPath(...)` and the mod…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
