---
id: 20260508-venv-python-link-rwaexp
name: Repair RWAExpResults Virtualenv Python Link
slug: rwaexp-venv-python-link
cwd: /media/windows-c/Users/15056/Desktop/code/RWAExpResults
summary: Fixed a broken .venv/bin/python chain caused by an unsupported Windows reparse-point symlink and verified plot_3_throught.py runs.
tags:
  - python
  - venv
  - rwaexpresults
  - plotting
priority: normal
---

# Repair RWAExpResults Virtualenv Python Link

## Current Snapshot

- status: 已完成
- goal: Explain and fix why `.venv/bin/python` could not be executed for `plot_3_throught.py`.
- blocker: none
- next: none
- updated: 2026-05-08 11:18:00 +0800

## Key Results

- Found `.venv/bin/python -> python3`, while `.venv/bin/python3` was an unsupported Windows reparse-point symlink.
- Replaced `.venv/bin/python3` with a Linux symlink to `/usr/bin/python3.12`.
- Verified `.venv/bin/python` reports Python 3.12.3 and can import `matplotlib`, `pandas`, and `numpy`.
- Ran `plot_3_throught.py` successfully; it generated:
  - `figures/03_throughput/throughput_stability_pos.pdf`
  - `figures/03_throughput/throughput_stability_pow.pdf`
- Restored the generated throughput PDFs back to the previous Git version at the user's request.
- Updated `plot_3_throught.py` so future PoW generation uses the original vertical broken-axis line chart instead of the newer boxplot branch.

## Broken Virtualenv Interpreter Link On Windows Mount

- updated: 2026-05-08 11:18:00 +0800
- cwd: `/media/windows-c/Users/15056/Desktop/code/RWAExpResults`
- source instruction: User ran `.venv/bin/python plot_3_throught.py` and Bash reported `没有那个文件或目录`.
- problem:
  - The venv directory existed, but the interpreter chain ended at an unsupported reparse-point symlink on the Windows-mounted filesystem.
  - `pyvenv.cfg` also showed the venv had originally been created under `/media/loviya/Windows-SSD/...`, different from the current `/media/windows-c/...` path.
- improvement:
  - Repaired only the broken interpreter symlink instead of clearing or recreating the whole virtual environment.
- commands:
  - `rm .venv/bin/python3 && ln -s /usr/bin/python3.12 .venv/bin/python3`
  - `.venv/bin/python -c "import matplotlib, pandas, numpy; print('imports ok')"`
  - `.venv/bin/python plot_3_throught.py`
- result:
  - The original command now runs successfully.
  - Matplotlib emitted a non-fatal deprecation warning: `labels` in `boxplot()` has been renamed to `tick_labels`.

## Restore Throughput Stability PDFs To Previous Version

- updated: 2026-05-08 11:22:00 +0800
- cwd: `/media/windows-c/Users/15056/Desktop/code/RWAExpResults`
- source instruction: User asked why the code/results became this way and requested `throughput_s...` images return to the previous version.
- problem:
  - Running `plot_3_throught.py` regenerated the throughput PDF outputs, changing the checked-in files.
- improvement:
  - Restored only the two requested generated PDF files from Git, leaving script edits and unrelated repository changes untouched.
- commands:
  - `git restore -- figures/03_throughput/throughput_stability_pos.pdf figures/03_throughput/throughput_stability_pow.pdf`
- result:
  - `figures/03_throughput/throughput_stability_pos.pdf` and `figures/03_throughput/throughput_stability_pow.pdf` now match the previous Git version.

## Make Plot 3 Regenerate The Original PoW Throughput Figure

- updated: 2026-05-08 11:24:00 +0800
- cwd: `/media/windows-c/Users/15056/Desktop/code/RWAExpResults`
- source instruction: User clarified that the PoW figure should be adjusted back to the original by modifying `plot_3_throught.py`.
- problem:
  - The current PoW branch had the original broken-axis line chart under `if False:` and actively generated a protocol boxplot instead.
  - Regenerating the script would therefore overwrite the restored PoW PDF with the wrong chart style again.
- improvement:
  - Removed the active PoW boxplot path and restored the original vertical broken-axis line chart path.
  - PoW now uses seconds on the x-axis with `k` tick formatting and the old large axis/legend font sizes.
  - Verification called only `plot_throughput_stability('pow', ...)` to avoid regenerating the PoS PDF.
- result:
  - `plot_3_throught.py` now regenerates `figures/03_throughput/throughput_stability_pow.pdf` in the original chart form.
  - `figures/03_throughput/throughput_stability_pos.pdf` was left untouched during this verification.
