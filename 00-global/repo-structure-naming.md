# EvoZeus Repo Structure And Naming

- Status: draft
- Last updated: 2026-06-19
- Source reference: `larksuite/cli` at https://github.com/larksuite/cli
- Scope: EvoZeus repo 命名、目录结构、skill/factor/runtime 文件组织

本文借鉴 `larksuite/cli` 的结构纪律，但不照搬其 Go CLI 目录。EvoZeus 主 repo 当前采用 Protocol-only 边界：首先是 protocol / governance / evidence system / registry pointer，不是成熟 CLI 产品，也不是 runtime implementation repo。

## 1. 从 larksuite/cli 借鉴什么

`larksuite/cli` 的关键结构模式：

| Pattern | 在 larksuite/cli 中的表现 | EvoZeus 借鉴方式 |
| --- | --- | --- |
| 顶层按 surface 分区 | `cmd/`、`shortcuts/`、`skills/`、`skill-template/`、`internal/`、`scripts/`、`tests/` | 不同 repo 内也按入口、资产、模板、质量门禁、测试分区 |
| 领域名稳定 | `skills/lark-doc`、`shortcuts/doc`、`tests/cli_e2e/docs` | EvoZeus 用稳定 domain：`candidate`、`factor`、`runtime`、`redaction`、`registry` |
| skill 自带上下文 | 每个 `skills/lark-*` 下可有 `references/`、`assets/`、`scripts/` | EvoZeus scenario skill 也按需要拆 `references/`，避免把长说明塞进单个 `SKILL.md` |
| template 独立 | `skill-template/`、脚本模板和 domain 模板分开 | EvoZeus 的 candidate/factor/skill templates 要单独管理，不混入 examples |
| 质量门禁独立 | `internal/qualitygate`、`scripts/skill-format-check` | EvoZeus 的 schema/proof/privacy/skill/factor checks 也应独立成 `quality-gates/` 或 `scripts/checks/` |
| agents 友好 | README、AGENTS、Skills 都强调 agent 可读输出和错误恢复 | EvoZeus 文档和 runtime 要优先保证 agent 可读、可路由、可恢复 |

不照搬的部分：

- `cmd/`、`internal/` 是 CLI/runtime 实现结构，不应提前塞进 `EvoZeus` protocol repo。
- `skills/` 在 `larksuite/cli` 中随 CLI 一起发布；EvoZeus 当前 skills 仍是 protocol/governance surface，不单独拆 repo。
- `shortcuts/` 适合成熟 CLI 的高频命令封装；EvoZeus 进入 runtime 阶段后再引入。

## 2. Repo 命名规则

GitHub repo 命名建议：

| Repo | 建议名称 | 说明 |
| --- | --- | --- |
| 主协议 repo | `EvoZeus` | 保留品牌大小写，作为 public canonical repo |
| 官网 / Web 入口源码 | `evozeus-web` | Web 源码保持 private；repo 已统一为 lower kebab-case |
| Session Signal SKILL / factor tools | `evozeus-session-signal-skill` | 已符合规则；official 指官方判断方法和 tools，不指 pack 仓库 |
| Runtime | `evozeus-infra` | 已符合规则 |
| Coordination workspace | `EvoZeus-MegaRepo` 或未来 `evozeus-workspace` | 当前可保留；若希望减少内部感，后续可改名为 `evozeus-workspace` |
| Future skill distribution | `evozeus-skills` | deferred，不创建；只在 reviewed/core Skills 需要独立安装时使用 |

命名原则：

- public satellite repo 统一 lower kebab-case：`evozeus-<surface>`；private Web source repo 也可采用同样命名以降低认知成本。
- public canonical product repo 可保留品牌名：`EvoZeus`。
- 不在 repo 名里使用 `repo`、`new`、`temp`、`v2`、`final`。
- 用单数还是复数看资产类型：
  - `session-signal-skill`：官方超级 SKILL 和一组 factor tools，复数 factors。
  - `runtime`：一个运行时产品面，单数 runtime。
  - `skills`：未来多个可安装 skills，复数 skills。

## 3. Mega Repo 目录

当前数字前缀可以保留，因为这是协调工作区，排序价值高于目录名的 public 美观。

```text
EvoZeus-MegaRepo/
  AGENTS.md
  README.md
  00-global/
    evozeus-overall-design.md
    repo-index.md
    repo-structure-naming.md
    material-index.md
    decision-log.md
  docs/
    README.md
    development-direction/
    tutorials/
    reference/
  10-repos/
    evozeus/
    evozeus-web/
    evozeus-session-signal-skill/
    evozeus-infra/
  20-materials/
  30-ops/
    discord-openclaw-governance-plan.md
  90-archive/
```

规则：

- `00-global/` 放跨 repo 的设计、索引、命名、决策。
- `docs/` 放面向人和 Agent 的介绍、开发方向和 tutorial，不放正式决策底账。
- `10-repos/` 只放 submodule 或 repo mirror，不放散落资料。
- `20-materials/` 放外部资料、调研、会议纪要、Feishu 导出。
- `30-ops/` 放社区试运行、发布操作、迁移脚本、权限执行计划。
- `90-archive/` 放冻结上下文，不参与当前决策。

## 4. EvoZeus 主 repo 目录

定位：public canonical protocol / governance / community intake / registry pointer repo。

生命周期职责：

| 主 repo 拥有 | 主 repo 不拥有 |
| --- | --- |
| `SKILL.md` zero-install entry | CLI / TUI / companion / local API |
| ontology、evidence、verdict、review contract | scanner implementation |
| Case / Candidate intake 和 lifecycle | installable Factor pack / scanner pack |
| semantic Factor / Skill / Pattern proposal | `.evozeus/` local state、SQLite ledger、lockfile |
| factor source pointer / registry reference | report execution、pack execution、upload / network runtime |

旧主 repo 执行层结构与目标职责不一致，已从主 repo 清理。执行层归 `evozeus-infra`；`evozeus-session-signal-skill` 只负责 Session Signal SKILL 和 factor tools，不负责 installable pack 或 scanner pack。主 repo 不应重新引入 runtime implementation、installable pack 或 scanner pack。

建议结构：

```text
EvoZeus/
  SKILL.md
  README.md
  CONTRIBUTING.md
  SECURITY.md
  AGENTS.md
  .github/
    ISSUE_TEMPLATE/
    PULL_REQUEST_TEMPLATE/
    workflows/
    CODEOWNERS
  docs/
    reference/
    governance/
    decisions/
    design/
    rfcs/
  schemas/
  candidates/
    community/
    reviewed/
    core/
    deprecated/
  cases/
  factors/
  patterns/
  examples/
    cases/
    reports/
    valid-candidates/
    invalid-candidates/
    rejected-prs/
  skills/
    index/
      SKILL.md
    evozeus-community-contribution/
      SKILL.md
      references/
    evozeus-redaction/
      SKILL.md
      references/
    evozeus-reporting/
      SKILL.md
      references/
    evozeus-factor-authoring/
      SKILL.md
      references/
    evozeus-skill-proposal/
      SKILL.md
      references/
  templates/
    candidate/
    factor/
    report/
    skill/
  scripts/
    github/
    checks/
    migrations/
  quality-gates/
    proof/
    privacy/
    schema/
    skill/
    factor/
```

相对当前结构，建议新增但不急于立即迁移：

- `templates/`：统一放 Candidate、Factor、Report、Skill 模板。当前模板分散在 GitHub templates 和 docs 中，后续容易重复。
- `quality-gates/`：放规则说明、测试夹具、门禁配置。当前 `scripts/github/` 偏 GitHub automation，未来 proof/privacy/schema/skill/factor 检查会更独立。
- skills 下的 `references/`：借鉴 `larksuite/cli`，长说明和流程拆出去，`SKILL.md` 只保留触发、核心规则、路由。

不建议新增：

- `cmd/`：主 repo 不是 runtime。
- `internal/`：主 repo 不承接 runtime implementation。
- `shortcuts/`：等 runtime/CLI 阶段再用。
- `__infra__/`：已清理，不属于目标结构。
- `factor_packs/` / `scanner_packs/`：installable pack 不放主 repo。

## 5. Skill 目录命名

当前命名 `skills/evozeus-*` 是合理的。建议保持：

```text
skills/
  index/
  evozeus-community-contribution/
  evozeus-development/
  evozeus-doctor-debugging/
  evozeus-factor-authoring/
  evozeus-redaction/
  evozeus-reporting/
  evozeus-infra/
  evozeus-skill-proposal/
```

命名规则：

- scenario skill 用 `evozeus-<scenario>`。
- `<scenario>` 用动作或工作流，不用抽象名词：
  - 好：`evozeus-redaction`、`evozeus-reporting`、`evozeus-factor-authoring`
  - 避免：`evozeus-utils`、`evozeus-common`、`evozeus-advanced`
- 每个 skill 的内部结构：

```text
skills/evozeus-<scenario>/
  SKILL.md
  references/
    <scenario>-workflow.md
    <scenario>-checklist.md
  assets/
  scripts/
```

- `references/` 用于长规则、模板解释、案例。
- `assets/` 只放 skill 执行需要的静态素材。
- `scripts/` 只放 skill 专属脚本；跨 skill 脚本放 repo 根部 `scripts/`。

## 6. Session Signal Skill 目录

定位：Session Signal SKILL + official factor tools。`SKILL.md` 是方法层，负责综合判断什么样的历史记录是高价值的；`factors/<slug>/` 是它可调用、可解释、可测试的 tools。

建议结构：

```text
evozeus-session-signal-skill/
  AGENTS.md
  README.md
  SKILL.md
  pyproject.toml
  src/
    evozeus_session_signal_skill/
      __init__.py
      factor.py
  schemas/
    official-factor-spec.schema.json
  factors/
    <factor-slug>/
      FACTOR.xml
      factor.py
      spec.json
      session.json
  scripts/
    validate_official_factor_spec.py
  tests/
```

命名规则：

- Python package 使用 `evozeus_session_signal_skill`。
- 抽象类命名为 `OfficialFactor`。
- 每个 factor tool 使用 `factors/<factor-slug>/`，slug 用 lower kebab-case。
- 顶层 `SKILL.md` 说明如何组合 factor tool 输出，而不是只描述 Python contract。
- official spec 必须包含 `stability: official`、`compatibility` 和 `governance.owner`。
- 不放 pack release、manifest、checksum、SBOM、attestation 或 promotion queue。
- `evozeus-factor-lab` 已转为 private/internal 历史实验仓库，不再是 mega repo active component，也不作为 public contribution route。

## 7. Runtime 目录

定位：未来 CLI/TUI/local registry/report/selective install runtime。它承接所有需要执行、安装、扫描、生成本地 report、维护 local state 或暴露 local API 的能力。

借鉴 `larksuite/cli`，但等 runtime 语言和发布方式稳定后再落地。

如果采用 Go CLI：

```text
evozeus-infra/
  cmd/
    evozeus/
    doctor/
    registry/
    report/
    install/
  internal/
    registry/
    report/
    scanner/
    policy/
    lockfile/
    output/
    security/
    qualitygate/
  schemas/
  examples/
  tests/
    cli_e2e/
  scripts/
```

如果采用 TypeScript / package workspace：

```text
evozeus-infra/
  packages/
    cli/
    core/
    registry/
    scanner/
  schemas/
  examples/
  tests/
  scripts/
```

命名规则：

- CLI 命令面用任务名：`judge`、`report`、`install`、`doctor`、`registry`。
- 内部模块用能力名：`scanner`、`policy`、`lockfile`、`output`。
- 不在 runtime repo 放 Session Signal SKILL 的方法定义；方法定义属于 `evozeus-session-signal-skill`，公共语义仍属于 `EvoZeus` 主 repo。
- runtime 只消费主 registry pointer、用户批准的 factor source 和 Python Factor contract。
- runtime 可以在 trust policy 稳定后承接旧主 repo prototype 的设计意图，但实现必须在本 repo 重新经过 permission、sandbox、dependency 和 public install gate。

## 8. Web 目录

定位：官网源码、public deployed surface、Discord / contribution route 入口。源码 private，页面输出 public。

建议结构：

```text
evozeus-web/
  src/
    app/
    components/
    lib/
    content/
      docs/
      guides/
      changelog/
  public/
  docs/
    launch-checklist.md
    content-policy.md
  tests/
```

命名规则：

- 页面内容放 `src/content/`，不要散在 components。
- 产品解释用 `guides/`，治理细节链接到主 repo，不复制一份。
- Discord 入口页只提供路线，不接收 raw evidence。

## 9. 迁移优先级

不建议一次性重排所有目录。建议按风险从低到高：

1. 在 mega repo 落地本命名规范。
2. 在全局文档中确认 `EvoZeus` 主 repo Protocol-only，并保持无执行层结构。
3. 在 `EvoZeus` 主 repo 新增 `templates/` 和 `quality-gates/`，先只放 README / 草案。
4. 给重型 scenario skills 增加 `references/`，不改 skill 行为。
5. 将 `evozeus-factor-lab` 从 active mega repo submodule 移除，并保持 private/internal。
6. 把 `evozeus-session-signal-skill` 收敛为 Session Signal SKILL + factor tools。
7. 等 runtime 技术栈确定后，在 `evozeus-infra` 引入 `cmd/internal` 或 `packages/*`，并按权限模型重建 runtime 能力。
8. Web source repo 已统一命名为 `evozeus-web`；这不改变源码 private 策略。

## 10. 当前判断

- 先不新建 `evozeus-skills`。
- 先不把 `cmd/`、`shortcuts/`、`internal/` 引入主 repo。
- `EvoZeus` 主 repo 不再被定义为 runtime 或 reference implementation repo；执行层结构不回流主 repo。
- `evozeus-factor-lab` 不再是 active component repo；不再作为 public contribution、contract 前置层或 runtime 默认来源。
- `evozeus-session-signal-skill` 是 Session Signal SKILL，不是 pack release 仓库。
- 可以立即采用 lower kebab-case 的新增目录和 future repo 命名。
- 可以立即把 skill 内长文档拆到 `references/`，借鉴 `larksuite/cli` 的 progressive disclosure。
