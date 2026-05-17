---
id: 20260513-elf-format-mini-lab
name: ELF Format Mini Lab
slug: elf-format-mini-lab
cwd: /home/loviya/notes/obsidian_notes/25_2/os
summary: Created an os/elf mini lab with a runnable ELF sample and inspection commands.
tags:
  - elf
  - cdos
  - linux
priority: normal
---

# ELF Format Mini Lab

## Current Snapshot

- status: 已完成
- goal: 在操作系统学习目录 `os/elf/` 下建立一个可执行的 ELF 学习样例。
- blocker: none
- next: none
- updated: 2026-05-13 22:52:00 +0800

## Key Results

- Created `os/elf/hello_elf.c`, a small C program with global data, read-only string data, functions, and `main`.
- Created `os/elf/Makefile` with `make`, `make run`, `make inspect`, and `make clean`.
- Created `os/elf/inspect_elf.sh` to inspect the generated executable with `file`, `readelf`, and `objdump`.
- Created `os/elf/README.md` with quick commands and the main ELF sections to observe.

## Commands

- `make run`
- `make inspect`

## ELF Sample Verified

- updated: 2026-05-13 22:49:00 +0800
- cwd: `/home/loviya/notes/obsidian_notes/25_2/cn`
- source instruction: `我要学习elf的格式,在cdos下面,建立一个elf目录,然后写一个相关的文件来执行,等等,反正随便一个就行`
- problem:
  - The user needed a simple local ELF learning artifact under `cdos`.
- improvement:
  - Added a runnable C program and helper commands that expose ELF header, section table, symbol table, and disassembly output.
- result:
  - `make run` printed the sample output.
  - `make inspect` confirmed an `ELF 64-bit LSB executable, x86-64` with visible `main`, `add`, `message`, and `global_counter` symbols.
- next:
  - none

## Move ELF Lab Into OS Notes

- updated: 2026-05-13 22:52:00 +0800
- cwd: `/home/loviya/notes/obsidian_notes/25_2/cn`
- source instruction: `搞错了,放到os里面,这是操作系统的学习`
- problem:
  - The ELF lab was first placed under `cn/cdos/elf`, but it belongs to the operating system study directory.
- improvement:
  - Moved the lab to `/home/loviya/notes/obsidian_notes/25_2/os/elf`.
  - Removed the empty `cn/cdos` directory.
- result:
  - `make inspect` still succeeds from the new `os/elf` location.
- next:
  - none
