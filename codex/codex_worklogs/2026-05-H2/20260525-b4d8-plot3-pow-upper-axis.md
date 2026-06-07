---
id: 20260525-b4d8-plot3-pow-upper-axis
name: Plot3 POW Upper Axis
slug: plot3-pow-upper-axis
cwd: /home/loviya/code/rwa_plots
summary: 调整 plot_3_throught.py 的 PoW 上方面板：y 轴刻度更宽松，x 轴范围展开到与 Deep. 面板一致但不共享轴。
tags:
  - rwa_plots
  - plot3
  - throughput
  - pow
---

# Current Snapshot

- workflow id: 20260525-b4d8-plot3-pow-upper-axis
- current status: 已完成
- current goal: 让 `plot_3_throught.py` 的 PoW 上方面板 y 轴刻度更稀疏，并把上方面板 x 轴范围改成与下方 Deep. 面板一致的 0-360 min 视图，同时保持不共享 x 轴。
- current blocker: 无
- next step: 无
- tags: rwa_plots, plot3, throughput, pow
- summary: PoW 上方面板 x 轴已改成与下方 Deep. 面板相同的 0 到 `X_MAX_SECONDS / 60` 独立范围，刻度显示到 360 min；上方面板 y 轴主刻度改成 20 TPS 一档。已重新生成 `figures/03_throughput/throughput_stability_pow.pdf`。

# Session Notes

- 2026-05-25 13:28:16 +0800: 用户要求“上面的部分的y轴图例也改的宽松一点,并且把上面的x轴的刻度也改成360的范围,和下面的一样,但是不要共用x轴”。已确认代码中 `plt.subplots(... sharex=False ...)` 已保持不共享 x 轴。
- 2026-05-25 13:30:09 +0800: 修改 `plot_3_throught.py`，新增 `POW_COMBINED_Y_TICK_STEP = 20.0`，并让 PoW 两个面板都独立设置 `x_upper, x_step = X_MAX_SECONDS / SECONDS_PER_MINUTE, X_TICK_MINUTES`。保留 `sharex=False`。

# Verification

- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python -m py_compile plot_3_throught.py` 通过。
- 只调用 `plot_throughput_stability('pow', target_dir)`，重新生成 `figures/03_throughput/throughput_stability_pow.pdf`。
- `pdftotext figures/03_throughput/throughput_stability_pow.pdf -` 显示上方面板 y 轴为 `80, 60, 40, 20, 0.00`，上下面板 x 轴均显示 `40 80 120 160 200 240 280 320 360`。
- `pdftoppm -png -singlefile figures/03_throughput/throughput_stability_pow.pdf /tmp/plot3_pow_upper_axis_check` 渲染预览通过。
