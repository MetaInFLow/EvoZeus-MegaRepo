# Infra Local Execution Kernel 开发标准

- Status: active
- Last updated: 2026-06-19
- Scope: 旧 `__infra__` 到 `evozeus-infra` 的迁移开发边界、repo 分工、验收和验证标准
- Owner: MetaInFlow

本文定义 EvoZeus 本地执行层的开发标准。它放在 `EvoZeus-MegaRepo`，因为它不是某个单一 repo 的实现说明，而是跨 `EvoZeus` main repo、`evozeus-community`、`evozeus-infra`、`evozeus-factor-lab` 和 `evozeus-factors-official` 的分工与验收契约。

一句话原则：

```text
infra = local execution kernel
```

`evozeus-infra` 承接本地执行平面：workspace、scanner framework、factor runner、SQLite ledger、report、CLI/TUI、companion backend。Factor 协议语义、Factor Python contract、社区入口和治理不属于 infra。

> Naming note: 当前本地目录仍是 `10-repos/evozeus-runtime`，但 package name、README 和 SKILL 已按 `evozeus-infra` 定义。本文使用产品名 `evozeus-infra`，并在路径中保留当前本地目录名。

## 1. 开发落点判定

开发前先按对象归属判断 repo，不按“哪里代码方便”判断。

| 你要改什么 | 目标 repo | 判定标准 |
| --- | --- | --- |
| Protocol、Verdict、Case、Evidence、Candidate 语义 | `10-repos/evozeus` | 公共协议、治理、schema、ontology 或贡献生命周期 |
| Evidence Report 格式、report 模板协议 | `10-repos/evozeus` | 规定输出语义，不执行本地生成 |
| public Case / Candidate / Pattern | `10-repos/evozeus` | 可公开、可脱敏、可被社区 review 的资产 |
| registry pointer、default factor set 指针 | `10-repos/evozeus` | 只引用可信来源和 contract version，不存执行包 |
| `/skill` 安装入口、用户引导、官网文案 | `10-repos/evozeus-community` | public-facing front door，不跑 scan/analyze |
| workspace bootstrap、paths、config、lockfile | `10-repos/evozeus-runtime` | 本地状态和执行权限属于 infra |
| SQLite Local Analysis Ledger | `10-repos/evozeus-runtime` | 本地事实账本，记录 scan/analyze/result |
| session scan engine、scanner sandbox、resolver runtime | `10-repos/evozeus-runtime` | 执行 scanner、读本地文件、控制权限 |
| CLI / TUI / local companion API | `10-repos/evozeus-runtime` | 本地执行入口和本地服务 |
| factor runner、runtime isolation、`subprocess_uv` | `10-repos/evozeus-runtime` | 执行框架属于 infra |
| report generator / local HTML dashboard | `10-repos/evozeus-runtime` | 本地执行输出，不是 protocol 格式定义 |
| Factor 抽象类草案、spec 草案、examples | `10-repos/evozeus-factor-lab` | 只定义 Python Factor contract，不存真实业务 pack |
| 稳定 OfficialFactor 抽象类、官方 spec、canonical examples | `10-repos/evozeus-factors-official` | official 表示稳定合约，不表示 pack 发布仓库 |
| scanner sandbox、scanner resolver、provider scanner execution | `10-repos/evozeus-runtime` | scanner 是本地执行能力，不放 factor lab |
| factor 业务逻辑包 / scanner pack 发布物 | 待独立发布机制或外部可信来源 | 当前不放 `factor-lab` / `factors-official` |
| upload / GitHub issue / PR automation 规则 | `10-repos/evozeus` + optional infra action | 规则在 main；用户批准后 infra 可执行 |

禁止混放：

- 不把可执行 scanner、factor pack、SQLite、CLI、TUI、companion API 加回 `EvoZeus` main repo。
- 不让 `evozeus-infra` 直接消费 lab moving branch 或 examples。
- 不把 factor lab examples 当成普通用户 runtime install source。
- 不把 pack release、manifest、checksum、SBOM/attestation 塞进 `evozeus-factor-lab` 或 `evozeus-factors-official`。
- 不在 community page 收 raw session、secret、客户资料或未脱敏 evidence。

## 2. 分支和 PR 标准

每个开发任务必须先判断单 repo 还是跨 repo。

| 任务类型 | 分支位置 | PR 形态 |
| --- | --- | --- |
| 只改跨 repo 文档、索引、决策 | `EvoZeus-MegaRepo` | 一个 mega repo PR |
| 只改 main protocol / governance | `10-repos/evozeus` | 子 repo PR，完成后再更新 mega repo submodule pointer |
| 只改 community frontend | `10-repos/evozeus-community` | 子 repo PR，完成后再更新 mega repo submodule pointer |
| 只改 infra implementation | `10-repos/evozeus-runtime` | 子 repo PR，完成后再更新 mega repo submodule pointer |
| 只改 Factor contract / examples | 对应 factor repo | 子 repo PR，完成后再更新 mega repo submodule pointer |
| 同时改协议、infra 和 Factor contract | 拆成多个 PR | 先 main protocol，再 factor contract，再 infra consumer，最后 mega repo 指针 |

分支命名：

```text
codex/<short-topic>
```

本轮文档分支：

```text
codex/infra-dev-doc-standards
```

提交前要求：

- 子 repo 有变更时，先在子 repo 内完成 commit；mega repo 只更新 submodule pointer。
- 不把 unrelated dirty submodule pointer 一起提交。
- 不用一个 PR 同时改变 protocol contract 和 runtime implementation，除非 PR 说明明确列出兼容性和回滚路径。

## 3. 迁移顺序

旧 `__infra__` 只作为 migration-source prototype。主动开发必须在当前 owner repo 重建能力，不原样把 prototype 变成默认入口。

推荐顺序：

1. `workspace + paths + config + lockfile`
2. `SQLite Local Analysis Ledger`
3. `Codex scanner + resolver contract`
4. `factor pack discovery + factor runner`
5. `scan/analyze service`
6. `CLI/TUI/companion/browser workspace/report`

每一阶段必须形成可验证闭环，再进入下一阶段。

## 4. 各阶段正确性标准

### Phase 1: workspace + paths + config + lockfile

目标：用户明确批准后，本地有稳定、可回滚、可解释的 `.evozeus/infra` 状态。

必须验证：

- 不写入 `EvoZeus` main repo 的 protocol 目录。
- 初次 bootstrap 只创建最小状态：config、infra dir、lockfile schema 或空 ledger。
- lockfile 记录 selected factors、contract version、source pointer、checksum 或等价完整性信息、compatibility。
- rollback path 明确：删除 `.evozeus/infra` 或禁用 selected factors。
- doctor 能解释当前状态。

Done means：

```text
onboard -> write local state -> show lockfile -> doctor explains state
```

### Phase 2: SQLite Local Analysis Ledger

目标：SQLite 成为 TUI、browser workspace、companion backend 和 report generator 共享的本地事实账本。

必须验证：

- 有 source、scanner、capability、execution、result、route 分层。
- SQLite 不默认保存完整 raw session 原文，只保存 locator、hash、redacted preview 和结构化字段。
- 能回答“扫到了什么、跑过什么、哪些过期、哪些需要重跑”。
- result route 不硬编码 UI 位置，使用 route registry。
- schema migration 可重复运行，不破坏已有 ledger。

Done means：

```text
scan fixture -> write ledger -> query sessions/results/routes -> rerun skips unchanged input
```

### Phase 3: Codex scanner + resolver contract

目标：infra 拥有 scanner 执行框架和 resolver contract；provider-specific scanner 是本地执行能力，不进入 Factor contract repo。

必须验证：

- infra 只定义 scanner sandbox、resolver registry、locator envelope 和 permission gate。
- Codex scanner pack 草稿在 `evozeus-runtime` 的实验区或独立 scanner 发布机制中声明 files read、files written、env、external commands、network、side effects。
- scanner 输出统一 `SessionEnvelope` 或等价标准事件模型。
- resolver 能从 ledger locator 定位原始 event，并检测 source missing / hash mismatch。
- scanner 默认不联网，不上传。

Done means：

```text
scan Codex fixture -> normalized events -> ledger locator -> resolver returns source or structured mismatch
```

### Phase 4: factor pack discovery + factor runner

目标：infra 能发现、校验并运行实现 Python Factor contract 的 selected factors；`factor-lab` / `factors-official` 只提供 contract 和 examples。

必须验证：

- draft factor pack 不在 lab；lab 只保存 `AbstractFactor`、spec 和 examples。
- official repo 不保存 official factor pack；它只保存稳定 `OfficialFactor`、schema 和 canonical examples。
- infra 只通过 main registry pointer 或用户批准的本地来源解析 factor source。
- factor runner 默认按 Python Factor contract 执行，支持 `in_process` 和 `subprocess_uv` 的 contract、timeout、错误隔离和 result schema 校验。
- factor 失败不会中断其他 factor。
- evidence refs 指向存在的 session event。

Done means：

```text
registry pointer -> factor source + contract version -> selected Python Factor -> FactorResult -> ledger/report
```

### Phase 5: scan/analyze service

目标：形成最小本地闭环：`onboard -> scan -> analyze -> report -> doctor`。

必须验证：

- scan 和 analyze 有明确 user approval gate。
- scan/analyze 输入输出写入 ledger。
- 重跑使用 fingerprint 判断 skip / rerun / stale / failed。
- service 可以被 CLI/TUI/companion 复用，而不是绑定单一 UI。
- 网络、上传、issue/PR automation 默认关闭。

Done means：

```text
onboard -> scan fixture -> analyze selected factors -> write ledger -> generate report -> doctor ok
```

### Phase 6: CLI/TUI/companion/browser workspace/report

目标：本地入口可用，但仍受 permission、lockfile、ledger 和 registry contract 约束。

必须验证：

- CLI/TUI/companion 只读同一个 ledger。
- local companion 只监听 `127.0.0.1`，端口和 token 明确。
- HTML dashboard 是本地 report 输出，不是云端上传。
- UI 不直接读取 raw provider files；展开 source 时通过 resolver 和权限 gate。
- report 同时有 Markdown/JSON first fallback。

Done means：

```text
CLI/TUI/browser can show the same session, factor result, route, evidence refs, and rollback state
```

## 5. Repo 级验证命令

验证必须在对应 repo 内运行。只改文档时可以运行较轻的文档级检查；改 executable code、schema、runtime、pack 或 frontend 时必须运行该 repo 的完整相关命令。

### Mega repo

适用：跨 repo 文档、索引、决策、tutorial。

```bash
git diff --check
git status --short --branch
git submodule status
```

### `10-repos/evozeus`

适用：protocol、governance、schema、Case/Candidate、registry pointer、report format。

```bash
git diff --check
python3 scripts/check_pr_ready.py
npm run test:github-gates
```

### `10-repos/evozeus-community`

适用：官网、`/skill`、用户引导、frontend。

```bash
git diff --check
npm run lint
npm run test
npm run build
```

### `10-repos/evozeus-runtime`

适用：`evozeus-infra` active implementation、doctor、permission gate、lockfile、scanner sandbox、factor runner、report generator。

```bash
git diff --check
npm run doctor
npm test
npm run test:infra-components
npm run test:infra-contract
```

旧 prototype 只能作为迁移参考。如果某个 PR 明确修改 `prototypes/main-repo-runtime/`，需要额外运行该 prototype 自己的 Python tests 或 smoke checks；但 prototype 通过不等于 active infra 通过。

### `10-repos/evozeus-factor-lab`

适用：Python Factor contract 草案、spec schema、examples、contract tests。

```bash
git diff --check
python3 -m unittest discover -s tests
python3 scripts/validate_factor_spec.py examples/specs/*.json
```

### `10-repos/evozeus-factors-official`

适用：稳定 Python OfficialFactor contract、官方 spec schema、canonical examples。

```bash
git diff --check
python3 -m unittest discover -s tests
python3 scripts/validate_official_factor_spec.py examples/specs/*.json
```

## 6. 正确性验收定义

一个开发任务只有同时满足下面条件，才可以说“验证为正确”：

1. **落点正确**：改动位于本文件第 1 节规定的 owner repo。
2. **边界正确**：没有把执行层塞回 main repo，没有让 infra 绕过 registry pointer，没有让 community 收 raw evidence。
3. **权限正确**：涉及本地文件、env、外部命令、网络、上传、issue/PR automation 时，有 user approval gate 和 rollback path。
4. **供应链正确**：涉及可安装 factor source 时，有 source pointer、完整性校验、compatibility 和回滚策略；factor contract repo 不承载 pack release 物。
5. **数据正确**：raw session 默认本地；ledger 保存 locator/hash/redacted preview；公开资产已脱敏。
6. **可复现正确**：有 fixture、contract test 或 smoke path 能复现核心行为。
7. **命令正确**：第 5 节相关命令 fresh run 通过；若无法运行，PR 必须说明原因、风险和替代验证。
8. **文档正确**：README、tutorial、SKILL 或 development-direction 中至少有一个入口说明如何使用或继续开发。

最低证据格式：

```text
Changed owner repo: <repo>
User-facing path: <entry command/page/doc>
Verification:
- <command>: pass
- <command>: pass
Boundary checks:
- no raw session committed
- no direct lab install path
- no runtime code in main repo
Rollback:
- <how to disable/delete/revert local state or release pointer>
```

## 7. 不合格示例

下面这些即使测试通过，也不能算正确：

- 在 `EvoZeus` main repo 增加 `scanner.py`、`factor.py`、SQLite schema 或 `.evozeus` bootstrap。
- `evozeus-infra` 直接从 `evozeus-factor-lab/examples` 安装默认 Factor。
- community `/skill` 页面承诺自动扫描本地文件或直接上传 session。
- 把 official pack release、manifest、checksum、SBOM/attestation 放进 `evozeus-factors-official`，混淆 contract repo 与 release repo。
- report dashboard 直接读 provider raw file，不通过 resolver 和 permission gate。
- PR 只说“已验证”，但没有 fresh command output 对应的命令。

## 8. 下一步开发切分

建议按下面 backlog 开独立分支和 PR：

| 顺序 | Repo | 分支建议 | 输出 |
| --- | --- | --- | --- |
| 1 | `10-repos/evozeus-runtime` | `codex/infra-workspace-lockfile` | active workspace/config/lockfile implementation |
| 2 | `10-repos/evozeus-runtime` | `codex/infra-local-ledger` | SQLite Local Analysis Ledger |
| 3 | `10-repos/evozeus-factor-lab` | `codex/python-factor-contract-draft` | Python AbstractFactor contract draft and examples |
| 4 | `10-repos/evozeus-runtime` | `codex/infra-scanner-resolver` | scanner sandbox + resolver contract consumer |
| 5 | `10-repos/evozeus-factors-official` | `codex/python-official-factor-contract` | stable OfficialFactor contract and canonical examples |
| 6 | `10-repos/evozeus` | `codex/default-factor-registry-pointer` | registry pointer schema to approved factor source |
| 7 | `10-repos/evozeus-runtime` | `codex/infra-factor-runner` | Python factor discovery + runner |
| 8 | `10-repos/evozeus-runtime` | `codex/infra-scan-analyze-service` | onboard -> scan -> analyze -> report -> doctor |
| 9 | `10-repos/evozeus-runtime` | `codex/infra-local-surfaces` | CLI/TUI/companion/browser workspace/report |

这些 PR 可以串行推进。不要把第 3 到第 7 步压进一个大 PR；否则很难判断是 protocol、contract 还是 infra consumer 出错。
