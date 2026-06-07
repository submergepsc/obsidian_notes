---
id: 20260525-d6f1-plot5-font-unify
name: Plot5 Font Unify
slug: plot5-font-unify
cwd: /home/loviya/code/rwa_plots
summary: 将 plot_5_scalability.py 的图例、x/y label 和 x/y tick 字号统一为原 ylabel 字号。
tags:
  - rwa_plots
  - plot5
  - scalability
  - fonts
---

# Current Snapshot

- workflow id: 20260525-d6f1-plot5-font-unify
- current status: 已完成
- current goal: 把 Plot5 quantity_vs_time 图中的 legend、xlabel、ylabel、xtick、ytick 字号全部改成当前 ylabel 的大小。
- current blocker: 无
- next step: 无
- tags: rwa_plots, plot5, scalability, fonts
- summary: 已将 Plot5 的 `AXIS_LABEL_SIZE` 改为原 ylabel 字号 `25.6`，并让 `TICK_LABEL_SIZE`、`LEGEND_FONT_SIZE` 均引用它；xlabel、ylabel、x/y tick 和 legend 字号统一。已重新生成 PoW/PoS Plot5 PDF。

# Session Notes

- 2026-05-25 13:36:57 +0800: 用户要求“把这个图的所有字体,图例,x,ylabel和x,ystick的大小都改成ylabel的大小”，延续上一张 Plot5 scalability 图。
- 2026-05-25 13:39:34 +0800: 修改 `plot_5_scalability.py`：`AXIS_LABEL_SIZE = 25.6`，`TICK_LABEL_SIZE = AXIS_LABEL_SIZE`，`LEGEND_FONT_SIZE = AXIS_LABEL_SIZE`；`ylabel` 不再乘 `0.8`。

# Verification

- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python -m py_compile plot_5_scalability.py` 通过。
- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python plot_5_scalability.py` 通过，重新生成 `figures/05_scalability/pow_quantity_vs_time.pdf` 和 `pos_quantity_vs_time.pdf`。
- `pdftoppm -png -singlefile figures/05_scalability/pow_quantity_vs_time.pdf /tmp/plot5_pow_font_unify_check` 渲染预览通过，legend、x/y label 和 x/y tick 字号已统一且未遮挡。
