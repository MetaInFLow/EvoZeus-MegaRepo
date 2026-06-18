# EvoZeus 整体设计

- Status: active
- Last updated: 2026-06-18
- Scope: EvoZeus 全局产品、repo 拓扑、贡献治理、Factor registry、未来 runtime
- Owner: MetaInFlow

本文是 EvoZeus mega repo 的全局设计入口。它不替代 `10-repos/evozeus` 中的协议、schema、技能和治理细节，而是说明多个 repo 如何协同承载 EvoZeus。

## 1. One-line Definition

EvoZeus（宙斯）是 Agent Session Judgment Layer：把真实 Agent Session 放上审判台，什么该沉淀，什么该修正，什么该淘汰，由证据决定。

EvoZeus 不做 agent score，不把 Skill creation 当作唯一目标。它管理：

```text
Session -> Evidence -> Case -> Verdict -> Artifact -> Library
```

## 2. Product Boundary

EvoZeus 当前首先是 agent-readable protocol repo，不是稳定 CLI 产品。

默认承诺：

- zero-install entry：Agent 读 `SKILL.md` 即可开始。
- local-first：raw session 默认留在本地。
- evidence-backed：没有 Evidence 不形成 Verdict。
- user-approved contribution：创建 issue、PR、上传外部平台前必须得到用户确认。
- opt-in runtime packs：scanner、Factor code、MCP、LLM、可视化等运行包必须显式启用。

当前不承诺：

- 自动 raw session 上传。
- 默认扫描本地所有文件。
- 自动创建或合并 PR。
- 完整 CLI/TUI/browser companion/cloud runtime。
- 大规模 benchmark 或 agent 排名。

## 3. Core Loop

```mermaid
flowchart LR
  A["Session<br/>一次真实 Agent 执行"] --> B["Evidence<br/>可复核证据"]
  B --> C["Case<br/>等待审判的发现"]
  C --> D["Verdict<br/>证据化裁决"]
  D --> E["Artifact<br/>可沉淀资产"]
  E --> F["Library<br/>可复用公共资产库"]

  D --> G["Preserve"]
  D --> H["Promote to Skill"]
  D --> I["Extract Factor"]
  D --> J["Keep as Habit"]
  D --> K["Fix Environment"]
  D --> L["Reject Pattern"]
  D --> M["Open Case"]
```

核心对象：

| Object | 含义 | 默认边界 |
| --- | --- | --- |
| Session | 一次真实 Agent 执行 | 原始材料默认本地保存 |
| Evidence | 支撑判断的最小证据 | 必须可追溯、可脱敏 |
| Case | 等待审判的 session-derived finding | 不是任意观点 |
| Verdict | 对 Case 或 Candidate 的裁决 | 必须绑定证据和下一步动作 |
| Artifact | Verdict 落成的资产 | Skill、Factor、Habit、Environment Rule、Accepted Case、Rejected Pattern |
| Library | 被接受的可复用公共资产库 | 需要索引、生命周期、淘汰路径 |

## 4. Global Repo Topology

```mermaid
flowchart TB
  Mega["EvoZeus-MegaRepo<br/>全局索引、决策、跨 repo 设计"] --> Main["EvoZeus<br/>protocol / docs / schemas / governance"]
  Mega --> Community["EvoZeus-community<br/>官网 / 社区入口 / 展示层"]
  Mega --> Lab["evozeus-factor-lab<br/>社区 Factor 和 scanner 投稿孵化"]
  Mega --> Official["evozeus-factors-official<br/>官方 Factor packs / releases"]
  Mega --> Runtime["evozeus-runtime<br/>future CLI / TUI / local registry / report generation"]

  Lab --> Official
  Official --> Main
  Main --> Runtime
  Main --> Community
```

### 4.1 EvoZeus Repo 体系设计图

```mermaid
C4Container
  title EvoZeus Repo 体系设计图

  Person(user, "Agent User", "使用 zero-install entry 和未来 runtime 的用户")
  Person(contributor, "Contributor / Maintainer", "提交 evidence、Factor、scanner 或治理变更")
  System_Ext(github, "GitHub / MetaInFLow", "Repo hosting、PR review、release 和权限管理")

  System_Boundary(evozeusSystem, "EvoZeus Repo System") {
    Container(mega, "EvoZeus-MegaRepo", "Git mega workspace", "全局索引、跨 repo 决策、资料和设计入口")
    Container(main, "EvoZeus", "Protocol repo", "SKILL.md、docs、schemas、governance 和 main registry")
    Container(community, "EvoZeus-community", "Frontend repo", "官网、社区解释层和 public docs surface")
    Container(lab, "evozeus-factor-lab", "Factor lab repo", "submissions、reviewed、rejected 和 templates")
    Container(official, "evozeus-factors-official", "Official pack repo", "official packs、release manifests、checksums 和 attestations")
    Container(runtime, "evozeus-runtime", "Future runtime repo", "CLI/TUI、local registry、reports 和 selective install")
  }

  Rel(user, community, "读取产品和社区入口", "HTTPS")
  Rel(user, main, "启动 zero-install judgment", "SKILL.md")
  Rel(user, runtime, "未来选择性安装 Factors", "CLI/TUI")
  Rel(contributor, lab, "提交 evidence-backed candidates", "Issue/PR")
  Rel(lab, official, "promotion reviewed candidates", "Promotion PR")
  Rel(official, main, "发布 release manifest 引用", "Registry PR")
  Rel(main, runtime, "定义 protocol、schemas 和 trust policy", "Git tag / schema")
  Rel(main, community, "提供 canonical docs 和 positioning", "Docs / content")
  Rel(mega, main, "submodule 管理", "Git")
  Rel(mega, community, "submodule 管理", "Git")
  Rel(mega, lab, "submodule 管理", "Git")
  Rel(mega, official, "submodule 管理", "Git")
  Rel(mega, runtime, "submodule 管理", "Git")
  Rel(main, github, "review governance changes", "PR")
  Rel(official, github, "发布 tagged releases", "GitHub Release")
```

Repo 职责：

| Repo | 职责 | 当前状态 |
| --- | --- | --- |
| `EvoZeus-MegaRepo` | 全局工作区、跨 repo 决策、资料索引、repo 拓扑 | active / remote 已创建 |
| `EvoZeus` | 核心 protocol、`SKILL.md`、docs、schemas、governance gates | active |
| `EvoZeus-community` | 官网、社区解释层、未来 public docs surface | active / 已接入 |
| `evozeus-factor-lab` | 社区 Factor / scanner module 投稿、reviewed/rejected 记录 | active shell / 已接入 |
| `evozeus-factors-official` | maintainer-promoted official Factor packs、GitHub Releases | active shell / 已接入 |
| `evozeus-runtime` | 未来 CLI/TUI/browser companion/local registry | active shell / 已接入，产品能力仍为 future |

### 4.2 Repo 可见性和权限模型

设计原则：

- `EvoZeus` 的协议、`SKILL.md`、公开 docs 和 schema 应保持 public，作为社区可信入口。
- 含全局决策、私有资料、未发布路线图、商业上下文和跨 repo 工作记录的空间默认 private。
- 未来会被用户安装或审计的 runtime、official Factor packs，应在安全边界稳定后转 public。
- 所有 public artifact 必须先通过 redaction、secret scan、license check 和 maintainer review。
- visibility change 只能由 `evozeus-owners` 执行，并必须写入 `decision-log.md`。

当前组织事实：

- MetaInFlow 组织当前已有团队：`0812team`，权限语义为 `pull/read`。
- `0812team` 只能作为内部只读团队使用，不承载 Admin、Maintain、Write 权限。
- 高权限需要新增专门的 EvoZeus teams，避免把其它项目的默认团队权限混进 EvoZeus 治理。

目标团队：

| Team | GitHub 权限定位 | 成员范围 | 用途 |
| --- | --- | --- | --- |
| `evozeus-owners` | Admin | 组织 owner、EvoZeus DRI | repo settings、visibility、secrets、branch protection、release override |
| `evozeus-maintainers` | Maintain | 核心 maintainer | 日常治理、label、branch policy、release 协调，不默认管理 org-level secrets |
| `evozeus-protocol-maintainers` | Write / CODEOWNERS review | protocol / schema / governance 负责人 | `EvoZeus` 主 repo 的协议、docs、schema、registry review |
| `evozeus-community-maintainers` | Write | 官网和内容维护者 | `EvoZeus-community` 的页面、内容、部署变更 |
| `evozeus-factor-reviewers` | Triage / Write by phase | Factor reviewer | lab issue triage、candidate review、reviewed/rejected 记录 |
| `evozeus-security-reviewers` | Maintain 或 required reviewer | 安全、供应链、runtime reviewer | scanner module、official pack、runtime 权限和上传链路 review |
| `evozeus-runtime-maintainers` | Write | runtime 负责人 | future CLI/TUI/local registry/report 代码维护 |
| `metainflow-internal-read` 或 `0812team` | Read | 内部观察者、协作者 | private repo 只读访问，不参与 merge 或 settings |

每个 repo 的目标可见性：

| Repo | 当前可见性 | 目标可见性 | 理由 | Public gate |
| --- | --- | --- | --- | --- |
| `EvoZeus-MegaRepo` | private | private | 含全局设计、私有资料索引、路线图、跨 repo 决策和 submodule 工作面 | 不公开；如需对外同步，只摘录到 public docs |
| `EvoZeus` | public | public | EvoZeus 的可信入口；协议、zero-install `SKILL.md`、schema 和 governance 需要可审计 | 已 public；持续执行 secret scan 和 CODEOWNERS |
| `EvoZeus-community` | private | launch 后 public | 官网和社区解释层最终应公开，但 launch 前可能含品牌草稿、未发布内容和部署实验 | 内容定稿、无 secrets、部署配置隔离、public docs review |
| `evozeus-factor-lab` | private | gate 完成后 public 或 invite-only public | 社区投稿入口最终需要透明，但早期缺 schema/template/CI gate，直接公开会放大审核和安全成本 | schema、PR template、secret/license scan、scanner sandbox policy、moderation rules |
| `evozeus-factors-official` | private | 首个 stable pack 前转 public | official packs、checksums、SBOM、attestation 必须可被用户审计和安装 | 至少 1 个 reviewed candidate、tagged release flow、checksums、SBOM、attestation、registry PR 流程 |
| `evozeus-runtime` | private | alpha/beta 后 public | runtime 会执行本地扫描、安装和报告生成，公开源码有助于建立信任；边界未稳前先 private | trust policy、permission model、scanner sandbox、upload-off-by-default、installer lockfile |

每个 repo 的权限分配：

| Repo | Admin | Maintain | Write | Triage / Read | 特殊规则 |
| --- | --- | --- | --- | --- | --- |
| `EvoZeus-MegaRepo` | `evozeus-owners` | `evozeus-maintainers` | 不默认开放 | `metainflow-internal-read` / `0812team` read | main protected；submodule 指针变化必须说明影响；不得存 raw private session |
| `EvoZeus` | `evozeus-owners` | `evozeus-maintainers` | `evozeus-protocol-maintainers` | public read；外部贡献走 fork PR | `SKILL.md`、`schemas/`、`docs/reference/`、governance 变更需 CODEOWNERS review |
| `EvoZeus-community` | `evozeus-owners` | `evozeus-maintainers` | `evozeus-community-maintainers` | `metainflow-internal-read` / `0812team` read；public 后开放 public read | 部署 secrets 只能在 GitHub Environments / Vercel 中管理；content launch 前 owner review |
| `evozeus-factor-lab` | `evozeus-owners` | `evozeus-maintainers` | `evozeus-factor-reviewers` | early phase read: internal only；public phase: public issue/PR | scanner code 不能只由 factor reviewer 合并，必须 security review |
| `evozeus-factors-official` | `evozeus-owners` | `evozeus-maintainers` + `evozeus-security-reviewers` | 少量 release operator | read 随 visibility；public 后开放 public read | release 只能来自 reviewed candidate；tag、manifest、checksum、SBOM 必须一致 |
| `evozeus-runtime` | `evozeus-owners` | `evozeus-maintainers` + `evozeus-security-reviewers` | `evozeus-runtime-maintainers` | `metainflow-internal-read` / `0812team` read；public 后开放 public read | 涉及扫描、上传、联网、执行插件的变更必须 security review |

Branch protection baseline：

| Repo 类型 | Required reviews | Required checks | 其它保护 |
| --- | --- | --- | --- |
| mega repo | 1 maintainer review | markdown / link check 可后补 | 禁止 force push；submodule pointer 变化必须在 PR 描述中说明 |
| protocol repo | 2 reviews；高风险路径必须 CODEOWNERS | schema validate、docs checks、secret scan | 禁止 direct push to main；require conversation resolution |
| community frontend | 1 review；launch 内容需 owner review | build、test、lint、secret scan | preview deployment 必须与 PR 绑定 |
| factor lab | 1 factor review；scanner code 追加 1 security review | schema、privacy、secret、license、scanner static checks | 投稿默认不能直接进入 official 或 registry |
| official packs | 2 reviews；至少 1 security reviewer | manifest validate、checksum verify、SBOM/attestation check | release 必须绑定 tag；禁止从 moving branch 发布 |
| runtime | 2 reviews；权限/上传/扫描路径必须 security review | build、test、sandbox tests、secret scan、dependency audit | 默认 local-first；上传和联网必须 opt-in |

权限授予流程：

1. 先判断身份类型：owner、core maintainer、repo maintainer、reviewer、internal observer、external contributor。
2. 优先加 team，不直接给个人 repo 权限；临时协作必须有到期时间。
3. 只给完成任务所需的最低权限：Read < Triage < Write < Maintain < Admin。
4. Admin 只给 `evozeus-owners`；任何 visibility、secret、branch protection 变更都需要 owner 确认。
5. 外部贡献默认通过 public repo fork PR；private repo 外部协作使用临时 read/write 并定期回收。
6. 每月审计 Write 及以上权限；每次人员离开项目时立即移除 team，并轮换相关 secrets。

建议执行顺序：

1. 新建 `evozeus-owners`、`evozeus-maintainers`、`evozeus-protocol-maintainers`、`evozeus-community-maintainers`、`evozeus-factor-reviewers`、`evozeus-security-reviewers`、`evozeus-runtime-maintainers`。
2. 保留 `0812team` 为 read-only，不授予 Write 及以上权限。
3. 先对 private repo 设置 team read / write / maintain，再补 main branch protection。
4. 等 public gate 满足后，按顺序公开 `EvoZeus-community`、`evozeus-factor-lab`、`evozeus-factors-official`、`evozeus-runtime`。
5. 每次公开前新增一条 `decision-log.md` 记录，并在对应 repo 内补 `SECURITY.md`、`CONTRIBUTING.md`、CODEOWNERS 和 secret scan。

## 5. User Paths

### 5.1 Judge One Session

```text
User copies entry prompt
-> Agent reads SKILL.md
-> Collects local evidence
-> Outputs Session Verdict Card
-> User decides whether to preserve or contribute
```

原则：

- 第一次使用不安装依赖。
- 不上传 raw session。
- 先输出 Verdict Card，不默认写文件或发 GitHub。

### 5.2 Contribute a Case or Candidate

```text
Local Evidence Report
-> redaction
-> Candidate / Case draft
-> user approval
-> issue or PR
-> dry-run governance gates
-> maintainer review
```

社区贡献优先是 evidence contribution，不是随意改 runtime、workflow 或 agent instructions。

### 5.3 Install Selected Factors

```text
main registry
-> release manifest
-> select factor / bundle / pack
-> checksum verification
-> local lockfile
-> runtime executes by declared permissions
```

用户应该能只安装少数 Factors，而不是 clone 全量 Factor library。

## 6. Factor Registry Design

Factor 生态采用 manifest-driven selective install。

主规则：

```text
lab merge != official release != main registry publication
```

分层：

| Layer | 负责什么 | 默认信任 |
| --- | --- | --- |
| Main registry | 收录已审核 release manifest 引用 | stable only |
| Factor lab repo | 社区投稿、自动门禁、reviewed/rejected 记录 | explicit install only |
| Official pack repo | official packs、release assets、checksums、SBOM、attestation | registry approved |
| Third-party pack | 社区自托管 pack | community opt-in |

主 registry 不抓 lab repo 的 moving branch。它只接受：

- allowlisted repo
- Git tag 或 commit SHA
- release manifest
- checksum
- channel
- review state
- optional artifact attestation

## 7. Community Upload to Launch Flow

```mermaid
flowchart LR
  A["Contributor"] --> B["Issue / Discussion<br/>problem, evidence, scenario"]
  B --> C["PR to factor lab<br/>submissions/author/factor-id"]
  C --> D["Automated gates<br/>schema / privacy / secret / license"]
  D --> E{"Contains scanner code?"}

  E -- "No" --> F["Factor Review<br/>semantics, evidence, reuse"]
  E -- "Yes" --> G["Security CI<br/>lockfile, static analysis, sandbox, determinism"]
  G --> H["Security Review<br/>permissions, deps, outputs"]

  F --> I{"Approved?"}
  H --> I

  I -- "No" --> J["Rejected Record<br/>negative pattern or revision request"]
  I -- "Yes" --> K["Reviewed Candidate<br/>explicit install only"]

  K --> L["Promotion PR<br/>official Factor pack repo"]
  L --> M["Official CI<br/>manifest, hashes, compatibility"]
  M --> N["CODEOWNERS + Maintainer Approval"]
  N --> O["GitHub Release<br/>index, checksums, SBOM, attestation"]
  O --> P["Registry PR<br/>EvoZeus main registry"]
  P --> Q["Registry Published<br/>stable channel"]
  Q --> R["User selective install<br/>lockfile"]
```

`factor.yaml` 和 scanner module 分开治理：

- `factor.yaml` 重点审核语义、证据、触发条件、反例和隐私。
- scanner module 是可执行插件，必须审核权限、依赖、沙箱、确定性和供应链。

## 8. Governance Defaults

EvoZeus 的治理原则：

- One PR, one primary layer, one review target.
- High-risk paths require owner / maintainer review.
- GitHub automation dry-run by default：label、comment、status 可以，approve、merge、promote、auto-close 不可以。
- Public artifact 必须脱敏，不依赖 raw private session 才能理解。
- Rejected contribution 也有价值，应沉淀为 negative pattern 或 rejected record。

高风险面：

- `SKILL.md`
- `skills/`
- `.github/workflows/`
- `schemas/`
- `docs/reference/ontology.md`
- `docs/reference/evidence-grading.md`
- privacy / redaction rules
- future `factors/registry/`
- official Factor pack manifests
- scanner modules
- runtime upload / extraction code

## 9. Roadmap

### Now

- 保持 `EvoZeus` 主仓库小而清晰。
- 合并 Factor registry ADR 和 governance。
- 在 mega repo 维护跨 repo 拓扑和决策记录。
- 所有核心 repo 已建仓并作为 submodule 接入 mega repo。
- 暂不公开开放 lab repo 投稿。

### Next

- 在主仓库补最小 schema：
  - `factor.schema.json`
  - `factor-pack.schema.json`
  - `scanner-manifest.schema.json`
- 补主 registry 示例：
  - `factors/registry/index.example.json`
- 补 registry / manifest 校验脚本。
- 设计 lab repo PR template 和 CI gate。

### Then

- 启用 `evozeus-factor-lab` 投稿流程。
- 接收少量内部/邀请制 Factor 投稿。
- 形成 reviewed/rejected 记录。
- 有 1-3 个 reviewed candidates 后启用 `evozeus-factors-official` release 流程。

### Later

- 实现 local runtime：
  - `.evozeus/` local registry
  - Markdown/JSON report
  - selective Factor install
  - scanner sandbox
  - lockfile
- 再评估 CLI/TUI/browser companion/cloud 是否拆 repo。

## 10. Open Decisions

| Decision | Current bias | Blocker |
| --- | --- | --- |
| lab repo 是否立即公开投稿 | 先 private 或邀请制 | schema、template、CI gate 未补齐 |
| official Factor pack repo 何时启用 release 流程 | 有 reviewed candidates 后启用 | 需要真实候选资产 |
| runtime 何时从 shell repo 进入正式开发 | 暂不实现稳定 runtime | CLI/TUI 边界未稳定 |
| Factor pack 是否支持第三方 registry | 支持，但默认不显示 | installer 和 trust policy 未实现 |
| scanner 是否允许联网 | 默认不允许 | 需要明确权限模型和安全 review |

## 11. Source Links

当前本地来源：

- `10-repos/evozeus/SKILL.md`
- `10-repos/evozeus/docs/design/active/design_doc-v0.1-agent-session-judgment-layer.md`
- `10-repos/evozeus/docs/decisions/ADR-0001-static-skill-entry-and-zero-install.md`

待主 repo 分支合并后同步的来源：

- `docs/decisions/ADR-0002-factor-pack-registry-and-community-promotion.md`
- `docs/governance/factor-registry-governance.md`
