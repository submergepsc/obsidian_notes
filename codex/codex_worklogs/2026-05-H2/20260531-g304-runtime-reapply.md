---
id: 20260531-g304-runtime-reapply
name: G304 鼠标运行态重套配置
slug: g304-runtime-reapply
cwd: /home/loviya
summary: "修复当前 X11 会话中 Logitech G304 button map 和高精度滚轮属性回退的问题。"
tags:
  - mouse
  - logitech-g304
  - xinput
  - imwheel
---

# Current Snapshot

- workflow id: 20260531-g304-runtime-reapply
- current status: 待继续
- current goal: 修复当前会话里 G304 鼠标在 WPS 中滚动过快、其他应用正常的问题。
- current blocker: 需要用户重新登录或重启，让 Xorg 重新加载输入驱动后再测试 WPS。
- next step: 用户重新登录或重启后，在 WPS 中测试滚轮；若仍过快，读取 `xinput list-props` 和 Xorg 日志确认 G304 是否已切到 `evdev`。
- tags: mouse, logitech-g304, xinput, imwheel
- summary: 已安装 `xserver-xorg-input-evdev`，并写入 `/etc/X11/xorg.conf.d/90-logitech-g304-evdev.conf`，只匹配 `Logitech G304` pointer 使用 `evdev`；触摸板和其他设备继续使用默认 `libinput`。当前 Xorg 会话仍显示 G304 由 `libinput` 管理，这是预期现象，需要重新登录或重启后生效并在 WPS 中体感验证。

# Log

## 2026-06-03 10:42 +0800

- 处理: 安装 `xserver-xorg-input-evdev`，版本 `1:2.10.6-2build3`。
- 处理: 新增 `/etc/X11/xorg.conf.d/90-logitech-g304-evdev.conf`，内容只匹配 `MatchProduct "Logitech G304"`、`MatchIsPointer "on"`、`Driver "evdev"`。
- 验证: `dpkg -l xserver-xorg-input-evdev` 显示 `ii`；配置文件权限为 `-rw-r--r-- root root`。
- 验证: 当前 `xinput list-props 12` 仍显示 `libinput` 属性，说明当前已启动 Xorg 会话尚未切换驱动；需重登/重启后验证。
- 回滚: 如重启后鼠标异常，删除 `/etc/X11/xorg.conf.d/90-logitech-g304-evdev.conf` 并再次重启即可回到默认 `libinput` 路径。

## 2026-06-03 10:23 +0800

- 新反馈: 用户反馈“鼠标在 WPS 上还是滚动非常快，其他地方正常”。
- 当前环境: `XDG_SESSION_TYPE=x11`，Ubuntu `24.04.4 LTS`，WPS `12.1.2.25882.AK.preread.sw~spark1`。
- 当前设备: `xinput list` 显示 `Logitech G304` 为 pointer id `12`，触摸板为 id `14`。
- 当前输入链路: G304 仍由 `libinput` 管理，`xserver-xorg-input-evdev` 未安装；`/etc/X11/xorg.conf.d` 为空，系统默认配置在 `/usr/share/X11/xorg.conf.d/40-libinput.conf`。
- 当前 imwheel: `/home/loviya/.imwheelrc` 只保留 `Thumb1/Thumb2` 侧键转换，自启动为 `imwheel -b "0 0 0 0 8 9"`，不再接管普通滚轮。
- 判断: 这次不是 `imwheel` 放大普通滚轮，而是 WPS 在 `libinput` 离散滚轮事件下仍滚动过快；后续尝试只让 G304 使用 `evdev`，避免影响触摸板。

## 2026-05-31 22:38 +0800

- 来源指令: 用户要求“帮我修一下鼠标当前的问题”。
- 账户/环境: `CODEX_HOME=/home/loviya/.codex-b`，cwd `/home/loviya`，`XDG_SESSION_TYPE=x11`，`DISPLAY=:0`。
- 复用历史: 查到此前 G304 鼠标管理记录，当前配置应由 `ratbagd/Piper`、`xinput` 登录脚本和 `imwheel` 三层组成。
- 当前进程: `imwheel` 正在运行，命令为 `/usr/bin/imwheel -b 4 5 0 0 8 9`。
- 当前偏差: `xinput get-button-map 12` 修复前为默认映射，未把物理侧键 `12/13` 映射到 logical `8/9`。
- 当前偏差: `xinput list-props 12` 修复前显示 `libinput High Resolution Wheel Scroll Enabled` 为 `1`，与登录脚本期望的 `0` 不一致。
- 处理: 运行 `/home/loviya/.local/bin/configure-logitech-g304` 重新应用当前 X11 会话中的 G304 映射和 libinput 属性。
- 验证: `xinput get-button-map 12` 已恢复为 `1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20`。
- 验证: `xinput list-props 12` 显示 `libinput High Resolution Wheel Scroll Enabled` 已恢复为 `0`，`libinput Accel Speed` 为 `0.000000`，profile 为 `0, 1`。
- 注意: 这次没有修改配置文件；如果重插鼠标或接收器后再次回退，原因更可能是热插拔后 `xinput` 运行态重置，需要增加热插拔触发脚本或用户级 watcher。

## 2026-05-31 22:50 +0800

- 新反馈: 用户反馈鼠标仍然无法滚动。
- 诊断: `xinput test 12` 在滚动时能看到 `button press 5` / `button release 5`，说明 G304 和 X11 仍有滚轮事件。
- 判断: 既然设备层有 `4/5` 事件，应用不能滚动更可能是 `imwheel` 抓取普通滚轮后的转换层导致。
- 处理: 备份 `/home/loviya/.imwheelrc` 到 `/home/loviya/.imwheelrc.bak-20260531-no-scroll`。
- 处理: 备份 `/home/loviya/.config/autostart/imwheel.desktop` 到 `/home/loviya/.config/autostart/imwheel.desktop.bak-20260531-no-scroll`。
- 处理: 将 `/home/loviya/.imwheelrc` 降级为只保留 `Thumb1/Thumb2` 侧键转换。
- 处理: 将 autostart 从 `imwheel -b "4 5 0 0 8 9"` 改为 `imwheel -b "0 0 0 0 8 9"`，不再接管普通滚轮 `4/5`。
- 运行态: 已重启 `imwheel` 为 `imwheel -k -b 0 0 0 0 8 9`。
- 验证: `imwheel -q -b "0 0 0 0 8 9"` 解析通过；`pgrep` 最终显示 `345383 imwheel -k -b 0 0 0 0 8 9`。
- Note: 已更新用户请求 note `/home/loviya/.codex/codex_notes/requested/2026-05-16-logitech-g304-xinput-imwheel.md`，记录当前“滚轮优先可用，imwheel 只管侧键”的方案。

- 注意: 验证 notes 残留命令时曾因 shell 反引号误触发默认 `imwheel` 启动；已 `pkill -f imwheel` 后重新启动为 `imwheel -k -b 0 0 0 0 8 9`，最终只保留该进程。
