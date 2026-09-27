# Issue Boundary Evidence

- Issue: [oven-sh/bun#44134](https://github.com/oven-sh/bun/issues/44134) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/oven-sh/bun/issues/44134)): Bun.WebView (webkit): navigate() sometimes never settles when the reply frame is over 8 KB (URL longer than ~8.15 KB)
- State at retrieval ([issue metadata](https://github.com/oven-sh/bun/issues/44134)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Platform mentioned: macOS.
  - Source: [issue_body](https://github.com/oven-sh/bun/issues/44134), issue body — “1.4.2+744846f84 ### What platform is your computer? Darwin 27.0.0 arm64 arm (macOS 27.0, WebKit backend) ### What steps can reproduce the bug? The script needs no dependencies and”

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **fact** — Version mentioned: 8.15.
  - Source: [issue_title](https://github.com/oven-sh/bun/issues/44134), issue title — “e() sometimes never settles when the reply frame is over 8 KB (URL longer than ~8.15 KB)”
  - Source: [issue_body](https://github.com/oven-sh/bun/issues/44134), issue body — “d, whatever the URL length. ### What do you see instead? For a URL over about 8.15 KB, a few percent of `navigate()` calls stay pending after the page has loaded (`document.readyStat”
- **strong_clue** — Version or regression language: Workaround: while `navigate()` is pending, send a no-op `evaluate("0")` every 100 ms.
  - Source: [issue_body](https://github.com/oven-sh/bun/issues/44134), issue body — “Workaround: while `navigate()` is pending, send a no-op `evaluate("0")` every 100 ms.”

## Related evidence

- No evidence extracted in this category.

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/oven-sh/bun/issues/44134), issue body — “### What version of Bun is running? 1.4.2+744846f84 ### What platform is your computer? Darwin 27.0.0 arm64 arm (macOS 27.0, WebKit backend) ### What steps can reproduce the bug? The script needs no dependencies and no server. Run it as `b…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
