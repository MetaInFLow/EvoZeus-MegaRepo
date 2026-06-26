# Development Direction

- Status: active
- Last updated: 2026-06-20
- Scope: EvoZeus 当前阶段开发方向、repo 分工和完成标准
- Owner: MetaInFlow

本目录定义 EvoZeus 的开发方向。它不是长期愿景口号，而是回答当前阶段应该先做什么、为什么做、做到什么程度才算完成。

## 1. 当前阶段判断

EvoZeus 当前处在 **methodology-first + community-intake-first + protocol-only-boundary** 阶段。

含义：

- 先稳定“判断高质量信号”的方法论：Evidence grading、Case framing、Verdict criteria、counterexample loop 和 artifact promotion。
- `EvoZeus` 主 repo 的 zero-install protocol、Case / Candidate / Verdict / Factor 语义和治理流程服务于这套方法论。
- `EvoZeus` 主 repo 只拥有 protocol、governance、intake、semantic artifact 和 registry pointer，不拥有 runtime 执行层。
- 让 `evozeus-web` 的部署面成为 public-facing 解释层和社区入口，重点解释如何贡献高质量信号判断材料；Web 源码保持 private。
- Skill 不是北极星。Skill 体系只负责 agent-readable 接入、路由和行为固化；只有当判断规则足够稳定时，才考虑沉淀为 Skill。
- Factor tools 不直接塞进主 repo；`evozeus-session-signal-skill` 承载 Session Signal SKILL、Python factor tool contract、spec 和脱敏 examples，不承载真实业务 pack 生命周期。
- `evozeus-infra` 暂时不抢跑，等 registry、trust policy、scanner permission model 稳定后再进入可执行产品面。
- 主 repo 的旧执行层遗留已清理；runtime 设计材料已移至 `10-repos/evozeus-infra/docs/`，scanner / runner prototype 已移至 `10-repos/evozeus-infra/prototypes/main-repo-runtime/`，不作为主 repo 的默认用户入口、安装源或 official runtime contract。

## 2. 开发方向

| 方向 | 当前优先级 | 目标 |
| --- | --- | --- |
| High-quality Signal Methodology | P0 | 按 [高质量信号判断方法论](high-quality-signal-methodology.md) 收敛 Evidence、Case、Verdict、反例和沉淀标准 |
| Protocol / Governance | P0 | 主 repo 的核心语义、贡献路径、review gate、privacy gate 和 registry pointer 稳定 |
| Web Surface | P0 | 官网部署面能解释高质量信号判断方法论、社区贡献路径和 `/skill` agent 接入边界；源码保持 private |
| Interaction / Verdict Surface | P0/P1/P2 | 按 [EvoZeus 交互体验设计路线](evozeus-interaction-design-roadmap.md) 先做 Verdict Card，再改首页体验，最后沉淀 Signal Review Rubric |
| Skill System Support | P1 | `/skill`、注册安装、scenario skills、component handoff 和 validator 形成支撑闭环，但不作为项目主产出 |
| Infra Local Execution Kernel | P1 | 按 [Infra Local Execution Kernel 开发标准](infra-local-execution-kernel-development-standard.md) 将旧 `__infra__` 拆成可验证的本地执行内核 |
| Official Super SKILL / Factor Tools | P1 | `SKILL.md` 能组合 factor tool 输出判断高价值历史记录；Python factor tool contract、spec、example 和 result contract 清晰 |
| Runtime Trust | P1 | 明确 local-first、opt-in scanner、permission、Factor contract、lockfile 规则，并在 `evozeus-infra` 承接实现 |
| Tutorials / Onboarding | P1 | 每个部分都有可跟随的入门教程，降低 Agent 和新人进入成本 |
| Automation / CI | P2 | 把已经稳定的手工门禁沉淀为脚本或 CI |

## 3. Repo 分工

| Repo | 开发方向 |
| --- | --- |
| `EvoZeus-MegaRepo` | 跨 repo 方向、索引、教程、权限模型、决策记录 |
| `EvoZeus` | public protocol、`SKILL.md`、ontology、schema、governance、Case/Candidate intake、semantic artifact、registry pointer |
| `evozeus-web` | private Web 源码；公开部署面、`/skill`、Discord / GitHub contribution route |
| `evozeus-session-signal-skill` | Session Signal SKILL：`SKILL.md` 方法层、Python OfficialFactor tools、官方 spec schema、canonical examples |
| `evozeus-infra` | future CLI/TUI/local registry/report/selective install；承接执行层和从主 repo 迁出的 runtime prototype |

## 4. 当前执行顺序

1. 稳定高质量信号判断方法论：Evidence grading、Case framing、Verdict criteria、counterexample loop 和 artifact promotion。
2. 稳定主 repo 的 Protocol-only 边界：protocol、Candidate schema、PR routing、privacy、proof gates、registry pointer。
3. 按 [EvoZeus 交互体验设计路线](evozeus-interaction-design-roadmap.md) 先产品化 `Session Verdict Card`，再把首页改成“体验一次裁决”，最后沉淀 Signal Review Rubric。
4. 把社区入口讲清楚：官网、Discord 缓冲层、GitHub issue / PR 路线，优先承接 Case / Evidence / counterexample，而不是直接承接 Skill 生成。
5. 收敛 Skill 体系：按 [Skill System Implementation Plan](skill-system-implementation.md) 修正 `/skill`、注册安装 owner、runtime skill 命名冲突、route precedence 和 cluster validator；这属于 agent 接入支撑层。
6. 保持 `EvoZeus` 主 repo 无执行层结构；runtime 文档和未来实现落在 `evozeus-infra`。
7. 按 [Infra Local Execution Kernel 开发标准](infra-local-execution-kernel-development-standard.md) 拆迁旧 `__infra__`：先 workspace/config/lockfile，再 SQLite ledger，再 scanner/resolver、factor runner、scan/analyze service 和 CLI/TUI/companion/report。
8. 收敛 Session Signal SKILL：`session-signal-skill` 的 `SKILL.md` 负责高价值历史记录判断方法，`factors/<slug>/` 是可解释 factor tools。
9. 补齐 factor tool contract：稳定 Python `OfficialFactor`、官方 schema、`FACTOR.xml`、spec 和 canonical examples。
10. 等 trust policy 稳定后，在 `evozeus-infra` 启动可执行能力；用户可安装前 repo 必须 public。

## 5. 完成标准

一个方向可以算阶段性完成，至少要满足：

- 有清晰 owner。
- 有 repo 落点。
- 有 docs 或 tutorial 入口。
- 有 review gate 或手工 checklist。
- 有 privacy / security 边界。
- 有一条从 contribution 到 accepted artifact 的路径。
- 能说明它如何提升“判断高质量信号”的方法论。
- 有明确不做什么。

## 6. 不做什么

当前阶段不做：

- 自动上传 raw session。
- 默认安装 scanner / runtime / cloud client。
- 把 Skill 生成数量当作项目目标或阶段性 KPI。
- 把 Factor pack、scanner code 或 official release 直接放进 `EvoZeus` 主 repo。
- 把真实业务 Factor pack、scanner module、manifest、checksum、SBOM 或 attestation 放进 `evozeus-session-signal-skill`。
- 把 CLI / TUI / companion / local API / `.evozeus` state / SQLite ledger 作为 `EvoZeus` 主 repo 的目标职责。
- 先做复杂 dashboard 再补语义。
- 给社区共创者默认 repo write 权限。
- 创建独立 `evozeus-skills` repo；该决策仍为 deferred。
