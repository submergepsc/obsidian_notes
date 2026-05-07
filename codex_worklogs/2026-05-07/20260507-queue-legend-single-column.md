---
id: 20260507-queue-legend-single-column
name: Queue Legend Single Column
slug: queue-legend-single-column
cwd: /home/loviya/code/RWAExpResults
summary: Adjusted the queue dynamics figure legend from two columns to one column and regenerated the queue PDFs.
tags:
  - RWAExpResults
  - plots
  - queue
priority: normal
---

# Queue Legend Single Column

## Current Snapshot

- status: 已完成
- goal: Change the queue dynamics plot legend to a single column.
- blocker: 无。
- next: 无。
- updated: 2026-05-07 22:56:20 +0800

## Key Results

- Changed the queue dynamics legend in `plot_2_queue.py` from `ncol=2` to `ncol=1`.
- Regenerated `figures/02_queue/queue_dynamics_pos.pdf` and `figures/02_queue/queue_dynamics_pow.pdf` with `python3 plot_2_queue.py`.
- Render-checked `queue_dynamics_pow.pdf`; the legend is now vertically arranged in one column.

## Queue Figure Legend Should Be Single Column

- updated: 2026-05-07 22:56:20 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `你自己看看这个图例,改成一列`
- problem:
  - The queue dynamics figure legend was configured with two columns, making the narrow figure layout look crowded.
- improvement:
  - Updated the legend call to use one column and refreshed the generated PDFs.
- result:
  - `queue_dynamics_pos.pdf` and `queue_dynamics_pow.pdf` now show a one-column legend.
- next:
  - 无。
