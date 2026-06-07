---
id: 20260506-ubuntu-input-experience-tools
name: Ubuntu Input Experience Tools
slug: ubuntu-input-experience-tools
cwd: /home/loviya
summary: "整理 Ubuntu 上改善鼠标、触控板和键盘体验的常用工具。"
tags:
  - ubuntu
  - input
  - tools
priority: normal
---

# Ubuntu 输入 Experience Tools

## 当前快照

- 状态: 已完成
- 目标: 回答 Ubuntu 是否有改善鼠标、触控板和键盘体验的相关工具。
- 阻塞: 无
- 下一步: 无
- 更新时间: 2026-05-06 10:25:54 +0800

## 关键结果

- 推荐从 GNOME Tweaks、Input Remapper、Solaar、Piper、libinput-gestures/Touchegg、keyd、Kanata、KMonad、Barrier/Input Leap 等工具中按设备和需求选择。
- 鼠标手势、触控板手势、按键重映射、外设管理和跨设备键鼠共享应分开处理，避免一个工具承担过多职责。
- Solaar 不只支持办公鼠标；它面向使用 Logitech HID++/Centurion 协议的罗技键盘、鼠标、轨迹球、触控板、耳机和接收器。游戏鼠标的 DPI、按键和灯光配置通常优先看 Piper/libratbag。
- 本机 G304 已被 `ratbagctl list` 识别为 `Logitech G304`，USB 接收器为 `046d:c53f`，设备模型为 `usb:046d:4074:0`。Piper/libratbag 可调 6 个按键、1 个 profile、1000Hz report rate、400/800/1600/3200 DPI 档。

## Ubuntu 输入 Experience Tool 推荐

- 更新时间: 2026-05-06 10:25:54 +0800
- 工作目录: `/home/loviya`
- 来源指令: `ubuntu有没有增加鼠标和触控便,键盘体验的相关工具`
- 问题:
  - 用户希望了解 Ubuntu 上改善鼠标、触控板和键盘体验的工具。
- 结果:
  - 给出按用途分类的推荐清单和安装优先级。
- 下一步:
  - 无

## Clarify Solaar And Logitech Gaming 设备 Scope

- 更新时间: 2026-05-06 10:30:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `关于这个罗技,我记得这个工具只能支持办公鼠标对吗`
- 问题:
  - 用户询问罗技工具是否只支持办公鼠标。
- 结果:
  - 区分 Solaar 和 Piper：Solaar 覆盖很多罗技 HID++/Centurion 设备和接收器管理；Piper/libratbag 更适合游戏鼠标的 DPI、按键、灯光配置。
- 下一步:
  - 如用户提供具体型号，可按型号判断更适合哪个工具。

## Verify Logitech G304 本地 Support

- 更新时间: 2026-05-06 10:35:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `我的罗技g304有没有好的支持`
- 问题:
  - 用户询问 Logitech G304 在 Ubuntu 上是否有较好的支持。
- 命令:
  - `command -v piper`
  - `command -v ratbagctl`
  - `lsusb`
  - `ratbagctl list`
  - `ratbagctl singing-hare info`
- 结果:
  - 本机已安装 `piper` 和 `ratbagctl`。
  - `lsusb` 显示 `046d:c53f Logitech, Inc. USB Receiver`。
  - `ratbagctl list` 显示 `singing-hare: Logitech G304`。
  - `ratbagctl singing-hare info` 显示可用配置包括 6 个按键、1000Hz report rate、400/800/1600/3200 DPI 档，当前 800dpi。
- 下一步:
  - 用 Piper 图形界面调 DPI/按键；如只需要侧键映射到系统快捷键，可配合 Input Remapper。
