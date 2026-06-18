# Tutorial: User Journey

## 目标

理解用户从 `evozeus-community/#register` 进入后，如何从 EvoZeus skeleton 按需拼接 runtime、default official factors、judgment 和沉淀路径。

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

1. 用户访问 community 注册入口：
   - 入口：`https://evozeus-community.vercel.app/#register`
   - 用户复制 Start Here command。
2. Agent 读取 `EvoZeus` 主 repo 的 root `SKILL.md`：
   - 启动 skeleton：protocol、ontology、evidence、verdict、privacy gate。
   - 不静默安装 runtime、scanner 或 factors。
3. 如果需要本地执行，Agent 按 `skills/index/SKILL.md` 路由到 runtime 场景：
   - 读取 `skills/evozeus-runtime/SKILL.md`。
   - 向用户说明要启用的本地能力、读取范围、写入范围、网络行为和回滚方式。
   - 等用户确认后，才进入 runtime path。
4. runtime 只通过可信路径拼接 default official factors：
   - 读取 `EvoZeus` registry pointer。
   - 读取 `evozeus-factors-official` release manifest。
   - 校验 checksum、SBOM / attestation 和 compatibility。
   - 只启用用户选择的 factors。
5. runtime 在本地跑 judgment：
   - 扫描 session evidence。
   - 运行 selected official factors。
   - 生成 Session Verdict Card、Evidence Report 或本地 report。
6. 用户决定是否沉淀：
   - 不沉淀：结果留在本地。
   - 沉淀：先走 redaction，再按对象分流。
7. 按沉淀对象进入对应 repo：

| 沉淀对象 | 路由 |
| --- | --- |
| Case / Evidence / judgment report | `EvoZeus` issue 或 Candidate PR |
| semantic Factor proposal | 先进入 `EvoZeus` 主 repo |
| executable Factor pack / scanner module | `evozeus-factor-lab` |
| promoted official pack | `evozeus-factors-official` |
| runtime / infra / CLI / scanner execution / local state | `evozeus-runtime` |

## 产出

- 一次本地 judgment。
- 一个用户确认过的沉淀决定。
- 必要时，一个路由正确、脱敏后的 issue 或 PR。

## 不要做

- 不要把 Start Here 变成静默安装。
- 不要让 runtime 直接消费 lab moving branch。
- 不要把 executable Factor pack、scanner module 或 runtime infra PR 提到 `EvoZeus` 主 repo。
- 不要上传 raw private session。
- 不要绕过 manifest、checksum、attestation 或用户确认。

## 验证

检查这条链路是否成立：

```text
community/#register
  -> EvoZeus root SKILL.md
  -> optional runtime approval
  -> registry pointer
  -> official manifest / checksum / attestation
  -> local judgment
  -> user-approved redacted preservation
  -> correct repo route
```

如果任何一步需要执行代码、扫描本地文件、安装 pack 或维护 local state，它不属于 `EvoZeus` 主 repo 目标职责，应路由到 `evozeus-runtime` 或 Factor lifecycle repo。
