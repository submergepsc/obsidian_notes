---
id: 20260515-rust-uninstall
name: Uninstall Local Rust Toolchains
slug: rust-uninstall
cwd: /home/loviya/.config/autostart
summary: 已删除 user-level rustup/Cargo and system apt Rust packages so Rust can be reinstalled cleanly.
tags:
  - system
  - rust
  - uninstall
priority: normal
---

# Uninstall 本地 Rust Toolchains

## 当前快照

- 状态: 已完成
- 目标: 重装 Rust 前移除本机所有 Rust 相关安装产物。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-15 13:52:00 +0800

## 关键结果

- 已删除 rustup-managed installation under `/home/loviya/.rustup` and `/home/loviya/.cargo`.
- Purged apt packages `cargo`, `rustc`, `libstd-rust-1.75:amd64`, and `libstd-rust-dev:amd64`.
- Autoremoved no-longer-needed apt dependencies `libgit2-1.7`, `libhttp-parser2.9`, and `libllvm17t64`.
- 已删除 Cargo startup hooks from `/home/loviya/.bashrc` and `/home/loviya/.zshrc`.
- Verified `rustc`, `cargo`, and `rustup` no longer resolve on PATH.

## 决策

- Treated both user-level rustup installation and system apt Rust packages as in scope 因为 both were installed.
- Backed up shell startup files before editing: `/tmp/.bashrc.20260515-1350-rust-uninstall.bak` and `/tmp/.zshrc.20260515-1350-rust-uninstall.bak`.

## Remove Rust Before Reinstall

- 更新时间: 2026-05-15 13:52:00 +0800
- 工作目录: `/home/loviya/.config/autostart`
- 来源指令: `卸载本机安装的所有rust相关内容,我要重新安装`
- 问题:
  - The machine had Rust installed through rustup under `/home/loviya/.cargo` and `/home/loviya/.rustup`.
  - The machine also had apt packages `cargo`, `rustc`, `libstd-rust-1.75:amd64`, and `libstd-rust-dev:amd64` installed.
- 改进:
  - 已删除 both installation sources and stale shell startup hooks.
- 结果:
  - Rust tools and packages are removed and PATH no longer resolves `rustc`, `cargo`, or `rustup`.
- 下一步:
  - 无
