---
id: 20260510-c8e2-plot5-worklog-restore
name: Plot5 Restore From Obsidian Worklog
slug: plot5-worklog-restore
cwd: /home/loviya/code/RWAExpResults
summary: 查询 `~/obnotes/codex_worklogs`，并将 Plot 5 恢复到最新记录的 marker-density 状态。
tags:
  - RWAExpResults
  - plotting
  - worklog
priority: normal
---

# Plot5 Restore From Obsidian 工作日志

## 当前快照

- 状态: 已完成
- 目标: 检查 Obsidian 支撑的 worklog，并把 Plot 5 恢复到此前记录的状态。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-10 15:21:00 +0800

## 关键结果

- 已确认 `~/obnotes` points to `/home/loviya/notes/obsidian_notes`.
- 已找到 relevant Plot 5 history in `~/obnotes/codex_worklogs/2026-05-06/20260506-plot5-text-size.md` and `~/obnotes/codex_worklogs/2026-05-07/20260507-run-all-plots-continue.md`.
- Restored `plot_5_scalability.py` to the latest recorded Plot 5 marker state:
  - `interval = 500`
  - `markersize = 9/6`
  - `linewidth = 4/2.5`
  - log x-axis and scientific-notation tick formatting retained
- Regenerated `figures/05_scalability/pos_quantity_vs_time.pdf` and `figures/05_scalability/pow_quantity_vs_time.pdf`.

## 验证

- `.venv/bin/python plot_5_scalability.py` completed successfully.
- `.venv/bin/python -m py_compile plot_5_scalability.py` passed.
- Rendered `figures/05_scalability/pos_quantity_vs_time.pdf` to `/tmp/plot5_pos_check.png` and visually confirmed smaller, denser markers on the log x-axis.
