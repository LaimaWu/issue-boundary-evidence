# Issue Boundary Evidence

- Issue: [pytest-dev/pytest#12425](https://github.com/pytest-dev/pytest/issues/12425) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/pytest-dev/pytest/issues/12425)): pytest 8.2.0 regresses collection and now collects non-Test* classes
- State at retrieval ([issue metadata](https://github.com/pytest-dev/pytest/issues/12425)): closed
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- **strong_clue** — Investigate the external repository boundary with `apache/libcloud`.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12425), issue body — “Discovered while testing [libcloud](https://github.com/apache/libcloud) with pytest 8.2.0, as seen in https://github.com/apache/libcloud/blob/trunk/libcloud/test/__init__”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12425), issue body — “ng [libcloud](https://github.com/apache/libcloud) with pytest 8.2.0, as seen in https://github.com/apache/libcloud/blob/trunk/libcloud/test/__init__.py#L90 the MockHttp class is also collected and attempted to be instantiated, leading to c…”
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12425#issuecomment-2151440096), comment 1 — “https://github.com/apache/libcloud/blob/6f1f83d57fb6bbf7d932ea2c4e312ba5fd86fb81/libcloud/test/common/test_cloudstack.py#L119 is fundamentally broken, it was pure dumb luck it ever worked imho its a upstream bug that was a”

## Version and regression clues

- **fact** — Version mentioned: 8.2.0.
  - Source: [issue_title](https://github.com/pytest-dev/pytest/issues/12425), issue title — “pytest 8.2.0 regresses collection and now collects non-Test* classes”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12425), issue body — “overed while testing [libcloud](https://github.com/apache/libcloud) with pytest 8.2.0, as seen in https://github.com/apache/libcloud/blob/trunk/libcloud/test/__init__.py#L90 the MockHtt”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12425), issue body — “2.22 PyNaCl 1.5.0 pyOpenSSL 24.1.0 pytest 8.2.0 requests 2.32.2 requests-mock 1.12.1 ruff 0.4.4 setuptools”
- **fact** — Historical commit referenced: [1a5e0eb71d2af0ad113ccd9ee596c7d724d7a4b6](https://github.com/pytest-dev/pytest/commit/1a5e0eb71d2af0ad113ccd9ee596c7d724d7a4b6).
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12425), issue body — “dConnection.__init__() missing 1 required positional argument: 'port' ``` I bisected this down to first occurring with https://github.com/pytest-dev/pytest/commit/1a5e0eb71d2af0ad113ccd9ee596c7d724d7a4b6 (sixth commit or so of 8.2.0) pip l…”

## Related evidence

- **fact** — Explicit GitHub link to apache/libcloud (external repository): https://github.com/apache/libcloud.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12425), issue body — “Discovered while testing [libcloud](https://github.com/apache/libcloud) with pytest 8.2.0, as seen in https://github.com/apache/libcloud/blob/trunk/libcloud/test/__init__”
- **fact** — Explicit GitHub link to apache/libcloud (external repository): https://github.com/apache/libcloud/blob/trunk/libcloud/test/__init__.py#L90.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12425), issue body — “ng [libcloud](https://github.com/apache/libcloud) with pytest 8.2.0, as seen in https://github.com/apache/libcloud/blob/trunk/libcloud/test/__init__.py#L90 the MockHttp class is also collected and attempted to be instantiated, leading to c…”
- **fact** — Explicit GitHub link to pytest-dev/pytest (same repository): https://github.com/pytest-dev/pytest/commit/1a5e0eb71d2af0ad113ccd9ee596c7d724d7a4b6.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12425), issue body — “ositional argument: 'port' ``` I bisected this down to first occurring with https://github.com/pytest-dev/pytest/commit/1a5e0eb71d2af0ad113ccd9ee596c7d724d7a4b6 (sixth commit or so of 8.2.0) pip list output: ``` Package Version -----------…”
- **fact** — Explicit GitHub link to apache/libcloud (external repository): https://github.com/apache/libcloud/blob/6f1f83d57fb6bbf7d932ea2c4e312ba5fd86fb81/libcloud/test/common/test_cloudstack.py#L119.
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12425#issuecomment-2151440096), comment 1 — “https://github.com/apache/libcloud/blob/6f1f83d57fb6bbf7d932ea2c4e312ba5fd86fb81/libcloud/test/common/test_cloudstack.py#L119 is fundamentally broken, it was pure dumb luck it ever worked imho its a upstream bug that was a”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12425), issue body — “Discovered while testing [libcloud](https://github.com/apache/libcloud) with pytest 8.2.0, as seen in https://github.com/apache/libcloud/blob/trunk/libcloud/test/__init__.py#L90 the MockHttp class is also collected and attempted to be inst…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
