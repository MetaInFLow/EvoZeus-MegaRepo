# Tutorial: Official Factors

## 目标

理解 `10-repos/evozeus-factors-official` 如何发布 maintainer-promoted official Factor packs。

## 适合谁

- release operator。
- Factor maintainer。
- security reviewer。

## 前置条件

先读：

- `../../10-repos/evozeus-factors-official/README.md`
- `../../10-repos/evozeus-factors-official/manifests/README.md`
- `../../10-repos/evozeus-factors-official/scripts/README.md`
- factor lab 中对应 reviewed asset。

## 操作步骤

1. 确认来源是 `evozeus-factor-lab/reviewed/...`，不是普通投稿或 moving private branch。
2. 在 `packs/<pack-id>/` 准备 pack 内容。
3. 在 `manifests/releases/<pack-id>/<version>.yaml` 准备 release manifest。
4. 在 `checksums/<pack-id>/<version>.sha256` 准备 checksum。
5. 在 `attestations/<pack-id>/` 准备 SBOM / attestation。
6. release PR 通过 review 后打 tag。
7. 用 stable manifest reference 更新 `EvoZeus` main registry。

## 产出

- 一个可审计 official release。
- 一个可被主 repo registry 引用的 stable manifest。

## 不要做

- 不要从 lab branch 直接发布。
- 不要无 checksum / SBOM / attestation 发布 scanner 或可执行 pack。
- 不要静默覆盖已经发布的 checksum。

## 验证

```bash
git diff --check
node -e "JSON.parse(require('fs').readFileSync('schemas/release-manifest.schema.json','utf8')); console.log('release manifest schema json ok')"
```
