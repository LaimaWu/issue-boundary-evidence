# Cohort 2 capture note

This note supplements the immutable Cohort 2 ZIP, SHA-256 `be0d203542a3fa77d286e20a54d127264d1f13e45643efc3781d03adfb495d31`. It does not alter the frozen archive, original issue snapshots, reports or journal.

The 20 issue, comment, timeline and event files preserve the complete JSON response content returned by the read connector. The capture wrote one trailing newline after each response string. Thus the freeze README's phrase “exact public GitHub REST response bodies” means content fidelity and should **not** be read as a claim of byte-for-byte HTTP body identity. Stored file hashes and archive SHA-256 identify the exact frozen bytes, including that newline. The connector did not expose HTTP response headers or per-response server time; each case records the UTC capture interval and `snapshot_completed_utc`. The independent post-execution check found no issue update or new comments between each cutoff and engine execution.

Selection discovery also encountered GitHub search HTTP 422 for the prespecified `facebook/react` queue entry. No issue in that repository was inspected or counted; the next queued repositories supplied the 20 eligible cases. The original candidate manifest and selection lock remain unchanged.
