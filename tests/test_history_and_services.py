import unittest
from unittest.mock import patch

from issue_boundary_evidence.extract import extract_evidence
from issue_boundary_evidence.models import Issue


class HistoryAndExternalServiceTests(unittest.TestCase):
    def test_contextual_commit_sha_becomes_same_repo_history_evidence(self):
        sha = "a6988aa0b92c93bfd397d6b788249488b8f5d300"
        issue = Issue(
            "pytest-dev",
            "pytest",
            1,
            "https://github.com/pytest-dev/pytest/issues/1",
            "Historical workaround",
            f"The workaround was introduced in commit {sha}.",
        )
        history = [item for item in extract_evidence(issue) if item.claim.startswith("Historical commit referenced:")]
        self.assertEqual(len(history), 1)
        self.assertIn(f"https://github.com/pytest-dev/pytest/commit/{sha}", history[0].claim)
        self.assertEqual(history[0].category, "version")

    def test_arbitrary_hash_is_not_history_evidence(self):
        issue = Issue(
            "org",
            "repo",
            1,
            "https://github.com/org/repo/issues/1",
            "Build data",
            "Checksum: a6988aa0b92c93bfd397d6b788249488b8f5d300",
        )
        self.assertFalse(any("Historical commit" in item.claim for item in extract_evidence(issue)))

    def test_environment_commit_field_is_not_history_evidence(self):
        sha = "d9cdd2ee5a58015ef6f4d15c7226110c9aab8140"
        issue = Issue(
            "org",
            "repo",
            1,
            "https://github.com/org/repo/issues/1",
            "Environment",
            f"INSTALLED VERSIONS\ncommit : {sha}\npython : 3.11.0",
        )
        self.assertFalse(any("Historical commit" in item.claim for item in extract_evidence(issue)))

    def test_commit_like_log_line_in_code_fence_is_not_history_evidence(self):
        issue = Issue(
            "org",
            "repo",
            1,
            "https://github.com/org/repo/issues/1",
            "Build log",
            "```text\ncommit a6988aa0b92c93bfd397d6b788249488b8f5d300\n```",
        )
        self.assertFalse(any("Historical commit" in item.claim for item in extract_evidence(issue)))

    @patch("urllib.request.urlopen", side_effect=AssertionError("external URLs must not be fetched"))
    def test_external_service_url_in_ci_context_becomes_boundary_without_fetching(self, mocked_urlopen):
        issue = Issue(
            "org",
            "repo",
            2,
            "https://github.com/org/repo/issues/2",
            "CI repository failure",
            "CI signature verification failed for repository metadata at https://packages.example.net/repo/repomd.xml.",
        )
        claims = [item.claim for item in extract_evidence(issue) if item.category == "boundary"]
        self.assertIn("Investigate external repository/service boundary: `packages.example.net`.", claims)
        mocked_urlopen.assert_not_called()


if __name__ == "__main__":
    unittest.main()
