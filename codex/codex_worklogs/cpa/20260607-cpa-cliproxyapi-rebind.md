---
id: 20260607-cpa-cliproxyapi-rebind
name: cpa 指向 CLIProxyAPI
slug: cpa-cliproxyapi-rebind
cwd: /home/loviya
summary: "把 shell 里的 cpa 命令从 Clash Verge 入口纠正回本机 CLIProxyAPI。"
tags:
  - cpa
  - cliproxyapi
  - shell-config
---

# Current Snapshot

- workflow id: 20260607-cpa-cliproxyapi-rebind
- current status: 进行中
- current goal: 让 `cpa` 正确指向 `/home/loviya/cpa` 下的 CLIProxyAPI 管理页。
- current blocker: sandbox 下无法直接核验 `tmux -L cpa` socket 和 `127.0.0.1:8317` 监听。
- next step: 让用户在新 shell 中执行 `source ~/.zshrc` 后再次测试 `cpa`。
- tags: cpa, cliproxyapi, shell-config
- summary: 已把 `~/.zshrc` 里的 `cpa()` 从 Clash Verge 逻辑改回 CLIProxyAPI，目标地址仍为 `http://127.0.0.1:8317/management.html`。

# Log

## 2026-06-07 20:32 +0800

- 用户明确纠正：`cpa` 是 `cliproxyapi`，不是 Clash Verge。
- 复查结果：
  - `/home/loviya/cpa` 目录存在，内含 `cli-proxy-api` 可执行文件、`config.yaml`、`README_CN.md`、`static/` 和认证目录 `.cli-proxy-api/`。
  - 旧工作流 `20260606-cliproxyapi-run-check` 记录过该服务的标准启动方式和管理页地址。
  - 当前 `~/.zshrc` 里的 `cpa()` 被误改成了 Clash Verge 入口。
- 已执行修改：
  - 把 `cpa()` 改为先检查 `http://127.0.0.1:8317/management.html`。
  - 若页面不可达，则尝试通过 `tmux -L cpa` 启动 `/home/loviya/cpa/cli-proxy-api -config /home/loviya/cpa/config.yaml`。
  - 然后轮询管理页，成功后用 `xdg-open` 打开。
- 验证：
  - `zsh -n /home/loviya/.zshrc` 通过。

