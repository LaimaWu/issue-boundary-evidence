import unittest

from issue_boundary_evidence.extract import extract_github_links
from issue_boundary_evidence.github import parse_issue_url


class GitHubLinkTests(unittest.TestCase):
    def test_parse_issue_url(self):
        self.assertEqual(
            parse_issue_url("https://github.com/example/project/issues/123"),
            ("example", "project", 123),
        )

    def test_extracts_issue_pull_and_repo_links(self):
        links = extract_github_links(
            "See https://github.com/org/repo/issues/12 and https://github.com/other/tool/pull/3. "
            "Source at https://github.com/acme/widget/blob/main/a.py."
        )
        self.assertEqual([(item["repo"], item["number"]) for item in links], [("repo", 12), ("tool", 3), ("widget", None)])

    def test_extracts_repository_number_shorthand(self):
        links = extract_github_links("The upstream fix is python/cpython#61648.")
        self.assertEqual(
            links,
            [{
                "url": "https://github.com/python/cpython/issues/61648",
                "owner": "python",
                "repo": "cpython",
                "kind": "issues",
                "number": 61648,
            }],
        )

    def test_user_attachment_is_not_treated_as_repository(self):
        self.assertEqual(
            extract_github_links("https://github.com/user-attachments/files/12345/report.txt"),
            [],
        )

    def test_rejects_non_issue_urls_as_input(self):
        with self.assertRaises(ValueError):
            parse_issue_url("https://example.com/org/repo/issues/1")


if __name__ == "__main__":
    unittest.main()
