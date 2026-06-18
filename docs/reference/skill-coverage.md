# Skill Coverage

- Status: active
- Last updated: 2026-06-18
- Scope: EvoZeus 用户旅程和 component repo 的 Skill 覆盖矩阵
- Owner: MetaInFlow

本文记录从 `community/#register` 到 judgment、沉淀和开发分流的 Skill 覆盖。它不是 release checklist；release checklist 仍属于各 component repo。

## 1. 用户旅程覆盖

| Step | 目标 | Skill / 入口 | 状态 |
| --- | --- | --- | --- |
| Register | 用户从 community 复制 Start Here | `evozeus-community` page + `EvoZeus/skills/evozeus-start-here-onboarding` | covered |
| Start Here | 激活 skeleton，不静默安装 | `EvoZeus/SKILL.md` | covered |
| Scenario routing | 选择 runtime、report、redaction、contribution、development 等场景 | `EvoZeus/skills/index/SKILL.md` | covered |
| First judgment | 在回复中输出 Session Verdict Card | `EvoZeus/SKILL.md` + `evozeus-reporting` | covered |
| Runtime approval | 用户确认本地执行、读取、写入、安装和网络行为 | `EvoZeus/skills/evozeus-runtime` + `evozeus-runtime/SKILL.md` | covered as policy |
| Default official factors | 从 registry pointer 解析 default official factors | `evozeus-registry-release` + `evozeus-runtime/SKILL.md` + `evozeus-runtime/test:runtime-contract` | covered as test contract |
| Official release verification | 校验 manifest、checksum、SBOM / attestation | `evozeus-factors-official/SKILL.md` + `evozeus-factors-official/test:release-contract` | covered as test contract |
| Local runtime execution | 扫描、运行 factors、生成 report、写 lockfile | `evozeus-runtime/SKILL.md` + `evozeus-runtime/test:infra-components` | component availability covered; product implementation still future |
| Preservation decision | 用户确认是否沉淀 | `evozeus-artifact-preservation` | covered |
| Public redaction | 去除 raw session、secret、客户资料和私有路径 | `evozeus-redaction` | covered |
| Main repo contribution | Case、Candidate、semantic Factor、Pattern、Habit | `evozeus-community-contribution` | covered |
| Pack / scanner lab | executable Factor pack、scanner module、resolver | `evozeus-scanner-pack-authoring` + `evozeus-factor-lab/SKILL.md` + `test:lab-contract` + `test:fixed-factor` + `test:factor` | covered as executable test contract |
| Official pack promotion | lab reviewed asset 进入 official release | `evozeus-factors-official/SKILL.md` + `test:release-contract` + `test:fixed-factor` + `test:factor` | covered as executable test contract |
| Runtime / infra development | CLI、TUI、companion、scanner execution、local state | `evozeus-runtime/SKILL.md` | covered as route |

## 2. Main Repo Scenario Skills

| Skill | 职责 | 不做什么 |
| --- | --- | --- |
| `SKILL.md` | root skeleton、zero-install judgment、Verdict routing | 不静默安装、不写 `.evozeus/`、不 GitHub |
| `evozeus-start-here-onboarding` | community registration / Start Here 首次进入 | 不扫描、不安装、不写文件 |
| `index` | scenario router | 不替代具体 Skill |
| `evozeus-reporting` | Evidence Report、Session Verdict Card、Case summary | 不发布 raw evidence |
| `evozeus-artifact-preservation` | Verdict -> Artifact -> repo route | 不处理 runtime implementation |
| `evozeus-community-contribution` | public Case/Candidate/contribution | 不允许无关 runtime/governance 混入 |
| `evozeus-redaction` | public evidence privacy gate | 不判断 artifact value |
| `evozeus-factor-authoring` | semantic Factor quality | 不承接 executable pack code |
| `evozeus-scanner-pack-authoring` | executable pack / scanner lab route | 不发布 official release |
| `evozeus-registry-release` | registry pointer、default official factors、release reference | 不存 pack body |
| `evozeus-runtime` | runtime route and trust policy from main repo context | 不实现 runtime in main repo |
| `evozeus-development` | protocol/governance/docs development | 不扩展 `__infra__` as product runtime |
| `evozeus-doctor-debugging` | failure diagnosis and environment classification | 不把环境问题误升为 Skill |
| `evozeus-skill-proposal` | Skill changes and instruction governance | 不为一次性经验创建 Skill |

## 3. Component Repo Skills

| Repo | Skill | 职责 |
| --- | --- | --- |
| `evozeus-runtime` | `SKILL.md` + `npm run test:infra-components` + `npm run test:runtime-contract` | runtime enablement、infra components、permissions、default official factors、lockfile、local judgment、runtime PR |
| `evozeus-factor-lab` | `SKILL.md` + `npm run test:lab-contract` + `npm run test:fixed-factor` + `npm run test:factor` | lab submission、evidence/privacy/domain/scanner gate、固定 Factor、指定 Factor、reviewed/rejected |
| `evozeus-factors-official` | `SKILL.md` + `npm run test:release-contract` + `npm run test:fixed-factor` + `npm run test:factor` | official release unit、manifest/checksum/SBOM/attestation、固定 Factor、指定 Factor、tag、registry pointer |

## 4. Remaining Contract Gaps

这些不是 Skill 缺失，而是产品契约尚未完成：

1. Main registry schema / index。
2. Default official factor set 的完整发布资产：recommended vs enabled、channel、version pinning、deprecated/yanked 行为。
3. 首个 official pack release asset。
4. Runtime lockfile schema、registry consumer implementation。
5. CI 集成：当前已有本地 `npm test`，尚未接入 GitHub Actions。

## 5. Review Rule

每次新增用户旅程步骤或 component repo 时，必须回答：

- 有没有对应 Skill 或 AGENTS 入口？
- 有没有明确 owner repo？
- 是否需要用户确认？
- 是否涉及 raw session、secret、客户资料、私有路径？
- 是否需要 manifest、checksum、attestation 或 lockfile？
- 失败时应该停在哪里，而不是自动绕过？
