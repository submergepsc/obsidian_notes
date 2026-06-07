---
id: 20260529-python-command-alias
name: Python command alias setup
slug: python-command-alias
cwd: /home/loviya/.codex
summary: 检查本机 Python 状态，并安装 python-is-python3 让 python 命令指向 python3。
tags:
  - python
  - apt
  - system
---

# Current Snapshot

- workflow id: 20260529-python-command-alias
- current status: 已完成
- current goal: 按用户“下载一下python”的要求，确认本机 Python 状态并补齐 `python` 命令。
- current blocker: none
- next step: none
- tags: python, apt, system
- summary: 已安装 Ubuntu 包 `python-is-python3`，现在 `python` 和 `python3` 都指向 Python 3.12.3。

# Key Results

- 已安装 `python-is-python3`。
- 验证通过：`python --version` -> `Python 3.12.3`。
- 验证通过：`python3 --version` -> `Python 3.12.3`。
- `/usr/bin/python` 现在是指向 `python3` 的符号链接。

# Commands

- `python3 --version` -> `Python 3.12.3`
- `python --version` -> command not found
- `apt-cache policy python3 python-is-python3` -> `python3` 已安装，`python-is-python3` 未安装。
- `sudo apt-get install -y python-is-python3` -> 安装成功。
