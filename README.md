# EvoZeus Mega Repo

本空间用于统一处理 EvoZeus 全局所有 repo、资料、运行记录和跨项目决策。

归属：metainflow private  
定位：EvoZeus 全局工作区 / mega repo
远程：`https://github.com/MetaInFLow/EvoZeus-MegaRepo.git`

## 目录结构

- `00-global/`：全局索引、架构、策略、跨 repo 约定与总览文档。
- `docs/`：介绍文档、开发方向和各部分 tutorial。
- `10-repos/`：各业务 repo 的本地工作副本、submodule、mirror 或 repo 索引。
- `20-materials/`：需求、调研、会议纪要、Feishu 导出资料、客户资料与附件。
- `30-ops/`：运行维护、脚本、任务记录、发布与排障资料。
- `90-archive/`：历史版本、过期资料、冻结项目与不再活跃的上下文。

## 工作原则

1. 项目产出文件默认使用中文；关键专有名词、专业名词可以保留英文。
2. Feishu 相关操作统一使用 `larkcli`。
3. 涉及 private 信息、客户信息、商业资料时，默认只在 metainflow private 范围内处理。
4. 新增 repo 或资料时，优先补充索引，避免只堆文件不留上下文。

## 建议索引

后续可以在 `00-global/` 中补充：

- `repo-index.md`：记录所有 EvoZeus 相关 repo 的用途、路径、owner、状态。
- `material-index.md`：记录资料来源、主题、更新时间、敏感级别。
- `decision-log.md`：记录跨 repo 的关键技术和产品决策。

## 当前核心文档

- [Docs 入口](docs/README.md)
- [Development Direction](docs/development-direction/README.md)
- [Tutorials](docs/tutorials/README.md)
- [Docs Structure](docs/reference/docs-structure.md)
- [EvoZeus 整体设计](00-global/evozeus-overall-design.md)
- [Repo Structure And Naming](00-global/repo-structure-naming.md)
- [Repo Index](00-global/repo-index.md)
- [Decision Log](00-global/decision-log.md)
- [Material Index](00-global/material-index.md)

## 当前 Repo 体系

- `10-repos/evozeus`：核心 protocol、`SKILL.md`、docs、schemas、governance。
- `10-repos/evozeus-community`：前端 / 官网 / 社区解释层。
- `10-repos/evozeus-factor-lab`：Factor 和 scanner 投稿孵化。
- `10-repos/evozeus-factors-official`：官方 Factor packs、release manifests、checksums、attestations。
- `10-repos/evozeus-runtime`：未来 runtime，承接 CLI / TUI / local registry / reports / selective install。

## Submodule

初始化或更新所有 repo：

```bash
git submodule update --init --recursive
```

新增 EvoZeus repo 时，默认放入 `10-repos/`，并同步更新 `00-global/repo-index.md`。

新增教程或开发方向文档时，默认放入 `docs/`，并按 [Docs Structure](docs/reference/docs-structure.md) 更新导航。
