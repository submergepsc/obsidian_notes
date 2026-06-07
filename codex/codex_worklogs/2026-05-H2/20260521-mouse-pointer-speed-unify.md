---
id: 20260521-mouse-pointer-speed-unify
name: 鼠标移动速率统一
slug: mouse-pointer-speed-unify
cwd: /home/loviya
summary: "统一 X11/GNOME 下鼠标指针移动速度和加速 profile，避免不同应用体感不一致。"
tags:
  - mouse
  - xinput
  - gnome
---

# Current Snapshot

- workflow id: 20260521-mouse-pointer-speed-unify
- current status: 已完成
- current goal: 统一鼠标指针移动速率，让应用继承同一套系统指针速度。
- current blocker: 无
- next step: 无；用户实际体感测试各应用中的指针移动。
- tags: mouse, xinput, gnome
- summary: 已将 GNOME 鼠标和触摸板持久设置统一为 `speed 0.0`、`accel-profile flat`；当前 X11 设备 G304、内置 Mouse、Touchpad 均已实时设置为 `libinput Accel Speed 0.0` 和 flat profile；G304 登录脚本也补充同样设置。

# Log

## 2026-05-21 13:35 +0800

- 来源指令: 用户要求“调整一下鼠标的移动速率，很怪，把所有的应用都设置成一样”。
- 账户/环境: `CODEX_HOME=/home/loviya/.codex-b`，cwd `/home/loviya`，会话 `ubuntu-xorg`，`XDG_SESSION_TYPE=x11`。
- 复用历史: 发现 2026-05-19/20 的 G304/xinput/imwheel 工作流；那些是按钮和滚轮配置，当前是指针移动速度，创建新 workflow。
- 当前 GNOME 设置: `org.gnome.desktop.peripherals.mouse speed 0.0`、`accel-profile 'flat'`；`touchpad speed 0.0`、`accel-profile 'default'`。
- 当前 X11 设备: `Logitech G304` id `12`；`FTCS0038:00 2808:0106 Mouse` id `13`；`FTCS0038:00 2808:0106 Touchpad` id `14`。
- 当前 xinput 属性: G304 为 `libinput Accel Speed 0.0` 且 profile `0, 1`；内置 Mouse 和 Touchpad 为 `0.0` 且 profile `1, 0`。

## 2026-05-21 13:39 +0800

- 处理: 写入 GNOME 持久设置：mouse speed 0.0、mouse accel-profile flat、touchpad speed 0.0、touchpad accel-profile flat。
- 处理: 对当前 X11 设备实时应用相同策略：G304 id 12、内置 Mouse id 13 设置 `libinput Accel Speed 0.0` 和 `libinput Accel Profile Enabled 0 1`；Touchpad id 14 设置 `libinput Accel Speed 0.0` 和 `libinput Accel Profile Enabled 0 1 0`。
- 处理: `apply_patch` 因 sandbox 符号链接挂载问题无法读取 `/home/loviya/.local/bin/configure-logitech-g304`；改用提升权限下的最小 `sed` 追加，补充 G304 登录时的 `libinput Accel Speed 0.0` 和 flat profile。
- 验证: `gsettings list-recursively` 显示 mouse/touchpad 均为 `speed 0.0`、`accel-profile flat`。
- 验证: `xinput list-props` 显示 G304、内置 Mouse、Touchpad 均为 `libinput Accel Speed 0.000000`；profile 分别为 G304 `0, 1`、内置 Mouse `0, 1`、Touchpad `0, 1, 0`。
