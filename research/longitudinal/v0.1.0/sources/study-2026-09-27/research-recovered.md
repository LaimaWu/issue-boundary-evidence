IBE v0.1.0 Longitudinal Research Report — Word Conversion

Source file: IBE_v0.1.0_longitudinal_research_report_2026-09-27.md
Converted from Markdown for transfer to Codex. No research conclusions were added or rewritten.

# IBE v0.1.0：第一次纵向证据判定

观察截止：2026-09-26T23:41:39Z；逐案冻结：2026-09-19 11:43:12–11:43:41 UTC。

## 结论摘要

- 十案中，冻结日期后有 3 案关闭、7 案仍开放。关闭的三案分别是：CI 后续成功但原因未明；Matplotlib 的 CI 镜像调整合并至主线；Pydantic maintainer 确认私有模块不可导入但决定不修。

- 已取得并核验原始冻结包：10 份未修改的 CLI 报告、逐案原始 issue/comments 与时间戳，98/98 项 SHA-256 校验通过。报告的线索现在可与后续证据逐案对照。

- 一案出现有意义的方向吻合： Matplotlib #32339 的报告抓到了 Homebrew 边界，随后主线合并了调整 macOS CI builder 的 PR。但 Homebrew 在冻结前的 issue 正文里已被点名，不能称为工具提前独立发现根因。

- 一案只确认现象、没有确认工具的归属推断： Pydantic #13835 后来由 maintainer 确认私有模块不可导入，却认为它无 v2 入口并决定不修。scikit-learn #34977 的 CI 恢复和关闭也没有确认报告里较强的 joblib/parallel 线索。其余七案尚无可作为最终裁决的 issue 结局。

- 冻结时即可识别的缺漏与噪声更具体： uv #21720 漏了当时 maintainer 对 .venv/requires-python 的解释，却把示例项目 demo 当作较强边界；Requests #7620 找到了历史 PR 和 commit，却漏了已明确的 master/main 分支原因；scikit-learn #34975 把贡献者 fork 标成较强的外部仓库边界。

- uv #21720 的两项合并，以及 uv 0.12.16 列出的局部修复，都发生在冻结之前；Requests 的分支归属和保留旧 license classifier 的理由也早已明确。它们只能用于判定冻结报告有没有用好当时已有的证据。

- 主线合并与发布要分开：Matplotlib #32372 在 9 月 23 日合并并关闭关联 issue，但 9 月 25–26 日仍在讨论 3.11 回移；Pydantic #13834 的一个 PR 获得贡献者审查通过，之后仍被 maintainer 关闭且没有合并。

## 口径与资料完整性

- 样本：原始 prospective-freeze-v0.1.0-2026-09-19.zip 的 MANIFEST.md 列出的五库十案；工具 tag v0.1.0、SHA 0a21ea25ce03bcc68ef32a6b477244089dcf5ecd。10 案在各自冻结时均开放，CLI 退出码均为 0。

- 压缩包 SHA-256：f398678f387c4b37e4d08285a0637d70f653aa2aa536e032d58b06beb20ec070。包内 SHA256SUMS.txt 的 98 项全部与原文件相符。原报告逐字节保留；本研究只写新 JSON 与研究报告。

- 只读取公开 GitHub issue、comments、timeline、关联 PR 与 release；无 issue/仓库写入，无产品代码修改。关联 PR 的 merged_at 比关闭状态更能说明是否真的合并。

- 每案以 metadata.json 的 snapshot_completed_utc 为界，包括 9 月 19 日稍晚出现的事件。Matplotlib 的关联 PR 在当天 16:49 UTC 以后出现新构建阻碍；它不在 11:43 UTC 的冻结输出里。一个 CI bot 评论在冻结前说过“CI 已恢复”，后来又改成指向 9 月 23 日的新绿灯；以两份原始 JSON 的内容差异和编辑时间识别，不能将现今版本倒灌进冻结报告。

- 观察事实 = 可从当前公开记录直接核对的事件、状态或原话；贡献者自称复现仍只表示其曾作此报告。maintainer 明确确认 = 仓库成员作出的结论，bot 不算。研究者推断 = 对责任、影响或严重程度的有条件判断。GitHub 历史评论可能被编辑或删除；Pydantic #13834 有删除事件，删除内容不可还原。

- severity 是当前证据能支撑的影响范围，不是项目官方优先级。冻结工具本身不输出 severity、最终原因、归属或修复决定；“未声称”不能算成错误。未按十案硬算准确率，也不将“开放未回复”当作反证。

## 十案当前状态

| 案件 | 当前 | 纵向结果 |
| --- | --- | --- |
| [scikit-learn/scikit-learn#34977](https://github.com/scikit-learn/scikit-learn/issues/34977) | 关闭 | CI 恢复后关闭；致因未知 |
| [scikit-learn/scikit-learn#34975](https://github.com/scikit-learn/scikit-learn/issues/34975) | 开放 | 精度 PR 仍未合并 |
| [astral-sh/uv#21829](https://github.com/astral-sh/uv/issues/21829) | 开放 | 缓存粒度需求未决 |
| [astral-sh/uv#21720](https://github.com/astral-sh/uv/issues/21720) | 开放 | 默认差异仍开放；局部修复在冻结前发布 |
| [matplotlib/matplotlib#32339](https://github.com/matplotlib/matplotlib/issues/32339) | 关闭 | 主线 CI 调整合并；回移未决 |
| [matplotlib/matplotlib#32329](https://github.com/matplotlib/matplotlib/issues/32329) | 开放 | 重叠路径语义未决 |
| [pydantic/pydantic#13835](https://github.com/pydantic/pydantic/issues/13835) | 关闭 | 明确承认不可导入，但选择不修 |
| [pydantic/pydantic#13834](https://github.com/pydantic/pydantic/issues/13834) | 开放 | 两个 PR 均关闭未合并 |
| [psf/requests#7620](https://github.com/psf/requests/issues/7620) | 开放 | 错误目标分支已在冻结前确认 |
| [psf/requests#7610](https://github.com/psf/requests/issues/7610) | 开放 | 兼容性理由导致暂缓 |

## 逐案证据时间线与五维判定

### [scikit-learn/scikit-learn#34977](https://github.com/scikit-learn/scikit-learn/issues/34977) — Wheel builder CI failure

冻结时刻： 2026-09-19T11:43:12Z–2026-09-19T11:43:15Z；原报告：cases/01-scikit-learn-scikit-learn-34977/report.md（SHA-256 b6aa3961affa123b9db077ddfe6b55b3d7b315183df5d5094272d2e8b83ebf9d）。

冻结报告实际输出〔观察事实〕： 报告将 cp314t 轮包、joblib 和 parallel 列作较强线索，也记录了冻结前就已有的 CI 成功运行。

对照判定〔研究者推断〕： 轮包平台与失败日志的引文准确。joblib 只是堆栈中的模块，parallel 也可能只是 API 名；后来 CI 再次成功并关单，并未证实这些是原因。

纵向结论： 新绿灯与关闭均不能裁定报告的包边界。

冻结前背景： 冻结前 issue 仍开放，但 bot 已指向 9 月 19 日的一次成功运行；maintainer 留下 Windows arm64 失败日志。

原始评论对照： 冻结时 2 条；现存新增 ID []，正文变更 ID [5722880061]。

冻结日期后的证据：

- 2026-09-23T04:34:55Z · 观察事实 · A bot comment created September 18 was edited to report a successful September 23 CI run; its creation date is not the success time. [原始记录](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5722880061)

- 2026-09-23T20:56:04Z · 观察事实 · A repository member closed the issue. [原始记录](https://github.com/scikit-learn/scikit-learn/issues/34977)

| 维度 | 判定与证据性质 |
| --- | --- |
| 现象 | 观察事实：CI wheel build failed on cp314t Windows arm64; later run succeeded. [证据 1](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5723076602), [证据 2](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5722880061) |
| 原因 | 研究者推断：Exact underlying cause and reason for recovery are unconfirmed; exception alone does not establish a code defect. [证据 1](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5723076602) |
| 归属 | 研究者推断：Repository CI incident; ownership of the underlying fault is undetermined. [证据 1](https://github.com/scikit-learn/scikit-learn/issues/34977) |
| 严重程度 | 研究者推断：Build pipeline interruption, scope limited to observed wheel job; wider release impact unproven. [证据 1](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5723076602) |
| 修复轨迹 | 观察事实：A successful run preceded closure; no linked repair PR or release was established. [证据 1](https://github.com/scikit-learn/scikit-learn/issues/34977#issuecomment-5722880061), [证据 2](https://github.com/scikit-learn/scikit-learn/issues/34977) |

未决： Failure mechanism；Whether a particular code or infrastructure change caused recovery。

### [scikit-learn/scikit-learn#34975](https://github.com/scikit-learn/scikit-learn/issues/34975) — float32 scores and ranking count precision

冻结时刻： 2026-09-19T11:43:15Z–2026-09-19T11:43:17Z；原报告：cases/02-scikit-learn-scikit-learn-34975/report.md（SHA-256 27ff56a24e509e25a3e589f48d9ac6b903ca22ba1326c77cb62c5b6f7f6f10be）。

冻结报告实际输出〔观察事实〕： 报告抓到 float32 回归表述，却把贡献者 fork 提升为外部仓库边界。

对照判定〔研究者推断〕： 回归提法及 ranking 模块位置可追溯。ammar-iitm/scikit-learn 是提交修复的 fork，并非上游故障方；NumPy 是输入后端，拟修复的转换发生在 scikit-learn。

纵向结论： PR 仍未合并，无冻结后的维护者根因结论。

冻结前背景： 冻结前 maintainer 已请作者开 PR，#34980 已开放；回归原因主要由报告者提出。

冻结日期后： 截至 2026-09-26T23:41:39Z，所查 issue 时间线无新的实质评论、关闭/重开或关联修复；这只表示公开记录未出现判定所需的新信息。

| 维度 | 判定与证据性质 |
| --- | --- |
| 现象 | 观察事实：Reporter reproduces integer count rounding above 2**24 when float32 scores are used on NumPy. [证据 1](https://github.com/scikit-learn/scikit-learn/issues/34975) |
| 原因 | 研究者推断：Casting exact int64 counts to y_score float32 is the reporter and PR author’s proposed mechanism; no later maintainer conclusion. [证据 1](https://github.com/scikit-learn/scikit-learn/issues/34975), [证据 2](https://github.com/scikit-learn/scikit-learn/pull/34980) |
| 归属 | maintainer 明确确认：Proposed fix targets scikit-learn ranking metrics; maintainer invited PR before freeze. [证据 1](https://github.com/scikit-learn/scikit-learn/issues/34975#issuecomment-5715288844), [证据 2](https://github.com/scikit-learn/scikit-learn/pull/34980) |
| 严重程度 | 研究者推断：Potential silent numerical imprecision on large inputs; frequency and production impact unmeasured. [证据 1](https://github.com/scikit-learn/scikit-learn/issues/34975) |
| 修复轨迹 | 观察事实：#34980 remains open and unmerged as of cutoff; no release or backport evidenced. [证据 1](https://github.com/scikit-learn/scikit-learn/pull/34980) |

关联 PR： [34980](https://github.com/scikit-learn/scikit-learn/pull/34980)（未合并）。

未决： Maintainer validation of regression cause；PR review, merge and release。

### [astral-sh/uv#21829](https://github.com/astral-sh/uv/issues/21829) — Granular cache management

冻结时刻： 2026-09-19T11:43:17Z–2026-09-19T11:43:20Z；原报告：cases/03-astral-sh-uv-21829/report.md（SHA-256 4f3423d816b53256fc521ff7fcb1c836ae06249b38f91e48ec35029fce002c4b）。

冻结报告实际输出〔观察事实〕： 报告未提炼出缓存管理的功能缺口；把普通依赖升级当成较强回归线索，并抽取示例 torch 版本。

对照判定〔研究者推断〕： 示例引文真实，但 torch==2.14.0+cu132 是举例而非 uv 版本；冻结前 maintainer 已纠正“只有 symlink 能省空间”并提到 uv cache prune，报告没有提炼。

纵向结论： 冻结后无实质维护者结论。

冻结前背景： 冻结前 maintainer 已纠正缓存机制的部分前提，报告者继续要求按发行包精确管理。

冻结日期后的证据：

- 2026-09-21T12:19:20Z · 观察事实 · A user subscribed; no substantive comment or resolution followed. [原始记录](https://github.com/astral-sh/uv/issues/21829)

| 维度 | 判定与证据性质 |
| --- | --- |
| 现象 | 观察事实：Feature request for listing and pruning particular cached distributions; no verified failure in existing cache prune. [证据 1](https://github.com/astral-sh/uv/issues/21829) |
| 原因 | maintainer 明确确认：Request concerns missing granularity; initial premise that only symlinks avoid duplication was corrected by maintainer before freeze. [证据 1](https://github.com/astral-sh/uv/issues/21829#issuecomment-5734801101), [证据 2](https://github.com/astral-sh/uv/issues/21829#issuecomment-5735325203) |
| 归属 | 研究者推断：Requested interface belongs to uv; local Windows filesystem and package sizes affect the motivating example. [证据 1](https://github.com/astral-sh/uv/issues/21829) |
| 严重程度 | 研究者推断：Potential high disk/network cost for specific large packages, quantified impact absent. [证据 1](https://github.com/astral-sh/uv/issues/21829#issuecomment-5735325203) |
| 修复轨迹 | 观察事实：Issue remains open with no linked merged PR or release conclusion after freeze. [证据 1](https://github.com/astral-sh/uv/issues/21829) |

未决： Whether maintainers accept the requested granularity；Implementation scope。

### [astral-sh/uv#21720](https://github.com/astral-sh/uv/issues/21720) — uv check and ty check Python-version divergence

冻结时刻： 2026-09-19T11:43:20Z–2026-09-19T11:43:22Z；原报告：cases/04-astral-sh-uv-21720/report.md（SHA-256 b1c7e815fbf05d19b634eedc3cca80cc650796f7d3f7202a27a5a889f3f65a31）。

冻结报告实际输出〔观察事实〕： 报告列出 Python、uv、ty 版本，唯一较强边界却是最小示例项目名 demo。

对照判定〔研究者推断〕： 环境版本提取准确，但漏了冻结前 maintainer 对 .venv 与 requires-python 的解释、两项已合并 PR 及 uv 0.12.16；demo 并非依赖。

纵向结论： issue 仍开放，现有局部发布发生在冻结前。

冻结前背景： 冻结前 maintainer 已解释行为差异，两项局部改动已合并，uv 0.12.16 已发布。

冻结日期后： 截至 2026-09-26T23:41:39Z，所查 issue 时间线无新的实质评论、关闭/重开或关联修复；这只表示公开记录未出现判定所需的新信息。

| 维度 | 判定与证据性质 |
| --- | --- |
| 现象 | 观察事实：The two commands can report different diagnostics from different effective Python version choices. [证据 1](https://github.com/astral-sh/uv/issues/21720) |
| 原因 | maintainer 明确确认：Maintainer explains uv prefers current environment while ty reads project support floor; explicit --python forwarding was separately changed. [证据 1](https://github.com/astral-sh/uv/issues/21720#issuecomment-5695949350), [证据 2](https://github.com/astral-sh/uv/pull/21744), [证据 3](https://github.com/astral-sh/ruff/pull/28646) |
| 归属 | 研究者推断：Cross-component uv/ty behavioral contract, rather than evidence that one checker is categorically broken. [证据 1](https://github.com/astral-sh/uv/issues/21720#issuecomment-5695949350), [证据 2](https://github.com/astral-sh/uv/pull/21744), [证据 3](https://github.com/astral-sh/ruff/pull/28646) |
| 严重程度 | 研究者推断：Surprising check discrepancy, with documented workaround; no measured prevalence. [证据 1](https://github.com/astral-sh/uv/issues/21720) |
| 修复轨迹 | 观察事实：Narrow changes merged and uv #21744 was listed in 0.12.16 before freeze; default discrepancy remains an open issue. [证据 1](https://github.com/astral-sh/uv/issues/21720), [证据 2](https://github.com/astral-sh/uv/pull/21744), [证据 3](https://github.com/astral-sh/ruff/pull/28646), [证据 4](https://github.com/astral-sh/uv/releases/tag/0.12.16) |

关联 PR： [21744](https://github.com/astral-sh/uv/pull/21744)（已合并）；[28646](https://github.com/astral-sh/ruff/pull/28646)（已合并）。

发布/回移： [0.12.16](https://github.com/astral-sh/uv/releases/tag/0.12.16)：Lists uv #21744; before freeze。

未决： Whether default behaviors should converge；Any later version-specific regression conclusion。

### [matplotlib/matplotlib#32339](https://github.com/matplotlib/matplotlib/issues/32339) — macOS 14 CI dependency installation

冻结时刻： 2026-09-19T11:43:22Z–2026-09-19T11:43:25Z；原报告：cases/05-matplotlib-matplotlib-32339/report.md（SHA-256 46e9615bee88cfffe76d902ba0d4ba00f2c8890b5d2fee5a2cfa2fbf0ac0f8b6）。

冻结报告实际输出〔观察事实〕： 报告将 Homebrew/homebrew-core 列为较强外部边界并链接公式变更。

对照判定〔研究者推断〕： 与后来合并的 CI builder 调整方向吻合；但 Homebrew 本已在正文出现。背景兼容表中的五个 Python 版本增添噪声，后来 LLVM 问题与回移仍未决。

纵向结论： 边界方向得到后续行动支持，但谈不上独立预测根因。

冻结前背景： 冻结前 Homebrew 缺瓶包和调整 CI 镜像的方案已公开，#32372 尚未合并。

冻结日期后的证据：

- 2026-09-19T16:49:52Z · 观察事实 · A contributor narrowed a new macOS 26 interactive-framework crash to framework load order while the CI-image PR was being tested. [原始记录](https://github.com/matplotlib/matplotlib/pull/32372#issuecomment-5743638528)

- 2026-09-19T17:01:41Z · 观察事实 · PR #32376 opened to load AppKit before CoreText, a blocker encountered while testing the builder-image change. [原始记录](https://github.com/matplotlib/matplotlib/pull/32376)

- 2026-09-19T18:48:59Z · 观察事实 · Contributor review approved #32372 conditional on #32376 landing. [原始记录](https://github.com/matplotlib/matplotlib/pull/32372)

- 2026-09-19T19:03:14Z · 观察事实 · Contributor clarified macOS 10.14 and macOS 14 are different releases, limiting an overly broad reading of usage statistics. [原始记录](https://github.com/matplotlib/matplotlib/pull/32372#issuecomment-5744556853)

- 2026-09-23T00:54:33Z · 观察事实 · The separate macOS framework-load PR #32376 merged before the CI-image PR. [原始记录](https://github.com/matplotlib/matplotlib/pull/32376)

- 2026-09-23T15:19:01Z · 观察事实 · PR #32372 changed macOS CI builder images and explicitly marked the issue fixed; merged to main. [原始记录](https://github.com/matplotlib/matplotlib/pull/32372)

- 2026-09-23T15:19:02Z · 观察事实 · Issue closed one second after PR merge. [原始记录](https://github.com/matplotlib/matplotlib/issues/32339)

- 2026-09-25T20:21:25Z · maintainer 明确确认 · Maintainer said they were debating a 3.11 backport as CI was failing again, with a possible new LLVM problem. [原始记录](https://github.com/matplotlib/matplotlib/pull/32372#issuecomment-5839025923)

- 2026-09-25T22:36:03Z · 观察事实 · Contributor supported backporting the CI change without treating it as a user-platform support drop. [原始记录](https://github.com/matplotlib/matplotlib/pull/32372#issuecomment-5840606172)

- 2026-09-26T02:23:26Z · 观察事实 · Contributor described Homebrew on macOS 14 and earlier as unreliable under its Tier 3 policy. [原始记录](https://github.com/matplotlib/matplotlib/pull/32372#issuecomment-5842344428)

| 维度 | 判定与证据性质 |
| --- | --- |
| 现象 | 观察事实：macOS 14 CI package installation became unreliable; later CI failures persisted in a possible separate LLVM path. [证据 1](https://github.com/matplotlib/matplotlib/issues/32339), [证据 2](https://github.com/matplotlib/matplotlib/pull/32372#issuecomment-5839025923) |
| 原因 | maintainer 明确确认：Homebrew support and bottle availability are the maintained explanation of the original failure; later LLVM failure not established as same cause. [证据 1](https://github.com/matplotlib/matplotlib/issues/32339), [证据 2](https://github.com/matplotlib/matplotlib/pull/32372#issuecomment-5839025923), [证据 3](https://github.com/matplotlib/matplotlib/pull/32372#issuecomment-5842344428) |
| 归属 | 研究者推断：CI image choice is Matplotlib’s; upstream Homebrew package support is outside its repository. [证据 1](https://github.com/matplotlib/matplotlib/issues/32339), [证据 2](https://github.com/matplotlib/matplotlib/pull/32372) |
| 严重程度 | 研究者推断：Active CI breakage; no evidence that installed Matplotlib stopped supporting macOS 14. [证据 1](https://github.com/matplotlib/matplotlib/issues/32339), [证据 2](https://github.com/matplotlib/matplotlib/pull/32372#issuecomment-5840606172) |
| 修复轨迹 | 观察事实：Main-branch CI builder update merged and issue closed; backport was being debated, no 3.11 release/backport verified. [证据 1](https://github.com/matplotlib/matplotlib/pull/32372), [证据 2](https://github.com/matplotlib/matplotlib/issues/32339), [证据 3](https://github.com/matplotlib/matplotlib/pull/32372#issuecomment-5839025923) |

关联 PR： [32372](https://github.com/matplotlib/matplotlib/pull/32372)（已合并）；[32376](https://github.com/matplotlib/matplotlib/pull/32376)（已合并）。

发布/回移： [发布记录](https://github.com/matplotlib/matplotlib/releases)：Latest checked Matplotlib GitHub release v3.11.2 was September 11; backport discussion September 25–26.。

未决： Whether the CI change was backported to v3.11.x；Cause of renewed LLVM failures。

### [matplotlib/matplotlib#32329](https://github.com/matplotlib/matplotlib/issues/32329) — contains() and fill-rule inconsistency

冻结时刻： 2026-09-19T11:43:25Z–2026-09-19T11:43:28Z；原报告：cases/06-matplotlib-matplotlib-32329/report.md（SHA-256 426e5fe4f1a325a8f83217642f8cc0a63eb9dc9c98e3e4a86902820f03a22f00）。

冻结报告实际输出〔观察事实〕： 报告明确表示“未发现主要边界证据”，仍保留内部代码与关联 PR 的链接。

对照判定〔研究者推断〕： 针对内部几何语义问题，暂不猜外部依赖是合理的；后来尚无最终语义或修复结论。

纵向结论： 维持未决，弃判没有遭后续反证。

冻结前背景： 冻结前作者已描述 contains 与填充规则的不一致，倾向今后再处理。

冻结日期后： 截至 2026-09-26T23:41:39Z，所查 issue 时间线无新的实质评论、关闭/重开或关联修复；这只表示公开记录未出现判定所需的新信息。

| 维度 | 判定与证据性质 |
| --- | --- |
| 现象 | 观察事实：Reporter’s examples show path contains() can disagree with both fill rules for overlapping subpaths. [证据 1](https://github.com/matplotlib/matplotlib/issues/32329) |
| 原因 | 研究者推断：Reporter attributes behavior to point_in_path_impl handling each subpath and combining membership; no later maintainer conclusion. [证据 1](https://github.com/matplotlib/matplotlib/issues/32329) |
| 归属 | 研究者推断：Candidate fix would connect Matplotlib fill-rule choice to path containment internals. [证据 1](https://github.com/matplotlib/matplotlib/issues/32329) |
| 严重程度 | 研究者推断：Hit testing mismatch for special overlapping paths; user impact unmeasured. [证据 1](https://github.com/matplotlib/matplotlib/issues/32329) |
| 修复轨迹 | 观察事实：Open; no new linked fix PR, release, or backport after freeze. [证据 1](https://github.com/matplotlib/matplotlib/issues/32329) |

未决： Chosen semantic rule；Fix plan and version。

### [pydantic/pydantic#13835](https://github.com/pydantic/pydantic/issues/13835) — v1 Hypothesis plugin import under v2

冻结时刻： 2026-09-19T11:43:28Z–2026-09-19T11:43:30Z；原报告：cases/07-pydantic-pydantic-13835/report.md（SHA-256 00d8100444c6a2889303acd034a2468ba9c8c770bac670ad82f18907bb2b2bbf）。

冻结报告实际输出〔观察事实〕： 报告提取 v2/Python 版本和贡献者“修复与回归测试已准备好”的说法，没有识别模块的私有性与入口边界。

对照判定〔研究者推断〕： 标题所述不可导入后来由 maintainer 证实；但“已有 PR”并不等于维护者接受修复，也不证明版本回归。维护者认定该私有模块在 v2 没有注册入口，最终选择不修。

纵向结论： 现象获得确认，修复必要性与归属没有被报告预见。

冻结前背景： 冻结前已有直接导入的复现和因未获分配而关闭的 #13836。

原始评论对照： 冻结时 3 条；现存新增 ID [5754533343, 5825685645]，正文变更 ID []。

冻结日期后的证据：

- 2026-09-21T02:14:46Z · 观察事实 · Contributor asked for assignment to reopen #13836 after adjusting tests. [原始记录](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5754533343)

- 2026-09-25T02:28:13Z · maintainer 明确确认 · Repository member confirmed module cannot be imported, said no v2 entry point registers it and it is private, and preferred leaving it unchanged; closed issue. [原始记录](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5825685645)

| 维度 | 判定与证据性质 |
| --- | --- |
| 现象 | maintainer 明确确认：Private v1 Hypothesis module is not importable under v2; maintainer agrees. [证据 1](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5825685645) |
| 原因 | maintainer 明确确认：No v2 entry point registers the private module; the import failure itself remains, while precise import statements were established by reporter/contributor. [证据 1](https://github.com/pydantic/pydantic/issues/13835), [证据 2](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5825685645) |
| 归属 | maintainer 明确确认：Maintainer judges it outside a supported v2 public integration and prefers no change. [证据 1](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5825685645) |
| 严重程度 | 研究者推断：Direct private-module import is broken, but no supported v2 entry point invokes it; low demonstrated product impact. [证据 1](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5825685645) |
| 修复轨迹 | maintainer 明确确认：Issue closed without fix; #13836 never merged; maintainer explicitly declined change. [证据 1](https://github.com/pydantic/pydantic/issues/13835#issuecomment-5825685645), [证据 2](https://github.com/pydantic/pydantic/pull/13836) |

关联 PR： [13836](https://github.com/pydantic/pydantic/pull/13836)（未合并）。

未决： Whether private module will eventually be removed。

### [pydantic/pydantic#13834](https://github.com/pydantic/pydantic/issues/13834) — create_model __validators__ static annotation

冻结时刻： 2026-09-19T11:43:30Z–2026-09-19T11:43:34Z；原报告：cases/08-pydantic-pydantic-13834/report.md（SHA-256 a3febe6be5fd4e5878863a2e1ddfe0093cce1697b51a7b32e7564c741a812563）。

冻结报告实际输出〔观察事实〕： 报告记录环境版本、早期 #9690/#9697 和贡献者提案，未将静态注解与运行时行为不一致提炼成核心线索。

对照判定〔研究者推断〕： 历史关联准确；“回归测试”却被当作回归表述，明确提到的 #13837 也没有被拉入同库引用。后续两个提案 PR 均未合并。

纵向结论： 审查意见与 PR 关闭不足以说明修复落地。

冻结前背景： 冻结前已有静态注解问题复现和 #13837 提案。

冻结日期后的证据：

- 2026-09-20T14:07:36Z · 观察事实 · A contributor reviewer approved #13837 after a static typing regression case was added. [原始记录](https://github.com/pydantic/pydantic/pull/13837#pullrequestreview-5260777891)

- 2026-09-20T15:15:35Z · 观察事实 · Repository member closed #13837 without merge; the available PR comments do not establish why. [原始记录](https://github.com/pydantic/pydantic/pull/13837)

- 2026-09-23T02:29:31Z · 观察事实 · Four issue comment-deletion events were logged; deleted content is unavailable and not interpreted. [原始记录](https://github.com/pydantic/pydantic/issues/13834)

- 2026-09-23T05:16:04Z · 观察事实 · #13851 proposed a similar annotation widening. [原始记录](https://github.com/pydantic/pydantic/pull/13851)

- 2026-09-23T05:16:16Z · 观察事实 · Bot closed #13851 because the author was not assigned to the issue. [原始记录](https://github.com/pydantic/pydantic/pull/13851#issuecomment-5789492583)

| 维度 | 判定与证据性质 |
| --- | --- |
| 现象 | 观察事实：Reporter and contributors observe runtime acceptance with three static checkers rejecting the declared type. [证据 1](https://github.com/pydantic/pydantic/issues/13834), [证据 2](https://github.com/pydantic/pydantic/pull/13837) |
| 原因 | 观察事实：Reviewer identified a static typing regression, since runtime tests already passed before annotation change. [证据 1](https://github.com/pydantic/pydantic/pull/13837) |
| 归属 | 研究者推断：Candidate annotation change is in Pydantic; maintainer has not stated final intended API type. [证据 1](https://github.com/pydantic/pydantic/issues/13834), [证据 2](https://github.com/pydantic/pydantic/pull/13837), [证据 3](https://github.com/pydantic/pydantic/pull/13851) |
| 严重程度 | 研究者推断：Type-checking friction with working runtime behavior; no measured usage impact. [证据 1](https://github.com/pydantic/pydantic/issues/13834) |
| 修复轨迹 | 观察事实：Both related PRs are closed unmerged; issue open; no release/backport. Approval of #13837 did not imply merge. [证据 1](https://github.com/pydantic/pydantic/pull/13837), [证据 2](https://github.com/pydantic/pydantic/pull/13851), [证据 3](https://github.com/pydantic/pydantic/issues/13834) |

关联 PR： [13837](https://github.com/pydantic/pydantic/pull/13837)（未合并）；[13851](https://github.com/pydantic/pydantic/pull/13851)（未合并）。

未决： Reason maintainer closed approved #13837；Final accepted annotation and tests；Deleted-comment contents。

### [psf/requests#7620](https://github.com/psf/requests/issues/7620) — Old PR merged to master but absent from main

冻结时刻： 2026-09-19T11:43:34Z–2026-09-19T11:43:37Z；原报告：cases/09-psf-requests-7620/report.md（SHA-256 152f3d0b3165495b42e834f68c8889c72b5b4e2402dfbb93dc88fed323dda591）。

冻结报告实际输出〔观察事实〕： 报告抓到历史合并 SHA 和 PR #5410，却没有提炼 maintainer 已确认的 master/main 分支错位。

对照判定〔研究者推断〕： 历史链接有用；“下次发布可考虑”被当作版本/回归线索，但没有随后发布承诺。

纵向结论： 冻结后仍无实质推进。

冻结前背景： 冻结前 maintainer 已指出旧 PR 目标是 master，不是 main。

冻结日期后： 截至 2026-09-26T23:41:39Z，所查 issue 时间线无新的实质评论、关闭/重开或关联修复；这只表示公开记录未出现判定所需的新信息。

| 维度 | 判定与证据性质 |
| --- | --- |
| 现象 | 观察事实：GitHub records historical #5410 as merged, but that old master merge is absent from current main per issue report. [证据 1](https://github.com/psf/requests/issues/7620), [证据 2](https://github.com/psf/requests/pull/5410) |
| 原因 | maintainer 明确确认：Maintainer identified wrong base branch at master/main cutover. [证据 1](https://github.com/psf/requests/issues/7620#issuecomment-5626752874), [证据 2](https://github.com/psf/requests/issues/7620#issuecomment-5701707334), [证据 3](https://github.com/psf/requests/pull/5410) |
| 归属 | 研究者推断：Historical repository branch management; not evidence of a current downstream package fault. [证据 1](https://github.com/psf/requests/issues/7620), [证据 2](https://github.com/psf/requests/pull/5410) |
| 严重程度 | 研究者推断：Old uncarried minor shebang change; maintainer found no other identified instances, broader loss unproven. [证据 1](https://github.com/psf/requests/issues/7620#issuecomment-5701707334) |
| 修复轨迹 | 观察事实：No new PR on main, release or backport after freeze; issue remains open. [证据 1](https://github.com/psf/requests/issues/7620) |

关联 PR： [5410](https://github.com/psf/requests/pull/5410)（已合并）。

未决： Whether change will be reapplied；Whether any other historical PR was stranded。

### [psf/requests#7610](https://github.com/psf/requests/issues/7610) — License classifier and SPDX metadata

冻结时刻： 2026-09-19T11:43:37Z–2026-09-19T11:43:41Z；原报告：cases/10-psf-requests-7610/report.md（SHA-256 b0a1a759232f2a7a19b413fd7e91b43e2d5fdecb0f65af3583e4ea015cccb6cb）。

冻结报告实际输出〔观察事实〕： 报告从 maintainer 评论中抓到旧 setuptools 兼容性，是正文之外的有价值线索。

对照判定〔研究者推断〕： 兼容性引文准确；未充分呈现这是维护者有意取舍，同时把泛指旧版本的评论放入回归语言。

纵向结论： 有助于冻结时理解问题，没有新增的 prospective 验证。

冻结前背景： 冻结前 maintainer 已说明保留旧 classifier 的兼容性理由，并暂缓删除。

冻结日期后： 截至 2026-09-26T23:41:39Z，所查 issue 时间线无新的实质评论、关闭/重开或关联修复；这只表示公开记录未出现判定所需的新信息。

| 维度 | 判定与证据性质 |
| --- | --- |
| 现象 | 观察事实：Metadata carries both an SPDX license and legacy classifier; downstream SBOM tooling emits redundant free-text license. [证据 1](https://github.com/psf/requests/issues/7610) |
| 原因 | maintainer 明确确认：Maintainer intentionally retains classifier for older setuptools users; reporter points to deprecation and downstream interpretation. [证据 1](https://github.com/psf/requests/issues/7610#issuecomment-5427534997), [证据 2](https://github.com/psf/requests/issues/7610) |
| 归属 | 研究者推断：Compatibility choice in Requests packaging and SBOM interpretation downstream both contribute; maintainer explicitly declined immediate removal. [证据 1](https://github.com/psf/requests/issues/7610#issuecomment-5427534997) |
| 严重程度 | 研究者推断：Downstream metadata noise with no blocking pipeline according to reporter; removal risks older build workflows per maintainer. [证据 1](https://github.com/psf/requests/issues/7610#issuecomment-5460764689), [证据 2](https://github.com/psf/requests/issues/7610#issuecomment-5427534997) |
| 修复轨迹 | maintainer 明确确认：Deferred by maintainer before freeze; still open with no merged change or release. [证据 1](https://github.com/psf/requests/issues/7610#issuecomment-5427534997), [证据 2](https://github.com/psf/requests/issues/7610) |

未决： Criteria and date for future classifier removal。

## 对 v0.1.0 research hypotheses 的证据上限

| 假设 | 目前支持/反驳到哪里 |
| --- | --- |
| 确定性提取能在维护者尚未完成判断前提出有用边界 | 有限支持。 Matplotlib #32339 指出 Homebrew，与后来主线 PR 的方向一致；Requests #7610 从正文之外的 maintainer 评论抓到旧 setuptools 兼容性。但前者本来已在 issue 正文，后者在冻结前已经有解释，尚不能证明“提前发现”或比只读正文的基线持续更好。 |
| 版本、回归与外部仓库线索会保持足够低的噪声 | 受到具体反例挑战。 uv #21829 的依赖升级描述并非软件回归；uv #21720 的 demo 是示例名；scikit-learn #34975 的 fork 是贡献者修复分支；Matplotlib #32339 的背景 Python 版本表占据篇幅。这些噪声已在原始冻结输出中出现。 |
| 报告覆盖关键现成线索，保留可追溯性 | 溯源可核，但完整性不足。 uv #21720 和 Requests #7620 已有 maintainer 解释却未被提炼成关键边界；Pydantic #13834 的历史 PR 有价值，但注解/静态检查器不一致仍未成为主线索。 |
| 边界线索能够推出真正根因、归属和修复 | 强版本不能成立，但超出 v0.1.0 声称的能力。 Pydantic #13835 的技术失败被确认，maintainer 仍不认为应修；scikit-learn CI 后续绿灯也未说明根因。不能把贡献者“fix ready”当维护者认可或发布。 |
| 这批样本能证明外部 maintainer 使用或采纳 IBE | 不支持。 上游讨论与修复是独立发生的公开事件，没有上游使用 IBE 的证据。 |
| 十份冻结报告能对后续结论作 prospective 验证 | 已有第一轮窄证据。 三案在冻结后关闭：一案 Homebrew 边界方向吻合，一案私有模块的现象确认但修复必要性被否定，一案 CI 恢复而根因未决；其余七案不足以裁定最终方向。十案不能据此给出稳定准确率。 |

最需要保留的开放问题是：Matplotlib #32339 是否回移且后续 LLVM 失败是否同因；Pydantic #13834 已获贡献者审查通过的 PR 为何仍被 maintainer 关闭；scikit-learn #34975 的精度 PR 是否获维护者确认并进入发布；scikit-learn #34977 的恢复究竟由什么变化引起。

本报告的逐事件 URL、状态字段、五维判定与未决项均在配套 JSON 数据集内，可直接复核和继续追踪。
