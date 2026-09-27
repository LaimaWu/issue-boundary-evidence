# Issue Boundary Evidence

- Issue: [pydantic/pydantic#13834](https://github.com/pydantic/pydantic/issues/13834) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/pydantic/pydantic/issues/13834)): `create_model`'s `__validators__` annotation excludes the descriptor proxy returned by `model_validator`
- State at retrieval ([issue metadata](https://github.com/pydantic/pydantic/issues/13834)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Runtime mentioned: python=3.14.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13834), issue body — “lated Pixi environment created with: ```shell pixi init --format pixi pixi add python=3.14 pixi add --pypi pydantic==2.13.5 mypy==2.3.1 pyright==1.1.414 pyrefly==0.42.3 ``` Save the example”
- **fact** — Runtime mentioned: python version: 3.14.7.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13834), issue body — “2.46.5 pydantic-core build: profile=release pgo=false python version: 3.14.7 \| packaged by conda-forge \| (main, Sep 2 2026, 21:12:42) [MSC v.1944 64 bit (AMD64)]”
- **fact** — Platform mentioned: Windows.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13834), issue body — “ry used for this reproduction. The interpreter option explicitly selects Pixi's Windows Python executable. ``` No matching overload found for function `pydantic.main.create_model` called”
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13834), issue body — “p 2 2026, 21:12:42) [MSC v.1944 64 bit (AMD64)] platform: Windows-11-10.0.26200-SP0 related packages: mypy-2.3.1 pyright-1.1.414 typing_extensions-4.16.”

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **fact** — Version mentioned: 3.14.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13834), issue body — “ixi environment created with: ```shell pixi init --format pixi pixi add python=3.14 pixi add --pypi pydantic==2.13.5 mypy==2.3.1 pyright==1.1.414 pyrefly==0.42.3 ``` Save the example”
- **fact** — Version mentioned: 2.13.5.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13834), issue body — “```shell pixi init --format pixi pixi add python=3.14 pixi add --pypi pydantic==2.13.5 mypy==2.3.1 pyright==1.1.414 pyrefly==0.42.3 ``` Save the example as `repro.py`. The checker confi”
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13834), issue body — “"value": 1})) ``` ### Python, Pydantic & OS Version ```Text pydantic version: 2.13.5 pydantic-core version: 2.46.5 pydantic-core build: profile=release pgo=false”
- **strong_clue** — Version or regression language: I would keep the change narrow: update the accepted validator type and add regression typing coverage, without changing runtime behavior.
  - Source: [issue_comment](https://github.com/pydantic/pydantic/issues/13834#issuecomment-5738191846), comment 1 — “I would keep the change narrow: update the accepted validator type and add regression typing coverage, without changing runtime behavior.”
- **strong_clue** — Version or regression language: I have a fix and regression tests (both runtime unit tests and type-checking tests for Mypy, Pyright, and Pyrefly) ready on a branch.
  - Source: [issue_comment](https://github.com/pydantic/pydantic/issues/13834#issuecomment-5739824024), comment 2 — “I have a fix and regression tests (both runtime unit tests and type-checking tests for Mypy, Pyright, and Pyrefly) ready on a branch.”
- **strong_clue** — Version or regression language: I have created a minimal PR fixing this in #13837 by updating the __validators__ overloads to include _decorators.PydanticDescriptorProxy[Any] along with regression tests.
  - Source: [issue_comment](https://github.com/pydantic/pydantic/issues/13834#issuecomment-5740498717), comment 3 — “I have created a minimal PR fixing this in #13837 by updating the __validators__ overloads to include _decorators.PydanticDescriptorProxy[Any] along with regression tests.”

## Related evidence

- **fact** — Explicit GitHub link to pydantic/pydantic (same repository): https://github.com/pydantic/pydantic/issues/9690.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13834), issue body — “DecoratorInfo]]) [no-matching-overload] ``` ### Related History Issue [#9690](https://github.com/pydantic/pydantic/issues/9690), resolved by PR [#9697](https://github.com/pydantic/pydantic/pull/9697), addressed a related incom”
- **fact** — Explicit GitHub link to pydantic/pydantic (same repository): https://github.com/pydantic/pydantic/pull/9697.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13834), issue body — “9690](https://github.com/pydantic/pydantic/issues/9690), resolved by PR [#9697](https://github.com/pydantic/pydantic/pull/9697), addressed a related incompatibility by changing the `__validators__` value annotation from `class”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/pydantic/pydantic/issues/13834), issue body — “### Initial Checks - [x] I confirm that I'm using Pydantic V2 ### Description ### Description Passing the result of `model_validator(mode="before")(function)` to `create_model(__validators__=...)` works at runtime, but fails type checking…”

## Retrieved same-repository references

- **fact** — [pydantic/pydantic#9690: Mypy error on __validators__ when using create_model](https://github.com/pydantic/pydantic/issues/9690) (source kind: related issue metadata; structured location: title and state=closed)
- **fact** — [pydantic/pydantic#9697: Relax type specification for `__validators__` values in `create_model`](https://github.com/pydantic/pydantic/pull/9697) (source kind: related issue metadata; structured location: title and state=closed)

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
