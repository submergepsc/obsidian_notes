---
id: 20260515-g304-button-wheel-fix
name: Logitech G304 Button And Wheel Fix
slug: g304-button-wheel-fix
cwd: /home/loviya
summary: Restore Logitech G304 wheel button mapping and keep side buttons as browser back/forward.
tags:
  - terminal
  - mouse
  - xinput
  - imwheel
priority: normal
---

# Logitech G304 Button And Wheel Fix

## Current Snapshot

- status: 待确认
- goal: Fix mouse side-button browser navigation and wheel behavior for the Logitech G304.
- blocker: none
- next: User should test side buttons in a browser; if direction is reversed, swap physical 12/13 mapping values `8 9` to `9 8` in `/home/loviya/.local/bin/configure-logitech-g304`.
- updated: 2026-05-16 13:51:01 +0800

## Key Results

- X11 session detected: `XDG_SESSION_TYPE=x11`, `DISPLAY=:0`.
- Active external pointer: `Logitech G304`, initially id `12`.
- Problem found: G304 button map was `1 2 3 8 9 6 7 8 9 ...`, so physical wheel up/down buttons `4/5` were mapped to browser back/forward `8/9`.
- Applied standard mapping immediately: `1 2 3 4 5 6 7 8 9 10 ...`.
- Resulting behavior:
  - Wheel up/down remains button `4/5` for scrolling.
  - Side buttons remain button `8/9` for browser back/forward.
- Added persistent login script: `/home/loviya/.local/bin/configure-logitech-g304`.
- Added autostart entry: `/home/loviya/.config/autostart/logitech-g304-buttons.desktop`.
- Updated existing imwheel autostart to `imwheel -b "4 5"` so it only handles wheel buttons and does not capture side buttons.
- Started host-side `imwheel -b 4 5`; existing `/home/loviya/.imwheelrc` doubles normal wheel scrolling.
- Added `imwheel` translations for side buttons: logical button 8 emits `Alt+Left`, logical button 9 emits `Alt+Right`.
- Corrected `imwheel` startup to `imwheel -b "4 5 0 0 8 9"` so buttons 8/9 are interpreted as thumb buttons rather than horizontal wheel buttons.
- Replaced stale `imwheel` processes with one host process: `imwheel -k -b 4 5 0 0 8 9`.
- Live `xinput test 12` showed the actual side buttons report as `button 12` and `button 13` on this host.
- Corrected the active and persistent button map so physical `12/13` emit logical browser buttons `8/9`: `1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20`.
- User-requested reusable note written to `/home/loviya/.codex/codex_notes/requested/2026-05-16-logitech-g304-xinput-imwheel.md`.

## Restore G304 Wheel And Side Buttons

- updated: 2026-05-16 00:51:01 +0800
- cwd: `/home/loviya`
- source instruction: `快帮我调整一下鼠标,尤其是4,5button的前进和后退功能和滚轮`
- problem:
  - The Logitech G304 had wheel buttons `4/5` remapped to `8/9`, which can make wheel movement trigger browser back/forward instead of scrolling.
- improvement:
  - Restored the standard X11 mapping and made it persistent through a GNOME autostart script.
  - Limited imwheel to buttons `4 5` only, preserving side-button back/forward behavior.
- result:
- `xinput get-button-map 12` returns `1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20`.
- Host process list shows `imwheel -kill -b 4 5` running.
- next:
  - Ask user to test browser side buttons and scrolling; tune `.imwheelrc` if the wheel is too fast or too slow.

## Map Physical 10 And 11 To Browser Navigation

- updated: 2026-05-16 00:56:58 +0800
- cwd: `/home/loviya`
- source instruction: `不行,前进后退实现不了`
- problem:
  - The standard mapping kept wheel behavior correct, but browser forward/back did not work from the side buttons.
- improvement:
  - Inspected XI2 device metadata. The G304 exposes labels for `Button Forward` and `Button Back` beyond the usual 8/9 positions.
  - Updated the active X11 button map to `1 2 3 4 5 6 7 8 9 9 8 12 13 14 15 16 17 18 19 20`, preserving wheel buttons 4/5 and mapping physical 10/11 to logical browser forward/back 9/8.
  - Updated `/home/loviya/.local/bin/configure-logitech-g304` with the same mapping for persistence.
- result:
  - `xinput get-button-map 12` now returns `1 2 3 4 5 6 7 8 9 9 8 12 13 14 15 16 17 18 19 20`.
- next:
  - User should test the two side buttons in a browser. If direction is reversed, swap the 10th and 11th mapping values from `9 8` to `8 9`.

## Translate Side Buttons To Browser Shortcuts With Imwheel

- updated: 2026-05-16 11:51:47 +0800
- cwd: `/home/loviya`
- source instruction: `继续帮我修复鼠标问题`
- problem:
  - The active X11 button map already preserved wheel buttons `4/5` and mapped physical G304 buttons `10/11` to logical browser buttons `9/8`, but browser back/forward still needed a more reliable path.
  - An initial `imwheel -b "4 5 8 9"` attempt put buttons `8/9` into horizontal wheel slots, causing `Thumb1` and `Thumb2` actions to be rejected.
- improvement:
  - Updated `/home/loviya/.imwheelrc` so `Thumb1` emits `Alt_L|Left` and `Thumb2` emits `Alt_L|Right`, while preserving the existing doubled wheel scroll mappings.
  - Updated `/home/loviya/.config/autostart/imwheel.desktop` to start `imwheel -b "4 5 0 0 8 9"`, placing buttons `8/9` in the thumb-button slots.
  - Restarted host-side `imwheel` with `imwheel -k -b "4 5 0 0 8 9"` so only one corrected process remains.
- result:
  - `imwheel -q -b "4 5 0 0 8 9"` parses the config cleanly.
  - Host process list shows one active corrected process: `imwheel -k -b 4 5 0 0 8 9`.
  - `xinput get-button-map 12` remains `1 2 3 4 5 6 7 8 9 9 8 12 13 14 15 16 17 18 19 20`.
- next:
  - User should test side buttons in a browser; if direction is reversed, swap the `Thumb1` and `Thumb2` outputs in `/home/loviya/.imwheelrc`.

## Correct Actual Physical Side Buttons 12 And 13

- updated: 2026-05-16 13:51:01 +0800
- cwd: `/home/loviya`
- source instruction: `还是不行`
- problem:
  - The previous attempts assumed the G304 side buttons were physical `10/11`, but the browser navigation still did not work.
  - A first `xinput test-xi2 --root 12` capture was overwhelmed by motion events and only showed unrelated left-button and wheel events.
- improvement:
  - Switched to `xinput test 12` and asked the user to press both side buttons with minimal motion.
  - Confirmed the actual side buttons report as `button 12` and `button 13`.
  - Applied the active map `1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20`, mapping physical `12/13` to logical browser buttons `8/9`.
  - Updated `/home/loviya/.local/bin/configure-logitech-g304` with the same mapping for persistence.
  - Restarted `imwheel` with `imwheel -k -b "4 5 0 0 8 9"`.
- result:
  - `xinput get-button-map 12` returns `1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20`.
  - Host process list shows one corrected `imwheel` process: `imwheel -k -b 4 5 0 0 8 9`.
- next:
  - User should test side buttons in a browser; if direction is reversed, swap physical 12/13 mapping values `8 9` to `9 8` in `/home/loviya/.local/bin/configure-logitech-g304`.

## Write User-Requested Mouse Notes

- updated: 2026-05-16 13:52:58 +0800
- cwd: `/home/loviya`
- source instruction: `把所有会话涉及到的两个鼠标相关的应用,以及所有的命令和介绍,写到notes里面去`
- problem:
  - The user wanted the mouse-related applications, commands, and explanations from the session preserved as a reusable note.
- improvement:
  - Wrote `/home/loviya/.codex/codex_notes/requested/2026-05-16-logitech-g304-xinput-imwheel.md`.
  - Covered the two tools `xinput` and `imwheel`, final state, involved files, commands used, troubleshooting procedure, and caveats.
  - Updated `/home/loviya/.codex/codex_notes/INDEX.md` with a high-priority user-requested entry.
- result:
  - The reusable note is available from the Codex notes knowledge base and links back to this worklog.
- next:
  - Continue testing the physical side buttons in a browser.
