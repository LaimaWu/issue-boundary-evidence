# v0.1.2 — Packaging and distribution maintenance

## Fixed

- Correct the package version metadata to `0.1.2`.
- Add public repository and issue-tracker metadata to the package.

## Distribution readiness

- Add a manually triggered GitHub Actions workflow for PyPI Trusted Publishing with OIDC and the `pypi` environment.
- Build and validate both the wheel and source distribution.
- Document installation from the v0.1.2 GitHub release wheel.
- Publish the package to PyPI through the Trusted Publishing workflow.

## Behavior

This release changes packaging and distribution metadata only. Extraction, retrieval, confidence, classification, and report behavior are unchanged.
