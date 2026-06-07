---
id: 20260526-a6e1-dns-fake-ip-cache
name: DNS fake-ip cache 排查
slug: dns-fake-ip-cache
cwd: /home/loviya
summary: 排查本机 Clash/Mihomo fake-ip 模式下 typo 域名仍解析到 28.0.0.0/8 并可 ping 通的原因。
tags:
  - dns
  - clash
  - mihomo
  - fake-ip
---

# DNS fake-ip cache 排查

## Current Snapshot

- workflow id: `20260526-a6e1-dns-fake-ip-cache`
- current status: `已完成`
- current goal: 检查本地 DNS 缓存和 fake-ip 映射，解释 `grok.coom` 这类域名为什么显示可 ping 通。
- current blocker: 无
- next step: 无
- tags: `dns`, `clash`, `mihomo`, `fake-ip`
- summary: 用户已启用 Clash/Mihomo `dns.enhanced-mode: fake-ip`，示例中 `chatgpt.com`、`google.com`、`grok.coom` 均解析到 `28.0.0.x` 并可本地 ping 通；需确认这是 fake-ip 虚拟地址行为还是真实 DNS 缓存。

## Session Notes

- 2026-05-26 13:29:39 +0800: 开始排查。当前 `CODEX_HOME=/home/loviya/.codex-b`，cwd 为 `/home/loviya`。
- 既有 worklog 中未找到当前 DNS/fake-ip 缓存问题的强匹配未完成 workflow；新建本 workflow。
- 注意: 用户贴出的 Clash 节点配置包含敏感字段，本 worklog 不记录节点密码、secret、完整代理配置或完整请求/响应正文。

## Commands

- `pwd`, `printenv CODEX_HOME`, `date ...`: 确认运行态。
- `rg -n "...dns/cache/clash/mihomo..." ~/.codex/worklogs ~/.codex-b/worklogs`: 查找可续接 workflow，未发现强匹配。


## Key Results

- `resolvectl status` 初始显示 `Link 12 (Mihomo)` 作为 DNS 链路，DNS server 为 `28.0.0.2`，说明系统 DNS 曾被 Mihomo/TUN 接管。
- `getent ahosts grok.coom` 与 `ping -c 1 grok.coom` 曾返回 `28.0.0.7` 并 0ms 级响应；该地址属于配置中的 fake-ip 段，不是真实公网解析。
- `resolvectl query grok.coom` 和 Mihomo 控制接口 `/dns/query?name=grok.coom&type=A` 返回 NXDOMAIN/Status 3，说明上游真实 DNS 不存在该域名。
- `/etc/resolv.conf` 指向 `127.0.0.53`；`127.0.0.53` 曾通过 Mihomo 链路返回 fake-ip，而 `127.0.0.1:53` 是 `dnsmasq` 并对该域名返回 REFUSED。
- 后续复查时 `resolvectl status` 显示 `Mihomo` 链路 `Current Scopes: none`，`resolvectl dns` 只剩 `wlp9s0: 10.42.239.149`；`getent` 无输出，`ping grok.coom` 为 `Name or service not known`。
- 当前 Mihomo `/configs` 显示 `mixed-port: 7897`、`tun.enable: false`、`ipv6: true`；这与用户贴出的 `mixed-port: 7890`、TUN/DNS接管状态不同，推测运行中的 Clash Verge 覆盖或重建了最终配置。

## Conclusion

- 结论: `grok.coom` 能 ping 通不是普通 DNS 缓存，也不是 typo 域名真实存在；是 Mihomo fake-ip/TUN 接管时给域名分配了 `28.0.0.x` 虚拟地址，ICMP 响应为本地/TUN 层行为。
- 验证: 2026-05-26 14:11 后系统 DNS 接管状态撤销，`grok.coom` 已无法通过系统 resolver 解析；正常域名 `chatgpt.com`、`google.com` 通过 `127.0.0.53` 返回真实公网 IP。
