---
id: 20260508-find-flameshot-save-path
name: Find Flameshot Save Path
slug: find-flameshot-save-path
cwd: /home/loviya/notes/obsidian_notes/homework/os
summary: 定位 Flameshot 配置的保存路径，并与最近保存的截图文件对照。
tags:
  - desktop
  - flameshot
  - screenshots
priority: normal
---

# Find Flameshot Save Path

## 当前快照

- 状态: 已完成
- 目标: 找到 Flameshot 截图保存位置。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-08 20:24:00 +0800

## 关键结果

- Flameshot 配置文件：`/home/loviya/.config/flameshot/flameshot.ini`。
- 配置项显示 `savePath=/home/loviya/\x56fe\x7247/Screenshots`，对应中文路径 `/home/loviya/图片/Screenshots`。
- `savePath已修复=true`，表示 Flameshot 使用固定保存路径。
- 实测 `/home/loviya/图片/Screenshots` 当前为空。
- 最近已有截图文件主要位于 `/home/loviya/图片/截图/`，最新发现文件为 `/home/loviya/图片/截图/截图 2026-05-08 20-14-01.png`。

## 定位 Flameshot Screenshot Directory

- 更新时间: 2026-05-08 20:24:00 +0800
- 工作目录: `/home/loviya/notes/obsidian_notes/homework/os`
- 来源指令: `找一下我使用flameshot截图后的图片保存在哪里`
- 问题:
  - 需要确认 Flameshot 截图保存路径，并区分配置路径与系统截图目录。
- 命令:
  - `sed -n '1,220p' /home/loviya/.config/flameshot/flameshot.ini`
  - `rg -n '^(savePath|savePath已修复|filenamePattern)=' /home/loviya/.config/flameshot/flameshot.ini`
  - `ls -la /home/loviya/图片/Screenshots`
  - `find /home/loviya/图片/截图 -maxdepth 1 -type f -printf '%TY-%Tm-%Td %TH:%TM %p\n'`
- 结果:
  - Flameshot 的固定保存目录配置为 `/home/loviya/图片/Screenshots`。
  - 当前目录为空；如果用户看到最近的截图文件，应同时检查 `/home/loviya/图片/截图/`。
- 下一步:
  - 无

## Correct Distinction From System Screenshots

- 更新时间: 2026-05-08 20:31:00 +0800
- 工作目录: `/home/loviya/notes/obsidian_notes/homework/os`
- 来源指令: `我告诉你这不是flameshot截图的`
- 问题:
  - Earlier interpretation mixed GNOME/system screenshot files under `/home/loviya/图片/截图/` 带 Flameshot results.
- correction:
  - `/home/loviya/图片/截图/` should be treated as the desktop environment/system screenshot directory, not evidence of Flameshot output.
  - Flameshot configuration still points at `/home/loviya/图片/Screenshots`, but that directory is empty.
  - `~/.cache/flameshot/flameshot/` only contains `region.txt`; no saved PNG/JPG screenshot file was found there.
- 结果:
  - If the recent Flameshot action used copy/clipboard 而不是 save, there may be no file on disk.
- 下一步:
  - To force a saved file next time, use the save icon in Flameshot or run `flameshot gui -p /home/loviya/图片/Screenshots`.

## 使用Flameshot Native Copy Shortcut To Also Save

- 更新时间: 2026-05-08 20:43:00 +0800
- 工作目录: `/home/loviya/notes/obsidian_notes/homework/os`
- 来源指令: `不,我需要直接使用flame的自己框选,然后使用他自己的快捷键来c完成两个事情`
- 问题:
  - 用户不想使用外部同步脚本，而是要保留 Flameshot 原生框选界面，并在框选后按 Flameshot 内部快捷键 `C` 同时完成复制和保存。
- 决策:
  - 使用 Flameshot 内置选项 `saveAfterCopy=true`。
  - 将 `TYPE_COPY=C`，让 `C` 触发复制动作；Flameshot 内置的 `saveAfterCopy` 会在复制后保存到固定目录。
  - 将 `TYPE_SAVE=Ctrl+S`，避免 `C` 同时绑定复制和保存导致快捷键冲突。
- changed:
  - `/home/loviya/.config/flameshot/flameshot.ini` 增加 `saveAfterCopy=true`。
  - `/home/loviya/.config/flameshot/flameshot.ini` 设置 `TYPE_COPY=C`、`TYPE_SAVE=Ctrl+S`。
  - 删除了早先临时创建但不采用的 `/home/loviya/bin/flameshot-sync` 和 `/tmp/flameshot-sync`。
- 验证:
  - `flameshot config --check` 返回 `No errors detected.`。
  - `rg -n 'saveAfterCopy|TYPE_COPY|TYPE_SAVE|savePath' /home/loviya/.config/flameshot/flameshot.ini` 确认配置已写入。
- 结果:
  - 现在用户可继续运行 `flameshot gui`，框选后按 `C`；该按键会复制截图，并由 Flameshot 自动保存文件到 `/home/loviya/图片/Screenshots`。
- 下一步:
  - 无
