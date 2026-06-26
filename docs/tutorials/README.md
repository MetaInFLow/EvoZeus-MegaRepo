# Tutorials

- Status: active
- Last updated: 2026-06-19
- Scope: EvoZeus mega repo 各部分入门教程
- Owner: MetaInFlow

本目录放 tutorial，不放正式决策。Tutorial 的目标是让人或 Agent 能完成一个具体动作：理解一个 repo、更新一个索引、维护 Session Signal SKILL / official factor tools、整理一批资料。

## Tutorial 列表

| Tutorial | 适合场景 | 产出 |
| --- | --- | --- |
| [Mega Repo Workspace](mega-repo-workspace.md) | 第一次进入 mega repo，需要知道从哪里改 | 正确定位 docs、global、repos、materials、ops |
| [User Journey](user-journey.md) | 要理解从注册、Start Here 到 judgment、沉淀和开发分流 | 用户旅程和 repo 路由判断 |
| [EvoZeus 主 Repo](evozeus-main-repo.md) | 要改 protocol、docs、schema、governance 或贡献入口 | 小范围主 repo 变更和验证 |
| [Web Frontend](web-frontend.md) | 要推进官网部署面、社区解释层、`/skill` 路由 | private Web 源码变更和公开内容同步路线 |
| [Session Signal Skill](session-signal-skill.md) | 要维护 Session Signal SKILL 或 official factor tools | `SKILL.md` 方法层、`OfficialFactor`、官方 schema、canonical examples |
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
