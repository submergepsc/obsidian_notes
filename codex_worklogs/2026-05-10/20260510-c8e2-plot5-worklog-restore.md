---
id: 20260510-c8e2-plot5-worklog-restore
name: Plot5 Restore From Obsidian Worklog
slug: plot5-worklog-restore
cwd: /home/loviya/code/RWAExpResults
summary: Queried ~/obnotes/codex_worklogs and restored Plot 5 to the latest recorded marker-density state.
tags:
  - RWAExpResults
  - plotting
  - worklog
priority: normal
---

# Plot5 Restore From Obsidian Worklog

## Current Snapshot

- status: 已完成
- goal: Check the Obsidian-backed worklog and restore Plot 5 to the previously recorded state.
- blocker: none
- next: none
- updated: 2026-05-10 15:21:00 +0800

## Key Results

- Confirmed `~/obnotes` points to `/home/loviya/notes/obsidian_notes`.
- Found relevant Plot 5 history in `~/obnotes/codex_worklogs/2026-05-06/20260506-plot5-text-size.md` and `~/obnotes/codex_worklogs/2026-05-07/20260507-run-all-plots-continue.md`.
- Restored `plot_5_scalability.py` to the latest recorded Plot 5 marker state:
  - `interval = 500`
  - `markersize = 9/6`
  - `linewidth = 4/2.5`
  - log x-axis and scientific-notation tick formatting retained
- Regenerated `figures/05_scalability/pos_quantity_vs_time.pdf` and `figures/05_scalability/pow_quantity_vs_time.pdf`.

## Verification

- `.venv/bin/python plot_5_scalability.py` completed successfully.
- `.venv/bin/python -m py_compile plot_5_scalability.py` passed.
- Rendered `figures/05_scalability/pos_quantity_vs_time.pdf` to `/tmp/plot5_pos_check.png` and visually confirmed smaller, denser markers on the log x-axis.
