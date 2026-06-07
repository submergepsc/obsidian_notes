---
id: 20260517-no-sleep-background-runtime
name: No Sleep Background Runtime
slug: no-sleep-background-runtime
cwd: /home/loviya
summary: 配置本机避免自动睡眠/休眠/关机，使桌面会话和后台进程尽量持续运行。
tags:
  - power
  - systemd
  - desktop
---

# 当前快照

- 工作流 ID: `20260517-no-sleep-background-runtime`
- 当前状态: `已完成`
- 当前目标: 临时禁止本机自动睡眠/休眠/关机，使后台任务不因电源管理被中断。
- 当前阻塞: none
- 下一步: none
- 标签: `power`, `systemd`, `desktop`
- 摘要: 已按用户改为临时设置。已删除本轮短暂写入的持久 systemd drop-in；当前通过 PID `719451` 的 `systemd-inhibit` 后台进程临时 block `shutdown:sleep:idle`。该设置在进程结束或系统重启后失效。

# 关键结果

- 临时 inhibitor 已启动：`systemd-inhibit --what=sleep:shutdown:idle --mode=block --who=codex --why=temporary-background-runtime sleep infinity`
- `systemd-inhibit --list` 显示 `codex` / PID `719451` / `shutdown:sleep:idle` / `block`。
- 已撤销持久配置：`/etc/systemd/logind.conf.d/99-codex-no-sleep.conf` 和 `/etc/systemd/sleep.conf.d/99-codex-disable-sleep.conf` 均不存在。
- 如需停止临时设置，可结束 PID `719451`，或执行匹配 `temporary-background-runtime` 的停止命令。

# 命令

- `gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type` -> `'nothing'`
- `gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type` -> `'suspend'`
- `gsettings get org.gnome.desktop.session idle-delay` -> `uint32 300`
- `setsid -f systemd-inhibit --what=sleep:shutdown:idle --mode=block --who=codex --why=temporary-background-runtime sleep infinity` -> started
- `systemd-inhibit --list` -> `codex` inhibitor active 带 `shutdown:sleep:idle` and `block`
