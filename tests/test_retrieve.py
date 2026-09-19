import unittest

from issue_boundary_evidence.models import Issue
from issue_boundary_evidence.retrieve import related_same_repo_urls


class RetrievalSelectionTests(unittest.TestCase):
    def test_only_same_repo_references_are_selected(self):
        issue = Issue(
            "org",
            "repo",
            10,
            "https://github.com/org/repo/issues/10",
            "Related references",
            "See #11, https://github.com/org/repo/pull/12, and https://github.com/other/repo/issues/99.",
        )
        self.assertEqual(
            related_same_repo_urls(issue),
            ["https://github.com/org/repo/pull/12", "https://github.com/org/repo/issues/11"],
        )

    def _urls_for(self, body):
        issue = Issue("org", "repo", 99, "https://github.com/org/repo/issues/99", "Example", body)
        return related_same_repo_urls(issue, limit=10)

    def test_environment_kernel_number_is_not_a_reference(self):
        self.assertEqual(self._urls_for("Version : #1 SMP Thu Jan 4"), [])

    def test_arbitrary_bare_number_is_not_a_reference(self):
        self.assertEqual(self._urls_for("I tried #1 and then option #2."), [])

    def test_contextual_prefix_references_are_accepted(self):
        self.assertEqual(
            self._urls_for("change in #12368. Regression fix: #12471."),
            ["https://github.com/org/repo/issues/12368", "https://github.com/org/repo/issues/12471"],
        )

    def test_contextual_suffix_reference_is_accepted(self):
        self.assertEqual(
            self._urls_for("#8796 links to the historical workaround."),
            ["https://github.com/org/repo/issues/8796"],
        )

    def test_reference_inside_code_fence_is_ignored(self):
        self.assertEqual(self._urls_for("```text\nsee #123\n```"), [])


if __name__ == "__main__":
    unittest.main()
