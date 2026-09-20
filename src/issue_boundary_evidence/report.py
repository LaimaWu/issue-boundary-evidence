from __future__ import annotations

import re

from .models import Analysis, Evidence


SECTION_ORDER = (
    ("environment", "Environment facts"),
    ("boundary", "Boundary candidates"),
    ("version", "Version and regression clues"),
    ("related", "Related evidence"),
    ("gap", "Evidence gaps"),
)

MARKDOWN_CONTROL_CHARACTERS = frozenset("\\`*_{}[]()#!<>|~")
CANONICAL_GITHUB_SOURCE_URL_RE = re.compile(
    r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/"
    r"(?:issues|pull)/[1-9][0-9]*(?:#issuecomment-[1-9][0-9]*)?"
)


def _literal_text(value: str) -> str:
    """Render untrusted text inline without granting it Markdown or HTML structure."""
    normalized = re.sub(r"\s+", " ", value).strip()
    return "".join(
        f"\\{character}" if character in MARKDOWN_CONTROL_CHARACTERS else character
        for character in normalized
    )


def _source_link(label: str, url: str) -> str:
    """Link only canonical GitHub issue, pull-request, or issue-comment sources."""
    rendered_label = _literal_text(label)
    if CANONICAL_GITHUB_SOURCE_URL_RE.fullmatch(url):
        return f"[{rendered_label}]({url})"
    return f"{rendered_label} ({_literal_text(url)})"


def _render_item(item: Evidence) -> list[str]:
    lines = [f"- **{item.confidence.value}** — {_literal_text(item.claim)}"]
    for source in item.sources:
        lines.append(
            f"  - Source: {_source_link(source.kind, source.url)}, "
            f"{_literal_text(source.location)} — “{_literal_text(source.excerpt)}”"
        )
    return lines


def render_report(analysis: Analysis) -> str:
    issue = analysis.issue
    issue_label = f"{issue.owner}/{issue.repo}#{issue.number}"
    issue_link = _source_link(issue_label, issue.url)
    metadata_link = _source_link("issue metadata", issue.url)
    lines = [
        "# Issue Boundary Evidence",
        "",
        f"- Issue: {issue_link} (source kind: issue metadata)",
        f"- Title ({metadata_link}): {_literal_text(issue.title)}",
        f"- State at retrieval ({metadata_link}): {_literal_text(issue.state or 'unknown')}",
        "- Method: deterministic, read-only extraction from the issue and its comments",
        "",
    ]
    major = any(
        item.category in {"boundary", "version"} and item.confidence.value == "strong_clue"
        for item in analysis.evidence
    )
    if not major:
        lines.extend(["> No major boundary evidence found.", ""])

    for category, heading in SECTION_ORDER:
        lines.extend([f"## {heading}", ""])
        selected = [item for item in analysis.evidence if item.category == category]
        if selected:
            for item in selected:
                lines.extend(_render_item(item))
        else:
            lines.append("- No evidence extracted in this category.")
        lines.append("")

    lines.extend(["## Retrieved same-repository references", ""])
    if analysis.related_issues:
        for related in analysis.related_issues:
            related_label = f"{related.owner}/{related.repo}#{related.number}: {related.title}"
            lines.append(
                f"- **fact** — {_source_link(related_label, related.url)} "
                "(source kind: related issue metadata; structured location: title and "
                f"state={_literal_text(related.state)})"
            )
    else:
        lines.append("- No justified same-repository issue or pull-request references were retrieved.")
    lines.extend(
        [
            "",
            "## Interpretation guardrail",
            "",
            "Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.",
            "Issue text is untrusted and was never executed.",
            "",
        ]
    )
    return "\n".join(lines)
