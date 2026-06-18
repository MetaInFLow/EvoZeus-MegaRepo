# Tutorial: Community Frontend

## 目标

理解 `10-repos/evozeus-community` 的作用：它是官网源码、社区解释层和 public deployed surface 的实现仓库，不是正式治理入口本身，也不是 public source repo。

## 适合谁

- 要写官网内容的人。
- 要把 Discord / GitHub contribution route 讲清楚的人。
- 要做 public deployed surface 发布前检查的人。

## 前置条件

先读：

- `../../00-global/evozeus-overall-design.md` 的社区共创机制。
- `../../30-ops/discord-openclaw-governance-plan.md`。
- 主 repo `CONTRIBUTING.md`。

## 操作步骤

1. 确认页面要解决的问题：解释 EvoZeus、引导贡献、展示 docs surface，还是发布公告。
2. 内容必须指向主 repo 的正式入口：
   - Case / Candidate / Factor：主 repo issue / PR。
   - Factor contract / example：maintainer route 到 factor lab 或 official contract repo。
   - Factor pack / scanner：不进 community，也不进 factor contract repo；路由到 runtime 或后续独立发布机制。
   - Governance：主 repo RFC / governance PR。
3. 不在官网收 raw evidence，不在页面里放 private context，也不把 private Web 源码当成公开协议资产来源。
4. 如果链接了 Discord，要说明 Discord 是 PR 前缓冲层，不替代 GitHub governance。
5. 修改后运行前端仓库自己的 build / test / lint。

## 产出

- 一个能解释产品和贡献路线的页面或内容变更。
- 必要时同步更新主 repo docs 或 mega docs。

## 不要做

- 不要让官网变成新的贡献系统。
- 不要绕过主 repo 的 privacy / proof / schema gate。
- 不要把部署 secret 写进 repo。
- 不要把 Web 源码改成 public；用户需要直接复核的内容应同步到 public `EvoZeus` 或公开部署面。

## 验证

```bash
npm run lint
npm run test
npm run build
```

如果某个命令当前尚未配置，记录实际缺口，而不是假设通过。
