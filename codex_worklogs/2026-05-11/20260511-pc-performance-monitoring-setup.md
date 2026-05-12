---
id: 20260511-pc-performance-monitoring-setup
name: PC Performance Monitoring Setup
slug: pc-performance-monitoring-setup
cwd: /home/loviya
summary: Install and verify Linux CPU/performance monitoring tools.
tags:
  - system
  - performance
  - linux-tools
  - cpufreq
priority: normal
---

# PC Performance Monitoring Setup

## Current Snapshot

- status: 已完成
- goal: Install Linux performance detection tools and verify the relevant CPU/performance inspection commands.
- blocker: none
- next: none; use `sudo perf ...` or relax `kernel.perf_event_paranoid` later if full unprivileged perf profiling is required.
- updated: 2026-05-11 22:26:30 +0800

## Key Results

- Kernel: `6.8.0-111-generic`.
- Installed/verified kernel and CPU frequency tools:
  - `linux-tools-common`
  - `linux-tools-generic`
  - `linux-tools-6.8.0-111-generic`
  - `cpufrequtils`
  - `libcpufreq0`
- Added monitoring and validation tools:
  - `lm-sensors`
  - `powertop`
  - `iotop`
  - `stress-ng`
- Existing useful tools confirmed:
  - `iostat`
  - `mpstat`
  - `pidstat`
  - `sar`
  - `htop`
  - `vmstat`
- CPU frequency driver: `intel_pstate`.
- Available CPU governors: `performance`, `powersave`.
- Current CPU policy during verification: governor `powersave`, frequency range `800 MHz` to `5.00/5.20 GHz` on P-cores and `800 MHz` to `3.70 GHz` on E-cores.
- Sensor configuration:
  - `sensors-detect --auto` detected Intel `coretemp`.
  - `/etc/modules` now includes `coretemp` for persistent CPU temperature sensor loading.
  - `sensors` reads CPU package/core temperature, NVMe temperature, ACPI, battery, and USB-C power source entries.
- Historical performance collection:
  - `/etc/default/sysstat` now has `ENABLED="true"`.
  - `sysstat`, `sysstat-collect.timer`, and `sysstat-summary.timer` are enabled and active.
- Perf caveat:
  - `kernel.perf_event_paranoid = 4`, so unprivileged `perf` profiling is restricted. Use sudo for full profiling unless this policy is intentionally relaxed later.

## Performance Monitoring Setup Started

- updated: 2026-05-11 22:21:12 +0800
- cwd: `/home/loviya`
- source instruction: `sudo apt install linux-tools-common linux-tools-generic cpufrequtils -y,我要配置一下电脑的性能检测所有相关的配置,开一个新的wroklog`
- problem:
  - The machine needs CPU/performance monitoring utilities installed and verified.
- improvement:
  - Opened a dedicated worklog before changing system packages.
- result:
  - Worklog is ready to track package installation and verification commands.
- next:
  - Install packages and check command availability.

## Performance Tooling Installed And Configured

- updated: 2026-05-11 22:26:30 +0800
- cwd: `/home/loviya`
- source instruction: `sudo apt install linux-tools-common linux-tools-generic cpufrequtils -y,我要配置一下电脑的性能检测所有相关的配置,开一个新的wroklog`
- problem:
  - The machine needed kernel/performance tools, CPU frequency inspection, temperature sensors, IO/CPU historical metrics, power observation, and stress validation utilities.
- improvement:
  - Installed the requested packages with `sudo apt-get install -y linux-tools-common linux-tools-generic cpufrequtils`.
  - Added related monitoring packages: `lm-sensors`, `powertop`, `iotop`, and `stress-ng`.
  - Ran `sudo sensors-detect --auto`; detected Intel `coretemp`.
  - Added `coretemp` to `/etc/modules`.
  - Enabled persistent `sysstat` collection by changing `/etc/default/sysstat` to `ENABLED="true"`.
  - Enabled and started `sysstat`, `sysstat-collect.timer`, and `sysstat-summary.timer`.
- result:
  - Commands verified in PATH: `perf`, `cpufreq-info`, `cpufreq-set`, `turbostat`, `cpupower`, `sensors`, `iotop`, `powertop`, `stress-ng`, `iostat`, `mpstat`, `pidstat`, `sar`, `htop`, and `vmstat`.
  - `sensors` successfully reports CPU and NVMe temperatures.
  - `sar -u 1 1` and `iostat -xz 1 1` work for immediate sampling.
- commands:
  - `sudo apt-get install -y linux-tools-common linux-tools-generic cpufrequtils`
  - `sudo apt-get install -y lm-sensors powertop iotop stress-ng`
  - `sudo sensors-detect --auto`
  - `sudo sed -i '$acoretemp' /etc/modules`
  - `sudo sed -i 's/^ENABLED="false"/ENABLED="true"/' /etc/default/sysstat`
  - `sudo systemctl enable --now sysstat sysstat-collect.timer sysstat-summary.timer`
- next:
  - none; if full user-level `perf` profiling is needed, decide whether to lower `kernel.perf_event_paranoid` from `4`.
