---
id: 20260517-1b4e-rwaexpresults-project-read
name: RWAExpResults Project Read
slug: rwaexpresults-project-read
cwd: /home/loviya/code/RWAExpResults
summary: 阅读 RWAExpResults 项目结构、核心绘图脚本、数据文件和 LaTeX 图表引用。
tags:
  - RWAExpResults
  - project-read
priority: normal
---

# RWAExpResults 项目 读取

## 当前快照

- 状态: 已完成
- 目标: 理解 RWAExpResults 的完整项目结构，并识别主要脚本、数据流、输出和当前风险。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-17 15:57:12 +0800

## 关键结果

- Project is a FastOracle/RWA experiment and paper workspace containing Python plotting scripts, prepared CSV result tables, generated figure PDFs/PNGs, and `main.tex` / `main.pdf`.
- Main plotting entrypoint is `run_all_plots.py`, which runs `plot_2_queue.py`, `plot_3_throught.py`, `plot_4_certifycate.py`, and `plot_5_scalability.py`.
- `plot_1_stacked_bars.py` exists but is currently omitted from `run_all_plots.py`.
- Current LaTeX source references `figure/...`; `figure` is a symlink to `figures`, so those references resolve through the generated output directory.
- `plot_2_queue.py` currently fails Python syntax compilation at line 115 因为 `LogLocator(base=10.0, subs=(2.0, 5.` is incomplete.

## 决策

- 不要edit project files during this read-only project pass.
- Report the syntax issue and project map to the user as the immediate actionable result.

## 读取 RWAExpResults 项目 Structure

- 更新时间: 2026-05-17 15:57:12 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `读取整个项目`
- 问题:
  - 用户询问 to read the whole project, so the useful deliverable is a project map rather than a blind dump of every file.
- 改进:
  - Inspected file list, directory layout, core scripts, CSV headers, LaTeX figure references, generated output paths, and Python syntax status.
- 结果:
  - Identified the core data flow: raw/backup result CSVs -> prepared aggregate CSVs -> plot scripts -> `figures/...` PDFs -> `main.tex`.
  - 已找到 the current blocking syntax error in `plot_2_queue.py`.
- 下一步:
  - 无; if the user asks to fix or run the project, start 带 `plot_2_queue.py` line 115.
