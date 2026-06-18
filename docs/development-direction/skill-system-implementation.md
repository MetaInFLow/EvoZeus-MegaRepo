# Skill System Implementation Plan

- Status: implemented in PR branch
- Last updated: 2026-06-18
- Scope: EvoZeus Skill 体系 review 后的整改实施路线
- Owner: MetaInFlow

本文是 `00-global/evozeus-skill-system-design.md` 的实施文档。目标不是一次性重写所有 skill，而是按风险顺序把入口、命名、路由和校验闭环补齐。

## 1. 背景

2026-06-18 对当前项目所有 `SKILL.md` 的 review 结论：

- 正式 skill 没有明显 orphan；root -> index -> scenario skill 的文件层面入口基本完整。
- 最大问题不是 skill 数量，而是 `/skill`、注册安装、runtime handoff 和 component ownership 没有统一成一条链。
- 主 repo `skills/evozeus-runtime/SKILL.md` 和 `evozeus-runtime/SKILL.md` 使用相同 `name: evozeus-runtime`，会在全局 skill registry 中冲突。
- `runtime` / `registry-release`、`reporting` / `runtime`、`doctor` / `runtime`、`development` / `skill-proposal` 的 precedence 不够硬。
- `check_pr_ready.py` 只检查主 repo 内部 skill，不能发现跨 repo duplicate name 或 historical prototype `SKILL.md` 误发现。

## 2. 实施目标

| Goal | Done means |
| --- | --- |
| `/skill` install-first | community `/skill` 只指导注册和安装，不直接 judgment/runtime |
| install owner 明确 | 有 `EvoZeus-Install Registration` 或等价 skill 定义 `.evozeus` 检查、注册、skeleton install、skills install |
| skill name 全局唯一 | cluster-level validator 不再发现重复 `name` |
| route precedence 明确 | index/root/scenario skills 对 runtime、registry、reporting、doctor、skill proposal 有一致优先级 |
| docs 同步 | 英文 README、中文 README、skill coverage、user journey、community 文案口径一致 |
| validation 自动化 | 本地命令可发现 frontmatter、重复名、prototype 误发现和断链引用 |

## 3. 非目标

本轮不做：

- 不实现完整 runtime CLI / TUI。
- 不默认启用 scanner、runner 或 default official factors。
- 不创建独立 `evozeus-skills` repo。
- 不把 runtime prototype 迁回主 repo。
- 不把 lab `reviewed` 资产作为普通用户可安装 official source。

## 4. Workstream A：统一 `/skill` 和安装链路

**Owner repos**

- `EvoZeus-community`
- `EvoZeus`
- `EvoZeus-MegaRepo`

**Required changes**

| File | Change |
| --- | --- |
| `10-repos/evozeus-community/src/app/skill/skill-content.ts` | 改成 registration / install guide；移除“Agent Skill Router”主语；不要求直接输出 Verdict / Evidence Report |
| `10-repos/evozeus-community/src/app/skill/route.test.ts` | 测试 `/skill` 包含 `.evozeus` 检查、skeleton install、skills install、install inventory、next command |
| `10-repos/evozeus-community/src/app/page.tsx` | 首页把 `/skill` 描述为注册和安装入口，不承诺直接进入因子库或 runtime |
| `10-repos/evozeus/SKILL.md` | 把 `#register` / old host 更新为 `/skill`；声明 `/skill` 完成安装后才进入 root protocol judgment |
| `10-repos/evozeus/skills/evozeus-start-here-onboarding/SKILL.md` | 收窄为安装后的 first-use protocol-only judgment，不再负责注册安装 |
| `10-repos/evozeus/docs/README.zh-CN.md` | 同步英文 README 的 Registration / Install Sequence |
| `docs/reference/skill-coverage.md` | 把 Register 拆成 registration、install、first judgment 三步 |
| `docs/tutorials/user-journey.md` | 从 `#register` 改为 `/skill`，补安装完成后“本地有什么、下一步跑什么、得到什么” |

**Acceptance criteria**

- `rg -n "community/#register|/#register|/register|Agent Skill Router|不是单一注册说明" 00-global docs 10-repos/evozeus 10-repos/evozeus-community -g '!docs/development-direction/skill-system-implementation.md' -g '!10-repos/evozeus-community/src/app/skill/route.test.ts'` 不再命中需要废弃的入口语义。
- `/skill` 输出中必须包含：
  - 检查 `.evozeus` 是否存在。
  - 已注册 / 未注册 / 本地缺失但远端存在的处理方式。
  - 安装 EvoZeus skeleton。
  - 安装 EvoZeus skills。
  - 安装完成后的 inventory。
  - 下一步命令和预期输出：protocol-only Session Verdict Card。

## 5. Workstream B：新增 install registration skill

**Target file**

`10-repos/evozeus/skills/evozeus-install-registration/SKILL.md`

**Skill contract**

```yaml
name: evozeus-install-registration
description: Use when registering a local EvoZeus workspace, installing the EvoZeus skeleton, installing EvoZeus skills, or reconciling existing .evozeus registration state.
```

**Required content**

- Trigger:
  - 用户来自 `https://evozeus-community.vercel.app/skill`。
  - 用户要求安装、注册、恢复或检查 EvoZeus。
- Input:
  - 当前 workspace path。
  - `.evozeus` 是否存在。
  - local install manifest。
  - optional community registration API result。
- Process:
  - 先读本地 state。
  - 已注册则检查 skeleton 和 skills inventory。
  - 未注册则说明要写哪些文件，等待用户批准。
  - 安装 skeleton 和 skills 后输出 install report。
- Output:
  - registration status。
  - skeleton version / source commit。
  - installed skill list。
  - files written。
  - next command。
- Boundary:
  - 不运行 runtime。
  - 不扫描 raw session。
  - 不创建 GitHub issue/PR。
  - 不上传 private context。

**Index changes**

- `skills/index/SKILL.md` 增加 install registration 行。
- `docs/reference/skill-coverage.md` 增加 `evozeus-install-registration`。
- community `/skill` 指向这个 skill，而不是把自己当 router。

## 6. Workstream C：解决 `evozeus-runtime` 命名冲突

**Recommended migration**

1. 将主 repo scenario skill 改名为：
   - folder: `skills/evozeus-runtime-routing/`
   - frontmatter: `name: evozeus-runtime-routing`
   - title: `EvoZeus-Runtime Routing`
2. 更新所有引用：
   - root `SKILL.md`
   - `skills/index/SKILL.md`
   - `docs/reference/skill-coverage.md`
   - community `/skill`
   - README / tutorials。
3. runtime repo root skill 保留 component owner 语义；如果 cluster validator 要求 component 名也带后缀，可改为 `name: evozeus-runtime-component`，但不要和主 repo scenario skill 同名。
4. 可选：保留一个迁移说明，说明旧 `evozeus-runtime` scenario name 已废弃。

**Acceptance criteria**

- cluster-level validator 没有 duplicate `name`。
- `rg -n "evozeus-runtime" docs 00-global 10-repos/evozeus 10-repos/evozeus-community` 中能区分 route skill 和 component repo。

## 7. Workstream D：补硬 precedence

**Target files**

- `10-repos/evozeus/SKILL.md`
- `10-repos/evozeus/skills/index/SKILL.md`
- `10-repos/evozeus/skills/evozeus-runtime-routing/SKILL.md`
- `10-repos/evozeus/skills/evozeus-registry-release/SKILL.md`
- `10-repos/evozeus/skills/evozeus-reporting/SKILL.md`
- `10-repos/evozeus/skills/evozeus-doctor-debugging/SKILL.md`
- `10-repos/evozeus/skills/evozeus-development/SKILL.md`
- `10-repos/evozeus/skills/evozeus-skill-proposal/SKILL.md`

**Rules to encode**

| Conflict | Rule |
| --- | --- |
| runtime vs registry-release | registry-release 发布/变更 registry pointer；runtime 消费/启用 verified release |
| reporting vs runtime | reporting 写内容；runtime 执行本地生成、文件输出、HTML/JSON pipeline |
| doctor vs runtime | doctor 做诊断；修改 doctor/runtime implementation 才读 runtime |
| development vs skill-proposal | 改 `SKILL.md` / `skills/` 必须读两者 |
| preservation vs contribution | preservation 先判断 artifact route；公开贡献再读 contribution + redaction |

**Acceptance criteria**

- `skills/index/SKILL.md` 有一张 precedence table。
- root `SKILL.md` 不再把 report、runtime、install 混在同一条描述里。
- 每个受影响 skill 有最小 Output Shape。

## 8. Workstream E：统一 lab reviewed channel

**Decision to implement**

普通用户 runtime consumption 只允许 official release manifest。

**Required changes**

| File | Change |
| --- | --- |
| `10-repos/evozeus/docs/governance/factor-registry-governance.md` | 移除或限定 reviewed explicit install；改为 maintainer experimental only |
| `10-repos/evozeus-factor-lab/README.md` | 保持 reviewed not runtime-installable |
| `10-repos/evozeus-factor-lab/reviewed/README.md` | 明确 reviewed 只能 promotion / lab-local test |
| `10-repos/evozeus-runtime/SKILL.md` | 保持 official-only consumption |
| `docs/reference/skill-coverage.md` | 明确 lab reviewed 不等于 runtime install source |

**Acceptance criteria**

- 没有文档同时说 reviewed 可以被普通 runtime 安装。
- runtime docs 始终要求 registry pointer + official manifest + checksum + attestation。

## 9. Workstream F：新增 cluster-level validator

**Recommended location**

- `scripts/validate_skill_system.py` at mega repo root, or
- `30-ops/scripts/validate_skill_system.py` if scripts should stay ops-scoped.

Given this mega repo already uses `docs/reference/skill-coverage.md` as cluster-level source, root `scripts/validate_skill_system.py` is clearer.

**Checks**

1. Discover formal skills:
   - `10-repos/evozeus/SKILL.md`
   - `10-repos/evozeus/skills/*/SKILL.md`
   - `10-repos/evozeus-runtime/SKILL.md`
   - `10-repos/evozeus-factor-lab/SKILL.md`
   - `10-repos/evozeus-factors-official/SKILL.md`
2. Exclude:
   - `node_modules`
   - `10-repos/evozeus-runtime/prototypes/main-repo-runtime/**`
3. Validate:
   - YAML frontmatter exists。
   - `name` exists and matches lowercase kebab-case。
   - `description` exists and starts with `Use when`。
   - `name` is globally unique。
   - documented folder/name exceptions are declared。
4. Reference checks:
   - `docs/reference/skill-coverage.md` references existing skills。
   - community `/skill` scenario list references existing skills。
   - no canonical docs point to historical prototype `SKILL.md` as formal skill。

**Acceptance criteria**

```bash
python3 scripts/validate_skill_system.py
git diff --check
```

Both pass.

## 10. Suggested rollout order

1. **P0.1** Update community `/skill` to install-first and adjust tests.
2. **P0.2** Add `EvoZeus-Install Registration` skill and route it from root/index/coverage.
3. **P0.3** Rename main runtime route skill to avoid `evozeus-runtime` collision.
4. **P0.4** Sync English README, Chinese README, user journey, skill coverage.
5. **P1.1** Add precedence table and output shapes.
6. **P1.2** Resolve reviewed lab channel wording.
7. **P1.3** Add cluster-level validator.
8. **P2** Decide whether to add `EvoZeus-Candidate Review`, `EvoZeus-Source Locator`, and `EvoZeus-PR Triage`.

## 11. Verification matrix

| Repo | Command |
| --- | --- |
| `EvoZeus-community` | `npm test` |
| `EvoZeus` | `/usr/bin/python3 -m py_compile scripts/check_pr_ready.py` |
| `EvoZeus` | `git diff --check` |
| `EvoZeus-MegaRepo` | `python3 scripts/validate_skill_system.py` |
| `EvoZeus-MegaRepo` | `git diff --check` |

If `python3 scripts/check_pr_ready.py --base HEAD` hangs in the local environment, use `/usr/bin/python3` for syntax validation and record the runtime issue separately under Doctor / environment diagnostics.

## 12. Definition of Done

Skill system remediation is complete when:

- `/skill` is an install guide, not a judgment/runtime runner.
- Existing `.evozeus` is checked before creating or updating registration.
- Install report states local inventory and next command.
- All formal skill `name` values are globally unique.
- No formal docs route scanner/runner implementation back to the main repo.
- Runtime consumes only official release manifests by default.
- The validator prevents duplicate names and prototype `SKILL.md` mis-discovery.
- Chinese and English user-facing docs describe the same sequence.
