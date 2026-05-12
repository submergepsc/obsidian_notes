---
id: 20260511-b3e7-plot4-red-left-arrow
name: Plot4 Red Left Arrow
slug: plot4-red-left-arrow
cwd: /home/loviya/code/RWAExpResults
summary: Updated plot4 certificate annotation arrow to be red, thicker, and start from the left side of the text box.
tags:
  - RWAExpResults
  - plot4
  - figure
priority: normal
---

# Plot4 Red Left Arrow

## Current Snapshot

- status: 已完成
- goal: Adjust the plot4 peak annotation arrow style and placement.
- blocker: none
- next: none
- updated: 2026-05-11 19:28:00 +0800

## Key Results

- Updated `plot_4_certifycate.py` so the peak annotation arrow starts near the left side of the text box.
- Changed the arrow color to `#d62728`, increased line width to `3.0`, and set `mutation_scale=18`.
- Regenerated `figures/04_certificate/certificate_cdf_pos.pdf` and `figures/04_certificate/certificate_cdf_pow.pdf`.
- Rendered `certificate_cdf_pow.pdf` to `/tmp/certificate_cdf_pow_check.png` for visual verification.

## Commands

- `python3 plot_4_certifycate.py`
- `pdftoppm -png -singlefile figures/04_certificate/certificate_cdf_pow.pdf /tmp/certificate_cdf_pow_check`
