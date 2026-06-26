# 高质量信号判断方法论

- Status: active
- Last updated: 2026-06-26
- Scope: EvoZeus 当前阶段的北极星、社区共创闭环和方法论资产边界
- Owner: MetaInFlow

EvoZeus 的核心目标不是生产 Skill，而是通过社区真实案例，迭代一套可复核、可反驳、可沉淀的“高质量信号判断方法论”。

## 1. 北极星

EvoZeus 要回答的问题是：

> 在一次真实 Agent Session 中，哪些迹象值得被认为是高质量信号，为什么，适用于哪些上下文，遇到什么反例时应该收回或修正？

因此，项目成功不看生成了多少 Skill，而看社区是否能更稳定地完成这些动作：

- 从真实 session 中识别有价值的信号。
- 用 Evidence 说明判断依据。
- 把发现整理成 Case，而不是停留在观点。
- 通过 Verdict 明确下一步动作。
- 用反例、边界条件和复盘结果持续修正判断规则。
- 把稳定规则沉淀为合适的 Artifact。

## 2. 什么是高质量信号

高质量信号不是“看起来有道理”的建议。它至少满足：

| 条件 | 含义 |
| --- | --- |
| 来自真实情境 | 来源于真实 session、issue、review、运营记录或可复现实验 |
| 可被复核 | 有可定位、可脱敏、可供 reviewer 检查的 Evidence |
| 有判断价值 | 能帮助未来更好地 preserve、fix、extract、reject 或 open |
| 有适用边界 | 说明在哪些场景有效，哪些场景不适用 |
| 可被反驳 | 能记录 counterexample，而不是变成不可质疑的原则 |
| 可落地 | 最终能进入 Case、Factor、Pattern、Habit、Environment Rule、Skill 或 Rejected Pattern |

## 3. 社区共创闭环

```text
Community Observation
  -> Evidence Packet
  -> Case
  -> Verdict
  -> Counterexample / Review
  -> Judgment Rule
  -> Artifact
  -> Library
  -> New Observation
```

社区贡献的重点是提供更好的判断材料，而不是直接提交结论。

| 阶段 | 社区贡献什么 | Reviewer 判断什么 |
| --- | --- | --- |
| Observation | 真实现象、上下文、影响 | 是否来自真实情境 |
| Evidence Packet | 脱敏证据、定位信息、复现条件 | 证据是否足够支撑判断 |
| Case | 问题或机会的结构化描述 | 是否值得进入 Verdict |
| Verdict | 建议 preserve / extract / fix / reject / open | 动作是否匹配证据 |
| Counterexample | 反例、边界、失败案例 | 规则是否需要收窄 |
| Artifact | Factor、Pattern、Habit、Environment Rule、Skill 等 | 是否应该进入 Library |

## 4. Artifact 边界

Skill 只是 Artifact 的一种。默认不应该把每个发现都升级为 Skill。

| Artifact | 适合什么时候用 |
| --- | --- |
| Case | 有价值但还需要继续观察 |
| Factor | 判断规则可以被重复触发或自动辅助识别 |
| Pattern | 行为模式值得保留、传播或对照 |
| Habit | 轻量实践足够，不需要完整指令体系 |
| Environment Rule | 问题根因在路径、版本、权限、网络或工具配置 |
| Skill | 行为模式已经稳定，且需要成为 agent-readable instruction |
| Rejected Pattern | 明确有害、低信号或容易误导，需要沉淀为反例 |

判断顺序应该是：先问“这个信号是否成立”，再问“它应该沉淀成什么”。不要从“我要生成一个 Skill”倒推材料。

## 5. 当前 P0-P2 工作

当前阶段优先补齐：

1. P0 Session Verdict Card：把一次 session 的 Evidence、Judgment Signals、Proposed Verdict、Artifact Route 和 Next Action 放到同一张卡里。
2. P1 首页体验：第一屏直接展示一次真实裁决，而不是抽象介绍项目愿景。
3. P2 Signal Review Rubric：用 review gate 判断信号强度，避免默认升级为 Skill。
4. Evidence grading：什么证据足以支持一个高质量信号。
5. Case framing：社区如何把观察写成可审查 Case。
6. Verdict criteria：不同 Verdict 的判断边界。
7. Counterexample loop：如何收集反例并修正规则。
8. Community intake：Discord、GitHub issue / PR 和 docs 如何承接贡献。

Skill 体系、runtime、Factor contract 和 report 生成都是支撑这些工作的工具层。

## 6. Signal Review Rubric

Rubric 是 reviewer 的 decision gate，不是 agent score。Factor 可以提出信号，不能替代最终裁决。

| Rating | 使用条件 | 默认动作 |
| --- | --- | --- |
| Strong | 至少 `E3` evidence；有直接 judgment signal；能说明适用边界和反例风险；下一步 Artifact Route 清晰 | 进入 Candidate Review，可提议 Accepted Artifact |
| Medium | 有 `E2` 或 `E3` evidence；信号有价值但边界、重复性或 route 仍需讨论 | `Open Case` 或 `Preserve`，继续补 evidence / counterexample |
| Weak | 只有 `E1` 或零散 `E2`；更像观察、偏好或单次体验 | 保留为 Draft Case，不进入 Library |
| Blocked | evidence 无法定位、未脱敏、raw material 不可公开，或 claim 和 evidence 不匹配 | 不进入 public review，先补定位、脱敏或重写 claim |

Reviewer 每次至少回答四个问题：

1. 这个 claim 是否有可定位 evidence 支撑？
2. 这个信号会改变下一次 agent / human 的判断吗？
3. 它应该落成哪类 Artifact，而不是默认 Skill？
4. 什么反例会让这条判断收窄、降级或撤回？

## 7. 非目标

当前阶段不以这些作为核心目标：

- 追求 Skill 数量。
- 把一次性经验包装成长期指令。
- 用自动化评分替代社区 review。
- 默认上传 raw session。
- 先做复杂 runtime / dashboard，再补判断方法论。
- 把没有 Evidence 的观点收进 Library。
