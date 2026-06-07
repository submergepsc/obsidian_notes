---
id: 20260524-f8c1-plot3-pos-independent-x
name: Plot3 POS Independent X Axes
slug: plot3-pos-independent-x
cwd: /home/loviya/code/rwa_plots
summary: 调整 plot_3_throught.py 的 POS throughput 分面图，让每个 High/Mid/Low 子图各自显示完整横轴长度，不再共享 x 轴。
tags:
  - rwa_plots
  - plot3
  - throughput
  - pos
---

# Current Snapshot

- workflow id: 20260524-f8c1-plot3-pos-independent-x
- current status: 已完成
- current goal: 修改 `plot_3_throught.py`，让 POS throughput 的每个分面都使用完整 0-366.67 min 横轴，并独立显示 x 轴刻度，不共享 x 轴。
- current blocker: 无
- next step: 无
- tags: rwa_plots, plot3, throughput, pos
- summary: 已确认当前问题来自 POS 分面图使用 `sharex=True`，且只对最后一个 axes 设置 xlim/x tick/label，导致上方两个分面看起来没有完整横轴。

# Session Notes

- 2026-05-24 18:34:19 +0800: 用户要求“每个部分都拓展到完整的横轴长度上，不要共享 x 轴”。截图对应 `figures/03_throughput/throughput_stability_pos.pdf`。
- 初始状态: `plot_3_throught.py`、POS/POW throughput PDF、`README.md` 已有未提交修改；本轮只处理 plot3 POS x-axis 行为，保留其他已有变更。
- 定位: `plot_3_throught.py` POS 分支当前使用 `plt.subplots(... sharex=True ...)`，并只在 `axes[-1]` 调用 `set_xlim`、设置 major locator/formatter 和 xlabel，上方分面隐藏 x tick labels。
- 修改: POS 分支改为 `sharex=False`；每个 High/Mid/Low 分面按组内数据最大时间计算独立 xlim 和 nice tick step。High/Mid/Low 都各自在横轴长度上铺开。
- 后续微调: 用户要求把完成点圆圈调大；新增 `POS_COMPLETION_RING_SIZE = 170` 和 `POS_COMPLETION_DOT_SIZE = 36`，并把外圈线宽调为 `1.6`。

# Verification

- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python -m py_compile plot_3_throught.py` 通过。
- 使用 `plot_throughput_stability('pos', target_dir)` 只重新生成 `figures/03_throughput/throughput_stability_pos.pdf`。
- `pdftoppm -png -singlefile figures/03_throughput/throughput_stability_pos.pdf /tmp/plot3_pos_bigger_circle_check` 渲染检查通过：三段横轴独立展开，完成点圆圈更大且未与标题或边框冲突。
