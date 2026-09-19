import unittest

from issue_boundary_evidence.extract import extract_evidence
from issue_boundary_evidence.models import Confidence, Evidence, Issue


class ConfidenceTests(unittest.TestCase):
    def test_import_only_package_is_not_a_strong_boundary(self):
        issue = Issue(
            "example-org",
            "host-project",
            20,
            "https://github.com/example-org/host-project/issues/20",
            "Adapter failure",
            "Reproducer:\nimport helperlib\nThe host plugin integration is incompatible.",
        )
        clues = [item for item in extract_evidence(issue) if item.category == "boundary" and "helperlib" in item.claim]
        self.assertFalse(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_environment_only_package_is_not_a_strong_boundary(self):
        issue = Issue(
            "example-org",
            "host-project",
            21,
            "https://github.com/example-org/host-project/issues/21",
            "Environment details",
            "Package: samplelib\nThe host plugin integration is incompatible.",
        )
        clues = [item for item in extract_evidence(issue) if item.category == "boundary" and "samplelib" in item.claim]
        self.assertFalse(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_pytest_command_is_not_a_strong_boundary(self):
        issue = Issue(
            "example-org",
            "host-project",
            22,
            "https://github.com/example-org/host-project/issues/22",
            "Test failure",
            "Run `python -m pytest -q tests/widget_test.py`. The adapter plugin integration is incompatible.",
        )
        clues = [item for item in extract_evidence(issue) if item.category == "boundary" and "`pytest`" in item.claim]
        self.assertFalse(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_stdlib_import_is_not_an_external_strong_boundary(self):
        issue = Issue(
            "example-org",
            "host-project",
            23,
            "https://github.com/example-org/host-project/issues/23",
            "Plugin regression",
            "import json\nThe adapter plugin regression is under investigation.",
        )
        clues = [item for item in extract_evidence(issue) if item.category == "boundary" and "`json`" in item.claim]
        self.assertFalse(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_comparison_repository_link_is_not_a_strong_boundary(self):
        issue = Issue(
            "example-org",
            "host-project",
            24,
            "https://github.com/example-org/host-project/issues/24",
            "Comparison",
            "For comparison, see the failing example at https://github.com/reference-org/reference-project.",
        )
        clues = [
            item
            for item in extract_evidence(issue)
            if item.category == "boundary" and "reference-org/reference-project" in item.claim
        ]
        self.assertFalse(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_personal_fork_commit_link_is_not_a_strong_boundary(self):
        sha = "34567890abcdef1234567890abcdef1234567890"
        issue = Issue(
            "example-org",
            "host-project",
            28,
            "https://github.com/example-org/host-project/issues/28",
            "Patch reference",
            f"Patch provenance: https://github.com/contributor-user/personal-fork/commit/{sha}.",
        )
        clues = [
            item
            for item in extract_evidence(issue)
            if item.category == "boundary" and "contributor-user/personal-fork" in item.claim
        ]
        self.assertFalse(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_fork_branch_with_regression_tests_is_not_a_strong_boundary(self):
        issue = Issue(
            "example-org",
            "host-project",
            29,
            "https://github.com/example-org/host-project/issues/29",
            "Patch reference",
            "A fix and regression tests are prepared on fork branch "
            "https://github.com/contributor-user/personal-fork/tree/fix-branch.",
        )
        clues = [
            item
            for item in extract_evidence(issue)
            if item.category == "boundary" and "contributor-user/personal-fork" in item.claim
        ]
        self.assertFalse(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_package_only_in_code_expression_is_not_a_strong_boundary(self):
        issue = Issue(
            "example-org",
            "host-project",
            30,
            "https://github.com/example-org/host-project/issues/30",
            "Output failure",
            'Package: samplelib\nThe call `set_mode(target="samplelib")` is broken.',
        )
        clues = [item for item in extract_evidence(issue) if item.category == "boundary" and "samplelib" in item.claim]
        self.assertFalse(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_ordinary_worked_on_package_prose_is_not_a_strong_boundary(self):
        issue = Issue(
            "example-org",
            "host-project",
            31,
            "https://github.com/example-org/host-project/issues/31",
            "Contributor background",
            "Package: samplelib\nI worked on tools like samplelib in earlier projects.",
        )
        clues = [item for item in extract_evidence(issue) if item.category == "boundary" and "samplelib" in item.claim]
        self.assertFalse(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_explicit_plugin_integration_incompatibility_is_strong(self):
        issue = Issue(
            "example-org",
            "host-project",
            25,
            "https://github.com/example-org/host-project/issues/25",
            "Plugin incompatibility",
            "import bridge_plugin\nbridge_plugin is incompatible with the host integration.",
        )
        clues = [item for item in extract_evidence(issue) if item.category == "boundary" and "bridge_plugin" in item.claim]
        self.assertTrue(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_explicit_external_package_regression_is_strong(self):
        issue = Issue(
            "example-org",
            "host-project",
            26,
            "https://github.com/example-org/host-project/issues/26",
            "Dependency regression",
            "import fluxwidget\nfluxwidget regressed after upgrading fluxwidget.",
        )
        clues = [item for item in extract_evidence(issue) if item.category == "boundary" and "fluxwidget" in item.claim]
        self.assertTrue(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_explicit_upstream_responsibility_statement_is_strong(self):
        issue = Issue(
            "example-org",
            "host-project",
            27,
            "https://github.com/example-org/host-project/issues/27",
            "Upstream ownership",
            "The root cause belongs upstream in https://github.com/upstream-org/upstream-project/issues/41.",
        )
        clues = [
            item
            for item in extract_evidence(issue)
            if item.category == "boundary" and "upstream-org/upstream-project" in item.claim
        ]
        self.assertTrue(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_enum_has_only_allowed_values(self):
        self.assertEqual(
            {value.value for value in Confidence},
            {"fact", "strong_clue", "weak_clue"},
        )

    def test_repeated_plugin_is_a_strong_clue(self):
        issue = Issue(
            "org",
            "core",
            1,
            "https://github.com/org/core/issues/1",
            "Plugin integration regression",
            "pytest-rerunfailures stopped working after upgrading.",
            [{"html_url": "https://github.com/org/core/issues/1#issuecomment-1", "body": "This may involve pytest-rerunfailures hooks."}],
        )
        clues = [item for item in extract_evidence(issue) if "pytest-rerunfailures" in item.claim]
        self.assertTrue(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_repeated_incidental_package_is_not_a_strong_clue(self):
        issue = Issue(
            "org",
            "core",
            3,
            "https://github.com/org/core/issues/3",
            "Unexpected result",
            "pandas is installed. pandas appears in the environment.",
            [{"html_url": "https://github.com/org/core/issues/3#issuecomment-1", "body": "I also have pandas installed."}],
        )
        clues = [item for item in extract_evidence(issue) if item.category == "boundary" and "pandas" in item.claim]
        self.assertFalse(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_evidence_requires_provenance(self):
        with self.assertRaises(ValueError):
            Evidence("boundary", Confidence.WEAK_CLUE, "unsupported", ())

    def test_free_threading_is_a_runtime_boundary(self):
        issue = Issue(
            "org",
            "core",
            2,
            "https://github.com/org/core/issues/2",
            "Crash on Python free-threading build",
            "The cp313t ABI tag is installed.",
        )
        claims = [item.claim for item in extract_evidence(issue) if item.category == "boundary"]
        self.assertIn("Investigate the free-threading/no-GIL runtime boundary.", claims)
        self.assertIn("Investigate the wheel/ABI packaging boundary.", claims)

    def test_plain_wheel_version_in_environment_is_not_packaging_boundary(self):
        issue = Issue(
            "org",
            "core",
            4,
            "https://github.com/org/core/issues/4",
            "Environment report",
            "setuptools 70.0.0 wheel 0.43.0 urllib3 2.1.0",
        )
        claims = [item.claim for item in extract_evidence(issue) if item.category == "boundary"]
        self.assertNotIn("Investigate the wheel/ABI packaging boundary.", claims)
        self.assertFalse(any("setuptools" in claim for claim in claims))

    def test_external_package_in_issue_title_is_a_strong_clue(self):
        issue = Issue(
            "org",
            "numpy",
            5,
            "https://github.com/org/numpy/issues/5",
            "Incorrect results when used with joblib",
            "Minimal reproduction attached.",
        )
        clues = [item for item in extract_evidence(issue) if item.category == "boundary" and "joblib" in item.claim]
        self.assertTrue(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_generic_pip_install_near_ci_regression_is_not_strong(self):
        issue = Issue(
            "org",
            "core",
            6,
            "https://github.com/org/core/issues/6",
            "CI regression",
            "In CI run `pip install core==2.0` before executing the tests.",
        )
        clues = [item for item in extract_evidence(issue) if item.category == "boundary" and "`pip`" in item.claim]
        self.assertFalse(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_pip_version_controlling_correct_abi_wheel_is_strong(self):
        issue = Issue(
            "org",
            "core",
            7,
            "https://github.com/org/core/issues/7",
            "Wrong free-threaded wheel",
            "Which pip version is used? pip 24.0 installs the wrong wheel without the cp313t ABI tag.",
        )
        clues = [item for item in extract_evidence(issue) if item.category == "boundary" and "`pip`" in item.claim]
        self.assertTrue(any(item.confidence is Confidence.STRONG_CLUE for item in clues))

    def test_quoted_regression_phrase_is_deduplicated(self):
        sentence = "This worked in version 1.0 before upgrading."
        issue = Issue(
            "org",
            "core",
            8,
            "https://github.com/org/core/issues/8",
            "Example",
            sentence,
            [{"html_url": "https://github.com/org/core/issues/8#issuecomment-1", "body": f"> {sentence}"}],
        )
        clues = [
            item
            for item in extract_evidence(issue)
            if item.category == "version" and item.claim.startswith("Version or regression language:")
        ]
        self.assertEqual(len(clues), 1)
        self.assertEqual(len(clues[0].sources), 2)


if __name__ == "__main__":
    unittest.main()
