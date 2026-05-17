---
id: 20260516-b7c1-clash-anytls-config
name: Clash AnyTLS Config
slug: clash-anytls-config
cwd: /home/loviya
summary: Created a Clash YAML subscription file from user-provided AnyTLS node details.
tags:
  - clash
  - proxy
  - config
priority: normal
---

# Clash AnyTLS Config

## Current Snapshot

- status: 已完成
- goal: Create a Clash-compatible YAML file for importing an AnyTLS proxy node.
- blocker: none
- next: none
- updated: 2026-05-17 01:43:49 +0800

## Key Results

- Created `/home/loviya/frontier-anytls-clash.yaml`.
- Included the user-provided AnyTLS node settings in the config file.
- Avoided recording proxy credentials in this worklog.

## Clash Import File Created

- updated: 2026-05-17 01:43:49 +0800
- cwd: `/home/loviya`
- source instruction: `吧这个文件配置一下,然后我会导入到clash里面去`
- problem:
  - The user needed a local YAML file suitable for importing into Clash.
- improvement:
  - Wrote a complete minimal Clash configuration with mixed port, rule mode, proxy group, and routing rules.
- result:
  - The config file can be imported from `/home/loviya/frontier-anytls-clash.yaml`.
- next:
  - Import the YAML file in a Clash client that supports `anytls`.
