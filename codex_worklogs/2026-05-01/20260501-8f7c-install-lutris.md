---
id: 20260501-8f7c-install-lutris
name: install-lutris
slug: install-lutris
cwd: /home/loviya
summary: Installed Lutris from Ubuntu multiverse via apt and verified the package state.
tags:
  - lutris
  - wine
  - gaming
  - apt
priority: normal
---

# Install Lutris

## Current Snapshot

- status: 已完成
- goal: Install Lutris on the Ubuntu workstation for Wine/game management.
- blocker: 无
- next: 无；launch Lutris from the application menu or run `/usr/games/lutris` in a normal graphical session.
- updated: 2026-05-02 03:29:06 +0800

## Key Results

- Installed `lutris` from Ubuntu 24.04 multiverse using `sudo apt-get install -y lutris`.
- Installed package version: `0.5.14-2`.
- Verified with `dpkg-query`: `lutris 0.5.14-2 install ok installed`.
- Command path: `/usr/games/lutris`.

## Commands

- `sudo apt-get update`
- `sudo apt-get install -y lutris`
- `dpkg-query -W -f='${Package} ${Version} ${Status}\n' lutris`

## Notes

- Running `lutris --version` from the sandboxed non-GUI command context failed because it could not open display `:0`; the package installation itself is valid.
- For normal use, start Lutris from the desktop application launcher or from a graphical terminal.
