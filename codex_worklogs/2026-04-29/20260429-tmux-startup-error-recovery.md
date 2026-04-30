---
id: 20260429-tmux-startup-error-recovery
name: tmux-startup-error-recovery
slug: tmux-startup-error-recovery
cwd: /home/loviya
tags: [terminal, tmux, bashrc, recovery]
priority: normal
summary: "记录终端启动时 `(NULL):0: unknown command: tmux` 的排查、修复、验证和用户确认恢复正常。"
---



## 排查并修复每次打开终端都会显示 (NULL):0: unknown command: t...
- updated: 2026-04-29 12:59:20 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `124922-4680:0.1 /home/loviya`
- source instruction: `我现在每次打开终端,都会显示(NULL):0: unknown command: tmux,检查一下怎么一回事`
- context: 新建
- status: 已完成
- problem:
  - goal: 排查并修复每次打开终端都会显示 `(NULL):0: unknown command: tmux` 的问题，并把恢复过程记录下来。
  - blocker: 无
- result:
  - 已确认问题来自 `~/.tmux.conf` 中 `pane-focus-in` hook 的错误配置，已修复并经用户确认恢复正常。
- next: 无
- tags: terminal, tmux, bashrc, recovery
#### 错误现象

- 用户反馈：每次打开终端都会显示：

```text
(NULL):0: unknown command: tmux
```

- 用户明确表示：非常在意这些过去的错误内容，需要把错误配置如何修改并恢复正常的过程记录下来。
- 用户后续澄清：这些内容记录到 worklog，不记录到 `AGENTS.md`。

#### 排查过程

- 检查 `tmux` 是否存在：

```text
/usr/bin/tmux
```

- 结论：不是 `tmux` 未安装导致。
- 搜索启动配置中与 `tmux` 相关的内容，发现 `~/.bashrc` 中存在自动进入 tmux 的逻辑：

```bash
if command -v tmux >/dev/null 2>&1 && [ -z "$TMUX" ] && [ "$TERM" != "dumb" ]; then
    exec tmux new-session  -s "$(date +%H%M%S)-$$"
fi
```

- 进一步检查 `~/.tmux.conf`，发现第 72 行 hook 写法有问题：

```tmux
set-hook -g pane-focus-in 'if-shell "ps -o comm= -t #{pane_tty} | grep -Eq \"nano|vim|nvim\"" "tmux set -g mouse off" "tmux set -g mouse on"'
```

#### 根因

- `set-hook` 的命令体运行在 tmux 的命令解析环境内。
- 在 tmux 配置内部，`if-shell` 后面的 `"..."` 分支本来就应该是 tmux 命令。
- 因此这里不能写外部命令形式的 `tmux set -g mouse off`。
- tmux 会把 `tmux` 当作一个 tmux 内部命令名解析，但 tmux 内部没有名为 `tmux` 的命令，于是报：

```text
(NULL):0: unknown command: tmux
```

#### 实际修改

- 修改文件：`/home/loviya/.tmux.conf`
- 修改位置：第 72 行。
- 修改前：

```tmux
set-hook -g pane-focus-in 'if-shell "ps -o comm= -t #{pane_tty} | grep -Eq \"nano|vim|nvim\"" "tmux set -g mouse off" "tmux set -g mouse on"'
```

- 修改后：

```tmux
set-hook -g pane-focus-in 'if-shell "ps -o comm= -t #{pane_tty} | grep -Eq \"nano|vim|nvim\"" "set -g mouse off" "set -g mouse on"'
```

- 修改含义：去掉 hook 分支中的 `tmux` 前缀，改为直接执行 tmux 内部命令 `set -g mouse off` / `set -g mouse on`。

#### 验证过程

- 第一次执行：

```bash
tmux source-file /home/loviya/.tmux.conf
```

- 第一次重新加载时仍出现一次旧错误：

```text
(NULL):0: unknown command: tmux
```

- 判断：这是连接当前 tmux server 和加载配置时，内存中旧的 `pane-focus-in` hook 被触发造成的残留报错。
- 随后读取 tmux server 当前 hook：

```bash
tmux show-hooks -g pane-focus-in
```

- 读取结果已变为修复后的内容：

```text
pane-focus-in[0] if-shell "ps -o comm= -t #{pane_tty} | grep -Eq \"nano|vim|nvim\"" "set -g mouse off" "set -g mouse on"
```

- 第二次重新加载：

```bash
tmux source-file /home/loviya/.tmux.conf
```

- 第二次无错误输出。

#### 恢复结论

- 配置错误已修复。
- 当前 tmux server 中的 hook 已确认不再包含错误的 `tmux set -g mouse ...`。
- 第二次加载配置无错误输出。
- 用户确认：已经恢复正常。
- 本次没有写入 `AGENTS.md`；按用户纠正，记录目标改为 worklog。

## 整理 /home/loviya/.tmux.conf，去掉重复和被覆盖的配置，保持现有行...
- updated: 2026-04-29 13:45:58 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `124922-4680:0.1 /home/loviya`
- source instruction: `整理一下`
- context: 继续当前 tmux 配置维护任务。
- status: 已完成
- problem:
  - goal: 整理 `/home/loviya/.tmux.conf`，去掉重复和被覆盖的配置，保持现有行为不变。
  - blocker: 无
- result:
  - 已将 `~/.tmux.conf` 整理为 prefix、reload、panes、mouse/scroll、copy-mode、hook 六段；保留 `C-a` prefix、分屏、hjkl pane 切换、滚轮进入 copy-mode、copyq 复制和 nano/vim mouse hook。
- next: 无
- tags: terminal, tmux, bashrc, recovery
#### 整理内容

- 合并重复的 `set -g mouse on`，保留单处全局设置。
- 合并重复的 `setw -g mode-keys vi`，保留单处窗口级设置。
- 去掉早期被后续覆盖的 `WheelUpPane` 绑定，保留当前实际生效的 `#{pane_in_mode}` 版本。
- 去掉被后续覆盖的 `copy-mode-vi y send -X copy-selection`，保留当前实际生效的 `copy-pipe-and-cancel "copyq copy -"`。
- 保留已修复的 `pane-focus-in` hook，仍使用 tmux 内部命令：

```tmux
set-hook -g pane-focus-in 'if-shell "ps -o comm= -t #{pane_tty} | grep -Eq \"nano|vim|nvim\"" "set -g mouse off" "set -g mouse on"'
```

#### 验证结果

- 执行 `tmux source-file /home/loviya/.tmux.conf`，无错误输出。
- 关键选项确认：

```text
default-shell /usr/bin/bash
status-left-length 100
history-limit 100000
mouse on
prefix C-a
mode-keys vi
```

- `pane-focus-in` hook 查询结果仍为修复后的版本，不包含错误的 `tmux set -g mouse ...`。

## 修复 tmux pane 内鼠标拖选不能进入系统剪贴板的问题
- updated: 2026-04-29 14:20:38 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `124922-4680:0.1 /home/loviya`
- source instruction: `我现在在这个pane里面选择的内容,无法复制,我唯一可以复制的方式是shift+鼠标,但是这会选择所有pane里面的内容`
- context: 继续当前 tmux 配置维护任务。
- status: 已完成
- problem:
  - goal: 修复 tmux pane 内鼠标拖选不能进入系统剪贴板的问题。
  - blocker: 无
- result:
  - 已将 `copy-mode` 和 `copy-mode-vi` 的 `MouseDragEnd1Pane` 绑定到 `copyq copy -`，避免必须用 `Shift+鼠标` 绕过 tmux。
- next: 用户在 pane 内直接鼠标拖选文本并松开，验证是否能粘贴到系统剪贴板。
- tags: terminal, tmux, copyq, mouse-copy
#### 修改内容

- 问题原因：`set -g mouse on` 后，普通鼠标拖选由 tmux 接管；`Shift+鼠标` 是终端绕过 tmux 的选择方式，因此会跨 pane 选择终端屏幕内容。
- 原状态：`MouseDragEnd1Pane` 只执行 `copy-pipe-and-cancel`，没有写入系统剪贴板。
- 修改文件：`/home/loviya/.tmux.conf`
- 新增绑定：

```tmux
bind -T copy-mode MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "copyq copy -"
bind -T copy-mode-vi MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "copyq copy -"
```

#### 验证结果

- `copyq` 存在于 `/usr/bin/copyq`。
- 执行 `tmux source-file /home/loviya/.tmux.conf` 无错误输出。
- 当前生效绑定：

```text
bind-key -T copy-mode MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "copyq copy -"
bind-key -T copy-mode-vi MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "copyq copy -"
```

## 让 tmux 复制同时进入系统剪贴板和 CopyQ 历史列表
- updated: 2026-04-29 14:28:04 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `124922-4680:0.0 /home/loviya`
- source instruction: `我查看了,进入了系统剪切板,但是没有进入copyq`
- context: 继续当前 tmux 配置维护任务。
- status: 已完成
- problem:
  - goal: 让 tmux 复制同时进入系统剪贴板和 CopyQ 历史列表。
  - blocker: 无
- result:
  - 确认 `copyq copy -` 只写系统剪贴板，不保证进入 CopyQ 历史；已改为 `copyq --start-server add - && copyq --start-server select 0`。
- next: 用户在 pane 内直接鼠标拖选文本并松开，检查 CopyQ 历史和系统剪贴板是否都更新。
- tags: terminal, tmux, copyq, mouse-copy
#### 修正原因

- 用户验证发现：上一版绑定会进入系统剪贴板，但不会出现在 CopyQ 历史中。
- 本机检查时 `copyq count` 起初报错：`无法连接到服务端！请先启动 CopyQ 服务端。`
- 结论：`copyq copy -` 更接近“设置系统剪贴板”；要进入 CopyQ 历史，应使用 `copyq add -`。
- 进一步验证：`copyq --start-server add -` 会写入 CopyQ 历史，但不会自动设置系统剪贴板；`copyq --start-server select 0` 会把最新历史项设为系统剪贴板。

#### 实际修改

- 修改文件：`/home/loviya/.tmux.conf`
- 将 `y`、`Enter`、`copy-mode MouseDragEnd1Pane`、`copy-mode-vi MouseDragEnd1Pane` 都改为：

```tmux
copyq --start-server add - && copyq --start-server select 0
```

- 当前生效绑定：

```text
bind-key -T copy-mode MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "copyq --start-server add - && copyq --start-server select 0"
bind-key -T copy-mode-vi MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "copyq --start-server add - && copyq --start-server select 0"
bind-key -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "copyq --start-server add - && copyq --start-server select 0"
bind-key -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "copyq --start-server add - && copyq --start-server select 0"
```

#### 验证结果

- 临时测试确认：`copyq --start-server add - && copyq --start-server select 0` 能同时让最新文本出现在 CopyQ row 0 和系统剪贴板。
- 已删除测试用的两条临时 CopyQ 记录，并重新选择当前 CopyQ 最新真实历史项恢复剪贴板。
- 执行 `tmux source-file /home/loviya/.tmux.conf` 无错误输出。
