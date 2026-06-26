# Tutorial: Session Signal Skill

## 目标

理解 `10-repos/evozeus-session-signal-skill` 如何维护 Session Signal SKILL 和 official factor tools：`SKILL.md` 负责判断什么样的历史记录是高价值的，`factors/<slug>/` 提供可解释、可测试、可被 runtime 调用的 Python tools。

## 适合谁

- 维护高价值 session 判断方法的人。
- 需要新增或校准 official factor tool 的 maintainer。
- 需要确认 FactorResult shape、evidence refs 和 presentation contract 的 reviewer。

## 前置条件

先读：

- `../../10-repos/evozeus-session-signal-skill/README.md`
- `../../10-repos/evozeus-session-signal-skill/SKILL.md`
- `../../10-repos/evozeus-session-signal-skill/src/evozeus_session_signal_skill/factor.py`

## 操作步骤

1. 判断变更属于哪一层：
   - `SKILL.md`：改变如何综合多个 factor tool 的输出，判断是否值得沉淀。
   - `factors/<slug>/`：新增或调整一个具体 factor tool。
   - `src/evozeus_session_signal_skill/factor.py` / schema：改变 Python contract 或 spec shape。
2. 如果改变判断方法，先更新顶层 `SKILL.md`，说明新信号如何影响 `success_skill_candidate`、`problem_skill_candidate`、`failure_skill_candidate`、`repeat_skill_candidate`、`workflow_skill_candidate`、`review_needed` 或 `not_skill_candidate`。
3. 如果改变 factor tool，先更新 `factors/<slug>/FACTOR.xml`，再同步 `factor.py`、`spec.json` 和脱敏 `session.json`。
4. 如果改变 contract，再同步 `schemas/official-factor-spec.schema.json` 和相关 tests。
5. 运行 tests 和 spec validator。

## 产出

- Session Signal SKILL 的判断规则。
- 稳定官方 Python factor tool contract。
- `FACTOR.xml`、spec、canonical examples 和测试向量。

## 不要做

- 不要放真实业务 Factor pack。
- 不要放 release manifest、checksum、SBOM 或 attestation。
- 不要把本 repo 当 runtime 安装源。
- 不要把 examples 或测试向量当默认可安装 factor source。
- 不要记录 private lab promotion state。

## 验证

```bash
git diff --check
python3 -m unittest discover -s tests
python3 scripts/validate_official_factor_spec.py factors/*/spec.json
```
