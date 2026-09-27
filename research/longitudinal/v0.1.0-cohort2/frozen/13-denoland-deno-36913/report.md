# Issue Boundary Evidence

- Issue: [denoland/deno#36913](https://github.com/denoland/deno/issues/36913) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/denoland/deno/issues/36913)): deno desktop - delayed window closure broken
- State at retrieval ([issue metadata](https://github.com/denoland/deno/issues/36913)): open
- Method: deterministic, read-only extraction from the issue and its comments

> No major boundary evidence found.

## Environment facts

- **fact** — Platform mentioned: MacOS.
  - Source: [issue_body](https://github.com/denoland/deno/issues/36913), issue body — “Version: Deno 2.9.7 MacOS 27.0 Golden Gate MBP Pro M1 The ability to do some actions before the window is closed using the m”

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **fact** — Version mentioned: 2.9.7.
  - Source: [issue_body](https://github.com/denoland/deno/issues/36913), issue body — “Version: Deno 2.9.7 MacOS 27.0 Golden Gate MBP Pro M1 The ability to do some actions before the window is closed using”

## Related evidence

- No evidence extracted in this category.

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/denoland/deno/issues/36913), issue body — “Version: Deno 2.9.7 MacOS 27.0 Golden Gate MBP Pro M1 The ability to do some actions before the window is closed using the main window close control appears to be broken. According to the docs - <pre> win.addEventListener("close", async (e…”

## Retrieved same-repository references

- **fact** — [denoland/deno#36666: fix(desktop): complete the window close in the close-requested handler](https://github.com/denoland/deno/pull/36666) (source kind: related issue metadata; structured location: title and state=closed)

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
