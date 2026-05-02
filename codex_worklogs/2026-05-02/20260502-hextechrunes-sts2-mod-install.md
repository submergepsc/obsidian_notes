---
id: 20260502-hextechrunes-sts2-mod-install
name: hextechrunes-sts2-mod-install
slug: hextechrunes-sts2-mod-install
cwd: /home/loviya
summary: "Inspected a WeChat-provided HextechRunes zip for Slay the Spire 2 and identified the safe manual install path."
tags:
  - steam
  - slay-the-spire-2
  - mods
priority: normal
---

# HextechRunes STS2 Mod Install

## Current Snapshot

- status: 已完成
- goal: Explain and complete installation of the local `HextechRunes V0.5.2公开版可用.zip` mod with Steam Slay the Spire 2.
- blocker: 无。
- next: 无；从 Steam 启动游戏检查 modded 状态。
- updated: 2026-05-02 21:07:38 +0800

## Key Results

- Zip path: `/home/loviya/文档/xwechat_files/wxid_s8p1csclabg322_6e01/msg/file/2026-05/HextechRunes V0.5.2公开版可用.zip`
- SHA256: `222743eeefd21f6094eb83c1be1c04f01aee1febf8c0c00e6f83e13aa9e1482a`
- The zip contains `HextechRunes/HextechRunes.json`, `HextechRunes/HextechRunes.pck`, and `HextechRunes/HextechRunes.dll`; `__MACOSX` entries are macOS metadata and are not needed.
- Installed game path: `/home/loviya/.steam/debian-installation/steamapps/common/Slay the Spire 2`
- Steam app id: `2868840`; current Steam branch in manifest: `public-beta`.
- No existing `mods` directory was present in the game folder during inspection.
- After the user's first paste failed because a newline entered the long zip path, the mod was installed directly with the exact quoted path.
- Save/config backup created at `/home/loviya/.local/share/SlayTheSpire2.backup-before-mod`.
- Installed files:
  - `/home/loviya/.steam/debian-installation/steamapps/common/Slay the Spire 2/mods/HextechRunes/HextechRunes.json`
  - `/home/loviya/.steam/debian-installation/steamapps/common/Slay the Spire 2/mods/HextechRunes/HextechRunes.pck`
  - `/home/loviya/.steam/debian-installation/steamapps/common/Slay the Spire 2/mods/HextechRunes/HextechRunes.dll`

## Decisions

- Do not execute the DLL during inspection.
- Recommend preserving the packaged `HextechRunes` folder under the game `mods` directory:
  - `/home/loviya/.steam/debian-installation/steamapps/common/Slay the Spire 2/mods/HextechRunes/HextechRunes.json`
  - `/home/loviya/.steam/debian-installation/steamapps/common/Slay the Spire 2/mods/HextechRunes/HextechRunes.pck`
  - `/home/loviya/.steam/debian-installation/steamapps/common/Slay the Spire 2/mods/HextechRunes/HextechRunes.dll`

## Local Mod Package Was Identified Safely

- updated: 2026-05-02 20:45:49 +0800
- cwd: `/home/loviya`
- source instruction: 使用 WeChat 收到的 `HextechRunes V0.5.2公开版可用.zip` 作为 Steam Slay the Spire 2 mod。
- problem:
  - 用户需要知道 zip 该放到哪里以及如何启用，且 zip 包含可执行 DLL。
- result:
  - 只读检查确认它是 STS2 mod package，给出解压到 Steam 游戏目录 `mods` 文件夹的安装方式和删除方式。
- next:
  - 用户确认来源可信后，解压安装并从 Steam 启动游戏测试。

## Long Path Paste Failed, Direct Install Completed

- updated: 2026-05-02 21:07:38 +0800
- cwd: `/home/loviya`
- source instruction: 用户执行 `unzip -o "$ZIP" 'HextechRunes/*' -d "$GAME/mods"` 后提示找不到 zip。
- problem:
  - 终端错误中的路径在 `V0.5.2` 后出现换行，说明复制长文件名时把换行带进了 `$ZIP`。
- result:
  - 创建游戏 `mods` 目录，备份 `~/.local/share/SlayTheSpire2` 到 `~/.local/share/SlayTheSpire2.backup-before-mod`，并成功解压 `HextechRunes` 文件夹到游戏目录。
- next:
  - 从 Steam 启动 Slay the Spire 2，检查游戏是否显示 modded 状态或提示重启进入 modded mode。

## Explain The Mods Directory Convention

- updated: 2026-05-02 21:24:00 +0800
- cwd: `/home/loviya`
- source instruction: 用户询问为什么知道要在 Slay the Spire 2 目录下建立 `mods`，这是什么规范。
- problem:
  - 需要区分官方/游戏层面的 mod manifest 机制、社区安装说明，以及按 zip 自带目录结构安装的推断。
- result:
  - 公开 STS2 安装说明写明在游戏根目录创建 `mods` 并放入 mod 文件；官方/补丁说明写明当前 mod 结构使用 `<mod_id>.json` manifest，并由 JSON 声明是否包含 PCK/DLL；本机 `sts2.dll` 字符串也包含 `ModsDirectory`、`mods_enabled`、`has_pck`、`has_dll` 等字段。
  - 对于是否每个 mod 一个子文件夹，社区资料不完全统一：有些指南说直接把 `.dll/.pck/.json` 放在 `mods` 根目录；多个 Nexus mod 说明则要求在 `mods` 下创建 mod 专属文件夹并把该 mod 的 dll/pck/json 放进去。
- next:
  - 如果用户遇到游戏不识别该 mod，优先改为把 `HextechRunes.json/.pck/.dll` 放到 `mods` 根目录或按作者说明调整。
