---
id: 20260429-linux-wechat-keeper
name: linux-wechat-keeper
slug: linux-wechat-keeper
cwd: /home/loviya
summary: 为 Linux 微信配置用户级保活服务，降低每次重新登录的概率。
tags:
  - linux
  - wechat
  - systemd
  - worklog
priority: medium
---

# linux-wechat-keeper

## Summary

为 `/usr/bin/wechat` 配置用户级保活机制：新增监督脚本、systemd user service、自启动入口，并修正桌面与应用菜单入口，确保微信退出后自动重启。

## Current Snapshot

- status: 已完成
- goal: 让 Linux 微信在桌面会话中自动启动和保活，降低每次打开都要求重新登录的概率。
- blocker: 电脑关机/断电期间进程无法后台常驻；微信是否保留登录态最终由微信客户端和服务端校验决定。
- next: 正常关机重启后登录桌面，观察微信是否自动启动并保留登录；不要用 `pkill` 强杀结果判断登录态。
- updated: 2026-04-30 13:08:00 +0800

## 让 Linux 微信进程尽量持续运行，避免因进程退出导致下次打开需要重新登录
- updated: 2026-04-29 12:52:58 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `unknown`
- source instruction: `可不可以让linux_wechat这个进程永远不要断(实际上是解决我每次打开都要重新登录的问题)`
- context: 未发现匹配的未完成 workflow；创建新 workflow。
- status: 已完成
- problem:
  - goal: 让 Linux 微信进程尽量持续运行，避免因进程退出导致下次打开需要重新登录。
  - blocker: 无。曾遇到 `~/.codex/worklogs` 在 Codex 沙箱内只读，初次未能写入 worklog；后续按用户要求补写。
- result:
  - 确认系统安装的是腾讯 Linux 微信 `wechat 4.1.1.4`，登录数据位于 `~/.xwechat`；发现用户级应用入口原本指向不存在的 `/home/loviya/run-wechat.sh`，桌面入口指向 `/home/loviya/linux_wechat.sh`。新增 `/home/loviya/.local/bin/linux-wechat-keeper`，每 20 秒检查真实微信进程，不存在则启动 `/usr/bin/wechat`；新增并启用 `/home/loviya/.config/systemd/user/linux-wechat-keeper.service`；新增 `/home/loviya/.config/autostart/linux-wechat-keeper.desktop`；同步修正 `~/.local/share/applications/wechat.desktop` 和 `~/桌面/wechat.desktop`。最终确认服务 `enabled` 且 `active`，真实用户会话内 `/usr/bin/wechat` 正在运行。
- next: 无。
- tags: linux, wechat, systemd, worklog
## 补写本次 worklog，并在 AGENTS 规则中明确只读时必须申请提升权限写入
- updated: 2026-04-29 13:43:56 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `unknown`
- source instruction: `肯定要补上啊,这是agents.md里面要求的,如果感觉没有,那么在agents.md也补上相关写入要求`
- context: 接续同一 `linux_wechat` 保活 workflow，补齐强制 worklog 记录。
- status: 已完成
- problem:
  - goal: 补写本次 worklog，并在 AGENTS 规则中明确只读时必须申请提升权限写入。
  - blocker: 无；`~/.codex/worklogs` 对当前沙箱不可写，需要使用提升权限复制 staged 文件。
- result:
  - 补写 `20260429-linux-wechat-keeper.md`，刷新 `INDEX.md`，并在 AGENTS 的 Worklog Module 中增加只读/权限受限时的处理规则。
- next: 无。
- tags: linux, wechat, systemd, worklog
## 解释并修复 Linux 微信仍反复要求登录验证的直接原因
- updated: 2026-04-29 18:47:46 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `unknown`
- source instruction: `我的微信登陆为什么还是需要验证,`
- context: 接续 `linux-wechat-keeper`，用户反馈保活后仍需微信登录验证。
- status: 已完成
- problem:
  - goal: 解释并修复 Linux 微信仍反复要求登录验证的直接原因。
  - blocker: 无。
- result:
  - 确认原配置下 `linux-wechat-keeper.service` 虽然 active，但从 18:14 起每 20 秒启动的 `/usr/bin/wechat` 都 `中止（核心已转储）`，真实微信进程不存在，因此登录态无法持续。新增桌面会话启动器 `~/.local/bin/linux-wechat-keeper-start`，让桌面自启动和菜单入口先导入图形会话环境再重启 user service；更新 keeper 脚本补 `DISPLAY`、`XAUTHORITY`、`DBUS_SESSION_BUS_ADDRESS` 兜底和无图形环境等待逻辑；同步更新 autostart、菜单和桌面入口。重载并重启服务后确认真实 `/usr/bin/wechat` 进程存在，PID `36189`。
- next: 无；如后续仍提示验证，优先检查 `/usr/bin/wechat` 是否仍在运行以及 `~/.local/state/wechat-keeper/keeper.log` 是否继续出现崩溃。
- tags: linux, wechat, systemd, autostart
## 确认 pkill -f /usr/bin/wechat 后需要重新登录是否代表保活失败
- updated: 2026-04-29 21:59:40 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `unknown`
- source instruction: `不行, pkill -f /usr/bin/wechat sleep 30 pgrep -a -u loviya wechat 执行玩这个后需要重新登陆,只是需要确认一下`
- context: 继续确认 Linux 微信保活测试方法。
- status: 已完成
- problem:
  - goal: 确认 `pkill -f /usr/bin/wechat` 后需要重新登录是否代表保活失败。
  - blocker: 无。
- result:
  - 用户执行 `pkill -f /usr/bin/wechat` 后自动重启但仍需登录。结论：`pkill` 是强制终止，等价于异常崩溃测试，微信可能主动要求重新验证；该结果只能证明 keeper 能重拉进程，不能证明或否定正常重启/桌面登录场景下能否保持登录态。
- next: 用非强杀方式验证，例如正常关窗口/注销桌面/重启后观察是否自动启动和保持登录；不要用 `pkill` 判断登录态。
- tags: linux, wechat, systemd, test

## 复查关机后免重新登录配置的当前状态和边界
- updated: 2026-04-30 13:08:00 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `unknown`
- source instruction: `之前让你配置过微信后台常驻,也就是电脑关机后,微信不用重新登陆`
- context: 接续 `linux-wechat-keeper`，复查之前配置和当前机器状态。
- status: 已完成
- problem:
  - goal: 确认之前配置过的 Linux 微信后台保活/开机恢复机制是否仍存在，以及它是否等同于关机后常驻。
  - blocker: 关机/断电后 Linux 用户进程无法继续运行；只能在下次进入桌面会话后自动启动微信并尽量沿用 `~/.xwechat` 登录态。
- result:
  - 当前 `linux-wechat-keeper.service` 仍为 `enabled` 且 `active (running)`，启动时间为 2026-04-30 13:01:38 +0800；真实 `/usr/bin/wechat` 进程存在，PID 为 `4624`。
  - 配置文件仍存在：`~/.local/bin/linux-wechat-keeper`、`~/.local/bin/linux-wechat-keeper-start`、`~/.config/systemd/user/linux-wechat-keeper.service`、`~/.config/autostart/linux-wechat-keeper.desktop`。
  - 结论：之前配置的是桌面会话内保活和开机进桌面后自动拉起，不是物理关机后的后台运行。若正常关机重启后仍要求扫码，优先检查微信客户端自己的登录态策略和 `~/.xwechat` 数据状态。
- next: 正常重启后观察是否自动启动并保留登录；不要用 `pkill -f /usr/bin/wechat` 作为免登录验证标准。
- tags: linux, wechat, systemd, autostart
