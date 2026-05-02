---
id: 20260502-4a9f-wine-tool-lookup
name: wine-tool-lookup
slug: wine-tool-lookup
cwd: /home/loviya
summary: Looked up the previously installed Wine management tool and verified its installed command path.
tags:
  - wine
  - lutris
  - lookup
priority: normal
---

# Wine Tool Lookup

## Current Snapshot

- status: 已完成
- goal: 找回之前下载/安装过的 Wine 管理工具名称。
- blocker: 无
- next: 无；从应用菜单启动 Lutris，或在图形终端运行 `/usr/games/lutris`。
- updated: 2026-05-02 22:32:33 +0800

## Key Results

- 之前安装的 Wine 管理工具是 `Lutris`。
- 相关旧 worklog 是 `/home/loviya/.codex/worklogs/2026-05-01/20260501-8f7c-install-lutris.md`。
- 当前系统仍安装 `lutris 0.5.14-2`，命令路径是 `/usr/games/lutris`。
- `wine` 和 `winetricks` 也仍在系统中：`/usr/bin/wine`、`/usr/bin/winetricks`。

## Commands

- `rg -n -i "wine|bottles|lutris|winetricks|proton|crossover|playonlinux" /home/loviya/.codex/worklogs /home/loviya/.codex/continue.md`
- `dpkg-query -W -f='${Package} ${Version} ${Status}\n' lutris wine winetricks`
- `command -v lutris wine winetricks proton proton-viewer`

## Notes

- `Watt Toolkit` 也存在桌面入口，但它是 Steam/网络工具，不是这次问题里最匹配的 Wine 管理工具。
