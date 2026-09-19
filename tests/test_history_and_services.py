import unittest
from unittest.mock import patch

from issue_boundary_evidence.extract import extract_evidence
from issue_boundary_evidence.models import Issue


class HistoryAndExternalServiceTests(unittest.TestCase):
    def test_external_commit_url_preserves_original_repository_and_url(self):
        sha = "0123456789abcdef0123456789abcdef01234567"
        external_url = f"https://github.com/fork-owner/fork-repo/commit/{sha}"
        issue = Issue(
            "issue-owner",
            "issue-repo",
            1,
            "https://github.com/issue-owner/issue-repo/issues/1",
            "Upstream fix",
            f"The fix landed in {external_url}.",
        )

        history = [item for item in extract_evidence(issue) if item.claim.startswith("Historical commit referenced:")]

        self.assertEqual(len(history), 1)
        self.assertEqual(history[0].claim, f"Historical commit referenced: [{sha}]({external_url}).")
        self.assertNotIn(f"https://github.com/issue-owner/issue-repo/commit/{sha}", history[0].claim)

    def test_external_commit_url_with_short_display_sha_uses_full_target(self):
        full_sha = "fedcba9876543210fedcba9876543210fedcba98"
        short_sha = full_sha[:8]
        external_url = f"https://github.com/example-contributor/example-fork/commit/{full_sha}"
        issue = Issue(
            "example-org",
            "example-project",
            2,
            "https://github.com/example-org/example-project/issues/2",
            "Linked fix",
            f"Fixed by [{short_sha}]({external_url}).",
        )

        history = [item for item in extract_evidence(issue) if item.claim.startswith("Historical commit referenced:")]

        self.assertEqual(len(history), 1)
        self.assertEqual(history[0].claim, f"Historical commit referenced: [{full_sha}]({external_url}).")
        self.assertFalse(any("example-org/example-project/commit" in item.claim for item in history))

    def test_external_commit_target_suppresses_attached_bare_sha_fact(self):
        full_sha = "abcdef0123456789abcdef0123456789abcdef01"
        short_sha = full_sha[:9]
        external_url = f"https://github.com/contributor/forked-project/commit/{full_sha}"
        issue = Issue(
            "main-org",
            "main-project",
            3,
            "https://github.com/main-org/main-project/issues/3",
            "External fix",
            f"Fixed in commit {short_sha} ({external_url}).",
        )

        history = [item for item in extract_evidence(issue) if item.claim.startswith("Historical commit referenced:")]

        self.assertEqual(len(history), 1)
        self.assertEqual(history[0].claim, f"Historical commit referenced: [{full_sha}]({external_url}).")

    def test_checksum_commit_url_is_not_history_evidence(self):
        sha = "234567890abcdef1234567890abcdef123456789"
        external_url = f"https://github.com/archive-owner/archive-repo/commit/{sha}"
        issue = Issue(
            "product-org",
            "product-repo",
            4,
            "https://github.com/product-org/product-repo/issues/4",
            "Artifact checksum",
            f"Checksum: {external_url}",
        )

        history = [item for item in extract_evidence(issue) if item.claim.startswith("Historical commit referenced:")]

        self.assertEqual(history, [])

    def test_sha_in_external_non_commit_url_does_not_create_history_evidence(self):
        sha = "1234567890abcdef1234567890abcdef12345678"
        issue = Issue(
            "sample-org",
            "sample-project",
            3,
            "https://github.com/sample-org/sample-project/issues/3",
            "Fork comparison",
            f"The regression was compared in https://github.com/sample-user/sample-fork/compare/main...{sha}.",
        )

        history = [item for item in extract_evidence(issue) if item.claim.startswith("Historical commit referenced:")]

        self.assertEqual(history, [])

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
