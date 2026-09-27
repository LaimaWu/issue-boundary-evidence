# Issue Boundary Evidence

- Issue: [rust-lang/cargo#17519](https://github.com/rust-lang/cargo/issues/17519) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/rust-lang/cargo/issues/17519)): `build.warnings` is not honored when using `cargo clippy --message-format=json`
- State at retrieval ([issue metadata](https://github.com/rust-lang/cargo/issues/17519)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- **fact** — Platform mentioned: linux.
  - Source: [issue_body](https://github.com/rust-lang/cargo/issues/17519), issue body — “e937d6127d0f49881bf689c560b36d35c4 commit-date: 2026-09-25 host: x86_64-unknown-linux-gnu libgit2: 1.9.6 (sys:0.21.0 vendored) libcurl: 8.21.0-DEV (sys:0.4.90+curl-8.21.0 vendored ssl:O”
- **fact** — Platform mentioned: Debian.
  - Source: [issue_body](https://github.com/rust-lang/cargo/issues/17519), issue body — “.4.90+curl-8.21.0 vendored ssl:OpenSSL/3.6.3) ssl: OpenSSL 3.6.3 9 Jun 2026 os: Debian n/a (forky) [64-bit] ```”

## Boundary candidates

- **strong_clue** — Investigate the external repository boundary with `ComunidadAylas/vorbis-rs`.
  - Source: [issue_body](https://github.com/rust-lang/cargo/issues/17519), issue body — “ARNINGS=deny` also causes Clippy to error out. Link to the CI run shown above: https://github.com/ComunidadAylas/vorbis-rs/actions/runs/36269077411/job/108479444526#step:6:118 ### Steps 1. Clone https://github.com/ComunidadAylas/vorbis-rs…”
  - Source: [issue_body](https://github.com/rust-lang/cargo/issues/17519), issue body — “ARNINGS=deny` also causes Clippy to error out. Link to the CI run shown above: https://github.com/ComunidadAylas/vorbis-rs/actions/runs/36269077411/job/108479444526#step:6:118 ### Steps 1. Clone https://github.com/Comuni”

## Version and regression clues

- **fact** — Version mentioned: 1.100.0.
  - Source: [issue_body](https://github.com/rust-lang/cargo/issues/17519), issue body — “tegration with GitHub's code analysis tools and UI. ### Version ```text cargo 1.100.0-nightly (3d7cf6e93 2026-09-25) release: 1.100.0-nightly commit-hash: 3d7cf6e937d6127d0f49881bf689c5”
- **fact** — Historical commit referenced: [36269077411](https://github.com/rust-lang/cargo/commit/36269077411).
  - Source: [issue_body](https://github.com/rust-lang/cargo/issues/17519), issue body — “switch instead of `CARGO_BUILD_WARNINGS=deny` also causes Clippy to error out. Link to the CI run shown above: https://github.com/ComunidadAylas/vorbis-rs/actions/runs/36269077411/job/108479444526#step:6:118 ### Steps 1. Clone https://gith…”
- **fact** — Historical commit referenced: [bd160df](https://github.com/rust-lang/cargo/commit/bd160df).
  - Source: [issue_body](https://github.com/rust-lang/cargo/issues/17519), issue body — “#step:6:118 ### Steps 1. Clone https://github.com/ComunidadAylas/vorbis-rs at commit `bd160df`. 2. Run `CARGO_BUILD_WARNINGS=deny cargo clippy --message-format=json` and watch it complete succe”

## Related evidence

- **fact** — Explicit GitHub link to ComunidadAylas/vorbis-rs (external repository): https://github.com/ComunidadAylas/vorbis-rs/actions/runs/36269077411/job/108479444526#step:6:118.
  - Source: [issue_body](https://github.com/rust-lang/cargo/issues/17519), issue body — “ARNINGS=deny` also causes Clippy to error out. Link to the CI run shown above: https://github.com/ComunidadAylas/vorbis-rs/actions/runs/36269077411/job/108479444526#step:6:118 ### Steps 1. Clone https://github.com/ComunidadAylas/vorbis-rs…”
- **fact** — Explicit GitHub link to ComunidadAylas/vorbis-rs (external repository): https://github.com/ComunidadAylas/vorbis-rs.
  - Source: [issue_body](https://github.com/rust-lang/cargo/issues/17519), issue body — “ARNINGS=deny` also causes Clippy to error out. Link to the CI run shown above: https://github.com/ComunidadAylas/vorbis-rs/actions/runs/36269077411/job/108479444526#step:6:118 ### Steps 1. Clone https://github.com/Comuni”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/rust-lang/cargo/issues/17519), issue body — “### Problem While taking care of miscellaneous maintenance tasks in my `vorbis-rs` project, I noticed that using `CARGO_BUILD_WARNINGS=deny cargo clippy --message-format=json` does not cause Cargo to error out on Clippy warnings as expecte…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
