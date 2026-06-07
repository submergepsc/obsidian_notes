---
id: 20260511-pyall-project-python-alias
name: Pyall Project Python Alias
slug: pyall-project-python-alias
cwd: /home/loviya/code/RWAExpResults
summary: 已更新 the pyall shell alias to run RWAExpResults plotting through the project-specific Python path.
tags:
  - RWAExpResults
  - shell
  - alias
priority: normal
---

# Pyall 项目 Python alias

## 当前快照

- 状态: 已完成
- 目标: 让 `pyall` 使用 RWAExpResults 项目的 Python 路径调用 `run_all_plots.py`。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-11 23:08:57 +0800

## 关键结果

- 已修改 `/home/loviya/.bashrc` line for `pyall` from system `python` to `/home/loviya/code/RWAExpResults/.venv/bin/python`.
- `pyall` now expands to `/home/loviya/code/RWAExpResults/.venv/bin/python /home/loviya/code/RWAExpResults/run_all_plots.py`.
- `pa` remains an alias for `pyall`.
- Verified the alias in a fresh interactive Bash shell.
- The current API session had an empty `CODEX_HOME`, not `/home/loviya/.codex-api`; no Codex runtime-home files were modified.

## 命令

- `rg -n "alias pyall|alias pa" /home/loviya/.bashrc`
- `bash -ic 'alias pyall; alias pa'`

## Pyall Should Use 项目 Python

- 更新时间: 2026-05-11 23:08:57 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `设置一下pyall的alias命令,改成指定环境的python路径调用`
- 问题:
  - `pyall` previously used whichever `python` appeared first on `PATH`, which could bypass the intended RWAExpResults environment.
- 改进:
  - 已更新 `/home/loviya/.bashrc` so `pyall` explicitly calls `/home/loviya/code/RWAExpResults/.venv/bin/python`.
- 结果:
  - New interactive Bash sessions resolve `pyall` to the project Python path and absolute `run_all_plots.py` path.
- 下一步:
  - 无
