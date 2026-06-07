---
id: 20260520-imwheel-up-scroll-tune
name: imwheel 上滚速度调优
slug: imwheel-up-scroll-tune
cwd: /home/loviya
summary: "调整 imwheel 普通上滚倍数，修复鼠标向上滚动过快、上下滚动速度不匹配。"
tags:
  - mouse
  - imwheel
  - scroll
---

# Current Snapshot

- workflow id: 20260520-imwheel-up-scroll-tune
- current status: 已完成
- current goal: 按用户要求撤销上滚倍率调低，恢复普通上下滚动同为倍率 2。
- current blocker: 无
- next step: 无
- tags: mouse, imwheel, scroll
- summary: 当前 GNOME X11 会话运行 `imwheel -b 4 5 0 0 8 9`；用户反馈调回原状；已将 `/home/loviya/.imwheelrc` 普通 `Up` 倍数从 `1` 改回 `2`，普通 `Down` 保持 `2`；`imwheel -q` 解析通过，并已重启为单进程 `imwheel -k -b 4 5 0 0 8 9`。

# Key Results

- 修改文件: `/home/loviya/.imwheelrc`
- 备份文件: `/home/loviya/.imwheelrc.bak-20260520-1001`
- 最终状态: `None, Up, Button4, 2` 和 `None, Down, Button5, 2`
- 保留: 普通下滚倍数 `2`、Shift+滚轮横向滚动、侧键 `Thumb1/Thumb2` 到浏览器前进后退快捷键。

# Log

## 2026-05-20 10:01 +0800

- 来源指令: 用户反馈“鼠标的向上滚动和向下滚动速度不匹配，向上滚动太快”。
- 环境确认: `XDG_SESSION_TYPE=x11`，`DESKTOP_SESSION=ubuntu-xorg`，桌面为 GNOME X11。
- 当前进程: `/usr/bin/imwheel -b 4 5 0 0 8 9`。
- 当前配置: `/home/loviya/.imwheelrc` 中普通 `None, Up, Button4, 2` 和 `None, Down, Button5, 2` 同为倍数 `2`。
- 处理: 备份配置后，将普通上滚倍数降为 `1`。
- 验证: `imwheel -q -b "4 5 0 0 8 9"` 解析通过；`imwheel -k -b "4 5 0 0 8 9"` 已重启，当前 `pgrep -a -u "$USER" imwheel` 仅见 `60092 imwheel -k -b 4 5 0 0 8 9`。
## 2026-05-20 10:15 +0800

- 来源指令: 用户要求“改回去”。
- 处理: 将 `/home/loviya/.imwheelrc` 普通 `None, Up, Button4, 1` 改回 `None, Up, Button4, 2`。
- 验证: `imwheel -q -b "4 5 0 0 8 9"` 解析通过；已执行 `imwheel -k -b "4 5 0 0 8 9"`，当前进程为 `89690 imwheel -k -b 4 5 0 0 8 9`。
