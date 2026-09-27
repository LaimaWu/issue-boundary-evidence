# Issue Boundary Evidence

- Issue: [pypa/pip#14315](https://github.com/pypa/pip/issues/14315) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/pypa/pip/issues/14315)): Link hashes are parsed from the query string, not only the URL fragment
- State at retrieval ([issue metadata](https://github.com/pypa/pip/issues/14315)): open
- Method: deterministic, read-only extraction from the issue and its comments

> No major boundary evidence found.

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- No evidence extracted in this category.

## Related evidence

- No evidence extracted in this category.

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/pypa/pip/issues/14315), issue body — “`LinkHash.find_hash_url_fragment()` searches the **whole URL** for `[#&](algo)=value`, so a query-string parameter named after a hash algorithm is read as a hash: ```python >>> from pip._internal.models.link import Link >>> Link("https://e…”

## Retrieved same-repository references

- **fact** — [pypa/pip#14316: Read link hashes only from the URL fragment](https://github.com/pypa/pip/pull/14316) (source kind: related issue metadata; structured location: title and state=closed)

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
