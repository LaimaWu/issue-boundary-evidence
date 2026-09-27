# Issue Boundary Evidence

- Issue: [matplotlib/matplotlib#32393](https://github.com/matplotlib/matplotlib/issues/32393) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/matplotlib/matplotlib/issues/32393)): [Bug]: webagg backend uses non-existent unload event
- State at retrieval ([issue metadata](https://github.com/matplotlib/matplotlib/issues/32393)): open
- Method: deterministic, read-only extraction from the issue and its comments

> No major boundary evidence found.

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- No evidence extracted in this category.

## Related evidence

- **fact** — Explicit GitHub link to matplotlib/matplotlib (same repository): https://github.com/matplotlib/matplotlib/blob/c1afaeca985ba7cfce0bfcef40a315f641855456/lib/matplotlib/backends/web_backend/js/mpl.js#L83-L85.
  - Source: [issue_body](https://github.com/matplotlib/matplotlib/issues/32393), issue body — “bagg backend uses the `onunload` attribute of the image to close the websocket: https://github.com/matplotlib/matplotlib/blob/c1afaeca985ba7cfce0bfcef40a315f641855456/lib/matplotlib/backends/web_backend/js/mpl.js#L83-L85 I cannot find any…”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/matplotlib/matplotlib/issues/32393), issue body — “### Bug summary The webagg backend uses the `onunload` attribute of the image to close the websocket: https://github.com/matplotlib/matplotlib/blob/c1afaeca985ba7cfce0bfcef40a315f641855456/lib/matplotlib/backends/web_backend/js/mpl.js#L83-…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
