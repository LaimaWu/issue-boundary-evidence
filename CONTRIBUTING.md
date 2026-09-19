# Contributing

Issue Boundary Evidence targets Python 3.10+ and intentionally keeps its core deterministic, read-only, and small.

## Setup

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
```

## Tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Contribution rules

- Add regression tests for every new extraction or retrieval rule.
- Do not hard-code behavior for a single historical issue or repository.
- Preserve provenance for factual evidence.
- Keep GitHub access read-only; do not add write actions to the core tool.
- Do not execute issue-provided code, commands, or scripts.
- Avoid adding LLM/API dependencies unless future evaluation shows deterministic retrieval is insufficient.
