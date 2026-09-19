# Issue Boundary Evidence

- Issue: [pytest-dev/pytest#12424](https://github.com/pytest-dev/pytest/issues/12424) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/pytest-dev/pytest/issues/12424)): pytest 8.2.2 breaks pytest-rerunfailures for tests that inherit unittest.TestCase
- State at retrieval ([issue metadata](https://github.com/pytest-dev/pytest/issues/12424)): closed
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- **strong_clue** — Investigate the package/runtime boundary involving `pytest-rerunfailures`.
  - Source: [issue_title](https://github.com/pytest-dev/pytest/issues/12424), issue title — “pytest 8.2.2 breaks pytest-rerunfailures for tests that inherit unittest.TestCase”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12424), issue body — “## pytest 8.2.2 breaks pytest-rerunfailures for tests that inherit unittest.TestCase The code: (placed in `new_file.py`) ```python from”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12424), issue body — “24.0 pluggy 1.5.0 pytest 8.2.2 pytest-rerunfailures 14.0 ```”

## Version and regression clues

- **fact** — Version mentioned: 8.2.2.
  - Source: [issue_title](https://github.com/pytest-dev/pytest/issues/12424), issue title — “pytest 8.2.2 breaks pytest-rerunfailures for tests that inherit unittest.TestCase”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12424), issue body — “## pytest 8.2.2 breaks pytest-rerunfailures for tests that inherit unittest.TestCase The code: (placed in `new_f”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12424), issue body — “one new_file.py:5: AssertionError ``` Regression output: (Using `pytest==8.2.2` / latest version) ``` self = <TestCaseFunction test_base> def runtest(self) -> None:”
- **fact** — Version mentioned: 8.2.1.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12424), issue body — “```bash pytest new_file.py --reruns=1 ``` Expected output: (Using `pytest==8.2.1` / previous version) ``` self = <examples.new_file.MyTestClass testMethod=test_base> def”
- **strong_clue** — Version or regression language: ## pytest 8.2.2 breaks pytest-rerunfailures for tests that inherit unittest.TestCase The code: (placed in `new_file.py`) Run command: Expected output: (Using `pytest==8.2.1` / previous version) Regre…
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12424), issue body — “## pytest 8.2.2 breaks pytest-rerunfailures for tests that inherit unittest.TestCase The code: (placed in `new_file.py`) Run command: Expected output: (Using `pytest==8.2.1` / previous version) Regression output: (Using `pytest==8.2.2` / l…”

## Related evidence

- No evidence extracted in this category.

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12424), issue body — “## pytest 8.2.2 breaks pytest-rerunfailures for tests that inherit unittest.TestCase The code: (placed in `new_file.py`) ```python from unittest import TestCase class MyTestClass(TestCase): def test_base(self): self.fail() ``` Run command:…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
