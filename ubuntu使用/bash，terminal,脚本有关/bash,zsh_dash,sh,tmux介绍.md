sh指向dash,,都是系统脚本,命令少
zsh>bash,
tmux进行管理

你看到这么一堆 shell，其实不是“你装了一堆奇怪东西”，而是 **Linux 系统本来就自带多种 shell + 一些是同一个程序的不同入口**。我帮你拆清楚👇
# 🧠 先给你一个核心认知
👉 `/etc/shells` 只是“允许作为登录 shell 的程序列表”
👉 不代表你全部都在用
👉 甚至很多是“同一个东西的不同路径”
# 🧩 分类讲清楚（你这份列表）
## 🟢 1️⃣ 主流 shell（你真正会用的）
### 🔹 `bash`（你最熟的）
* `/bin/bash`
* `/usr/bin/bash`
👉 实际是同一个东西（路径不同）
✔ Ubuntu 默认 shell
✔ 你现在各种 `.bashrc`、alias、nvm 都是基于它
### 🔹 `zsh`（你现在在用的）
* `/bin/zsh`
* `/usr/bin/zsh`
👉 也是同一个
✔ 支持 oh-my-zsh、主题、补全更强
✔ 你之前折腾 powerlevel10k 就是这个
## 🟡 2️⃣ 系统用的轻量 shell（不是给你交互用的）
### 🔹 `sh`
* `/bin/sh`
* `/usr/bin/sh`
👉 **兼容模式入口**
📌 在 Ubuntu 里：
👉 实际指向 `dash`（不是 bash）
### 🔹 `dash`
* `/bin/dash`
* `/usr/bin/dash`
👉 超轻量 shell
✔ 启动极快
✔ 系统脚本用（比如开机脚本）
❌ 不适合你平时用（功能太少）
## 🔴 3️⃣ 限制版 shell（安全/受限环境）
### 🔹 `rbash`
* `/bin/rbash`
* `/usr/bin/rbash`
👉 Restricted Bash（受限 bash）
✔ 禁止：
* cd
* 修改 PATH
* 执行某些命令
📌 用于：
👉 限制用户权限（服务器）
❌ 你基本用不到
## 🔵 4️⃣ 特殊项（你这个比较少见）
### 🔹 `tmux`
* `/usr/bin/tmux`
👉 这个不是 shell！
👉 是终端复用器（类似“终端管理器”）
✔ 可以：
* 多窗口
* 分屏
* 后台运行 session
📌 有人会把它设为 login shell：
👉 一登录就自动进 tmux
# 🧠 为什么有 `/bin` 和 `/usr/bin` 两份？
👉 现代 Linux 的历史遗留：
* `/bin`：早期系统核心命令
* `/usr/bin`：用户程序
现在很多系统已经合并（符号链接）
👉 所以你看到“双份”，其实是同一个
# 🧪 验证一下（你可以试）
```bash
ls -l /bin/bash
ls -l /usr/bin/bash
```
你会看到：
```bash
/bin/bash -> /usr/bin/bash
```
或者反过来
# 🎯 总结你这台机器
你真正需要关心的只有：

| shell | 用途         |
| ----- | ---------- |
| bash  | 稳定、默认      |
| zsh   | 高级玩家用（你现在） |
其他：
👉 系统用 / 特殊用途 / 可以无视
# ⚠️ 重点提醒（你现在的坑）
你当前是：
👉 默认 zsh
👉 但一直在改 `.bashrc`
💥 这就是你各种问题的根源（nvm / alias / openclaw 全乱）
# 🚀 给你一个干净建议（直接上结论）
👉 二选一：
## ✅ 方案 A（推荐你现在走这个）
👉 专心用 zsh
* 用 `.zshrc`
* 别再改 `.bashrc`
## ✅ 方案 B
👉 回 bash：
```bash
chsh -s /bin/bash
```
# 🧨 最关键一句话
👉 你现在不是 shell 多
👉 是 **配置混在两个 shell 里了**
如果你愿意，我可以帮你做一件狠的👇
👉 把你现在环境（nvm / alias / fcitx / wine）整理成一套“不会再炸”的配置（zsh版）
你以后基本不会再遇到这些乱七八糟的问题。




