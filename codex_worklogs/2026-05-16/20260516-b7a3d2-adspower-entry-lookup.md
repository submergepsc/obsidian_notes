---
id: 20260516-b7a3d2-adspower-entry-lookup
name: AdsPower Entry Lookup
slug: adspower-entry-lookup
cwd: /home/loviya
summary: Locate how to open the local AdsPower browser installation.
tags:
  - adspower
  - browser
  - desktop-entry
priority: normal
---

# AdsPower Entry Lookup

## Current Snapshot

- status: 已完成
- goal: Find how to enter/open the local ADS browser.
- blocker: none
- next: none
- updated: 2026-05-16 21:06:40 +0800

## Key Results

- The installed ADS browser is `AdsPower Browser`.
- Desktop launcher: `/usr/share/applications/adspower_global.desktop`
- Launcher command: `"/opt/AdsPower Global/adspower_global" %U`
- Actual executable: `/opt/AdsPower Global/adspower_global`
- PATH command wrapper: `/home/loviya/.local/bin/adspower`
- User data/config directory exists at `/home/loviya/.config/adspower_global`.

## Decisions

- Prefer launching from the desktop app menu by searching `AdsPower Browser`, or from terminal with `adspower`.
- Use the absolute executable path only if the PATH wrapper is unavailable.

## Locate AdsPower Browser Entry

- updated: 2026-05-16 21:06:40 +0800
- cwd: `/home/loviya`
- source instruction: `查找一下本机的ads浏览器怎么进入`
- problem:
  - The user needed the local entry point for the ADS browser.
- improvement:
  - Searched desktop files, local commands, and install directories for ADS/AdsPower-related entries.
- result:
  - Found `AdsPower Browser` installed under `/opt/AdsPower Global/` with a desktop launcher and terminal command.
- next:
  - none
