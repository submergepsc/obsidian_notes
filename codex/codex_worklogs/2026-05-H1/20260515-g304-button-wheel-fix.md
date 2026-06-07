---
id: 20260515-g304-button-wheel-fix
name: Logitech G304 Button And Wheel Fix
slug: g304-button-wheel-fix
cwd: /home/loviya
summary: 恢复 Logitech G304 中键映射，并保留侧键作为浏览器后退/前进。
tags:
  - terminal
  - mouse
  - xinput
  - imwheel
priority: normal
---

# Logitech G304 按键 And Wheel 修复

## 当前快照

- 状态: 待确认
- 目标: 修复 Logitech G304 的侧键浏览器导航和滚轮行为。
- 阻塞: 无。
- 下一步: User should test side buttons in a browser; if direction is reversed, swap physical 12/13 mapping values `8 9` to `9 8` in `/home/loviya/.local/bin/configure-logitech-g304`.
- 更新时间: 2026-05-16 13:51:01 +0800

## 关键结果

- X11 session detected: `XDG_SESSION_TYPE=x11`, `DISPLAY=:0`.
- Active external pointer: `Logitech G304`, initially id `12`.
- Problem found: G304 button map was `1 2 3 8 9 6 7 8 9 ...`, so physical wheel up/down buttons `4/5` were mapped to browser back/forward `8/9`.
- Applied standard mapping immediately: `1 2 3 4 5 6 7 8 9 10 ...`.
- Resulting behavior:
  - Wheel up/down remains button `4/5` for scrolling.
  - Side buttons remain button `8/9` for browser back/forward.
- 已新增 persistent login script: `/home/loviya/.local/bin/configure-logitech-g304`.
- 已新增 autostart entry: `/home/loviya/.config/autostart/logitech-g304-buttons.desktop`.
- 已更新 existing imwheel autostart to `imwheel -b "4 5"` so it only handles wheel buttons and does not capture side buttons.
- 已开始 host-side `imwheel -b 4 5`; existing `/home/loviya/.imwheelrc` doubles normal wheel scrolling.
- 已新增 `imwheel` translations for side buttons: logical button 8 emits `Alt+Left`, logical button 9 emits `Alt+Right`.
- Corrected `imwheel` startup to `imwheel -b "4 5 0 0 8 9"` so buttons 8/9 are interpreted as thumb buttons rather than horizontal wheel buttons.
- Replaced stale `imwheel` processes 带 one host process: `imwheel -k -b 4 5 0 0 8 9`.
- Live `xinput test 12` showed the actual side buttons report as `button 12` and `button 13` on this host.
- Corrected the active and persistent button map so physical `12/13` emit logical browser buttons `8/9`: `1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20`.
- User-requested reusable note written to `/home/loviya/.codex/codex_notes/requested/2026-05-16-logitech-g304-xinput-imwheel.md`.

## Restore G304 Wheel And Side 按键

- 更新时间: 2026-05-16 00:51:01 +0800
- 工作目录: `/home/loviya`
- 来源指令: `快帮我调整一下鼠标,尤其是4,5button的前进和后退功能和滚轮`
- 问题:
  - The Logitech G304 had wheel buttons `4/5` remapped to `8/9`, which can make wheel movement trigger browser back/forward 而不是 scrolling.
- 改进:
  - Restored the standard X11 mapping and made it persistent through a GNOME autostart script.
  - Limited imwheel to buttons `4 5` only, preserving side-button back/forward behavior.
- 结果:
- `xinput get-button-map 12` 返回 `1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20`.
- Host process list shows `imwheel -kill -b 4 5` running.
- 下一步:
  - Ask user to test browser side buttons and scrolling; tune `.imwheelrc` if the wheel is too fast or too slow.

## 映射 Physical 10 And 11 To 浏览器 Navigation

- 更新时间: 2026-05-16 00:56:58 +0800
- 工作目录: `/home/loviya`
- 来源指令: `不行,前进后退实现不了`
- 问题:
  - The standard mapping kept wheel behavior correct, but browser forward/back did not work from the side buttons.
- 改进:
  - Inspected XI2 device metadata. The G304 exposes labels for `Button Forward` and `Button Back` beyond the usual 8/9 positions.
  - 已更新 the active X11 button map to `1 2 3 4 5 6 7 8 9 9 8 12 13 14 15 16 17 18 19 20`, preserving wheel buttons 4/5 and mapping physical 10/11 to logical browser forward/back 9/8.
  - 已更新 `/home/loviya/.local/bin/configure-logitech-g304` 带 the same mapping for persistence.
- 结果:
  - `xinput get-button-map 12` now 返回 `1 2 3 4 5 6 7 8 9 9 8 12 13 14 15 16 17 18 19 20`.
- 下一步:
  - User should test the two side buttons in a browser. If direction is reversed, swap the 10th and 11th mapping values from `9 8` to `8 9`.

## Translate Side 按键 To 浏览器 Shortcuts With Imwheel

- 更新时间: 2026-05-16 11:51:47 +0800
- 工作目录: `/home/loviya`
- 来源指令: `继续帮我修复鼠标问题`
- 问题:
  - The active X11 button map already preserved wheel buttons `4/5` and mapped physical G304 buttons `10/11` to logical browser buttons `9/8`, but browser back/forward still needed a more reliable path.
  - An initial `imwheel -b "4 5 8 9"` attempt put buttons `8/9` into horizontal wheel slots, causing `Thumb1` and `Thumb2` actions to be rejected.
- 改进:
  - 已更新 `/home/loviya/.imwheelrc` so `Thumb1` emits `Alt_L|Left` and `Thumb2` emits `Alt_L|Right`, while preserving the existing doubled wheel scroll mappings.
  - 已更新 `/home/loviya/.config/autostart/imwheel.desktop` to start `imwheel -b "4 5 0 0 8 9"`, placing buttons `8/9` in the thumb-button slots.
  - Restarted host-side `imwheel` 带 `imwheel -k -b "4 5 0 0 8 9"` so only one corrected process remains.
- 结果:
  - `imwheel -q -b "4 5 0 0 8 9"` parses the config cleanly.
  - Host process list shows one active corrected process: `imwheel -k -b 4 5 0 0 8 9`.
  - `xinput get-button-map 12` remains `1 2 3 4 5 6 7 8 9 9 8 12 13 14 15 16 17 18 19 20`.
- 下一步:
  - User should test side buttons in a browser; if direction is reversed, swap the `Thumb1` and `Thumb2` outputs in `/home/loviya/.imwheelrc`.

## Correct Actual Physical Side 按键 12 And 13

- 更新时间: 2026-05-16 13:51:01 +0800
- 工作目录: `/home/loviya`
- 来源指令: `还是不行`
- 问题:
  - The previous attempts assumed the G304 side buttons were physical `10/11`, but the browser navigation still did not work.
  - A first `xinput test-xi2 --root 12` capture was overwhelmed by motion events and only showed unrelated left-button and wheel events.
- 改进:
  - Switched to `xinput test 12` and asked the user to press both side buttons 带 minimal motion.
  - 已确认 the actual side buttons report as `button 12` and `button 13`.
  - Applied the active map `1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20`, mapping physical `12/13` to logical browser buttons `8/9`.
  - 已更新 `/home/loviya/.local/bin/configure-logitech-g304` 带 the same mapping for persistence.
  - Restarted `imwheel` 带 `imwheel -k -b "4 5 0 0 8 9"`.
- 结果:
  - `xinput get-button-map 12` 返回 `1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20`.
  - Host process list shows one corrected `imwheel` process: `imwheel -k -b 4 5 0 0 8 9`.
- 下一步:
  - User should test side buttons in a browser; if direction is reversed, swap physical 12/13 mapping values `8 9` to `9 8` in `/home/loviya/.local/bin/configure-logitech-g304`.

## Write User-Requested Mouse 笔记

- 更新时间: 2026-05-16 13:52:58 +0800
- 工作目录: `/home/loviya`
- 来源指令: `把所有会话涉及到的两个鼠标相关的应用,以及所有的命令和介绍,写到notes里面去`
- 问题:
  - 用户需要 the mouse-related applications, commands, and explanations from the session preserved as a reusable note.
- 改进:
  - Wrote `/home/loviya/.codex/codex_notes/requested/2026-05-16-logitech-g304-xinput-imwheel.md`.
  - Covered the two tools `xinput` and `imwheel`, final state, involved files, commands used, troubleshooting procedure, and caveats.
  - 已更新 `/home/loviya/.codex/codex_notes/INDEX.md` 带 a high-priority user-requested entry.
- 结果:
  - The reusable note is available from the Codex notes knowledge base and links back to this worklog.
- 下一步:
  - Continue testing the physical side buttons in a browser.
