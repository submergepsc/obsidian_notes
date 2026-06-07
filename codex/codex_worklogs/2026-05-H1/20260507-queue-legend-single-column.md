---
id: 20260507-queue-legend-single-column
name: Queue 图例改为单列
slug: queue-legend-single-column
cwd: /home/loviya/code/RWAExpResults
summary: 将 queue dynamics 图例从两列改为一列，并重新生成 queue PDF。
tags:
  - RWAExpResults
  - plots
  - queue
priority: normal
---

# Queue 图例改为单列

## 当前快照

- 状态: 已完成
- 目标: 将 queue dynamics 图例改为单列。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-07 22:56:20 +0800

## 关键结果

- 已修改 the queue dynamics legend in `plot_2_queue.py` from `ncol=2` to `ncol=1`.
- Regenerated `figures/02_queue/queue_dynamics_pos.pdf` and `figures/02_queue/queue_dynamics_pow.pdf` 带 `python3 plot_2_queue.py`.
- Render-checked `queue_dynamics_pow.pdf`; the legend is now vertically arranged in one column.

## Queue 图图例应改为单列

- 更新时间: 2026-05-07 22:56:20 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `你自己看看这个图例,改成一列`
- 问题:
  - The queue dynamics figure legend was configured 带 two columns, making the narrow figure layout look crowded.
- 改进:
  - 已更新 the legend call to use one column and refreshed the generated PDFs.
- 结果:
  - `queue_dynamics_pos.pdf` and `queue_dynamics_pow.pdf` now show a one-column legend.
- 下一步:
  - 无。
