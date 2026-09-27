# Issue Boundary Evidence

- Issue: [microsoft/TypeScript#64477](https://github.com/microsoft/TypeScript/issues/64477) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/microsoft/TypeScript/issues/64477)): TS6059 error count flakes between runs unless --singleThreaded
- State at retrieval ([issue metadata](https://github.com/microsoft/TypeScript/issues/64477)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- **strong_clue** — Investigate the external repository boundary with `mui/material-ui.git`.
  - Source: [issue_body](https://github.com/microsoft/TypeScript/issues/64477), issue body — “project (the `mui-docs` scenario in typescript-benchmarking): ```sh git clone https://github.com/mui/material-ui.git cd material-ui git checkout 190a83cf3784c53b57d7a80cf96df27276eed079 pnpm install --ignore-scripts”

## Version and regression clues

- **fact** — Version mentioned: 7.0.2.
  - Source: [issue_body](https://github.com/microsoft/TypeScript/issues/64477), issue body — “ror count, singleThreaded ### 🕗 Version & Regression Information seeing it on 7.0.2 and on main (4f5ddae2). havent tried older versions ### ⏯ Playground Link _No response_ ### 💻 Co”
- **strong_clue** — Version or regression language: ### 🔎 Search Terms TS6059, rootDir, flaky error count, singleThreaded ### 🕗 Version & Regression Information seeing it on 7.0.2 and on main (4f5ddae2).
  - Source: [issue_body](https://github.com/microsoft/TypeScript/issues/64477), issue body — “### 🔎 Search Terms TS6059, rootDir, flaky error count, singleThreaded ### 🕗 Version & Regression Information seeing it on 7.0.2 and on main (4f5ddae2).”
- **strong_clue** — Version or regression language: havent tried older versions ### ⏯ Playground Link _No response_ ### 💻 Code repros on material-ui's docs project (the `mui-docs` scenario in typescript-benchmarking): tried to get a small repro (tscon…
  - Source: [issue_body](https://github.com/microsoft/TypeScript/issues/64477), issue body — “havent tried older versions ### ⏯ Playground Link _No response_ ### 💻 Code repros on material-ui's docs project (the `mui-docs` scenario in typescript-benchmarking): tried to get a small repro (tsconfig `paths` pointing outside `rootDir`,…”

## Related evidence

- **fact** — Explicit GitHub link to mui/material-ui.git (external repository): https://github.com/mui/material-ui.git.
  - Source: [issue_body](https://github.com/microsoft/TypeScript/issues/64477), issue body — “project (the `mui-docs` scenario in typescript-benchmarking): ```sh git clone https://github.com/mui/material-ui.git cd material-ui git checkout 190a83cf3784c53b57d7a80cf96df27276eed079 pnpm install --ignore-scripts”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/microsoft/TypeScript/issues/64477), issue body — “### 🔎 Search Terms TS6059, rootDir, flaky error count, singleThreaded ### 🕗 Version & Regression Information seeing it on 7.0.2 and on main (4f5ddae2). havent tried older versions ### ⏯ Playground Link _No response_ ### 💻 Code repros on ma…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
