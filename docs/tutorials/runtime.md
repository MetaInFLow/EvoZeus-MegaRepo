# Tutorial: Runtime

## 目标

理解 `10-repos/evozeus-infra` 的未来边界：CLI / TUI / local registry / report generation / selective install。当前阶段先设计 trust policy，不抢跑默认执行能力；旧主 repo runtime prototype 的设计材料已移入 runtime docs，后续实现必须按 runtime 权限模型重新审查。

## 适合谁

- runtime maintainer。
- security reviewer。
- 要设计 scanner / registry consumer 的开发者。

## 前置条件

先读：

- `../../00-global/evozeus-overall-design.md`
- `../../00-global/repo-structure-naming.md`
- `../../10-repos/evozeus-infra/README.md`
- Python Factor contract 规则。

## 操作步骤

1. 先写清楚 runtime 要消费什么：
   - 主 repo protocol / schema。
   - 主 repo registry pointer。
   - factor source pointer 和 contract version。
   - local registry。
   - opt-in scanner。
2. 对每个可执行能力定义权限：
   - 文件读取。
   - 网络访问。
   - 环境变量读取。
   - 文件写入。
   - 外部命令调用。
3. 默认 local-first，不自动上传 raw session。
4. scanner / factor code / MCP / LLM / visualization pack 必须显式启用。
5. runtime 不直接消费 Discord thread、factor lab examples 或未审 source。
6. 任何从旧 prototype 设计意图延伸出的代码，都必须重新声明权限、依赖、sandbox、默认关闭行为和 public install gate。

## 产出

- trust policy。
- permission model。
- local registry / report / scanner 的最小可执行设计。
- runtime migration / rebuild plan，如果本次工作涉及旧 prototype 能力。
- 后续可落到 CLI/TUI 的命令设计。

## 不要做

- 不要默认安装 scanner。
- 不要自动联网或上传。
- 不要绕过 source pointer、contract version、完整性校验和用户确认。

## 验证

当前 runtime 仍是 future shell。设计变更至少需要：

```bash
git diff --check
```

等 runtime 有实现后，再补 build、test、sandbox test 和 dependency audit。
