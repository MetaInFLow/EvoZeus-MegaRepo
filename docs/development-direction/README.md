# Development Direction

- Status: active
- Last updated: 2026-06-18
- Scope: EvoZeus 当前阶段开发方向、repo 分工和完成标准
- Owner: MetaInFlow

本目录定义 EvoZeus 的开发方向。它不是长期愿景口号，而是回答当前阶段应该先做什么、为什么做、做到什么程度才算完成。

## 1. 当前阶段判断

EvoZeus 当前处在 **protocol-first + community-intake-first + protocol-only-boundary** 阶段。

含义：

- 先让 `EvoZeus` 主 repo 的 zero-install protocol、Case / Candidate / Verdict / Factor 语义和治理流程稳定。
- `EvoZeus` 主 repo 只拥有 protocol、governance、intake、semantic artifact 和 registry pointer，不拥有 runtime 执行层。
- 让 `EvoZeus-community` 的部署面成为 public-facing 解释层和社区入口，但 Web 源码保持 private。
- Factor 不直接塞进主 repo；按 lifecycle 拆到 `evozeus-factor-lab` 和 `evozeus-factors-official`。
- `evozeus-runtime` 暂时不抢跑，等 registry、trust policy、scanner permission model 稳定后再进入可执行产品面。
- 主 repo 的旧执行层遗留已清理；runtime 设计材料已移至 `10-repos/evozeus-runtime/docs/`，scanner / runner prototype 已移至 `10-repos/evozeus-runtime/prototypes/main-repo-runtime/`，不作为主 repo 的默认用户入口、安装源或 official runtime contract。

## 2. 开发方向

| 方向 | 当前优先级 | 目标 |
| --- | --- | --- |
| Protocol / Governance | P0 | 主 repo 的核心语义、贡献路径、review gate、privacy gate 和 registry pointer 稳定 |
| Community Surface | P0 | 官网部署面和 `/skill` 能解释 EvoZeus，并把注册安装导向 public 主 repo；源码保持 private |
| Skill System Closure | P0 | `/skill`、注册安装、scenario skills、component handoff 和 validator 形成闭环 |
| Factor Lifecycle | P1 | Factor Candidate、lab、official release、registry pointer 的流转清晰 |
| Runtime Trust | P1 | 明确 local-first、opt-in scanner、permission、manifest、checksum、attestation 规则，并在 `evozeus-runtime` 承接实现 |
| Tutorials / Onboarding | P1 | 每个部分都有可跟随的入门教程，降低 Agent 和新人进入成本 |
| Automation / CI | P2 | 把已经稳定的手工门禁沉淀为脚本或 CI |

## 3. Repo 分工

| Repo | 开发方向 |
| --- | --- |
| `EvoZeus-MegaRepo` | 跨 repo 方向、索引、教程、权限模型、决策记录 |
| `EvoZeus` | public protocol、`SKILL.md`、ontology、schema、governance、Case/Candidate intake、semantic artifact、registry pointer |
| `EvoZeus-community` | private Web 源码；公开部署面、`/skill`、Discord / GitHub contribution route |
| `evozeus-factor-lab` | Factor pack / scanner module 的 submissions、reviewed、rejected、templates、checks |
| `evozeus-factors-official` | official Factor packs、release manifest、checksum、SBOM/attestation |
| `evozeus-runtime` | future CLI/TUI/local registry/report/selective install；承接执行层和从主 repo 迁出的 runtime prototype |

## 4. 当前执行顺序

1. 稳定主 repo 的 Protocol-only 边界：protocol、Candidate schema、PR routing、privacy、proof gates、registry pointer。
2. 收敛 Skill 体系：按 [Skill System Implementation Plan](skill-system-implementation.md) 修正 `/skill`、注册安装 owner、runtime skill 命名冲突、route precedence 和 cluster validator。
3. 把社区入口讲清楚：官网、Discord 缓冲层、GitHub issue / PR 路线。
4. 保持 `EvoZeus` 主 repo 无执行层结构；runtime 文档和未来实现落在 `evozeus-runtime`。
5. 补齐 Factor lab 的 public gate：submission template、redaction rule、scanner permission policy、secret/license scan；用户投稿前 repo 必须 public / PR-gated。
6. 用第一个 reviewed Factor pack 跑通 official release：tag、manifest、checksum、SBOM/attestation、main registry pointer；用户或 runtime 可消费前 repo 必须 public。
7. 等 trust policy 稳定后，在 `evozeus-runtime` 启动可执行能力；用户可安装前 repo 必须 public。

## 5. 完成标准

一个方向可以算阶段性完成，至少要满足：

- 有清晰 owner。
- 有 repo 落点。
- 有 docs 或 tutorial 入口。
- 有 review gate 或手工 checklist。
- 有 privacy / security 边界。
- 有一条从 contribution 到 accepted artifact 的路径。
- 有明确不做什么。

## 6. 不做什么

当前阶段不做：

- 自动上传 raw session。
- 默认安装 scanner / runtime / cloud client。
- 把 Factor pack、scanner code 或 official release 直接放进 `EvoZeus` 主 repo。
- 把 CLI / TUI / companion / local API / `.evozeus` state / SQLite ledger 作为 `EvoZeus` 主 repo 的目标职责。
- 先做复杂 dashboard 再补语义。
- 给社区共创者默认 repo write 权限。
- 创建独立 `evozeus-skills` repo；该决策仍为 deferred。
