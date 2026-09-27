# Issue Boundary Evidence

- Issue: [astral-sh/uv#21829](https://github.com/astral-sh/uv/issues/21829) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/astral-sh/uv/issues/21829)): granular and user-friendly management of cached packages
- State at retrieval ([issue metadata](https://github.com/astral-sh/uv/issues/21829)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **strong_clue** — Version or regression language: Different projects may have different dependencies and when some are upgraded, the previous version is left behind unused in the cache.
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/21829), issue body — “Different projects may have different dependencies and when some are upgraded, the previous version is left behind unused in the cache.”
- **fact** — Version mentioned: 2.14.0.
  - Source: [issue_comment](https://github.com/astral-sh/uv/issues/21829#issuecomment-5735325203), comment 2 — “f my use case is, for example, removing one exact distribution, such as `torch==2.14.0+cu132`, while retaining `torch==2.14.0+cu130`. Torch is emblematic as it requires GBs, so you can s”
  - Source: [issue_comment](https://github.com/astral-sh/uv/issues/21829#issuecomment-5735325203), comment 2 — “one exact distribution, such as `torch==2.14.0+cu132`, while retaining `torch==2.14.0+cu130`. Torch is emblematic as it requires GBs, so you can see that the aforementioned pain points”

## Related evidence

- No evidence extracted in this category.

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/astral-sh/uv/issues/21829), issue body — “Using a symlink cache is the only way to prevent wastage of disk space for a machine with multiple projects. Different projects may have different dependencies and when some are upgraded, the previous version is left behind unused in the c…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
