---
id: 20260512-ipconfig-linux-command-explain
name: IPConfig Linux Command Explain
slug: ipconfig-linux-command-explain
cwd: /home/loviya/notes/obsidian_notes/25_2/cn/class
summary: 解释why ipconfig is not a standard Linux command and point to ip/ifconfig alternatives.
tags:
  - linux
  - networking
  - command
priority: normal
---

# IPConfig Linux 命令 Explain

## 当前快照

- 状态: 已完成
- 目标: 解释为什么 Linux 上 `ipconfig` 不可用，以及应使用哪些替代命令。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-12 14:44:13 +0800

## 关键结果

- `ipconfig` 是 Windows 的网络配置查询命令，不是 Linux 的通用标准命令。
- Linux 现代系统推荐使用 `ip addr`、`ip route`、`ip link` 等 `iproute2` 命令。
- 老教程里的 Linux 命令通常是 `ifconfig`，它来自 `net-tools`，很多发行版默认不再安装。

## 解释ipconfig on Linux

- 更新时间: 2026-05-12 14:44:13 +0800
- 工作目录: `/home/loviya/notes/obsidian_notes/25_2/cn/class`
- 来源指令: `为什么我的电脑上ipconfig没有用,这个不应该是所有的linux设备都能使用吗`
- 问题:
  - 用户误以为 `ipconfig` 是所有 Linux 设备都应提供的命令。
- 结果:
  - 结论是 `ipconfig` 属于 Windows；Linux 上应优先使用 `ip addr` 查看网卡和地址，必要时安装 `net-tools` 使用旧命令 `ifconfig`。
- 下一步:
  - 无。
