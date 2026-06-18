# Discord OpenClaw 机制融入方案

- 状态：draft
- 更新时间：2026-06-18
- 适用范围：EvoZeus Discord 社区频道、社区贡献分流、Candidate 孵化、证据补齐

## 核心判断

Discord 不应该替代 GitHub 治理，而应该成为 GitHub PR 之前的社区缓冲层。

OpenClaw 值得吸收的不是完整 bot、label、automerge 和 release train，而是四件事：

1. 分层治理：讨论、证据、Candidate、PR、promotion 分开。
2. 证据优先：不要用观点、热情或投票替代 real behavior proof。
3. 小单元贡献：一个 thread 只处理一个 Case、Candidate、Pattern、Factor 或问题。
4. 维护者门禁：Discord 可以推荐进入 PR，但不能批准、合并或 promotion。

## 推荐定位

把 Discord 定位成三个层级：

| 层级 | Discord 承担 | 不承担 |
| --- | --- | --- |
| 社区入口 | 问题、使用反馈、Case 线索、贡献意愿 | 长期决策、正式发布 |
| Candidate 孵化 | 补 evidence、做 redaction、判断路线 | 直接进入 core 或 reviewed |
| PR 前分流 | 判断是否需要 Issue、Candidate PR、docs PR、RFC | merge approval、CODEOWNERS、release gate |

## MVP：先用一个频道跑

如果现在只有一个 Discord 频道，先不要拆很多区。建议用 thread 前缀和置顶模板管理：

| Thread 前缀 | 用途 |
| --- | --- |
| `[case]` | 真实 session / 使用场景 / 失败案例 |
| `[candidate]` | 可复用规则、Pattern、Factor、Environment Rule |
| `[proof]` | 证据补齐、复现步骤、before/after 行为 |
| `[redaction]` | 隐私脱敏确认 |
| `[question]` | 非贡献型问题 |
| `[rfc]` | 可能影响治理、ontology、workflow、skill 的讨论 |

每个 thread 只保留一个主要对象。混合多个对象时，维护者要求拆 thread。

## 成熟后可拆分的频道

| 频道 | 作用 | 规则 |
| --- | --- | --- |
| `start-here` | 入口说明、链接、贡献路线 | 只放置顶和维护者公告 |
| `cases` | 用户提交真实 Case | 必须先 redaction |
| `candidate-lab` | 社区 Candidate 孵化 | 使用 Candidate 模板 |
| `proof-review` | 复现、证据等级、before/after | 不讨论产品方向 |
| `redaction-help` | 隐私、客户信息、路径、日志脱敏 | 默认 private-first |
| `maintainer-triage` | 维护者分流、准备转 GitHub | 可先设为 private |
| `release-log` | reviewed/core/deprecated 变更摘要 | 只读或维护者发言 |

## 贡献路线映射

| Discord 输入 | 下一步 |
| --- | --- |
| 使用问题、安装问题 | 留在 Discord 或转 docs issue |
| Bug 且有复现 | 转 GitHub issue 或 code PR |
| 真实 session 发现的判断规则 | 转 Candidate thread |
| Candidate 已有 Level 2+ evidence | 转 Candidate PR |
| 影响 `SKILL.md`、`skills/`、ontology、schema、workflow | 先走 `[rfc]`，不要直接 PR |
| 包含客户信息、内部路径、原始日志、secret | 先走 `[redaction]`，未脱敏前不进 PR |

## Discord 置顶说明草案

```markdown
# EvoZeus 贡献入口

这里是 PR 之前的讨论和 Candidate 孵化区。

请按 thread 前缀发起讨论：

- `[case]` 真实使用场景、失败案例、session 观察
- `[candidate]` 可复用规则、Pattern、Factor 或环境判断
- `[proof]` 复现步骤、before/after、证据补齐
- `[redaction]` 隐私脱敏确认
- `[question]` 普通问题
- `[rfc]` 影响治理、ontology、workflow、skill 的提案

基本规则：

1. 一个 thread 只讨论一个对象。
2. 行为改变必须提供 evidence，不只给观点。
3. 不贴 raw private logs、secret、客户资料、内部 URL 或未脱敏路径。
4. Discord 只能帮助分流和准备 PR，不能批准 merge 或 promotion。
```

## Candidate thread 模板

```markdown
## 类型

Case / Candidate Pattern / Factor / Environment Rule / Negative Pattern

## 观察到的问题

一句话说明这个对象解决什么判断问题。

## 证据

- 场景来源：
- 复现步骤或 session 摘要：
- before 行为：
- after / expected 行为：
- 当前 evidence level：Level 0 / 1 / 2 / 3 / 4 / 5

## 隐私

- 是否包含客户、公司、内部路径、secret、原始日志：
- 已做的 redaction：
- 仍不确定的风险：

## 建议路线

留在 Discord / 转 GitHub issue / 转 Candidate PR / 转 RFC / 暂不吸收
```

## 维护者 triage 口径

维护者在 Discord 只做四类判断：

1. `needs-proof`：证据不足，要求补 real behavior proof。
2. `needs-redaction`：存在隐私风险，先脱敏。
3. `ready-for-pr`：可以转 GitHub issue 或 PR。
4. `route-to-rfc`：影响治理、ontology、workflow、skill，先 RFC。

不要在 Discord 做 `approved`、`merged`、`core` 这类正式结论。正式状态仍以 GitHub repo 和 governance 文档为准。

## 与现有治理文档的对应关系

| 已有机制 | Discord 融入方式 |
| --- | --- |
| `PR Guidelines` 的 one PR / one layer | one thread / one object |
| `Evidence Policy` 的 evidence levels | Candidate 模板要求标注 evidence level |
| `Candidate Lifecycle` | Discord 只到 draft / ready-for-pr，不直接 promotion |
| `Auto Triage Policy` | 先由维护者用文字标签模拟，后续再接 bot |
| `Maintainer Playbook` | Discord triage 后才进入 GitHub review queue |
| `Release And Promotion Policy` | reviewed/core/deprecated 仍在 repo 内维护 |

## 不建议现在做的事

- 不要接 Discord bot 自动判定 approved。
- 不要把 GitHub label 和 automerge 搬到 Discord。
- 不要让投票决定 Candidate promotion。
- 不要在 Discord 保存 raw session log。
- 不要让 Discord thread 替代 RFC、PR template 或 CODEOWNERS。

## 7 天试运行

第 1 天：

- 建立一个贡献频道。
- 置顶说明草案。
- 要求所有讨论使用 thread 前缀。

第 2-4 天：

- 维护者只做 route、proof、redaction 三类提醒。
- 不急着引入 bot。
- 收集 3-5 个真实 thread 作为样本。

第 5-7 天：

- 复盘哪些 thread 能转为 Candidate PR。
- 把常见问题沉淀为 FAQ 或 docs issue。
- 判断是否需要拆出 `candidate-lab` 和 `redaction-help`。

试运行成功标准：

- 至少 3 个 thread 能明确分流。
- 至少 1 个 Candidate 达到 Level 2+ evidence。
- 没有 raw private context 被直接搬进公开 PR。
- 维护者没有被零散聊天淹没。
