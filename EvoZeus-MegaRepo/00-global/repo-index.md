# EvoZeus Repo Index

用于记录 EvoZeus 相关 repo 的全局索引。

| Repo | 本地路径 | 类型 | 当前可见性 | 目标可见性 | Owner | 状态 | 权限原则 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EvoZeus-MegaRepo | `EvoZeus-MegaRepo` | mega repo / coordination workspace | private | private | MetaInFLow | active / remote 已创建 | 内部协调层。Admin: `evozeus-owners`；Maintain: `evozeus-maintainers`；Read: `metainflow-internal-read` 或 `0812team`。不公开 raw private context。 |
| EvoZeus | `EvoZeus-MegaRepo/10-repos/evozeus` | 主 repo / public intake / submodule | public | public | MetaInFLow | active / 已接入 | 社区共创主入口。Admin: `evozeus-owners`；Maintain: `evozeus-maintainers`；Write: `evozeus-protocol-maintainers` + `evozeus-factor-maintainers`；Triage: `evozeus-triagers`；外部贡献走 issue/fork PR。 |
| EvoZeus-community | `EvoZeus-MegaRepo/10-repos/evozeus-community` | 前端 / 官网 / submodule | private | 尽快 public-read | MetaInFLow | active / 已接入 | 官网和贡献路线入口。Admin: `evozeus-owners`；Write: `evozeus-community-maintainers`；公开前需无 secret、部署配置隔离、链接主 repo intake。 |
| evozeus-factor-lab | `EvoZeus-MegaRepo/10-repos/evozeus-factor-lab` | Factor / scanner 孵化 repo / submodule | private | 模板和门禁后 public-read / PR-gated | MetaInFLow | active / 已接入 | 只承接 Factor pack、scanner module、实验性 reviewed/rejected 孵化，不是普通 Case 入口。Write: `evozeus-factor-maintainers`；scanner code 必须 `evozeus-security-reviewers` review。 |
| evozeus-factors-official | `EvoZeus-MegaRepo/10-repos/evozeus-factors-official` | 官方 Factor pack repo / submodule | private | 首个 official pack 前 public-read | MetaInFLow | active / 已接入 | official release 源。Maintain: `evozeus-maintainers` + `evozeus-security-reviewers`；只接 promotion PR；release 必须 tag + manifest + checksum + SBOM。 |
| evozeus-runtime | `EvoZeus-MegaRepo/10-repos/evozeus-runtime` | future runtime repo / submodule | private | trust policy 稳定后 public-read | MetaInFLow | active shell / 已接入 | 可执行 runtime，最终需要可审计。Write: `evozeus-runtime-maintainers`；扫描、上传、联网、插件执行需 security review。 |
| evozeus-skills | 待定 | future skill distribution repo | 不创建 | 条件成熟后 public-read / PR-gated | MetaInFLow | deferred | 当前不建仓。root `SKILL.md` 和 scenario skills 继续留在 `EvoZeus` 主 repo；只有 reviewed/core public Skills 形成独立安装需求后再拆。 |
