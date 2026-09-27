# Issue Boundary Evidence

- Issue: [vitejs/vite#23588](https://github.com/vitejs/vite/issues/23588) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/vitejs/vite/issues/23588)): New Vite SVG logo renders incorrectly in WebKit
- State at retrieval ([issue metadata](https://github.com/vitejs/vite/issues/23588)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Platform mentioned: macOS.
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “ite.dev/vite-dark.svg These assets were introduced by #21339. In WebKit 27 on macOS 27, rendering either SVG at approximately 24px height can produce: - A soft or blurry appearance -”
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “` height. ### Steps to reproduce 1. Open the reproduction URL in WebKit 27 on macOS 27. 2. Display the official Vite light/dark SVG logos at approximately 24px height. 3. Compare the”
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “eeding, and incorrect edges in WebKit. ### System Info ```shell System: OS: macOS 27.0 (26A428) CPU: Apple M4 Memory: 16 GB Shell: zsh 5.9 Browsers: WebKit: 27.0 Chrome:”

## Boundary candidates

- **strong_clue** — Investigate the external repository boundary with `vuejs/vitepress`.
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “consumers. VitePress documented the same issue and applied a raster fallback in https://github.com/vuejs/vitepress/pull/5466. ### Reproduction https://htmlpreview.github.io/?https://gist.githubusercontent.com/ChisakaKanako”
  - Source: [issue_comment](https://github.com/vitejs/vite/issues/23588#issuecomment-5844668137), comment 1 — “e fallback recommended in this issue and already adopted for the same assets in vuejs/vitepress#5466. File paths, extensions, and `viewBox` are unchanged, so no downstream consumer needs to update any”
- **strong_clue** — Investigate the external repository boundary with `vitejs/.github`.
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “without a raster fallback. ### Validations - [x] Follow our [Code of Conduct](https://github.com/vitejs/.github/blob/main/CODE_OF_CONDUCT.md) - [x] Read the [Contributing Guidelines](https://github.com/vitejs/vite/blob/main/CONTRIBUTING.md)”
- **strong_clue** — Investigate the external repository boundary with `vuejs/core`.
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “le, if it's a Vue SFC related bug, it should likely be reported to [vuejs/core](https://github.com/vuejs/core) instead. - [x] Check that this is a concrete bug. For Q&A open a [GitHub Discussion](https://githu”

## Version and regression clues

- **strong_clue** — Version or regression language: ### System Info ### Used Package Manager npm ### Logs Official Vite logo SVG structure: - filters: 15 - feGaussianBlur: 15 - masks: 1 - viewBox: 0 0 87 15 Downstream workaround and screenshots: https…
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “### System Info ### Used Package Manager npm ### Logs Official Vite logo SVG structure: - filters: 15 - feGaussianBlur: 15 - masks: 1 - viewBox: 0 0 87 15 Downstream workaround and screenshots: https://github.com/vuejs/vitepress/pull/5466…”

## Related evidence

- **fact** — Explicit GitHub link to vuejs/vitepress (external repository): https://github.com/vuejs/vitepress/pull/5466.
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “consumers. VitePress documented the same issue and applied a raster fallback in https://github.com/vuejs/vitepress/pull/5466. ### Reproduction https://htmlpreview.github.io/?https://gist.githubusercontent.com/ChisakaKanako”
- **fact** — Explicit GitHub link to vitejs/.github (external repository): https://github.com/vitejs/.github/blob/main/CODE_OF_CONDUCT.md.
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “without a raster fallback. ### Validations - [x] Follow our [Code of Conduct](https://github.com/vitejs/.github/blob/main/CODE_OF_CONDUCT.md) - [x] Read the [Contributing Guidelines](https://github.com/vitejs/vite/blob/main/CONTRIBUTING.md)”
- **fact** — Explicit GitHub link to vitejs/vite (same repository): https://github.com/vitejs/vite/blob/main/CONTRIBUTING.md.
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “/.github/blob/main/CODE_OF_CONDUCT.md) - [x] Read the [Contributing Guidelines](https://github.com/vitejs/vite/blob/main/CONTRIBUTING.md). - [x] Read the [docs](https://vite.dev/guide). - [x] Check that there isn't [already an issue](ht”
- **fact** — Explicit GitHub link to vitejs/vite (same repository): https://github.com/vitejs/vite/issues.
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “[docs](https://vite.dev/guide). - [x] Check that there isn't [already an issue](https://github.com/vitejs/vite/issues) that reports the same bug to avoid creating a duplicate. - [x] Make sure this is a Vite issue and”
- **fact** — Explicit GitHub link to vuejs/core (external repository): https://github.com/vuejs/core.
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “le, if it's a Vue SFC related bug, it should likely be reported to [vuejs/core](https://github.com/vuejs/core) instead. - [x] Check that this is a concrete bug. For Q&A open a [GitHub Discussion](https://githu”
- **fact** — Explicit GitHub link to vitejs/vite (same repository): https://github.com/vitejs/vite/discussions.
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “ad. - [x] Check that this is a concrete bug. For Q&A open a [GitHub Discussion](https://github.com/vitejs/vite/discussions) or join our [Discord Chat Server](https://chat.vite.dev/). - [x] The provided reproduction is a [m”
- **fact** — Explicit GitHub link to vuejs/vitepress (external repository): https://github.com/vuejs/vitepress/issues/5466.
  - Source: [issue_comment](https://github.com/vitejs/vite/issues/23588#issuecomment-5844668137), comment 1 — “e fallback recommended in this issue and already adopted for the same assets in vuejs/vitepress#5466. File paths, extensions, and `viewBox` are unchanged, so no downstream consumer needs to update any”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/vitejs/vite/issues/23588), issue body — “### Describe the bug The official Vite light and dark SVG logos can render inconsistently in WebKit when displayed at small icon sizes. Affected official assets: - https://vite.dev/vite-light.svg - https://vite.dev/vite-dark.svg These asse…”

## Retrieved same-repository references

- **fact** — [vitejs/vite#5466: fix(hmr): client pinging behind a proxy on websocket disconnect (fix #4501)](https://github.com/vitejs/vite/pull/5466) (source kind: related issue metadata; structured location: title and state=closed)

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
