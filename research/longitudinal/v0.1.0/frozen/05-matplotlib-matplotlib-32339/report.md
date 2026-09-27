# Issue Boundary Evidence

- Issue: [matplotlib/matplotlib#32339](https://github.com/matplotlib/matplotlib/issues/32339) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/matplotlib/matplotlib/issues/32339)): [MNT]: Old macOS CI is failing to install
- State at retrieval ([issue metadata](https://github.com/matplotlib/matplotlib/issues/32339)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Platform mentioned: macOS.
  - Source: [issue_title](https://github.com/matplotlib/matplotlib/issues/32339), issue title — “[MNT]: Old macOS CI is failing to install”
  - Source: [issue_body](https://github.com/matplotlib/matplotlib/issues/32339), issue body — “### Summary Since about 12-15 hours ago, the builds on `macOS-14` are failing with: ``` Error: tesseract: no bottle available! If you're feeling brave, you can t”
  - Source: [issue_body](https://github.com/matplotlib/matplotlib/issues/32339), issue body — “a from Ghostscript as well. Maybe what we'll have to do is bump all CI jobs to macOS 15? @iccir”
- **fact** — Runtime mentioned: Python 3.11.
  - Source: [issue_comment](https://github.com/matplotlib/matplotlib/issues/32339#issuecomment-5639654297), comment 3 — “ython version / macOS Version \| Python version \| Installer requires: \| \|-\|-\| \| Python 3.11 \| macOS 10.9 \| \| Python 3.12 \| macOS 10.13 \| \| Python 3.13 \| macOS 10.13 \| \| Python 3.14 \| macOS 10”
- **fact** — Runtime mentioned: Python 3.12.
  - Source: [issue_comment](https://github.com/matplotlib/matplotlib/issues/32339#issuecomment-5639654297), comment 3 — “\| Python version \| Installer requires: \| \|-\|-\| \| Python 3.11 \| macOS 10.9 \| \| Python 3.12 \| macOS 10.13 \| \| Python 3.13 \| macOS 10.13 \| \| Python 3.14 \| macOS 10.15 \| \| Python 3.15 \| macOS 1”
- **fact** — Runtime mentioned: Python 3.13.
  - Source: [issue_comment](https://github.com/matplotlib/matplotlib/issues/32339#issuecomment-5639654297), comment 3 — “requires: \| \|-\|-\| \| Python 3.11 \| macOS 10.9 \| \| Python 3.12 \| macOS 10.13 \| \| Python 3.13 \| macOS 10.13 \| \| Python 3.14 \| macOS 10.15 \| \| Python 3.15 \| macOS 10.15 \|”
- **fact** — Runtime mentioned: Python 3.14.
  - Source: [issue_comment](https://github.com/matplotlib/matplotlib/issues/32339#issuecomment-5639654297), comment 3 — “11 \| macOS 10.9 \| \| Python 3.12 \| macOS 10.13 \| \| Python 3.13 \| macOS 10.13 \| \| Python 3.14 \| macOS 10.15 \| \| Python 3.15 \| macOS 10.15 \|”
- **fact** — Runtime mentioned: Python 3.15.
  - Source: [issue_comment](https://github.com/matplotlib/matplotlib/issues/32339#issuecomment-5639654297), comment 3 — “2 \| macOS 10.13 \| \| Python 3.13 \| macOS 10.13 \| \| Python 3.14 \| macOS 10.15 \| \| Python 3.15 \| macOS 10.15 \|”

## Boundary candidates

- **strong_clue** — Investigate the external repository boundary with `Homebrew/homebrew-core`.
  - Source: [issue_body](https://github.com/matplotlib/matplotlib/issues/32339), issue body — “es or PRs. ``` It looks like about 15 hours ago Homebrew updated their formula: https://github.com/Homebrew/homebrew-core/pull/304735 and dropped Sonoma. ### Proposed fix I'm not totally familiar with Homebrew, but since this is a”

## Version and regression clues

- **fact** — Version mentioned: 3.11.
  - Source: [issue_comment](https://github.com/matplotlib/matplotlib/issues/32339#issuecomment-5639654297), comment 3 — “ersion / macOS Version \| Python version \| Installer requires: \| \|-\|-\| \| Python 3.11 \| macOS 10.9 \| \| Python 3.12 \| macOS 10.13 \| \| Python 3.13 \| macOS 10.13 \| \| Python 3.14 \| macOS 10”
- **fact** — Version mentioned: 3.12.
  - Source: [issue_comment](https://github.com/matplotlib/matplotlib/issues/32339#issuecomment-5639654297), comment 3 — “hon version \| Installer requires: \| \|-\|-\| \| Python 3.11 \| macOS 10.9 \| \| Python 3.12 \| macOS 10.13 \| \| Python 3.13 \| macOS 10.13 \| \| Python 3.14 \| macOS 10.15 \| \| Python 3.15 \| macOS 1”
- **fact** — Version mentioned: 3.13.
  - Source: [issue_comment](https://github.com/matplotlib/matplotlib/issues/32339#issuecomment-5639654297), comment 3 — “es: \| \|-\|-\| \| Python 3.11 \| macOS 10.9 \| \| Python 3.12 \| macOS 10.13 \| \| Python 3.13 \| macOS 10.13 \| \| Python 3.14 \| macOS 10.15 \| \| Python 3.15 \| macOS 10.15 \|”
- **fact** — Version mentioned: 3.14.
  - Source: [issue_comment](https://github.com/matplotlib/matplotlib/issues/32339#issuecomment-5639654297), comment 3 — “cOS 10.9 \| \| Python 3.12 \| macOS 10.13 \| \| Python 3.13 \| macOS 10.13 \| \| Python 3.14 \| macOS 10.15 \| \| Python 3.15 \| macOS 10.15 \|”
- **fact** — Version mentioned: 3.15.
  - Source: [issue_comment](https://github.com/matplotlib/matplotlib/issues/32339#issuecomment-5639654297), comment 3 — “OS 10.13 \| \| Python 3.13 \| macOS 10.13 \| \| Python 3.14 \| macOS 10.15 \| \| Python 3.15 \| macOS 10.15 \|”

## Related evidence

- **fact** — Explicit GitHub link to Homebrew/homebrew-core (external repository): https://github.com/Homebrew/homebrew-core/pull/304735.
  - Source: [issue_body](https://github.com/matplotlib/matplotlib/issues/32339), issue body — “es or PRs. ``` It looks like about 15 hours ago Homebrew updated their formula: https://github.com/Homebrew/homebrew-core/pull/304735 and dropped Sonoma. ### Proposed fix I'm not totally familiar with Homebrew, but since this is a”
- **fact** — Explicit GitHub link to matplotlib/matplotlib (same repository): https://github.com/matplotlib/matplotlib/actions/runs/35039338170/job/104615460661#step:4:330.
  - Source: [issue_comment](https://github.com/matplotlib/matplotlib/issues/32339#issuecomment-5690247832), comment 4 — “somehow been magically fixed, though there are no bottle for tesseract any more https://github.com/matplotlib/matplotlib/actions/runs/35039338170/job/104615460661#step:4:330”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/matplotlib/matplotlib/issues/32339), issue body — “### Summary Since about 12-15 hours ago, the builds on `macOS-14` are failing with: ``` Error: tesseract: no bottle available! If you're feeling brave, you can try to install from source with: brew install --build-from-source tesseract Thi…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
