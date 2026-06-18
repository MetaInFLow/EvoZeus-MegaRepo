# Tutorial: EvoZeus 主 Repo

## 目标

理解什么时候应该修改 `10-repos/evozeus`，以及如何保持主 repo 的 public protocol / governance 边界。

## 适合谁

- 要改 `SKILL.md`、docs、schema、governance、issue/PR template 的 maintainer。
- 要提交 Case / Candidate / Factor proposal 的 contributor。
- 要让 Agent 评估当前 session 的用户。

## 前置条件

先读主 repo 内：

- `README.md`
- `CONTRIBUTING.md`
- `docs/reference/ontology.md`
- `docs/governance/pr-routing-policy.md`

## 操作步骤

1. 判断改动层级：
   - semantic：ontology、verdict、evidence、schema。
   - governance：PR routing、privacy、proof、labels、CODEOWNERS。
   - docs/example：README、example cases、report templates。
2. 保持 PR 小范围，不混合 runtime code、governance、docs 和 community Case。
3. Factor 相关改动先问：这是 Candidate / registry pointer，还是 pack / scanner？
   - Candidate / registry pointer 留在主 repo。
   - pack / scanner 路由到 `evozeus-factor-lab`。
   - official release 路由到 `evozeus-factors-official`。
4. 修改后运行主 repo 校验。

## 产出

- 一个小范围、可 review 的 public protocol / governance 变更。
- 必要时更新 mega repo 的 `00-global/decision-log.md`。

## 不要做

- 不要把 executable Factor pack 或 scanner module 放进主 repo。
- 不要上传 raw private session。
- 不要把社区共创等同于给 contributor repo write 权限。

## 验证

```bash
git diff --check
python3 scripts/check_pr_ready.py --allow-cross-layer
```

如果本地 Python 环境异常，可以先用等价静态检查覆盖 branch、PR template、required governance files 和 skill frontmatter，并在提交说明里记录限制。
