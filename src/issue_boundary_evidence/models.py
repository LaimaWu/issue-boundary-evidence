from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Confidence(str, Enum):
    FACT = "fact"
    STRONG_CLUE = "strong_clue"
    WEAK_CLUE = "weak_clue"


@dataclass(frozen=True)
class Source:
    url: str
    kind: str
    location: str
    excerpt: str


@dataclass(frozen=True)
class Evidence:
    category: str
    confidence: Confidence
    claim: str
    sources: tuple[Source, ...]

    def __post_init__(self) -> None:
        if not self.sources:
            raise ValueError("Every evidence item must preserve at least one source")


@dataclass(frozen=True)
class Document:
    url: str
    kind: str
    location: str
    text: str


@dataclass
class Issue:
    owner: str
    repo: str
    number: int
    url: str
    title: str
    body: str
    comments: list[dict] = field(default_factory=list)
    state: str = ""


@dataclass
class Analysis:
    issue: Issue
    evidence: list[Evidence]
    related_issues: list[Issue] = field(default_factory=list)

