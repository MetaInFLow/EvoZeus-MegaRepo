# Development Direction

- Status: active
- Last updated: 2026-06-18
- Scope: EvoZeus 当前阶段开发方向、repo 分工和完成标准
- Owner: MetaInFlow

本目录定义 EvoZeus 的开发方向。它不是长期愿景口号，而是回答当前阶段应该先做什么、为什么做、做到什么程度才算完成。

## 1. 当前阶段判断

EvoZeus 当前处在 **protocol-first + community-intake-first** 阶段。

含义：

- 先让 `EvoZeus` 主 repo 的 zero-install protocol、Case / Candidate / Verdict / Factor 语义和治理流程稳定。
- 再让 `EvoZeus-community` 成为 public-facing 解释层和社区入口。
- Factor 不直接塞进主 repo；按 lifecycle 拆到 `evozeus-factor-lab` 和 `evozeus-factors-official`。
- `evozeus-runtime` 暂时不抢跑，等 registry、trust policy、scanner permission model 稳定后再进入可执行产品面。

## 2. 开发方向

| 方向 | 当前优先级 | 目标 |
| --- | --- | --- |
| Protocol / Governance | P0 | 主 repo 的核心语义、贡献路径、review gate、privacy gate 稳定 |
| Community Surface | P0 | 官网和社区入口能解释 EvoZeus，并把贡献导向主 repo |
| Factor Lifecycle | P1 | Factor Candidate、lab、official release、registry pointer 的流转清晰 |
| Runtime Trust | P1 | 明确 local-first、opt-in scanner、permission、manifest、checksum、attestation 规则 |
| Tutorials / Onboarding | P1 | 每个部分都有可跟随的入门教程，降低 Agent 和新人进入成本 |
| Automation / CI | P2 | 把已经稳定的手工门禁沉淀为脚本或 CI |

## 3. Repo 分工

| Repo | 开发方向 |
| --- | --- |
| `EvoZeus-MegaRepo` | 跨 repo 方向、索引、教程、权限模型、决策记录 |
| `EvoZeus` | public protocol、`SKILL.md`、ontology、schema、governance、Case/Candidate intake |
| `EvoZeus-community` | 官网、社区解释层、Discord / GitHub contribution route |
| `evozeus-factor-lab` | Factor pack / scanner module 的 submissions、reviewed、rejected、templates、checks |
| `evozeus-factors-official` | official Factor packs、release manifest、checksum、SBOM/attestation |
| `evozeus-runtime` | future CLI/TUI/local registry/report/selective install |

## 4. 当前执行顺序

1. 稳定主 repo 的 protocol、Candidate schema、PR routing、privacy 和 proof gates。
2. 把社区入口讲清楚：官网、Discord 缓冲层、GitHub issue / PR 路线。
3. 补齐 Factor lab 的 public gate：submission template、redaction rule、scanner permission policy、secret/license scan。
4. 用第一个 reviewed Factor pack 跑通 official release：tag、manifest、checksum、SBOM/attestation、main registry pointer。
5. 等 trust policy 稳定后，再启动 runtime 的可执行能力。

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
- 先做复杂 dashboard 再补语义。
- 给社区共创者默认 repo write 权限。
- 创建独立 `evozeus-skills` repo；该决策仍为 deferred。
