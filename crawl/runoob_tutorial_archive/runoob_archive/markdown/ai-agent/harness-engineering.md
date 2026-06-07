# Harness Engineering（驾驭工程）

- Source: https://www.runoob.com/ai-agent/harness-engineering.html

---


## 一、什么是 Harness Engineering？



**Harness Engineering（驾驭工程）**是围绕 AI 智能体设计和构建**约束机制、反馈回路、工作流控制和持续改进循环**的系统工程实践。


它不优化模型本身，而是优化模型运行的环境。核心哲学八个字：**人类掌舵，智能体执行（Human Steer, Agent Execute）**。


Harness一词来自马具——缰绳、马鞍、嚼子——这是一套引导强大但不可预测的动物的完整装备。**驾驭工程不是去削弱 AI 的能力，而是为它打造一套黄金缰绳，让它跑得又快又稳。**


这个概念由 HashiCorp 联合创始人 Mitchell Hashimoto 在 2026 年 2 月 5 日首次提出，六天后 OpenAI 在百万行代码实验报告中正式采用这一术语，随后 Martin Fowler 撰文深度分析，一个月内成为开发者社区的高频词。



harness engineering is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent will not make that mistake again in the future.

—— Mitchell Hashimoto


这句话的潜台词是：**Agent 的每一次失败，都是环境设计不完善的信号。**正确的回应不是换一个更强的模型，而是重新设计它运行的环境。


---


## 二、为什么需要驾驭工程？真实数据说话



    100万
    OpenAI 团队 5 个月产出代码行数


    0行
    工程师手动编写的代码


    3~7人
    团队规模，人均每日 3.5 个 PR


    30 → 5
    LangChain 仅改 Harness，Terminal Bench 排名跃升



LangChain 的案例尤其有说服力：底层模型一个参数都没动，**仅仅通过优化外部驾驭环境**（文档结构、验证回路、追踪系统），编码 Agent 在 Terminal Bench 2.0 的得分从 52.8% 飙升至 66.5%，全球排名从第 30 位跃升至第 5 位。


五个独立团队也得出了相同结论：**瓶颈不在模型智能，而在基础设施。**


---


## 三、AI 工程范式的三次跃迁


要理解驾驭工程为何重要，需要先看清楚我们是怎么一步步走到这里的。





Prompt Engineering 提示词工程 优化对象：输入措辞 解决：单次对话质量 2023 ~ 2024 Context Engineering 上下文工程 优化对象：信息输入 解决：知识边界与幻觉 2025 Harness Engineering 驾驭工程 优化对象：运行环境 解决：Agent 可靠性与可持续性 2026 ~ 不够用了 还不够 | 范式 | 核心问题 | 优化对象 | 交互模式 | | --- | --- | --- | --- | | 提示词工程 | 怎么把话说清楚 | Prompt 的措辞、格式、示例 | 一问一答 | | 上下文工程 | 怎么给 AI 喂信息 | 文档、代码片段、历史对话 | 信息注入 → 生成 | | 驾驭工程 | 怎么让 Agent 可靠工作 | 约束、反馈回路、控制系统 | 人类掌舵，Agent 执行 | 一个好记的类比：


- Prompt Engineering —— **对马喊话的技巧**
- Context Engineering —— **给马看的地图**
- Harness Engineering —— **给马造一条高速公路，配上护栏、限速牌和加油站**


---


## 四、Agent 常见失败模式


Anthropic 工程师在长时间运行 Agent 的过程中，总结了三种典型的翻车姿势，正是驾驭工程要解决的核心痛点：



**失败模式 1：试图一步到位（One-shotting）**


Agent 倾向于在一个会话里把所有功能都做完。结果是上下文窗口耗尽，留下一堆没有文档的半成品代码，下一个会话启动时只能花大量时间猜测之前发生了什么。



**失败模式 2：过早宣布胜利**


在项目后期，当部分功能已经完成后，Agent 会环顾四周，看到已有进展就直接宣布任务完成——即使还有大量功能未实现。



**失败模式 3：过早标记功能完成**


在没有明确提示的情况下，Agent 写完代码就标记为完成，却没有做端到端测试。单元测试或 curl 命令通过了不代表功能真正可用。


此外，智能体还有一个危险特性：**它非常擅长模式复制**。代码库里有什么模式，它就忠实地复制并放大——包括坏模式和架构漂移。这意味着不加约束的 Agent 会以惊人的速度积累技术债务。


---


## 五、驾驭工程的四大护栏


综合 OpenAI、Anthropic、LangChain 和 Martin Fowler 的实践，Harness 可以归纳为四个核心组件，即四根"护栏"：











  AI Agent
  智能体



  上下文工程
  Context Engineering
  动态知识注入 · AGENTS.md
  按需检索 · 活文档机制




  架构约束
  Architecture Constraints
  分层依赖模型 · 自动 Linter
  CI 强制阻断 · 类型系统




  反馈循环
  Feedback Loop
  智能体审智能体 · 自动测试
  CI 验证 · 错误信号回传




  熵管理
  Entropy Management
  定期垃圾回收 · 文档园丁
  持续小额偿还技术债



### 护栏一：上下文工程（Context Engineering）——新员工手册




就像给新员工一本详细的工作手册，**AGENTS.md** 是 AI 智能体进入代码仓库时看到的第一份指南。但这不是一本静态的 1000 页说明书——上下文是稀缺资源，过多的指导反而会挤掉任务、代码和相关文档的空间，变成陈旧规则的坟场。


更好的做法是：提供一个稳定、小巧的入口点，然后教 Agent 根据当前任务按需检索和拉取更多的上下文。Mitchell Hashimoto 的 Ghostty 项目 AGENTS.md 里每一行都对应一个历史 Agent 失败案例——文档是活的反馈循环，不是静态制品。




### 护栏二：架构约束（Architecture Constraints）——缰绳




OpenAI 团队建立了严格的层级依赖模型：


**Types → Config → Repo → Service → Runtime → UI**


下层不能反向依赖上层。所有架构规则被编码为**自定义 Linter 规则**，违反即 CI 阻止合并——无论代码是人写的还是 AI 写的。


有个关键细节：Linter 的错误信息本身也是上下文工程。它不只说你违反了规则 X，而是解释为什么这个规则存在、正确做法是什么，这样 Agent 读到错误后就能自我理解并修正，不需要人类介入。




### 护栏三：反馈循环（Feedback Loop）——智能体审智能体




传统开发中，人类工程师负责代码审查（Code Review）。在驾驭工程中，这个工作变成了智能体对智能体的方式：Codex 在本地审核自身更改，请求额外审查，循环往复直到通过。


反馈循环中的钩子可以运行预定义的测试套件，并在失败时带着错误信息循环回到模型，或者提示模型独立评估其代码。如果 AI 写的测试用例通过了带有 Bug 的代码，Harness 就会判定测试无效，强迫它重新思考测试边界。




### 护栏四：熵管理（Entropy Management）——垃圾回收




随着时间推移，软件系统会逐渐混乱（熵增），技术债务会积累。OpenAI 采用持续小额偿还的策略，而不是等问题严重时集中处理——他们把这个方法形象地称为**垃圾回收**，并认为技术债务就像高息贷款。


具体措施：定期运行后台 Codex 任务扫描偏差、更新质量等级、发起针对性重构 PR。此外还有一个专门的 **Doc-gardening Agent**（文档园丁代理），在后台自动扫描文档与代码之间的不一致，发现过时内容就自动提交 PR 修复——Agent 为 Agent 维护文档。




---



## 六、六大行业共识



综合 OpenAI、Anthropic、LangChain、Stripe、HashiCorp 等多个独立信息源，业界在以下六个方面已形成明确共识：



| # | 共识 | 核心观点 |
| --- | --- | --- |
| 1 | 瓶颈在基础设施，不在模型智能 | 五个独立团队得出相同结论。仅改变 Harness 工具格式，就能让模型得分从 6.7% 跳到 68.3% |
| 2 | 文档必须是活的反馈循环 | 静态文档是坟场，动态文档才有价值。让后台 Agent 定期清理过时文档并提交 PR |
| 3 | 思考与执行分离 | 复杂任务不可能在单个上下文窗口内完成，需要 Orchestrator + Worker 分层架构，状态持久化到外部存储 |
| 4 | 上下文不是越多越好 | 上下文是稀缺资源。巨大的指令文件会挤掉任务空间，应按需检索、动态注入 |
| 5 | 约束必须自动化 | 人工 Review 是瓶颈。护栏要编码为 Linter、CI、类型系统，让机器来执行而非人 |
| 6 | 工程师角色在转变 | 从代码的编写者变成环境的建筑师。最大的工程挑战是设计让 Agent 可靠工作的控制系统 |



---



## 七、Harness 与传统框架的关系



Harness 不是 SDK、脚手架或 Agent 框架的替代品，而是**位于它们之上的一层**：






  Harness Layer（驾驭层）
  约束 · 反馈循环 · 上下文工程 · 熵管理 · 生命周期管理


  Agent Frameworks（LangGraph / AutoGen / CrewAI）
  智能体定义 · 消息路由 · 任务生命周期 · 依赖管理


  SDK / API（OpenAI / Anthropic / Gemini）
  模型调用 · 工具注册 · 流式输出


  Foundation Model（GPT / Claude / Gemini / DeepSeek）


  Harness
  框架层
  SDK 层
  模型层



传统框架解决的是**如何构建 AI 智能体**，而驾驭层解决的是完全不同的问题：**智能体如何可靠地运行**。



模型正在逐渐吸收框架约 80% 的功能（智能体定义、消息路由、任务生命周期……），但剩余 20%——**持久化、确定性重放、成本控制、可观测性、错误恢复**——正是驾驭层存在的价值。



---



## 总结



Harness Engineering 不是某一家公司的实验，而是整个行业正在经历的范式转移。




**Birgitta Böckeler 的总结最为精辟：**

为了获得更高的 AI 自主性，运行时必须受到更严格的约束。增加信任需要的不是更多自由，而是更多限制。

就像高速公路上的护栏——正是因为有护栏，你才敢踩到 120 码。




| 核心组件 | 解决的问题 | 代表实践 |
| --- | --- | --- |
| 上下文工程 Context | Agent 不知道该看什么、怎么找 | AGENTS.md 活文档、按需检索 |
| 架构约束 Constraints | Agent 复制并放大坏模式 | 分层依赖、自定义 Linter、CI 强制阻断 |
| 反馈循环 Feedback | Agent 不知道自己做错了 | Agent-to-Agent Review、自动测试套件 |
| 熵管理 Entropy | 技术债务和文档腐烂 | Doc-gardening Agent、持续垃圾回收 |



软件开发的未来，可能不再是关于我们能写多快多好的代码，而是关于**我们能设计多聪明、多鲁棒的系统来驾驭 AI 代理的巨大能量**。


工程师的价值正在从执行者转变为赋能者和系统思考者 —— 从构建产品转向构建能够构建产品的工厂。











	  AI 思考中...





			** [LangGraph 入门教程](https://www.runoob.com/langgraph-quick-start.html)
			[Hermes Agent](https://www.runoob.com/hermes-agent.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/../html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/../css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/../js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/../ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/../jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/../xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/../java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/../charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/../tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/../tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/../skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/../skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/../skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/../skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/../skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/../skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/../skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)

      : · [免责声明](https://www.runoob.com/../disclaimer/index.html)

      : · [关于我们](https://www.runoob.com/../aboutus/index.html)

      : · [文章归档](https://www.runoob.com/../archives/index.html)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/../index/index.html)**
    **[runoob.com](https://www.runoob.com/../index/index.html)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **