# EvoZeus Mega Repo

EvoZeus 的全局协调工作区：定义方向、组织 repo、保存决策、承接资料和维护跨 repo tutorial。

这个 repo 不是产品入口本身。产品协议入口在 `10-repos/evozeus`；本 repo 是 MetaInFlow 内部用来协调 EvoZeus 全局系统的 operation contract。

```text
direction
  -> repo topology
  -> docs / tutorials
  -> submodule work
  -> decision log
```

## What It Is

`EvoZeus-MegaRepo` 是 EvoZeus 的 private mega workspace。

它负责回答：

- EvoZeus 当前开发方向是什么。
- 每个 repo 承担什么职责。
- 哪些 repo 应该 public / private。
- Factor、runtime、community、official release 如何协同。
- 新资料、会议纪要、Feishu 导出、运营动作应该放哪里。
- 新人或 agent 应该从哪篇 tutorial 开始。

## What It Is Not

本 repo 不承担这些职责：

- 不替代 `EvoZeus` 主 repo 的 public protocol。
- 不接收普通社区贡献。
- 不存 raw private session、客户资料、secret 或未脱敏日志。
- 不直接发布 official Factor pack。
- 不直接运行 runtime scanner。

## Start Here

第一次进入：

1. 读 [Docs 入口](docs/README.md)。
2. 读 [Development Direction](docs/development-direction/README.md)。
3. 按任务进入 [Tutorials](docs/tutorials/README.md)。
4. 查正式事实时读 [EvoZeus 整体设计](00-global/evozeus-overall-design.md) 和 [Decision Log](00-global/decision-log.md)。

初始化所有 submodule：

```bash
git submodule update --init --recursive
```

给 Agent 的最短指令：

```text
Read the root README, docs/README.md, and docs/tutorials/README.md. Identify which EvoZeus repo or workspace area owns the task. Do not change submodules without committing inside the child repo first. Do not store raw private evidence.
```

## Who Should Use This

| Role | Use this repo when | Stop when |
| --- | --- | --- |
| Maintainer | 需要跨 repo 决策、submodule 指针、权限设计 | 变更只属于单一业务 repo |
| Agent | 需要判断任务应该落到哪个 repo / docs / ops | 无法确认 privacy boundary |
| Operator | 需要整理资料、Feishu 导出、发布或权限计划 | 内容应进入 public main repo |
| Product owner | 需要定义开发方向或当前优先级 | 决策没有 owner 或 evidence |

## Task Routes

| 你要做什么 | 去哪里 |
| --- | --- |
| 查全局设计 | `00-global/evozeus-overall-design.md` |
| 查 repo 权限和可见性 | `00-global/repo-index.md` |
| 记录跨 repo 决策 | `00-global/decision-log.md` |
| 理解开发方向 | `docs/development-direction/README.md` |
| 找 tutorial | `docs/tutorials/README.md` |
| 改主 protocol | `10-repos/evozeus` |
| 改官网 | `10-repos/evozeus-community` |
| 处理 Factor lab | `10-repos/evozeus-factor-lab` |
| 发布 official factors | `10-repos/evozeus-factors-official` |
| 规划 runtime | `10-repos/evozeus-runtime` |
| 放资料 / Feishu 导出 | `20-materials/` + `00-global/material-index.md` |
| 放运营 / 发布 / 权限执行 | `30-ops/` |

## Repo Topology

```text
EvoZeus-MegaRepo
  -> EvoZeus                 public protocol / governance
  -> evozeus-community       community surface
  -> evozeus-factor-lab      Factor pack / scanner incubation
  -> evozeus-factors-official official Factor release source
  -> evozeus-runtime         future local runtime
```

## Trust Contract

本 repo 的默认契约：

- private by default。
- raw session 不入仓。
- private customer context 不入仓。
- repo visibility、权限、release、拆 repo 决策必须写入 `decision-log.md`。
- submodule 内容先在子 repo 提交，再更新 mega repo 指针。
- Feishu 相关操作统一使用 `larkcli`。

## Directory Map

| Path | Purpose |
| --- | --- |
| `00-global/` | 全局设计、repo index、material index、decision log、命名和目录规则 |
| `docs/` | 介绍文档、开发方向、tutorial 和文档结构规则 |
| `10-repos/` | EvoZeus 相关 repo 的 submodule 工作区 |
| `20-materials/` | 外部资料、调研、会议纪要、Feishu 导出和素材 |
| `30-ops/` | 社区运营、权限执行、发布操作、迁移和排障记录 |
| `90-archive/` | 冻结上下文、历史版本和过期资料 |

## Current Status

- Repo visibility: private。
- Submodules: active。
- Main public protocol repo: `10-repos/evozeus`。
- Current docs layer: `docs/`。
- Current decision source: `00-global/decision-log.md`。

## Not Promised

- 不保证这里的所有 private 决策都已公开同步。
- 不保证 submodule branch 都是默认可 merge 状态。
- 不保证资料区内容适合公开。
- 不保证 runtime 或 official Factor release 已稳定。

## Validation

```bash
git status --short --branch
git submodule status
git diff --check
```
