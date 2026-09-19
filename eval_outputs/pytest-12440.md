# Issue Boundary Evidence

- Issue: [pytest-dev/pytest#12440](https://github.com/pytest-dev/pytest/issues/12440) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/pytest-dev/pytest/issues/12440)): pytest 8.2.2 fails assertion
- State at retrieval ([issue metadata](https://github.com/pytest-dev/pytest/issues/12440)): closed
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Runtime mentioned: Python 3.10.14.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “=3.5 pytest==8.2.2 pytest-rerunfailures==14.0 pytest-xv ``` We're using: Python 3.10.14, pytest-8.2.2, pluggy-1.5.0 and pytest plugins rerunfailures-14.0, xvfb-3.0.0. OS is whatever GitHu”
- **fact** — Platform mentioned: windows.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “ibly because of the change in #12368. I can't reproduce the error locally on my windows machine, however when pinning [pytest's version to <8.2.2](https://github.com/LabExT/LabExT/pull/22”
- **fact** — Platform mentioned: ubuntu.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “t plugins rerunfailures-14.0, xvfb-3.0.0. OS is whatever GitHub CI installs on 'ubuntu-latest'. - [x] a detailed description of the bug or problem you are having - [x] output of `pip”

## Boundary candidates

- **strong_clue** — Investigate the external repository boundary with `LabExT/LabExT`.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “Discovered while testing [LabExT](https://github.com/LabExT/LabExT) with pytest 8.2.2. We do integration testing of a TKinter GUI as part of our CI. A [particularly l”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “egration testing of a TKinter GUI as part of our CI. A [particularly long test](https://github.com/LabExT/LabExT/blob/93aa981d394ea4d8ac9e3c72b3b34b2763115b65/LabExT/Tests/View/MainWindow_test.py#L69) fails with an assertion error when usi…”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “ocally on my windows machine, however when pinning [pytest's version to <8.2.2](https://github.com/LabExT/LabExT/pull/221/files), this assertion is not triggered and our CI succeeds. Console output from the CI run here”

## Version and regression clues

- **fact** — Version mentioned: 8.2.2.
  - Source: [issue_title](https://github.com/pytest-dev/pytest/issues/12440), issue title — “pytest 8.2.2 fails assertion”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “Discovered while testing [LabExT](https://github.com/LabExT/LabExT) with pytest 8.2.2. We do integration testing of a TKinter GUI as part of our CI. A [particularly long test](https://g”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “ts/View/MainWindow_test.py#L69) fails with an assertion error when using pytest=8.2.2 instead of an older version. The assertion error is raised possibly because of the change in #12368”
- **fact** — Version mentioned: 2.3.0.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “ExT_pkg @ file:///home/runner/work/LabExT/LabExT/.tox/.tmp/package/4/labext_pkg-2.3.0.tar.gz#sha256=adab0666260601cb92a80e42cfc5a4b5c35c944d75742b8252b5b7fff29eba39 Markdown==3.5.2 Ma”
- **fact** — Version mentioned: 3.10.14.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “ytest==8.2.2 pytest-rerunfailures==14.0 pytest-xv ``` We're using: Python 3.10.14, pytest-8.2.2, pluggy-1.5.0 and pytest plugins rerunfailures-14.0, xvfb-3.0.0. OS is whatever GitHu”
- **strong_clue** — Version or regression language: A [particularly long test](https://github.com/LabExT/LabExT/blob/93aa981d394ea4d8ac9e3c72b3b34b2763115b65/LabExT/Tests/View/MainWindow_test.py#L69) fails with an assertion error when using pytest=8.2…
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “A [particularly long test](https://github.com/LabExT/LabExT/blob/93aa981d394ea4d8ac9e3c72b3b34b2763115b65/LabExT/Tests/View/MainWindow_test.py#L69) fails with an assertion error when using pytest=8.2.2 instead of an older version.”
- **strong_clue** — Version or regression language: Thanks for the report, we have fixed this issue yesterday and it will be included in the next release.
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12440#issuecomment-2155858201), comment 1 — “Thanks for the report, we have fixed this issue yesterday and it will be included in the next release.”

## Related evidence

- **fact** — Explicit GitHub link to LabExT/LabExT (external repository): https://github.com/LabExT/LabExT.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “Discovered while testing [LabExT](https://github.com/LabExT/LabExT) with pytest 8.2.2. We do integration testing of a TKinter GUI as part of our CI. A [particularly l”
- **fact** — Explicit GitHub link to LabExT/LabExT (external repository): https://github.com/LabExT/LabExT/blob/93aa981d394ea4d8ac9e3c72b3b34b2763115b65/LabExT/Tests/View/MainWindow_test.py#L69.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “egration testing of a TKinter GUI as part of our CI. A [particularly long test](https://github.com/LabExT/LabExT/blob/93aa981d394ea4d8ac9e3c72b3b34b2763115b65/LabExT/Tests/View/MainWindow_test.py#L69) fails with an assertion error when usi…”
- **fact** — Explicit GitHub link to LabExT/LabExT (external repository): https://github.com/LabExT/LabExT/pull/221.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “ocally on my windows machine, however when pinning [pytest's version to <8.2.2](https://github.com/LabExT/LabExT/pull/221/files), this assertion is not triggered and our CI succeeds. Console output from the CI run here”

## Evidence gaps

- **fact** — Responsibility or reproduction uncertainty is explicit: I can't reproduce the error locally on my windows machine, however when pinning [pytest's version to <8.2.2](https://github.com/LabExT/LabExT/pull/221/files), this assertion is not triggered and our…
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12440), issue body — “I can't reproduce the error locally on my windows machine, however when pinning [pytest's version to <8.2.2](https://github.com/LabExT/LabExT/pull/221/files), this assertion is not triggered and our CI succeeds.”

## Retrieved same-repository references

- **fact** — [pytest-dev/pytest#12368: unittest: fix class instances no longer released on test teardown since pytest 8.2.0](https://github.com/pytest-dev/pytest/pull/12368) (source kind: related issue metadata; structured location: title and state=closed)

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
