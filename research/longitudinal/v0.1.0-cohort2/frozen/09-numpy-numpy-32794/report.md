# Issue Boundary Evidence

- Issue: [numpy/numpy#32794](https://github.com/numpy/numpy/issues/32794) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/numpy/numpy/issues/32794)): import error if numpy >2.3.5
- State at retrieval ([issue metadata](https://github.com/numpy/numpy/issues/32794)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Runtime mentioned: python 3.13.15.
  - Source: [issue_body](https://github.com/numpy/numpy/issues/32794), issue body — “### Steps to reproduce: I'm on a fresh windows10 setup, python 3.13.15 x64 I installed numpy with `pip install numpy`: it installed numpy 2.5.3, but `imports numpy` fail”
- **fact** — Runtime mentioned: Python 3.13.
  - Source: [issue_body](https://github.com/numpy/numpy/issues/32794), issue body — “orterror.html Please note and check the following: * The Python version is: Python 3.13 from "C:\Python\Python313\pythonw.exe" * The NumPy version is: "2.5.3" and make sure that they a”
- **fact** — Platform mentioned: windows.
  - Source: [issue_comment](https://github.com/numpy/numpy/issues/32794#issuecomment-5846093788), comment 1 — “hon and numpy i.e. what is your environment setup (from the paths it looks like windows installed from python.org and then global pip install?) and also what cpu do you have? Numpy 2.4 ra”

## Boundary candidates

- **strong_clue** — Investigate the package/runtime boundary involving `error`.
  - Source: [issue_title](https://github.com/numpy/numpy/issues/32794), issue title — “import error if numpy >2.3.5”

## Version and regression clues

- **fact** — Version mentioned: 2.3.5.
  - Source: [issue_title](https://github.com/numpy/numpy/issues/32794), issue title — “import error if numpy >2.3.5”
  - Source: [issue_body](https://github.com/numpy/numpy/issues/32794), issue body — “shooting-importerror.html](url) didn't solve the issue. I then installed numpy 2.3.5: this one imports fine and I can work with it with no issues. I searched here for issues on import”
- **fact** — Version mentioned: 3.13.15.
  - Source: [issue_body](https://github.com/numpy/numpy/issues/32794), issue body — “### Steps to reproduce: I'm on a fresh windows10 setup, python 3.13.15 x64 I installed numpy with `pip install numpy`: it installed numpy 2.5.3, but `imports numpy` fail”
- **fact** — Version mentioned: 2.5.3.
  - Source: [issue_body](https://github.com/numpy/numpy/issues/32794), issue body — “hon 3.13.15 x64 I installed numpy with `pip install numpy`: it installed numpy 2.5.3, but `imports numpy` fails. I tried installing numpy 2.4.1 and the same happened. The tips at [http”
- **fact** — Version mentioned: 2.4.1.
  - Source: [issue_body](https://github.com/numpy/numpy/issues/32794), issue body — “: it installed numpy 2.5.3, but `imports numpy` fails. I tried installing numpy 2.4.1 and the same happened. The tips at [https://numpy.org/devdocs/user/troubleshooting-importerror.html”
- **fact** — Version mentioned: 2.4.
  - Source: [issue_comment](https://github.com/numpy/numpy/issues/32794#issuecomment-5846093788), comment 1 — “m python.org and then global pip install?) and also what cpu do you have? Numpy 2.4 raised the default cpu base line to the v2 microarchitecture for x86 822665c9c3633e97fa599311b9b4dc”
- **fact** — Historical commit referenced: [822665c9c3633e97fa599311b9b4dcc50bae2527](https://github.com/numpy/numpy/commit/822665c9c3633e97fa599311b9b4dcc50bae2527).
  - Source: [issue_comment](https://github.com/numpy/numpy/issues/32794#issuecomment-5854562610), comment 3 — “Now that you pointed me to #30492 , #31478 and https://github.com/numpy/numpy/commit/822665c9c3633e97fa599311b9b4dcc50bae2527 I see the issue is probably related to my CPU not supporting x86-64-v2 fully. But I'll be frank, I”

## Related evidence

- **fact** — Explicit GitHub link to numpy/numpy (same repository): https://github.com/numpy/numpy/issues/30492.
  - Source: [issue_comment](https://github.com/numpy/numpy/issues/32794#issuecomment-5846127377), comment 2 — “Also looks like the same problem as https://github.com/numpy/numpy/issues/30492 to me as well and somewhat related to https://github.com/numpy/numpy/issues/31478.”
- **fact** — Explicit GitHub link to numpy/numpy (same repository): https://github.com/numpy/numpy/issues/31478.
  - Source: [issue_comment](https://github.com/numpy/numpy/issues/32794#issuecomment-5846127377), comment 2 — “tps://github.com/numpy/numpy/issues/30492 to me as well and somewhat related to https://github.com/numpy/numpy/issues/31478.”
- **fact** — Explicit GitHub link to numpy/numpy (same repository): https://github.com/numpy/numpy/commit/822665c9c3633e97fa599311b9b4dcc50bae2527.
  - Source: [issue_comment](https://github.com/numpy/numpy/issues/32794#issuecomment-5854562610), comment 3 — “.org, and then numpy using pip. Now that you pointed me to #30492 , #31478 and https://github.com/numpy/numpy/commit/822665c9c3633e97fa599311b9b4dcc50bae2527 I see the issue is probably related to my CPU not supporting x86-64-v2 fully. But…”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/numpy/numpy/issues/32794), issue body — “### Steps to reproduce: I'm on a fresh windows10 setup, python 3.13.15 x64 I installed numpy with `pip install numpy`: it installed numpy 2.5.3, but `imports numpy` fails. I tried installing numpy 2.4.1 and the same happened. The tips at […”

## Retrieved same-repository references

- **fact** — [numpy/numpy#30492: BUG: illegal instruction on import](https://github.com/numpy/numpy/issues/30492) (source kind: related issue metadata; structured location: title and state=open)
- **fact** — [numpy/numpy#31478: Un-redirect SSE41, SSE42, POPCNT](https://github.com/numpy/numpy/issues/31478) (source kind: related issue metadata; structured location: title and state=open)

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
