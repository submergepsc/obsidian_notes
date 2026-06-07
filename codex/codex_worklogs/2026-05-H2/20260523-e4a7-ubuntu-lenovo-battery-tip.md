---
id: 20260523-e4a7-ubuntu-lenovo-battery-tip
name: Ubuntu Lenovo 充电保护 tips
slug: ubuntu-lenovo-battery-tip
cwd: /home/loviya
summary: 将 Lenovo Ideapad 在 Ubuntu 中关闭 80% 停充的 conservation_mode 操作写入 codex_notes tips，并补充 AGENTS tips 路由规则。
tags:
  - ubuntu
  - tips
  - lenovo
  - battery
  - codex-notes
---

# Ubuntu Lenovo 充电保护 tips

## Current Snapshot
- workflow id: 20260523-e4a7-ubuntu-lenovo-battery-tip
- current status: 已完成
- current goal: 将 Ubuntu 中关闭 Lenovo 80% 充电保护的方法写入正确的 codex_notes tips 文件，并更新 AGENTS 路由规则
- current blocker: 无
- next step: 无
- tags: ubuntu, tips, lenovo, battery, codex-notes
- summary: 已撤销误写到 Obsidian `ubuntu_little_tips.md` 的小节，改写到 `codex_notes/tips/tips.md`；`AGENTS.md` 已明确 `tips` 请求默认路由到 codex_notes 的小 tips 文件。

## Key Results
- 正确 tips 文件：`/home/loviya/obnotes/codex/codex_notes/tips/tips.md`
- 撤销误写文件：`/home/loviya/notes/obsidian_notes/ubuntu使用/ubuntu_little_tips.md`
- 规则文件：`/home/loviya/.codex/AGENTS.md`
- 记录 Lenovo Ideapad/小新类机器的接口：`/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode`
- 记录含义：`1` 为开启电池养护/80% 停充，`0` 为关闭。

## Decisions
- 用户说 `tips` 时，默认不是普通 Obsidian tips，也不是主题笔记，而是 `~/.codex/codex_notes/tips/tips.md`。
- 顶部 `## 目录` 必须维护为所有 tips 小节的索引；新增、删除或重命名 tips 小节时同步更新目录链接。

## Verification
- 定点读取确认 `codex_notes/tips/tips.md` 新增小节存在。
- 定点读取确认 `ubuntu_little_tips.md` 中误写小节已移除。
- 定点读取确认 `AGENTS.md` 已新增 tips 路由规则和 tips 目录维护规则。
