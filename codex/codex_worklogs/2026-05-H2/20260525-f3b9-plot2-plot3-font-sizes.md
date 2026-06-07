---
id: 20260525-f3b9-plot2-plot3-font-sizes
name: Plot2 Plot3 Font Sizes
slug: plot2-plot3-font-sizes
cwd: /home/loviya/code/rwa_plots
summary: 将 plot2 和 plot3 的轴标签字号设为 28，轴刻度字号设为 24，并重新生成对应 PDF。
tags:
  - rwa_plots
  - plot2
  - plot3
  - fonts
---

# Current Snapshot

- workflow id: 20260525-f3b9-plot2-plot3-font-sizes
- current status: 已完成
- current goal: 将 `plot_2_queue.py` 和 `plot_3_throught.py` 的 label 字号设为 `28`、tick 字号设为 `24`。
- current blocker: 无
- next step: 无
- tags: rwa_plots, plot2, plot3, fonts
- summary: 已将 plot2 的 `L_SIZE/T_SIZE` 改为 `28/24`；plot3 的全局、POS 和 POW 分面 label/tick 常量改为 `28/24`。为避免新字号裁切，plot2/plot3 左边距和底边距略微加宽。已重新生成 plot2 和 plot3 的 POS/POW PDF。

# Session Notes

- 2026-05-25 14:18:28 +0800: 用户要求“字体大小:标签28，刻度24把这个应用到plot3,2上面”。
- 2026-05-25 17:25:41 +0800: 修改 `plot_2_queue.py`：`L_SIZE=28`, `T_SIZE=24`，并将 `FIGURE_MARGINS` 调整为 `left=0.22`, `bottom=0.20`。修改 `plot_3_throught.py`：`AXIS_LABEL_SIZE=28`, `TICK_LABEL_SIZE=24`, `POW_PANEL_TICK_LABEL_SIZE=24`, `POS_AXIS_LABEL_SIZE=28`, `POS_TICK_LABEL_SIZE=24`，并加宽 POS/POW 左边距。

# Verification

- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python -m py_compile plot_2_queue.py plot_3_throught.py` 通过。
- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python plot_2_queue.py` 通过，重新生成 `figures/02_queue/queue_dynamics_pos.pdf` 和 `queue_dynamics_pow.pdf`。
- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python plot_3_throught.py` 通过，重新生成 `figures/03_throughput/throughput_stability_pos.pdf` 和 `throughput_stability_pow.pdf`。
- `pdftoppm` 渲染检查 `plot2_pow`, `plot3_pos`, `plot3_pow` 通过：新字号下轴标签和刻度未裁切或互相遮挡。
