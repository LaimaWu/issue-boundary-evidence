# IBE longitudinal adjudication / outcome report

Dataset: ibe\-v0\.1\.0\-prospective · Frozen release: v0\.1\.0

Knowledge cutoff (recorded_at): 2026\-09\-27T01&#58;38&#58;50Z

Source study observation cutoff(s): 2026\-09\-26T23&#58;41&#58;39Z

Independent research layer. Frozen reports are immutable inputs. Issue closure does not establish a final research outcome. No accuracy score is computed.

Pre-freeze context is shown separately from post-freeze evidence. Claim status is recorded by the researcher; validation checks structure and provenance, not the truth of a claim.

Research snapshots retain source-assigned labels and are not upstream events. Imported summaries are secondary provenance, not freshly fetched GitHub records. source_recorded is a lossless transport state, not a success score.

## Case overview

| Case | Issue state | Research outcome | Review status |
|---|---|---|---|
| 01\-scikit\-learn\-scikit\-learn\-34977 | closed | unresolved | current as recorded |
| 02\-scikit\-learn\-scikit\-learn\-34975 | open | unresolved | current as recorded |
| 03\-astral\-sh\-uv\-21829 | open | unresolved | current as recorded |
| 04\-astral\-sh\-uv\-21720 | open | unresolved | current as recorded |
| 05\-matplotlib\-matplotlib\-32339 | closed | unresolved | current as recorded |
| 06\-matplotlib\-matplotlib\-32329 | open | unresolved | current as recorded |
| 07\-pydantic\-pydantic\-13835 | closed | unresolved | current as recorded |
| 08\-pydantic\-pydantic\-13834 | open | unresolved | current as recorded |
| 09\-psf\-requests\-7620 | open | unresolved | current as recorded |
| 10\-psf\-requests\-7610 | open | unresolved | current as recorded |

## 01\-scikit\-learn\-scikit\-learn\-34977

Issue: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34977

Frozen at: 2026\-09\-19T11&#58;43&#58;15Z

Frozen report: frozen/01\-scikit\-learn\-scikit\-learn\-34977/report\.md

SHA-256: `b6aa3961affa123b9db077ddfe6b55b3d7b315183df5d5094272d2e8b83ebf9d`

### Dimension adjudication

| Dimension | Frozen alignment / verdict | Source status | Source evidence basis | Record |
|---|---|---|---|---|
| phenomenon | partial\_pre\_freeze | supported | observed\_fact | study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-phenomenon |
| cause | unresolved | unresolved | researcher\_inference | study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-cause |
| ownership | unresolved | unresolved | researcher\_inference | study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-ownership |
| severity | not\_claimed | provisional | researcher\_inference | study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-severity |
| fix\_trajectory | no\_prospective\_gain | closed\_without\_identified\_fix | observed\_fact | study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-fix\_trajectory |

### Evidence timeline

#### pre\_freeze\_context

No evidence imported for this scope.

#### post\_freeze

- **2026\-09\-23T04&#58;34&#58;55Z — study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-1** (comment\_edit; observed\_fact)
  - Statement: A bot comment created September 18 was edited to report a successful September 23 CI run; its creation date is not the success time\.
  - Source: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34977\#issuecomment\-5722880061; locator: /cases/0/evidence\_timeline/0; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): A bot comment created September 18 was edited to report a successful September 23 CI run; its creation date is not the success time\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-23T20&#58;56&#58;04Z — study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-2** (closed; observed\_fact)
  - Statement: A repository member closed the issue\.
  - Source: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34977; locator: /cases/0/evidence\_timeline/1; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): A repository member closed the issue\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

#### research\_snapshot

- **2026\-09\-26T23&#58;41&#58;39Z — study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;snapshot** (case\_state\_as\_of; observed\_fact)
  - Statement: At the 11&#58;43&#58;15 UTC snapshot the issue remained open\. A bot comment already pointed to a successful September 19 run; a maintainer comment included the cp314t Windows arm64 failure and ValueError trace\.
  - Source: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34977; locator: /cases/0; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): At the 11&#58;43&#58;15 UTC snapshot the issue remained open\. A bot comment already pointed to a successful September 19 run; a maintainer comment included the cp314t Windows arm64 failure and ValueError trace\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

### Source case research context

Study observation cutoff: 2026\-09\-26T23&#58;41&#58;39Z

Title: Wheel builder CI failure

Freeze context: At the 11&#58;43&#58;15 UTC snapshot the issue remained open\. A bot comment already pointed to a successful September 19 run; a maintainer comment included the cp314t Windows arm64 failure and ValueError trace\.

Frozen-report summary: ABI/wheel, joblib and parallel were flagged strong; the report also recorded a successful CI run already visible at freeze\.

Supported extraction: The report traced the Windows arm64 wheel job and cp314t tag to a comment\.

Misses / noise: \`joblib\` appears in a stack frame and \`parallel\` is also an API name; later success and closure identify no cause, so neither strong boundary is validated\. The bot success mentioned in the report was already known on September 19\.

Literal report signals: \[&quot;strong\_clue joblib&quot;, &quot;strong\_clue parallel&quot;, &quot;successful CI run 35419499583 already present at freeze&quot;\]

Temporal conclusion: later closure and a new bot success\-run link do not confirm the flagged package boundaries

Assessment scope: Alignment means the report’s evidence orientation versus available pre\-freeze information and later independent record\. It is not a numerical accuracy score or claim of maintainer use\.

Snapshot diff: \{&quot;surviving\_comment\_ids\_added\_after\_freeze&quot;&#58; \[\], &quot;frozen\_comment\_ids\_no\_longer\_present&quot;&#58; \[\], &quot;surviving\_comment\_ids\_with\_body\_edit&quot;&#58; \[5722880061\], &quot;issue\_body\_changed\_as\_of&quot;&#58; false, &quot;note&quot;&#58; &quot;A current\-state diff cannot reconstruct deleted comments that appeared and disappeared between snapshots\.&quot;\}

Linked PRs (source state at cutoff):

- None recorded.

Release / backport evidence:

- None recorded.

Source: study\-20260927\-adjudication\-recovered\-json /cases/0

### Adjudication and outcome history (append order)

#### study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-phenomenon — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: phenomenon; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: ABI/wheel, joblib and parallel were flagged strong; the report also recorded a successful CI run already visible at freeze\.

Source dimension status: supported; source evidence basis: observed\_fact; frozen alignment: partial\_pre\_freeze

Source evidence URLs: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34977\#issuecomment\-5723076602, https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34977\#issuecomment\-5722880061

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/0

Rationale: CI wheel build failed on cp314t Windows arm64; later run succeeded\.

Evidence: study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;snapshot, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-1, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-2

Unresolved questions:

- None recorded.

#### study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-cause — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: cause; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: ABI/wheel, joblib and parallel were flagged strong; the report also recorded a successful CI run already visible at freeze\.

Source dimension status: unresolved; source evidence basis: researcher\_inference; frozen alignment: unresolved

Source evidence URLs: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34977\#issuecomment\-5723076602

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/0

Rationale: Exact underlying cause and reason for recovery are unconfirmed; exception alone does not establish a code defect\.

Evidence: study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;snapshot, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-1, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-2

Unresolved questions:

- None recorded.

#### study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-ownership — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: ownership; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: ABI/wheel, joblib and parallel were flagged strong; the report also recorded a successful CI run already visible at freeze\.

Source dimension status: unresolved; source evidence basis: researcher\_inference; frozen alignment: unresolved

Source evidence URLs: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34977

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/0

Rationale: Repository CI incident; ownership of the underlying fault is undetermined\.

Evidence: study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;snapshot, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-1, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-2

Unresolved questions:

- None recorded.

#### study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-severity — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: severity; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: ABI/wheel, joblib and parallel were flagged strong; the report also recorded a successful CI run already visible at freeze\.

Source dimension status: provisional; source evidence basis: researcher\_inference; frozen alignment: not\_claimed

Source evidence URLs: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34977\#issuecomment\-5723076602

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/0

Rationale: Build pipeline interruption, scope limited to observed wheel job; wider release impact unproven\.

Evidence: study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;snapshot, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-1, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-2

Unresolved questions:

- None recorded.

#### study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-fix\_trajectory — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: fix\_trajectory; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: ABI/wheel, joblib and parallel were flagged strong; the report also recorded a successful CI run already visible at freeze\.

Source dimension status: closed\_without\_identified\_fix; source evidence basis: observed\_fact; frozen alignment: no\_prospective\_gain

Source evidence URLs: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34977\#issuecomment\-5722880061, https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34977

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/0

Rationale: A successful run preceded closure; no linked repair PR or release was established\.

Evidence: study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;snapshot, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-1, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-2

Unresolved questions:

- None recorded.

#### study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;outcome — outcome

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Source disposition (verbatim): closed\_without\_identified\_fix. Generic resolution remains unknown because the import does not infer a normalized resolution or finality.

Outcome: unresolved; issue: closed; resolution: unknown

Dimension records: study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-phenomenon, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-cause, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-ownership, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-severity, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;dimension\-fix\_trajectory

Rationale: A successful run preceded closure; no linked repair PR or release was established\.

Evidence: study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;snapshot, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-1, study\-20260927&#58;01\-scikit\-learn\-scikit\-learn\-34977&#58;timeline\-2

Unresolved questions:

- Failure mechanism
- Whether a particular code or infrastructure change caused recovery


## 02\-scikit\-learn\-scikit\-learn\-34975

Issue: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34975

Frozen at: 2026\-09\-19T11&#58;43&#58;17Z

Frozen report: frozen/02\-scikit\-learn\-scikit\-learn\-34975/report\.md

SHA-256: `27ff56a24e509e25a3e589f48d9ac6b903ca22ba1326c77cb62c5b6f7f6f10be`

### Dimension adjudication

| Dimension | Frozen alignment / verdict | Source status | Source evidence basis | Record |
|---|---|---|---|---|
| phenomenon | partial\_pre\_freeze | reported\_unconfirmed | observed\_fact | study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-phenomenon |
| cause | unresolved | unresolved | researcher\_inference | study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-cause |
| ownership | misleading\_boundary | provisional | maintainer\_confirmed\_fact | study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-ownership |
| severity | not\_claimed | provisional | researcher\_inference | study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-severity |
| fix\_trajectory | unresolved | open\_pr | observed\_fact | study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-fix\_trajectory |

### Evidence timeline

#### pre\_freeze\_context

- **2026\-09\-17T13&#58;51&#58;51Z — study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;linked\_prs\-1\-opened\_utc** (opened\_utc; observed\_fact)
  - Statement: Source records opened\_utc=2026\-09\-17T13&#58;51&#58;51Z\. Other fields describe state at study cutoff\.
  - Source: https&#58;//github\.com/scikit\-learn/scikit\-learn/pull/34980; locator: /cases/1/linked\_prs/0; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Source records opened\_utc=2026\-09\-17T13&#58;51&#58;51Z\. Other fields describe state at study cutoff\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

#### post\_freeze

No evidence imported for this scope.

#### research\_snapshot

- **2026\-09\-26T23&#58;41&#58;39Z — study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;snapshot** (case\_state\_as\_of; observed\_fact)
  - Statement: At the 11&#58;43&#58;17 UTC snapshot the issue remained open\. Reporter proposed a float32 count\-cast regression in scikit\-learn; maintainer had invited a PR and \#34980 was already open\.
  - Source: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34975; locator: /cases/1; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): At the 11&#58;43&#58;17 UTC snapshot the issue remained open\. Reporter proposed a float32 count\-cast regression in scikit\-learn; maintainer had invited a PR and \#34980 was already open\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

### Source case research context

Study observation cutoff: 2026\-09\-26T23&#58;41&#58;39Z

Title: float32 scores and ranking count precision

Freeze context: At the 11&#58;43&#58;17 UTC snapshot the issue remained open\. Reporter proposed a float32 count\-cast regression in scikit\-learn; maintainer had invited a PR and \#34980 was already open\.

Frozen-report summary: The report surfaced the author’s claimed NumPy float32 regression and linked a contributor fork, but promoted that fork as an external\-repository boundary\.

Supported extraction: Version/regression clue and source location in ranking metrics were traceable before freeze\.

Misses / noise: \`ammar\-iitm/scikit\-learn\` is a proposed fix branch, not a plausible upstream owner; NumPy is the input backend while the proposed cast is in scikit\-learn\. PR \#34980 is still unmerged and root cause lacks a new maintainer conclusion\.

Literal report signals: \[&quot;strong\_clue regression from \#34817&quot;, &quot;strong\_clue external repo ammar\-iitm/scikit\-learn&quot;, &quot;strong\_clue numpy&quot;\]

Temporal conclusion: no independent post\-freeze resolution

Assessment scope: Alignment means the report’s evidence orientation versus available pre\-freeze information and later independent record\. It is not a numerical accuracy score or claim of maintainer use\.

Snapshot diff: \{&quot;surviving\_comment\_ids\_added\_after\_freeze&quot;&#58; \[\], &quot;frozen\_comment\_ids\_no\_longer\_present&quot;&#58; \[\], &quot;surviving\_comment\_ids\_with\_body\_edit&quot;&#58; \[\], &quot;issue\_body\_changed\_as\_of&quot;&#58; false, &quot;note&quot;&#58; &quot;A current\-state diff cannot reconstruct deleted comments that appeared and disappeared between snapshots\.&quot;\}

Linked PRs (source state at cutoff):

- \{&quot;url&quot;&#58; &quot;https&#58;//github\.com/scikit\-learn/scikit\-learn/pull/34980&quot;, &quot;state&quot;&#58; &quot;open&quot;, &quot;merged&quot;&#58; false, &quot;opened\_utc&quot;&#58; &quot;2026\-09\-17T13&#58;51&#58;51Z&quot;\}

Release / backport evidence:

- None recorded.

Source: study\-20260927\-adjudication\-recovered\-json /cases/1

### Adjudication and outcome history (append order)

#### study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-phenomenon — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: phenomenon; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report surfaced the author’s claimed NumPy float32 regression and linked a contributor fork, but promoted that fork as an external\-repository boundary\.

Source dimension status: reported\_unconfirmed; source evidence basis: observed\_fact; frozen alignment: partial\_pre\_freeze

Source evidence URLs: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34975

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/1

Rationale: Reporter reproduces integer count rounding above 2\*\*24 when float32 scores are used on NumPy\.

Evidence: study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;snapshot, study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;linked\_prs\-1\-opened\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-cause — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: cause; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report surfaced the author’s claimed NumPy float32 regression and linked a contributor fork, but promoted that fork as an external\-repository boundary\.

Source dimension status: unresolved; source evidence basis: researcher\_inference; frozen alignment: unresolved

Source evidence URLs: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34975, https&#58;//github\.com/scikit\-learn/scikit\-learn/pull/34980

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/1

Rationale: Casting exact int64 counts to y\_score float32 is the reporter and PR author’s proposed mechanism; no later maintainer conclusion\.

Evidence: study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;snapshot, study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;linked\_prs\-1\-opened\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-ownership — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: ownership; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report surfaced the author’s claimed NumPy float32 regression and linked a contributor fork, but promoted that fork as an external\-repository boundary\.

Source dimension status: provisional; source evidence basis: maintainer\_confirmed\_fact; frozen alignment: misleading\_boundary

Source evidence URLs: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34975\#issuecomment\-5715288844, https&#58;//github\.com/scikit\-learn/scikit\-learn/pull/34980

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/1

Rationale: Proposed fix targets scikit\-learn ranking metrics; maintainer invited PR before freeze\.

Evidence: study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;snapshot, study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;linked\_prs\-1\-opened\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-severity — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: severity; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report surfaced the author’s claimed NumPy float32 regression and linked a contributor fork, but promoted that fork as an external\-repository boundary\.

Source dimension status: provisional; source evidence basis: researcher\_inference; frozen alignment: not\_claimed

Source evidence URLs: https&#58;//github\.com/scikit\-learn/scikit\-learn/issues/34975

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/1

Rationale: Potential silent numerical imprecision on large inputs; frequency and production impact unmeasured\.

Evidence: study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;snapshot, study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;linked\_prs\-1\-opened\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-fix\_trajectory — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: fix\_trajectory; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report surfaced the author’s claimed NumPy float32 regression and linked a contributor fork, but promoted that fork as an external\-repository boundary\.

Source dimension status: open\_pr; source evidence basis: observed\_fact; frozen alignment: unresolved

Source evidence URLs: https&#58;//github\.com/scikit\-learn/scikit\-learn/pull/34980

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/1

Rationale: \#34980 remains open and unmerged as of cutoff; no release or backport evidenced\.

Evidence: study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;snapshot, study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;linked\_prs\-1\-opened\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;outcome — outcome

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Source disposition (verbatim): open\_pr. Generic resolution remains unknown because the import does not infer a normalized resolution or finality.

Outcome: unresolved; issue: open; resolution: unknown

Dimension records: study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-phenomenon, study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-cause, study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-ownership, study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-severity, study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;dimension\-fix\_trajectory

Rationale: \#34980 remains open and unmerged as of cutoff; no release or backport evidenced\.

Evidence: study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;snapshot, study\-20260927&#58;02\-scikit\-learn\-scikit\-learn\-34975&#58;linked\_prs\-1\-opened\_utc

Unresolved questions:

- Maintainer validation of regression cause
- PR review, merge and release


## 03\-astral\-sh\-uv\-21829

Issue: https&#58;//github\.com/astral\-sh/uv/issues/21829

Frozen at: 2026\-09\-19T11&#58;43&#58;20Z

Frozen report: frozen/03\-astral\-sh\-uv\-21829/report\.md

SHA-256: `4f3423d816b53256fc521ff7fcb1c836ae06249b38f91e48ec35029fce002c4b`

### Dimension adjudication

| Dimension | Frozen alignment / verdict | Source status | Source evidence basis | Record |
|---|---|---|---|---|
| phenomenon | undercovered\_at\_freeze | supported | observed\_fact | study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-phenomenon |
| cause | missed\_pre\_freeze\_maintainer\_context | supported | maintainer\_confirmed\_fact | study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-cause |
| ownership | unresolved | provisional | researcher\_inference | study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-ownership |
| severity | not\_claimed | provisional | researcher\_inference | study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-severity |
| fix\_trajectory | unresolved | unresolved | observed\_fact | study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-fix\_trajectory |

### Evidence timeline

#### pre\_freeze\_context

No evidence imported for this scope.

#### post\_freeze

- **2026\-09\-21T12&#58;19&#58;20Z — study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;timeline\-1** (subscription; observed\_fact)
  - Statement: A user subscribed; no substantive comment or resolution followed\.
  - Source: https&#58;//github\.com/astral\-sh/uv/issues/21829; locator: /cases/2/evidence\_timeline/0; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): A user subscribed; no substantive comment or resolution followed\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

#### research\_snapshot

- **2026\-09\-26T23&#58;41&#58;39Z — study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;snapshot** (case\_state\_as\_of; observed\_fact)
  - Statement: At the 11&#58;43&#58;20 UTC snapshot the issue remained open\. Maintainer had corrected the initial symlink\-only premise and pointed to cache prune; reporter still requested individual distribution management\.
  - Source: https&#58;//github\.com/astral\-sh/uv/issues/21829; locator: /cases/2; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): At the 11&#58;43&#58;20 UTC snapshot the issue remained open\. Maintainer had corrected the initial symlink\-only premise and pointed to cache prune; reporter still requested individual distribution management\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

### Source case research context

Study observation cutoff: 2026\-09\-26T23&#58;41&#58;39Z

Title: Granular cache management

Freeze context: At the 11&#58;43&#58;20 UTC snapshot the issue remained open\. Maintainer had corrected the initial symlink\-only premise and pointed to cache prune; reporter still requested individual distribution management\.

Frozen-report summary: No meaningful cache/API boundary was extracted; the report elevated ordinary dependency upgrades as regression language and the example torch version as a version fact\.

Supported extraction: Cited the exact user example, with no invented version\.

Misses / noise: \`torch==2\.14\.0\+cu132\` was an illustrative distribution, not the uv version or a confirmed regression; the pre\-freeze maintainer correction about reflinks/hardlinks and \`uv cache prune\` was missed\.

Literal report signals: \[&quot;no boundary candidates&quot;, &quot;strong\_clue upgrade prose as regression&quot;, &quot;example torch 2\.14\.0&quot;\]

Temporal conclusion: no substantive post\-freeze maintainer outcome

Assessment scope: Alignment means the report’s evidence orientation versus available pre\-freeze information and later independent record\. It is not a numerical accuracy score or claim of maintainer use\.

Snapshot diff: \{&quot;surviving\_comment\_ids\_added\_after\_freeze&quot;&#58; \[\], &quot;frozen\_comment\_ids\_no\_longer\_present&quot;&#58; \[\], &quot;surviving\_comment\_ids\_with\_body\_edit&quot;&#58; \[\], &quot;issue\_body\_changed\_as\_of&quot;&#58; false, &quot;note&quot;&#58; &quot;A current\-state diff cannot reconstruct deleted comments that appeared and disappeared between snapshots\.&quot;\}

Linked PRs (source state at cutoff):

- None recorded.

Release / backport evidence:

- None recorded.

Source: study\-20260927\-adjudication\-recovered\-json /cases/2

### Adjudication and outcome history (append order)

#### study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-phenomenon — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: phenomenon; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: No meaningful cache/API boundary was extracted; the report elevated ordinary dependency upgrades as regression language and the example torch version as a version fact\.

Source dimension status: supported; source evidence basis: observed\_fact; frozen alignment: undercovered\_at\_freeze

Source evidence URLs: https&#58;//github\.com/astral\-sh/uv/issues/21829

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/2

Rationale: Feature request for listing and pruning particular cached distributions; no verified failure in existing cache prune\.

Evidence: study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;snapshot, study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;timeline\-1

Unresolved questions:

- None recorded.

#### study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-cause — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: cause; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: No meaningful cache/API boundary was extracted; the report elevated ordinary dependency upgrades as regression language and the example torch version as a version fact\.

Source dimension status: supported; source evidence basis: maintainer\_confirmed\_fact; frozen alignment: missed\_pre\_freeze\_maintainer\_context

Source evidence URLs: https&#58;//github\.com/astral\-sh/uv/issues/21829\#issuecomment\-5734801101, https&#58;//github\.com/astral\-sh/uv/issues/21829\#issuecomment\-5735325203

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/2

Rationale: Request concerns missing granularity; initial premise that only symlinks avoid duplication was corrected by maintainer before freeze\.

Evidence: study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;snapshot, study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;timeline\-1

Unresolved questions:

- None recorded.

#### study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-ownership — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: ownership; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: No meaningful cache/API boundary was extracted; the report elevated ordinary dependency upgrades as regression language and the example torch version as a version fact\.

Source dimension status: provisional; source evidence basis: researcher\_inference; frozen alignment: unresolved

Source evidence URLs: https&#58;//github\.com/astral\-sh/uv/issues/21829

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/2

Rationale: Requested interface belongs to uv; local Windows filesystem and package sizes affect the motivating example\.

Evidence: study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;snapshot, study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;timeline\-1

Unresolved questions:

- None recorded.

#### study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-severity — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: severity; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: No meaningful cache/API boundary was extracted; the report elevated ordinary dependency upgrades as regression language and the example torch version as a version fact\.

Source dimension status: provisional; source evidence basis: researcher\_inference; frozen alignment: not\_claimed

Source evidence URLs: https&#58;//github\.com/astral\-sh/uv/issues/21829\#issuecomment\-5735325203

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/2

Rationale: Potential high disk/network cost for specific large packages, quantified impact absent\.

Evidence: study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;snapshot, study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;timeline\-1

Unresolved questions:

- None recorded.

#### study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-fix\_trajectory — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: fix\_trajectory; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: No meaningful cache/API boundary was extracted; the report elevated ordinary dependency upgrades as regression language and the example torch version as a version fact\.

Source dimension status: unresolved; source evidence basis: observed\_fact; frozen alignment: unresolved

Source evidence URLs: https&#58;//github\.com/astral\-sh/uv/issues/21829

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/2

Rationale: Issue remains open with no linked merged PR or release conclusion after freeze\.

Evidence: study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;snapshot, study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;timeline\-1

Unresolved questions:

- None recorded.

#### study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;outcome — outcome

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Source disposition (verbatim): unresolved. Generic resolution remains unknown because the import does not infer a normalized resolution or finality.

Outcome: unresolved; issue: open; resolution: unknown

Dimension records: study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-phenomenon, study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-cause, study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-ownership, study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-severity, study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;dimension\-fix\_trajectory

Rationale: Issue remains open with no linked merged PR or release conclusion after freeze\.

Evidence: study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;snapshot, study\-20260927&#58;03\-astral\-sh\-uv\-21829&#58;timeline\-1

Unresolved questions:

- Whether maintainers accept the requested granularity
- Implementation scope


## 04\-astral\-sh\-uv\-21720

Issue: https&#58;//github\.com/astral\-sh/uv/issues/21720

Frozen at: 2026\-09\-19T11&#58;43&#58;22Z

Frozen report: frozen/04\-astral\-sh\-uv\-21720/report\.md

SHA-256: `b1c7e815fbf05d19b634eedc3cca80cc650796f7d3f7202a27a5a889f3f65a31`

### Dimension adjudication

| Dimension | Frozen alignment / verdict | Source status | Source evidence basis | Record |
|---|---|---|---|---|
| phenomenon | partial\_pre\_freeze | supported | observed\_fact | study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-phenomenon |
| cause | missed\_pre\_freeze\_maintainer\_context | supported | maintainer\_confirmed\_fact | study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-cause |
| ownership | misleading\_boundary | supported | researcher\_inference | study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-ownership |
| severity | not\_claimed | provisional | researcher\_inference | study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-severity |
| fix\_trajectory | missed\_pre\_freeze\_release | partial\_pre\_freeze | observed\_fact | study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-fix\_trajectory |

### Evidence timeline

#### pre\_freeze\_context

- **2026\-09\-17T14&#58;26&#58;25Z — study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-2\-merged\_utc** (merged\_utc; observed\_fact)
  - Statement: Source records merged\_utc=2026\-09\-17T14&#58;26&#58;25Z\. Other fields describe state at study cutoff\.
  - Source: https&#58;//github\.com/astral\-sh/ruff/pull/28646; locator: /cases/3/linked\_prs/1; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Source records merged\_utc=2026\-09\-17T14&#58;26&#58;25Z\. Other fields describe state at study cutoff\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-17T14&#58;33&#58;03Z — study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-1\-merged\_utc** (merged\_utc; observed\_fact)
  - Statement: Source records merged\_utc=2026\-09\-17T14&#58;33&#58;03Z\. Other fields describe state at study cutoff\.
  - Source: https&#58;//github\.com/astral\-sh/uv/pull/21744; locator: /cases/3/linked\_prs/0; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Source records merged\_utc=2026\-09\-17T14&#58;33&#58;03Z\. Other fields describe state at study cutoff\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-18T01&#58;01&#58;42Z — study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;release\_and\_backport\-1\-published\_utc** (published\_utc; observed\_fact)
  - Statement: Source records published\_utc=2026\-09\-18T01&#58;01&#58;42Z\. Other fields describe state at study cutoff\.
  - Source: https&#58;//github\.com/astral\-sh/uv/releases/tag/0\.12\.16; locator: /cases/3/release\_and\_backport/0; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Source records published\_utc=2026\-09\-18T01&#58;01&#58;42Z\. Other fields describe state at study cutoff\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

#### post\_freeze

No evidence imported for this scope.

#### research\_snapshot

- **2026\-09\-26T23&#58;41&#58;39Z — study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;snapshot** (case\_state\_as\_of; observed\_fact)
  - Statement: At the 11&#58;43&#58;22 UTC snapshot the issue remained open\. Maintainer had explained intentional environment preference; uv \#21744 and ty \#28646 were merged and uv 0\.12\.16 had been published\.
  - Source: https&#58;//github\.com/astral\-sh/uv/issues/21720; locator: /cases/3; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): At the 11&#58;43&#58;22 UTC snapshot the issue remained open\. Maintainer had explained intentional environment preference; uv \#21744 and ty \#28646 were merged and uv 0\.12\.16 had been published\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

### Source case research context

Study observation cutoff: 2026\-09\-26T23&#58;41&#58;39Z

Title: uv check and ty check Python\-version divergence

Freeze context: At the 11&#58;43&#58;22 UTC snapshot the issue remained open\. Maintainer had explained intentional environment preference; uv \#21744 and ty \#28646 were merged and uv 0\.12\.16 had been published\.

Frozen-report summary: The report captured Python, uv and ty environment versions, but its sole strong boundary was the placeholder project named \`demo\`\.

Supported extraction: Faithfully extracted Python and uv version facts\.

Misses / noise: It omitted the pre\-freeze maintainer explanation contrasting current \`\.venv\` with \`requires\-python\`, and did not surface the already merged uv/ty PRs or uv 0\.12\.16\. \`demo\` is a minimal\-example name, not a dependency boundary\.

Literal report signals: \[&quot;strong\_clue demo&quot;, &quot;missing uv/ty semantics&quot;, &quot;missing pre\-freeze partial fixes&quot;\]

Temporal conclusion: the issue remains open; release evidence predates freeze

Assessment scope: Alignment means the report’s evidence orientation versus available pre\-freeze information and later independent record\. It is not a numerical accuracy score or claim of maintainer use\.

Snapshot diff: \{&quot;surviving\_comment\_ids\_added\_after\_freeze&quot;&#58; \[\], &quot;frozen\_comment\_ids\_no\_longer\_present&quot;&#58; \[\], &quot;surviving\_comment\_ids\_with\_body\_edit&quot;&#58; \[\], &quot;issue\_body\_changed\_as\_of&quot;&#58; false, &quot;note&quot;&#58; &quot;A current\-state diff cannot reconstruct deleted comments that appeared and disappeared between snapshots\.&quot;\}

Linked PRs (source state at cutoff):

- \{&quot;url&quot;&#58; &quot;https&#58;//github\.com/astral\-sh/uv/pull/21744&quot;, &quot;state&quot;&#58; &quot;closed&quot;, &quot;merged&quot;&#58; true, &quot;merged\_utc&quot;&#58; &quot;2026\-09\-17T14&#58;33&#58;03Z&quot;\}
- \{&quot;url&quot;&#58; &quot;https&#58;//github\.com/astral\-sh/ruff/pull/28646&quot;, &quot;state&quot;&#58; &quot;closed&quot;, &quot;merged&quot;&#58; true, &quot;merged\_utc&quot;&#58; &quot;2026\-09\-17T14&#58;26&#58;25Z&quot;\}

Release / backport evidence:

- \{&quot;url&quot;&#58; &quot;https&#58;//github\.com/astral\-sh/uv/releases/tag/0\.12\.16&quot;, &quot;version&quot;&#58; &quot;0\.12\.16&quot;, &quot;published\_utc&quot;&#58; &quot;2026\-09\-18T01&#58;01&#58;42Z&quot;, &quot;relationship&quot;&#58; &quot;Lists uv \#21744; before freeze&quot;\}

Source: study\-20260927\-adjudication\-recovered\-json /cases/3

### Adjudication and outcome history (append order)

#### study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-phenomenon — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: phenomenon; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report captured Python, uv and ty environment versions, but its sole strong boundary was the placeholder project named \`demo\`\.

Source dimension status: supported; source evidence basis: observed\_fact; frozen alignment: partial\_pre\_freeze

Source evidence URLs: https&#58;//github\.com/astral\-sh/uv/issues/21720

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/3

Rationale: The two commands can report different diagnostics from different effective Python version choices\.

Evidence: study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;snapshot, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-1\-merged\_utc, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-2\-merged\_utc, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;release\_and\_backport\-1\-published\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-cause — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: cause; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report captured Python, uv and ty environment versions, but its sole strong boundary was the placeholder project named \`demo\`\.

Source dimension status: supported; source evidence basis: maintainer\_confirmed\_fact; frozen alignment: missed\_pre\_freeze\_maintainer\_context

Source evidence URLs: https&#58;//github\.com/astral\-sh/uv/issues/21720\#issuecomment\-5695949350, https&#58;//github\.com/astral\-sh/uv/pull/21744, https&#58;//github\.com/astral\-sh/ruff/pull/28646

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/3

Rationale: Maintainer explains uv prefers current environment while ty reads project support floor; explicit \-\-python forwarding was separately changed\.

Evidence: study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;snapshot, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-1\-merged\_utc, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-2\-merged\_utc, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;release\_and\_backport\-1\-published\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-ownership — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: ownership; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report captured Python, uv and ty environment versions, but its sole strong boundary was the placeholder project named \`demo\`\.

Source dimension status: supported; source evidence basis: researcher\_inference; frozen alignment: misleading\_boundary

Source evidence URLs: https&#58;//github\.com/astral\-sh/uv/issues/21720\#issuecomment\-5695949350, https&#58;//github\.com/astral\-sh/uv/pull/21744, https&#58;//github\.com/astral\-sh/ruff/pull/28646

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/3

Rationale: Cross\-component uv/ty behavioral contract, rather than evidence that one checker is categorically broken\.

Evidence: study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;snapshot, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-1\-merged\_utc, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-2\-merged\_utc, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;release\_and\_backport\-1\-published\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-severity — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: severity; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report captured Python, uv and ty environment versions, but its sole strong boundary was the placeholder project named \`demo\`\.

Source dimension status: provisional; source evidence basis: researcher\_inference; frozen alignment: not\_claimed

Source evidence URLs: https&#58;//github\.com/astral\-sh/uv/issues/21720

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/3

Rationale: Surprising check discrepancy, with documented workaround; no measured prevalence\.

Evidence: study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;snapshot, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-1\-merged\_utc, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-2\-merged\_utc, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;release\_and\_backport\-1\-published\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-fix\_trajectory — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: fix\_trajectory; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report captured Python, uv and ty environment versions, but its sole strong boundary was the placeholder project named \`demo\`\.

Source dimension status: partial\_pre\_freeze; source evidence basis: observed\_fact; frozen alignment: missed\_pre\_freeze\_release

Source evidence URLs: https&#58;//github\.com/astral\-sh/uv/issues/21720, https&#58;//github\.com/astral\-sh/uv/pull/21744, https&#58;//github\.com/astral\-sh/ruff/pull/28646, https&#58;//github\.com/astral\-sh/uv/releases/tag/0\.12\.16

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/3

Rationale: Narrow changes merged and uv \#21744 was listed in 0\.12\.16 before freeze; default discrepancy remains an open issue\.

Evidence: study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;snapshot, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-1\-merged\_utc, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-2\-merged\_utc, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;release\_and\_backport\-1\-published\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;outcome — outcome

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Source disposition (verbatim): partial\_pre\_freeze. Generic resolution remains unknown because the import does not infer a normalized resolution or finality.

Outcome: unresolved; issue: open; resolution: unknown

Dimension records: study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-phenomenon, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-cause, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-ownership, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-severity, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;dimension\-fix\_trajectory

Rationale: Narrow changes merged and uv \#21744 was listed in 0\.12\.16 before freeze; default discrepancy remains an open issue\.

Evidence: study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;snapshot, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-1\-merged\_utc, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;linked\_prs\-2\-merged\_utc, study\-20260927&#58;04\-astral\-sh\-uv\-21720&#58;release\_and\_backport\-1\-published\_utc

Unresolved questions:

- Whether default behaviors should converge
- Any later version\-specific regression conclusion


## 05\-matplotlib\-matplotlib\-32339

Issue: https&#58;//github\.com/matplotlib/matplotlib/issues/32339

Frozen at: 2026\-09\-19T11&#58;43&#58;25Z

Frozen report: frozen/05\-matplotlib\-matplotlib\-32339/report\.md

SHA-256: `46e9615bee88cfffe76d902ba0d4ba00f2c8890b5d2fee5a2cfa2fbf0ac0f8b6`

### Dimension adjudication

| Dimension | Frozen alignment / verdict | Source status | Source evidence basis | Record |
|---|---|---|---|---|
| phenomenon | supported | supported | observed\_fact | study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-phenomenon |
| cause | directionally\_supported\_post\_freeze | supported\_original\_only | maintainer\_confirmed\_fact | study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-cause |
| ownership | directionally\_supported\_post\_freeze | supported | researcher\_inference | study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-ownership |
| severity | not\_claimed | provisional | researcher\_inference | study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-severity |
| fix\_trajectory | not\_claimed | main\_merged\_backport\_unresolved | observed\_fact | study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-fix\_trajectory |

### Evidence timeline

#### pre\_freeze\_context

No evidence imported for this scope.

#### post\_freeze

- **2026\-09\-19T16&#58;49&#58;52Z — study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-1** (ci\_bump\_new\_blocker; observed\_fact)
  - Statement: A contributor narrowed a new macOS 26 interactive\-framework crash to framework load order while the CI\-image PR was being tested\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/pull/32372\#issuecomment\-5743638528; locator: /cases/4/evidence\_timeline/0; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): A contributor narrowed a new macOS 26 interactive\-framework crash to framework load order while the CI\-image PR was being tested\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-19T17&#58;01&#58;41Z — study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-2** (related\_pr\_opened; observed\_fact)
  - Statement: PR \#32376 opened to load AppKit before CoreText, a blocker encountered while testing the builder\-image change\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/pull/32376; locator: /cases/4/evidence\_timeline/1; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): PR \#32376 opened to load AppKit before CoreText, a blocker encountered while testing the builder\-image change\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-19T18&#58;48&#58;59Z — study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-3** (conditional\_review; observed\_fact)
  - Statement: Contributor review approved \#32372 conditional on \#32376 landing\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/pull/32372; locator: /cases/4/evidence\_timeline/2; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Contributor review approved \#32372 conditional on \#32376 landing\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-19T19&#58;03&#58;14Z — study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-4** (platform\_scope\_clarification; observed\_fact)
  - Statement: Contributor clarified macOS 10\.14 and macOS 14 are different releases, limiting an overly broad reading of usage statistics\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/pull/32372\#issuecomment\-5744556853; locator: /cases/4/evidence\_timeline/3; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Contributor clarified macOS 10\.14 and macOS 14 are different releases, limiting an overly broad reading of usage statistics\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-23T00&#58;54&#58;33Z — study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-2\-merged\_utc** (merged\_utc; observed\_fact)
  - Statement: Source records merged\_utc=2026\-09\-23T00&#58;54&#58;33Z\. Other fields describe state at study cutoff\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/pull/32376; locator: /cases/4/linked\_prs/1; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Source records merged\_utc=2026\-09\-23T00&#58;54&#58;33Z\. Other fields describe state at study cutoff\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-23T00&#58;54&#58;33Z — study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-5** (related\_pr\_merged; observed\_fact)
  - Statement: The separate macOS framework\-load PR \#32376 merged before the CI\-image PR\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/pull/32376; locator: /cases/4/evidence\_timeline/4; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): The separate macOS framework\-load PR \#32376 merged before the CI\-image PR\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-23T15&#58;19&#58;01Z — study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-1\-merged\_utc** (merged\_utc; observed\_fact)
  - Statement: Source records merged\_utc=2026\-09\-23T15&#58;19&#58;01Z\. Other fields describe state at study cutoff\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/pull/32372; locator: /cases/4/linked\_prs/0; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Source records merged\_utc=2026\-09\-23T15&#58;19&#58;01Z\. Other fields describe state at study cutoff\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-23T15&#58;19&#58;01Z — study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-6** (pr\_merged; observed\_fact)
  - Statement: PR \#32372 changed macOS CI builder images and explicitly marked the issue fixed; merged to main\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/pull/32372; locator: /cases/4/evidence\_timeline/5; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): PR \#32372 changed macOS CI builder images and explicitly marked the issue fixed; merged to main\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-23T15&#58;19&#58;02Z — study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-7** (closed; observed\_fact)
  - Statement: Issue closed one second after PR merge\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/issues/32339; locator: /cases/4/evidence\_timeline/6; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Issue closed one second after PR merge\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-25T20&#58;21&#58;25Z — study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-8** (backport\_discussion; maintainer\_confirmed\_fact)
  - Statement: Maintainer said they were debating a 3\.11 backport as CI was failing again, with a possible new LLVM problem\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/pull/32372\#issuecomment\-5839025923; locator: /cases/4/evidence\_timeline/7; author: Not named in supplied research; attribution retained from source (maintainer)
  - Excerpt (research\_summary): Maintainer said they were debating a 3\.11 backport as CI was failing again, with a possible new LLVM problem\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-25T22&#58;36&#58;03Z — study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-9** (backport\_discussion; observed\_fact)
  - Statement: Contributor supported backporting the CI change without treating it as a user\-platform support drop\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/pull/32372\#issuecomment\-5840606172; locator: /cases/4/evidence\_timeline/8; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Contributor supported backporting the CI change without treating it as a user\-platform support drop\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-26T02&#58;23&#58;26Z — study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-10** (cause\_discussion; observed\_fact)
  - Statement: Contributor described Homebrew on macOS 14 and earlier as unreliable under its Tier 3 policy\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/pull/32372\#issuecomment\-5842344428; locator: /cases/4/evidence\_timeline/9; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Contributor described Homebrew on macOS 14 and earlier as unreliable under its Tier 3 policy\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

#### research\_snapshot

- **2026\-09\-26T23&#58;41&#58;39Z — study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;snapshot** (case\_state\_as\_of; observed\_fact)
  - Statement: At the 11&#58;43&#58;25 UTC snapshot the issue remained open\. Homebrew macOS 14 bottle failure and a proposed CI\-image change were already public; \#32372 was open but not merged\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/issues/32339; locator: /cases/4; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): At the 11&#58;43&#58;25 UTC snapshot the issue remained open\. Homebrew macOS 14 bottle failure and a proposed CI\-image change were already public; \#32372 was open but not merged\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

### Source case research context

Study observation cutoff: 2026\-09\-26T23&#58;41&#58;39Z

Title: macOS 14 CI dependency installation

Freeze context: At the 11&#58;43&#58;25 UTC snapshot the issue remained open\. Homebrew macOS 14 bottle failure and a proposed CI\-image change were already public; \#32372 was open but not merged\.

Frozen-report summary: The report flagged Homebrew/homebrew\-core as a strong external boundary and cited the formula change\.

Supported extraction: Directionally consistent with the later merged CI\-builder change and the discussion of Homebrew’s support tier\.

Misses / noise: Homebrew was explicit in the issue body, so this is extraction of pre\-existing evidence, not an independently discovered cause\. Five Python\-version facts from a background compatibility table add noise; the subsequent LLVM failure/backport remains separate and unresolved\.

Literal report signals: \[&quot;strong\_clue Homebrew/homebrew\-core&quot;, &quot;macOS platform&quot;, &quot;five Python versions from background table&quot;\]

Temporal conclusion: one useful boundary aligned with later PR merge, without a novel pre\-resolution prediction

Assessment scope: Alignment means the report’s evidence orientation versus available pre\-freeze information and later independent record\. It is not a numerical accuracy score or claim of maintainer use\.

Snapshot diff: \{&quot;surviving\_comment\_ids\_added\_after\_freeze&quot;&#58; \[\], &quot;frozen\_comment\_ids\_no\_longer\_present&quot;&#58; \[\], &quot;surviving\_comment\_ids\_with\_body\_edit&quot;&#58; \[\], &quot;issue\_body\_changed\_as\_of&quot;&#58; false, &quot;note&quot;&#58; &quot;A current\-state diff cannot reconstruct deleted comments that appeared and disappeared between snapshots\.&quot;\}

Linked PRs (source state at cutoff):

- \{&quot;url&quot;&#58; &quot;https&#58;//github\.com/matplotlib/matplotlib/pull/32372&quot;, &quot;state&quot;&#58; &quot;closed&quot;, &quot;merged&quot;&#58; true, &quot;merged\_utc&quot;&#58; &quot;2026\-09\-23T15&#58;19&#58;01Z&quot;, &quot;commit&quot;&#58; &quot;a8cabafa9a9b80f59ca5eee929ac02f4649b9851&quot;\}
- \{&quot;url&quot;&#58; &quot;https&#58;//github\.com/matplotlib/matplotlib/pull/32376&quot;, &quot;state&quot;&#58; &quot;closed&quot;, &quot;merged&quot;&#58; true, &quot;merged\_utc&quot;&#58; &quot;2026\-09\-23T00&#58;54&#58;33Z&quot;, &quot;commit&quot;&#58; &quot;4836ff616ccbd79f6499e84aebc4451e1d77c94a&quot;, &quot;relationship&quot;&#58; &quot;Separate blocker on macOS 26 encountered by \#32372, not the original macOS 14 Homebrew issue&quot;\}

Release / backport evidence:

- \{&quot;status&quot;&#58; &quot;no\_post\_freeze\_release\_found&quot;, &quot;note&quot;&#58; &quot;Latest checked Matplotlib GitHub release v3\.11\.2 was September 11; backport discussion September 25–26\.&quot;, &quot;url&quot;&#58; &quot;https&#58;//github\.com/matplotlib/matplotlib/releases&quot;\}

Source: study\-20260927\-adjudication\-recovered\-json /cases/4

### Adjudication and outcome history (append order)

#### study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-phenomenon — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: phenomenon; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report flagged Homebrew/homebrew\-core as a strong external boundary and cited the formula change\.

Source dimension status: supported; source evidence basis: observed\_fact; frozen alignment: supported

Source evidence URLs: https&#58;//github\.com/matplotlib/matplotlib/issues/32339, https&#58;//github\.com/matplotlib/matplotlib/pull/32372\#issuecomment\-5839025923

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/4

Rationale: macOS 14 CI package installation became unreliable; later CI failures persisted in a possible separate LLVM path\.

Evidence: study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;snapshot, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-1, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-2, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-3, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-4, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-5, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-6, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-7, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-8, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-9, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-10, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-1\-merged\_utc, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-2\-merged\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-cause — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: cause; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report flagged Homebrew/homebrew\-core as a strong external boundary and cited the formula change\.

Source dimension status: supported\_original\_only; source evidence basis: maintainer\_confirmed\_fact; frozen alignment: directionally\_supported\_post\_freeze

Source evidence URLs: https&#58;//github\.com/matplotlib/matplotlib/issues/32339, https&#58;//github\.com/matplotlib/matplotlib/pull/32372\#issuecomment\-5839025923, https&#58;//github\.com/matplotlib/matplotlib/pull/32372\#issuecomment\-5842344428

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/4

Rationale: Homebrew support and bottle availability are the maintained explanation of the original failure; later LLVM failure not established as same cause\.

Evidence: study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;snapshot, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-1, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-2, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-3, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-4, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-5, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-6, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-7, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-8, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-9, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-10, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-1\-merged\_utc, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-2\-merged\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-ownership — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: ownership; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report flagged Homebrew/homebrew\-core as a strong external boundary and cited the formula change\.

Source dimension status: supported; source evidence basis: researcher\_inference; frozen alignment: directionally\_supported\_post\_freeze

Source evidence URLs: https&#58;//github\.com/matplotlib/matplotlib/issues/32339, https&#58;//github\.com/matplotlib/matplotlib/pull/32372

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/4

Rationale: CI image choice is Matplotlib’s; upstream Homebrew package support is outside its repository\.

Evidence: study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;snapshot, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-1, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-2, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-3, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-4, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-5, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-6, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-7, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-8, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-9, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-10, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-1\-merged\_utc, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-2\-merged\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-severity — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: severity; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report flagged Homebrew/homebrew\-core as a strong external boundary and cited the formula change\.

Source dimension status: provisional; source evidence basis: researcher\_inference; frozen alignment: not\_claimed

Source evidence URLs: https&#58;//github\.com/matplotlib/matplotlib/issues/32339, https&#58;//github\.com/matplotlib/matplotlib/pull/32372\#issuecomment\-5840606172

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/4

Rationale: Active CI breakage; no evidence that installed Matplotlib stopped supporting macOS 14\.

Evidence: study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;snapshot, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-1, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-2, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-3, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-4, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-5, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-6, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-7, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-8, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-9, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-10, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-1\-merged\_utc, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-2\-merged\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-fix\_trajectory — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: fix\_trajectory; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report flagged Homebrew/homebrew\-core as a strong external boundary and cited the formula change\.

Source dimension status: main\_merged\_backport\_unresolved; source evidence basis: observed\_fact; frozen alignment: not\_claimed

Source evidence URLs: https&#58;//github\.com/matplotlib/matplotlib/pull/32372, https&#58;//github\.com/matplotlib/matplotlib/issues/32339, https&#58;//github\.com/matplotlib/matplotlib/pull/32372\#issuecomment\-5839025923

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/4

Rationale: Main\-branch CI builder update merged and issue closed; backport was being debated, no 3\.11 release/backport verified\.

Evidence: study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;snapshot, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-1, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-2, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-3, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-4, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-5, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-6, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-7, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-8, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-9, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-10, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-1\-merged\_utc, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-2\-merged\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;outcome — outcome

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Source disposition (verbatim): main\_merged\_backport\_unresolved. Generic resolution remains unknown because the import does not infer a normalized resolution or finality.

Outcome: unresolved; issue: closed; resolution: unknown

Dimension records: study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-phenomenon, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-cause, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-ownership, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-severity, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;dimension\-fix\_trajectory

Rationale: Main\-branch CI builder update merged and issue closed; backport was being debated, no 3\.11 release/backport verified\.

Evidence: study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;snapshot, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-1, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-2, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-3, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-4, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-5, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-6, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-7, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-8, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-9, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;timeline\-10, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-1\-merged\_utc, study\-20260927&#58;05\-matplotlib\-matplotlib\-32339&#58;linked\_prs\-2\-merged\_utc

Unresolved questions:

- Whether the CI change was backported to v3\.11\.x
- Cause of renewed LLVM failures


## 06\-matplotlib\-matplotlib\-32329

Issue: https&#58;//github\.com/matplotlib/matplotlib/issues/32329

Frozen at: 2026\-09\-19T11&#58;43&#58;28Z

Frozen report: frozen/06\-matplotlib\-matplotlib\-32329/report\.md

SHA-256: `426e5fe4f1a325a8f83217642f8cc0a63eb9dc9c98e3e4a86902820f03a22f00`

### Dimension adjudication

| Dimension | Frozen alignment / verdict | Source status | Source evidence basis | Record |
|---|---|---|---|---|
| phenomenon | not\_characterized | reported\_unconfirmed | observed\_fact | study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-phenomenon |
| cause | abstention | unresolved | researcher\_inference | study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-cause |
| ownership | abstention | provisional | researcher\_inference | study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-ownership |
| severity | not\_claimed | provisional | researcher\_inference | study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-severity |
| fix\_trajectory | unresolved | unresolved | observed\_fact | study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-fix\_trajectory |

### Evidence timeline

#### pre\_freeze\_context

No evidence imported for this scope.

#### post\_freeze

No evidence imported for this scope.

#### research\_snapshot

- **2026\-09\-26T23&#58;41&#58;39Z — study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;snapshot** (case\_state\_as\_of; observed\_fact)
  - Statement: At the 11&#58;43&#58;28 UTC snapshot the issue remained open\. The author described overlapping\-path containment as inconsistent with fill rules and deferred a change to a later PR\.
  - Source: https&#58;//github\.com/matplotlib/matplotlib/issues/32329; locator: /cases/5; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): At the 11&#58;43&#58;28 UTC snapshot the issue remained open\. The author described overlapping\-path containment as inconsistent with fill rules and deferred a change to a later PR\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

### Source case research context

Study observation cutoff: 2026\-09\-26T23&#58;41&#58;39Z

Title: contains\(\) and fill\-rule inconsistency

Freeze context: At the 11&#58;43&#58;28 UTC snapshot the issue remained open\. The author described overlapping\-path containment as inconsistent with fill rules and deferred a change to a later PR\.

Frozen-report summary: The report explicitly abstained&#58; “No major boundary evidence found\.”

Supported extraction: Reasonable abstention for an internal geometry/fill\-rule semantic issue, while preserving its code and PR links\.

Misses / noise: The actual path\-containment issue remains unresolved; no later evidence can establish the final semantics or correctness of the cited internal link\.

Literal report signals: \[&quot;No major boundary evidence found&quot;, &quot;same\-repository \#32253 metadata&quot;\]

Temporal conclusion: no substantive post\-freeze outcome

Assessment scope: Alignment means the report’s evidence orientation versus available pre\-freeze information and later independent record\. It is not a numerical accuracy score or claim of maintainer use\.

Snapshot diff: \{&quot;surviving\_comment\_ids\_added\_after\_freeze&quot;&#58; \[\], &quot;frozen\_comment\_ids\_no\_longer\_present&quot;&#58; \[\], &quot;surviving\_comment\_ids\_with\_body\_edit&quot;&#58; \[\], &quot;issue\_body\_changed\_as\_of&quot;&#58; false, &quot;note&quot;&#58; &quot;A current\-state diff cannot reconstruct deleted comments that appeared and disappeared between snapshots\.&quot;\}

Linked PRs (source state at cutoff):

- None recorded.

Release / backport evidence:

- None recorded.

Source: study\-20260927\-adjudication\-recovered\-json /cases/5

### Adjudication and outcome history (append order)

#### study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-phenomenon — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: phenomenon; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report explicitly abstained&#58; “No major boundary evidence found\.”

Source dimension status: reported\_unconfirmed; source evidence basis: observed\_fact; frozen alignment: not\_characterized

Source evidence URLs: https&#58;//github\.com/matplotlib/matplotlib/issues/32329

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/5

Rationale: Reporter’s examples show path contains\(\) can disagree with both fill rules for overlapping subpaths\.

Evidence: study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;snapshot

Unresolved questions:

- None recorded.

#### study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-cause — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: cause; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report explicitly abstained&#58; “No major boundary evidence found\.”

Source dimension status: unresolved; source evidence basis: researcher\_inference; frozen alignment: abstention

Source evidence URLs: https&#58;//github\.com/matplotlib/matplotlib/issues/32329

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/5

Rationale: Reporter attributes behavior to point\_in\_path\_impl handling each subpath and combining membership; no later maintainer conclusion\.

Evidence: study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;snapshot

Unresolved questions:

- None recorded.

#### study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-ownership — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: ownership; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report explicitly abstained&#58; “No major boundary evidence found\.”

Source dimension status: provisional; source evidence basis: researcher\_inference; frozen alignment: abstention

Source evidence URLs: https&#58;//github\.com/matplotlib/matplotlib/issues/32329

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/5

Rationale: Candidate fix would connect Matplotlib fill\-rule choice to path containment internals\.

Evidence: study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;snapshot

Unresolved questions:

- None recorded.

#### study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-severity — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: severity; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report explicitly abstained&#58; “No major boundary evidence found\.”

Source dimension status: provisional; source evidence basis: researcher\_inference; frozen alignment: not\_claimed

Source evidence URLs: https&#58;//github\.com/matplotlib/matplotlib/issues/32329

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/5

Rationale: Hit testing mismatch for special overlapping paths; user impact unmeasured\.

Evidence: study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;snapshot

Unresolved questions:

- None recorded.

#### study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-fix\_trajectory — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: fix\_trajectory; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report explicitly abstained&#58; “No major boundary evidence found\.”

Source dimension status: unresolved; source evidence basis: observed\_fact; frozen alignment: unresolved

Source evidence URLs: https&#58;//github\.com/matplotlib/matplotlib/issues/32329

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/5

Rationale: Open; no new linked fix PR, release, or backport after freeze\.

Evidence: study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;snapshot

Unresolved questions:

- None recorded.

#### study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;outcome — outcome

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Source disposition (verbatim): unresolved. Generic resolution remains unknown because the import does not infer a normalized resolution or finality.

Outcome: unresolved; issue: open; resolution: unknown

Dimension records: study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-phenomenon, study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-cause, study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-ownership, study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-severity, study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;dimension\-fix\_trajectory

Rationale: Open; no new linked fix PR, release, or backport after freeze\.

Evidence: study\-20260927&#58;06\-matplotlib\-matplotlib\-32329&#58;snapshot

Unresolved questions:

- Chosen semantic rule
- Fix plan and version


## 07\-pydantic\-pydantic\-13835

Issue: https&#58;//github\.com/pydantic/pydantic/issues/13835

Frozen at: 2026\-09\-19T11&#58;43&#58;30Z

Frozen report: frozen/07\-pydantic\-pydantic\-13835/report\.md

SHA-256: `00d8100444c6a2889303acd034a2468ba9c8c770bac670ad82f18907bb2b2bbf`

### Dimension adjudication

| Dimension | Frozen alignment / verdict | Source status | Source evidence basis | Record |
|---|---|---|---|---|
| phenomenon | confirmed\_post\_freeze | confirmed | maintainer\_confirmed\_fact | study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-phenomenon |
| cause | partial | partially\_confirmed | maintainer\_confirmed\_fact | study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-cause |
| ownership | missed\_later\_scope | confirmed\_scope | maintainer\_confirmed\_fact | study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-ownership |
| severity | not\_claimed | provisional | researcher\_inference | study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-severity |
| fix\_trajectory | no\_fix\_not\_predicted | closed\_no\_fix | maintainer\_confirmed\_fact | study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-fix\_trajectory |

### Evidence timeline

#### pre\_freeze\_context

- **2026\-09\-19T01&#58;00&#58;39Z — study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;linked\_prs\-1\-closed\_utc** (closed\_utc; observed\_fact)
  - Statement: Source records closed\_utc=2026\-09\-19T01&#58;00&#58;39Z\. Other fields describe state at study cutoff\.
  - Source: https&#58;//github\.com/pydantic/pydantic/pull/13836; locator: /cases/6/linked\_prs/0; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Source records closed\_utc=2026\-09\-19T01&#58;00&#58;39Z\. Other fields describe state at study cutoff\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

#### post\_freeze

- **2026\-09\-21T02&#58;14&#58;46Z — study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-1** (contributor\_comment; observed\_fact)
  - Statement: Contributor asked for assignment to reopen \#13836 after adjusting tests\.
  - Source: https&#58;//github\.com/pydantic/pydantic/issues/13835\#issuecomment\-5754533343; locator: /cases/6/evidence\_timeline/0; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Contributor asked for assignment to reopen \#13836 after adjusting tests\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-25T02&#58;28&#58;13Z — study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-2** (maintainer\_conclusion; maintainer\_confirmed\_fact)
  - Statement: Repository member confirmed module cannot be imported, said no v2 entry point registers it and it is private, and preferred leaving it unchanged; closed issue\.
  - Source: https&#58;//github\.com/pydantic/pydantic/issues/13835\#issuecomment\-5825685645; locator: /cases/6/evidence\_timeline/1; author: Not named in supplied research; attribution retained from source (maintainer)
  - Excerpt (research\_summary): Repository member confirmed module cannot be imported, said no v2 entry point registers it and it is private, and preferred leaving it unchanged; closed issue\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

#### research\_snapshot

- **2026\-09\-26T23&#58;41&#58;39Z — study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;snapshot** (case\_state\_as\_of; observed\_fact)
  - Statement: At the 11&#58;43&#58;30 UTC snapshot the issue remained open\. Reporter and outside contributor had reproduced a private v1 plugin import failure, and \#13836 had been bot\-closed for lack of assignment\.
  - Source: https&#58;//github\.com/pydantic/pydantic/issues/13835; locator: /cases/6; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): At the 11&#58;43&#58;30 UTC snapshot the issue remained open\. Reporter and outside contributor had reproduced a private v1 plugin import failure, and \#13836 had been bot\-closed for lack of assignment\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

### Source case research context

Study observation cutoff: 2026\-09\-26T23&#58;41&#58;39Z

Title: v1 Hypothesis plugin import under v2

Freeze context: At the 11&#58;43&#58;30 UTC snapshot the issue remained open\. Reporter and outside contributor had reproduced a private v1 plugin import failure, and \#13836 had been bot\-closed for lack of assignment\.

Frozen-report summary: The report listed v2/Python versions and contributor assertions that a fix and regression test were ready; it did not identify the public/private module scope\.

Supported extraction: The title and cited reports accurately identify an import failure, later acknowledged by a repository member\.

Misses / noise: Later maintainer concluded the module is private and not registered in v2, and declined repair\. A proposed PR and regression test are not evidence of an accepted fix or version regression; report did not resolve that distinction\.

Literal report signals: \[&quot;import failure in title&quot;, &quot;contributor fix and regression\-test text&quot;, &quot;private/entry\-point scope absent&quot;\]

Temporal conclusion: phenomenon confirmed but no\-fix ownership/scope conclusion was not anticipated

Assessment scope: Alignment means the report’s evidence orientation versus available pre\-freeze information and later independent record\. It is not a numerical accuracy score or claim of maintainer use\.

Snapshot diff: \{&quot;surviving\_comment\_ids\_added\_after\_freeze&quot;&#58; \[5754533343, 5825685645\], &quot;frozen\_comment\_ids\_no\_longer\_present&quot;&#58; \[\], &quot;surviving\_comment\_ids\_with\_body\_edit&quot;&#58; \[\], &quot;issue\_body\_changed\_as\_of&quot;&#58; false, &quot;note&quot;&#58; &quot;A current\-state diff cannot reconstruct deleted comments that appeared and disappeared between snapshots\.&quot;\}

Linked PRs (source state at cutoff):

- \{&quot;url&quot;&#58; &quot;https&#58;//github\.com/pydantic/pydantic/pull/13836&quot;, &quot;state&quot;&#58; &quot;closed&quot;, &quot;merged&quot;&#58; false, &quot;closed\_utc&quot;&#58; &quot;2026\-09\-19T01&#58;00&#58;39Z&quot;\}

Release / backport evidence:

- None recorded.

Source: study\-20260927\-adjudication\-recovered\-json /cases/6

### Adjudication and outcome history (append order)

#### study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-phenomenon — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: phenomenon; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report listed v2/Python versions and contributor assertions that a fix and regression test were ready; it did not identify the public/private module scope\.

Source dimension status: confirmed; source evidence basis: maintainer\_confirmed\_fact; frozen alignment: confirmed\_post\_freeze

Source evidence URLs: https&#58;//github\.com/pydantic/pydantic/issues/13835\#issuecomment\-5825685645

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/6

Rationale: Private v1 Hypothesis module is not importable under v2; maintainer agrees\.

Evidence: study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;snapshot, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-1, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-2, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;linked\_prs\-1\-closed\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-cause — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: cause; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report listed v2/Python versions and contributor assertions that a fix and regression test were ready; it did not identify the public/private module scope\.

Source dimension status: partially\_confirmed; source evidence basis: maintainer\_confirmed\_fact; frozen alignment: partial

Source evidence URLs: https&#58;//github\.com/pydantic/pydantic/issues/13835, https&#58;//github\.com/pydantic/pydantic/issues/13835\#issuecomment\-5825685645

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/6

Rationale: No v2 entry point registers the private module; the import failure itself remains, while precise import statements were established by reporter/contributor\.

Evidence: study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;snapshot, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-1, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-2, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;linked\_prs\-1\-closed\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-ownership — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: ownership; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report listed v2/Python versions and contributor assertions that a fix and regression test were ready; it did not identify the public/private module scope\.

Source dimension status: confirmed\_scope; source evidence basis: maintainer\_confirmed\_fact; frozen alignment: missed\_later\_scope

Source evidence URLs: https&#58;//github\.com/pydantic/pydantic/issues/13835\#issuecomment\-5825685645

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/6

Rationale: Maintainer judges it outside a supported v2 public integration and prefers no change\.

Evidence: study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;snapshot, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-1, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-2, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;linked\_prs\-1\-closed\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-severity — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: severity; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report listed v2/Python versions and contributor assertions that a fix and regression test were ready; it did not identify the public/private module scope\.

Source dimension status: provisional; source evidence basis: researcher\_inference; frozen alignment: not\_claimed

Source evidence URLs: https&#58;//github\.com/pydantic/pydantic/issues/13835\#issuecomment\-5825685645

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/6

Rationale: Direct private\-module import is broken, but no supported v2 entry point invokes it; low demonstrated product impact\.

Evidence: study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;snapshot, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-1, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-2, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;linked\_prs\-1\-closed\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-fix\_trajectory — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: fix\_trajectory; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report listed v2/Python versions and contributor assertions that a fix and regression test were ready; it did not identify the public/private module scope\.

Source dimension status: closed\_no\_fix; source evidence basis: maintainer\_confirmed\_fact; frozen alignment: no\_fix\_not\_predicted

Source evidence URLs: https&#58;//github\.com/pydantic/pydantic/issues/13835\#issuecomment\-5825685645, https&#58;//github\.com/pydantic/pydantic/pull/13836

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/6

Rationale: Issue closed without fix; \#13836 never merged; maintainer explicitly declined change\.

Evidence: study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;snapshot, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-1, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-2, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;linked\_prs\-1\-closed\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;outcome — outcome

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Source disposition (verbatim): closed\_no\_fix. Generic resolution remains unknown because the import does not infer a normalized resolution or finality.

Outcome: unresolved; issue: closed; resolution: unknown

Dimension records: study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-phenomenon, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-cause, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-ownership, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-severity, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;dimension\-fix\_trajectory

Rationale: Issue closed without fix; \#13836 never merged; maintainer explicitly declined change\.

Evidence: study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;snapshot, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-1, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;timeline\-2, study\-20260927&#58;07\-pydantic\-pydantic\-13835&#58;linked\_prs\-1\-closed\_utc

Unresolved questions:

- Whether private module will eventually be removed


## 08\-pydantic\-pydantic\-13834

Issue: https&#58;//github\.com/pydantic/pydantic/issues/13834

Frozen at: 2026\-09\-19T11&#58;43&#58;34Z

Frozen report: frozen/08\-pydantic\-pydantic\-13834/report\.md

SHA-256: `a3febe6be5fd4e5878863a2e1ddfe0093cce1697b51a7b32e7564c741a812563`

### Dimension adjudication

| Dimension | Frozen alignment / verdict | Source status | Source evidence basis | Record |
|---|---|---|---|---|
| phenomenon | undercovered\_at\_freeze | supported\_reported | observed\_fact | study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-phenomenon |
| cause | undercovered\_at\_freeze | supported\_review | observed\_fact | study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-cause |
| ownership | unresolved | unresolved | researcher\_inference | study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-ownership |
| severity | not\_claimed | provisional | researcher\_inference | study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-severity |
| fix\_trajectory | unresolved | open\_no\_merged\_fix | observed\_fact | study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-fix\_trajectory |

### Evidence timeline

#### pre\_freeze\_context

No evidence imported for this scope.

#### post\_freeze

- **2026\-09\-20T14&#58;07&#58;36Z — study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-1** (pr\_review; observed\_fact)
  - Statement: A contributor reviewer approved \#13837 after a static typing regression case was added\.
  - Source: https&#58;//github\.com/pydantic/pydantic/pull/13837\#pullrequestreview\-5260777891; locator: /cases/7/evidence\_timeline/0; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): A contributor reviewer approved \#13837 after a static typing regression case was added\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-20T15&#58;15&#58;35Z — study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-1\-closed\_utc** (closed\_utc; observed\_fact)
  - Statement: Source records closed\_utc=2026\-09\-20T15&#58;15&#58;35Z\. Other fields describe state at study cutoff\.
  - Source: https&#58;//github\.com/pydantic/pydantic/pull/13837; locator: /cases/7/linked\_prs/0; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Source records closed\_utc=2026\-09\-20T15&#58;15&#58;35Z\. Other fields describe state at study cutoff\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-20T15&#58;15&#58;35Z — study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-2** (pr\_closed; observed\_fact)
  - Statement: Repository member closed \#13837 without merge; the available PR comments do not establish why\.
  - Source: https&#58;//github\.com/pydantic/pydantic/pull/13837; locator: /cases/7/evidence\_timeline/1; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Repository member closed \#13837 without merge; the available PR comments do not establish why\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-23T02&#58;29&#58;31Z — study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-3** (deleted\_comments; observed\_fact)
  - Statement: Four issue comment\-deletion events were logged; deleted content is unavailable and not interpreted\.
  - Source: https&#58;//github\.com/pydantic/pydantic/issues/13834; locator: /cases/7/evidence\_timeline/2; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Four issue comment\-deletion events were logged; deleted content is unavailable and not interpreted\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-23T05&#58;16&#58;04Z — study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-4** (new\_pr; observed\_fact)
  - Statement: \#13851 proposed a similar annotation widening\.
  - Source: https&#58;//github\.com/pydantic/pydantic/pull/13851; locator: /cases/7/evidence\_timeline/3; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): \#13851 proposed a similar annotation widening\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-23T05&#58;16&#58;16Z — study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-2\-closed\_utc** (closed\_utc; observed\_fact)
  - Statement: Source records closed\_utc=2026\-09\-23T05&#58;16&#58;16Z\. Other fields describe state at study cutoff\.
  - Source: https&#58;//github\.com/pydantic/pydantic/pull/13851; locator: /cases/7/linked\_prs/1; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Source records closed\_utc=2026\-09\-23T05&#58;16&#58;16Z\. Other fields describe state at study cutoff\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

- **2026\-09\-23T05&#58;16&#58;16Z — study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-5** (pr\_closed; observed\_fact)
  - Statement: Bot closed \#13851 because the author was not assigned to the issue\.
  - Source: https&#58;//github\.com/pydantic/pydantic/pull/13851\#issuecomment\-5789492583; locator: /cases/7/evidence\_timeline/4; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Bot closed \#13851 because the author was not assigned to the issue\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

#### research\_snapshot

- **2026\-09\-26T23&#58;41&#58;39Z — study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;snapshot** (case\_state\_as\_of; observed\_fact)
  - Statement: At the 11&#58;43&#58;34 UTC snapshot the issue remained open\. Reporter described runtime acceptance and static annotation mismatch; contributor PR \#13837 had opened\.
  - Source: https&#58;//github\.com/pydantic/pydantic/issues/13834; locator: /cases/7; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): At the 11&#58;43&#58;34 UTC snapshot the issue remained open\. Reporter described runtime acceptance and static annotation mismatch; contributor PR \#13837 had opened\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

### Source case research context

Study observation cutoff: 2026\-09\-26T23&#58;41&#58;39Z

Title: create\_model \_\_validators\_\_ static annotation

Freeze context: At the 11&#58;43&#58;34 UTC snapshot the issue remained open\. Reporter described runtime acceptance and static annotation mismatch; contributor PR \#13837 had opened\.

Frozen-report summary: The report collected environment versions, earlier related \#9690/\#9697 and contributors’ proposed fixes; the type\-annotation mismatch itself was not promoted as the primary boundary\.

Supported extraction: The prior annotation\-history references are useful and traceable\.

Misses / noise: “Regression tests” were classified as regression language without showing a version regression\. The report did not retrieve \#13837 despite an issue comment naming it as a PR; later two related PRs closed unmerged, so readiness was not fix trajectory\.

Literal report signals: \[&quot;related \#9690/\#9697&quot;, &quot;strong\_clue regression\-test prose&quot;, &quot;unretrieved \#13837&quot;\]

Temporal conclusion: post\-freeze PR closures do not establish accepted fix

Assessment scope: Alignment means the report’s evidence orientation versus available pre\-freeze information and later independent record\. It is not a numerical accuracy score or claim of maintainer use\.

Snapshot diff: \{&quot;surviving\_comment\_ids\_added\_after\_freeze&quot;&#58; \[\], &quot;frozen\_comment\_ids\_no\_longer\_present&quot;&#58; \[\], &quot;surviving\_comment\_ids\_with\_body\_edit&quot;&#58; \[\], &quot;issue\_body\_changed\_as\_of&quot;&#58; false, &quot;note&quot;&#58; &quot;A current\-state diff cannot reconstruct deleted comments that appeared and disappeared between snapshots\.&quot;\}

Linked PRs (source state at cutoff):

- \{&quot;url&quot;&#58; &quot;https&#58;//github\.com/pydantic/pydantic/pull/13837&quot;, &quot;state&quot;&#58; &quot;closed&quot;, &quot;merged&quot;&#58; false, &quot;closed\_utc&quot;&#58; &quot;2026\-09\-20T15&#58;15&#58;35Z&quot;\}
- \{&quot;url&quot;&#58; &quot;https&#58;//github\.com/pydantic/pydantic/pull/13851&quot;, &quot;state&quot;&#58; &quot;closed&quot;, &quot;merged&quot;&#58; false, &quot;closed\_utc&quot;&#58; &quot;2026\-09\-23T05&#58;16&#58;16Z&quot;\}

Release / backport evidence:

- None recorded.

Source: study\-20260927\-adjudication\-recovered\-json /cases/7

### Adjudication and outcome history (append order)

#### study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-phenomenon — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: phenomenon; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report collected environment versions, earlier related \#9690/\#9697 and contributors’ proposed fixes; the type\-annotation mismatch itself was not promoted as the primary boundary\.

Source dimension status: supported\_reported; source evidence basis: observed\_fact; frozen alignment: undercovered\_at\_freeze

Source evidence URLs: https&#58;//github\.com/pydantic/pydantic/issues/13834, https&#58;//github\.com/pydantic/pydantic/pull/13837

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/7

Rationale: Reporter and contributors observe runtime acceptance with three static checkers rejecting the declared type\.

Evidence: study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;snapshot, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-1, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-2, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-3, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-4, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-5, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-1\-closed\_utc, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-2\-closed\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-cause — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: cause; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report collected environment versions, earlier related \#9690/\#9697 and contributors’ proposed fixes; the type\-annotation mismatch itself was not promoted as the primary boundary\.

Source dimension status: supported\_review; source evidence basis: observed\_fact; frozen alignment: undercovered\_at\_freeze

Source evidence URLs: https&#58;//github\.com/pydantic/pydantic/pull/13837

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/7

Rationale: Reviewer identified a static typing regression, since runtime tests already passed before annotation change\.

Evidence: study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;snapshot, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-1, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-2, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-3, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-4, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-5, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-1\-closed\_utc, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-2\-closed\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-ownership — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: ownership; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report collected environment versions, earlier related \#9690/\#9697 and contributors’ proposed fixes; the type\-annotation mismatch itself was not promoted as the primary boundary\.

Source dimension status: unresolved; source evidence basis: researcher\_inference; frozen alignment: unresolved

Source evidence URLs: https&#58;//github\.com/pydantic/pydantic/issues/13834, https&#58;//github\.com/pydantic/pydantic/pull/13837, https&#58;//github\.com/pydantic/pydantic/pull/13851

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/7

Rationale: Candidate annotation change is in Pydantic; maintainer has not stated final intended API type\.

Evidence: study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;snapshot, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-1, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-2, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-3, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-4, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-5, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-1\-closed\_utc, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-2\-closed\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-severity — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: severity; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report collected environment versions, earlier related \#9690/\#9697 and contributors’ proposed fixes; the type\-annotation mismatch itself was not promoted as the primary boundary\.

Source dimension status: provisional; source evidence basis: researcher\_inference; frozen alignment: not\_claimed

Source evidence URLs: https&#58;//github\.com/pydantic/pydantic/issues/13834

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/7

Rationale: Type\-checking friction with working runtime behavior; no measured usage impact\.

Evidence: study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;snapshot, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-1, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-2, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-3, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-4, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-5, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-1\-closed\_utc, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-2\-closed\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-fix\_trajectory — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: fix\_trajectory; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report collected environment versions, earlier related \#9690/\#9697 and contributors’ proposed fixes; the type\-annotation mismatch itself was not promoted as the primary boundary\.

Source dimension status: open\_no\_merged\_fix; source evidence basis: observed\_fact; frozen alignment: unresolved

Source evidence URLs: https&#58;//github\.com/pydantic/pydantic/pull/13837, https&#58;//github\.com/pydantic/pydantic/pull/13851, https&#58;//github\.com/pydantic/pydantic/issues/13834

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/7

Rationale: Both related PRs are closed unmerged; issue open; no release/backport\. Approval of \#13837 did not imply merge\.

Evidence: study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;snapshot, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-1, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-2, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-3, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-4, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-5, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-1\-closed\_utc, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-2\-closed\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;outcome — outcome

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Source disposition (verbatim): open\_no\_merged\_fix. Generic resolution remains unknown because the import does not infer a normalized resolution or finality.

Outcome: unresolved; issue: open; resolution: unknown

Dimension records: study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-phenomenon, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-cause, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-ownership, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-severity, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;dimension\-fix\_trajectory

Rationale: Both related PRs are closed unmerged; issue open; no release/backport\. Approval of \#13837 did not imply merge\.

Evidence: study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;snapshot, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-1, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-2, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-3, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-4, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;timeline\-5, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-1\-closed\_utc, study\-20260927&#58;08\-pydantic\-pydantic\-13834&#58;linked\_prs\-2\-closed\_utc

Unresolved questions:

- Reason maintainer closed approved \#13837
- Final accepted annotation and tests
- Deleted\-comment contents


## 09\-psf\-requests\-7620

Issue: https&#58;//github\.com/psf/requests/issues/7620

Frozen at: 2026\-09\-19T11&#58;43&#58;37Z

Frozen report: frozen/09\-psf\-requests\-7620/report\.md

SHA-256: `152f3d0b3165495b42e834f68c8889c72b5b4e2402dfbb93dc88fed323dda591`

### Dimension adjudication

| Dimension | Frozen alignment / verdict | Source status | Source evidence basis | Record |
|---|---|---|---|---|
| phenomenon | partial\_pre\_freeze | supported | observed\_fact | study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-phenomenon |
| cause | missed\_pre\_freeze\_maintainer\_context | confirmed | maintainer\_confirmed\_fact | study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-cause |
| ownership | undercovered\_at\_freeze | supported | researcher\_inference | study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-ownership |
| severity | not\_claimed | provisional | researcher\_inference | study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-severity |
| fix\_trajectory | unresolved | unresolved | observed\_fact | study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-fix\_trajectory |

### Evidence timeline

#### pre\_freeze\_context

- **2021\-11\-28T14&#58;32&#58;29Z — study\-20260927&#58;09\-psf\-requests\-7620&#58;linked\_prs\-1\-merged\_utc** (merged\_utc; observed\_fact)
  - Statement: Source records merged\_utc=2021\-11\-28T14&#58;32&#58;29Z\. Other fields describe state at study cutoff\.
  - Source: https&#58;//github\.com/psf/requests/pull/5410; locator: /cases/8/linked\_prs/0; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): Source records merged\_utc=2021\-11\-28T14&#58;32&#58;29Z\. Other fields describe state at study cutoff\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

#### post\_freeze

No evidence imported for this scope.

#### research\_snapshot

- **2026\-09\-26T23&#58;41&#58;39Z — study\-20260927&#58;09\-psf\-requests\-7620&#58;snapshot** (case\_state\_as\_of; observed\_fact)
  - Statement: At the 11&#58;43&#58;37 UTC snapshot the issue remained open\. Maintainer had already explained that historical \#5410 targeted master rather than main\.
  - Source: https&#58;//github\.com/psf/requests/issues/7620; locator: /cases/8; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): At the 11&#58;43&#58;37 UTC snapshot the issue remained open\. Maintainer had already explained that historical \#5410 targeted master rather than main\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

### Source case research context

Study observation cutoff: 2026\-09\-26T23&#58;41&#58;39Z

Title: Old PR merged to master but absent from main

Freeze context: At the 11&#58;43&#58;37 UTC snapshot the issue remained open\. Maintainer had already explained that historical \#5410 targeted master rather than main\.

Frozen-report summary: The report captured the historical merge SHA and PR \#5410 but did not surface the maintainer\-confirmed master/main branch divergence\.

Supported extraction: The historical commit and PR links are accurate and relevant\.

Misses / noise: The decisive explanation was in pre\-freeze maintainer comments; “next release” text was elevated as version/regression language although no release commitment followed\.

Literal report signals: \[&quot;historical merge commit&quot;, &quot;same\-repository PR \#5410&quot;, &quot;missing master/main branch distinction&quot;\]

Temporal conclusion: no substantive post\-freeze outcome

Assessment scope: Alignment means the report’s evidence orientation versus available pre\-freeze information and later independent record\. It is not a numerical accuracy score or claim of maintainer use\.

Snapshot diff: \{&quot;surviving\_comment\_ids\_added\_after\_freeze&quot;&#58; \[\], &quot;frozen\_comment\_ids\_no\_longer\_present&quot;&#58; \[\], &quot;surviving\_comment\_ids\_with\_body\_edit&quot;&#58; \[\], &quot;issue\_body\_changed\_as\_of&quot;&#58; false, &quot;note&quot;&#58; &quot;A current\-state diff cannot reconstruct deleted comments that appeared and disappeared between snapshots\.&quot;\}

Linked PRs (source state at cutoff):

- \{&quot;url&quot;&#58; &quot;https&#58;//github\.com/psf/requests/pull/5410&quot;, &quot;state&quot;&#58; &quot;closed&quot;, &quot;merged&quot;&#58; true, &quot;merged\_utc&quot;&#58; &quot;2021\-11\-28T14&#58;32&#58;29Z&quot;, &quot;base&quot;&#58; &quot;master&quot;, &quot;note&quot;&#58; &quot;Historical merge does not imply inclusion in main&quot;\}

Release / backport evidence:

- None recorded.

Source: study\-20260927\-adjudication\-recovered\-json /cases/8

### Adjudication and outcome history (append order)

#### study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-phenomenon — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: phenomenon; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report captured the historical merge SHA and PR \#5410 but did not surface the maintainer\-confirmed master/main branch divergence\.

Source dimension status: supported; source evidence basis: observed\_fact; frozen alignment: partial\_pre\_freeze

Source evidence URLs: https&#58;//github\.com/psf/requests/issues/7620, https&#58;//github\.com/psf/requests/pull/5410

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/8

Rationale: GitHub records historical \#5410 as merged, but that old master merge is absent from current main per issue report\.

Evidence: study\-20260927&#58;09\-psf\-requests\-7620&#58;snapshot, study\-20260927&#58;09\-psf\-requests\-7620&#58;linked\_prs\-1\-merged\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-cause — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: cause; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report captured the historical merge SHA and PR \#5410 but did not surface the maintainer\-confirmed master/main branch divergence\.

Source dimension status: confirmed; source evidence basis: maintainer\_confirmed\_fact; frozen alignment: missed\_pre\_freeze\_maintainer\_context

Source evidence URLs: https&#58;//github\.com/psf/requests/issues/7620\#issuecomment\-5626752874, https&#58;//github\.com/psf/requests/issues/7620\#issuecomment\-5701707334, https&#58;//github\.com/psf/requests/pull/5410

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/8

Rationale: Maintainer identified wrong base branch at master/main cutover\.

Evidence: study\-20260927&#58;09\-psf\-requests\-7620&#58;snapshot, study\-20260927&#58;09\-psf\-requests\-7620&#58;linked\_prs\-1\-merged\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-ownership — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: ownership; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report captured the historical merge SHA and PR \#5410 but did not surface the maintainer\-confirmed master/main branch divergence\.

Source dimension status: supported; source evidence basis: researcher\_inference; frozen alignment: undercovered\_at\_freeze

Source evidence URLs: https&#58;//github\.com/psf/requests/issues/7620, https&#58;//github\.com/psf/requests/pull/5410

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/8

Rationale: Historical repository branch management; not evidence of a current downstream package fault\.

Evidence: study\-20260927&#58;09\-psf\-requests\-7620&#58;snapshot, study\-20260927&#58;09\-psf\-requests\-7620&#58;linked\_prs\-1\-merged\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-severity — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: severity; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report captured the historical merge SHA and PR \#5410 but did not surface the maintainer\-confirmed master/main branch divergence\.

Source dimension status: provisional; source evidence basis: researcher\_inference; frozen alignment: not\_claimed

Source evidence URLs: https&#58;//github\.com/psf/requests/issues/7620\#issuecomment\-5701707334

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/8

Rationale: Old uncarried minor shebang change; maintainer found no other identified instances, broader loss unproven\.

Evidence: study\-20260927&#58;09\-psf\-requests\-7620&#58;snapshot, study\-20260927&#58;09\-psf\-requests\-7620&#58;linked\_prs\-1\-merged\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-fix\_trajectory — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: fix\_trajectory; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report captured the historical merge SHA and PR \#5410 but did not surface the maintainer\-confirmed master/main branch divergence\.

Source dimension status: unresolved; source evidence basis: observed\_fact; frozen alignment: unresolved

Source evidence URLs: https&#58;//github\.com/psf/requests/issues/7620

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/8

Rationale: No new PR on main, release or backport after freeze; issue remains open\.

Evidence: study\-20260927&#58;09\-psf\-requests\-7620&#58;snapshot, study\-20260927&#58;09\-psf\-requests\-7620&#58;linked\_prs\-1\-merged\_utc

Unresolved questions:

- None recorded.

#### study\-20260927&#58;09\-psf\-requests\-7620&#58;outcome — outcome

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Source disposition (verbatim): unresolved. Generic resolution remains unknown because the import does not infer a normalized resolution or finality.

Outcome: unresolved; issue: open; resolution: unknown

Dimension records: study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-phenomenon, study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-cause, study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-ownership, study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-severity, study\-20260927&#58;09\-psf\-requests\-7620&#58;dimension\-fix\_trajectory

Rationale: No new PR on main, release or backport after freeze; issue remains open\.

Evidence: study\-20260927&#58;09\-psf\-requests\-7620&#58;snapshot, study\-20260927&#58;09\-psf\-requests\-7620&#58;linked\_prs\-1\-merged\_utc

Unresolved questions:

- Whether change will be reapplied
- Whether any other historical PR was stranded


## 10\-psf\-requests\-7610

Issue: https&#58;//github\.com/psf/requests/issues/7610

Frozen at: 2026\-09\-19T11&#58;43&#58;41Z

Frozen report: frozen/10\-psf\-requests\-7610/report\.md

SHA-256: `b0a1a759232f2a7a19b413fd7e91b43e2d5fdecb0f65af3583e4ea015cccb6cb`

### Dimension adjudication

| Dimension | Frozen alignment / verdict | Source status | Source evidence basis | Record |
|---|---|---|---|---|
| phenomenon | partial\_pre\_freeze | supported | observed\_fact | study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-phenomenon |
| cause | supported\_pre\_freeze | confirmed\_policy | maintainer\_confirmed\_fact | study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-cause |
| ownership | supported\_pre\_freeze | supported | researcher\_inference | study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-ownership |
| severity | not\_claimed | provisional | researcher\_inference | study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-severity |
| fix\_trajectory | unresolved | deferred\_pre\_freeze | maintainer\_confirmed\_fact | study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-fix\_trajectory |

### Evidence timeline

#### pre\_freeze\_context

No evidence imported for this scope.

#### post\_freeze

No evidence imported for this scope.

#### research\_snapshot

- **2026\-09\-26T23&#58;41&#58;39Z — study\-20260927&#58;10\-psf\-requests\-7610&#58;snapshot** (case\_state\_as\_of; observed\_fact)
  - Statement: At the 11&#58;43&#58;41 UTC snapshot the issue remained open\. Maintainer had already justified retaining the classifier to support older setuptools and deferred removal\.
  - Source: https&#58;//github\.com/psf/requests/issues/7610; locator: /cases/9; author: Not named in supplied research; attribution retained from source (researcher)
  - Excerpt (research\_summary): At the 11&#58;43&#58;41 UTC snapshot the issue remained open\. Maintainer had already justified retaining the classifier to support older setuptools and deferred removal\.
  - Observed: 2026\-09\-26T23&#58;41&#58;39Z; recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); artifact: study\-20260927\-adjudication\-recovered\-json

### Source case research context

Study observation cutoff: 2026\-09\-26T23&#58;41&#58;39Z

Title: License classifier and SPDX metadata

Freeze context: At the 11&#58;43&#58;41 UTC snapshot the issue remained open\. Maintainer had already justified retaining the classifier to support older setuptools and deferred removal\.

Frozen-report summary: The report identified older setuptools compatibility as a strong package boundary, drawing from a maintainer comment beyond the initial issue body\.

Supported extraction: A useful traceable maintainer rationale&#58; preserving legacy build behavior is why the classifier remains\.

Misses / noise: It did not clearly distinguish maintainer’s deliberate compatibility choice from the reporter’s SBOM interpretation; generic talk of older versions was framed as version/regression language\. No new resolution followed\.

Literal report signals: \[&quot;strong\_clue setuptools&quot;, &quot;older versions regression language&quot;, &quot;maintainer comment beyond initial body&quot;\]

Temporal conclusion: useful pre\-freeze evidence extraction, not prospective confirmation

Assessment scope: Alignment means the report’s evidence orientation versus available pre\-freeze information and later independent record\. It is not a numerical accuracy score or claim of maintainer use\.

Snapshot diff: \{&quot;surviving\_comment\_ids\_added\_after\_freeze&quot;&#58; \[\], &quot;frozen\_comment\_ids\_no\_longer\_present&quot;&#58; \[\], &quot;surviving\_comment\_ids\_with\_body\_edit&quot;&#58; \[\], &quot;issue\_body\_changed\_as\_of&quot;&#58; false, &quot;note&quot;&#58; &quot;A current\-state diff cannot reconstruct deleted comments that appeared and disappeared between snapshots\.&quot;\}

Linked PRs (source state at cutoff):

- None recorded.

Release / backport evidence:

- None recorded.

Source: study\-20260927\-adjudication\-recovered\-json /cases/9

### Adjudication and outcome history (append order)

#### study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-phenomenon — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: phenomenon; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report identified older setuptools compatibility as a strong package boundary, drawing from a maintainer comment beyond the initial issue body\.

Source dimension status: supported; source evidence basis: observed\_fact; frozen alignment: partial\_pre\_freeze

Source evidence URLs: https&#58;//github\.com/psf/requests/issues/7610

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/9

Rationale: Metadata carries both an SPDX license and legacy classifier; downstream SBOM tooling emits redundant free\-text license\.

Evidence: study\-20260927&#58;10\-psf\-requests\-7610&#58;snapshot

Unresolved questions:

- None recorded.

#### study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-cause — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: cause; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report identified older setuptools compatibility as a strong package boundary, drawing from a maintainer comment beyond the initial issue body\.

Source dimension status: confirmed\_policy; source evidence basis: maintainer\_confirmed\_fact; frozen alignment: supported\_pre\_freeze

Source evidence URLs: https&#58;//github\.com/psf/requests/issues/7610\#issuecomment\-5427534997, https&#58;//github\.com/psf/requests/issues/7610

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/9

Rationale: Maintainer intentionally retains classifier for older setuptools users; reporter points to deprecation and downstream interpretation\.

Evidence: study\-20260927&#58;10\-psf\-requests\-7610&#58;snapshot

Unresolved questions:

- None recorded.

#### study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-ownership — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: ownership; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report identified older setuptools compatibility as a strong package boundary, drawing from a maintainer comment beyond the initial issue body\.

Source dimension status: supported; source evidence basis: researcher\_inference; frozen alignment: supported\_pre\_freeze

Source evidence URLs: https&#58;//github\.com/psf/requests/issues/7610\#issuecomment\-5427534997

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/9

Rationale: Compatibility choice in Requests packaging and SBOM interpretation downstream both contribute; maintainer explicitly declined immediate removal\.

Evidence: study\-20260927&#58;10\-psf\-requests\-7610&#58;snapshot

Unresolved questions:

- None recorded.

#### study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-severity — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: severity; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report identified older setuptools compatibility as a strong package boundary, drawing from a maintainer comment beyond the initial issue body\.

Source dimension status: provisional; source evidence basis: researcher\_inference; frozen alignment: not\_claimed

Source evidence URLs: https&#58;//github\.com/psf/requests/issues/7610\#issuecomment\-5460764689, https&#58;//github\.com/psf/requests/issues/7610\#issuecomment\-5427534997

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/9

Rationale: Downstream metadata noise with no blocking pipeline according to reporter; removal risks older build workflows per maintainer\.

Evidence: study\-20260927&#58;10\-psf\-requests\-7610&#58;snapshot

Unresolved questions:

- None recorded.

#### study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-fix\_trajectory — adjudication

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Dimension: fix\_trajectory; verdict: source\_recorded; basis: researcher\_inference

Frozen claim / omission: The report identified older setuptools compatibility as a strong package boundary, drawing from a maintainer comment beyond the initial issue body\.

Source dimension status: deferred\_pre\_freeze; source evidence basis: maintainer\_confirmed\_fact; frozen alignment: unresolved

Source evidence URLs: https&#58;//github\.com/psf/requests/issues/7610\#issuecomment\-5427534997, https&#58;//github\.com/psf/requests/issues/7610

Source pointer: study\-20260927\-adjudication\-recovered\-json /cases/9

Rationale: Deferred by maintainer before freeze; still open with no merged change or release\.

Evidence: study\-20260927&#58;10\-psf\-requests\-7610&#58;snapshot

Unresolved questions:

- None recorded.

#### study\-20260927&#58;10\-psf\-requests\-7610&#58;outcome — outcome

Recorded: 2026\-09\-27T01&#58;38&#58;50Z; actor: source\-study import \(no new adjudication\); supersedes: none

Source disposition (verbatim): deferred\_pre\_freeze. Generic resolution remains unknown because the import does not infer a normalized resolution or finality.

Outcome: unresolved; issue: open; resolution: unknown

Dimension records: study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-phenomenon, study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-cause, study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-ownership, study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-severity, study\-20260927&#58;10\-psf\-requests\-7610&#58;dimension\-fix\_trajectory

Rationale: Deferred by maintainer before freeze; still open with no merged change or release\.

Evidence: study\-20260927&#58;10\-psf\-requests\-7610&#58;snapshot

Unresolved questions:

- Criteria and date for future classifier removal

## Source artifact registry

| Artifact | Kind | Path | SHA-256 |
|---|---|---|---|
| freeze\-archive | freeze\_archive | sources/freeze\.zip | `f398678f387c4b37e4d08285a0637d70f653aa2aa536e032d58b06beb20ec070` |
| freeze\-checksums | freeze\_manifest | sources/SHA256SUMS\.txt | `3616906f8dd402fa8869a7d434d302e0640e21dee73c53f2d0b95ae58729fe47` |
| 01\-scikit\-learn\-scikit\-learn\-34977\-report | frozen\_report | frozen/01\-scikit\-learn\-scikit\-learn\-34977/report\.md | `b6aa3961affa123b9db077ddfe6b55b3d7b315183df5d5094272d2e8b83ebf9d` |
| 01\-scikit\-learn\-scikit\-learn\-34977\-metadata | frozen\_metadata | frozen/01\-scikit\-learn\-scikit\-learn\-34977/metadata\.json | `1032fafa059a9b98a79d8c25dc41e8320dc89f683d43b5c07e203ae798f37b19` |
| 02\-scikit\-learn\-scikit\-learn\-34975\-report | frozen\_report | frozen/02\-scikit\-learn\-scikit\-learn\-34975/report\.md | `27ff56a24e509e25a3e589f48d9ac6b903ca22ba1326c77cb62c5b6f7f6f10be` |
| 02\-scikit\-learn\-scikit\-learn\-34975\-metadata | frozen\_metadata | frozen/02\-scikit\-learn\-scikit\-learn\-34975/metadata\.json | `e01c408b84c3f0acfdd710f8454eca1857f7783232e2b41cbdd33e3c2496e437` |
| 03\-astral\-sh\-uv\-21829\-report | frozen\_report | frozen/03\-astral\-sh\-uv\-21829/report\.md | `4f3423d816b53256fc521ff7fcb1c836ae06249b38f91e48ec35029fce002c4b` |
| 03\-astral\-sh\-uv\-21829\-metadata | frozen\_metadata | frozen/03\-astral\-sh\-uv\-21829/metadata\.json | `891e6c405654c036046a7fe17f45a7fa6fa311309776a1ff4714b0151f6c3b7e` |
| 04\-astral\-sh\-uv\-21720\-report | frozen\_report | frozen/04\-astral\-sh\-uv\-21720/report\.md | `b1c7e815fbf05d19b634eedc3cca80cc650796f7d3f7202a27a5a889f3f65a31` |
| 04\-astral\-sh\-uv\-21720\-metadata | frozen\_metadata | frozen/04\-astral\-sh\-uv\-21720/metadata\.json | `7b39712b7993728c6dc35db96f6e26e3eba096ca01f8bf0a059b62d960365c2d` |
| 05\-matplotlib\-matplotlib\-32339\-report | frozen\_report | frozen/05\-matplotlib\-matplotlib\-32339/report\.md | `46e9615bee88cfffe76d902ba0d4ba00f2c8890b5d2fee5a2cfa2fbf0ac0f8b6` |
| 05\-matplotlib\-matplotlib\-32339\-metadata | frozen\_metadata | frozen/05\-matplotlib\-matplotlib\-32339/metadata\.json | `b774bcadd77bc9ed8f9c65c7fc616d3bad6eb4a10cafbce97976683d1483c042` |
| 06\-matplotlib\-matplotlib\-32329\-report | frozen\_report | frozen/06\-matplotlib\-matplotlib\-32329/report\.md | `426e5fe4f1a325a8f83217642f8cc0a63eb9dc9c98e3e4a86902820f03a22f00` |
| 06\-matplotlib\-matplotlib\-32329\-metadata | frozen\_metadata | frozen/06\-matplotlib\-matplotlib\-32329/metadata\.json | `ae5ca620620002526fed95124aa6cd883c7793ef8370b439fd5e35988667d434` |
| 07\-pydantic\-pydantic\-13835\-report | frozen\_report | frozen/07\-pydantic\-pydantic\-13835/report\.md | `00d8100444c6a2889303acd034a2468ba9c8c770bac670ad82f18907bb2b2bbf` |
| 07\-pydantic\-pydantic\-13835\-metadata | frozen\_metadata | frozen/07\-pydantic\-pydantic\-13835/metadata\.json | `23dc59d6b4222fecd30cf427395843c1653140580eadf5f811c5260874ac09da` |
| 08\-pydantic\-pydantic\-13834\-report | frozen\_report | frozen/08\-pydantic\-pydantic\-13834/report\.md | `a3febe6be5fd4e5878863a2e1ddfe0093cce1697b51a7b32e7564c741a812563` |
| 08\-pydantic\-pydantic\-13834\-metadata | frozen\_metadata | frozen/08\-pydantic\-pydantic\-13834/metadata\.json | `548a3ceffa6e31a35e3682064791fa0ce35f6cea97335370e781380ba14093b0` |
| 09\-psf\-requests\-7620\-report | frozen\_report | frozen/09\-psf\-requests\-7620/report\.md | `152f3d0b3165495b42e834f68c8889c72b5b4e2402dfbb93dc88fed323dda591` |
| 09\-psf\-requests\-7620\-metadata | frozen\_metadata | frozen/09\-psf\-requests\-7620/metadata\.json | `833c1d5b2bde9980b40ab69da84c3c488a759d8ff3c70c96b887c41c5bf180a2` |
| 10\-psf\-requests\-7610\-report | frozen\_report | frozen/10\-psf\-requests\-7610/report\.md | `b0a1a759232f2a7a19b413fd7e91b43e2d5fdecb0f65af3583e4ea015cccb6cb` |
| 10\-psf\-requests\-7610\-metadata | frozen\_metadata | frozen/10\-psf\-requests\-7610/metadata\.json | `a7cb7324a90327bcd2c9cb75f8f43f0ed85b972d3bd86cd8cdb1adac90f44876` |
| study\-20260927\-adjudication\-original\-docx | research\_dataset | sources/study\-2026\-09\-27/adjudication\-original\.docx | `2fd1e4f1c18625a0f304f508914984059f1f6ab68f6816c7a7248512219b5134` |
| study\-20260927\-research\-original\-docx | research\_report | sources/study\-2026\-09\-27/research\-original\.docx | `43063543f868268d1c30b3b983a69712e36343a1a334863a7a68aa529e45e7a5` |
| study\-20260927\-adjudication\-recovered\-json | research\_dataset | sources/study\-2026\-09\-27/adjudication\-recovered\.json | `c6d7b269e73a785e20fe8a977b95026509d78f136992b8cb76730dbb93a3763a` |
| study\-20260927\-research\-recovered\-md | research\_report | sources/study\-2026\-09\-27/research\-recovered\.md | `16af924ca3ec2ea8d3764bb9e172a2e146392cd35ba1bf1143da1e3be63b93ad` |
| study\-20260927\-extraction\-audit\-json | evidence\_snapshot | sources/study\-2026\-09\-27/extraction\-audit\.json | `548b30e33903cdf9e93f04a2fd750f64b68bc7653644f7c12a62d0b0e6350987` |
