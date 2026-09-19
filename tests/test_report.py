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
        self.assertIn("issue_body", report)
        self.assertIn("Python 3.13 on Linux", report)

    def test_no_major_evidence_path(self):
        source = Source(self.issue.url, "issue_body", "issue body", "Plain report")
        report = render_report(Analysis(self.issue, [Evidence("gap", Confidence.WEAK_CLUE, "Need confirmation.", (source,))]))
        self.assertIn("No major boundary evidence found.", report)

    def test_strong_boundary_suppresses_no_major_message(self):
        source = Source(self.issue.url, "issue_body", "issue body", "plugin interaction")
        report = render_report(Analysis(self.issue, [Evidence("boundary", Confidence.STRONG_CLUE, "Investigate plugin.", (source,))]))
        self.assertNotIn("No major boundary evidence found.", report)


if __name__ == "__main__":
    unittest.main()

