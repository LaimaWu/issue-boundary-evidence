# Issue Boundary Evidence

- Issue: [vercel/next.js#99318](https://github.com/vercel/next.js/issues/99318) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/vercel/next.js/issues/99318)): notFound() returns 200 instead of 404 when a sibling route has dynamicParams: true
- State at retrieval ([issue metadata](https://github.com/vercel/next.js/issues/99318)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Platform mentioned: Windows 11.
  - Source: [issue_body](https://github.com/vercel/next.js/issues/99318), issue body — “information ```bash Operating System: Platform: win32 Arch: x64 Version: Windows 11 Pro Available memory (MB): 8007 Available CPU cores: 8 Binaries: Node: 20.19.5 npm: 10.8.2”

## Boundary candidates

- **strong_clue** — Investigate the external repository boundary with `afaqjutt786470-ops/nextjs-nested-notfound-200-bug`.
  - Source: [issue_body](https://github.com/vercel/next.js/issues/99318), issue body — “### Link to the code that reproduces this issue https://github.com/afaqjutt786470-ops/nextjs-nested-notfound-200-bug ### To Reproduce 1. Clone the linked reproduction and `npm install` 2. `npm run build && npm run”

## Version and regression clues

- **fact** — Version mentioned: 16.3.4.
  - Source: [issue_body](https://github.com/vercel/next.js/issues/99318), issue body — “yed) ### Additional context This was originally found on a production Next.js 16.3.4 app deployed to Vercel, where an unmatched param under a `dynamicParams: false` route (e.g. `/brand”
- **fact** — Version mentioned: 16.3.6.
  - Source: [issue_body](https://github.com/vercel/next.js/issues/99318), issue body — “xt` directory (ruling out a stale-cache artifact). The app was then upgraded to 16.3.6, and the bug was still present, confirming it independently of the specific canary/stable build. T”

## Related evidence

- **fact** — Explicit GitHub link to afaqjutt786470-ops/nextjs-nested-notfound-200-bug (external repository): https://github.com/afaqjutt786470-ops/nextjs-nested-notfound-200-bug.
  - Source: [issue_body](https://github.com/vercel/next.js/issues/99318), issue body — “### Link to the code that reproduces this issue https://github.com/afaqjutt786470-ops/nextjs-nested-notfound-200-bug ### To Reproduce 1. Clone the linked reproduction and `npm install` 2. `npm run build && npm run”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/vercel/next.js/issues/99318), issue body — “### Link to the code that reproduces this issue https://github.com/afaqjutt786470-ops/nextjs-nested-notfound-200-bug ### To Reproduce 1. Clone the linked reproduction and `npm install` 2. `npm run build && npm run start` 3. `curl -I http:/…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
