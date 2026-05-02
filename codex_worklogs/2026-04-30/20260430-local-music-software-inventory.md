---
id: 20260430-local-music-software-inventory
name: local-music-software-inventory
slug: local-music-software-inventory
cwd: /home/loviya
summary: 盘点本机已存在的音乐播放器、媒体播放器和相关安装包。
tags:
  - local-software
  - music
  - inventory
priority: normal
---

# Local Music Software Inventory

## Current Snapshot

- status: 已完成
- goal: 找出本机存在的音乐软件和相关线索。
- blocker: 无。
- next: 无。
- updated: 2026-04-30 21:22:00 +0800

## Key Results

- APT/dpkg 已安装 `rhythmbox` 3.4.7、`com.kugou.spark` 20.0.52.27315spark8、`totem` 43.0。
- Snap 路径和桌面入口显示存在 `/snap/bin/spotify`、`/snap/bin/vlc`，对应桌面入口在 `/var/lib/snapd/desktop/applications/`。
- `~/apps/music/` 和 `~/下载/` 均有酷狗安装包 `com.kugou.spark_20.0.52.27315spark8_all.deb`。
- 用户配置目录存在 `~/.config/MoeKoe Music` 和 `~/.config/moekoemusic`，但未发现 MoeKoe Music 的桌面入口或可执行命令。
- `~/.opencli/spotify.env` 是 Spotify 相关配置线索，不是播放器安装本体。

## 本机音乐软件盘点

- updated: 2026-04-30 21:22:00 +0800
- cwd: `/home/loviya`
- source instruction: `找一下本机存在的音乐软件`
- problem:
  - 用户需要知道当前机器上已经存在的音乐软件，而不是安装新软件。
- improvement:
  - 交叉查询了桌面入口、`dpkg-query`、Snap 路径、常见命令、用户目录配置和本地安装包目录。
- result:
  - 可直接启动或系统级安装的软件包括 Rhythmbox、KuGou Music、Spotify、VLC、Totem。
  - MoeKoe Music 只确认有配置/缓存残留，未确认有可启动安装。
- commands:
  - `rg --files /usr/share/applications ~/.local/share/applications ...`
  - `dpkg-query -W ... | rg -i ...`
  - `command -v rhythmbox totem vlc spotify ...`
  - `find /home/loviya/apps/music ...`
- artifacts:
  - `/usr/share/applications/org.gnome.Rhythmbox3.desktop`
  - `/usr/share/applications/com.kugou.spark.desktop`
  - `/var/lib/snapd/desktop/applications/spotify_spotify.desktop`
  - `/var/lib/snapd/desktop/applications/vlc_vlc.desktop`
  - `/home/loviya/apps/music/com.kugou.spark_20.0.52.27315spark8_all.deb`
- next:
  - 无。
