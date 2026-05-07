---
id: 20260506-plot5-text-size
name: Plot 5 Text Size Adjustment
slug: plot5-text-size
cwd: /home/loviya/code/RWAExpResults
summary: Reduced Plot 5 axis, tick, and legend font sizes to match surrounding paper text more closely.
tags:
  - rwa-exp-results
  - plotting
  - paper-figures
priority: normal
---

# Plot 5 Text Size Adjustment

## Current Snapshot

- status: 已完成
- goal: Make all text in Plot 5 figures visually consistent with surrounding paper text.
- blocker: 无。
- next: 无。
- updated: 2026-05-07 00:22:17 +0800

## Key Results

- Reduced Plot 5 font constants in `plot_5_scalability.py`.
- Regenerated `figures/05_scalability/pos_quantity_vs_time.pdf`.
- Regenerated `figures/05_scalability/pow_quantity_vs_time.pdf`.
- Executed the full plot sequence from `run_all_plots.py` order after working around a mixed Matplotlib environment.
- Replaced the broken migrated `.venv` with a fresh Python `venv` and added `requirements.txt`.

## Plot 5 Font Size Should Match Paper Context

- updated: 2026-05-07 00:22:17 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `首先把这个plot5的图片中所有文字的大小改成和周围的文本一样大`
- problem:
  - Plot 5 axis labels, tick labels, and legends were too large after inclusion in `main.tex`.
- improvement:
  - Changed `AXIS_LABEL_SIZE` from 44 to 34, `TICK_LABEL_SIZE` from 38 to 28, and `LEGEND_FONT_SIZE` from 35 to 24 in `plot_5_scalability.py`.
- result:
  - Re-ran `python3 plot_5_scalability.py` and regenerated both Plot 5 PDF outputs.
- next:
  - 无。

## Full Plot Sequence Execution Needed A Clean Import Path

- updated: 2026-05-07 00:45:14 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `直接帮我执行`
- problem:
  - Plain `python3 run_all_plots.py` failed because Python loaded Matplotlib from `~/.local/lib/python3.12/site-packages` but `mpl_toolkits` from `/usr/lib/python3/dist-packages`.
  - `PYTHONNOUSERSITE=1 python3 run_all_plots.py` avoided the Matplotlib mismatch but lost user-installed pandas.
- improvement:
  - Created temporary dependency links under `/tmp/rwa-python-deps` for `packaging`, `pyparsing`, `dateutil`, `PIL`, and `six.py`.
  - Ran each script in `run_all_plots.py` order with `PYTHONPATH=/home/loviya/.local/lib/python3.12/site-packages:/tmp/rwa-python-deps python3 -S`.
- result:
  - Regenerated queue, throughput, certificate, and scalability PDFs under `figures/02_queue`, `figures/03_throughput`, `figures/04_certificate`, and `figures/05_scalability`.
- next:
  - If full reruns become frequent, update `run_all_plots.py` or repair the project `.venv` so the same clean environment is automatic.

## Project Virtualenv Recreated With venv

- updated: 2026-05-07 00:50:05 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `使用删除旧的.venv ,使用venv为这个项目创建一个环境`
- problem:
  - The existing `.venv` was migrated from a Windows path and contained a broken `bin/python3` link.
  - The global Python environment mixed user-site Matplotlib with system `mpl_toolkits`, causing `run_all_plots.py` to fail.
- improvement:
  - Removed the broken `.venv`.
  - Created a fresh environment with `python3 -m venv .venv`.
  - Installed `numpy`, `pandas`, and `matplotlib`.
  - Added `requirements.txt` with pinned top-level plotting dependencies.
- result:
  - `.venv/bin/python run_all_plots.py` completed successfully and regenerated all plot PDFs.
- next:
  - Use `source .venv/bin/activate` or `.venv/bin/python run_all_plots.py` for future plotting work.

## Use Shell Activation Instead Of Script Reexec

- updated: 2026-05-07 00:55:43 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `不是,你直接激活环境默认不就是这个环境的python吗`
- problem:
  - A proposed script-level auto-reexec helper was unnecessary because activating `.venv` already makes `python3` resolve to the virtualenv Python in that shell.
- improvement:
  - Removed the temporary `project_venv.py` helper and its imports from the plotting scripts.
  - Verified `source .venv/bin/activate && which python3` returns `/home/loviya/code/RWAExpResults/.venv/bin/python3`.
- result:
  - `source .venv/bin/activate && python3 run_all_plots.py` completed successfully.
- next:
  - Activate `.venv` in the working terminal before running project Python commands.

## VS Code Workspace Uses Project venv

- updated: 2026-05-07 00:57:36 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `设置一下吧`
- problem:
  - The user wanted VS Code/project settings to use the recreated `.venv` without choosing it manually each time.
- improvement:
  - Added `.vscode/settings.json` with `python.defaultInterpreterPath` set to `${workspaceFolder}/.venv/bin/python`.
  - Enabled `python.terminal.activateEnvironment`.
- result:
  - VS Code should select the project virtualenv and auto-activate it in new integrated terminals for this workspace.
- next:
  - Reload the VS Code window or open a new integrated terminal if the current terminal does not pick up the setting immediately.

## Plot 5 Text Size Refined Further

- updated: 2026-05-07 01:01:44 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `你继续上面文字的修改`
- problem:
  - Plot 5 text still needed further adjustment after the environment setup detour.
- improvement:
  - Set `AXIS_LABEL_SIZE` to 30, `TICK_LABEL_SIZE` to 26, and `LEGEND_FONT_SIZE` to 24.
  - Removed the special `0.8` scaling on the y-axis label so axis titles use one consistent size.
- result:
  - Regenerated `figures/05_scalability/pos_quantity_vs_time.pdf` and `figures/05_scalability/pow_quantity_vs_time.pdf`.
  - Verified `source .venv/bin/activate && python3 run_all_plots.py` completes successfully.
- next:
  - Review the updated PDFs in the paper layout and fine-tune again if needed.
