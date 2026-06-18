# Tutorials

- Status: active
- Last updated: 2026-06-18
- Scope: EvoZeus mega repo 各部分入门教程
- Owner: MetaInFlow

本目录放 tutorial，不放正式决策。Tutorial 的目标是让人或 Agent 能完成一个具体动作：理解一个 repo、更新一个索引、提交一个 Factor、推进一次 release、整理一批资料。

## Tutorial 列表

| Tutorial | 适合场景 | 产出 |
| --- | --- | --- |
| [Mega Repo Workspace](mega-repo-workspace.md) | 第一次进入 mega repo，需要知道从哪里改 | 正确定位 docs、global、repos、materials、ops |
| [EvoZeus 主 Repo](evozeus-main-repo.md) | 要改 protocol、docs、schema、governance 或贡献入口 | 小范围主 repo 变更和验证 |
| [Community Frontend](community-frontend.md) | 要推进官网、社区解释层、public docs surface | 内容或前端变更路线 |
| [Factor Lab](factor-lab.md) | 要处理 Factor pack / scanner module 投稿 | lab submission / reviewed / rejected 记录 |
| [Official Factors](official-factors.md) | 要发布 maintainer-promoted Factor pack | manifest、checksum、attestation 和 registry PR |
| [Runtime](runtime.md) | 要规划或实现 future CLI/TUI/local registry | trust-first runtime 变更 |
| [Materials And Ops](materials-and-ops.md) | 要整理资料、会议纪要、Feishu 导出或运营动作 | 有索引、有敏感级别、有后续动作的资料记录 |

## Tutorial 模板

每篇 tutorial 建议包含：

1. 目标：这篇教程帮你完成什么。
2. 适合谁：maintainer、contributor、Agent、ops。
3. 前置条件：需要读哪些文档、确认哪些权限。
4. 操作步骤：按顺序执行。
5. 产出：完成后应该留下些什么。
6. 不要做：常见越界动作。
7. 验证：怎么知道自己没有破坏边界。

## 与 `00-global/` 的关系

- Tutorial 可以解释“怎么做”。
- `00-global/` 记录“为什么这样设计”和“正式事实是什么”。
- Tutorial 不应绕过 `decision-log.md`。如果教程引入新方向、新权限模型、新 repo 拆分或发布规则，必须同步写入 `00-global/decision-log.md`。
