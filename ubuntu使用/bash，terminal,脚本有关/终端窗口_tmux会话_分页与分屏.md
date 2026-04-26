你现在卡的是**三个“窗口”的概念混在一起了**，我帮你一次性彻底分清👇（这是 tmux 入门最关键的一步）
# 🧠 一张图先看懂（核心结构）
```text
系统窗口（Ctrl+Alt+T）
  ↓
tmux session（会话）
  ↓
tmux window（窗口/标签页）
  ↓
tmux pane（分屏）
```
# 🎯 1️⃣ Ctrl + Alt + T 打开的是什么？
👉 叫：
```text
终端窗口（Terminal Window）
```
✔ 是操作系统层的
✔ GNOME Terminal / Konsole 创建的
👉 每一个都是一个**独立进程**
# 🎯 2️⃣ 你自动进入 tmux 后
```text
终端窗口
  ↓
tmux session
```
👉 这个叫：
```text
tmux 会话（session）
```
✔ 你现在每开一个终端，就进一个新的 session（因为你用了动态名字）
# 🎯 3️⃣ tmux 内部的“分页”是什么？
你看到底部：
```text
[0] 0:bash  1:bash  2:obsidian*
```
👉 这个叫：
```text
tmux window（窗口）
```
👉 类似浏览器标签页
## 快捷键：
```text
Ctrl + b  c   新建 window（分页）
Ctrl + b  n   下一个
Ctrl + b  p   上一个
Ctrl + b  0-9 切换
```
# 🎯 4️⃣ tmux 内部分屏是什么？
👉 叫：
```text
tmux pane（窗格）
```
👉 一个 window 可以分成多个 pane
## 快捷键：
```text
Ctrl + b  %   左右分屏
Ctrl + b  "   上下分屏
Ctrl + b  方向键   切 pane
```
# 🎯 现在帮你对照你说的三个东西
| 你说的            | 正确名字                   |
| -------------- | ---------------------- |
| Ctrl+Alt+T 新窗口 | 终端窗口（Terminal Window）  |
| 内部新窗口          | tmux window（标签页）       |
| 分页             | 👉 其实你说的就是 tmux window |
| 分屏             | tmux pane              |
# 🧠 用一个生活类比（最清晰）
```text
电脑桌面 = 操作系统
一个终端窗口 = 一个浏览器窗口
tmux session = 一个工作空间
tmux window = 浏览器标签页
tmux pane = 一个标签页里的分屏
```
# 🎯 你现在的正确使用方式
👉 每次：
```text
Ctrl + Alt + T
```
得到：
```text
一个新的 tmux session（独立工作空间）
```
👉 在里面：
```text
Ctrl+b c     开“分页”
Ctrl+b %     分屏
```
# 🧠 为什么你之前会混乱？
因为你之前用了：
```bash
tmux new-session -A -s main
```
👉 所有终端都连到一个 session
👉 所以：
```text
多个终端窗口 = 同一个 tmux 世界
```
👉 看起来像“复制”
# 🎯 一句话总结
```text
Ctrl+Alt+T = 新终端窗口（系统级）
Ctrl+b c   = tmux 新窗口（标签页）
Ctrl+b %   = tmux 分屏
```
# 🚀 如果你想更高级一点（建议）
我可以帮你做到👇
👉 每个终端自动开 tmux + 自动三分屏
👉 每个项目一个 session
👉 打开终端直接恢复开发环境
你现在已经在“tmux正确使用门槛”上了 👍
