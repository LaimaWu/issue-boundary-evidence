from __future__ import annotations

import re

from .extract import extract_evidence, extract_github_links, issue_documents, mask_code_fences
from .github import GitHubClient
from .models import Analysis, Issue


CONTEXTUAL_SHORT_REF_RE = re.compile(
    r"(?:\b(?:see|issue|pr|pull\s+request|change\s+in|related(?:\s+to)?|fixed\s+by|"
    r"fixed\s+in|fixes|regression\s+fix\s*:)\s*#(?P<prefix>[1-9][0-9]{0,8})\b|"
    r"(?<![\w])#(?P<suffix>[1-9][0-9]{0,8})\s+links?\s+to\b)",
    re.IGNORECASE,
)


def related_same_repo_urls(issue: Issue, *, limit: int = 5) -> list[str]:
    urls: list[str] = []
    seen_numbers = {issue.number}
    base = f"https://github.com/{issue.owner}/{issue.repo}"
    for doc in issue_documents(issue):
        for link in extract_github_links(doc.text):
            if (
                str(link["owner"]).casefold() == issue.owner.casefold()
                and str(link["repo"]).casefold() == issue.repo.casefold()
                and link["number"] is not None
                and int(link["number"]) not in seen_numbers
            ):
                seen_numbers.add(int(link["number"]))
                urls.append(str(link["url"]))
        prose = mask_code_fences(doc.text)
        for match in CONTEXTUAL_SHORT_REF_RE.finditer(prose):
            number = int(match.group("prefix") or match.group("suffix"))
            if number not in seen_numbers:
                seen_numbers.add(number)
                urls.append(f"{base}/issues/{number}")
        if len(urls) >= limit:
            break
    return urls[:limit]


def analyze_issue(url: str, client: GitHubClient | None = None, *, related_limit: int = 5) -> Analysis:
    client = client or GitHubClient()
    issue = client.fetch_issue(url, include_comments=True)
    evidence = extract_evidence(issue)
    related: list[Issue] = []
    for related_url in related_same_repo_urls(issue, limit=related_limit):
        candidate = client.fetch_issue(related_url, include_comments=False)
        related.append(candidate)
    return Analysis(issue=issue, evidence=evidence, related_issues=related)
