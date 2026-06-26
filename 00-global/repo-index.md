# EvoZeus Repo Index

用于记录 EvoZeus 相关 repo 的全局索引。

| Repo | 本地路径 | 类型 | 当前可见性 | 目标可见性 | Owner | 状态 | 权限原则 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EvoZeus-MegaRepo | `EvoZeus-MegaRepo` | mega repo / coordination workspace | public | public | MetaInFlow | active / remote 已创建 / 可公开 | 公开协调层。Admin: `evozeus-owners`；Maintain: `evozeus-maintainers`；外部只读。raw private context、客户资料、secret 和未脱敏 evidence 不入仓。 |
| EvoZeus | `10-repos/evozeus` | canonical protocol / public intake / registry pointer / submodule | public | public | MetaInFlow | active / 已接入；执行层遗留已从主 repo 清理，runtime 设计材料和 prototype 已移至 `evozeus-infra` | 社区共创主入口和治理事实源。只拥有 protocol、ontology、schema、governance、Case/Candidate lifecycle、semantic artifact 和 official registry pointer；不拥有 runtime 执行层、scanner implementation、installable Factor tools 或本地状态。Admin: `evozeus-owners`；Maintain: `evozeus-maintainers`；Write: `evozeus-protocol-maintainers` + `evozeus-factor-maintainers`；Triage: `evozeus-triagers`；外部贡献走 issue/fork PR。 |
| evozeus-web | `10-repos/evozeus-web` | Web frontend source / 官网部署源 / submodule | private | private source / public deployed surface | MetaInFlow | active / 已接入 | Web 源码不公开；用户只访问 Vercel 部署面、`/skill` 和公开 docs。Admin: `evozeus-owners`；Write: `evozeus-web-maintainers`；不得把 secret、客户资料或 raw evidence 写入源码。 |
| evozeus-session-signal-skill | `10-repos/evozeus-session-signal-skill` | Session Signal SKILL / factor tools / submodule | private | public before official method/tool distribution | MetaInFlow | active / 已接入 / `SKILL.md` + official factor tools | official 表示一套可解释、可校准的高价值 session 判断方法。顶层 `SKILL.md` 是超级 SKILL，`factors/<slug>/` 是它调用和解释的 tools；不再把本 repo 定义为 pack release、promotion queue 或单纯 contract repo。Maintain: `evozeus-maintainers` + `evozeus-factor-maintainers`。 |
| EvoZeus-wrapper | `10-repos/EvoZeus-wrapper` | static SKILL wrapper harness / submodule | public | public | MetaInFlow | active seed / 已创建 / 已接入 | 只负责静态 `SKILL.md` 的 case、run card、evaluation notes 和 evolution proposal；不拥有 runtime 执行、scanner、ledger、Session Signal 方法或 official factor tools。Maintain: `evozeus-maintainers`；涉及执行能力必须路由到 `evozeus-infra`。 |
| evozeus-infra | `10-repos/evozeus-infra` | future infra repo / submodule | private | public before user-installable runtime | MetaInFlow | active shell / 已接入 | 可执行 runtime 面向用户前必须可审计。Write: `evozeus-infra-maintainers`；扫描、上传、联网、插件执行需 security review；未稳定前不提供用户安装入口。 |
| evozeus-skills | 待定 | future skill distribution repo | 不创建 | 条件成熟后 public-read / PR-gated | MetaInFlow | deferred | 当前不建仓。root `SKILL.md` 和 scenario skills 继续留在 `EvoZeus` 主 repo；只有 reviewed/core public Skills 形成独立安装需求后再拆。 |

## Removed From Active Mega Repo

| Repo | 状态 | 说明 |
| --- | --- | --- |
| evozeus-factor-lab | private / removed from mega repo submodules | Lab 不再作为公开协作路径或 active component repo。历史 contract 实验可在 private repo 内保留，但新的高价值记录判断、official 方法和 factor tools 进入 `evozeus-session-signal-skill` 或 `EvoZeus` 主 repo。 |
