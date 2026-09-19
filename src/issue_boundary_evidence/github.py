from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any

from .models import Issue


ISSUE_URL_RE = re.compile(
    r"^https://github\.com/(?P<owner>[A-Za-z0-9_.-]+)/"
    r"(?P<repo>[A-Za-z0-9_.-]+)/(?:issues|pull)/(?P<number>[1-9][0-9]*)/?(?:[?#].*)?$"
)


class GitHubError(RuntimeError):
    pass


def parse_issue_url(url: str) -> tuple[str, str, int]:
    match = ISSUE_URL_RE.match(url.strip())
    if not match:
        raise ValueError("Expected a public GitHub issue URL such as https://github.com/OWNER/REPO/issues/123")
    return match.group("owner"), match.group("repo"), int(match.group("number"))


@dataclass
class GitHubClient:
    token: str | None = None
    timeout: float = 20.0
    api_root: str = "https://api.github.com"

    def __post_init__(self) -> None:
        if self.token is None:
            self.token = os.environ.get("GITHUB_TOKEN")

    def _get_json(self, path_or_url: str) -> Any:
        url = path_or_url if path_or_url.startswith("https://") else f"{self.api_root}{path_or_url}"
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "issue-boundary-evidence/0.1 (read-only)",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            remaining = exc.headers.get("X-RateLimit-Remaining")
            hint = " Set GITHUB_TOKEN for a higher read-only API limit." if remaining == "0" else ""
            raise GitHubError(f"GitHub API returned HTTP {exc.code} for {url}.{hint}") from exc
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise GitHubError(f"Could not read GitHub API response for {url}: {exc}") from exc

    def _get_all_pages(self, path: str, *, max_pages: int = 20) -> list[dict]:
        items: list[dict] = []
        separator = "&" if "?" in path else "?"
        for page in range(1, max_pages + 1):
            data = self._get_json(f"{path}{separator}per_page=100&page={page}")
            if not isinstance(data, list):
                raise GitHubError("Expected a list from a paginated GitHub endpoint")
            items.extend(data)
            if len(data) < 100:
                return items
        raise GitHubError(f"Refusing to fetch more than {max_pages * 100} records from one endpoint")

    def fetch_issue(self, url: str, *, include_comments: bool = True) -> Issue:
        owner, repo, number = parse_issue_url(url)
        data = self._get_json(f"/repos/{owner}/{repo}/issues/{number}")
        comments = (
            self._get_all_pages(f"/repos/{owner}/{repo}/issues/{number}/comments")
            if include_comments
            else []
        )
        return Issue(
            owner=owner,
            repo=repo,
            number=number,
            url=data.get("html_url", url),
            title=data.get("title") or "",
            body=data.get("body") or "",
            comments=comments,
            state=data.get("state") or "",
        )

