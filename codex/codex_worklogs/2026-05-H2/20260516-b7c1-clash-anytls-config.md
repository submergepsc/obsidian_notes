---
id: 20260516-b7c1-clash-anytls-config
name: Clash AnyTLS Config
slug: clash-anytls-config
cwd: /home/loviya
summary: 已创建 a Clash YAML subscription file from user-provided AnyTLS node details.
tags:
  - clash
  - proxy
  - config
priority: normal
---

# Clash AnyTLS Config

## 当前快照

- 状态: 已完成
- 目标: 创建 Clash 兼容 YAML，用于导入 AnyTLS 代理节点。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-17 01:43:49 +0800

## 关键结果

- 已创建 `/home/loviya/frontier-anytls-clash.yaml`.
- Included the user-provided AnyTLS node settings in the config file.
- Avoided recording proxy credentials in this worklog.

## Clash Import File 已创建

- 更新时间: 2026-05-17 01:43:49 +0800
- 工作目录: `/home/loviya`
- 来源指令: `吧这个文件配置一下,然后我会导入到clash里面去`
- 问题:
  - 用户需要 a local YAML file suitable for importing into Clash.
- 改进:
  - Wrote a complete minimal Clash configuration 带 mixed port, rule mode, proxy group, and routing rules.
- 结果:
  - The config file can be imported from `/home/loviya/frontier-anytls-clash.yaml`.
- 下一步:
  - Import the YAML file in a Clash client that supports `anytls`.
