---
id: 20260519-local-mouse-management-audit
name: 本机鼠标管理逻辑核查
slug: local-mouse-management-audit
cwd: /home/loviya
summary: "只读核查本机 Logitech G304 鼠标管理链路：ratbagd/Piper 设备级配置、xinput 登录映射、imwheel 滚轮与侧键转换。"
tags:
  - mouse
  - logitech-g304
  - xinput
  - imwheel
  - ratbagd
---

# Current Snapshot

- workflow id: 20260519-local-mouse-management-audit
- current status: 已完成
- current goal: 查清本机当前鼠标管理逻辑和实际生效状态。
- current blocker: 无。
- next step: 无；如用户反馈侧键方向或滚轮速度不符合预期，再调整 `/home/loviya/.imwheelrc` 或 `/home/loviya/.local/bin/configure-logitech-g304`。
- tags: mouse, logitech-g304, xinput, imwheel, ratbagd
- summary: 当前鼠标管理由三层叠加：系统级 `ratbagd`/Piper 管 G304 设备级按键和 DPI，登录自启动脚本用 `xinput` 固定 X11 按键映射和 libinput 属性，`imwheel` 登录自启动处理滚轮加速和 logical `8/9` 侧键到浏览器快捷键。

## Key Results

- 当前图形会话是 X11：`XDG_SESSION_TYPE=x11`，`DISPLAY=:0`，`XDG_SESSION_DESKTOP=ubuntu-xorg`。
- 当前外接鼠标指针设备是 `Logitech G304`，`xinput` pointer id 为 `12`。
- `xinput get-button-map 12` 当前为：

```text
1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20
```

- 含义：这台机器上 G304 物理侧键上报为 `12/13`，登录脚本把它们映射成 logical `8/9`，即浏览器后退/前进常用按键。
- `/home/loviya/.local/bin/configure-logitech-g304` 是 X11 登录后恢复 G304 映射的脚本；自启动入口是 `/home/loviya/.config/autostart/logitech-g304-buttons.desktop`。
- `configure-logitech-g304` 同时设置 `libinput Natural Scrolling Enabled=0`、`libinput High Resolution Wheel Scroll Enabled=1`、`libinput Scrolling Pixel Distance=15`。
- `imwheel` 当前进程为 `/usr/bin/imwheel -b 4 5 0 0 8 9`。
- `/home/loviya/.config/autostart/imwheel.desktop` 登录自启动 `imwheel -b "4 5 0 0 8 9"`。
- `/home/loviya/.imwheelrc` 当前规则：

```text
".*"
None,      Up,   Button4, 2
None,      Down, Button5, 2
None,      Thumb1, Alt_L|Left
None,      Thumb2, Alt_L|Right
Control_L, Up,   Control_L|Button4
Control_L, Down, Control_L|Button5
```

- 这表示普通滚轮放大 2 倍，logical `8/9` 侧键再被转换为 `Alt+Left` / `Alt+Right`。
- `ratbagd.service` 是系统级服务，当前 active running；`ratbagctl list` 识别设备为 `hooting-chinchilla: Logitech G304`。
- `ratbagctl hooting-chinchilla info` 当前设备级状态：report rate `1000Hz`，active/default DPI `800dpi`，DPI 档 `400/800/1600/3200`，Button 3 -> `button 8`，Button 4 -> `button 9`，Button 5 -> `resolution-cycle-up`。
- 已安装的相关包只有 `imwheel`、`piper`、`ratbagd`；未在 `dpkg -l` 输出中看到 `input-remapper`、`solaar`、`xbindkeys`、`keyd`、`libratbag-tools` 的 installed 条目。
- 在用户启动项和脚本中，鼠标相关命中集中于 `/home/loviya/.config/autostart/imwheel.desktop`、`/home/loviya/.config/autostart/logitech-g304-buttons.desktop`、`/home/loviya/.local/bin/configure-logitech-g304`。

## Commands

- `rg -n "mouse|鼠标|libinput|xinput|imwheel|gestures|ratbag|piper|solaar|hid|pointer|touchpad|libratbag" ~/.codex/worklogs/INDEX.md ~/.codex/worklogs`
- `sed -n '1,180p' ~/.codex/codex_notes/requested/2026-05-16-logitech-g304-xinput-imwheel.md`
- `sed -n '1,140p' ~/.imwheelrc`
- `sed -n '1,120p' ~/.config/autostart/imwheel.desktop`
- `pgrep -a -u loviya imwheel`
- `sed -n '1,180p' ~/.local/bin/configure-logitech-g304`
- `sed -n '1,120p' ~/.config/autostart/logitech-g304-buttons.desktop`
- `xinput list`
- `xinput get-button-map 12`
- `xinput list-props 12`
- `ratbagctl list`
- `ratbagctl hooting-chinchilla info`
- `systemctl status ratbagd.service`
- `dpkg -l input-remapper piper ratbagd solaar xbindkeys imwheel keyd libratbag-tools`
- `rg -n "imwheel|xinput|ratbag|piper|solaar|input-remapper|xbindkeys|keyd|configure-logitech|G304|mouse|鼠标" ~/.config/autostart ~/.config/systemd ~/.local/bin ~/.xprofile ~/.xsessionrc ~/.profile ~/.zprofile ~/.bashrc ~/.zshrc`

## Notes

- 本次只读核查没有修改鼠标配置。
- 沙箱启动本地命令时遇到 `~/.codex-b/memories` 符号链接导致的 bubblewrap 只读路径错误，因此本轮只读排查命令按权限规则在沙箱外执行。

## 2026-05-19 Shift+Wheel 横向滚动

- 来源指令: 用户指出 Windows 中 `Shift+滚轮` 有特殊功能，需要处理。
- 决策: 用 `imwheel` 模拟 Windows 常见行为：`Shift+WheelUp` -> horizontal left，`Shift+WheelDown` -> horizontal right。
- 修改文件: `/home/loviya/.imwheelrc`
- 新增规则:

```text
Shift_L,   Up,   Button6, 2
Shift_L,   Down, Button7, 2
Shift_R,   Up,   Button6, 2
Shift_R,   Down, Button7, 2
```

- 保留原有规则: 普通滚轮仍为 `Button4/Button5` 放大 2 倍；`Control_L+滚轮` 仍保留给应用缩放；侧键 `Thumb1/Thumb2` 仍转为 `Alt_L|Left` / `Alt_L|Right`。
- 验证:
  - `imwheel -q -b "4 5 0 0 8 9"` 解析通过。
  - 已执行 `imwheel -k -b "4 5 0 0 8 9"` 重启当前进程。
  - 当前进程: `274346 imwheel -k -b 4 5 0 0 8 9`。
- 后续: 用户在横向表格、浏览器宽页面、VS Code/Obsidian 横向代码块中测试 `Shift+滚轮`；如果方向反了，交换 `Button6` 和 `Button7`。

## 2026-05-19 更新鼠标配置总览 note

- 来源指令: 用户要求把整个系统所有鼠标配置全面介绍并写入 notes，结合本轮上下文。
- 修改 note: `/home/loviya/.codex/codex_notes/requested/2026-05-16-logitech-g304-xinput-imwheel.md`
- 内容更新: 重写为“本机 Logitech G304 鼠标配置总览”，覆盖 Piper/ratbagd、xinput、imwheel、自启动文件、X11 按钮编号、Shift+滚轮横向滚动、重复点和简化建议、故障处理、最小验证清单。
- 更新索引:
  - `/home/loviya/.codex/codex_notes/INDEX.md`
  - `/home/loviya/.codex/codex_notes/requested/INDEX.md`
- 验证: `rg` 已确认 note 关键章节和两个索引入口存在。

## 2026-05-20 补充配置文件位置速查

- 来源指令: 用户要求把三个鼠标配置的配置文件位置写到 notes。
- 修改 note: `/home/loviya/.codex/codex_notes/requested/2026-05-16-logitech-g304-xinput-imwheel.md`
- 新增小节: `配置文件位置速查`，列出 Piper/ratbagd、xinput、imwheel 的作用、配置或入口位置。
- 验证: `sed -n '19,58p'` 已检查新增小节存在。
