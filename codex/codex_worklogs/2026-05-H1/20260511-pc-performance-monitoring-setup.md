---
id: 20260511-pc-performance-monitoring-setup
name: PC Performance Monitoring Setup
slug: pc-performance-monitoring-setup
cwd: /home/loviya
summary: 安装and verify Linux CPU/performance monitoring tools.
tags:
  - system
  - performance
  - linux-tools
  - cpufreq
priority: normal
---

# PC 性能 监控 配置

## 当前快照

- 状态: 已完成
- 目标: 安装Linux performance detection tools and verify the relevant CPU/performance inspection commands.
- 阻塞: 无。
- 下一步: 无；use `sudo perf ...` or relax `kernel.perf_event_paranoid` later if full unprivileged perf profiling is required.
- 更新时间: 2026-05-11 22:26:30 +0800

## 关键结果

- Kernel: `6.8.0-111-generic`.
- 已安装/verified kernel and CPU frequency tools:
  - `linux-tools-common`
  - `linux-tools-generic`
  - `linux-tools-6.8.0-111-generic`
  - `cpufrequtils`
  - `libcpufreq0`
- 已新增 monitoring and validation tools:
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
  - `kernel.perf_event_paranoid = 4`, so unprivileged `perf` profiling is restricted. 使用sudo for full profiling unless this policy is intentionally relaxed later.

## 性能 监控 配置 已开始

- 更新时间: 2026-05-11 22:21:12 +0800
- 工作目录: `/home/loviya`
- 来源指令: `sudo apt install linux-tools-common linux-tools-generic cpufrequtils -y,我要配置一下电脑的性能检测所有相关的配置,开一个新的wroklog`
- 问题:
  - The machine needs CPU/performance monitoring utilities installed and verified.
- 改进:
  - Opened a dedicated worklog before changing system packages.
- 结果:
  - Worklog is ready to track package installation and verification commands.
- 下一步:
  - 安装packages and check command availability.

## 性能 Tooling Installed And Configured

- 更新时间: 2026-05-11 22:26:30 +0800
- 工作目录: `/home/loviya`
- 来源指令: `sudo apt install linux-tools-common linux-tools-generic cpufrequtils -y,我要配置一下电脑的性能检测所有相关的配置,开一个新的wroklog`
- 问题:
  - The machine needed kernel/performance tools, CPU frequency inspection, temperature sensors, IO/CPU historical metrics, power observation, and stress validation utilities.
- 改进:
  - 已安装 the requested packages 带 `sudo apt-get install -y linux-tools-common linux-tools-generic cpufrequtils`.
  - 已新增 related monitoring packages: `lm-sensors`, `powertop`, `iotop`, and `stress-ng`.
  - Ran `sudo sensors-detect --auto`; detected Intel `coretemp`.
  - 已新增 `coretemp` to `/etc/modules`.
  - Enabled persistent `sysstat` collection by changing `/etc/default/sysstat` to `ENABLED="true"`.
  - Enabled and started `sysstat`, `sysstat-collect.timer`, and `sysstat-summary.timer`.
- 结果:
  - Commands verified in PATH: `perf`, `cpufreq-info`, `cpufreq-set`, `turbostat`, `cpupower`, `sensors`, `iotop`, `powertop`, `stress-ng`, `iostat`, `mpstat`, `pidstat`, `sar`, `htop`, and `vmstat`.
  - `sensors` successfully reports CPU and NVMe temperatures.
  - `sar -u 1 1` and `iostat -xz 1 1` work for immediate sampling.
- 命令:
  - `sudo apt-get install -y linux-tools-common linux-tools-generic cpufrequtils`
  - `sudo apt-get install -y lm-sensors powertop iotop stress-ng`
  - `sudo sensors-detect --auto`
  - `sudo sed -i '$acoretemp' /etc/modules`
  - `sudo sed -i 's/^ENABLED="false"/ENABLED="true"/' /etc/default/sysstat`
  - `sudo systemctl enable --now sysstat sysstat-collect.timer sysstat-summary.timer`
- 下一步:
  - 无；if full user-level `perf` profiling is needed, decide whether to lower `kernel.perf_event_paranoid` from `4`.
