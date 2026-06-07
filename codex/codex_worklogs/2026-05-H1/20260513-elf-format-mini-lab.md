---
id: 20260513-elf-format-mini-lab
name: ELF Format Mini Lab
slug: elf-format-mini-lab
cwd: /home/loviya/notes/obsidian_notes/25_2/os
summary: 已创建 an os/elf mini lab 带 a runnable ELF sample and inspection commands.
tags:
  - elf
  - cdos
  - linux
priority: normal
---

# ELF 格式小实验

## 当前快照

- 状态: 已完成
- 目标: 在操作系统学习目录 `os/elf/` 下建立一个可执行的 ELF 学习样例。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-13 22:52:00 +0800

## 关键结果

- 已创建 `os/elf/hello_elf.c`, a small C program 带 global data, read-only string data, functions, and `main`.
- 已创建 `os/elf/Makefile` 带 `make`, `make run`, `make inspect`, and `make clean`.
- 已创建 `os/elf/inspect_elf.sh` to inspect the generated executable 带 `file`, `readelf`, and `objdump`.
- 已创建 `os/elf/README.md` 带 quick commands and the main ELF sections to observe.

## 命令

- `make run`
- `make inspect`

## ELF Sample 已验证

- 更新时间: 2026-05-13 22:49:00 +0800
- 工作目录: `/home/loviya/notes/obsidian_notes/25_2/cn`
- 来源指令: `我要学习elf的格式,在cdos下面,建立一个elf目录,然后写一个相关的文件来执行,等等,反正随便一个就行`
- 问题:
  - 用户需要 a simple local ELF learning artifact under `cdos`.
- 改进:
  - 已新增 a runnable C program and helper commands that expose ELF header, section table, symbol table, and disassembly output.
- 结果:
  - `make run` printed the sample output.
  - `make inspect` confirmed an `ELF 64-bit LSB executable, x86-64` 带 visible `main`, `add`, `message`, and `global_counter` symbols.
- 下一步:
  - 无

## Move ELF Lab Into OS 笔记

- 更新时间: 2026-05-13 22:52:00 +0800
- 工作目录: `/home/loviya/notes/obsidian_notes/25_2/cn`
- 来源指令: `搞错了,放到os里面,这是操作系统的学习`
- 问题:
  - The ELF lab was first placed under `cn/cdos/elf`, but it belongs to the operating system study directory.
- 改进:
  - 已移动 the lab to `/home/loviya/notes/obsidian_notes/25_2/os/elf`.
  - 已删除 the empty `cn/cdos` directory.
- 结果:
  - `make inspect` still succeeds from the new `os/elf` location.
- 下一步:
  - 无
