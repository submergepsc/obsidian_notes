# AI API 中转站汇总

> 收集来源: [relayAPI (zzsting88)](https://github.com/zzsting88/relayAPI) 推荐与评测、[Veridrop](https://github.com/canarybyte/veridrop) 检测工具
> 整理时间: 2026-05-15
> 注意: 中转站行业不稳定，不要大额充值，用多少充多少

## 推荐的中转站

### 编程类

| 站点                                                         | 支持模型                           | 特点                                                      |
| ---------------------------------------------------------- | ------------------------------ | ------------------------------------------------------- |
| [PackyCode](https://www.packyapi.com/register?aff=gF1p)    | Claude, GPT, Gemini, 国产模型      | 对 Claude Code 优化好，上游供应商；Sonnet4.6 ¥2.4~7.5/进 ¥12~37.5/出 |
| [RightCode](https://co.right.vg/register?ref=g3sd)         | Claude, Gemini, GPT            | 只支持编程；Opus4.6 ¥7.5/进 37.5/出；GPT5.5 ¥1/进 ¥6/出（主力推荐）      |
| [SSSAICode](https://www.sssaicode.com/register?ref=BO64DM) | Claude, GPT, Gemini            | 编程向，文档完善                                                |
| [SparkCode](https://sparkcode.top/register?aff=EYOo)       | Claude, Gemini, GPT, Kimi, GLM | Sonnet4.6 ¥3/进 ¥15/出                                    |
| [IKunCode](https://api.ikuncode.cc/)                       | Claude, GPT, Gemini            | 专注编程，仅按量计费                                              |
| [XcodeBest](https://xcode.best/register?aff=mLST)          | Claude, GPT                    | 新站，价格便宜                                                 |
| [Terminal.Pub](https://terminal.pub/register?aff=rJW5)     | Claude, GPT, Gemini            | 超低价，甚至有免费组                                              |
| [TimiCC](https://timicc.com/register?ref=2CT3TAP7)         | GPT(Codex), Claude             | 2026年1月成立                                               |
| [YesCode](https://co.yes.vg/register?ref=gasd)             | Claude, GPT, Gemini            | Opus4.6 官网2折                                            |
| [发现AI](https://findai.net/)                                | GPT, Claude, Gemini            | MAX 渠道质量高但贵                                             |
| [NekoCode](https://nekocode.cn/)                           | Claude, GPT                    | 2026年新站                                                 |
| [DawCode](https://dawcode.com/)                            | Claude, GPT, Gemini            | 2026年新站                                                 |

### 综合类

| 站点 | 支持模型 | 特点 |
|---|---|---|
| [Poixe AI](https://poixe.com/i/sgurn9) | 全系列 | 2024年开始的老站，UI 风格好 |
| [柏拉图AI](https://bltai.com/) | Claude, GPT, Gemini, DeepSeek, MJ, Suno, 可灵等 | 模型最全，几乎能找到所有接口 |
| [云雾AI (YUNWU)](https://yunwu.ai/register?aff=h4RW) | Claude, GPT, Gemini, DeepSeek, Qwen, MJ 等 | 老牌站，ys模型全 |
| [Aiberm](https://aiberm.com/register?aff=mZPL) | Claude (官网2折) | 稳定，站长有多个项目 |
| [DoroAI](https://doro.lol/register?aff=sAVO) | Claude, Gemini, GPT, Grok | 有美港双接入 |
| [Chintao AI](https://chintao.cn/register?aff=RF8V) | Claude | 接口质量好，新用户送10元 |
| [LingxiCode](https://new.050602.xyz/register) | Claude, Gemini, GPT, DeepSeek, Kimi | 价格便宜但质量一般 |
| [FoxCode](https://code.newcli.com/auth/register?aff=5O8P) | Claude (AWS/Kiro逆向) | Opus4.6 ¥0.5/进 ¥2.5/出（最低价） |
| [哈基米](https://api.gemai.cc/register?aff=tzn3) | Claude, DeepSeek, Gemini, GPT | 支持按量/按次 |
| [Ekan8](https://api.ekan8.com/register?aff=fLYm) | Gemini, Claude | "酒馆"站，Opus4.6 ¥3.5/进 ¥17.5/出 |
| [接口AI](https://jiekou.ai/) | 全系列 | 价格与官方接近，支持企业发票 |

### 检测工具

| 工具 | 用途 |
|---|---|
| [Veridrop](https://veridrop.org) | API 中转站真伪检测（Claude thinking 签名验证、长上下文探针等） |
| [禾维AI 排行榜](https://hvoy.ai/#sonnet-4-6-ranking) | 实时检测端口，更新价格排行 |

## 不推荐的

| 站点/渠道 | 原因 |
|---|---|
| 闲鱼/小红书上的不知名中转站 | 掺水严重，速度不达标，容易跑路 |
| AI派 | 缓存价格贵(0.52倍)，接口慢，扣费不透明 |
| 大肘子 | RP 友好站，接口质量差，按次收费非按量 |
| 注意: 价格异常便宜的模型可能拿国产模型（如 GLM）冒充高价国外模型 |

## 价格参考 (人民币/百万Token)

| 模型 | 低价渠道 | 正常渠道 |
|---|---|---|
| Claude Sonnet 4.6 | ¥0.9~3.6/进 | ¥4.5~12/进 |
| Claude Opus 4.6 | ¥0.5~5/进 | ¥7.5~20/进 |
| GPT 5.5 | ¥1/进 ¥6/出 | ¥2.5/进 ¥15/出 |
| GPT 5.4 | ¥0.5/进 ¥3/出 | ¥1.5/进 ¥9/出 |
| Gemini 3.1 Pro | ¥6/进 ¥36/出 | - |

## 配置 Claude Code CLI 使用中转站

`claude` CLI 支持通过 `ANTHROPIC_BASE_URL` 环境变量指向中转站地址：

```bash
export ANTHROPIC_BASE_URL=https://your-relay.com/v1
export ANTHROPIC_API_KEY=your-relay-api-key
claude
```

> 注意: 中转站必须完整兼容 Anthropic Messages API 协议才能用于 Claude Code

## 安全建议

1. 优先选择公司运营、有社群、运行时间长的站点
2. 优先香港/新加坡节点的中转站（延迟低）
3. 用 [Veridrop](https://veridrop.org) 检测中转站是否掺水
4. 不要大额充值
5. 关注价格异常低的接口（可能是掺水或国产冒充）
6. 注意缓存价格比例（正常约0.1倍，有些站收到0.52倍）

---

## 2026-05-15 补充：网上资源与后续跟踪清单

> 这一节偏“资源索引 + 判断框架”。中转站价格和质量变化非常快，具体站点仍以实时榜单、社群反馈、自己小额实测为准。

### 值得持续关注的资源

| 资源 | 链接 | 价值 | 备注 |
|---|---|---|---|
| relayAPI / zzsting88 | https://github.com/zzsting88/relayAPI | 中文中转站推荐、价格、主观体验更新 | 当前笔记主要来源之一；适合看“人肉试用反馈”，但仍要自己验证 |
| 禾维 AI 排行榜 | https://hvoy.ai/#sonnet-4-6-ranking | 中转站价格、端口可用性、模型排行 | 适合快速横向比价，重点看更新时间和检测口径 |
| Veridrop | https://veridrop.org / https://github.com/canarybyte/veridrop | 中转站真伪与协议能力检测 | Claude 的 thinking signature 是强验证点；测长上下文会烧 token |
| Awesome Free ChatGPT | https://github.com/LiLittleCat/awesome-free-chatgpt | 免费 ChatGPT 镜像/替代方案列表 | 更偏网页镜像，不等同于 API 中转；不要输入隐私或主力 key |
| OpenRouter | https://openrouter.ai | 正规多模型聚合 API | 质量和透明度相对好，但国内支付/网络可能麻烦，价格通常不便宜 |
| LiteLLM Providers | https://docs.litellm.ai/docs/providers | 官方/聚合商/自建网关支持列表 | 适合梳理“有哪些正规 API 源”和自建代理方案 |
| LiteLLM Proxy | https://docs.litellm.ai/docs/simple_proxy | 自建 OpenAI-compatible 网关 | 适合把多个官方 key、Azure、Vertex、OpenRouter 等统一成一个入口 |
| New API | https://github.com/Calcium-Ion/new-api | One API 分支，自建中转/分发面板 | 很多中转站用类似面板；自建时要注意安全和账单隔离 |
| One API | https://github.com/songquanpeng/one-api | 老牌开源 API 管理/分发项目 | 项目生态老，适合了解中转站面板形态 |
| Cloudflare AI Gateway | https://developers.cloudflare.com/ai-gateway/ | 官方网关、缓存、日志、限流 | 不是“便宜中转站”，更像可靠性/观测层 |
| Portkey AI Gateway | https://portkey.ai | 商业 AI Gateway | 适合企业路由、fallback、日志、guardrails；不是低价倒卖路线 |

### 分类看待：不要把所有“代理”混成一类

1. **正规聚合商 / Marketplace**
   - 例：OpenRouter。
   - 优点：模型来源、计费、协议通常更透明。
   - 缺点：可能贵；国内支付、账号风控、网络连通性未必省心。

2. **自建网关 / AI Gateway**
   - 例：LiteLLM Proxy、New API、One API、Cloudflare AI Gateway、Portkey。
   - 用途：统一多个官方/云厂商/聚合商 key，做限流、日志、fallback、预算控制。
   - 适合：团队或个人有多个正规 key，希望自己掌控路由。
   - 注意：这类工具本身不解决“便宜模型来源”，只是管理入口。

3. **国内商业中转站**
   - 例：本笔记上方列出的 PackyCode、RightCode、Poixe 等。
   - 优点：注册/充值方便，面向 Claude Code、Codex 等场景做了适配。
   - 风险：跑路、掺水、协议不完整、账单不透明、缓存费率坑、模型名和真实上游不一致。

4. **免费镜像 / 公益站**
   - 例：Awesome Free ChatGPT 里的网页镜像。
   - 用途：临时聊天、轻量尝试。
   - 不建议：输入隐私、长期保存重要上下文、填自己的主力 API key。

### 选站优先级（实用版）

1. **先定用途**
   - 写代码：优先 Claude Code / Codex / Gemini CLI 兼容性，重点看 streaming、tool use、长上下文、缓存计费。
   - 普通聊天：稳定性和价格更重要，不必追极限上下文。
   - 企业/长期项目：发票、SLA、客服、账单明细、可导出记录比低价重要。

2. **先试后充**
   - 优先选择最低充值 1–10 元、有试用额度、账单清晰的站。
   - 新站、异常低价站，不要一次充超过“亏了也不心疼”的额度。

3. **看缓存价格**
   - 写代码经常大量命中 prompt cache。
   - 正常缓存费率通常显著低于输入价；如果缓存按 0.5x 甚至更高收，实际成本会被放大。

4. **看协议完整度**
   - Claude：thinking、tool_use、PDF、streaming、message id、usage 字段。
   - OpenAI：function calling、structured output、stream usage、model 字段、tool_calls 结构。
   - Gemini OpenAI-compatible：function calling、thinking 相关字段、usage 合理性。

5. **看异常信号**
   - 价格低到离谱但没有解释。
   - 官网没有状态页/社群/客服渠道。
   - 账单只有总扣费，没有请求级明细。
   - 模型表现像低价国产模型，拒答/格式/知识风格明显不对。
   - 长上下文宣传 1M，但 100k/200k needle 测试就失败。

### 小额实测流程

1. 注册后只充最低额度。
2. 先跑最便宜的连通性测试：

```bash
curl "$BASE_URL/v1/models" \
  -H "Authorization: Bearer $API_KEY"
```

3. 用真实工作流小跑一轮：
   - Claude Code / Codex 跑一个小 repo 修改；
   - 或者让模型读长文件、调用工具、输出结构化 JSON。
4. 看后台账单是否能对应到请求。
5. 再用 Veridrop 做 quick / standard 检测；只有要认真长期使用时再跑 full + long-context。
6. 观察 1–3 天稳定性，再决定是否加钱。

### Claude Code / Codex 场景额外注意

- Claude Code 不只是“能聊天”就行，必须完整兼容 Anthropic Messages API。
- 重点测试：长输出、工具调用、多轮上下文、streaming 中断恢复、缓存计费。
- 如果中转站提供多个分组（如 max / cc / kiro / aws / 官方 key / 反代），要分别测试；同一站不同分组质量可能完全不同。
- Codex / OpenAI-compatible 场景要重点看 function calling、structured output 和流式返回是否标准。

### 推荐组合策略

| 预算/需求   | 推荐做法                                    |
| ------- | --------------------------------------- |
| 个人轻量使用  | 官方 ChatGPT/Claude 订阅 + 少量中转 API 备用      |
| 高频写代码   | 主力选 1 家质量稳定的编程向中转；再留 1 家备用；都只小额充值       |
| 企业/项目交付 | 优先正规聚合商或自建 LiteLLM/New API 网关；中转站只做备用通道 |
| 只想临时白嫖  | 用免费网页镜像，但不要填隐私、账号、key、代码仓库机密            |

### 待继续补充 / 后续可查

- 各站是否有状态页、QQ群/TG/Discord、客服响应时间。
- 各站 Claude cache 费率、最低充值、发票能力。
- 用 Veridrop 对常用站点跑一轮 quick/standard，记录报告链接。
- 针对 Claude Code 建一个统一小测试仓库：tool use、长上下文、缓存、流式输出、修改文件。

---

## 2026-05-15 补充：Codex / GPT API 比价结论

> 来源：本地 relayAPI_reference.md + 现场抓取禾维 AI 首页 SSR 表格（`gpt-5-5-ranking` / `gpt-5-4-ranking`）。价格单位按该页口径，通常理解为人民币 / 百万输入 token；输出价需进站核对。中转站变化快，只适合作为小额试用前的初筛。

### 禾维 AI 实时榜单摘录

#### GPT 5.5 / Codex

| 站点 | 分组 | 价格 | 在线率 | 掺水率 | 延迟 | 初步判断 |
|---|---:|---:|---:|---|---:|---|
| RightCode | codex | 1 | 98% | 几乎不 | 10.3s | 最均衡：便宜 + 资料里也长期推荐 |
| IKunCode | Codex | 1 | 91% | 较少 | 14.9s | 同价但在线率、掺水指标弱于 RightCode |
| UU API | Codex/GPT5.5 | 1.5 | 98% | 几乎不 | 9.5s | 价格略高，可做备选 |
| AOK | Codex-专用 | 2 | 98% | 几乎不 | 10.7s | 价格较高，资料里积累少 |
| DuckCoding | CodeX专用 | 4 | 100% | 几乎不 | 12.4s | 稳但贵 |
| RunAPI | default | 14 | 98% | 几乎不 | 10.4s | 太贵，不适合作为低价 Codex 主力 |

#### GPT 5.4 / Codex

| 站点 | 分组 | 价格 | 在线率 | 掺水率 | 延迟 | 初步判断 |
|---|---:|---:|---:|---|---:|---|
| RightCode | codex | 0.5 | 96% | 几乎不 | 3.3s | 最便宜梯队，且本地资料明确推荐 |
| UU API | Codex/GPT5.5 | 0.8 | 98% | 几乎不 | 2.7s | 略贵但指标好，可做备选 |
| AOK | Codex-专用 | 1 | 98% | 几乎不 | 3.4s | 可备选，但资料沉淀少 |
| ClaudeCN | CodeX | 1.3 | 100% | 较少 | 4.6s | 在线率好，但掺水指标弱一点 |
| DuckCoding | CodeX专用 | 2 | 100% | 几乎不 | 5s | 更贵但在线率好 |
| RunAPI | default | 7 | 98% | 几乎不 | 2.6s | 太贵 |

### 结合本地资料后的排序

1. **首选：RightCode codex**
   - GPT5.5：约 ¥1 / 百万输入 token；GPT5.4：约 ¥0.5 / 百万输入 token。
   - 本地资料也写了“GPT5.5 ¥1/进 ¥6/出（非常推荐/主力）”。
   - 禾维榜单显示 GPT5.5 在线率 98%、掺水率“几乎不”；GPT5.4 在线率 96%、掺水率“几乎不”。
   - 缺点：GPT5.5 延迟约 10s，不算快；仍要小额实测账单、输出价、缓存费率。

2. **备选：UU API Codex/GPT5.5**
   - GPT5.5 约 ¥1.5；GPT5.4 约 ¥0.8。
   - 在线率 98%，延迟比 RightCode 略低。
   - 本地资料沉淀较少，建议只做备用通道，小额试。

3. **备选：AOK Codex-专用**
   - GPT5.5 约 ¥2；GPT5.4 约 ¥1。
   - 指标不错，但资料沉淀较少，先小额测。

4. **不作为低价主力：DuckCoding / RunAPI**
   - DuckCoding 指标好，但 GPT5.5 约 ¥4，明显贵。
   - RunAPI GPT5.5 约 ¥14、GPT5.4 约 ¥7，性价比不适合作为 Codex API 主力。

### 当前结论

如果目标是“最便宜且相对可靠的 Codex API”，**优先试 RightCode 的 codex 分组**。  
更谨慎的做法：RightCode 充最低额度作为主力测试；同时给 UU API 或 AOK 小额备用，连续跑 1–3 天真实 Codex 任务后再决定是否加钱。

### 实测清单

- 最低额度充值，不要大额预存。
- 跑一个真实 Codex 小任务，确认：streaming、工具调用、结构化输出、长输出是否稳定。
- 对照后台账单：输入/输出 token、缓存费率、失败请求是否扣费。
- 高峰期再测一次延迟和失败率。
