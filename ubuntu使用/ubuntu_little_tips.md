---
data: 2026-04-27
tags:
  - Ubuntu
  - tips
  - index
cssclasses:
---

# ubuntu little tips

这个页面是 Ubuntu 使用过程中的高频速查页。
原则：一句话提醒 + 对应长文入口。

## 先看这里

- 总路线：[[ubuntu使用整体路线]]
- 终端/Bash 入口：[[bash，terminal,脚本有关]]
- 软件入口：[[ubuntu软件使用介绍]]
- 零散系统笔记：[[notes_ubuntu]]

## 终端高频

- 搜历史命令：`Ctrl + R`
- 查看命令本体：`command -v 命令名`
- 查看命令类型：`type 命令名`
- 立即让配置生效：`source ~/.bashrc`
- 打开当前目录：`nautilus .` 或 `xdg-open .`
- 查看当前 shell 调用链：`pstree -s $$`

延伸：
- [[bash，terminal,脚本有关/bash一些快捷操作]]
- [[bash，terminal,脚本有关/which和type的区别]]
- [[bash，terminal,脚本有关/bash指令顺序和错误示例]]

## tmux / nano / 鼠标冲突

- 鼠标争夺层次：图形系统 -> 终端 -> tmux -> 编辑器
- `Shift` 往往能把鼠标临时还给上层终端
- 如果 `nano` / `vim` 和 tmux 抢鼠标，直接看：[[bash，terminal,脚本有关/nano里面取消tmux接管鼠标]]

延伸：
- [[bash，terminal,脚本有关/bash,zsh_dash,sh,tmux介绍]]
- [[bash，terminal,脚本有关/tmux介绍]]
- [[bash，terminal,脚本有关/终端窗口_tmux会话_分页与分屏]]

## Node / npm / pnpm / corepack

- `nvm` 管 Node
- `npm` 跟着当前 Node 版本走
- `pnpm` 可能是独立安装的另一套
- 团队项目优先考虑 `packageManager + corepack`

详细说明：[[notes_ubuntu/nvm,nodejs,npn,corepack]]

## 安装与系统维护

- 安装本地 `deb`：`sudo apt install ./xxx.deb`
- 日常更新：
```bash
sudo apt update
sudo apt upgrade -y
sudo apt autoremove --purge -y
```
- 大版本升级前先备份，再看：[[ubuntu使用整体路线]]

延伸：
- [[notes_ubuntu/deb文件如何安装]]

## 磁盘与启动

- 看整体磁盘：`df -h`
- 看块设备：`lsblk`
- 定位大文件夹：`ncdu ~`
- 开机自启动和 GUI 环境变量问题，优先分清 `~/.profile` 和 `~/.bashrc`

延伸：
- [[notes_ubuntu/ubuntu应用_开机自启动]]

## 输入法 / Xorg / Wayland

- GUI 程序通常不读 `~/.bashrc`
- 输入法环境变量问题，优先排查 `~/.profile` / `~/.xprofile`
- Xorg 下异常多，Wayland 下很多事情会自动接管

相关说明已经散在：
- [[notes_ubuntu/ubuntu终端有关]]

## 还没补完的坑

- [[notes_ubuntu/长截图——未实现]]
- [[ubuntu软件使用介绍/终端工具拓展--为实现]]
