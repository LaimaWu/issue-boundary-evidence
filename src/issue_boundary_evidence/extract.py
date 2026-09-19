from __future__ import annotations

import re
import urllib.parse
from collections import defaultdict

from .models import Confidence, Document, Evidence, Issue, Source


GITHUB_LINK_RE = re.compile(
    r"https://github\.com/(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)"
    r"(?:/(?P<kind>issues|pull)/(?P<number>\d+)|(?P<path>/[^\s)>\]}`,'\"]*))?",
    re.IGNORECASE,
)
GITHUB_REPO_REF_RE = re.compile(
    r"(?<![\w./-])(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)#(?P<number>[1-9][0-9]*)\b"
)
GITHUB_RESERVED_ROOTS = {
    "assets",
    "collections",
    "features",
    "issues",
    "login",
    "marketplace",
    "notifications",
    "organizations",
    "orgs",
    "pulls",
    "search",
    "settings",
    "sponsors",
    "topics",
    "user-attachments",
}
VERSION_RE = re.compile(
    r"(?<![\w/])v?\d+(?:\.\d+){1,3}(?:[-+._]?(?:a|b|alpha|beta|rc|dev|post)\d+)?(?![\w/])",
    re.IGNORECASE,
)
PYTHON_RE = re.compile(
    r"(?<![\w.-])(?:Python|CPython|PyPy)(?![\w.-])(?:\s+version\s*[:=]?\s*|\s*[:=]\s*|\s+)"
    r"v?(\d+(?:\.\d+){1,3}(?:a|b|rc|dev|post)?\d*)\b",
    re.I,
)
ABI_RE = re.compile(r"\b(?:cp\d{2,3}t?|abi3|manylinux(?:_\d+_\d+)?|musllinux(?:_\d+_\d+)?)\b", re.I)
OS_RE = re.compile(
    r"\b(Windows(?:\s+\d+)?|macOS|Mac OS X|Linux|Ubuntu(?:\s+\d+(?:\.\d+)*)?|"
    r"Debian|Fedora|OpenSUSE(?:\s+Tumbleweed)?|Alpine|FreeBSD|WSL)\b",
    re.I,
)
STACK_MODULE_RE = re.compile(
    r"(?:File\s+[\"'][^\"']*(?:site-packages|dist-packages)[/\\]([^/\\\"']+)|"
    r"File\s+[\"'][^\"']*[/\\]([A-Za-z_][\w]*)\.(?:py|pyx)[\"']|"
    r"\b([A-Za-z_][\w.]*)\.(?:py|pyx):\d+)",
    re.I,
)
IMPORT_RE = re.compile(r"(?m)^\s*(?:from\s+([A-Za-z_][\w.]*)\s+import|import\s+([A-Za-z_][\w.]*))")
PACKAGE_ASSIGNMENT_RE = re.compile(
    r"(?im)^\s*(?:package|plugin|dependency|library|backend|runtime)\s*(?:name)?\s*[:=]\s*[`'\"]?([A-Za-z][\w.-]{1,60})"
)
INSTALL_RE = re.compile(r"\b(?:pip|pip3|conda|uv)\s+install\s+([A-Za-z][\w.-]{1,60})", re.I)
PACKAGE_WORD_RE = re.compile(
    r"\b(pytest-[a-z0-9_.-]+|[a-z0-9_.-]+-plugin|awkward_pandas|awkward-pandas|"
    r"OpenBLAS|MKL|joblib|pip|setuptools|wheel|CPython|PyPy|NumPy|pandas|pytest)\b",
    re.I,
)
REGRESSION_TERMS = re.compile(
    r"\b(regression|regressed|worked? (?:on|in|with|before)|used to work|no longer works?|"
    r"since (?:upgrading|updating|version)|older versions?|previous versions?|after (?:upgrading|updating)|"
    r"introduced in|fixed in|will be fixed|next release|workaround|behavior change[ds]?)\b",
    re.I,
)
UNCERTAINTY_TERMS = re.compile(
    r"\b(not sure (?:where|whether|if)|unsure (?:where|whether|if)|which (?:project|repo|package)|"
    r"belongs? (?:here|upstream)|report (?:this )?(?:here|upstream)|cannot reproduce|can't reproduce|"
    r"unable to reproduce|need more (?:information|details)|insufficient information)\b",
    re.I,
)
BOUNDARY_TERMS = re.compile(
    r"\b(plugin|dependency|upstream|downstream|runtime|backend|ABI|wheel|hook|integration|"
    r"third[- ]party|external|free[- ]thread|no[- ]GIL|threading|parallel|repository|CI)\b",
    re.I,
)
RUNTIME_BOUNDARY_RE = re.compile(
    r"\b(free[- ]thread(?:ed|ing)?|no[- ]GIL|GIL[- ]disabled|ABI(?:\s+tag)?|"
    r"wheel(?:\s+tag)?|shared librar(?:y|ies)|binary compatibility)\b",
    re.I,
)
EXTERNAL_URL_RE = re.compile(r"https?://[^\s<>\]})`'\"]+", re.I)
INFRASTRUCTURE_TERMS = re.compile(
    r"\b(CI|continuous integration|package repositor(?:y|ies)|repository|registry|package index|"
    r"signature(?: verification)?|download server|external service|repository metadata|repomd\.xml)\b",
    re.I,
)
HISTORY_SHA_RE = re.compile(
    r"\b(?:commit|introduced(?:\s+(?:in|by))?|bisected(?:\s+to)?|first\s+occurred(?:\s+in)?|"
    r"link(?:ed|s)?(?:\s+to)?|regression(?:\s+from)?|workaround\s+(?:was\s+)?introduced(?:\s+by)?|"
    r"added(?:\s+in)?|dates?\s+back\s+to)\b"
    r"(?:(?!\n\s*\n).){0,100}?\b(?P<sha>[0-9a-f]{7,40})\b",
    re.IGNORECASE,
)
VERSION_RELEVANCE_TERMS = re.compile(
    r"\b(regression|regressed|compatib(?:le|ility)|incompatib(?:le|ility)|supported?|requires?|"
    r"before|after|upgrade[ds]?|updat(?:e|ed|ing)|fixed|breaks?|broken|works?|fails?)\b",
    re.I,
)
PACKAGING_CONTEXT_RE = re.compile(
    r"\b(correct wheel|wheel\s+(?:tag|build|file|for)|build(?:ing|s|t)?\s+(?:a\s+)?wheel|"
    r"install(?:ing|s|ed)?[^.\n]{0,50}\bwheel|ABI(?:\s+tag)?|free[- ]thread(?:ed|ing)?|"
    r"binary compatibility|normal ABI)\b",
    re.I,
)
RELEASE_VERSION_CONTEXT_RE = re.compile(
    r"\b(fix(?:\s+actually)?\s+only\s+made\s+it\s+into|fix\s+made\s+it\s+into|"
    r"fix\s+landed\s+in|released\s+in|available\s+in|patch\s+release|fixed\s+as\s+of|"
    r"shipped\s+in)\b",
    re.I,
)
PACKAGING_TOOL_KEYS = {"pip", "setuptools", "wheel"}
PIP_INVESTIGATION_RE = re.compile(
    r"\b(?:which|what)\s+pip\s+version\b|\bpip\s+version\b|"
    r"\bpip\b[^.\n]{0,100}\b(?:correct|wrong|normal|free[- ]threaded)\s+wheel\b|"
    r"\b(?:correct|wrong|normal|free[- ]threaded)\s+wheel\b[^.\n]{0,100}\bpip\b|"
    r"\bpip\b[^.\n]{0,100}\b(?:ABI(?:\s+tag)?|cp\d{2,3}t|wheel\s+tag)\b",
    re.I,
)
SETUPTOOLS_INVESTIGATION_RE = re.compile(
    r"\bsetuptools\b[^.\n]{0,100}\b(?:behavior|check|support|version|responsib|work(?:s|ing)?)\b|"
    r"\b(?:behavior|check|support|version|responsib)\b[^.\n]{0,100}\bsetuptools\b",
    re.I,
)
CODE_FENCE_RE = re.compile(r"```.*?```", re.S)


def mask_code_fences(text: str) -> str:
    """Hide fenced code while preserving offsets for contextual prose parsing."""
    return CODE_FENCE_RE.sub(lambda match: " " * (match.end() - match.start()), text)


def issue_documents(issue: Issue) -> list[Document]:
    docs = [
        Document(issue.url, "issue_title", "issue title", issue.title),
        Document(issue.url, "issue_body", "issue body", issue.body),
    ]
    for index, comment in enumerate(issue.comments, start=1):
        docs.append(
            Document(
                comment.get("html_url") or f"{issue.url}#issuecomment-{comment.get('id', index)}",
                "issue_comment",
                f"comment {index}",
                comment.get("body") or "",
            )
        )
    return docs


def _sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+|\s*\n\s*", text) if part.strip()]


def _excerpt(text: str, start: int = 0, end: int | None = None, limit: int = 240) -> str:
    if end is None:
        end = min(len(text), start + limit)
    left = max(0, start - 80)
    right = min(len(text), end + 100)
    clean = re.sub(r"\s+", " ", text[left:right]).strip()
    if len(clean) > limit:
        clean = clean[: limit - 1].rstrip() + "…"
    return clean


def _source(doc: Document, match: re.Match[str] | None = None, excerpt: str | None = None) -> Source:
    if excerpt is None:
        excerpt = _excerpt(doc.text, match.start() if match else 0, match.end() if match else None)
    return Source(doc.url, doc.kind, doc.location, excerpt)


def _line_at(text: str, start: int) -> str:
    left = text.rfind("\n", 0, start) + 1
    right = text.find("\n", start)
    if right < 0:
        right = len(text)
    return text[left:right].strip()


def _context_at(text: str, start: int, end: int, radius: int = 220) -> str:
    return re.sub(r"\s+", " ", text[max(0, start - radius) : min(len(text), end + radius)]).strip()


def extract_versions(text: str) -> list[str]:
    return list(dict.fromkeys(match.group(0).lstrip("vV").rstrip(".,;:") for match in VERSION_RE.finditer(text)))


def extract_github_links(text: str) -> list[dict[str, str | int | None]]:
    links: list[dict[str, str | int | None]] = []
    seen: set[str] = set()
    for match in GITHUB_LINK_RE.finditer(text):
        if match.group("owner").casefold() in GITHUB_RESERVED_ROOTS:
            continue
        url = match.group(0).rstrip(".,;:")
        if url in seen:
            continue
        seen.add(url)
        links.append(
            {
                "url": url,
                "owner": match.group("owner"),
                "repo": match.group("repo"),
                "kind": match.group("kind"),
                "number": int(match.group("number")) if match.group("number") else None,
            }
        )
    for match in GITHUB_REPO_REF_RE.finditer(text):
        url = f"https://github.com/{match.group('owner')}/{match.group('repo')}/issues/{match.group('number')}"
        if url in seen:
            continue
        seen.add(url)
        links.append(
            {
                "url": url,
                "owner": match.group("owner"),
                "repo": match.group("repo"),
                "kind": "issues",
                "number": int(match.group("number")),
            }
        )
    return links


def extract_stack_modules(text: str) -> list[str]:
    modules: list[str] = []
    for match in STACK_MODULE_RE.finditer(text):
        value = next((group for group in match.groups() if group), "")
        root = re.split(r"[./\\]", value)[0]
        if root and root.lower() not in {"file", "line", "self", "test", "tests"}:
            modules.append(root)
    return list(dict.fromkeys(modules))


def extract_packages(text: str) -> list[str]:
    packages: list[str] = []
    for regex in (IMPORT_RE, PACKAGE_ASSIGNMENT_RE, INSTALL_RE, PACKAGE_WORD_RE):
        for match in regex.finditer(text):
            value = next((group for group in match.groups() if group), match.group(0))
            root = value.split(".")[0].strip("`'\"")
            if root.lower() not in {"python", "package", "plugin", "library"}:
                packages.append(root)
    packages.extend(extract_stack_modules(text))
    return list(dict.fromkeys(packages))


def extract_regression_phrases(text: str) -> list[str]:
    return [sentence for sentence in _sentences(text) if REGRESSION_TERMS.search(sentence)]


def _canonical_regression_phrase(sentence: str) -> str:
    without_quote = re.sub(r"^(?:\s*>\s*)+", "", sentence)
    return re.sub(r"\s+", " ", without_quote).strip()


def _packaging_tool_is_directly_investigated(key: str, context: str) -> bool:
    if key == "pip":
        return bool(PIP_INVESTIGATION_RE.search(context))
    if key == "setuptools":
        return bool(SETUPTOOLS_INVESTIGATION_RE.search(context))
    if key == "wheel":
        return bool(PACKAGING_CONTEXT_RE.search(context))
    return False


def _version_is_relevant(issue: Issue, doc: Document, match: re.Match[str]) -> bool:
    if doc.kind == "issue_title":
        return True
    line = _line_at(doc.text, match.start())
    line_start = doc.text.rfind("\n", 0, match.start()) + 1
    relative_start = match.start() - line_start
    relative_end = match.end() - line_start
    if any(
        python_match.start(1) <= relative_start and relative_end <= python_match.end(1)
        for python_match in PYTHON_RE.finditer(line)
    ):
        return True
    if re.search(r"\bFile\s+[\"']|(?:site|dist)-packages[/\\]", line, re.I):
        return False
    prefix = line[max(0, relative_start - 70) : relative_start]
    repo_prefix = re.compile(
        rf"(?<![\w.-]){re.escape(issue.repo)}(?:\s+version)?\s*(?:is\s+|==|=|:|---)?\s*v?\s*$",
        re.I,
    )
    if repo_prefix.search(prefix):
        return True
    local_context = line[max(0, relative_start - 100) : min(len(line), relative_end + 100)]
    if (
        REGRESSION_TERMS.search(local_context)
        or VERSION_RELEVANCE_TERMS.search(local_context)
        or RELEASE_VERSION_CONTEXT_RE.search(local_context)
        or RELEASE_VERSION_CONTEXT_RE.search(line)
    ):
        return True
    boundary_matches = [item.group(0).casefold() for item in BOUNDARY_TERMS.finditer(local_context)]
    has_specific_boundary = any(item != "wheel" for item in boundary_matches) or bool(
        PACKAGING_CONTEXT_RE.search(local_context)
    )
    if has_specific_boundary:
        for package in extract_packages(prefix):
            package_prefix = re.compile(
                rf"(?<![\w.-]){re.escape(package)}\s*(?:version\s*)?(?:==|=|:|-)\s*$",
                re.I,
            )
            if package_prefix.search(prefix):
                return True
    return False


def _dedupe(evidence: list[Evidence]) -> list[Evidence]:
    result: list[Evidence] = []
    indexes: dict[tuple[str, str, str], int] = {}
    for item in evidence:
        key = (item.category, item.confidence.value, item.claim.casefold())
        if key not in indexes:
            indexes[key] = len(result)
            result.append(item)
        else:
            index = indexes[key]
            existing = result[index]
            combined = tuple(dict.fromkeys(existing.sources + item.sources))[:3]
            result[index] = Evidence(existing.category, existing.confidence, existing.claim, combined)
    return result


def extract_evidence(issue: Issue) -> list[Evidence]:
    docs = issue_documents(issue)
    items: list[Evidence] = []
    package_sources: dict[str, list[Source]] = defaultdict(list)
    package_strong_sources: dict[str, list[Source]] = defaultdict(list)
    package_display: dict[str, str] = {}
    external_repo_sources: dict[str, list[Source]] = defaultdict(list)
    current_names = {issue.repo.casefold().replace("-", "_"), issue.owner.casefold().replace("-", "_")}

    for doc in docs:
        for match in PYTHON_RE.finditer(doc.text):
            runtime = match.group(0)
            items.append(Evidence("environment", Confidence.FACT, f"Runtime mentioned: {runtime}.", (_source(doc, match),)))
        for match in ABI_RE.finditer(doc.text):
            items.append(Evidence("environment", Confidence.FACT, f"ABI or wheel tag mentioned: {match.group(0)}.", (_source(doc, match),)))
        for match in OS_RE.finditer(doc.text):
            items.append(Evidence("environment", Confidence.FACT, f"Platform mentioned: {match.group(0)}.", (_source(doc, match),)))

        for match in VERSION_RE.finditer(doc.text):
            if not _version_is_relevant(issue, doc, match):
                continue
            version = match.group(0).lstrip("vV").rstrip(".,;:")
            items.append(Evidence("version", Confidence.FACT, f"Version mentioned: {version}.", (_source(doc, match),)))

        for link in extract_github_links(doc.text):
            match = re.search(re.escape(str(link["url"])), doc.text)
            if match is None and link["number"] is not None:
                shorthand = f"{link['owner']}/{link['repo']}#{link['number']}"
                match = re.search(re.escape(shorthand), doc.text, re.I)
            repo_name = f"{link['owner']}/{link['repo']}"
            relation = "external repository" if repo_name.casefold() != f"{issue.owner}/{issue.repo}".casefold() else "same repository"
            items.append(
                Evidence(
                    "related",
                    Confidence.FACT,
                    f"Explicit GitHub link to {repo_name} ({relation}): {link['url']}.",
                    (_source(doc, match),),
                )
            )
            if relation == "external repository":
                repo_key = str(link["repo"]).casefold().replace("-", "_")
                external_repo_sources[repo_key].append(_source(doc, match))
                items.append(
                    Evidence(
                        "boundary",
                        Confidence.STRONG_CLUE,
                        f"Investigate the external repository boundary with `{repo_name}`.",
                        (_source(doc, match),),
                    )
                )

        for match in EXTERNAL_URL_RE.finditer(doc.text):
            url = match.group(0).rstrip(".,;:")
            domain = (urllib.parse.urlsplit(url).hostname or "").casefold()
            if not domain or domain in {"github.com", "www.github.com"}:
                continue
            context = _context_at(doc.text, match.start(), match.end())
            if INFRASTRUCTURE_TERMS.search(context):
                items.append(
                    Evidence(
                        "boundary",
                        Confidence.STRONG_CLUE,
                        f"Investigate external repository/service boundary: `{domain}`.",
                        (_source(doc, match),),
                    )
                )

        for match in HISTORY_SHA_RE.finditer(mask_code_fences(doc.text)):
            sha = match.group("sha")
            if re.match(r"^\s*commit\s*:", _line_at(doc.text, match.start()), re.I):
                continue
            commit_url = f"https://github.com/{issue.owner}/{issue.repo}/commit/{sha}"
            items.append(
                Evidence(
                    "version",
                    Confidence.FACT,
                    f"Historical commit referenced: [{sha}]({commit_url}).",
                    (_source(doc, match),),
                )
            )

        for match in RUNTIME_BOUNDARY_RE.finditer(doc.text):
            signal = match.group(0)
            normalized = signal.casefold()
            if "thread" in normalized or "gil" in normalized:
                claim = "Investigate the free-threading/no-GIL runtime boundary."
            elif "wheel" in normalized or "abi" in normalized:
                claim = "Investigate the wheel/ABI packaging boundary."
            else:
                claim = "Investigate the binary runtime compatibility boundary."
            context = _context_at(doc.text, match.start(), match.end(), radius=120)
            if "wheel" in normalized and "abi" not in normalized and not PACKAGING_CONTEXT_RE.search(context):
                continue
            items.append(
                Evidence(
                    "boundary",
                    Confidence.STRONG_CLUE,
                    claim,
                    (_source(doc, match),),
                )
            )

        for package in extract_packages(doc.text):
            for match in re.finditer(rf"(?<![\w.-]){re.escape(package)}(?![\w.-])", doc.text, re.I):
                key = package.casefold().replace("-", "_")
                package_display.setdefault(key, package)
                source = _source(doc, match)
                package_sources[key].append(source)
                context = _context_at(doc.text, match.start(), match.end(), radius=120)
                stack_modules = {name.casefold().replace("-", "_") for name in extract_stack_modules(doc.text)}
                has_explicit_signal = bool(
                    (
                        BOUNDARY_TERMS.search(context)
                        and ("wheel" not in context.casefold() or PACKAGING_CONTEXT_RE.search(context))
                    )
                    or UNCERTAINTY_TERMS.search(context)
                    or REGRESSION_TERMS.search(context)
                    or (VERSION_RE.search(context) and VERSION_RELEVANCE_TERMS.search(context))
                    or (key in stack_modules and BOUNDARY_TERMS.search(context))
                    or (doc.kind == "issue_title" and key not in current_names)
                )
                if key in PACKAGING_TOOL_KEYS:
                    has_explicit_signal = _packaging_tool_is_directly_investigated(key, context)
                if has_explicit_signal:
                    package_strong_sources[key].append(source)

        prose = mask_code_fences(doc.text)
        for sentence in extract_regression_phrases(prose):
            canonical_sentence = _canonical_regression_phrase(sentence)
            items.append(
                Evidence(
                    "version",
                    Confidence.STRONG_CLUE,
                    f"Version or regression language: {_excerpt(canonical_sentence, limit=200)}",
                    (_source(doc, excerpt=_excerpt(sentence, limit=240)),),
                )
            )
        for sentence in _sentences(prose):
            if UNCERTAINTY_TERMS.search(sentence):
                items.append(
                    Evidence(
                        "gap",
                        Confidence.FACT,
                        f"Responsibility or reproduction uncertainty is explicit: {_excerpt(sentence, limit=200)}",
                        (_source(doc, excerpt=_excerpt(sentence, limit=240)),),
                    )
                )

    for key, sources in package_sources.items():
        display = package_display[key]
        unique_sources = list(dict.fromkeys(sources))
        strong_sources = list(dict.fromkeys(package_strong_sources[key] + external_repo_sources[key]))
        confidence = Confidence.STRONG_CLUE if strong_sources else Confidence.WEAK_CLUE
        if key in current_names or key == "wheel" or confidence == Confidence.WEAK_CLUE:
            continue
        items.append(
            Evidence(
                "boundary",
                confidence,
                f"Investigate the package/runtime boundary involving `{display}`.",
                tuple(dict.fromkeys(strong_sources + unique_sources))[:3],
            )
        )

    if not any(item.category == "gap" for item in items):
        body_source = Source(issue.url, "issue_body", "issue body", _excerpt(issue.body or issue.title))
        items.append(
            Evidence(
                "gap",
                Confidence.WEAK_CLUE,
                "No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.",
                (body_source,),
            )
        )
    return _dedupe(items)
