---
id: 20260503-7a9c2f-nvidia-driver-check
name: nvidia-driver-check
slug: nvidia-driver-check
cwd: /home/loviya/.local/share
summary: Checked RTX 4060 NVIDIA driver state and installed Ubuntu recommended 595 open driver because the existing 580 open driver could not communicate with nvidia-smi.
tags:
  - nvidia
  - driver
  - gpu
priority: normal
---

# NVIDIA Driver Check

## Current Snapshot

- status: 已完成
- goal: Detect NVIDIA driver state and install a driver if missing or broken.
- blocker: New 595 module is installed but current boot still has the old 580.126.09 module loaded, so `nvidia-smi` will not pass until reboot.
- next: Reboot the machine, then run `nvidia-smi` to confirm the loaded module switches to 595.58.03.
- updated: 2026-05-03 04:05:41 +0800

## Key Results

- Detected NVIDIA AD107M / GeForce RTX 4060 Max-Q Mobile at PCI `01:00.0`.
- Before repair, `lspci -nnk` showed `Kernel driver in use: nvidia`, but `nvidia-smi` failed with inability to communicate with the NVIDIA driver.
- Before repair, installed package set was `nvidia-driver-580-open` version `580.126.09-0ubuntu0.24.04.2`.
- `ubuntu-drivers devices` recommended `nvidia-driver-595-open`.
- Installed `nvidia-driver-595-open` version `595.58.03-0ubuntu0.24.04.1` with DKMS.
- DKMS status after install: `nvidia/595.58.03, 6.8.0-110-generic, x86_64: installed`.
- `modinfo nvidia` now resolves to `/lib/modules/6.8.0-110-generic/updates/dkms/nvidia.ko.zst` version `595.58.03`.
- Current boot still reports loaded module `580.126.09` in `/sys/module/nvidia/version` and `/proc/driver/nvidia/version`; reboot is required.

## Commands

- `lspci -nnk`
- `nvidia-smi`
- `ubuntu-drivers devices`
- `dpkg -l *nvidia*`
- `apt-cache policy nvidia-driver-595-open nvidia-driver-580-open nvidia-utils-595 nvidia-utils-580`
- `sudo apt-get install -y nvidia-driver-595-open`
- `dkms status`
- `modinfo nvidia`
- `cat /sys/module/nvidia/version`

## Driver Repair Result

- updated: 2026-05-03 04:05:41 +0800
- cwd: `/home/loviya/.local/share`
- source instruction: `检测一下nvidia驱动,没有就安装一个`
- problem:
  - The machine had an RTX 4060 and an installed 580 open NVIDIA driver, but `nvidia-smi` could not communicate with the driver.
  - Kernel logs included NVIDIA `NV_ERR_NO_MEMORY` failures, and the current boot lacked working NVIDIA device nodes in this sandbox view.
- improvement:
  - Installed Ubuntu recommended `nvidia-driver-595-open`, replacing most 580 packages and building the DKMS module for kernel `6.8.0-110-generic`.
- result:
  - Recommended 595 driver is installed and DKMS-built.
  - A reboot is needed because the old 580 module is still loaded in the running kernel.
- next:
  - Reboot, then run `nvidia-smi`. If it still fails after reboot, inspect `journalctl -k -b --grep=NVRM` and `/sys/module/nvidia/version` again.
