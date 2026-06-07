---
id: 20260607-g304-browser-backforward-fix
name: G304 浏览器后退前进修复
slug: g304-browser-backforward-fix
cwd: /home/loviya
summary: "修复 Logitech G304 在浏览器里侧键无法触发后退/前进的问题，减少 imwheel 对侧键的干预。"
tags:
  - mouse
  - logitech-g304
  - xinput
  - imwheel
---

# Current Snapshot

- workflow id: 20260607-g304-browser-backforward-fix
- current status: 进行中
- current goal: 恢复 Logitech G304 在浏览器中的后退/前进侧键行为。
- current blocker: sandbox 内无法直接连到图形 X 会话验证 `xinput` 实际事件。
- next step: 用户重新登录桌面后，在浏览器中测试侧键；若仍无效，再继续查当前会话的实际按钮编号。
- tags: mouse, logitech-g304, xinput, imwheel
- summary: 已把 `imwheel` 的自启动关闭，避免它继续干预侧键；同时把 `/home/loviya/.local/bin/configure-logitech-g304` 的设备查找重试次数加长，减少登录时脚本过早退出的概率。

# Log

## 2026-06-07 20:55 +0800

- 用户反馈：浏览器里鼠标侧键没有前进/后退功能。
- 现场判断：
  - 当前会话是 `x11`。
  - 本机存在三层鼠标链路历史：`ratbagd/Piper`、`xinput` 登录脚本、`imwheel`。
  - 现有配置里 `~/.imwheelrc` 只处理 `Thumb1/Thumb2`，而登录脚本 `configure-logitech-g304` 负责把 G304 物理侧键映射到 logical `8/9`。
- 已执行修改：
  - 将 `/home/loviya/.config/autostart/imwheel.desktop` 的 `X-GNOME-Autostart-enabled` 设为 `false`，先去掉对侧键的额外干预。
  - 将 `/home/loviya/.local/bin/configure-logitech-g304` 的设备查找重试从 10 次增加到 30 次，降低登录早期设备尚未枚举完成时脚本退出的概率。
- 验证：
  - `bash -n /home/loviya/.local/bin/configure-logitech-g304` 通过。
  - `.desktop` 文件已确认写入禁用状态。

