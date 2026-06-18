# Tutorial: Community Frontend

## 目标

理解 `10-repos/evozeus-community` 的作用：它是官网、社区解释层和 public docs surface，不是正式治理入口本身。

## 适合谁

- 要写官网内容的人。
- 要把 Discord / GitHub contribution route 讲清楚的人。
- 要做 public launch 前检查的人。

## 前置条件

先读：

- `../../00-global/evozeus-overall-design.md` 的社区共创机制。
- `../../30-ops/discord-openclaw-governance-plan.md`。
- 主 repo `CONTRIBUTING.md`。

## 操作步骤

1. 确认页面要解决的问题：解释 EvoZeus、引导贡献、展示 docs surface，还是发布公告。
2. 内容必须指向主 repo 的正式入口：
   - Case / Candidate / Factor：主 repo issue / PR。
   - Factor pack / scanner：maintainer route 到 factor lab。
   - Governance：主 repo RFC / governance PR。
3. 不在官网收 raw evidence，不在页面里放 private context。
4. 如果链接了 Discord，要说明 Discord 是 PR 前缓冲层，不替代 GitHub governance。
5. 修改后运行前端仓库自己的 build / test / lint。

## 产出

- 一个能解释产品和贡献路线的页面或内容变更。
- 必要时同步更新主 repo docs 或 mega docs。

## 不要做

- 不要让官网变成新的贡献系统。
- 不要绕过主 repo 的 privacy / proof / schema gate。
- 不要把部署 secret 写进 repo。

## 验证

```bash
npm run lint
npm run test
npm run build
```

如果某个命令当前尚未配置，记录实际缺口，而不是假设通过。
