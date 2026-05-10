---
id: 20260510-a7c9-plot2-log-scale
name: Plot2 Queue Log Scale Label
slug: plot2-log-scale
cwd: /home/loviya/code/RWAExpResults
summary: Updated plot_2_queue.py so queue dynamics figures explicitly label the logarithmic x-axis.
tags:
  - RWAExpResults
  - plotting
  - paper-figures
priority: normal
---

# Plot2 Queue Log Scale Label

## Current Snapshot

- status: 已完成
- goal: Add an explicit log-scale note to the plot2 queue dynamics x-axis.
- blocker: none
- next: none
- updated: 2026-05-10 12:32:00 +0800

## Key Results

- Updated `plot_2_queue.py` x-axis label from `Time (min)` to `Time (min)` plus `(log scale, base = 10)`.
- Increased the queue figure bottom margin from `0.16` to `0.23` so the two-line label is not clipped.
- Regenerated:
  - `figures/02_queue/queue_dynamics_pos.pdf`
  - `figures/02_queue/queue_dynamics_pow.pdf`

## Commands

- `python3 plot_2_queue.py`
- `pdftotext figures/02_queue/queue_dynamics_pos.pdf - | rg -n "log scale|Time|base|Queue"`
- `pdftotext figures/02_queue/queue_dynamics_pow.pdf - | rg -n "log scale|Time|base|Queue"`

## Verification

- PDF text extraction confirmed both generated queue figures include:
  - `Time (min)`
  - `(log scale, base = 10)`
