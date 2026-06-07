---
id: 20260522-ob-startup-slow-audit
name: ob 启动慢排查
slug: ob-startup-slow-audit
cwd: /home/loviya/notes/obsidian_notes/25_2/cn
summary: 排查本机 `ob` 打开 Obsidian 很慢的原因，区分 shell 启动链、`ob` 函数、Obsidian vault 配置和插件/缓存影响。
tags: [obsidian, ob, zsh, startup, performance]
---

# Current Snapshot

- workflow id: `20260522-ob-startup-slow-audit`
- current status: `已完成`
- current goal: 排查 `ob` 命令打开慢，判断是否可通过缓存、裁剪启动项或调整入口改善。
- current blocker: 无
- next step: 无；重启 Obsidian 后观察冷启动体感，如仍慢再做冷启动分阶段计时。
- tags: `obsidian`, `ob`, `zsh`, `startup`, `performance`
- summary: 已确认当前 zsh 中 `ob` 是 `/home/loviya/.zshrc` 的函数，默认发送 `obsidian://open?vault=obsidian_notes`。Obsidian 已运行时，真实 `ob` 请求返回约 0.3-0.4 秒；慢感主要来自冷启动/恢复工作区阶段。已关闭 BRAT 启动更新、Obsidian Git 启动自动 pull、PDF++ 自动更新检查。

## 过程记录

- 2026-05-22：开始排查。`zsh -lic 'whence -va ob'` 显示 `ob` 是 `/home/loviya/.zshrc` 中的 shell function；同一次启动里出现 `~/.cache/oh-my-zsh` 和 `.zcompdump` 写入失败，以及 `gitstatus` 初始化失败，这可能影响 shell 启动耗时，但需与 `ob` 命令本体分开测量。
- 当前入口：
  - `/home/loviya/.zshrc` 中 `ob()` 默认目标为 `/home/loviya/notes/obsidian_notes`；目录目标会调用 `obsidian://open?vault=$(basename "$target")`。
  - `/home/loviya/.local/bin/obsidian` 是薄包装，执行 `/home/loviya/apps/obsidian-1.12.7/obsidian --no-sandbox "$@"`。
  - `x-scheme-handler/obsidian` 注册到 `obsidian.desktop`，其 `Exec` 仍是 `/home/loviya/.local/bin/obsidian %U`。
- 配置观察：
  - vault 体量约 7.7G，`rg --files` 约 16326 个文件。
  - 启用社区插件 22 个；启动相关风险点包括 BRAT 启动更新、Obsidian Git 启动 pull、PDF++ 更新检查、Copilot 侧栏和索引配置、右侧 workspace 中恢复的插件视图。
  - `obsidian.log` 显示 Obsidian 启动和运行时频繁 `Checking for update using Github`，部分时间段出现网络超时或代理失败。
  - `git status --untracked-files=no` 本地很快，但当前 repo 有大量既有变更/删除，未处理这些用户已有变更。
- 已修改：
  - `/home/loviya/notes/obsidian_notes/.obsidian/plugins/obsidian42-brat/data.json`：`updateAtStartup=false`，`updateThemesAtStartup=false`。
  - `/home/loviya/notes/obsidian_notes/.obsidian/plugins/obsidian-git/data.json`：`autoPullOnBoot=false`。
  - `/home/loviya/notes/obsidian_notes/.obsidian/plugins/pdf-plus/data.json`：`autoCheckForUpdates=false`。
- 验证：
  - 修改后用 `rg` 定点确认上述配置均为 `false`。
  - Obsidian 已运行时，真实 `zsh -lic 'ob'` 发送 `obsidian://open?vault=obsidian_notes`，两次耗时约 0.31s 和 0.39s。
  - 未关闭 Obsidian 做冷启动测试，避免打断用户当前窗口状态。
