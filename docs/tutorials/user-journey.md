# Tutorial: User Journey

## 目标

理解用户从 `evozeus-community/skill` 进入后，如何先完成注册、安装 EvoZeus skeleton 与 EvoZeus skills，再在用户确认后按需拼接 runtime、default factors、judgment 和沉淀路径。

## 适合谁

- 第一次体验 EvoZeus 的用户。
- 设计 Start Here / onboarding 的 maintainer。
- 需要判断 PR 应该进入哪个 repo 的 Agent。

## 前置条件

先读：

- `../../00-global/evozeus-overall-design.md`
- `../../10-repos/evozeus/SKILL.md`
- `../../10-repos/evozeus/skills/index/SKILL.md`
- `runtime.md`
- `factor-lab.md`
- `official-factors.md`

## 操作步骤

1. 用户访问 community `/skill` 指引页：
   - 入口：`https://evozeus-community.vercel.app/skill`
   - 用户复制 registration / install command。
2. Agent 读取 `EvoZeus` 主 repo 的 `skills/evozeus-install-registration/SKILL.md`：
   - 检查本地是否已有 `.evozeus/`。
   - 如果已有注册信息，先核对 owner、workspace、已安装 skills 和 manifest。
   - 如果没有，创建最小 `.evozeus/` skeleton，并安装 EvoZeus 主 repo 内的 skills。
   - 输出 install report，然后停止在安装边界，不直接进入 judgment。
3. 用户明确要求开始判断时，Agent 才读取 `EvoZeus` 主 repo 的 root `SKILL.md` 和 `skills/evozeus-start-here-onboarding/SKILL.md`：
   - 启动 skeleton：protocol、ontology、evidence、verdict、privacy gate。
   - 输出 Session Verdict Card。
   - 不静默安装 runtime、scanner 或 factors。
4. 如果需要本地执行，Agent 按 `skills/index/SKILL.md` 路由到 runtime 场景：
   - 读取 `skills/evozeus-runtime-routing/SKILL.md`。
   - 再读取 `evozeus-runtime/SKILL.md` 承接 runtime、scanner、runner、local state 和 report generation。
   - 向用户说明要启用的本地能力、读取范围、写入范围、网络行为和回滚方式。
   - 等用户确认后，才进入 runtime path。
5. runtime 只通过可信路径拼接 default factors：
   - 读取 `EvoZeus` registry pointer。
   - 校验 factor source pointer、contract version、完整性信息和 compatibility。
   - 按 Python Factor contract 只启用用户选择的 factors。
6. runtime 在本地跑 judgment：
   - 扫描 session evidence。
   - 运行 selected official factors。
   - 生成 Session Verdict Card、Evidence Report 或本地 report。
7. 用户决定是否沉淀：
   - 不沉淀：结果留在本地。
   - 沉淀：先走 redaction，再按对象分流。
8. 按沉淀对象进入对应 repo：

| 沉淀对象 | 路由 |
| --- | --- |
| Case / Evidence / judgment report | `EvoZeus` issue 或 Candidate PR |
| semantic Factor proposal | 先进入 `EvoZeus` 主 repo |
| Python Factor contract / example | `evozeus-factor-lab` 或 `evozeus-factors-official` |
| executable Factor pack / scanner module | 不进入 factor contract repo；按 runtime / 独立发布机制处理 |
| runtime / infra / CLI / scanner execution / local state | `evozeus-runtime` |

## 产出

- 一次本地 judgment。
- 一个用户确认过的沉淀决定。
- 必要时，一个路由正确、脱敏后的 issue 或 PR。

## 不要做

- 不要把 `/skill` 变成 judgment 或 runtime 执行入口。
- 不要把 Start Here 变成静默安装。
- 不要让 runtime 直接消费 lab examples。
- 不要把 executable Factor pack、scanner module 或 runtime infra PR 提到 `EvoZeus` 主 repo 或 factor contract repo。
- 不要上传 raw private session。
- 不要绕过 source pointer、完整性校验、contract version 或用户确认。

## 验证

检查这条链路是否成立：

```text
evozeus-community/skill
  -> EvoZeus-Install Registration
  -> .evozeus reconciliation
  -> EvoZeus skeleton + skills installed
  -> user-approved protocol judgment
  -> optional runtime approval via EvoZeus-Runtime Routing
  -> registry pointer
  -> factor source pointer / contract version / integrity check
  -> local judgment
  -> user-approved redacted preservation
  -> correct repo route
```

如果任何一步需要执行代码、扫描本地文件、安装 pack 或维护 local state，它不属于 `EvoZeus` 主 repo 或 factor contract repo 目标职责，应路由到 `evozeus-runtime` 或后续独立发布机制。
