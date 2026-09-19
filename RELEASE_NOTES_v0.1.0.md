# v0.1.0 — Initial experimental release

## What this is

Issue Boundary Evidence is a small read-only CLI for OSS maintainers.

Given a public GitHub Issue URL, it extracts traceable evidence around:

- dependency and plugin boundaries;
- runtime and packaging boundaries;
- upstream or external-service clues;
- version and regression history;
- missing evidence that may block investigation.

Every factual item links back to its source.

## What this release includes

- deterministic GitHub Issue/comment retrieval;
- package, runtime, version, and regression extraction;
- related GitHub evidence parsing;
- contextual commit-history evidence;
- external repository/service boundary evidence;
- `fact`, `strong_clue`, and `weak_clue` confidence levels;
- Markdown output;
- frozen retrospective evaluation outputs;
- 38 unit tests.

## Safety / scope

This tool:

- does not comment on or modify GitHub Issues;
- does not create labels, PRs, or fixes;
- does not execute code from Issue bodies or comments;
- does not fetch arbitrary external service URLs;
- does not require an LLM or external model API.

## Status

This is an experimental v0.1.0 release.

The current goal is to test whether maintainers find the evidence pack useful on real issues, especially issues involving dependency, runtime, upstream, or version boundaries.

Feedback and real-world examples are welcome.
