---
id: 20260525-e8a4-plot-protocol-colors
name: Plot Protocol Colors
slug: plot-protocol-colors
cwd: /home/loviya/code/rwa_plots
summary: 将所有主绘图脚本的协议配色统一为用户指定的 PROTOCOL_COLORS，并重新生成图表。
tags:
  - rwa_plots
  - plotting
  - colors
---

# Current Snapshot

- workflow id: 20260525-e8a4-plot-protocol-colors
- current status: 已完成
- current goal: 按用户给定的 `PROTOCOL_COLORS` 更新所有图中的协议配色。
- current blocker: 无
- next step: 无
- tags: rwa_plots, plotting, colors
- summary: 已将主绘图脚本 `plot_1_stacked_bars.py` 到 `plot_5_scalability.py` 以及 legacy/备用分析脚本中的协议色统一为用户指定映射。已重新生成 `figures/01_breakdown` 到 `figures/05_scalability` 的主 PDF。

# Session Notes

- 2026-05-25 13:46:25 +0800: 用户要求“把所有的内容改一下配色,所有的”，并提供 `PROTOCOL_COLORS` 映射。
- 已确认 `run_all_plots.py` 当前运行 `plot_2_queue.py`, `plot_3_throught.py`, `plot_4_certifycate.py`, `plot_5_scalability.py`；`plot_1_stacked_bars.py` 也存在独立主图脚本。
- 2026-05-25 13:52:05 +0800: 更新主脚本协议颜色：
  - FastOracle/committee `#DF3156`
  - Deep./deepthought `#4A0080`
  - DECEN./decentruth `#009E73`
  - DAON/daon `#56B4E9`
  - Sen./seenfeed `#E69F00`
- 同步更新 legacy/备用脚本：`plot_advanced.py`, `plot_advanced_performance.py`, `plot_comparison.py`, `plot_full_8_analysis.py`, `plot_certify.py`, `recreate_figs.py`。
- 保留非协议辅助颜色，例如 `plot_4_certifycate.py` 的红色注释箭头 `#d62728`。

# Verification

- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python -m py_compile plot_1_stacked_bars.py plot_2_queue.py plot_3_throught.py plot_4_certifycate.py plot_5_scalability.py` 通过。
- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python plot_1_stacked_bars.py` 通过，重新生成 `figures/01_breakdown/stacked_breakdown_pos.pdf` 和 `stacked_breakdown_pow.pdf`。
- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python run_all_plots.py` 通过，重新生成 plot2-plot5 主 PDF。
- `rg` 检查主脚本和已同步 legacy 脚本中协议色均为目标映射；旧协议色 `#0088B2`, `#9467bd`, `#1f77b4`, `#ff7f0e`, `#2ca02c` 不再出现。
- `pdftoppm -png -singlefile figures/05_scalability/pow_quantity_vs_time.pdf /tmp/plot_colors_plot5_pow_check` 渲染预览通过，Deep. 已显示为紫色。
- legacy 编译补充：`plot_advanced.py`, `plot_comparison.py`, `recreate_figs.py`, `plot_certify.py` 可编译；`plot_advanced_performance.py` 当前开头整体缩进导致 `IndentationError`，`plot_full_8_analysis.py` 当前含 merge conflict marker 导致 `SyntaxError`，本轮未修复这些非配色问题。
