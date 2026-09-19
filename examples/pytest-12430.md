# Issue Boundary Evidence

- Issue: [pytest-dev/pytest#12430](https://github.com/pytest-dev/pytest/issues/12430) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/pytest-dev/pytest/issues/12430)): MockAwareDocTestFinder._find_lineno is stale
- State at retrieval ([issue metadata](https://github.com/pytest-dev/pytest/issues/12430)): closed
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Runtime mentioned: Python 3.11.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “0 issue17446 resolves to python/cpython#61648, the fix which was released in Python 3.11. #8796 links to 0191563fd605a839e9e9c299605c52725b4da17a, which indicates that the method has two p”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “ed to be reported upstream? Doing a bit of testing, the doctests all pass on Python 3.11 and later with that method removed, so I'm inclined to say there's no outstanding work to be done e”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “outstanding work to be done except to suppress the use of this workaround after Python 3.11.”
- **fact** — Runtime mentioned: Python 3.11.8.
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12430#issuecomment-2173542291), comment 1 — “for @webknjaz, and it was because he happened to be running the testsuite with Python 3.11.8. You said: > the fix which was released in Python 3.11 but the fix actually only made it i”
- **fact** — Runtime mentioned: Python 3.13.
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12430#issuecomment-2174743826), comment 2 — “karound should be enabled for the specified patch versions or made dependent on Python 3.13.”

## Boundary candidates

- **strong_clue** — Investigate the external repository boundary with `python/cpython`.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “4d3604e16ddebfe6e28f/src/_pytest/doctest.py#L514-L520 issue17446 resolves to python/cpython#61648, the fix which was released in Python 3.11. #8796 links to 0191563fd605a839e9e9c299605c52725b4da17a”
- **strong_clue** — Investigate the package/runtime boundary involving `cpython`.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “dicates that the method has two purposes, one to work around the aforementioned cpython issue and another "to be reported upstream," though I don't see that it was reported upstream. Does”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “4d3604e16ddebfe6e28f/src/_pytest/doctest.py#L514-L520 issue17446 resolves to python/cpython#61648, the fix which was released in Python 3.11. #8796 links to 0191563fd605a839e9e9c299605c52725b4da17a”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “16ddebfe6e28f/src/_pytest/doctest.py#L514-L520 issue17446 resolves to python/cpython#61648, the fix which was released in Python 3.11. #8796 links to 0191563fd605a839e9e9c299605c52725b”

## Version and regression clues

- **fact** — Version mentioned: 3.11.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “sue17446 resolves to python/cpython#61648, the fix which was released in Python 3.11. #8796 links to 0191563fd605a839e9e9c299605c52725b4da17a, which indicates that the method has two p”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “e reported upstream? Doing a bit of testing, the doctests all pass on Python 3.11 and later with that method removed, so I'm inclined to say there's no outstanding work to be done e”
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “ding work to be done except to suppress the use of this workaround after Python 3.11.”
- **fact** — Historical commit referenced: [0191563fd605a839e9e9c299605c52725b4da17a](https://github.com/pytest-dev/pytest/commit/0191563fd605a839e9e9c299605c52725b4da17a).
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “olves to python/cpython#61648, the fix which was released in Python 3.11. #8796 links to 0191563fd605a839e9e9c299605c52725b4da17a, which indicates that the method has two purposes, one to work around the aforementioned cpython is”
- **strong_clue** — Version or regression language: Doing a bit of testing, the doctests all pass on Python 3.11 and later with that method removed, so I'm inclined to say there's no outstanding work to be done except to suppress the use of this worka…
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “Doing a bit of testing, the doctests all pass on Python 3.11 and later with that method removed, so I'm inclined to say there's no outstanding work to be done except to suppress the use of this workaround after Python 3.11.”
- **fact** — Version mentioned: 3.11.8.
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12430#issuecomment-2173542291), comment 1 — “ebknjaz, and it was because he happened to be running the testsuite with Python 3.11.8. You said: > the fix which was released in Python 3.11 but the fix actually only made it i”
- **fact** — Version mentioned: 3.11.9.
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12430#issuecomment-2173542291), comment 1 — “h was released in Python 3.11 but the fix actually only made it into Python [3.11.9](https://www.python.org/downloads/release/python-3119/) and [3.12.3](https://www.python.org/downloa”
- **fact** — Version mentioned: 3.12.3.
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12430#issuecomment-2173542291), comment 1 — “nto Python [3.11.9](https://www.python.org/downloads/release/python-3119/) and [3.12.3](https://www.python.org/downloads/release/python-3124/), which are only around 2 months old now.”
- **fact** — Version mentioned: 3.12.
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12430#issuecomment-2173542291), comment 1 — “w. @jaraco I suppose it'd make sense to still use the workaround on 3.11 and 3.12 versions before those patch releases, no?”
- **strong_clue** — Version or regression language: @jaraco I suppose it'd make sense to still use the workaround on 3.11 and 3.12 versions before those patch releases, no?
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12430#issuecomment-2173542291), comment 1 — “@jaraco I suppose it'd make sense to still use the workaround on 3.11 and 3.12 versions before those patch releases, no?”
- **fact** — Version mentioned: 3.13.
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12430#issuecomment-2174743826), comment 2 — “should be enabled for the specified patch versions or made dependent on Python 3.13.”
- **strong_clue** — Version or regression language: I think you're right and the workaround should be enabled for the specified patch versions or made dependent on Python 3.13.
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12430#issuecomment-2174743826), comment 2 — “I think you're right and the workaround should be enabled for the specified patch versions or made dependent on Python 3.13.”
- **strong_clue** — Version or regression language: Regression fix: https://github.com/pytest-dev/pytest/pull/12471
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12430#issuecomment-2175563139), comment 3 — “Regression fix: https://github.com/pytest-dev/pytest/pull/12471”

## Related evidence

- **fact** — Explicit GitHub link to pytest-dev/pytest (same repository): https://github.com/pytest-dev/pytest/blob/043ff9abc657124db3504d3604e16ddebfe6e28f/src/_pytest/doctest.py#L514-L520.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “In doctest, the comment for _find_lineno is stale: https://github.com/pytest-dev/pytest/blob/043ff9abc657124db3504d3604e16ddebfe6e28f/src/_pytest/doctest.py#L514-L520 issue17446 resolves to python/cpython#61648, the fix which was released…”
- **fact** — Explicit GitHub link to python/cpython (external repository): https://github.com/python/cpython/issues/61648.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “4d3604e16ddebfe6e28f/src/_pytest/doctest.py#L514-L520 issue17446 resolves to python/cpython#61648, the fix which was released in Python 3.11. #8796 links to 0191563fd605a839e9e9c299605c52725b4da17a”
- **fact** — Explicit GitHub link to pytest-dev/pytest (same repository): https://github.com/pytest-dev/pytest/pull/12471.
  - Source: [issue_comment](https://github.com/pytest-dev/pytest/issues/12430#issuecomment-2175563139), comment 3 — “Regression fix: https://github.com/pytest-dev/pytest/pull/12471”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/pytest-dev/pytest/issues/12430), issue body — “In doctest, the comment for _find_lineno is stale: https://github.com/pytest-dev/pytest/blob/043ff9abc657124db3504d3604e16ddebfe6e28f/src/_pytest/doctest.py#L514-L520 issue17446 resolves to python/cpython#61648, the fix which was released…”

## Retrieved same-repository references

- **fact** — [pytest-dev/pytest#8796: Internal error when adding a skip mark to a doctest inside a contextmanager](https://github.com/pytest-dev/pytest/issues/8796) (source kind: related issue metadata; structured location: title and state=closed)
- **fact** — [pytest-dev/pytest#12471: 🚑 Clarify patch condition for doctest finder hack](https://github.com/pytest-dev/pytest/pull/12471) (source kind: related issue metadata; structured location: title and state=closed)

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
