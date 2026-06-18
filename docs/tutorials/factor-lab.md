# Tutorial: Factor Lab

## 目标

理解 `10-repos/evozeus-factor-lab` 如何维护 Python Factor contract 草案、spec 和 examples。

## 适合谁

- Factor contract 作者。
- 需要改 `AbstractFactor` API 的开发者。
- 需要补 Factor 示例和测试向量的 maintainer。

## 前置条件

先读：

- `../../10-repos/evozeus-factor-lab/README.md`
- `../../10-repos/evozeus-factor-lab/SKILL.md`
- `../../10-repos/evozeus-factor-lab/src/evozeus_factor_lab/factor.py`

## 操作步骤

1. 判断改动是否真的是 Factor contract，而不是业务 Factor 或 scanner。
2. 如果改抽象 API，先改 `src/evozeus_factor_lab/factor.py`。
3. 如果改 spec shape，同步改 `schemas/factor-spec.schema.json`。
4. 用 `examples/factors/` 补 Python 示例。
5. 用 `examples/specs/` 补 JSON spec 示例。
6. 用 `examples/sessions/` 放脱敏测试输入。
7. 运行 contract tests 和 spec validator。

## 产出

- Python `AbstractFactor` contract。
- Factor spec schema。
- 可运行、可复核、非业务化的 examples。

## 不要做

- 不要放真实业务 Factor pack。
- 不要放 scanner module。
- 不要创建 `submissions/`、`reviewed/`、`rejected/`。
- 不要把 examples 当成 runtime 默认安装源。

## 验证

```bash
git diff --check
python3 -m unittest discover -s tests
python3 scripts/validate_factor_spec.py examples/specs/*.json
```
