---
id: 20260506-plot5-text-size
name: Plot 5 Text Size Adjustment
slug: plot5-text-size
cwd: /home/loviya/code/RWAExpResults
summary: 缩小 Plot 5 的坐标轴、刻度和图例字号，使其更接近论文正文环境。
tags:
  - rwa-exp-results
  - plotting
  - paper-figures
priority: normal
---

# Plot 5 Text Size Adjustment

## 当前快照

- 状态: 已完成
- 目标: 让 Plot 5 图中的文字视觉上与论文周围文字保持一致。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-07 00:22:17 +0800

## 关键结果

- Reduced Plot 5 font constants in `plot_5_scalability.py`.
- Regenerated `figures/05_scalability/pos_quantity_vs_time.pdf`.
- Regenerated `figures/05_scalability/pow_quantity_vs_time.pdf`.
- Executed the full plot sequence from `run_all_plots.py` order after working around a mixed Matplotlib environment.
- Replaced the broken migrated `.venv` 带 a fresh Python `venv` and added `requirements.txt`.

## Plot 5 Font Size Should Match Paper 上下文

- 更新时间: 2026-05-07 00:22:17 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `首先把这个plot5的图片中所有文字的大小改成和周围的文本一样大`
- 问题:
  - Plot 5 axis labels, tick labels, and legends were too large after inclusion in `main.tex`.
- 改进:
  - 已修改 `AXIS_LABEL_SIZE` from 44 to 34, `TICK_LABEL_SIZE` from 38 to 28, and `LEGEND_FONT_SIZE` from 35 to 24 in `plot_5_scalability.py`.
- 结果:
  - Re-ran `python3 plot_5_scalability.py` and regenerated both Plot 5 PDF outputs.
- 下一步:
  - 无。

## Full Plot Sequence Execution Needed A Clean Import Path

- 更新时间: 2026-05-07 00:45:14 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `直接帮我执行`
- 问题:
  - Plain `python3 run_all_plots.py` failed 因为 Python loaded Matplotlib from `~/.local/lib/python3.12/site-packages` but `mpl_toolkits` from `/usr/lib/python3/dist-packages`.
  - `PYTHONNOUSERSITE=1 python3 run_all_plots.py` avoided the Matplotlib mismatch but lost user-installed pandas.
- 改进:
  - 已创建 temporary dependency links under `/tmp/rwa-python-deps` for `packaging`, `pyparsing`, `dateutil`, `PIL`, and `six.py`.
  - Ran each script in `run_all_plots.py` order 带 `PYTHONPATH=/home/loviya/.local/lib/python3.12/site-packages:/tmp/rwa-python-deps python3 -S`.
- 结果:
  - Regenerated queue, throughput, certificate, and scalability PDFs under `figures/02_queue`, `figures/03_throughput`, `figures/04_certificate`, and `figures/05_scalability`.
- 下一步:
  - If full reruns become frequent, update `run_all_plots.py` or repair the project `.venv` so the same clean environment is automatic.

## 项目 Virtualenv Recreated With venv

- 更新时间: 2026-05-07 00:50:05 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `使用删除旧的.venv ,使用venv为这个项目创建一个环境`
- 问题:
  - The existing `.venv` was migrated from a Windows path and contained a broken `bin/python3` link.
  - The global Python environment mixed user-site Matplotlib 带 system `mpl_toolkits`, causing `run_all_plots.py` to fail.
- 改进:
  - 已删除 the broken `.venv`.
  - 已创建 a fresh environment 带 `python3 -m venv .venv`.
  - 已安装 `numpy`, `pandas`, and `matplotlib`.
  - 已新增 `requirements.txt` 带 pinned top-level plotting dependencies.
- 结果:
  - `.venv/bin/python run_all_plots.py` completed successfully and regenerated all plot PDFs.
- 下一步:
  - 使用`source .venv/bin/activate` or `.venv/bin/python run_all_plots.py` for future plotting work.

## 使用Shell Activation Instead Of Script Reexec

- 更新时间: 2026-05-07 00:55:43 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `不是,你直接激活环境默认不就是这个环境的python吗`
- 问题:
  - A proposed script-level auto-reexec helper was unnecessary 因为 activating `.venv` already makes `python3` resolve to the virtualenv Python in that shell.
- 改进:
  - 已删除 the temporary `project_venv.py` helper and its imports from the plotting scripts.
  - Verified `source .venv/bin/activate && which python3` 返回 `/home/loviya/code/RWAExpResults/.venv/bin/python3`.
- 结果:
  - `source .venv/bin/activate && python3 run_all_plots.py` completed successfully.
- 下一步:
  - Activate `.venv` in the working terminal before running project Python commands.

## VS Code Workspace Uses 项目 venv

- 更新时间: 2026-05-07 00:57:36 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `设置一下吧`
- 问题:
  - 用户需要 VS Code/project settings to use the recreated `.venv` 不带 choosing it manually each time.
- 改进:
  - 已新增 `.vscode/settings.json` 带 `python.defaultInterpreterPath` set to `${workspaceFolder}/.venv/bin/python`.
  - Enabled `python.terminal.activateEnvironment`.
- 结果:
  - VS Code should select the project virtualenv and auto-activate it in new integrated terminals for this workspace.
- 下一步:
  - Reload the VS Code window or open a new integrated terminal if the current terminal does not pick up the setting immediately.

## Plot 5 Text Size Refined Further

- 更新时间: 2026-05-07 01:01:44 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `你继续上面文字的修改`
- 问题:
  - Plot 5 text still needed further adjustment after the environment setup detour.
- 改进:
  - Set `AXIS_LABEL_SIZE` to 30, `TICK_LABEL_SIZE` to 26, and `LEGEND_FONT_SIZE` to 24.
  - 已删除 the special `0.8` scaling on the y-axis label so axis titles use one consistent size.
- 结果:
  - Regenerated `figures/05_scalability/pos_quantity_vs_time.pdf` and `figures/05_scalability/pow_quantity_vs_time.pdf`.
  - Verified `source .venv/bin/activate && python3 run_all_plots.py` completes successfully.
- 下一步:
  - Review the updated PDFs in the paper layout and fine-tune again if needed.
