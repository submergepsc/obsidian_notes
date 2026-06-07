---
id: 20260503-7a9c2f-nvidia-driver-check
name: nvidia-driver-check
slug: nvidia-driver-check
cwd: /home/loviya/.local/share
summary: 已检查 RTX 4060 NVIDIA driver state and installed Ubuntu recommended 595 open driver 因为 the existing 580 open driver could not communicate 带 nvidia-smi.
tags:
  - nvidia
  - driver
  - gpu
priority: normal
---

# NVIDIA Driver 检查

## 当前快照

- 状态: 已完成
- 目标: 检测 NVIDIA 驱动状态，并在缺失或损坏时安装驱动。
- 阻塞: 595 模块已安装，但当前启动仍加载旧的 580.126.09 模块；重启前 `nvidia-smi` 不会通过。
- 下一步: 重启机器后运行 `nvidia-smi`，确认加载模块切换到 595.58.03。
- 更新时间: 2026-05-03 04:05:41 +0800

## 关键结果

- Detected NVIDIA AD107M / GeForce RTX 4060 Max-Q Mobile at PCI `01:00.0`.
- Before repair, `lspci -nnk` showed `Kernel driver in use: nvidia`, but `nvidia-smi` failed 带 inability to communicate 带 the NVIDIA driver.
- Before repair, installed package set was `nvidia-driver-580-open` version `580.126.09-0ubuntu0.24.04.2`.
- `ubuntu-drivers devices` recommended `nvidia-driver-595-open`.
- 已安装 `nvidia-driver-595-open` version `595.58.03-0ubuntu0.24.04.1` 带 DKMS.
- DKMS status after install: `nvidia/595.58.03, 6.8.0-110-generic, x86_64: installed`.
- `modinfo nvidia` now resolves to `/lib/modules/6.8.0-110-generic/updates/dkms/nvidia.ko.zst` version `595.58.03`.
- Current boot still reports loaded module `580.126.09` in `/sys/module/nvidia/version` and `/proc/driver/nvidia/version`; reboot is required.

## 命令

- `lspci -nnk`
- `nvidia-smi`
- `ubuntu-drivers devices`
- `dpkg -l *nvidia*`
- `apt-cache policy nvidia-driver-595-open nvidia-driver-580-open nvidia-utils-595 nvidia-utils-580`
- `sudo apt-get install -y nvidia-driver-595-open`
- `dkms status`
- `modinfo nvidia`
- `cat /sys/module/nvidia/version`

## Driver Repair 结果

- 更新时间: 2026-05-03 04:05:41 +0800
- 工作目录: `/home/loviya/.local/share`
- 来源指令: `检测一下nvidia驱动,没有就安装一个`
- 问题:
  - The machine had an RTX 4060 and an installed 580 open NVIDIA driver, but `nvidia-smi` could not communicate 带 the driver.
  - Kernel logs included NVIDIA `NV_ERR_NO_MEMORY` failures, and the current boot lacked working NVIDIA device nodes in this sandbox view.
- 改进:
  - 已安装 Ubuntu recommended `nvidia-driver-595-open`, replacing most 580 packages and building the DKMS module for kernel `6.8.0-110-generic`.
- 结果:
  - Recommended 595 driver is installed and DKMS-built.
  - A reboot is needed 因为 the old 580 module is still loaded in the running kernel.
- 下一步:
  - Reboot, then run `nvidia-smi`. If it still fails after reboot, inspect `journalctl -k -b --grep=NVRM` and `/sys/module/nvidia/version` again.
