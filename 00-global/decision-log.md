# EvoZeus Decision Log

用于记录 EvoZeus 跨 repo 的关键产品、技术和运营决策。

| 日期 | 决策 | 背景 | 影响范围 | Owner | 后续动作 |
| --- | --- | --- | --- | --- | --- |
| 2026-06-14 | EvoZeus 默认采用 static `SKILL.md` 和 zero-install entry | 用户必须能先审阅协议再信任 runtime；raw session 默认不能上传 | EvoZeus 主 repo、官网、未来 runtime | MetaInFlow | 保持 README / SKILL / docs 的 zero-install 承诺 |
| 2026-06-18 | 使用 EvoZeus-MegaRepo 承载全局设计和跨 repo 决策 | EvoZeus 会拆出 community、Factor lab、official packs、runtime 等多个 repo，需要统一索引 | 全部 EvoZeus repo | MetaInFlow | 持续维护 `00-global/repo-index.md`、`decision-log.md`、`material-index.md` |
| 2026-06-18 | Factor library 采用 manifest-driven registry，不把完整因子库塞进主仓库 | 主 repo 要保持轻量；社区贡献会很多；scanner code 有供应链风险 | EvoZeus 主 repo、factor lab、official Factor pack repo、future runtime | MetaInFlow | 在主 repo 合并 ADR-0002、Factor registry governance、schema 和 registry example |
| 2026-06-18 | lab repo 可先占名，但正式开放投稿要等 schema/template/CI gate | 社区共创需要先有上传、审核、上线和回滚机制 | evozeus-factor-lab、evozeus-factors-official | MetaInFlow | 先补主仓库 schema 和校验，再启用 lab；有 reviewed candidates 后启用 official pack repo |
| 2026-06-18 | EvoZeus repo 体系全部建仓并接入 mega repo submodule | 需要统一承载主 repo、前端、Factor lab、official packs 和 future runtime，避免后续资料和代码分散 | 全部 EvoZeus repo | MetaInFlow | 继续补主 repo registry schema、lab PR template、official release manifest 和 runtime trust policy |
| 2026-06-18 | EvoZeus 权限采用 least-privilege team model | 现有组织 team 只有 `0812team` 且为 read 权限，不适合承载 EvoZeus 高权限治理 | 全部 EvoZeus repo | MetaInFlow | 新建 EvoZeus 专用 teams；公开 private repo 前补 public gate、branch protection、CODEOWNERS 和 security review |
| 2026-06-18 | 社区共创入口以 Discord 缓冲层和 public `EvoZeus` 主 repo 为中心 | 现有机制已经在主 repo 提供 Case、Candidate、Factor、RFC issue/PR 路线；`factor-lab` 不应替代主 repo intake | EvoZeus、EvoZeus-community、evozeus-factor-lab、evozeus-factors-official、evozeus-runtime | MetaInFlow | `EvoZeus-community` 尽快 public-read；`factor-lab` 作为下游孵化层，模板和门禁补齐后 public-read / PR-gated |
| 2026-06-18 | 暂不创建独立 `evozeus-skills` repo | 当前 `skills/` 是主 repo 的 protocol / governance surface，和 root `SKILL.md`、ontology、evidence、privacy、PR routing 强耦合 | EvoZeus、future evozeus-skills、evozeus-runtime | MetaInFlow | 等 reviewed/core public Skills 形成独立安装需求、manifest schema 和 release gate 后再评估拆分 |
| 2026-06-18 | 目录结构借鉴 `larksuite/cli` 的 surface / domain / skill references 分层 | `larksuite/cli` 把 cmd、shortcuts、skills、skill-template、quality gates 和 tests 分层清晰，适合 EvoZeus 后续 runtime / skill / factor 组织参考 | 全部 EvoZeus repo | MetaInFlow | 先沉淀 `repo-structure-naming.md`；不立即重排主 repo 或引入 runtime 目录 |
| 2026-06-18 | 主 repo 的 Factor 从内置资产库拆为 public intake + registry pointer | `EvoZeus` 主 repo 已有 Factor issue、Candidate 和 skill 入口，但 `factors/` 不应承载未审 pack、scanner code 或 official release；需要把资产按生命周期路由到 lab / official | EvoZeus、evozeus-factor-lab、evozeus-factors-official、EvoZeus-MegaRepo | MetaInFlow | 主 repo 保留 Factor Candidate 和 registry surface；`factor-lab` 承接 domain/template/schema/check；`factors-official` 承接 manifest/checksum/attestation；后续补主 registry schema |
| 2026-06-18 | mega repo 新增 `docs/` 作为人类可读文档层 | `00-global/` 已承担正式设计和索引，但缺少新人/Agent 可直接阅读的介绍、开发方向和 tutorial 入口 | EvoZeus-MegaRepo | MetaInFlow | `docs/development-direction/` 定义开发方向；`docs/tutorials/` 做各部分 tutorial；`docs/reference/` 维护文档结构规则 |
