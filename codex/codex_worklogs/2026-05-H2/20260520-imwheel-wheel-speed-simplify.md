---
id: 20260520-imwheel-wheel-speed-simplify
name: imwheel 滚轮速度简化
slug: imwheel-wheel-speed-simplify
cwd: /home/loviya
summary: "移除 imwheel 对普通滚轮和 Shift+滚轮的速度/方向转换，只保留 G304 侧键快捷键转换。"
tags:
  - mouse
  - imwheel
  - scroll
---

# Current Snapshot

- workflow id: 20260520-imwheel-wheel-speed-simplify
- current status: 已完成
- current goal: 缓解 WPS Office PDF 阅读时鼠标滚轮跳页；对 WPS 单独把滚轮上下转换为键盘上下箭头。
- current blocker: 无
- next step: 用户在 WPS 中测试滚轮是否仍跳页；若仍跳页，尝试把 WPS 规则从上下箭头改为更细粒度的可用按键或禁用 WPS 滚轮接管。
- tags: mouse, imwheel, scroll
- summary: imwheel 全局滚轮仍保持 1 倍；因 WPS PDF 中仍出现跳页，已新增 WPS 专用规则 `(wpsoffice\.wpsoffice|WPS Office)`，将普通滚轮 Up/Down 转换为键盘 Up/Down，保留 Shift 横向滚动、侧键和 Ctrl+滚轮透传。

# Key Results

- 修改文件: `/home/loviya/.imwheelrc`
- 修改文件: `/home/loviya/.config/autostart/imwheel.desktop`
- 修改文件: `/home/loviya/.local/bin/configure-logitech-g304`
- 修改 note: `/home/loviya/.codex/codex_notes/requested/2026-05-16-logitech-g304-xinput-imwheel.md`
- 备份文件: `/home/loviya/.imwheelrc.bak-20260520-1058`
- 备份文件: `/home/loviya/.imwheelrc.bak-20260520-rollback-fast-wheel`
- 验证: `imwheel -q -b "4 5 0 0 8 9"` 解析通过；当前仅见 `266892 imwheel -k -b 4 5 0 0 8 9`。
- 验证: `xinput list-props 12` 显示 `libinput High Resolution Wheel Scroll Enabled` 为 `0`、`Horizontal Scroll Enabled` 为 `1`、`Scrolling Pixel Distance` 当前为 `10`。

# Log

## 2026-05-20 10:58 +0800

- 来源指令: 用户反馈“鼠标的滚轮很莫名其妙的有多种速度，能改就改，改不了就删了”。
- 复用历史: 查到 2026-05-19/20 的 G304 与 imwheel 配置记录；当前问题与 `imwheel` 滚轮倍数叠加强相关。
- 当前配置: `/home/loviya/.imwheelrc` 中普通 `Up/Down` 均为倍数 `2`，`Shift_L/Shift_R + Up/Down` 转为 `Button6/Button7` 且倍数 `2`，`Control_L + Up/Down` 透传，侧键 `Thumb1/Thumb2` 转为 `Alt_L|Left/Right`。
- 当前进程: `imwheel -k -b 4 5 0 0 8 9`。
- 处理: 备份 `/home/loviya/.imwheelrc` 到 `/home/loviya/.imwheelrc.bak-20260520-1058`。
- 处理: 删除 `.imwheelrc` 中所有滚轮相关规则，只保留 `Thumb1/Thumb2` 到 `Alt_L|Left/Right`。
- 处理: 将 `/home/loviya/.config/autostart/imwheel.desktop` 的 `Exec` 从 `imwheel -b "4 5 0 0 8 9"` 改为 `imwheel -b "0 0 0 0 8 9"`。
- 验证: `imwheel -q -b "0 0 0 0 8 9"` 解析通过。
- 运行时: 普通 sandbox 内 `imwheel -k` 不能打开 X display；按权限执行后成功杀掉旧进程并启动新进程 `245009 imwheel -k -b 0 0 0 0 8 9`。
- 文档: 更新用户请求 note 与 notes 索引，记录当前 `imwheel` 不再接管滚轮。

## 2026-05-20 11:05 +0800

- 来源指令: 用户反馈“现在滚轮非常快并且没有侧向滚动”。
- 判断: 把普通滚轮交回系统/libinput 后，实际系统层滚动过快；同时删除 `Shift+滚轮` 规则导致侧向滚动消失。
- 处理: 将 `/home/loviya/.imwheelrc` 改为普通滚轮倍率 `1`，`Shift_L/Shift_R + Up/Down` 横向滚动倍率 `1`，保留侧键 `Thumb1/Thumb2`，并补充 `Control_L/Control_R + Up/Down` 透传。
- 处理: 将 `/home/loviya/.config/autostart/imwheel.desktop` 改回 `Exec=imwheel -b "4 5 0 0 8 9"`。
- 处理: 重启运行时 `imwheel`，当前进程为 `266892 imwheel -k -b 4 5 0 0 8 9`。
- 处理: 发现 G304 `libinput High Resolution Wheel Scroll Enabled` 仍为 `1`；已立即设为 `0`，并将 `/home/loviya/.local/bin/configure-logitech-g304` 持久化为登录时设置 `0`。
- 验证: `imwheel -q -b "4 5 0 0 8 9"` 解析通过；`xinput list-props 12` 显示高精度滚轮已关闭、水平滚动仍启用。

## 2026-05-21 20:20 +0800

- 来源指令: 用户反馈 WPS 中仍然跳页。
- 当前状态: `imwheel` 已运行，`/home/loviya/.imwheelrc` 全局滚轮倍率已是 1；G304 `Scrolling Pixel Distance` 已降到 10，`High Resolution Wheel Scroll Enabled` 为 0。
- 判断: 继续调 libinput 像素距离无效；WPS 可能直接按滚轮离散事件翻页。
- 处理: 备份 `/home/loviya/.imwheelrc` 到 `/home/loviya/.imwheelrc.bak-20260521-wps-jump`。
- 处理: 在 `.imwheelrc` 顶部新增 `(wpsoffice\.wpsoffice|WPS Office)` 专用规则，把普通滚轮 Up/Down 转换为键盘 Up/Down，保留 Shift 横向滚动、侧键和 Ctrl+滚轮透传。
- 验证: `imwheel -q -b "4 5 0 0 8 9"` 解析通过；已重启为 `imwheel -k -b 4 5 0 0 8 9`，进程 pid 151112。
- 待测: 用户在 WPS PDF 中实测是否仍跳页。
