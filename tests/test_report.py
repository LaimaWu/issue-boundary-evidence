import unittest

from issue_boundary_evidence.models import Analysis, Confidence, Evidence, Issue, Source
from issue_boundary_evidence.report import render_report


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.issue = Issue(
            "org", "repo", 7, "https://github.com/org/repo/issues/7", "Example", "Plain report", state="open"
        )

    def test_preserves_provenance(self):
        source = Source(self.issue.url, "issue_body", "issue body", "Python 3.13 on Linux")
        report = render_report(Analysis(self.issue, [Evidence("environment", Confidence.FACT, "Runtime mentioned.", (source,))]))
        self.assertIn("https://github.com/org/repo/issues/7", report)
        self.assertIn("issue\\_body", report)
        self.assertIn("Python 3.13 on Linux", report)

    def test_no_major_evidence_path(self):
        source = Source(self.issue.url, "issue_body", "issue body", "Plain report")
        report = render_report(Analysis(self.issue, [Evidence("gap", Confidence.WEAK_CLUE, "Need confirmation.", (source,))]))
        self.assertIn("No major boundary evidence found.", report)

    def test_strong_boundary_suppresses_no_major_message(self):
        source = Source(self.issue.url, "issue_body", "issue body", "plugin interaction")
        report = render_report(Analysis(self.issue, [Evidence("boundary", Confidence.STRONG_CLUE, "Investigate plugin.", (source,))]))
        self.assertNotIn("No major boundary evidence found.", report)

    def test_untrusted_markdown_and_html_are_rendered_as_literal_text(self):
        payload = (
            "# heading > quote [link](https://example.invalid) "
            "![image](https://github.com/favicon.ico) <h1>raw</h1> "
            "<details open>details</details> <script>alert(1)</script> "
            "[unsafe](javascript:alert(1))"
        )
        issue = Issue(
            "org",
            "repo",
            7,
            self.issue.url,
            payload,
            "body",
            state="open",
        )
        source = Source(self.issue.url, "issue_body", payload, payload)
        related = Issue("org", "repo", 8, "https://github.com/org/repo/issues/8", payload, "", state="open")
        report = render_report(
            Analysis(
                issue,
                [Evidence("version", Confidence.STRONG_CLUE, payload, (source,))],
                [related],
            )
        )

        self.assertNotIn("\n# heading", report)
        self.assertNotIn("\n> quote", report)
        for unsafe_fragment in (
            "[link](https://example.invalid)",
            "![image](https://github.com/favicon.ico)",
            "<h1>",
            "<details open>",
            "<script>",
            "[unsafe](javascript:alert(1))",
        ):
            self.assertNotIn(unsafe_fragment, report)
        self.assertIn("\\# heading \\> quote", report)
        self.assertIn("\\[link\\]\\(https://example.invalid\\)", report)
        self.assertIn("\\!\\[image\\]\\(https://github.com/favicon.ico\\)", report)
        self.assertIn("\\<h1\\>raw\\</h1\\>", report)
        self.assertIn("\\<details open\\>details\\</details\\>", report)
        self.assertIn("\\<script\\>alert\\(1\\)\\</script\\>", report)
        self.assertIn("\\[unsafe\\]\\(javascript:alert\\(1\\)\\)", report)

    def test_ordinary_text_and_punctuation_remain_readable(self):
        source = Source(
            self.issue.url,
            "issue_body",
            "comment 2, line 4: observed",
            "Ordinary text, version 3.11: works (mostly).",
        )
        report = render_report(
            Analysis(
                self.issue,
                [Evidence("environment", Confidence.FACT, "Ordinary punctuation: clear, readable.", (source,))],
            )
        )

        self.assertIn("Ordinary punctuation: clear, readable.", report)
        self.assertIn("comment 2, line 4: observed", report)
        self.assertIn("Ordinary text, version 3.11: works \\(mostly\\).", report)

    def test_canonical_github_source_links_remain_clickable(self):
        source = Source(
            "https://github.com/org/repo/issues/7#issuecomment-11",
            "issue_comment",
            "comment 1",
            "Canonical source",
        )
        related = Issue(
            "org",
            "repo",
            8,
            "https://github.com/org/repo/pull/8",
            "Related title",
            "",
            state="closed",
        )
        report = render_report(
            Analysis(
                self.issue,
                [Evidence("related", Confidence.FACT, "Linked source.", (source,))],
                [related],
            )
        )

        self.assertIn(
            "[issue\\_comment](https://github.com/org/repo/issues/7#issuecomment-11)",
            report,
        )
        self.assertIn("(https://github.com/org/repo/pull/8)", report)
        self.assertIn("(https://github.com/org/repo/issues/7)", report)

    def test_noncanonical_and_unsafe_source_urls_are_not_linked(self):
        javascript_source = Source(
            "javascript:alert(1)",
            "issue_body",
            "issue body",
            "Unsafe scheme",
        )
        external_source = Source(
            "https://example.invalid/issue/7",
            "issue_body",
            "issue body",
            "External source",
        )
        report = render_report(
            Analysis(
                self.issue,
                [
                    Evidence("gap", Confidence.FACT, "Unsafe source.", (javascript_source,)),
                    Evidence("gap", Confidence.FACT, "External source.", (external_source,)),
                ],
            )
        )

        self.assertNotIn("](javascript:", report)
        self.assertNotIn("](https://example.invalid", report)
        self.assertIn("javascript:alert\\(1\\)", report)
        self.assertIn("https://example.invalid/issue/7", report)


if __name__ == "__main__":
    unittest.main()
