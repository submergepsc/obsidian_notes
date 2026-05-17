---
id: 20260515-rust-uninstall
name: Uninstall Local Rust Toolchains
slug: rust-uninstall
cwd: /home/loviya/.config/autostart
summary: Removed user-level rustup/Cargo and system apt Rust packages so Rust can be reinstalled cleanly.
tags:
  - system
  - rust
  - uninstall
priority: normal
---

# Uninstall Local Rust Toolchains

## Current Snapshot

- status: 已完成
- goal: Remove all local Rust-related install artifacts before reinstalling Rust.
- blocker: none
- next: none
- updated: 2026-05-15 13:52:00 +0800

## Key Results

- Removed rustup-managed installation under `/home/loviya/.rustup` and `/home/loviya/.cargo`.
- Purged apt packages `cargo`, `rustc`, `libstd-rust-1.75:amd64`, and `libstd-rust-dev:amd64`.
- Autoremoved no-longer-needed apt dependencies `libgit2-1.7`, `libhttp-parser2.9`, and `libllvm17t64`.
- Removed Cargo startup hooks from `/home/loviya/.bashrc` and `/home/loviya/.zshrc`.
- Verified `rustc`, `cargo`, and `rustup` no longer resolve on PATH.

## Decisions

- Treated both user-level rustup installation and system apt Rust packages as in scope because both were installed.
- Backed up shell startup files before editing: `/tmp/.bashrc.20260515-1350-rust-uninstall.bak` and `/tmp/.zshrc.20260515-1350-rust-uninstall.bak`.

## Remove Rust Before Reinstall

- updated: 2026-05-15 13:52:00 +0800
- cwd: `/home/loviya/.config/autostart`
- source instruction: `卸载本机安装的所有rust相关内容,我要重新安装`
- problem:
  - The machine had Rust installed through rustup under `/home/loviya/.cargo` and `/home/loviya/.rustup`.
  - The machine also had apt packages `cargo`, `rustc`, `libstd-rust-1.75:amd64`, and `libstd-rust-dev:amd64` installed.
- improvement:
  - Removed both installation sources and stale shell startup hooks.
- result:
  - Rust tools and packages are removed and PATH no longer resolves `rustc`, `cargo`, or `rustup`.
- next:
  - none
