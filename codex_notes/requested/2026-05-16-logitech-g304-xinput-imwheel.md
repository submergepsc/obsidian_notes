---
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
  - mouse
  - xinput
  - imwheel
  - logitech-g304
source_worklog: ~/.codex/worklogs/2026-05-15/20260515-g304-button-wheel-fix.md
---

# Logitech G304 Xinput And Imwheel Fix

## Scope

This note records the mouse-related tools, commands, files, and decisions used to fix Logitech G304 wheel scrolling and side-button browser navigation on this X11 desktop.

The two mouse-related applications involved were:

- `xinput`: X11 input-device inspection and button-map configuration.
- `imwheel`: mouse wheel and button translator used here for scroll-speed tuning and optional browser shortcut translation.

## Final State

- Desktop session: X11, `DISPLAY=:0`.
- Pointer device: `Logitech G304`, device id `12` during this session.
- Final active G304 button map:

```text
1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20
```

- Meaning of the final map:
  - physical `4/5`: wheel up/down, preserved for scrolling.
  - physical `12/13`: actual G304 side buttons on this host.
  - physical `12 -> logical 8`: browser back.
  - physical `13 -> logical 9`: browser forward.

If side-button direction is reversed, swap the `8 9` at positions 12 and 13 to `9 8` in `/home/loviya/.local/bin/configure-logitech-g304`, then rerun the script or apply the equivalent `xinput set-button-map` command.

## Files

### `/home/loviya/.local/bin/configure-logitech-g304`

Persistent login script. It finds the current G304 pointer device id and applies the button map.

Important line:

```bash
xinput set-button-map "$device_id" 1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20
```

It also keeps natural scrolling off and high-resolution wheel scrolling on when those libinput properties exist.

### `/home/loviya/.config/autostart/logitech-g304-buttons.desktop`

GNOME autostart entry for the G304 configuration script.

### `/home/loviya/.imwheelrc`

Current `imwheel` configuration:

```text
".*"
None,      Up,   Button4, 2
None,      Down, Button5, 2
None,      Thumb1, Alt_L|Left
None,      Thumb2, Alt_L|Right
Control_L, Up,   Control_L|Button4
Control_L, Down, Control_L|Button5
```

The wheel rules double normal wheel scroll. The thumb rules translate logical button `8/9` into browser keyboard shortcuts.

### `/home/loviya/.config/autostart/imwheel.desktop`

Current autostart command:

```text
Exec=imwheel -b "4 5 0 0 8 9"
```

The `0 0` placeholders are important. In `imwheel`, the button-spec slots are interpreted as:

```text
1: Wheel Up       -> button 4
2: Wheel Down     -> button 5
3: Wheel Left     -> button 6
4: Wheel Right    -> button 7
5: Thumb Button 1 -> button 8
6: Thumb Button 2 -> button 9
```

So `4 5 0 0 8 9` means: use wheel up/down, skip horizontal wheel, and use buttons `8/9` as thumb buttons.

## Commands Used

### Inspect session and device state

```bash
env | rg 'DISPLAY|XAUTHORITY|XDG_SESSION|WAYLAND|DBUS'
xinput list
xinput list 12 --long
xinput list-props 12
xinput get-button-map 12
```

Important observations:

- `XDG_SESSION_TYPE=x11`
- `DISPLAY=:0`
- `XAUTHORITY=/run/user/1000/gdm/Xauthority`
- `Logitech G304` was pointer id `12`.
- `xinput list 12 --long` showed 20 supported buttons, but labels alone were misleading for the physical side-button positions.

### Apply and verify button maps

Initial standard map used to restore wheel scrolling:

```bash
xinput set-button-map 12 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
xinput get-button-map 12
```

Incorrect intermediate assumption, based on labels, that side buttons were physical `10/11`:

```bash
xinput set-button-map 12 1 2 3 4 5 6 7 8 9 9 8 12 13 14 15 16 17 18 19 20
xinput get-button-map 12
```

Final correct map after live testing showed side buttons are physical `12/13`:

```bash
xinput set-button-map 12 1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20
xinput get-button-map 12
```

Final verification output:

```text
1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20
```

### Capture live button events

First attempt, too noisy because it included raw motion:

```bash
xinput test-xi2 --root 12
```

Better command for this case:

```bash
xinput test 12
```

Relevant result from the clean capture:

```text
button press   12
button release 12
button press   13
button release 13
```

This is the key finding: the actual physical G304 side buttons report as `12` and `13` on this host.

### Inspect `imwheel`

```bash
man imwheel | col -b | sed -n '25,42p'
man imwheel | col -b | sed -n '178,270p'
imwheel --help
strings /usr/bin/imwheel | rg 'Thumb|ExtBt|Button|Up|Down|Left|Right'
```

Important result: `imwheel -b "4 5 8 9"` is wrong for thumb buttons because it places `8/9` in the horizontal-wheel slots. The correct form is:

```bash
imwheel -b "4 5 0 0 8 9"
```

### Start, replace, and verify `imwheel`

Earlier wheel-only process:

```bash
imwheel -b "4 5"
```

Validate corrected config without staying running:

```bash
imwheel -q -b "4 5 0 0 8 9"
```

Replace stale instances and start the corrected process:

```bash
imwheel -k -b "4 5 0 0 8 9"
```

Verify host process:

```bash
ps -u loviya -o pid,comm,args | rg 'imwheel'
```

Expected relevant line:

```text
imwheel -k -b 4 5 0 0 8 9
```

## Troubleshooting Procedure

1. Identify the device id:

```bash
xinput list
```

2. Check current button map:

```bash
xinput get-button-map <device-id>
```

3. Capture actual side-button numbers:

```bash
xinput test <device-id>
```

4. Press the two side buttons once each, with minimal mouse movement.

5. Map the reported physical button numbers to logical `8/9`:

```bash
xinput set-button-map <device-id> 1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20
```

This exact command assumes side buttons are physical `12/13`. If a future capture reports different physical numbers, put `8` and `9` in those physical positions instead.

6. Persist the map in `/home/loviya/.local/bin/configure-logitech-g304`.

7. Restart `imwheel`:

```bash
imwheel -k -b "4 5 0 0 8 9"
```

## Caveats

- Device id `12` is not stable across reboots. The persistent script looks up `Logitech G304` dynamically, so use the script for login-time persistence.
- `xinput` requires access to the host X11 session. In a sandboxed Codex terminal, direct `xinput` may fail with `Unable to connect to X server`; run it with host-session permission when needed.
- Browser back/forward direction may depend on physical side-button order. If direction is reversed, swap the logical values assigned to physical `12/13`.
- `imwheel` can grab buttons and interfere with testing. Keep only one corrected `imwheel` process running.
