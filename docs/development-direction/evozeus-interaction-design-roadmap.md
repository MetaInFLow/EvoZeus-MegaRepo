# EvoZeus 交互体验设计路线

- Status: design draft
- Last updated: 2026-06-26
- Scope: P0 Verdict Card、P1 首页体验、P2 Signal Rubric
- Owner: MetaInFlow

本文定义 EvoZeus 下一阶段的交互体验设计路线。它不是视觉改版清单，而是把“高质量信号判断方法论”转成用户可以看见、理解、复核和继续行动的产品闭环。

## 0. TLDR

EvoZeus 当前的真问题不是缺页面，而是 judgment layer 的关键动作还不够可感知。

P0 先做一张高质量的 `Session Verdict Card`，让一次 session 的 Evidence、Signals、Verdict、Artifact Route 和 Next Action 在第一屏就能被复核。P1 再把官网首页改成“体验一次裁决”的叙事，让新用户不用读完整方法论文档也能理解 EvoZeus。P2 最后沉淀 Signal Review Rubric，让 reviewer 和 agent 能稳定判断什么信号值得留下，但不让自动评分替代 human review。

借鉴对象是 [`alchaincyf/darwin-skill`](https://github.com/alchaincyf/darwin-skill) 的交互骨架：闭环清楚、结果可视、阶段可验证、human-in-the-loop。相关方法论来源包括 [`karpathy/autoresearch`](https://github.com/karpathy/autoresearch) 和 [`microsoft/SkillOpt`](https://github.com/microsoft/SkillOpt)。不要照搬它的 orange 视觉、skill optimizer 定位或自动打分崇拜。

## 1. 背景与一阶判断

EvoZeus 的北极星是：

> 通过社区真实案例，持续迭代“如何判断高质量信号”的方法论。

现有资产已经具备语义基础：

- `10-repos/evozeus/docs/reference/verdict-card.md` 定义了 `Session Verdict Card` 的字段。
- `10-repos/evozeus-infra/src/evozeus_runtime/sessions/schema.py` 已有 `SessionVerdictCard` schema。
- `10-repos/evozeus-web/src/app/page.tsx` 已经使用真实案例解释 Before / After。
- `docs/development-direction/high-quality-signal-methodology.md` 已经定义 Evidence、Case、Verdict、Counterexample 和 Artifact 边界。

缺口在体验层：

| 缺口 | 当前表现 | 影响 |
| --- | --- | --- |
| 裁决结果不可视 | runtime HTML report 仍偏工程表格 | 用户看不出“为什么这样判” |
| 首页没有第一屏完成体验 | 首页解释了理念，但没有让用户看到完整裁决动作 | 新用户需要读太多文字才理解价值 |
| 信号判断缺少可复核 rubric | 方法论有方向，但 reviewer 执行时仍容易靠经验 | 社区贡献质量不稳定 |

第一性原则：EvoZeus 不是“生成更多 Skill”的系统，而是把一次真实 Agent Session 放到 Evidence-backed review 流程里，判断它是否值得沉淀、应该沉淀成什么、下一步谁来做。

## 2. 设计原则

| 原则 | 设计含义 |
| --- | --- |
| Outcome first | 每个入口先展示本次判断结果，不先展示系统能力清单 |
| Evidence first | 所有 Verdict 必须能回到具体 Evidence；没有 Evidence 就默认 Open Case |
| Progressive disclosure | 先给卡片摘要，再展开证据、信号、反例和 artifact route |
| Human review gate | 自动化只能给 proposed verdict；保存、公开、沉淀前需要人审 |
| No fake precision | 不用“Agent 得分”包装判断；必要时用证据强度或 confidence band，并说明来源 |
| Public-safe language | 对外页面不出现内部调试语言、未审承诺或 private context |

## 3. 非目标

本设计不做这些事：

- 不把 EvoZeus 改成 Skill optimizer。
- 不新增“Agent 排名”或“Agent 评分”。
- 不默认上传 raw session。
- 不让 homepage 承诺尚未稳定的 runtime / scanner 自动能力。
- 不先做复杂 dashboard。
- 不用自动 rubric 结果替代 reviewer 的最终 Verdict。

## 4. P0: Verdict Card 产品化

### 4.1 目标

把现有 `Session Verdict Card` 从 Markdown 输出结构升级为可视化、可复核、可导出的核心交互单元。

成功后，用户看到一张卡就能回答：

1. 这次 session 的建议 Verdict 是什么？
2. 这个 Verdict 由哪些 Evidence 支撑？
3. 触发了哪些 Judgment Signals？
4. 应该沉淀成什么 Artifact？
5. 哪些内容需要留在本地或脱敏？
6. 下一步动作是什么？

### 4.2 用户场景

| 用户 | 场景 | 期望 |
| --- | --- | --- |
| 首次用户 | 复制 `/skill` 入口后运行 protocol-only judgment | 在回复中看到可读的 Verdict Card |
| Maintainer | review 一个社区提交的 Case | 快速定位证据、反例和建议动作 |
| Agent | 执行 runtime report renderer | 从 JSON / FactorResult 生成同一语义的 HTML card |
| Contributor | 准备公开分享案例 | 知道哪些信息需要脱敏，哪些不能公开 |

### 4.3 信息结构

`Session Verdict Card` 使用 6 个区块：

| 区块 | 字段 | 说明 |
| --- | --- | --- |
| Header | session_id、task_context、proposed_verdict | 第一眼看到这次判断的对象和结论 |
| Evidence | key_evidence、evidence_refs、evidence_strength | 展示最小支撑证据，不展开 raw session |
| Signals | judgment_signals、top_factor_signals | 说明为什么这些行为有判断价值 |
| Artifact Route | suggested_artifact、route_reason | 说明 Preserve / Promote / Extract / Fix / Reject / Open 后落到哪里 |
| Risk & Boundary | counterexample_risk、privacy_note、uncertainty | 防止把局部经验包装成通用原则 |
| Next Action | suggested_next_action、optional_next_steps | 给出可执行的下一步，标明是否需要用户批准 |

### 4.4 视觉形态

卡片不做炫技 UI。优先使用稳定、可截图、可打印、可复制的布局：

```text
┌──────────────────────────────────────────────┐
│ Proposed Verdict: Fix Environment            │
│ Task: 读取 Feishu 文档前反复寻找入口          │
├──────────────────────────────────────────────┤
│ Evidence                                     │
│ - PATH 中无 larkcli，但存在 lark-cli fallback │
│ - 历史记录多次出现入口查找                   │
├──────────────────────────────────────────────┤
│ Signals                                      │
│ - repeated environment friction              │
│ - next-use value is high                     │
├──────────────────────────────────────────────┤
│ Artifact Route: Environment Rule             │
│ Risk: 只适用于本机 Feishu/Lark CLI 场景       │
│ Privacy: 不公开 raw path / private URL       │
├──────────────────────────────────────────────┤
│ Next Action: 保存脱敏 Case，更新入口规则      │
└──────────────────────────────────────────────┘
```

HTML 版本可以增强为：

- verdict 状态条：Preserve / Promote / Extract / Fix / Reject / Open。
- evidence trace 区：显示证据数量、证据类型、脱敏状态。
- signal chips：展示 top 3 signals。
- artifact route 区：显示建议沉淀类型。
- privacy banner：任何公开风险必须在卡片内可见。
- copy markdown / export HTML 两个基础动作；PNG export 作为后续增强，不进入 P0 默认范围。

### 4.5 数据和工程落点

| 落点 | 变更 |
| --- | --- |
| `10-repos/evozeus/docs/reference/verdict-card.md` | 补充 visual card contract，但保留 Markdown 为 canonical zero-install 输出 |
| `10-repos/evozeus-infra/src/evozeus_runtime/sessions/schema.py` | 如需要，扩展可选字段：`evidence_strength`、`suggested_artifact`、`counterexample_risk` |
| `10-repos/evozeus-infra/src/evozeus_runtime/reports/html.py` | 从简单表格升级为 Verdict Card HTML renderer |
| `10-repos/evozeus-infra/tests/` | 增加 fixture，验证 renderer 不泄露 raw session |
| `10-repos/evozeus/examples/` | 增加脱敏 sample card，供 homepage 和 docs 复用 |

### 4.6 验收标准

P0 完成必须满足：

- 一次 protocol-only judgment 能输出 Markdown `Session Verdict Card`。
- 一次 infra fixture report 能生成 HTML `Session Verdict Card`。
- 卡片必须包含 Evidence、Signals、Proposed Verdict、Artifact Route、Privacy、Next Action。
- 卡片不能展示未脱敏 raw private path、private URL、token 或完整 raw session。
- Verdict 必须绑定至少一条 Evidence；没有足够证据时默认 `Open Case`。
- 有一个脱敏样例可以放到官网首页复用。

### 4.7 验证命令

```bash
cd /Users/anthonyf/Documents/EvoZeus-cluster/10-repos/evozeus-infra
PYTHONPATH=src python -m pytest -q
PYTHONPATH=src python -m evozeus_runtime.cli.main report --session-id session-minimal --format html --workspace /tmp/evozeus-workspace
```

## 5. P1: 首页改成“体验一次裁决”

### 5.1 目标

官网首页第一屏不再只解释 EvoZeus 是什么，而是让用户看到一次具体 session 如何变成 Verdict。

用户 10 秒内应该理解：

```text
真实 Agent Session
  -> Evidence
  -> Judgment Signals
  -> Proposed Verdict
  -> Artifact Route
  -> Next Action
```

### 5.2 首页信息架构

| 顺序 | 模块 | 目标 |
| --- | --- | --- |
| 1 | Hero: 一次裁决 | 展示脱敏 Verdict Card 摘要，不只放 slogan |
| 2 | Case Before / After | 用真实例子解释为什么这个信号值得留下 |
| 3 | Evidence Trace | 展示证据如何支撑 Verdict |
| 4 | Artifact Route | 解释为什么不是所有发现都变成 Skill |
| 5 | Community Intake | 引导提交 Case / Counterexample，而不是直接提交结论 |
| 6 | Start Here | 保留 `/skill` 注册安装入口，明确它不是 runtime runner |

### 5.3 第一屏建议

Hero 的主文案不要抽象：

```text
把一次真实 Agent Session
变成可复核的裁决
```

副文案：

```text
EvoZeus 先看 Evidence，再判断这个经验该 preserve、fix、extract、reject，还是继续 open。
```

第一屏右侧或下方直接放脱敏 `Session Verdict Card`，展示：

- proposed verdict。
- 2 条 key evidence。
- 2 个 judgment signals。
- artifact route。
- next action。

CTA：

- 主按钮：`看一次裁决`
- 次按钮：`提交案例/反例`
- 辅助入口：`复制 /skill 接入`

### 5.4 交互规则

- 首页不承诺自动扫描用户 workspace。
- 首页不展示 private raw session 示例。
- 首页不把 Skill 生成作为默认成功路径。
- `/skill` 文案保持 install-first / bootstrap-only。
- 移动端第一屏必须同时露出主视觉和下一段内容提示，避免首屏像纯营销页。
- 保留当前真实案例方向，但把案例结果升级为 Verdict Card，而不是只做 Before / After 文案。

### 5.5 工程落点

| 落点 | 变更 |
| --- | --- |
| `10-repos/evozeus-web/src/app/page.tsx` | 重排首页模块，让 Verdict Card 成为第一屏信号 |
| `10-repos/evozeus-web/src/app/page.test.tsx` | 测试首页展示 `Session Verdict Card`、Evidence、Artifact Route、Start Here |
| `10-repos/evozeus-web/src/app/globals.css` | 若需要，补稳定卡片尺寸和 responsive constraints |
| `10-repos/evozeus/examples/` 或 web public assets | 使用脱敏样例，不使用真实 private context |

### 5.6 验收标准

P1 完成必须满足：

- 首屏出现 EvoZeus 的对象、动作和结果：Session、Evidence、Verdict。
- 页面不再把 `/skill` 描述成 judgment/runtime runner。
- 用户能从首页看懂“不是所有发现都变成 Skill”。
- 页面上所有案例都为脱敏案例。
- Desktop 和 mobile 截图无文字重叠、按钮溢出或卡片挤压。
- 现有 page tests 通过。

### 5.7 验证命令

```bash
cd /Users/anthonyf/Documents/EvoZeus-cluster/10-repos/evozeus-web
pnpm test
pnpm build
```

## 6. P2: Signal Review Rubric

### 6.1 目标

建立 reviewer 和 agent 都能使用的高质量信号判断 rubric。它用于校准判断，不用于生成“Agent 分数”。

rubric 的输出应该是：

- 每个维度的 evidence-backed rating。
- 是否足以形成 proposed verdict。
- 如果不足，缺什么证据。
- 推荐 artifact route。

### 6.2 Rubric 维度

| 维度 | 判断问题 | 强信号标准 | 弱信号或反例 |
| --- | --- | --- | --- |
| Evidence traceability | 能否回到具体证据？ | 有可定位、可脱敏、可复核的 evidence refs | 只有主观总结，没有上下文 |
| Recurrence | 是否重复出现或代表稳定模式？ | 多次独立出现，或一次高影响事件有清晰复现路径 | 只是一时偏好或偶然噪声 |
| Next-use value | 是否会改变下一次行动？ | 沉淀后能减少重复查找、误判、返工或风险 | 记录了也不会影响下一次 |
| Boundary clarity | 适用边界是否清楚？ | 明确适用场景、不适用场景和前置条件 | 被包装成万能原则 |
| Counterexample coverage | 是否允许被反驳和修正？ | 有反例入口，能说明何时收回规则 | 只保留正例，不能被挑战 |
| Artifact fit | 应该沉淀成什么？ | 能区分 Case、Factor、Pattern、Habit、Environment Rule、Skill、Rejected Pattern | 默认一切都 Promote to Skill |

### 6.3 Rating 规则

每个维度只给等级，不给产品化总分：

| Rating | 含义 | 后续动作 |
| --- | --- | --- |
| Strong | 证据足够，判断稳定 | 可进入 proposed verdict |
| Medium | 有价值，但边界或证据不足 | 保留为 Open Case 或补证据 |
| Weak | 当前不足以支撑判断 | 不进入 Library |
| Blocked | 涉及隐私、缺 source 或无法复核 | 先处理 privacy / evidence gap |

默认 gate：

- `Evidence traceability` 为 Weak 或 Blocked：不能 Promote / Extract / Fix，只能 Open Case 或 Reject Pattern。
- `Boundary clarity` 为 Weak：不能沉淀为通用 Skill。
- `Artifact fit` 为 Weak：不能进入 Library。
- 任何 privacy Blocked：不能公开。

### 6.4 输出结构

```json
{
  "signal_review": {
    "session_id": "string",
    "candidate_signal": "string",
    "ratings": [
      {
        "dimension": "Evidence traceability",
        "rating": "Strong",
        "evidence_refs": ["event-001"],
        "reason": "可定位到用户重复修正和工具输出"
      }
    ],
    "proposed_verdict": "Fix Environment",
    "suggested_artifact": "Environment Rule",
    "missing_evidence": [],
    "counterexample_questions": [
      "这个问题是否只发生在当前机器？",
      "换 runtime 后是否仍存在？"
    ],
    "human_review_required": true
  }
}
```

### 6.5 工程落点

| 落点 | 变更 |
| --- | --- |
| `docs/development-direction/high-quality-signal-methodology.md` | 增加 rubric 摘要和 gate 规则 |
| `10-repos/evozeus/docs/reference/evidence-grading.md` | 对齐 Evidence traceability gate |
| `10-repos/evozeus/docs/reference/verdicts.md` | 明确 rating 如何影响 Verdict |
| `10-repos/evozeus-session-signal-skill/SKILL.md` | 让 Session Signal SKILL 组合 factor tools 时使用 rubric |
| `10-repos/evozeus-infra/src/evozeus_runtime/factors/dashboard_signals.py` | 后续把 factor result 映射成 rubric evidence，不直接生成最终 Verdict |

### 6.6 验收标准

P2 完成必须满足：

- rubric 能处理至少 3 个脱敏案例：强信号、弱信号、隐私 blocked。
- reviewer 能根据 rubric 解释为什么一个发现是 Case / Factor / Skill / Rejected Pattern。
- factor output 只能提供 `verdict_signals` 和 evidence，不直接替代最终 Verdict。
- 文档明确“没有 Evidence 不形成 Verdict”。
- 公开入口不展示产品化总分。

## 7. 实施顺序

| 优先级 | 任务 | Owner repo | 验收 |
| --- | --- | --- | --- |
| P0.1 | 补 visual Verdict Card contract | `EvoZeus` | reference doc 更新 |
| P0.2 | 做 infra HTML Verdict Card renderer | `evozeus-infra` | fixture report 生成 HTML card |
| P0.3 | 产出脱敏样例卡片 | `EvoZeus` / `evozeus-infra` | 首页可复用 |
| P1.1 | 首页 IA 改成“体验一次裁决” | `evozeus-web` | 首屏可见 Verdict Card |
| P1.2 | 首页测试和响应式验证 | `evozeus-web` | test/build/screenshot 通过 |
| P2.1 | Signal Review Rubric 文档 | `EvoZeus` / mega docs | 3 个案例可套用 |
| P2.2 | official factor tools 对齐 rubric | `evozeus-session-signal-skill` | factor 不替代 Verdict |

## 8. 风险与处理

| 风险 | 表现 | 处理 |
| --- | --- | --- |
| 伪精确 | 用户误解为 Agent 得分系统 | 不展示总分，只展示 evidence-backed rating |
| 隐私泄露 | 卡片复制了 raw session、private URL 或 path | renderer 默认脱敏，公开前走 privacy gate |
| 跑偏成 Skill 生成器 | 首页把 Promote to Skill 作为主要成功路径 | Artifact Route 必须展示多种沉淀类型 |
| 视觉大于判断 | 花时间做 dashboard，核心 Verdict 仍不清楚 | P0 只做一张卡，P1 只复用这张卡 |
| 自动化越权 | factor output 直接给最终 Verdict | factor 只给 signals，human review 做最终裁决 |

## 9. 未决问题

1. HTML card 是否需要同时支持 PNG export，还是先只支持 HTML + Markdown。
2. 脱敏样例卡片放在主 repo `examples/`，还是 infra fixtures 生成后同步到 web public assets。
3. Signal Review Rubric 是否进入 `EvoZeus` 主 repo reference，还是先保留在 mega repo development direction 直到 reviewer 试用稳定。
4. Evidence strength 是否采用 E0-E4 等级，还是只用 Strong / Medium / Weak / Blocked。

建议默认答案：

- P0 先支持 Markdown + HTML，不做 PNG。
- 样例卡片由 infra fixture 生成，脱敏后复制到 web public assets。
- Rubric 先在 mega repo 固化方向，再进入主 repo reference。
- 产品面使用 Strong / Medium / Weak / Blocked；内部 Evidence Grading 可继续使用 E0-E4。
