---
id: 20260529-standalone-python-uv
name: Standalone Python via uv
slug: standalone-python-uv
cwd: /home/loviya/.codex
summary: 用户需要独立 Python；使用 uv 安装用户目录下的独立 CPython，而不是系统 python alias。
tags:
  - python
  - uv
  - standalone
---

# Current Snapshot

- workflow id: 20260529-standalone-python-uv
- current status: 已完成
- current goal: 安装一个独立于系统 `/usr/bin/python3` 的 Python，并给出可执行路径。
- current blocker: none
- next step: none
- tags: python, uv, standalone
- summary: 已用 uv 安装独立 CPython 3.12.13，并创建用户级 `~/.local/bin/python` 指向该独立解释器；系统 `/usr/bin/python` 仍是 3.12.3。

# Key Results

- 独立 Python 安装目录：`/home/loviya/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu`
- 便捷命令：`/home/loviya/.local/bin/python`
- 当前 shell 中 `which python` -> `/home/loviya/.local/bin/python`
- `python --version` -> `Python 3.12.13`
- `python -m pip --version` -> 独立安装目录下的 `pip 26.1.1`
- `/usr/bin/python --version` -> `Python 3.12.3`，系统 Python 未被替换。

# Commands

- `command -v uv` -> `/home/loviya/.local/bin/uv`
- `uv --version` -> `uv 0.11.15`
- `uv python install --help` -> 支持 `--install-dir` 和 managed Python 下载。
- `/home/loviya/.local/bin/uv python install 3.12` -> 下载并安装 `cpython-3.12.13-linux-x86_64-gnu`。
- `ln -s /home/loviya/.local/bin/python3.12 /home/loviya/.local/bin/python` -> 创建用户级 `python` 入口。
