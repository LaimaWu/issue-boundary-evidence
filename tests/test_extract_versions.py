import unittest

from issue_boundary_evidence.extract import extract_evidence, extract_regression_phrases, extract_versions
from issue_boundary_evidence.models import Issue


class VersionExtractionTests(unittest.TestCase):
    def test_extracts_versions_without_issue_numbers(self):
        text = "Worked in pytest 8.2.1, regressed in 8.2.2; Python 3.11.9 is fixed. See #12471."
        self.assertEqual(extract_versions(text), ["8.2.1", "8.2.2", "3.11.9"])

    def test_extracts_regression_phrase(self):
        phrases = extract_regression_phrases("It worked in 8.2.1. It no longer works after upgrading.")
        self.assertEqual(len(phrases), 2)

    def test_trailing_punctuation_is_not_part_of_version(self):
        self.assertEqual(extract_versions("Python 3.11. Previously 3.11.8."), ["3.11", "3.11.8"])

    def test_report_prioritizes_contextual_versions(self):
        issue = Issue(
            "org",
            "numpy",
            1,
            "https://github.com/org/numpy/issues/1",
            "NumPy regression",
            "Python 3.11.\nOS-release: 5.15.146.1.\nCompiler build: 14.2.1.\n"
            "Python 3.13 free threading on macOS 14.3.1.\nNumPy 2.0 regressed after updating.",
        )
        claims = [item.claim for item in extract_evidence(issue) if item.category == "version"]
        self.assertIn("Version mentioned: 3.11.", claims)
        self.assertIn("Version mentioned: 2.0.", claims)
        self.assertNotIn("Version mentioned: 14.2.1.", claims)
        self.assertNotIn("Version mentioned: 5.15.146.1.", claims)
        self.assertNotIn("Version mentioned: 14.3.1.", claims)

    def test_markdown_linked_patch_versions_in_fix_prose_are_relevant(self):
        issue = Issue(
            "org",
            "core",
            2,
            "https://github.com/org/core/issues/2",
            "Patch release boundary",
            "the fix actually only made it into Python [3.11.9](https://example.test/a) "
            "and [3.12.3](https://example.test/b)",
        )
        claims = [item.claim for item in extract_evidence(issue) if item.category == "version"]
        self.assertIn("Version mentioned: 3.11.9.", claims)
        self.assertIn("Version mentioned: 3.12.3.", claims)

    def test_python_runtime_tokens_require_token_boundaries(self):
        issue = Issue(
            "org",
            "core",
            3,
            "https://github.com/org/core/issues/3",
            "Runtime matrix",
            "Python 3.12.4\nCPython 3.13\nPyPy 3.10\nlibvirt-python 10.3.0\nfoo-python 3.11",
        )
        claims = [item.claim for item in extract_evidence(issue) if item.category == "environment"]
        self.assertIn("Runtime mentioned: Python 3.12.4.", claims)
        self.assertIn("Runtime mentioned: CPython 3.13.", claims)
        self.assertIn("Runtime mentioned: PyPy 3.10.", claims)
        self.assertFalse(any("10.3.0" in claim for claim in claims))
        self.assertFalse(any("foo-python" in claim for claim in claims))

        version_claims = [item.claim for item in extract_evidence(issue) if item.category == "version"]
        self.assertNotIn("Version mentioned: 10.3.0.", version_claims)


if __name__ == "__main__":
    unittest.main()
