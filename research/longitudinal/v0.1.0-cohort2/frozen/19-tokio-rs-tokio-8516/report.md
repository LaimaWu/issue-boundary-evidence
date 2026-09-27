# Issue Boundary Evidence

- Issue: [tokio-rs/tokio#8516](https://github.com/tokio-rs/tokio/issues/8516) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/tokio-rs/tokio/issues/8516)): net: UnixStream::peer_cred() fails with ENOPROTOOPT on NetBSD: LOCAL_PEEREID is asked at SOL_SOCKET instead of SOL_LOCAL
- State at retrieval ([issue metadata](https://github.com/tokio-rs/tokio/issues/8516)): open
- Method: deterministic, read-only extraction from the issue and its comments

## Environment facts

- No evidence extracted in this category.

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **fact** — Version mentioned: 1.53.1.
  - Source: [issue_body](https://github.com/tokio-rs/tokio/issues/8516), issue body — “**Version** tokio 1.53.1; the same code is on `master` today (`tokio/src/net/unix/ucred.rs`, `impl_netbsd`). **Platform**”
- **strong_clue** — Version or regression language: A regression test on NetBSD needs a listener-accepted connection rather than `UnixStream::pair()`, for the reason above.
  - Source: [issue_body](https://github.com/tokio-rs/tokio/issues/8516), issue body — “A regression test on NetBSD needs a listener-accepted connection rather than `UnixStream::pair()`, for the reason above.”
- **strong_clue** — Version or regression language: We worked around it in our code with `getpeereid(3)` on NetBSD; this report is so the workaround can be removed once a release carries the fix.
  - Source: [issue_body](https://github.com/tokio-rs/tokio/issues/8516), issue body — “We worked around it in our code with `getpeereid(3)` on NetBSD; this report is so the workaround can be removed once a release carries the fix.”

## Related evidence

- No evidence extracted in this category.

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/tokio-rs/tokio/issues/8516), issue body — “**Version** tokio 1.53.1; the same code is on `master` today (`tokio/src/net/unix/ucred.rs`, `impl_netbsd`). **Platform** NetBSD 11.0 amd64 (`NetBSD 11.0 (GENERIC) #0`), `x86_64-unknown-netbsd`. **Description** On NetBSD, `UnixStream::peer…”

## Retrieved same-repository references

- No justified same-repository issue or pull-request references were retrieved.

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
