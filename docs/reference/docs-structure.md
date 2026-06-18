# Docs Structure

- Status: active
- Last updated: 2026-06-18
- Scope: `docs/` 的结构、命名和维护规则
- Owner: MetaInFlow

## 1. 目录设计

```text
docs/
  README.md
  development-direction/
    README.md
    skill-system-implementation.md
  tutorials/
    README.md
    user-journey.md
    mega-repo-workspace.md
    evozeus-main-repo.md
    community-frontend.md
    factor-lab.md
    official-factors.md
    runtime.md
    materials-and-ops.md
  reference/
    docs-structure.md
    skill-coverage.md
```

## 2. 每层职责

| 路径 | 职责 | 不放什么 |
| --- | --- | --- |
| `docs/README.md` | mega repo 介绍、导航、阅读顺序 | 具体 repo 的长教程 |
| `development-direction/` | 当前阶段开发方向、优先级、完成标准 | 临时会议纪要、操作流水 |
| `tutorials/` | 每个部分怎么开始、怎么产出、怎么验证 | 正式决策底账 |
| `reference/` | 文档结构、命名、维护规则、Skill 覆盖矩阵 | 产品方向判断 |
| `00-global/` | 正式全局设计、索引、决策记录 | 面向新人阅读的教程正文 |
| `20-materials/` | 原始资料、调研、导出、会议纪要 | 已整理成正式方向的文档 |
| `30-ops/` | 运营、权限、发布、迁移、排障 | 产品介绍和 tutorial |

## 3. 命名规则

- 文件名使用 lower kebab-case：`factor-lab.md`。
- 目录名使用语义名称，不用 `misc`、`temp`、`new`。
- tutorial 文件名以对象命名，不加 `tutorial-` 前缀，因为目录已经表达类型。
- 方向文档优先用稳定主题命名，例如 `README.md`、`current-focus.md`、`release-sequence.md`。

## 4. 文档边界

写文档前先判断：

| 你要写的是 | 放哪里 |
| --- | --- |
| 这个系统是什么、从哪里读 | `docs/README.md` |
| 当前阶段先做什么 | `docs/development-direction/` |
| 某个部分怎么操作 | `docs/tutorials/` |
| 文档结构怎么维护 | `docs/reference/` |
| 正式架构、权限、repo index、decision log | `00-global/` |
| 外部资料、Feishu 导出、会议纪要 | `20-materials/` |
| 发布、运营、权限执行计划 | `30-ops/` |

## 5. 更新规则

- 新增 repo：更新 `00-global/repo-index.md`，必要时新增 tutorial。
- 改开发方向：更新 `development-direction/README.md` 和 `00-global/decision-log.md`。
- 改权限、visibility、release、repo 拆分：必须更新 `00-global/decision-log.md`。
- 新增资料：更新 `00-global/material-index.md`。
- 新增 tutorial：在 `tutorials/README.md` 加入口。

## 6. Tutorial 最小标准

每篇 tutorial 至少包含：

- 目标。
- 适合谁。
- 前置条件。
- 操作步骤。
- 产出。
- 不要做。
- 验证。

没有验证步骤的文档，不算完成的 tutorial。
