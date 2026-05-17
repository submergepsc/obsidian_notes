---
id: 20260512-ipconfig-linux-command-explain
name: IPConfig Linux Command Explain
slug: ipconfig-linux-command-explain
cwd: /home/loviya/notes/obsidian_notes/25_2/cn/class
summary: Explain why ipconfig is not a standard Linux command and point to ip/ifconfig alternatives.
tags:
  - linux
  - networking
  - command
priority: normal
---

# IPConfig Linux Command Explain

## Current Snapshot

- status: 已完成
- goal: 解释为什么 Linux 上 `ipconfig` 不可用，以及应使用哪些替代命令。
- blocker: none
- next: none
- updated: 2026-05-12 14:44:13 +0800

## Key Results

- `ipconfig` 是 Windows 的网络配置查询命令，不是 Linux 的通用标准命令。
- Linux 现代系统推荐使用 `ip addr`、`ip route`、`ip link` 等 `iproute2` 命令。
- 老教程里的 Linux 命令通常是 `ifconfig`，它来自 `net-tools`，很多发行版默认不再安装。

## Explain ipconfig on Linux

- updated: 2026-05-12 14:44:13 +0800
- cwd: `/home/loviya/notes/obsidian_notes/25_2/cn/class`
- source instruction: `为什么我的电脑上ipconfig没有用,这个不应该是所有的linux设备都能使用吗`
- problem:
  - 用户误以为 `ipconfig` 是所有 Linux 设备都应提供的命令。
- result:
  - 结论是 `ipconfig` 属于 Windows；Linux 上应优先使用 `ip addr` 查看网卡和地址，必要时安装 `net-tools` 使用旧命令 `ifconfig`。
- next:
  - 无。
