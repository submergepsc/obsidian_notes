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
  - piper
  - ratbagd
  - libinput
source_worklog: ~/.codex/worklogs/2026-05-H2/20260531-g304-runtime-reapply.md
updated: 2026-05-31
---

# 本机 Logitech G304 鼠标配置总览

## 一句话结论

这台机器的鼠标不是由单个工具管理，而是三层叠加：

```text
Piper/ratbagd 设备级配置
-> xinput X11 会话映射
-> imwheel 侧键快捷键转换
```

当前采用“滚轮优先可用”的保守方案：普通上下滚轮不再交给 `imwheel`，而是直接由 X11/libinput 送到应用；`imwheel` 只接管 logical `8/9` 侧键并转成 `Alt+Left` / `Alt+Right`。侧键逻辑仍有重复：`ratbagd/Piper`、`xinput`、`imwheel` 都参与了后退/前进。

## 配置文件位置速查

| 层级 | 作用 | 配置或入口位置 |
| --- | --- | --- |
| `Piper/ratbagd` | G304 设备级配置：DPI、report rate、设备级按键 | 主要通过 `piper` 图形界面和 `ratbagctl` 查看/修改；服务文件是 `/usr/lib/systemd/system/ratbagd.service` |
| `xinput` | X11 登录后修正 G304 按键映射和 libinput 属性 | 脚本：`/home/loviya/.local/bin/configure-logitech-g304`；自启动：`/home/loviya/.config/autostart/logitech-g304-buttons.desktop` |
| `imwheel` | 当前只做侧键快捷键转换；不再接管普通滚轮 `4/5` | 主配置：`/home/loviya/.imwheelrc`；自启动：`/home/loviya/.config/autostart/imwheel.desktop` |

最常改的是这两个文件：

```text
/home/loviya/.local/bin/configure-logitech-g304
/home/loviya/.imwheelrc
```

`Piper/ratbagd` 这一层一般不直接手写配置文件，优先用 `piper` 或下面命令查看：

```bash
ratbagctl list
ratbagctl hooting-chinchilla info
```

## 当前环境

- 桌面会话：X11
- 关键环境：`DISPLAY=:0`，`XDG_SESSION_TYPE=x11`，`XDG_SESSION_DESKTOP=ubuntu-xorg`
- 鼠标：`Logitech G304`
- 当前 `xinput` pointer id：`12`。这个 id 可能随重启或重插变化，所以脚本会动态查找。
- `ratbagctl` 设备名：`hooting-chinchilla: Logitech G304`。这个名字也可能在设备重新枚举后变化。

## X11 常用鼠标按钮编号

| 编号 | 常见含义 |
| ---: | --- |
| `1` | 左键 |
| `2` | 中键 / 滚轮按下 |
| `3` | 右键 |
| `4` | 垂直滚轮上滚 |
| `5` | 垂直滚轮下滚 |
| `6` | 横向滚轮左滚 |
| `7` | 横向滚轮右滚 |
| `8` | 浏览器后退 |
| `9` | 浏览器前进 |

本机 G304 的特殊点：实际物理侧键在 `xinput test` 中上报为 `12` 和 `13`，不是直观的 `8/9`。所以脚本把物理 `12/13` 映射到 logical `8/9`。

## 第 1 层：Piper / ratbagd

### 它负责什么

`Piper` 是图形界面，底层用 `ratbagd`。这一层负责 G304 的设备级配置：

- DPI 档位
- 当前 DPI
- report rate
- 鼠标设备级按键功能
- DPI 切换键

### 当前状态

`ratbagd.service` 是系统级服务，当前处于 running。当前 `ratbagctl hooting-chinchilla info` 的核心状态：

```text
Model: usb:046d:4074:0
Report Rate: 1000Hz
DPI: 800dpi active/default
DPI stages: 400 / 800 / 1600 / 3200
Button 0 -> button 1
Button 1 -> button 2
Button 2 -> button 3
Button 3 -> button 8
Button 4 -> button 9
Button 5 -> resolution-cycle-up
```

含义：设备级已经把两个侧键配置成 `button 8` 和 `button 9`，DPI 键保留为切换 DPI。

### 相关命令

```bash
ratbagctl list
ratbagctl hooting-chinchilla info
systemctl status ratbagd.service
```

如果只想用图形界面改 DPI 或鼠标设备级按键，用 `piper`。

## 第 2 层：xinput 登录脚本

### 它负责什么

`xinput` 管 X11 当前会话里的输入设备映射。它不是鼠标固件配置，而是“当前桌面会话如何解释这个鼠标”。

本机用登录脚本持久化 G304 的 X11 映射，因为设备 id 会变，登录后默认映射也可能不是想要的状态。

### 文件

```text
/home/loviya/.local/bin/configure-logitech-g304
/home/loviya/.config/autostart/logitech-g304-buttons.desktop
```

自启动入口：

```text
Exec=/home/loviya/.local/bin/configure-logitech-g304
```

脚本会动态查找 `Logitech G304` 的 pointer id，然后设置映射。

### 当前按键映射

```bash
xinput set-button-map "$device_id" 1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20
```

当前验证输出：

```text
1 2 3 4 5 6 7 8 9 10 11 8 9 14 15 16 17 18 19 20
```

关键含义：

- 物理 `1/2/3`：左键 / 中键 / 右键
- 物理 `4/5`：滚轮上 / 下
- 物理 `12/13`：本机 G304 实际侧键
- 物理 `12 -> logical 8`：浏览器后退
- 物理 `13 -> logical 9`：浏览器前进

如果侧键方向反了，改第 12、13 位，把 `8 9` 换成 `9 8`。

### libinput 属性

脚本还会设置：

```bash
xinput set-prop "$device_id" 'libinput Natural Scrolling Enabled' 0
xinput set-prop "$device_id" 'libinput High Resolution Wheel Scroll Enabled' 0
xinput set-prop "$device_id" 'libinput Scrolling Pixel Distance' 15
```

当前含义：

- 关闭自然滚动
- 关闭高精度滚轮事件，保留离散 `Button4/Button5` 滚轮事件；当前 `imwheel` 不再接管普通滚轮
- 滚轮像素距离为 `15`

### 相关命令

```bash
xinput list
xinput get-button-map 12
xinput list-props 12
xinput test 12
/home/loviya/.local/bin/configure-logitech-g304
```

`xinput test 12` 用来确认真实物理按钮编号。之前确认过本机侧键输出是：

```text
button press   12
button release 12
button press   13
button release 13
```

## 第 3 层：imwheel

### 它负责什么

`imwheel` 负责把被它抓取的鼠标按钮事件转换成别的按钮或快捷键。本机当前只让它做一件事：

- 侧键 `Thumb1/Thumb2` 转成 `Alt+Left` / `Alt+Right`

2026-05-31 因普通上下滚轮完全无法在应用中滚动，已从 `imwheel` 的接管范围中移除垂直滚轮 `4/5`。此前的 `imwheel -b "4 5 0 0 8 9"` 会抓普通滚轮；当前改为 `imwheel -b "0 0 0 0 8 9"`，让普通滚轮直接回到系统/libinput。

代价：`imwheel` 不再提供普通滚轮 1 倍归一化，也不再提供 `Shift+滚轮` 横向滚动。优先目标是保证上下滚动可靠可用。

### 文件

```text
/home/loviya/.imwheelrc
/home/loviya/.config/autostart/imwheel.desktop
```

自启动入口：

```text
Exec=imwheel -b "0 0 0 0 8 9"
```

当前运行进程形态：

```text
imwheel -k -b 0 0 0 0 8 9
```

### button-spec 解释

`imwheel -b` 的槽位顺序是固定的：

| 槽位 | imwheel 含义 | X11 按钮 | `.imwheelrc` 名称 |
| ---: | --- | ---: | --- |
| 1 | Wheel Up | `4` | `Up` |
| 2 | Wheel Down | `5` | `Down` |
| 3 | Wheel Left | `6` | `Left` |
| 4 | Wheel Right | `7` | `Right` |
| 5 | Thumb Button 1 | `8` | `Thumb1` |
| 6 | Thumb Button 2 | `9` | `Thumb2` |

当前使用：

```text
0 0 0 0 8 9
```

表示：不接管垂直滚轮 `4/5`，不接管水平滚轮 `6/7`，只用 `8/9` 作为两个侧键。前四个 `0` 很重要，不能省略。

旧方案：

```text
4 5 0 0 8 9
```

旧方案会接管垂直滚轮 `4/5`。如果应用完全滚不动，优先回到当前的 `0 0 0 0 8 9`。

错误示例：

```bash
imwheel -b "4 5 8 9"
```

这会把 `8/9` 塞进水平滚轮槽位，导致侧键解释错位。

### 当前 `.imwheelrc`

```text
".*"
None,      Thumb1, Alt_L|Left
None,      Thumb2, Alt_L|Right
```

含义：

- 侧键 1：输出 `Alt_L|Left`，通常是浏览器后退
- 侧键 2：输出 `Alt_L|Right`，通常是浏览器前进
- 普通上下滚轮：`imwheel` 不处理，直接交给系统和应用
- `Shift+滚轮`：`imwheel` 不处理，是否横向滚动取决于应用自身
- `Ctrl+滚轮`：`imwheel` 不处理，由浏览器、编辑器、Obsidian 等应用自行处理缩放

### 相关命令

```bash
sed -n '1,80p' ~/.imwheelrc
sed -n '1,80p' ~/.config/autostart/imwheel.desktop
imwheel -q -b "0 0 0 0 8 9"
imwheel -k -b "0 0 0 0 8 9"
pgrep -a -u loviya imwheel
```

## 当前完整事件流程

### 普通滚轮

```text
G304 滚轮
-> X11 button 4/5
-> xinput 保持正常滚轮方向，并关闭高精度滚轮事件
-> imwheel 不接管 4/5
-> 应用收到普通垂直滚动
```

### Shift + 滚轮

```text
G304 滚轮 + Shift
-> X11 button 4/5 + Shift_L/Shift_R
-> imwheel 不转换
-> 是否横向滚动由当前应用决定
```

### Ctrl + 滚轮

```text
G304 滚轮 + Ctrl
-> X11 button 4/5 + Ctrl
-> imwheel 不转换
-> 浏览器、编辑器、Obsidian 等应用自行处理缩放
```

### 侧键后退 / 前进

```text
G304 物理侧键
-> ratbagd/Piper 设备级设置为 button 8/9
-> xinput 登录脚本确保物理 12/13 映射为 logical 8/9
-> imwheel 把 Thumb1/Thumb2 转成 Alt+Left / Alt+Right
-> 浏览器执行后退 / 前进
```

## 已安装和未安装的相关工具

当前已安装并参与本机鼠标逻辑：

- `imwheel`
- `piper`
- `ratbagd`

本次核查未发现这些工具处于已安装接管状态：

- `input-remapper`
- `solaar`
- `xbindkeys`
- `keyd`
- `libratbag-tools`

## 重复点和简化建议

### 重复点

侧键后退/前进现在有三层参与：

```text
ratbagd/Piper: 侧键设为 button 8/9
xinput: 物理 12/13 再映射到 logical 8/9
imwheel: logical 8/9 再转成 Alt+Left / Alt+Right
```

这能提高“能用”的概率，但排错会更复杂。

### 不建议只留一个工具

单个工具很难完整替代全部功能：

- `Piper/ratbagd` 能管 DPI、report rate、设备级按键，但不适合做应用层快捷键转换。
- `xinput` 能管 X11 映射和 libinput 属性，但不能管 DPI，也不适合做复杂快捷键转换。
- `imwheel` 能管滚轮和快捷键转换，但当前只建议用来管侧键；让它接管普通滚轮时曾出现应用无法滚动。

### 更合理的目标结构

当前更合理的长期结构是两层：

```text
Piper/ratbagd: 管 G304 设备级设置、DPI、侧键为 button 8/9
xinput: 保留 G304 物理 12/13 到 logical 8/9 的登录修正，并设置 libinput 属性
imwheel: 只管侧键快捷键，不接管普通滚轮 4/5
```

`xinput` 脚本可以作为兼容补丁保留。如果确认多次重启、重插鼠标后 Piper 的设备级侧键稳定输出 `8/9`，再考虑删掉或弱化 `xinput` 侧键映射。

### 当前保守建议

现在配置已经改为滚轮优先可用：`imwheel` 不接管普通滚轮，只保留侧键快捷键转换。若要继续简化，按这个顺序测试：

1. 先从 `imwheel` 移除 `Thumb1/Thumb2` 两条侧键快捷键，测试浏览器侧键是否仍能后退/前进。
2. 如果正常，再临时跳过 `xinput set-button-map`，测试登录后侧键是否仍稳定为 `8/9`。
3. 如果仍正常，最终可只保留 `Piper/ratbagd`，或保留 `Piper/ratbagd + xinput` 作为登录兼容补丁。
4. 如果任一步失效，恢复上一层补丁。

## 常见故障处理

### 侧键方向反了

修改 `/home/loviya/.local/bin/configure-logitech-g304` 中映射的第 12、13 位：

```text
... 10 11 8 9 14 ...
```

改成：

```text
... 10 11 9 8 14 ...
```

然后运行：

```bash
/home/loviya/.local/bin/configure-logitech-g304
```

如果是 `imwheel` 层方向反，交换 `.imwheelrc` 中 `Thumb1` 和 `Thumb2` 的输出。

### Shift+滚轮没有横向滚动

当前配置为了保证普通上下滚动可靠，已经不让 `imwheel` 接管 `4/5`，所以 `Shift+滚轮` 不再由 `imwheel` 转成 `Button6/Button7`。如果以后确认普通滚轮稳定，并且确实需要恢复横向滚动，再把 `imwheel` 的 button-spec 改回 `4 5 0 0 8 9`，同时恢复对应的 `Shift_L/Shift_R` 规则。

### 滚轮太快或太慢

当前普通滚轮不由 `imwheel` 管，优先从系统或应用层调速度。先确认 G304 仍有正常离散滚轮事件：

```bash
xinput test 12
```

滚轮正常时应看到 `button press 4/5` 和 `button release 4/5`。如果只是速度不合适，不要优先把 `imwheel` 重新接回 `4/5`；之前接管普通滚轮时出现过应用完全无法滚动。

### 普通滚轮完全不能滚动

按顺序检查：

```bash
xinput list
xinput get-button-map <G304-pointer-id>
xinput list-props <G304-pointer-id>
xinput test <G304-pointer-id>
pgrep -a -u loviya imwheel
```

判断规则：

- 如果 `xinput test` 能看到 `button press 4/5`，说明硬件和 X11 设备仍在上报滚轮。
- 如果有 `4/5` 事件但应用不能滚动，优先怀疑 `imwheel` 抓取/转换层。
- 当前修复方案是让 `imwheel` 不再接管普通滚轮：

```bash
imwheel -q -b "0 0 0 0 8 9"
imwheel -k -b "0 0 0 0 8 9"
```

对应持久配置：

```text
/home/loviya/.config/autostart/imwheel.desktop
Exec=imwheel -b "0 0 0 0 8 9"
```

### 登录后侧键失效

按顺序检查：

```bash
xinput list
xinput get-button-map <G304-pointer-id>
pgrep -a -u loviya imwheel
ratbagctl list
ratbagctl <device-name> info
```

然后重新应用：

```bash
/home/loviya/.local/bin/configure-logitech-g304
imwheel -k -b "0 0 0 0 8 9"
```

### 重新确认物理侧键编号

```bash
xinput list
xinput test <G304-pointer-id>
```

分别按两个侧键。当前这台机器历史确认结果是 `12` 和 `13`。

## 重要文件清单

```text
/home/loviya/.local/bin/configure-logitech-g304
/home/loviya/.config/autostart/logitech-g304-buttons.desktop
/home/loviya/.imwheelrc
/home/loviya/.config/autostart/imwheel.desktop
```

## 最小验证清单

```bash
env | rg 'DISPLAY|XAUTHORITY|XDG_SESSION|WAYLAND|DBUS'
xinput list
xinput get-button-map 12
xinput list-props 12
ratbagctl list
ratbagctl hooting-chinchilla info
systemctl status ratbagd.service
imwheel -q -b "0 0 0 0 8 9"
pgrep -a -u loviya imwheel
```

## 当前维护原则

- DPI、report rate、设备级侧键：优先用 Piper/ratbagd。
- X11 会话中物理按钮编号不对：用 `xinput` 脚本修正。
- 普通滚轮 `4/5`：当前不交给 `imwheel`，优先保证应用能直接滚动。
- 侧键快捷键转换：当前由 `imwheel` 处理 logical `8/9` 到 `Alt+Left/Right`。
- 不要同时在多个地方做无意义的相同转换；但在确认稳定前，保留现有补丁比贸然删除更稳。
