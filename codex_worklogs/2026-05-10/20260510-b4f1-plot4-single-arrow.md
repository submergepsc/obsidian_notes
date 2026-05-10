---
id: 20260510-b4f1-plot4-single-arrow
name: Plot4 Certificate Single Arrow
slug: plot4-single-arrow
cwd: /home/loviya/code/RWAExpResults
summary: Adjusted plot4 certificate peak annotation so only one black pointer line is drawn.
tags:
  - RWAExpResults
  - plotting
  - certificate
priority: normal
---

# Plot4 Certificate Single Arrow

## Current Snapshot

- status: 已完成
- goal: Make the black peak annotation pointer in plot4 appear only once.
- blocker: none
- next: none
- updated: 2026-05-10 14:58:00 +0800

## Key Results

- `plot_4_certifycate.py` now keeps all peak circles but draws only one `ConnectionPatch` pointer line.
- The single pointer targets the `committee` / `FastOracle` peak by default, with a fallback to the first available peak if that key is absent.
- Regenerated `figures/04_certificate/certificate_cdf_pos.pdf` and `figures/04_certificate/certificate_cdf_pow.pdf`.

## Commands

- `.venv/bin/python plot_4_certifycate.py`
- `.venv/bin/python -m py_compile plot_4_certifycate.py`
- `pdftoppm -png -singlefile -r 120 figures/04_certificate/certificate_cdf_pos.pdf /tmp/certificate_cdf_pos_check`

## Verification

- The plotting script completed successfully for POS and POW.
- `py_compile` passed using the project virtualenv Python.
- The rendered POS check image showed one black annotation pointer line.
