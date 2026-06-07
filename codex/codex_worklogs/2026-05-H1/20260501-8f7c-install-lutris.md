---
id: 20260501-8f7c-install-lutris
name: install-lutris
slug: install-lutris
cwd: /home/loviya
summary: 已安装 Lutris from Ubuntu multiverse via apt and verified the package state.
tags:
  - lutris
  - wine
  - gaming
  - apt
priority: normal
---

# 安装 Lutris

## 当前快照

- 状态: 已完成
- 目标: 安装Lutris on the Ubuntu workstation for Wine/game management.
- 阻塞: 无
- 下一步: 无；launch Lutris from the application menu or run `/usr/games/lutris` in a normal graphical session.
- 更新时间: 2026-05-02 03:29:06 +0800

## 关键结果

- 已安装 `lutris` from Ubuntu 24.04 multiverse 使用 `sudo apt-get install -y lutris`.
- 已安装 package version: `0.5.14-2`.
- Verified 带 `dpkg-query`: `lutris 0.5.14-2 install ok installed`.
- Command path: `/usr/games/lutris`.

## 命令

- `sudo apt-get update`
- `sudo apt-get install -y lutris`
- `dpkg-query -W -f='${Package} ${Version} ${Status}\n' lutris`

## 说明

- Running `lutris --version` from the sandboxed non-GUI command context failed 因为 it could not open display `:0`; the package installation itself is valid.
- For normal use, start Lutris from the desktop application launcher or from a graphical terminal.
