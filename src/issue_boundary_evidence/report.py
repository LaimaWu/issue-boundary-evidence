from __future__ import annotations

from .models import Analysis, Evidence


SECTION_ORDER = (
    ("environment", "Environment facts"),
    ("boundary", "Boundary candidates"),
    ("version", "Version and regression clues"),
    ("related", "Related evidence"),
    ("gap", "Evidence gaps"),
)


def _render_item(item: Evidence) -> list[str]:
    lines = [f"- **{item.confidence.value}** — {item.claim}"]
    for source in item.sources:
        excerpt = source.excerpt.replace("\n", " ").replace("|", "\\|")
        lines.append(
            f"  - Source: [{source.kind}]({source.url}), {source.location} — “{excerpt}”"
        )
    return lines


def render_report(analysis: Analysis) -> str:
    issue = analysis.issue
    lines = [
        "# Issue Boundary Evidence",
        "",
        f"- Issue: [{issue.owner}/{issue.repo}#{issue.number}]({issue.url}) (source kind: issue metadata)",
        f"- Title ([issue metadata]({issue.url})): {issue.title}",
        f"- State at retrieval ([issue metadata]({issue.url})): {issue.state or 'unknown'}",
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
            lines.append(
                f"- **fact** — [{related.owner}/{related.repo}#{related.number}: {related.title}]({related.url}) "
                f"(source kind: related issue metadata; structured location: title and state={related.state})"
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
