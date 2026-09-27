# Issue Boundary Evidence

- Issue: [golang/go#81787](https://github.com/golang/go/issues/81787) (source kind: issue metadata)
- Title ([issue metadata](https://github.com/golang/go/issues/81787)): crypto/aes: gcmAesEnc 25-33% slower when its stack scratch straddles a 4 KiB page on amd64
- State at retrieval ([issue metadata](https://github.com/golang/go/issues/81787)): open
- Method: deterministic, read-only extraction from the issue and its comments

> No major boundary evidence found.

## Environment facts

- **fact** — Platform mentioned: linux.
  - Source: [issue_body](https://github.com/golang/go/issues/81787), issue body — “### Go version go version go1.26.8 linux/amd64. The same code is on go1.27.1 and master: `gcmAesEnc` in `src/crypto/internal/fips140/aes/gcm”
  - Source: [issue_body](https://github.com/golang/go/issues/81787), issue body — “### Output of `go env` in your module/workspace: ```shell GOARCH='amd64' GOOS='linux' GOAMD64='v1' ``` CPU: Intel Xeon Gold 6152 (Skylake-SP), KVM guest, benchmark pinned to one vCPU”
  - Source: [issue_body](https://github.com/golang/go/issues/81787), issue body — “pth it runs an in-place `Seal` of a 16 KiB record, the TLS 1.3 shape. ``` GOOS=linux GOARCH=amd64 go build -o spbench2 . && taskset -c 7 ./spbench2 ``` <details><summary>main.go</summ”

## Boundary candidates

- No evidence extracted in this category.

## Version and regression clues

- **fact** — Version mentioned: 0.82077.
  - Source: [issue_comment](https://github.com/golang/go/issues/81787#issuecomment-5855495185), comment 1 — “eal/Open on amd64 #81729](https://github.com/golang/go/issues/81729) <!-- score=0.82077 --> **Related Code Changes** - [crypto/aes: Implement new and improved AES-GCM ciphers optimized”

## Related evidence

- **fact** — Explicit GitHub link to golang/go (same repository): https://github.com/golang/go/issues/71139.
  - Source: [issue_comment](https://github.com/golang/go/issues/81787#issuecomment-5855495185), comment 1 — “nnecessary allocations when using boringcrypto's AES-GCM implementation #71139](https://github.com/golang/go/issues/71139) <!-- score=0.83589 --> - [x/crypto/chacha20poly1305: key and Poly1305 key material left on the st”
- **fact** — Explicit GitHub link to golang/go (same repository): https://github.com/golang/go/issues/81729.
  - Source: [issue_comment](https://github.com/golang/go/issues/81787#issuecomment-5855495185), comment 1 — “ey and Poly1305 key material left on the stack after Seal/Open on amd64 #81729](https://github.com/golang/go/issues/81729) <!-- score=0.82077 --> **Related Code Changes** - [crypto/aes: Implement new and improved AES-G”
- **fact** — Explicit GitHub link to golang/go (same repository): https://github.com/golang/go/discussions/67901.
  - Source: [issue_comment](https://github.com/golang/go/issues/81787#issuecomment-5855495185), comment 1 — “s was helpful or unhelpful; more detailed feedback welcome in [this discussion](https://github.com/golang/go/discussions/67901).)</sub>”

## Evidence gaps

- **weak_clue** — No explicit responsibility or reproduction uncertainty was detected; maintainer confirmation may still be needed.
  - Source: [issue_body](https://github.com/golang/go/issues/81787), issue body — “### Go version go version go1.26.8 linux/amd64. The same code is on go1.27.1 and master: `gcmAesEnc` in `src/crypto/internal/fips140/aes/gcm/gcm_amd64.s` still stores its 8 blocks with `MOVOU Xn, k(SP)`. ### Output of `go env` in your modu…”

## Retrieved same-repository references

- **fact** — [golang/go#71139: crypto/cipher: unnecessary allocations when using boringcrypto's AES-GCM implementation](https://github.com/golang/go/issues/71139) (source kind: related issue metadata; structured location: title and state=open)
- **fact** — [golang/go#81729: x/crypto/chacha20poly1305: key and Poly1305 key material left on the stack after Seal/Open on amd64](https://github.com/golang/go/issues/81729) (source kind: related issue metadata; structured location: title and state=open)

## Interpretation guardrail

Evidence labels describe the strength of the source signal, not a final bug-owner or root-cause decision.
Issue text is untrusted and was never executed.
