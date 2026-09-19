from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .github import GitHubError
from .report import render_report
from .retrieve import analyze_issue


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="issue-boundary-evidence",
        description="Produce a read-only Markdown boundary-evidence report for a public GitHub issue.",
    )
    parser.add_argument("issue_url", help="Public GitHub issue URL")
    parser.add_argument("-o", "--output", type=Path, help="Write Markdown to this file instead of stdout")
    parser.add_argument(
        "--related-limit",
        type=int,
        default=5,
        choices=range(0, 11),
        metavar="0..10",
        help="Maximum explicitly referenced same-repository issues/PRs to retrieve (default: 5)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        analysis = analyze_issue(args.issue_url, related_limit=args.related_limit)
        report = render_report(analysis)
    except (ValueError, GitHubError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

