---
date: 2026-05-17
area: terminal
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
  - zsh
  - nvm
  - startup-performance
source_worklog: 20260517-zsh-startup-performance
---

# Zsh 启动变慢的原因和优化结果

## 结论

这次 zsh 变慢不是 zsh 本身的问题，而是启动配置里每次都加载 `nvm.sh` 并执行 `nvm use 22`。

测量结果：

- 优化前：`zsh -ic exit` 约 `1.28s`
- 优化后：`zsh -ic exit` 约 `0.07s`
- PTY 真实终端场景：约 `0.08s`

## 主因

`zprof` 显示启动耗时主要集中在 `nvm`：

- `.zshrc` 中 `source "$NVM_DIR/nvm.sh"`
- `.zshrc` 中 `nvm use 22`
- `.zprofile` 中也重复加载 nvm

单独测量 `source nvm.sh` 和 `nvm use 22` 合计约 `0.7s`。

## 修改方式

保留 Node 22 默认可用，但不在每次启动 shell 时加载完整 nvm。

改为：

- 直接把 Node 22 的 bin 路径加入 `PATH`
- 定义 `nvm()` 懒加载函数
- 只有真正执行 `nvm` 命令时才加载 `nvm.sh`

相关文件：

- `/home/loviya/.zshrc`
- `/home/loviya/.zprofile`

核心配置：

```zsh
export NVM_DIR="$HOME/.nvm"
NVM_DEFAULT_NODE_BIN="$NVM_DIR/versions/node/v22.22.2/bin"
case ":$PATH:" in
  *":$NVM_DEFAULT_NODE_BIN:"*) ;;
  *) [ -d "$NVM_DEFAULT_NODE_BIN" ] && export PATH="$NVM_DEFAULT_NODE_BIN:$PATH" ;;
esac
unset NVM_DEFAULT_NODE_BIN

nvm() {
  unset -f nvm
  [ -s "$NVM_DIR/nvm.sh" ] && source "$NVM_DIR/nvm.sh"
  nvm "$@"
}
```

## 验证命令

```bash
/usr/bin/time -p zsh -ic exit
zsh -ic 'node -v; npm -v; command -v node; type nvm'
zsh -ic 'nvm current'
```

验证结果：

- `node -v` 为 `v22.22.2`
- `npm -v` 为 `10.9.7`
- `nvm current` 返回 `v22.22.2`

## 注意

Codex 的无 TTY 测试环境会打印 Powerlevel10k 的 `gitstatus failed to initialize`，但 PTY 真实终端测试正常。因此这不是实际终端启动慢的主因。
