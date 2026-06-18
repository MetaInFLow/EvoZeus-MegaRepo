# EvoZeus Repo Index

用于记录 EvoZeus 相关 repo 的全局索引。

| Repo | 本地路径 | 类型 | 当前可见性 | 目标可见性 | Owner | 状态 | 权限原则 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EvoZeus-MegaRepo | `EvoZeus-MegaRepo` | mega repo / coordination workspace | private | private | MetaInFLow | active / remote 已创建 | Admin: `evozeus-owners`；Maintain: `evozeus-maintainers`；Read: `metainflow-internal-read` 或 `0812team`。不公开 raw private context。 |
| EvoZeus | `EvoZeus-MegaRepo/10-repos/evozeus` | 主 repo / submodule | public | public | MetaInFLow | active / 已接入 | Admin: `evozeus-owners`；Maintain: `evozeus-maintainers`；Write: `evozeus-protocol-maintainers`；public fork PR。高风险路径需 CODEOWNERS。 |
| EvoZeus-community | `EvoZeus-MegaRepo/10-repos/evozeus-community` | 前端 / 官网 / submodule | private | launch 后 public | MetaInFLow | active / 已接入 | Admin: `evozeus-owners`；Write: `evozeus-community-maintainers`；Read: internal。公开前需内容、secret、部署配置审查。 |
| evozeus-factor-lab | `EvoZeus-MegaRepo/10-repos/evozeus-factor-lab` | Factor / scanner 社区孵化 repo / submodule | private | gate 完成后 public 或 invite-only public | MetaInFLow | active / 已接入 | Admin: `evozeus-owners`；Write: `evozeus-factor-reviewers`；scanner code 必须追加 `evozeus-security-reviewers` review。 |
| evozeus-factors-official | `EvoZeus-MegaRepo/10-repos/evozeus-factors-official` | 官方 Factor pack repo / submodule | private | 首个 stable pack 前 public | MetaInFLow | active / 已接入 | Admin: `evozeus-owners`；Maintain: `evozeus-maintainers` + `evozeus-security-reviewers`；release 必须 tag + manifest + checksum + SBOM。 |
| evozeus-runtime | `EvoZeus-MegaRepo/10-repos/evozeus-runtime` | future runtime repo / submodule | private | alpha/beta 后 public | MetaInFLow | active shell / 已接入 | Admin: `evozeus-owners`；Write: `evozeus-runtime-maintainers`；扫描、上传、联网、插件执行需 security review。 |
