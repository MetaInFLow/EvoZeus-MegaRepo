# Tutorial: Mega Repo Workspace

## 目标

理解 `EvoZeus-MegaRepo` 的工作区边界，知道新资料、新决策、新 tutorial、新 repo 变更应该放在哪里。

## 适合谁

- 第一次进入 EvoZeus 全局空间的 maintainer。
- 需要跨 repo 修改的 Agent。
- 需要整理资料、决策或运营记录的人。

## 前置条件

先读：

- `../README.md`
- `../../00-global/repo-index.md`
- `../../00-global/evozeus-overall-design.md`

## 操作步骤

1. 先看任务属于哪一类：
   - 改方向：进入 `docs/development-direction/`。
   - 写教程：进入 `docs/tutorials/`。
   - 记录正式决策：进入 `00-global/decision-log.md`。
   - 更新 repo 状态：进入 `00-global/repo-index.md`。
   - 整理资料：进入 `20-materials/`，并更新 `00-global/material-index.md`。
   - 做运营或发布动作：进入 `30-ops/`。
2. 如果要改 submodule，先进入对应 `10-repos/<repo>/` 独立提交。
3. 子 repo 提交后，回到 mega repo 顶层更新 submodule 指针。
4. 如果改动影响全局方向、权限、repo 可见性或发布路线，补 `00-global/decision-log.md`。

## 产出

- 清楚的文档入口或资料记录。
- 必要时有 submodule 指针更新。
- 必要时有 decision log。

## 不要做

- 不要把临时资料直接塞进 `docs/`。
- 不要把未脱敏 raw session、客户资料、secret 放进 public-facing 文档。
- 不要在 mega repo 里直接改业务 repo 文件后忘记进入子 repo 提交。

## 验证

```bash
git status --short --branch
git submodule status
git diff --check
```
