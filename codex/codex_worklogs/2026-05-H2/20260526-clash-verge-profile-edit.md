---
id: 20260526-clash-verge-profile-edit
name: Clash Verge profile 配置定位与修改
slug: clash-verge-profile-edit
cwd: /home/loviya
summary: 定位 Clash Verge 中截图对应的订阅/profile 配置文件，按用户要求尝试直接修改内部 YAML，并验证结构。
tags:
  - clash
  - mihomo
  - local-config
---

# Clash Verge profile 配置定位与修改

## Current Snapshot

- workflow id: 20260526-clash-verge-profile-edit
- current status: 待继续
- current goal: 等用户切换到 `a.yaml` 后测试是否稳定；当前已完成离线配置修正。
- current blocker: 无；等待用户手动切换到 `a.yaml` 做真实运行测试。
- next step: 用户在 Clash Verge UI 手动切换到 `a.yaml`；若 Codex 仍掉线，再切回当前 profile 并继续排查生成配置。
- tags: clash, mihomo, local-config
- summary: 已离线配置好 `a.yaml`：profile 自身 `tun.enable: false`、DNS `redir-host` 和明确上游、ChatGPT/OpenAI 规则走 `ChatGPT`、末尾 `MATCH,DIRECT`；全局 `verge.yaml` 已设 `enable_tun_mode: false`，模板 `config.yaml` 已补 `tun.enable: false`。当前 profile 仍是“八戒”，未切换到 `a.yaml`。
## 2026-05-26 续接运行态验证

- 来源指令: 用户要求“继续之前a.yaml的修改”。
- 当前确认: root profile 仍保留上次 profile 级修改；`/home/loviya/temp/a.yaml` 是另一份简化 YAML，不是 UI 正在使用的 root profile。
- 运行态初查: `verge-mihomo` 正以 root 运行，参数为 `-d /root/.local/share/io.github.clash-verge-rev.clash-verge-rev -f /root/.local/share/io.github.clash-verge-rev.clash-verge-rev/clash-verge.yaml -ext-ctl-unix /tmp/verge/verge-mihomo.sock`；`127.0.0.1:9090/configs` 不可连接。
- 生成配置验证: `mode: rule`、DNS `redir-host`、明确上游 DNS、ChatGPT/OpenAI rules 和末尾 `MATCH,DIRECT` 已进入 `clash-verge.yaml`；但 `tun.enable: true` 仍由全局层生成。
- 覆盖来源: `verge.yaml` 中 `enable_tun_mode: true`，且 `ip link show Mihomo` 显示 TUN 设备仍 UP。
- 连通性验证: `nslookup deepseek.com` 与 `nslookup chatgpt.com` 均成功；`curl --noproxy` 访问 `deepseek.com` 返回 HTTP 429，访问 `chatgpt.com` 连接被重置；普通代理路径访问 `chatgpt.com` 能建立连接但返回 Cloudflare 403 challenge。
- 2026-05-26 15:45: 已按用户要求不切换当前 profile，仅离线完成 `a.yaml` 测试前配置：`config.yaml` 已备份并补 `tun.enable: false`；`profiles.yaml` 已备份并将 `a.yaml` 的 `GLOBAL` 预选从 `REJECT` 改为可用 GPT 节点；静态 YAML 解析验证 `a.yaml` 为 `mode=rule`、`tun=False`、`dns_mode=redir-host`、rules=10、last=`MATCH,DIRECT`；模板解析验证 `template_tun=False`。当前 profile 仍为 `RfTVxSyusRAv`/“八戒”。

## 2026-05-26 启动

- 来源指令: 用户截图展示 Clash Verge 订阅页，并要求“试一下，能找到这个文件吗，并且更改”。
- 隐私约束: 用户此前贴出的 YAML 包含代理节点密码；worklog、最终回复和命令输出记录都只写路径、配置键和脱敏结论。
- 初步判断: 截图是 Clash Verge 的 profile/订阅管理界面，内部文件通常位于 `~/.config/clash-verge*`、`~/.local/share/clash-verge*` 或相关 AppImage/Electron 数据目录；订阅生成文件可能会被更新订阅覆盖，若支持 merge/script，长期方案应写扩展覆写。


## 2026-05-26 DNS 接管原因

- 关键定位: 当前 Clash Verge 由 `sudo clash-verge` 启动，运行中的 `verge-mihomo` 使用 root 数据目录；UI 里的 `a.yaml` 在 `profiles.yaml` 中是 `uid=LxJFLSqFLRqj`，实际文件是 `/root/.local/share/io.github.clash-verge-rev.clash-verge-rev/profiles/LxJFLSqFLRqj.yaml`。
- 用户约束: 只允许更改 Clash 内部的 `a.yaml`；其它 Clash/Mihomo/系统配置文件只读，不写入。
- 只读检查: `resolvectl status` 显示 `Link 17 (Mihomo)` 具备 `DNS Domain: ~.`，DNS server 为 `198.18.0.2`，说明系统解析被 Mihomo 虚拟网卡接管。
- 现象解释: `ping deepseek.com` 失败在 DNS 阶段；`198.18.0.2` 是 Mihomo fake-ip/TUN DNS，不是公网 DNS。当前 `a.yaml` 使用 `nameserver: system`，在 Mihomo 接管系统 DNS 时容易回环或转发到不可用上游，导致 SERVFAIL。
- 安全注意: 不在日志中记录代理密码、订阅 token 或完整 profile 内容。


## 2026-05-26 修改 Clash 内部 a.yaml

- 修改范围: 仅写回 Clash Verge root 数据目录中 UI 名称 `a.yaml` 对应的 profile 文件 `/root/.local/share/io.github.clash-verge-rev.clash-verge-rev/profiles/LxJFLSqFLRqj.yaml`。
- 行为变更: `mode: rule`、`tun.enable: false`、DNS 改为 `redir-host`，不再使用 `nameserver: system`/`direct-nameserver: system`；ChatGPT/OpenAI 相关域名走 `ChatGPT` 组，其它流量 `MATCH,DIRECT`。
- 验证: 用 Python YAML 解析验证 `mode=rule`、`tun.enable=false`、`dns.enhanced-mode=redir-host`、nameserver 为明确 DNS、末尾规则为 `MATCH,DIRECT`。
- 注意: 没有写入 `profiles.yaml`、`clash-verge.yaml`、系统 DNS 配置或其它 profile。运行中的 Clash Verge 若未自动重新生成配置，需要在 UI 中重新应用/切换一次 `a.yaml`。
