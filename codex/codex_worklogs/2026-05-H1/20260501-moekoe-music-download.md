---
id: 20260501-moekoe-music-download
name: MoeKoe Music download
slug: moekoe-music-download
cwd: /home/loviya
summary: 下载 MoeKoeMusic GitHub 仓库和最新 Linux AppImage 发行版。
tags:
  - github
  - download
  - moekoemusic
priority: normal
---

# MoeKoe Music 下载

## 当前快照

- 状态: 已完成
- 目标: 下载 MoeKoe Music，并让它更容易启动。
- 阻塞: 无。
- 下一步: 无；`music` works in new shells, and stale shells pointing at `/home/loviya/下载/...` are covered by a compatibility symlink.
- 更新时间: 2026-05-02 04:00:12 +0800

## 关键结果

- Cloned the source repository to `/home/loviya/MoeKoeMusic`.
- Initialized the `api` submodule at commit `9dca97a0cfc201db568b5f37366190e3271a97e7`.
- Downloaded latest Linux AppImage release `v1.6.2` to `/home/loviya/Downloads/MoeKoe_Music_v1.6.2.AppImage`.
- Set executable permissions on the AppImage.
- Corrected `music` alias in `/home/loviya/.bashrc` and added it to `/home/loviya/.zshrc`.
- The mistaken `musi` alias remains as an extra shortcut and points to the same AppImage.
- 已新增 compatibility symlink `/home/loviya/下载/MoeKoe_Music_v1.6.2.AppImage` -> `/home/loviya/Downloads/MoeKoe_Music_v1.6.2.AppImage` for stale already-open shells.
- Verified AppImage SHA256:
  - `79d1f1b99e81f659db3b5bce9301c4c8d8703ac5c62d4de1f8cbe9198d305718`

## 下载 MoeKoeMusic From GitHub

- 更新时间: 2026-05-02 03:04:04 +0800
- 工作目录: `/home/loviya`
- 来源指令: `https://github.com/MoeKoeMusic/MoeKoeMusic去这个网站下载一下`
- 问题:
  - 用户询问 to download a GitHub project and did not specify whether they wanted source code or an installer.
- 改进:
  - Downloaded both the repository source and the latest Linux AppImage release package.
- 结果:
  - Source directory: `/home/loviya/MoeKoeMusic`
  - AppImage: `/home/loviya/Downloads/MoeKoe_Music_v1.6.2.AppImage`
- 下一步:
  - 无。

## Correct music alias

- 更新时间: 2026-05-02 03:10:01 +0800
- 工作目录: `/home/loviya`
- 来源指令: `你搞错了,是music`
- 问题:
  - The previous alias edit added `musi`, but the intended command was `music`.
  - Existing bash `music` pointed to `/home/loviya/下载/MoeKoe_Music_v1.6.2.AppImage`, which was not the downloaded file path.
- 改进:
  - 已更新 bash `music` to `/home/loviya/Downloads/MoeKoe_Music_v1.6.2.AppImage`.
  - 已新增 the same `music` alias to zsh.
- 结果:
  - New bash/zsh shells can launch MoeKoe Music 带 `music`.
  - `musi` also remains available as an extra alias.
- 下一步:
  - Existing shells should run `source ~/.bashrc` or open a new terminal before 使用 `music`.

## Support Stale music alias Path

- 更新时间: 2026-05-02 04:00:12 +0800
- 工作目录: `/home/loviya`
- 来源指令: `music ... 没有那个文件或目录 ... 这为什么`
- 问题:
  - The user's already-open bash session still had the old `music` alias loaded, pointing to `/home/loviya/下载/MoeKoe_Music_v1.6.2.AppImage`.
  - Bash aliases are expanded from the current shell's memory and do not automatically update when `.bashrc` is edited.
  - Linux command names are case-sensitive, so `MUSIC` is not the same command as `music`.
- 改进:
  - 已确认 `.bashrc` and `.zshrc` now point `music` and `musi` at `/home/loviya/Downloads/MoeKoe_Music_v1.6.2.AppImage`.
  - 已创建 a compatibility symlink at the old Chinese `下载` path so stale shells can still launch the AppImage.
- 结果:
  - `/home/loviya/下载/MoeKoe_Music_v1.6.2.AppImage` now resolves to the real AppImage in `/home/loviya/Downloads/`.
  - Existing shells can either run `music` as-is or refresh 带 `source ~/.bashrc`.
- 下一步:
  - 无。
