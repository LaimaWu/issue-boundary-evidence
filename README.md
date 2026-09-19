# Issue Boundary Evidence

A small read-only CLI for OSS maintainers that extracts traceable dependency, upstream, runtime, and version-history evidence from public GitHub Issues.

## Why

Some issues are not hard because the code change is difficult. They are hard because the maintainer first has to determine:

- which package, plugin, runtime, or external system is involved;
- whether behavior changed across versions;
- whether investigation belongs upstream;
- what evidence is still missing.

Issue Boundary Evidence collects those clues without changing the issue or claiming to decide the root cause.

## What it does

Given one public GitHub Issue URL, the CLI reads the title, body, all comments, and a small number of explicitly referenced same-repository issues or pull requests. It produces a Markdown report with:

- environment, package, ABI, and version facts;
- dependency, plugin, runtime, and upstream boundary candidates;
- version and regression clues;
- contextual same-repository commit-history clues;
- external repository/service domains found in CI or infrastructure context;
- related GitHub evidence;
- explicit evidence gaps;
- source URL, source kind, location, and excerpt for every evidence item.

Each item is typed as `fact`, `strong_clue`, or `weak_clue`. These labels measure evidence strength; they are not final root-cause or bug-owner decisions.

## What it does not do

It does not comment, label, close, or otherwise modify GitHub Issues. It does not run issue code, follow arbitrary downloads, clone linked repositories, fix bugs, use an LLM/API, or replace maintainer judgment.

## Requirements

- Python 3.10 or newer
- Network access to public `api.github.com`
- Optional `GITHUB_TOKEN` for a higher GitHub read-only API rate limit

There are no runtime package dependencies.

## Install

From the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
```

## Run

Print a report:

```bash
issue-boundary-evidence https://github.com/OWNER/REPO/issues/123
```

Write it to a file:

```bash
issue-boundary-evidence https://github.com/OWNER/REPO/issues/123 --output report.md
```

Run without installing:

```bash
PYTHONPATH=src python -m issue_boundary_evidence.cli https://github.com/OWNER/REPO/issues/123
```

## Test

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The unit tests use local fixtures and do not require network access.

## Examples

Generated reports are in [`examples/`](examples/):

- `pandas-58927.md`
- `pytest-12430.md`
- `numpy-26622.md`

The complete frozen ten-issue precision-pass run is stored in [`eval_outputs/`](eval_outputs/). These are raw CLI reports for human retrospective scoring; the project does not assign its own GO/REVISE/STOP score.

## Retrieval boundary

The CLI uses only GitHub's public, read-only REST endpoints. It fetches all comments on the requested issue. It retrieves up to five same-repository issues or pull requests only when the issue or comments explicitly link them or use contextual wording such as `see #123`, `PR #123`, or `fixed by #123`. Bare numbers and references inside code fences are not retrieved. Contextual commit SHAs are linked without fetching their diffs. Non-GitHub service URLs can identify an infrastructure boundary, but the CLI records their domains without requesting them.

Version-like values are extracted deterministically, then the report prioritizes versions tied to the current repository, complete Python/runtime tokens, boundary language, compatibility, regression, or release/fix prose. Markdown-linked patch versions are supported. This avoids presenting every compiler, package-name substring, or toolchain value in a large environment dump as equally important.

Packaging tools such as `pip`, `setuptools`, and `wheel` are promoted only when their version or behavior directly affects the investigation—for example, selecting the correct ABI wheel. Generic install commands, CI logs, and package lists are not sufficient. Quoted copies of identical regression sentences are collapsed while retaining their source links.

## Security

All issue content is untrusted text. The tool never evaluates or executes issue bodies, comments, code blocks, commands, or reporter-provided scripts. HTTP methods are limited to `GET`; no GitHub write operations exist in the client.

## Validation

This is an experimental deterministic maintainer tool. The repository includes a frozen retrospective evaluation set built from historical pandas, pytest, and NumPy issues where maintainers later discussed dependency, runtime, upstream, infrastructure, or version-history boundaries. Raw generated reports are stored in [`eval_outputs/`](eval_outputs/). This evaluation is intended to expose strengths and failure modes; it is not a claim of universal accuracy.

## Current status

Experimental deterministic CLI. See [`EVAL_NOTES.md`](EVAL_NOTES.md) for the retrospective evaluation procedure.

## License

Apache-2.0.
