# Issue Boundary Evidence

- Issue: [nodejs/node#66349](https://github.com/nodejs/node/issues/66349) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/nodejs/node/issues/66349)): stream: Duplex.from errors when async function body resolves without consuming its input
- State at retrieval ([issue metadata](https://github.com/nodejs/node/issues/66349)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **fact** — Version mentioned: 26.10.0.
  - Source: [issue_body](https://github.com/nodejs/node/issues/66349), issue body — “tem _No response_ ### What steps will reproduce the bug? The bug, as of node 26.10.0: ``` node -v v26.10.0 node -e "require('node:stream').Duplex.from(async () => {})" node:events:505”
- **fact** — Version mentioned: 26.9.0.
  - Source: [issue_body](https://github.com/nodejs/node/issues/66349), issue body — “behavior? Why is that the expected behavior? The original behavior, as of node 26.9.0: ``` node -v v26.9.0 node -e "require('node:stream').Duplex.from(async () => {})" // no output; th”
- **strong_clue** — Version or regression language: ### Additional information `0bf9e9f833` (#65963) introduced a regression.
  - Source: [issue_body](https://github.com/nodejs/node/issues/66349), issue body — “### Additional information `0bf9e9f833` (#65963) introduced a regression.”

## Related evidence

- **fact** — Explicit GitHub link to nodejs/node (same repository): https://github.com/nodejs/node/pull/66243.
  - Source: [issue_body](https://github.com/nodejs/node/issues/66349), issue body — “anything that uses `p-transform` (yeoman-environment and mem-fs). PR fix here: https://github.com/nodejs/node/pull/66243”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/nodejs/node/issues/66349), issue body — “### Version 26.10.0 ### Platform ```text All ``` ### Subsystem _No response_ ### What steps will reproduce the bug? The bug, as of node 26.10.0: ``` node -v v26.10.0 node -e "require('node:stream').Duplex.from(async () => {})" node:events:…”

## Retrieved same-repository references

- **fact** — [nodejs/node#66243: stream: do not error on Duplex.from early return](https://github.com/nodejs/node/pull/66243) (source kind: related issue metadata; structured location: title and state=open)

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
