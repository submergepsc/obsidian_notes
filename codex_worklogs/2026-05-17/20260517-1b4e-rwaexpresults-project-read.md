---
id: 20260517-1b4e-rwaexpresults-project-read
name: RWAExpResults Project Read
slug: rwaexpresults-project-read
cwd: /home/loviya/code/RWAExpResults
summary: Read the RWAExpResults project structure, core plotting scripts, data files, and LaTeX figure references.
tags:
  - RWAExpResults
  - project-read
priority: normal
---

# RWAExpResults Project Read

## Current Snapshot

- status: 已完成
- goal: Understand the full RWAExpResults project layout and identify the main scripts, data flow, outputs, and immediate risks.
- blocker: none
- next: none
- updated: 2026-05-17 15:57:12 +0800

## Key Results

- Project is a FastOracle/RWA experiment and paper workspace containing Python plotting scripts, prepared CSV result tables, generated figure PDFs/PNGs, and `main.tex` / `main.pdf`.
- Main plotting entrypoint is `run_all_plots.py`, which runs `plot_2_queue.py`, `plot_3_throught.py`, `plot_4_certifycate.py`, and `plot_5_scalability.py`.
- `plot_1_stacked_bars.py` exists but is currently omitted from `run_all_plots.py`.
- Current LaTeX source references `figure/...`; `figure` is a symlink to `figures`, so those references resolve through the generated output directory.
- `plot_2_queue.py` currently fails Python syntax compilation at line 115 because `LogLocator(base=10.0, subs=(2.0, 5.` is incomplete.

## Decisions

- Do not edit project files during this read-only project pass.
- Report the syntax issue and project map to the user as the immediate actionable result.

## Read RWAExpResults Project Structure

- updated: 2026-05-17 15:57:12 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `读取整个项目`
- problem:
  - The user asked to read the whole project, so the useful deliverable is a project map rather than a blind dump of every file.
- improvement:
  - Inspected file list, directory layout, core scripts, CSV headers, LaTeX figure references, generated output paths, and Python syntax status.
- result:
  - Identified the core data flow: raw/backup result CSVs -> prepared aggregate CSVs -> plot scripts -> `figures/...` PDFs -> `main.tex`.
  - Found the current blocking syntax error in `plot_2_queue.py`.
- next:
  - None; if the user asks to fix or run the project, start with `plot_2_queue.py` line 115.
