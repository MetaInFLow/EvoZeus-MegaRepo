# Tutorial: Factor Lab

## 目标

理解 `10-repos/evozeus-factor-lab` 如何承接 Factor pack / scanner module 孵化。

## 适合谁

- Factor reviewer。
- scanner module 作者。
- 需要把主 repo Factor Candidate 路由到 lab 的 maintainer。

## 前置条件

先读：

- `../../10-repos/evozeus-factor-lab/README.md`
- `../../10-repos/evozeus-factor-lab/checks/README.md`
- `../../10-repos/evozeus-factor-lab/templates/factor-submission.md`
- `../../10-repos/evozeus-factor-lab/templates/scanner-submission.md`

## 操作步骤

1. 从主 repo issue / Candidate PR 接收 maintainer route，不直接接收未分流的普通投稿。
2. 判断 submission 类型：
   - pure Factor metadata。
   - Factor pack。
   - scanner module。
3. 选择 domain：
   - `agent-behavior`
   - `tool-use`
   - `privacy`
   - `environment`
   - `runtime`
4. 按模板补齐 evidence、privacy、when not to use、counterexample。
5. scanner module 必须追加 permission、dependency、sandbox、supply chain review。
6. review 后进入 `reviewed/` 或 `rejected/`，不要只关掉不留原因。

## 产出

- `submissions/`、`reviewed/` 或 `rejected/` 中的结构化记录。
- 如果准备 promotion，给 `evozeus-factors-official` 的 release PR 留出 evidence 和 source review。

## 不要做

- 不要把 lab merge 当作 official release。
- 不要让 runtime 直接消费 lab moving branch。
- 不要把 raw private session 放进 lab。

## 验证

```bash
git diff --check
node -e "JSON.parse(require('fs').readFileSync('schemas/factor-submission.schema.json','utf8')); console.log('factor schema json ok')"
```
