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
