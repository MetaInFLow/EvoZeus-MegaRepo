# Skill Coverage

- Status: active
- Last updated: 2026-06-26
- Scope: EvoZeus agent 接入和 component repo 的 Skill 支撑覆盖矩阵
- Owner: MetaInFlow

本文记录从 `evozeus-web /skill` 到 registration、install、judgment、沉淀和开发分流的 Skill 覆盖。它不是 release checklist，也不是项目主目标或 KPI；release checklist 仍属于各 component repo。EvoZeus 的主线是通过社区迭代“判断高质量信号”的方法论，Skill 只是让 Agent 可读、可路由、可复用的支撑层。

## 1. 用户旅程覆盖

| Step | 目标 | Skill / 入口 | 状态 |
| --- | --- | --- | --- |
| Registration guide | 用户从 community `/skill` 复制安装指令 | `evozeus-web` page | covered |
| Install / reconcile | 检查 `.evozeus`，注册或恢复，安装 skeleton 和 skills | `EvoZeus/skills/evozeus-install-registration` | covered |
| Start Here | 安装后的首次 protocol-only judgment | `EvoZeus/skills/evozeus-start-here-onboarding` + `EvoZeus/SKILL.md` | covered |
| Scenario routing | 选择 runtime、report、redaction、contribution、development 等场景 | `EvoZeus/skills/index/SKILL.md` | covered |
| First judgment | 在回复中输出 Session Verdict Card | `EvoZeus/SKILL.md` + `evozeus-reporting` | covered |
| Runtime approval | 用户确认本地执行、读取、写入、安装和网络行为 | `EvoZeus/skills/evozeus-runtime-routing` + `evozeus-infra/SKILL.md` | covered as policy |
| Default factor tools | 从 registry pointer 解析 default factor source 和 contract version | `evozeus-registry-release` + `evozeus-infra/SKILL.md` + `evozeus-infra/test:infra-contract` | covered as policy; implementation future |
| Session Signal SKILL / factor tools | 用 official factor tools 识别高价值 session，并校验 Python `OfficialFactor` contract、schema 和 canonical examples | `evozeus-session-signal-skill/SKILL.md` + `python3 -m unittest discover -s tests` | covered as method + tools |
| Local runtime execution | 扫描、运行 factors、生成 report、写 lockfile | `evozeus-infra/SKILL.md` + `evozeus-infra/test:infra-components` | component availability covered; product implementation still future |
| Preservation decision | 用户确认是否沉淀 | `evozeus-artifact-preservation` | covered |
| Public redaction | 去除 raw session、secret、客户资料和私有路径 | `evozeus-redaction` | covered |
| Main repo contribution | Case、Candidate、semantic Factor、Pattern、Habit | `evozeus-community-contribution` | covered |
| Session Signal SKILL / factor tools | `SKILL.md` 组合 factor tool 输出，判断历史记录价值；`factors/<slug>/` 提供可解释 tools | `evozeus-session-signal-skill/SKILL.md` + `python3 scripts/validate_official_factor_spec.py factors/*/spec.json` | covered as method + tools |
| Static Skill wrapper / evolution | 为静态 `SKILL.md` 建立 case、run card、evaluation notes 和 evolution proposal 闭环 | `EvoZeus-wrapper/SKILL.md` + `templates/*.md` | covered as seed harness |
| Runtime / infra development | CLI、TUI、companion、scanner execution、local state | `evozeus-infra/SKILL.md` | covered as route |

## 2. Main Repo Scenario Skills

| Skill | 职责 | 不做什么 |
| --- | --- | --- |
| `SKILL.md` | root skeleton、zero-install judgment、Verdict routing | 不静默安装、不写 `.evozeus/`、不 GitHub |
| `evozeus-install-registration` | `.evozeus` registration、skeleton install、skills install、install report | 不运行 judgment、不启用 runtime |
| `evozeus-start-here-onboarding` | 安装后的首次 protocol-only judgment | 不注册、不安装、不写 runtime state |
| `index` | scenario router | 不替代具体 Skill |
| `evozeus-reporting` | Evidence Report、Session Verdict Card、Case summary | 不发布 raw evidence |
| `evozeus-artifact-preservation` | Verdict -> Artifact -> repo route | 不处理 runtime implementation |
| `evozeus-community-contribution` | public Case/Candidate/contribution | 不允许无关 runtime/governance 混入 |
| `evozeus-redaction` | public evidence privacy gate | 不判断 artifact value |
| `evozeus-factor-authoring` | semantic Factor quality | 不承接 executable pack code |
| `evozeus-scanner-pack-authoring` | scanner / executable source route | 不把 scanner 放进 factor contract repo |
| `evozeus-registry-release` | registry pointer、default factors、contract/source reference | 不存 pack body |
| `evozeus-runtime-routing` | runtime route and trust policy from main repo context | 不实现 runtime in main repo |
| `evozeus-development` | protocol/governance/docs development | 不把 runtime implementation 加回主 repo |
| `evozeus-doctor-debugging` | failure diagnosis and environment classification | 不把环境问题误升为 Skill |
| `evozeus-skill-proposal` | Skill changes and instruction governance | 不为一次性经验创建 Skill |

## 3. Component Repo Skills

| Repo | Skill | 职责 |
| --- | --- | --- |
| `evozeus-infra` | `SKILL.md` + `npm run test:infra-components` + `npm run test:infra-contract` | runtime enablement、infra components、permissions、default official factors、lockfile、local judgment、runtime PR |
| `evozeus-session-signal-skill` | `SKILL.md` + `python3 -m unittest discover -s tests` + `python3 scripts/validate_official_factor_spec.py factors/*/spec.json` | Session Signal SKILL、Python OfficialFactor contract、官方 factor tools、canonical examples |
| `EvoZeus-wrapper` | `SKILL.md` + `templates/case.md` + `templates/run-card.md` + `templates/evolution-proposal.md` | 静态 Skill 的 case、run card、evaluation notes、evolution proposal 和 regression case 工作流 |

## 4. Remaining Contract Gaps

这些不是 Skill 缺失，而是产品契约尚未完成：

1. Main registry schema / index。
2. Default factor set 的 source pointer、contract version、recommended vs enabled、channel、version pinning 行为。
3. 真实业务 Factor pack 的发布机制尚未定义，不能落在 `evozeus-session-signal-skill`。
4. Runtime lockfile schema、registry consumer implementation。
5. CI 集成：当前已有本地 `npm test`，尚未接入 GitHub Actions。

## 5. Review Rule

每次新增用户旅程步骤或 component repo 时，必须回答：

- 有没有对应 Skill 或 AGENTS 入口？
- 有没有明确 owner repo？
- 是否需要用户确认？
- 是否涉及 raw session、secret、客户资料、私有路径？
- 是否需要 source pointer、完整性校验、contract version 或 lockfile？
- 失败时应该停在哪里，而不是自动绕过？
