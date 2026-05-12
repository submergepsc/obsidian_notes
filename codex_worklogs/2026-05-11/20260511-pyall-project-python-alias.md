---
id: 20260511-pyall-project-python-alias
name: Pyall Project Python Alias
slug: pyall-project-python-alias
cwd: /home/loviya/code/RWAExpResults
summary: Updated the pyall shell alias to run RWAExpResults plotting through the project-specific Python path.
tags:
  - RWAExpResults
  - shell
  - alias
priority: normal
---

# Pyall Project Python Alias

## Current Snapshot

- status: 已完成
- goal: Make `pyall` call `run_all_plots.py` with the RWAExpResults project Python path.
- blocker: none
- next: none
- updated: 2026-05-11 23:08:57 +0800

## Key Results

- Changed `/home/loviya/.bashrc` line for `pyall` from system `python` to `/home/loviya/code/RWAExpResults/.venv/bin/python`.
- `pyall` now expands to `/home/loviya/code/RWAExpResults/.venv/bin/python /home/loviya/code/RWAExpResults/run_all_plots.py`.
- `pa` remains an alias for `pyall`.
- Verified the alias in a fresh interactive Bash shell.
- The current API session had an empty `CODEX_HOME`, not `/home/loviya/.codex-api`; no Codex runtime-home files were modified.

## Commands

- `rg -n "alias pyall|alias pa" /home/loviya/.bashrc`
- `bash -ic 'alias pyall; alias pa'`

## Pyall Should Use Project Python

- updated: 2026-05-11 23:08:57 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `设置一下pyall的alias命令,改成指定环境的python路径调用`
- problem:
  - `pyall` previously used whichever `python` appeared first on `PATH`, which could bypass the intended RWAExpResults environment.
- improvement:
  - Updated `/home/loviya/.bashrc` so `pyall` explicitly calls `/home/loviya/code/RWAExpResults/.venv/bin/python`.
- result:
  - New interactive Bash sessions resolve `pyall` to the project Python path and absolute `run_all_plots.py` path.
- next:
  - none
