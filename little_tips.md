---
data: 2026-04-27
tags:
  - tips
  - index
cssclasses:
---

# little tips

这个页面只放高频、短平快、能立刻回想起解决路径的小提示。
长文原理说明不要堆这里，只放入口和一句话结论。

## 终端与命令行

- Ubuntu 终端/Bash 总入口：[[ubuntu使用/bash，terminal,脚本有关]]
- Windows Terminal / `cmd` / `powershell` / `pwsh`：[[tools/terminal有关问题或者脚本有关问题]]
- Bash 命令查询顺序：`alias -> function -> builtin -> PATH`
- 安静判断命令是否存在：`command -v xxx >/dev/null 2>&1`
- 历史命令搜索：`Ctrl + R`
- 当前 shell 立刻重载：Linux 用 `source ~/.bashrc`，Windows PowerShell 可用 `.$PROFILE` 或自定义 `rl`

## 文件与路径

- 文件名有空格或特殊字符，优先看：[[tools/tips/文件名空格解决方案]]
- 复杂文件名批量处理：[[tools/tips/带有复杂文件名文件的批量删除]]
- Obsidian 里不要直接把奇怪路径当标题，避免造出难处理的文件名

## Node / 包管理

- `nvm` 管 Node 版本，Node 自带 `npm`
- `pnpm` 是独立包管理器，不天然跟 `nvm` 绑定
- `corepack` 是包管理器版本调度器
- 详细速查：[[ubuntu使用/notes_ubuntu/nvm,nodejs,npn,corepack]]

## Ubuntu 高频入口

- Ubuntu 小技巧速查：[[ubuntu使用/ubuntu_little_tips]]
- Ubuntu 使用整体路线：[[ubuntu使用/ubuntu使用整体路线]]
- Ubuntu 软件索引：[[ubuntu使用/ubuntu软件使用介绍]]

## Windows 高频入口

- Windows 小技巧速查：[[tools/win_little_tips]]
- Windows 自启动：[[tools/tips/windows系统自启有关]]
- Windows 核心系统工具：[[tools/tools/Windows 核心系统工与运行命令指南]]

## 一眼记住的几条

- `nautilus .`：用文件管理器打开当前目录
- `xdg-open .`：按系统默认方式打开当前目录/文件
- `df -h`：看磁盘总览
- `ncdu ~`：找谁最占空间
- `sudo apt install ./xxx.deb`：安装本地 `deb` 的首选写法
