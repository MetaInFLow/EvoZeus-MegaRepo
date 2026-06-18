# Tutorial: Official Factors

## 目标

理解 `10-repos/evozeus-factors-official` 如何维护稳定 Python `OfficialFactor` contract、官方 spec 和 canonical examples。

## 适合谁

- Factor contract maintainer。
- 需要稳定官方 API 的 runtime 开发者。
- 需要确认 FactorResult shape 的 reviewer。

## 前置条件

先读：

- `../../10-repos/evozeus-factors-official/README.md`
- `../../10-repos/evozeus-factors-official/SKILL.md`
- `../../10-repos/evozeus-factors-official/src/evozeus_factors_official/factor.py`

## 操作步骤

1. 判断变更是否属于 official contract，而不是业务 factor pack release。
2. 修改 Python `OfficialFactor` 抽象类。
3. 同步修改 `schemas/official-factor-spec.schema.json`。
4. 更新 `examples/factors/` 中的 canonical Python examples。
5. 更新 `examples/specs/` 中的官方 spec 示例。
6. 运行 tests 和 spec validator。

## 产出

- 稳定官方 Python Factor 抽象类。
- 官方 Factor spec schema。
- canonical examples 和测试向量。

## 不要做

- 不要放真实业务 Factor pack。
- 不要放 release manifest、checksum、SBOM 或 attestation。
- 不要把本 repo 当 runtime 安装源。
- 不要记录 lab promotion state。

## 验证

```bash
git diff --check
python3 -m unittest discover -s tests
python3 scripts/validate_official_factor_spec.py examples/specs/*.json
```
