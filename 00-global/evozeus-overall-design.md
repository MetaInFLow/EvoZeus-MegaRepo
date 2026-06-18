# EvoZeus 整体设计

- Status: active
- Last updated: 2026-06-18
- Scope: EvoZeus 全局产品、repo 拓扑、贡献治理、Factor registry、未来 runtime
- Owner: MetaInFlow

本文是 EvoZeus mega repo 的全局设计入口。它不替代 `10-repos/evozeus` 中的协议、schema、技能和治理细节，而是说明多个 repo 如何协同承载 EvoZeus。

Repo 命名、目录结构和 future runtime / skill / factor 文件组织，见 `repo-structure-naming.md`。

## 1. One-line Definition

EvoZeus（宙斯）是 Agent Session Judgment Layer：把真实 Agent Session 放上审判台，什么该沉淀，什么该修正，什么该淘汰，由证据决定。

EvoZeus 不做 agent score，不把 Skill creation 当作唯一目标。它管理：

```text
Session -> Evidence -> Case -> Verdict -> Artifact -> Library
```

## 2. Product Boundary

EvoZeus 当前首先是 agent-readable protocol repo，不是稳定 CLI 产品。主 repo 采用 **Protocol-only** 职责边界：它拥有判断协议、治理流程、公共入口和 registry pointer，不拥有 runtime 执行层。

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

主 repo 不拥有：

- scanner implementation。
- runtime CLI / TUI / companion / local API。
- installable Factor pack 或 scanner pack。
- `.evozeus/` local state、lockfile、SQLite ledger、report execution。
- runtime upload、联网、插件执行或 sandbox 实现。

现有 `10-repos/evozeus/__infra__` 只作为待迁移 prototype / reference material，不是主 repo 目标职责。迁移完成前，它不应成为默认用户入口、安装源或 official runtime contract。

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
  Mega["EvoZeus-MegaRepo<br/>全局索引、决策、跨 repo 设计"] --> Main["EvoZeus<br/>protocol / governance / intake / registry pointer"]
  Mega --> Community["EvoZeus-community<br/>官网 / 社区入口 / 展示层"]
  Mega --> Lab["evozeus-factor-lab<br/>社区 Factor 和 scanner 投稿孵化"]
  Mega --> Official["evozeus-factors-official<br/>官方 Factor packs / releases"]
  Mega --> Runtime["evozeus-runtime<br/>runtime implementation / CLI / TUI / local registry"]

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
    Container(main, "EvoZeus", "Protocol-only repo", "SKILL.md、docs、schemas、governance、Case/Candidate intake 和 registry pointer")
    Container(community, "EvoZeus-community", "Private frontend source repo", "官网源码、社区解释层和 public deployed surface")
    Container(lab, "evozeus-factor-lab", "Factor lab repo", "submissions、reviewed、rejected 和 templates")
    Container(official, "evozeus-factors-official", "Official pack repo", "official packs、release manifests、checksums 和 attestations")
    Container(runtime, "evozeus-runtime", "Runtime repo", "CLI/TUI、local registry、reports、scanner execution 和 selective install")
  }

  Rel(user, community, "读取产品和社区入口", "HTTPS")
  Rel(user, main, "启动 zero-install judgment", "SKILL.md")
  Rel(user, runtime, "未来选择性安装 Factors", "CLI/TUI")
  Rel(contributor, lab, "提交 evidence-backed candidates", "Issue/PR")
  Rel(lab, official, "promotion reviewed candidates", "Promotion PR")
  Rel(official, main, "发布 release manifest 引用", "Registry PR")
  Rel(main, runtime, "提供 protocol、schemas、registry pointer 和 trust policy", "Git tag / schema")
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
| `EvoZeus` | Protocol-only 主 repo：`SKILL.md`、docs、schemas、governance gates、Case/Candidate intake、semantic artifact、registry pointer | active；`__infra__` 为待迁移 prototype |
| `EvoZeus-community` | private Web 源码、官网部署面、社区解释层 | active / 已接入 |
| `evozeus-factor-lab` | 社区 Factor / scanner module 投稿、reviewed/rejected 记录 | active shell / 已接入 |
| `evozeus-factors-official` | maintainer-promoted official Factor packs、GitHub Releases | active shell / 已接入 |
| `evozeus-runtime` | CLI/TUI/browser companion/local registry、scanner execution、report generation、selective install | active shell / 已接入，产品能力仍为 future |

### 4.2 EvoZeus 主 Repo 生命周期边界

Protocol-only 设计按资产生命周期拆分所有权：

```text
Session
  -> Evidence
  -> Case / Candidate
  -> Reviewed Semantic Artifact
  -> Lab Pack / Scanner
  -> Official Release
  -> Registry Pointer
  -> Runtime Install / Execution
  -> Feedback Case
```

| 阶段 | 关键问题 | 所属位置 | `EvoZeus` 主 repo 是否拥有 |
| --- | --- | --- | --- |
| Session | 原始 agent 执行发生了什么 | 用户本地 | 不拥有 raw session，只定义如何取证和脱敏 |
| Evidence | 证据是否可追溯、可复核、可脱敏 | 用户本地 + `EvoZeus` protocol | 拥有 evidence contract 和 redaction policy |
| Case / Candidate | 发现是否值得审查 | `EvoZeus` issue / PR / candidates | 拥有正式 intake 和 review lifecycle |
| Reviewed Semantic Artifact | 是否形成稳定规则、Factor proposal、Skill proposal、Pattern | `EvoZeus` docs / candidates / registry surface | 拥有 semantic artifact 和治理状态 |
| Lab Pack / Scanner | 是否需要代码、scanner、依赖和权限审查 | `evozeus-factor-lab` | 不拥有，只负责 route 和引用 |
| Official Release | 是否可被用户或 runtime 可信消费 | `evozeus-factors-official` | 不发布，只接收 release metadata pointer |
| Registry Pointer | 哪个 release 是 canonical、可引用、可撤回 | `EvoZeus` future registry | 拥有 stable pointer，不拥有 artifact 本体 |
| Runtime Install / Execution | 如何安装、运行、回滚、生成 report | `evozeus-runtime` | 不拥有执行层，只定义 contract |
| Feedback Case | runtime 运行后发现的新问题如何回流 | `EvoZeus` issue / Candidate | 拥有回流入口 |

主 repo 的目标职责是“判定和治理资产是否可信”，不是“执行资产”。一旦某个对象需要运行代码、读取本地文件、维护 local state、安装 pack、生成 report 或暴露 local API，它就越过了 `EvoZeus` 主 repo 边界，应进入 `evozeus-runtime` 或 Factor lifecycle repo。

### 4.3 用户旅程：从注册到组件拼接

EvoZeus 的用户旅程不是“下载一个全量工具箱”，而是“先获得 skeleton，再按需拼接组件”。

```text
Community / #register
  -> copy Start Here
  -> Agent reads EvoZeus SKILL.md
  -> EvoZeus skeleton activates
  -> user approves runtime path
  -> runtime installs / enables default official factors
  -> local judgment run
  -> judgment / Session Verdict Card
  -> user approves preservation
  -> contribution or development route
```

| 步骤 | 用户看到什么 | 系统拥有者 | Skill / route |
| --- | --- | --- | --- |
| Register | 官网注册入口、Start Here command | `EvoZeus-community` deployed surface | community page routes to public `EvoZeus` |
| Start Here | 一段可复制 prompt | `EvoZeus` 主 repo | root `SKILL.md` |
| Skeleton activation | protocol、ontology、evidence、verdict、privacy gate | `EvoZeus` 主 repo | root `SKILL.md` + `skills/index/SKILL.md` |
| Runtime approval | 是否启用本地执行、扫描、report generation | `evozeus-runtime` | `skills/evozeus-runtime/SKILL.md` routes implementation to runtime repo |
| Default official factors | 选择默认 official factor set | `EvoZeus` registry pointer + `evozeus-factors-official` release | manifest / checksum / attestation gate |
| Local judgment | 本地扫描 session、运行 factors、生成 report | `evozeus-runtime` | runtime permission model |
| Judgment result | Session Verdict Card / Evidence Report / proposed Case | `EvoZeus` protocol | `skills/evozeus-reporting/SKILL.md` |
| User-approved preservation | 用户确认是否沉淀、公开、开 issue/PR | user approval gate | `skills/evozeus-redaction/SKILL.md` + contribution route |
| Case / Candidate preservation | 普通 Case、semantic Factor proposal、Pattern、Habit | `EvoZeus` 主 repo | `skills/evozeus-community-contribution/SKILL.md` |
| Executable Factor / scanner | 需要代码、依赖、权限、sandbox 的组件 | `evozeus-factor-lab` | lab templates / checks |
| Official pack promotion | 通过 lab review 的组件发布 | `evozeus-factors-official` | release manifest / checksum / attestation |
| Runtime / infra development | CLI、TUI、companion、scanner execution、local state | `evozeus-runtime` | runtime PR，不进主 repo |

关键原则：

- Start Here 默认只激活 skeleton，不静默安装 runtime 或 factors。
- runtime 和 default official factors 可以是推荐路径，但必须有用户确认、manifest 可见、checksum/attestation 可复核。
- judgment 的沉淀按对象分流：普通 Case/Candidate 回主 repo；可执行 Factor/scanner 进 lab；official pack 进 official；runtime/infra 改动进 runtime。
- `EvoZeus` 主 repo 对组件只做标准、路由和 pointer，不承接组件实现。

### 4.4 社区共创机制

EvoZeus 的社区共创不是先给社区 repo write 权限，而是把真实 session 观察逐层变成可审查资产。

当前机制已经在 `EvoZeus` 主 repo 内成型：

- `CONTRIBUTING.md`：贡献以 Case 为中心，必须有 evidence、privacy note 和 proposed verdict。
- Issue templates：`case`、`candidate_suggestion`、`factor`、`governance_rfc` 分开收口。
- PR templates：Candidate、code、schema、skill instruction、governance、docs/example 分开审查。
- Candidate lifecycle：`community -> reviewed -> core -> deprecated`。
- PR routing：`review / needs-info / needs-redaction / convert-to-rfc / owner-only / close`。
- Automation：dry-run label/comment/status only，不 approve、不 merge、不 promotion。
- Discord / OpenClaw 融入方案：Discord 是 PR 前缓冲层，不替代 GitHub 治理。

共创漏斗：

```mermaid
flowchart LR
  A["Discord thread<br/>case / candidate / proof / redaction / rfc"] --> B{"Maintainer triage"}
  B --> C["Stay in Discord<br/>question / proof / redaction"]
  B --> D["GitHub Issue<br/>Case / Candidate suggestion / Factor proposal / RFC"]
  D --> E["Candidate PR<br/>redacted evidence + schema"]
  E --> F["EvoZeus main repo<br/>candidates/community"]
  F --> G["maintainer review<br/>evidence / privacy / value / operation"]
  G --> H["candidates/reviewed"]
  H --> I["candidates/core<br/>canonical reusable assets"]
  G --> J["candidate:rejected<br/>negative pattern / revision"]

  H --> K{"Needs executable Factor pack<br/>or scanner module?"}
  K -- "No" --> I
  K -- "Yes" --> L["evozeus-factor-lab<br/>submissions / reviewed / rejected"]
  L --> M["evozeus-factors-official<br/>tagged release + manifest + checksum"]
  M --> N["EvoZeus main registry<br/>stable manifest reference"]
  N --> O["evozeus-runtime<br/>selective install"]
```

关键边界：

- Discord 只做讨论、证据补齐、脱敏帮助和 PR 前分流。
- `EvoZeus` public 主 repo 是正式社区入口和 canonical governance surface。
- 普通 Case、Candidate、Pattern、docs/example 贡献不需要进入 `evozeus-factor-lab`。
- `evozeus-factor-lab` 只承接更重的孵化对象：Factor pack、scanner module、需要 reviewed/rejected 记录的实验性资产。
- `evozeus-factors-official` 只承接 maintainer-promoted official pack release。
- `evozeus-runtime` 只消费 registry 和 release manifest，不直接消费 Discord thread 或 lab moving branch。
- `EvoZeus` 主 repo 只 route、review、publish pointer，不运行 scanner、pack 或 runtime。
- raw private session、客户资料、secret、内部路径、未脱敏日志不进入任何 public repo。

### 4.5 Factor Repo 拆分设计

主 repo 里原有 `factors/` 表达的是公共语义和贡献入口，不应继续承担完整 Factor library、scanner module 或 official pack 发布职责。

拆分后的职责：

| 层级 | Repo / 路径 | 职责 | 不做什么 |
| --- | --- | --- | --- |
| Public intake | `EvoZeus` issue / Candidate PR | 接收 Factor Candidate、evidence、counterexample、review target | 不接收 raw session、scanner code、未审 pack |
| Registry surface | `EvoZeus/factors/` 和未来 main registry | 保存 Factor 语义说明、stable pointer、official manifest reference | 不追踪 lab branch，不作为安装源 |
| Incubation | `evozeus-factor-lab` | 承接 Factor pack、scanner module、reviewed/rejected、domain、template、schema、checks | 不发布 official pack，不替代主 repo intake |
| Official release | `evozeus-factors-official` | 发布 maintainer-promoted packs、manifest、checksum、SBOM/attestation | 不接收未经 lab review 的普通投稿 |
| Runtime consumption | `evozeus-runtime` | 未来选择性安装和执行 official pack | 不直接消费 Discord thread 或 lab moving branch |

拆分后的资产流：

```mermaid
flowchart LR
  A["Factor proposal<br/>EvoZeus issue / Candidate PR"] --> B{"Maintainer route"}
  B --> C["Semantic-only Factor<br/>EvoZeus registry pointer"]
  B --> D["Pack / scanner candidate<br/>evozeus-factor-lab/submissions"]
  D --> E["reviewed / rejected<br/>lab record"]
  E --> F["promotion PR<br/>evozeus-factors-official"]
  F --> G["tagged release<br/>manifest + checksum + attestation"]
  G --> H["EvoZeus main registry<br/>stable manifest reference"]
  H --> I["evozeus-runtime<br/>selective install"]
```

这个设计保留主 repo 作为社区共创正式入口，同时避免把未审可执行代码、供应链风险和 official release 责任混进 public protocol repo。

### 4.6 Repo 可见性和权限模型

设计原则：

- Web 源码默认 private；公开的是部署后的用户入口、`/skill`、公开文档和贡献路线。
- public 面优先承载共创入口、审查材料和任何用户 / agent 可直接访问、拉取、投稿或审计的资产。
- private 面只承载内部协调、未脱敏材料、未发布战略、部署 secret、安全敏感开发和 Web 实现源码。
- 权限授予围绕“分流、评审、合并、发布”四种动作拆开，不把社区共创误解成 repo write 权限。
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
| `evozeus-triagers` | Triage | Discord / issue 分流者 | issue 分类、label、needs-proof、needs-redaction、route-to-rfc，不 merge |
| `evozeus-protocol-maintainers` | Write / CODEOWNERS review | protocol / schema / governance 负责人 | `EvoZeus` 主 repo 的协议、docs、schema、registry review |
| `evozeus-community-maintainers` | Write | 官网和内容维护者 | `EvoZeus-community` 的页面、内容、部署变更 |
| `evozeus-factor-maintainers` | Write / CODEOWNERS review | Factor reviewer | `EvoZeus` candidate review、`evozeus-factor-lab` submissions/reviewed/rejected 维护 |
| `evozeus-security-reviewers` | Maintain 或 required reviewer | 安全、供应链、runtime reviewer | scanner module、official pack、runtime 权限、上传和联网链路 review |
| `evozeus-runtime-maintainers` | Write | runtime 负责人 | future CLI/TUI/local registry/report 代码维护 |
| `metainflow-internal-read` 或 `0812team` | Read | 内部观察者、协作者 | private repo 只读访问，不参与 merge 或 settings |

每个 repo 的目标可见性：

| Repo | 当前可见性 | 目标可见性 | 共创角色 | Public gate |
| --- | --- | --- | --- | --- |
| `EvoZeus-MegaRepo` | private | private | 内部协调层，不是社区入口 | 不公开；对外只摘录成熟决策到 public docs |
| `EvoZeus` | public | public | 正式社区入口、Case/Candidate/Factor/RFC intake、canonical governance | 已 public；持续执行 privacy、proof、schema、CODEOWNERS gates |
| `EvoZeus-community` | private | private source / public deployed surface | 官网、Discord 入口、贡献路线说明、`/skill` 部署面 | 源码不公开；部署面公开；无 secret、部署配置隔离、基础内容定稿、链接到主 repo issue/PR 路线 |
| `evozeus-factor-lab` | private | public before user contribution / PR-gated | Factor pack、scanner module、实验性 reviewed/rejected 孵化，不是普通 Case 入口 | 用户可访问或投稿前完成 README、submission template、redaction rule、scanner permission policy、secret/license scan |
| `evozeus-factors-official` | private | public before first user-consumable release | official pack 发布源，用户必须能审计 release assets | reviewed candidate、tagged release flow、manifest、checksum、SBOM/attestation、registry PR 流程 |
| `evozeus-runtime` | private | public before user-installable runtime | 可执行 runtime，用户安装前必须可审计；早期 private 避免未稳 API 被误用 | permission model、upload-off-by-default、scanner sandbox、lockfile、dependency audit |

每个 repo 的权限分配：

| Repo | Admin | Maintain | Write | Triage / Read | 特殊规则 |
| --- | --- | --- | --- | --- | --- |
| `EvoZeus-MegaRepo` | `evozeus-owners` | `evozeus-maintainers` | 不默认开放 | `metainflow-internal-read` / `0812team` read | 不存 raw private session；submodule 指针变化必须说明影响 |
| `EvoZeus` | `evozeus-owners` | `evozeus-maintainers` | `evozeus-protocol-maintainers` + `evozeus-factor-maintainers` | public read；`evozeus-triagers` triage；外部贡献走 issue/fork PR | 这是社区共创主入口；高风险路径需 CODEOWNERS；triager 不 merge |
| `EvoZeus-community` | `evozeus-owners` | `evozeus-maintainers` | `evozeus-community-maintainers` | private source read by approved internal teams only；public users access deployed site | 只指向贡献路线，不收 raw evidence；部署 secrets 只在 GitHub Environments / Vercel 管理 |
| `evozeus-factor-lab` | `evozeus-owners` | `evozeus-maintainers` | `evozeus-factor-maintainers` | public 后 public read/PR；`evozeus-triagers` triage | lab merge 不等于 official release；scanner code 必须 security review |
| `evozeus-factors-official` | `evozeus-owners` | `evozeus-maintainers` + `evozeus-security-reviewers` | 少量 release operator | public 后 public read | 只接 promotion PR；tag、manifest、checksum、SBOM 必须一致 |
| `evozeus-runtime` | `evozeus-owners` | `evozeus-maintainers` + `evozeus-security-reviewers` | `evozeus-runtime-maintainers` | public 后 public read；internal phase 由 `0812team` read | 用户可安装前必须 public；扫描、上传、联网、插件执行必须 security review |

Branch protection baseline：

| Repo 类型 | Required reviews | Required checks | 其它保护 |
| --- | --- | --- | --- |
| mega repo | 1 maintainer review | markdown / link check 可后补 | 禁止 force push；submodule pointer 变化必须在 PR 描述中说明 |
| public intake / protocol repo | 2 reviews；高风险路径必须 CODEOWNERS | schema validate、proof gate、privacy scan、dirty PR check、queue guard、secret scan | 禁止 direct push to main；require conversation resolution；first-time contributor approval |
| community frontend | 1 review；launch 内容需 owner review | build、test、lint、secret scan | preview deployment 必须与 PR 绑定；内容变更不得绕过主 repo governance |
| factor lab | 1 factor review；scanner code 追加 1 security review | schema、privacy、secret、license、scanner static checks | public-read does not mean install source；投稿默认不能进入 official 或 registry |
| official packs | 2 reviews；至少 1 security reviewer | manifest validate、checksum verify、SBOM/attestation check | release 必须绑定 tag；禁止从 moving branch 发布 |
| runtime | 2 reviews；权限/上传/扫描路径必须 security review | build、test、sandbox tests、secret scan、dependency audit | 默认 local-first；上传和联网必须 opt-in |

权限授予流程：

1. 先判断动作类型：分流、评审、合并、发布、settings 管理。
2. 优先加 team，不直接给个人 repo 权限；临时协作必须有到期时间。
3. 外部共创默认通过 Discord thread、GitHub issue、fork PR，不授予 repo write。
4. Triage 权限可以给社区维护者；Write 只给需要维护文件的人；Maintain/Admin 只给 release/settings 责任人。
5. Admin 只给 `evozeus-owners`；任何 visibility、secret、branch protection 变更都需要 owner 确认。
6. 每月审计 Write 及以上权限；每次人员离开项目时立即移除 team，并轮换相关 secrets。

建议执行顺序：

1. 新建 `evozeus-owners`、`evozeus-maintainers`、`evozeus-triagers`、`evozeus-protocol-maintainers`、`evozeus-community-maintainers`、`evozeus-factor-maintainers`、`evozeus-security-reviewers`、`evozeus-runtime-maintainers`。
2. 保留 `0812team` 为 read-only，不授予 Write 及以上权限。
3. 保持 `EvoZeus-community` 源码 private；只公开部署面、`/skill` 和路由到主 repo 的贡献入口。
4. 补齐 `evozeus-factor-lab` 的 template、redaction rule、scanner permission policy 后，在允许用户投稿前调整为 public / PR-gated。
5. 有第一个 reviewed Factor pack 后，在任何用户或 runtime 可消费 release 前，把 `evozeus-factors-official` 调整为 public，并发布 tag + manifest + checksum + SBOM。
6. `evozeus-runtime` 等 trust policy 和 permission model 稳定后，在提供用户安装入口前调整为 public。

### 4.7 Skill Repo 拆分判断

当前不单独创建 `evozeus-skills` repo。

原因：

- 现有 `skills/` 是 EvoZeus protocol surface 的一部分，不是独立内容库。
- root `SKILL.md`、`skills/index/SKILL.md`、scenario skills、ontology、evidence grading、privacy gate 和 PR routing 必须同步演进。
- `skills/` 已被主 repo 治理定义为高风险 instruction surface，变更需要 owner / CODEOWNERS review。
- 社区共创当前以 Case / Candidate / Factor / RFC 为入口，不应鼓励绕过 Candidate lifecycle 直接提交 agent instruction。
- Skill 是 Verdict 可能落成的一类 Artifact，但不是所有 contribution 的默认目标；过早拆 repo 会把 EvoZeus 拉回 prompt/skill collection。

保留在 `EvoZeus` 主 repo 的内容：

| 内容 | 原因 |
| --- | --- |
| root `SKILL.md` | zero-install canonical entry，必须跟 protocol 同步 |
| `skills/index/SKILL.md` | scenario router，依赖主 repo 的治理文档和术语 |
| `skills/evozeus-*` scenario skills | 当前是开发、贡献、redaction、runtime、reporting 等治理工作流 |
| skill proposal / skill instruction PR template | 属于 governance-risk change |

只有满足以下条件时，才考虑新建 `evozeus-skills`：

1. 出现一批已通过 `candidate -> reviewed -> core` 的 public Skills，需要独立版本和安装。
2. Skill 使用者不需要 clone 完整 `EvoZeus` protocol repo，也能按 manifest 选择安装。
3. Skill 与主 protocol 有明确 compatibility matrix，例如 `evozeus-protocol >= 0.x`。
4. Skill review queue 的流量已经影响主 repo 的 protocol / governance review。
5. 已有 skill manifest schema、validation、redaction、license、example proof 和 release gate。

如果未来拆分，建议边界是：

| Repo | 职责 |
| --- | --- |
| `EvoZeus` | 保留 root `SKILL.md`、canonical governance、ontology、schemas、candidate lifecycle、skill proposal gate |
| `evozeus-skills` | 只收已 reviewed/core 的可安装 public Skills、manifest、examples、compatibility matrix |
| `evozeus-factor-lab` | 仍只承接 Factor pack / scanner module 孵化，不承接普通 Skill 投稿 |
| `evozeus-runtime` | 未来按 manifest 选择安装 Skill / Factor，不直接消费未 reviewed 的 skill PR |

未来 `evozeus-skills` 的可见性应该是 public-read / PR-gated；但创建时机应晚于主 repo Candidate lifecycle 和 skill validation 成熟。

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
| Factor lab repo | Factor pack / scanner module 孵化、自动门禁、reviewed/rejected 记录 | explicit install only |
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
  A["Contributor"] --> B["Discord thread<br/>case / candidate / proof / redaction / rfc"]
  B --> C{"Ready for GitHub?"}
  C -- "No" --> D["Stay in Discord<br/>proof / redaction / split object"]
  C -- "Yes" --> E["EvoZeus main repo issue<br/>Case / Candidate / Factor / RFC"]
  E --> F{"Contribution kind"}

  F -- "Case / Candidate / Pattern / docs" --> G["Candidate PR to EvoZeus<br/>candidates/community"]
  G --> H["Main repo gates<br/>schema / proof / privacy / queue"]
  H --> I{"Reviewed?"}
  I -- "No" --> J["Rejected or revision requested<br/>negative pattern when useful"]
  I -- "Yes" --> K["candidates/reviewed or core<br/>canonical library asset"]

  F -- "Factor pack / scanner module" --> L["PR to factor lab<br/>submissions/author/factor-id"]
  L --> M["Lab gates<br/>schema / privacy / secret / license"]
  M --> N{"Contains scanner code?"}
  N -- "No" --> O["Factor review<br/>semantics / evidence / reuse"]
  N -- "Yes" --> P["Security review<br/>permissions / deps / sandbox / determinism"]
  O --> Q{"Approved for promotion?"}
  P --> Q
  Q -- "No" --> R["Lab rejected record<br/>revision or negative pattern"]
  Q -- "Yes" --> S["Promotion PR<br/>official Factor pack repo"]
  S --> T["Official release<br/>tag / manifest / checksum / SBOM"]
  T --> U["Registry PR<br/>EvoZeus main registry"]
  U --> V["Runtime selective install<br/>lockfile"]
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
- runtime upload / extraction code（归 `evozeus-runtime`，不归主 repo）

## 9. Roadmap

### Now

- 保持 `EvoZeus` 主仓库小而清晰。
- 确认 `EvoZeus` 主 repo 为 Protocol-only：治理、schema、intake、semantic artifact、registry pointer。
- 将 `10-repos/evozeus/__infra__` 标记为待迁移 prototype，不作为默认用户入口、安装源或 official runtime contract。
- 明确 `EvoZeus` public 主 repo 是社区共创正式入口。
- 使用 Discord 作为 PR 前缓冲层：route、proof、redaction、RFC 分流。
- 合并 Factor registry ADR 和 governance。
- 在 mega repo 维护跨 repo 拓扑和决策记录。
- 所有核心 repo 已建仓并作为 submodule 接入 mega repo。

### Next

- 保持 `EvoZeus-community` 源码 private；把公开官网部署面和 `/skill` 路由到 public `EvoZeus` 主 repo intake。
- 在主仓库补最小 schema：
  - `factor.schema.json`
  - `factor-pack.schema.json`
  - `scanner-manifest.schema.json`
- 补主 registry 示例：
  - `factors/registry/index.example.json`
- 补 registry / manifest 校验脚本。
- 设计 `evozeus-factor-lab` PR template、redaction rule、scanner permission policy 和 CI gate。

### Then

- 将 `evozeus-factor-lab` 在用户投稿前调整为 public / PR-gated。
- 接收少量 Factor pack / scanner module 投稿。
- 形成 lab reviewed/rejected 记录。
- 有 1-3 个 reviewed candidates 后启用 `evozeus-factors-official` release 流程。

### Later

- 实现 local runtime：
  - `.evozeus/` local registry
  - Markdown/JSON report
  - selective Factor install
  - scanner sandbox
  - lockfile
- 在 `evozeus-runtime` 承接 CLI/TUI/browser companion/cloud，不再把执行层放回主 repo。

## 10. Open Decisions

| Decision | Current bias | Blocker |
| --- | --- | --- |
| `EvoZeus-community` 源码是否公开 | 保持 private | Web 源码不是用户信任面；公开部署面、`/skill` 和主 repo intake 即可 |
| `evozeus-factor-lab` 何时公开 | 用户投稿前 public / PR-gated | schema、template、CI gate、scanner permission policy 未补齐 |
| official Factor pack repo 何时启用 release 流程 | 有 reviewed candidates 后启用 | 需要真实候选资产 |
| runtime 何时从 shell repo 进入正式开发 | Protocol / registry / trust policy 稳定后启动；`EvoZeus/__infra__` 只作为迁移源 | CLI/TUI 边界、permission model、scanner sandbox 未稳定 |
| Factor pack 是否支持第三方 registry | 支持，但默认不显示 | installer 和 trust policy 未实现 |
| scanner 是否允许联网 | 默认不允许 | 需要明确权限模型和安全 review |

## 11. Source Links

当前本地来源：

- `30-ops/discord-openclaw-governance-plan.md`
- `00-global/repo-structure-naming.md`
- `10-repos/evozeus/SKILL.md`
- `10-repos/evozeus/docs/design/active/design_doc-v0.1-agent-session-judgment-layer.md`
- `10-repos/evozeus/docs/decisions/ADR-0001-static-skill-entry-and-zero-install.md`

待主 repo 分支合并后同步的来源：

- `docs/decisions/ADR-0002-factor-pack-registry-and-community-promotion.md`
- `docs/governance/factor-registry-governance.md`
