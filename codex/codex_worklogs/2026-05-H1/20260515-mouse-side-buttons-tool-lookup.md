---
id: 20260515-mouse-side-buttons-tool-lookup
name: Mouse Side Buttons Tool Lookup
slug: mouse-side-buttons-tool-lookup
cwd: /home/loviya
summary: "定位并修复鼠标侧键前进后退失效：保留 imwheel 滚轮加速，将 G304 侧键改为 button 8/9。"
tags:
  - mouse
  - imwheel
  - piper
  - ratbagctl
priority: normal
---

# Mouse Side 按键 Tool 查找

## 当前快照

- 状态: 已完成
- 目标: 查找并修复导致鼠标侧键无法前进后退的映射问题。
- 阻塞: 无
- 下一步: 用户在浏览器中按 G304 两个侧键，确认后退/前进是否恢复。
- 更新时间: 2026-05-15 19:05:00 +0800

## 关键结果

- 本机已安装并运行 `imwheel`，进程为 `/usr/bin/imwheel`。
- `~/.config/autostart/imwheel.desktop` 会在桌面登录时自动执行 `imwheel`。
- `~/.imwheelrc` 创建于 2026-05-15 13:44，当前配置会处理 `Button4` / `Button5`，主要用于滚轮加速。
- 本机也安装了 `piper` 和 `ratbagd`，`ratbagctl` 识别到 `Logitech G304`。
- 修复前，`ratbagctl hooting-chinchilla info` 显示 G304 的物理第 4/5 键映射为 `button 4` / `button 5`，DPI 键映射为 `resolution-cycle-up`。
- 已保留 `imwheel` 运行状态，将 G304 侧键改为浏览器后退/前进常用的 `button 8` / `button 9`。

## 定位 Mouse 按键 Mapping Tools

- 更新时间: 2026-05-15 18:58:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `我现在的鼠标已经无法完成4,5按键的前进和后退了,我记得安装了一个工具,你查找一下`
- 问题:
  - 用户记得曾安装过一个工具，当前鼠标 4/5 键无法完成前进和后退。
- 命令:
  - `command -v piper`
  - `command -v ratbagctl`
  - `command -v imwheel`
  - `dpkg -l input-remapper piper ratbagd solaar xbindkeys imwheel keyd libratbag-tools`
  - `sed -n '1,160p' ~/.config/autostart/imwheel.desktop`
  - `sed -n '1,200p' ~/.imwheelrc`
  - `pgrep -a -u loviya imwheel`
  - `xinput list`
  - `xinput get-button-map 12`
  - `ratbagctl list`
  - `ratbagctl hooting-chinchilla info`
- 结果:
  - 关键工具是 `imwheel`：已安装、正在运行、设置为自启动，并且配置文件处理 `Button4` / `Button5`。
  - 另一个相关工具是 `piper`/`ratbagd`：用于 Logitech G304 的设备级按键和 DPI 配置。
  - 未发现 `input-remapper`、`solaar`、`xbindkeys`、`keyd` 已安装。
- 下一步:
  - 如要继续修复，优先短暂停用 `imwheel` 验证侧键是否恢复；若未恢复，再用 Piper 调整 G304 按键映射。

## Restore G304 Side 按键 To 浏览器 Back Forward

- 更新时间: 2026-05-15 19:05:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `你觉得应该修改哪个,自己决定`
- 问题:
  - `imwheel` 需要保留用于滚轮加速，但 G304 侧键被设备级映射成 `button 4` / `button 5`，容易与滚轮事件及 `imwheel` 配置冲突，也不符合浏览器后退/前进常用的 `button 8` / `button 9`。
- 决策:
  - 修改 Piper/libratbag 管理的 G304 设备级侧键映射，而不是停用 `imwheel`。
- 命令:
  - `ratbagctl hooting-chinchilla button 3 action set button 8`
  - `ratbagctl hooting-chinchilla button 4 action set button 9`
  - `ratbagctl hooting-chinchilla info`
  - `xinput get-button-map 12`
- 结果:
  - `ratbagctl hooting-chinchilla info` 已显示 `Button: 3 is mapped to 'button 8'` 和 `Button: 4 is mapped to 'button 9'`。
  - X11 的 Logitech G304 button map 仍为默认透传 `1 2 3 4 5 6 7 8 9 ...`。
  - `imwheel` 仍在运行，用于现有滚轮加速。
- 下一步:
  - 用户在浏览器中按 G304 两个侧键，确认后退/前进是否恢复。
