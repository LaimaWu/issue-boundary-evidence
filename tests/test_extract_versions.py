import unittest

from issue_boundary_evidence.extract import extract_evidence, extract_regression_phrases, extract_versions
from issue_boundary_evidence.models import Issue


class VersionExtractionTests(unittest.TestCase):
    def _version_claims(self, body):
        issue = Issue(
            "example-org",
            "example-project",
            40,
            "https://github.com/example-org/example-project/issues/40",
            "History check",
            body,
        )
        return [item.claim for item in extract_evidence(issue) if item.category == "version"]

    def _regression_claims(self, body):
        return [claim for claim in self._version_claims(body) if claim.startswith("Version or regression language:")]

    def test_add_regression_test_prose_is_not_history_evidence(self):
        self.assertEqual(self._regression_claims("Add a regression test for this bug."), [])

    def test_regression_test_version_without_transition_is_not_version_evidence(self):
        self.assertEqual(self._version_claims("Add a regression test for version 5.6."), [])

    def test_non_regression_test_prose_is_not_history_evidence(self):
        self.assertEqual(self._regression_claims("This is a non-regression test."), [])

    def test_fix_includes_regression_tests_is_not_history_evidence(self):
        self.assertEqual(self._regression_claims("The fix includes regression tests."), [])

    def test_tests_added_to_prevent_regression_are_not_history_evidence(self):
        self.assertEqual(self._regression_claims("Tests were added to prevent regression."), [])

    def test_explicit_before_after_versions_remain_history_evidence(self):
        claims = self._version_claims("This worked in 1.2 but fails in 1.3.")
        self.assertTrue(any(claim.startswith("Version or regression language:") for claim in claims))
        self.assertIn("Version mentioned: 1.2.", claims)
        self.assertIn("Version mentioned: 1.3.", claims)

    def test_stopped_working_after_upgrade_remains_history_evidence(self):
        claims = self._version_claims("It stopped working after upgrading to 2.0.")
        self.assertTrue(any(claim.startswith("Version or regression language:") for claim in claims))
        self.assertIn("Version mentioned: 2.0.", claims)

    def test_introduced_and_fixed_versions_remain_history_evidence(self):
        claims = self._version_claims("Introduced in 3.4.1 and fixed in 3.4.2.")
        self.assertTrue(any(claim.startswith("Version or regression language:") for claim in claims))
        self.assertIn("Version mentioned: 3.4.1.", claims)
        self.assertIn("Version mentioned: 3.4.2.", claims)

    def test_historical_workaround_tied_to_version_remains_history_evidence(self):
        claims = self._version_claims("A workaround became necessary after version 5.0.")
        self.assertTrue(any(claim.startswith("Version or regression language:") for claim in claims))
        self.assertIn("Version mentioned: 5.0.", claims)

    def test_generic_worked_prose_is_not_history_evidence(self):
        self.assertEqual(
            self._regression_claims("The documentation example worked with a custom formatter during this test."),
            [],
        )
        self.assertEqual(self._regression_claims("The contributor worked before lunch on a custom formatter."), [])

    def test_contextual_project_version_extraction_remains_intact(self):
        claims = self._version_claims("example-project version: 4.5.0")
        self.assertIn("Version mentioned: 4.5.0.", claims)
        self.assertFalse(any(claim.startswith("Version or regression language:") for claim in claims))

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
