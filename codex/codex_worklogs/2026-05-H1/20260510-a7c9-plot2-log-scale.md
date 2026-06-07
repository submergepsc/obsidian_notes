---
id: 20260510-a7c9-plot2-log-scale
name: Plot2 Queue Log Scale Label
slug: plot2-log-scale
cwd: /home/loviya/code/RWAExpResults
summary: 已更新 plot_2_queue.py so queue dynamics figures explicitly label the logarithmic x-axis.
tags:
  - RWAExpResults
  - plotting
  - paper-figures
priority: normal
---

# Plot2 Queue Log Scale Label

## 当前快照

- 状态: 已完成
- 目标: 在 plot2 queue dynamics x 轴上明确添加对数尺度说明。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-10 12:32:00 +0800

## 关键结果

- 已更新 `plot_2_queue.py` x-axis label from `Time (min)` to `Time (min)` plus `(log scale, base = 10)`.
- Increased the queue figure bottom margin from `0.16` to `0.23` so the two-line label is not clipped.
- Regenerated:
  - `figures/02_queue/queue_dynamics_pos.pdf`
  - `figures/02_queue/queue_dynamics_pow.pdf`

## 命令

- `python3 plot_2_queue.py`
- `pdftotext figures/02_queue/queue_dynamics_pos.pdf - | rg -n "log scale|Time|base|Queue"`
- `pdftotext figures/02_queue/queue_dynamics_pow.pdf - | rg -n "log scale|Time|base|Queue"`

## 验证

- PDF text extraction confirmed both generated queue figures include:
  - `Time (min)`
  - `(log scale, base = 10)`
