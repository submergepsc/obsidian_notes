---
id: 20260501-moekoe-music-download
name: MoeKoe Music download
slug: moekoe-music-download
cwd: /home/loviya
summary: Downloaded the MoeKoeMusic GitHub repository and latest Linux AppImage release.
tags:
  - github
  - download
  - moekoemusic
priority: normal
---

# MoeKoe Music Download

## Current Snapshot

- status: 已完成
- goal: Download and make MoeKoe Music easy to launch.
- blocker: 无。
- next: 无；`music` works in new shells, and stale shells pointing at `/home/loviya/下载/...` are covered by a compatibility symlink.
- updated: 2026-05-02 04:00:12 +0800

## Key Results

- Cloned the source repository to `/home/loviya/MoeKoeMusic`.
- Initialized the `api` submodule at commit `9dca97a0cfc201db568b5f37366190e3271a97e7`.
- Downloaded latest Linux AppImage release `v1.6.2` to `/home/loviya/Downloads/MoeKoe_Music_v1.6.2.AppImage`.
- Set executable permissions on the AppImage.
- Corrected `music` alias in `/home/loviya/.bashrc` and added it to `/home/loviya/.zshrc`.
- The mistaken `musi` alias remains as an extra shortcut and points to the same AppImage.
- Added compatibility symlink `/home/loviya/下载/MoeKoe_Music_v1.6.2.AppImage` -> `/home/loviya/Downloads/MoeKoe_Music_v1.6.2.AppImage` for stale already-open shells.
- Verified AppImage SHA256:
  - `79d1f1b99e81f659db3b5bce9301c4c8d8703ac5c62d4de1f8cbe9198d305718`

## Download MoeKoeMusic From GitHub

- updated: 2026-05-02 03:04:04 +0800
- cwd: `/home/loviya`
- source instruction: `https://github.com/MoeKoeMusic/MoeKoeMusic去这个网站下载一下`
- problem:
  - The user asked to download a GitHub project and did not specify whether they wanted source code or an installer.
- improvement:
  - Downloaded both the repository source and the latest Linux AppImage release package.
- result:
  - Source directory: `/home/loviya/MoeKoeMusic`
  - AppImage: `/home/loviya/Downloads/MoeKoe_Music_v1.6.2.AppImage`
- next:
  - 无。

## Correct music Alias

- updated: 2026-05-02 03:10:01 +0800
- cwd: `/home/loviya`
- source instruction: `你搞错了,是music`
- problem:
  - The previous alias edit added `musi`, but the intended command was `music`.
  - Existing bash `music` pointed to `/home/loviya/下载/MoeKoe_Music_v1.6.2.AppImage`, which was not the downloaded file path.
- improvement:
  - Updated bash `music` to `/home/loviya/Downloads/MoeKoe_Music_v1.6.2.AppImage`.
  - Added the same `music` alias to zsh.
- result:
  - New bash/zsh shells can launch MoeKoe Music with `music`.
  - `musi` also remains available as an extra alias.
- next:
  - Existing shells should run `source ~/.bashrc` or open a new terminal before using `music`.

## Support Stale music Alias Path

- updated: 2026-05-02 04:00:12 +0800
- cwd: `/home/loviya`
- source instruction: `music ... 没有那个文件或目录 ... 这为什么`
- problem:
  - The user's already-open bash session still had the old `music` alias loaded, pointing to `/home/loviya/下载/MoeKoe_Music_v1.6.2.AppImage`.
  - Bash aliases are expanded from the current shell's memory and do not automatically update when `.bashrc` is edited.
  - Linux command names are case-sensitive, so `MUSIC` is not the same command as `music`.
- improvement:
  - Confirmed `.bashrc` and `.zshrc` now point `music` and `musi` at `/home/loviya/Downloads/MoeKoe_Music_v1.6.2.AppImage`.
  - Created a compatibility symlink at the old Chinese `下载` path so stale shells can still launch the AppImage.
- result:
  - `/home/loviya/下载/MoeKoe_Music_v1.6.2.AppImage` now resolves to the real AppImage in `/home/loviya/Downloads/`.
  - Existing shells can either run `music` as-is or refresh with `source ~/.bashrc`.
- next:
  - 无。
