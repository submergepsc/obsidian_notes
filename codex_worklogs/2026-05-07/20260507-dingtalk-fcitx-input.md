---
id: 20260507-dingtalk-fcitx-input
name: DingTalk Fcitx Chinese Input
slug: dingtalk-fcitx-input
cwd: /home/loviya
summary: Diagnosed DingTalk Chinese input failure as an ibus/fcitx environment mismatch and added user desktop overrides that launch DingTalk with Fcitx5 variables.
tags:
  - ubuntu
  - dingtalk
  - fcitx5
  - input-method
priority: normal
---

# DingTalk Fcitx Chinese Input

## Current Snapshot

- status: 待继续
- goal: Restore Chinese input support in DingTalk on Ubuntu.
- blocker: 新钉钉进程已确认使用 Fcitx5 环境，仍需用户在当前钉钉窗口里验证候选框和中文上屏行为。
- next: 用户在当前钉钉聊天输入框测试中文输入；若仍失败，将 `GTK_IM_MODULE` 改为 `xim` 兼容模式后重启钉钉。
- updated: 2026-05-08 00:07:19 +0800

## Key Results

- Host process check showed Fcitx5 is running as `/usr/bin/fcitx5`.
- DingTalk was installed as `com.alibabainc.dingtalk 8.1.0.6021101` and launched through APM with `/opt/apps/com.alibabainc.dingtalk/files/Elevator.sh`.
- DingTalk process environment used `GTK_IM_MODULE=ibus`, `QT_IM_MODULE=ibus`, and `XMODIFIERS=@im=ibus`, while the desktop shell environment was configured for Fcitx5.
- Added user-level desktop overrides so future DingTalk launches explicitly use Fcitx5:
  - `/home/loviya/.local/share/applications/com.alibabainc.dingtalk.desktop`
  - `/home/loviya/.local/share/applications/com.alibabainc.dingtalk_std_int.desktop`
- Refreshed the user desktop database with `update-desktop-database /home/loviya/.local/share/applications`.
- After the user reported the issue still existed, process inspection showed the running DingTalk was still the old `23:47:15` process and still used ibus variables.
- Replaced the inline desktop `Exec=env ...` command with an executable wrapper:
  - `/home/loviya/.local/bin/dingtalk-fcitx`
- Manual APM `ace-run` launch confirmed the new DingTalk main process `629507` inherited `GTK_IM_MODULE=fcitx`, `QT_IM_MODULE=fcitx`, and `XMODIFIERS=@im=fcitx`.

## Decisions

- Use user-level `.desktop` overrides instead of editing `/usr/share/applications`, so package updates and system files are not modified directly.
- Keep the original APM launch command and only prepend the input method environment variables.
- Prefer a wrapper script over inline desktop environment assignments so the launch path is easier to inspect and reuse.

## Commands

- `ps -u loviya -o pid,comm,args | rg -i "dingtalk|ding|fcitx|ibus|sogou|rime"`
- `xargs -0 -L1 -a /proc/543593/environ | rg '^(XMODIFIERS|GTK_IM_MODULE|QT_IM_MODULE|SDL_IM_MODULE|GLFW_IM_MODULE|INPUT_METHOD|LANG|LANGUAGE|LC_|XDG_SESSION_TYPE|DISPLAY|WAYLAND_DISPLAY)='`
- `desktop-file-validate /home/loviya/.local/share/applications/com.alibabainc.dingtalk.desktop /home/loviya/.local/share/applications/com.alibabainc.dingtalk_std_int.desktop`
- `update-desktop-database /home/loviya/.local/share/applications`
- `fusermount3 -u /tmp/apm/com.alibabainc.dingtalk`
- `chrootEnvPath=/tmp/apm/com.alibabainc.dingtalk APM_PKG_NAME=com.alibabainc.dingtalk /var/lib/apm/apm/files/ace-run /opt/apps/com.alibabainc.dingtalk/files/Elevator.sh`

## DingTalk Used Ibus Instead Of Fcitx

- updated: 2026-05-07 23:53:19 +0800
- cwd: `/home/loviya`
- source instruction: `我现在在钉钉中无法使用中文输入`
- problem:
  - The active DingTalk process inherited ibus input method variables even though the user's desktop input method is Fcitx5.
  - This mismatch prevents DingTalk from using the active Chinese input method.
- improvement:
  - Added user-level desktop entries that set `XMODIFIERS=@im=fcitx`, `GTK_IM_MODULE=fcitx`, `QT_IM_MODULE=fcitx`, `SDL_IM_MODULE=fcitx`, and `GLFW_IM_MODULE=ibus` before calling the original APM DingTalk launcher.
- result:
  - New DingTalk launches from the application menu or URL scheme should inherit Fcitx5 input method settings.
- next:
  - Restart DingTalk and test Chinese input in a chat input box.

## Wrapper Launch Confirmed Fcitx Environment

- updated: 2026-05-08 00:07:19 +0800
- cwd: `/home/loviya`
- source instruction: `还是不行`
- problem:
  - The first fix had not reached the running DingTalk process because the visible process was still the old pre-fix instance.
  - Closing DingTalk through process termination left stale APM FUSE overlay mounts under `/tmp/apm/com.alibabainc.dingtalk`.
- improvement:
  - Cleaned the stale overlay with `fusermount3 -u`.
  - Added `/home/loviya/.local/bin/dingtalk-fcitx` and updated both user desktop files to call that wrapper.
  - Manually ran the APM `ace-run` stage after mounting to launch DingTalk and verify environment inheritance.
- result:
  - DingTalk main process `629507` now has `GTK_IM_MODULE=fcitx`, `QT_IM_MODULE=fcitx`, and `XMODIFIERS=@im=fcitx`.
- next:
  - User should test Chinese input in the current DingTalk window. If Fcitx still does not show candidates, switch `GTK_IM_MODULE` to `xim` in the wrapper and restart DingTalk.
