# Tutorial: Materials And Ops

## 目标

理解如何整理 `20-materials/` 和 `30-ops/`，避免资料、会议纪要、Feishu 导出、运营动作和发布记录散落。

## 适合谁

- 整理外部资料的人。
- 维护 Feishu 导出的人。
- 做社区运营、权限执行、发布或迁移记录的人。

## 前置条件

先读：

- `../../00-global/material-index.md`
- `../../30-ops/discord-openclaw-governance-plan.md`

## 操作步骤

1. 判断内容类型：
   - 外部资料、调研、会议纪要、Feishu 导出：放 `20-materials/`。
   - 社区运营、权限执行、发布、迁移、排障：放 `30-ops/`。
2. 给资料补最小 metadata：
   - 来源。
   - 日期。
   - 敏感级别。
   - owner。
   - 后续动作。
3. 更新 `00-global/material-index.md`。
4. 如果资料改变了产品方向或 repo 决策，更新 `00-global/decision-log.md`。
5. Feishu 相关操作用 `larkcli`。

## 产出

- 可追溯资料。
- 有索引、有敏感级别、有后续动作。
- 必要时有 decision log。

## 不要做

- 不要把客户资料或 private context 放进 public docs。
- 不要只存附件不写来源。
- 不要把临时运营记录混进 development direction。

## 验证

```bash
git diff --check
```
