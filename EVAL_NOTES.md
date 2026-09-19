# Evaluation Notes

## Purpose

This project is an evaluation spike. It tests whether deterministic evidence retrieval can surface useful dependency, upstream, runtime, and version boundaries before a maintainer manually reconstructs them. It is not a general issue summarizer and does not attempt root-cause diagnosis.

## Evaluation set

The frozen retrospective set contains ten historical closed issues from pandas, pytest, and NumPy:

- pandas: `#58927`
- pytest: `#12424`, `#12425`, `#12430`, `#12432`, `#12440`
- NumPy: `#26598`, `#26622`, `#26643`, `#26660`

The implementation contains no issue-number-specific rules or expected answers.

## Baseline

- Baseline A: read only the issue title and initial body.
- Spike: read the issue title, body, comments, and narrowly justified same-repository references.

## Scoring rubric

Score each case from 0 to 2 on each dimension:

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Boundary hit | missed | partial | main historical boundary surfaced |
| Version/history hit | absent | versions without structure | key version/history evidence surfaced |
| Traceability | many unsupported claims | partial sourcing | every factual claim traceable |
| Noise | more than 3 clearly irrelevant items | 1–3 irrelevant items | 0–1 irrelevant items |

Success requires at least 60/80, a full boundary hit in at least 7/10 cases, zero unsupported factual claims, and useful comment/history evidence beyond the initial body in at least three cases.

## Running the retrospective

Run each URL with the normal CLI and save the output. A human evaluator should compare reports to the frozen historical ground truth; do not convert that ground truth into extraction rules.

```bash
issue-boundary-evidence ISSUE_URL --output report.md
```

The checked-in examples demonstrate report generation, not a completed rubric score. A final GO/REVISE/STOP decision remains a human evaluation step.

Raw reports from the precision-pass run are checked in under `eval_outputs/` using stable repository-and-issue filenames.

## Known limitations

- Package discovery is lexical and deliberately conservative.
- Repetition alone does not raise a package to `strong_clue`; an explicit boundary, responsibility, runtime, regression, stack, or external-repository signal is required.
- External repositories are identified but not crawled.
- External service domains in infrastructure context are recorded but never fetched.
- Contextual commit SHAs are linked to their same-repository commit URL without fetching commit data or diffs.
- Version reporting is context-prioritized, so some environment-dump versions are intentionally omitted.
- Runtime names require complete `Python`, `CPython`, or `PyPy` tokens; package names ending in `-python` are not runtimes.
- Packaging tools require direct version, wheel-selection, ABI, or tool-behavior evidence before strong-clue promotion.
- Repeated regression prose quoted in later comments is canonicalized and deduplicated with provenance retained.
- Same-repository references are fetched for metadata only; broad search is intentionally absent.
- The GitHub API view may differ from the historical page if comments were edited or removed.
