---
id: 20260503-hs01-install-hearthstone-lutris
name: install-hearthstone-lutris
slug: install-hearthstone-lutris
cwd: /home/loviya
summary: Use Lutris to install Hearthstone through the current Lutris Hearthstone/Battle.net installer path.
tags:
  - lutris
  - hearthstone
  - battle.net
priority: normal
---

# Install Hearthstone With Lutris

## Current Snapshot

- status: 进行中
- goal: 使用 Lutris 安装炉石传说，并尽量走 Lutris 官方安装脚本。
- blocker: 普通 Codex 命令环境无法打开图形显示 `:0`；实际安装需要启动 Lutris GUI 并由用户在 Battle.net 安装/登录窗口中继续。
- next: 通过 `xdg-open lutris:install/hearthstone-standard` 启动 Lutris 安装器。
- updated: 2026-05-03 12:27:00 +0800

## Key Results

- Lutris 已安装：`/usr/games/lutris`。
- 系统包已具备 Wine 相关基础组件：`lutris 0.5.14-2`、`wine 9.0~repack-4build3`、`wine32`、`wine64`、`winetricks 20240105-2`、`gamemode 1.8.1-2build1`。
- Lutris 官网当前炉石脚本中，`hearthstone-standard` 会创建 64-bit Wine prefix 并安装 Battle.net；`hearthstone-battlenet-launcher` 依赖已有 `battlenet-standard`，主要用于增加炉石启动入口。

## Decisions

- 本机未找到已有 Hearthstone/Battle.net Lutris 安装目录，优先启动 `hearthstone-standard`。
- 不直接使用 `hearthstone-battlenet-launcher`，因为它要求先安装 Battle.net Standard。

## Commands

- `command -v lutris`
- `lutris --version`
- `dpkg-query -W -f='${Package} ${Version} ${Status}\n' lutris wine winetricks wine64 wine32 gamemode mangohud`
- `find /home/loviya -maxdepth 3 -iname '*Hearthstone*' -o -iname '*Battle.net*' -o -iname '*battle*net*'`

## Launch Lutris Hearthstone Installer

- updated: 2026-05-03 12:27:00 +0800
- cwd: `/home/loviya`
- source instruction: `帮我使用lutris安装一下炉石传说`
- problem:
  - 普通命令环境调用 `lutris --version` 会尝试初始化 GTK，因无法访问图形显示而报错。
  - 炉石的 Lutris 安装过程需要下载 Battle.net 安装器，并打开 Windows 安装/登录窗口。
- improvement:
  - 确认依赖已安装，并根据 Lutris 当前脚本选择 `lutris:install/hearthstone-standard`。
- result:
  - 准备通过系统 URL handler 启动 Lutris GUI 安装器。
- next:
  - 启动安装器后，在图形窗口中完成 Battle.net 安装、登录，并在 Battle.net 内安装 Hearthstone。
