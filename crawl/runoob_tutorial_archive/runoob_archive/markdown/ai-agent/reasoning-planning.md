# 推理与规划（Reasoning & Planning）

- Source: https://www.runoob.com/ai-agent/reasoning-planning.html

在构建自主 AI Agent 的过程中，如果说大语言模型（LLM）是 Agent 的大脑，工具调用（Tool Use）是手脚，那么**推理与规划（Reasoning & Planning）**就是将其从简单的问答机升级为自主问题解决者的核心引擎。


复杂的现实任务往往无法通过一次生成（One-pass generation）完成。AI 需要具备拆解目标、逻辑推演、探索路径、自我修正以及调度工具的能力。


以下是目前业界最主流的推理与规划框架。


---


## 思维链（Chain of Thought, CoT）


### 逐步推理能力


传统 LLM 生成答案时往往是直觉式的一步到位。

思维链（CoT）的核心思想是：**强制要求模型在输出最终答案前，先显式地输出中间的推理步骤（Let's think step by step）**。这种做法能显著激活模型在复杂数学、逻辑推理和常识问答中的潜力。


CoT 不仅让模型有了更多的计算时间（token 数量代表计算量），还让后续的生成能建立在前面正确的逻辑基础上。


## 实例：Few-shot CoT 提示词设计


```
# 通过提供包含推理过程的示例，引导模型进行 CoT 推理
prompt = """
问题：罗杰有5个网球。他又买了2罐网球。每罐有3个网球。他现在共有多少个网球？
解答：罗杰一开始有5个网球。2罐网球，每罐3个，共计 2 * 3 = 6 个网球。5 + 6 = 11。答案是11。

问题：食堂有23个苹果。如果他们用掉20个做午餐，又买了6个，现在有多少个苹果？
解答：食堂本来有23个苹果。用掉20个后剩下 23 - 20 = 3 个。又买了6个，现在有 3 + 6 = 9 个。答案是9。

问题：{user_question}
解答："""
```


---


## ReAct 框架（Reasoning + Acting）


### 推理 + 行动循环


如果说 CoT 只是在模型内部闭门造车，那么 **ReAct（Reason + Act）** 则是让模型睁开眼睛看世界。它将内部逻辑推理（Thought）与外部工具交互（Action）交织在一起，形成一个动态的闭环反馈系统。


在 ReAct 范式下，Agent 遵循 **Thought（思考） -> Action（行动） -> Observation（观察）** 的循环，直到得出最终结论。


ReAct 循环架构图
展示了 Thought, Action, Observation 之间的循环关系。


Thought 分析现状与目标 Action 调用外部工具/API Observation (观察) User Query **局限性：** ReAct 在短期的、步骤清晰的任务中表现优异。但由于整个思维和动作历史都积压在同一个上下文窗口中，当任务链条过长时，极易陷入死循环或因为上下文超载而遗忘初始目标。


---


## Plan-and-Execute（规划先行执行模式）


为了解决 ReAct 在长线任务中的疲软，Plan-and-Execute 将思考和行动进行了解耦，采用了类似人类做大型项目的策略：**先出排期表，再挨个干活**。


系统通常分为两个独立的角色：


- **Planner（规划者）**：负责接收大目标，生成详细的 Step-by-Step 子任务列表。
- **Executor（执行者）**：负责按顺序执行这些子任务。执行器通常就是一个小型的 ReAct Agent，每次只专注完成当前的一个小目标。


Plan-and-Execute 架构图


复杂目标 Planner (规划者) 1. 抓取网页 2. 提取数据 3. 生成报告 Executor (执行者) 逐个处理子任务 (每次独立上下文) 最终交付 --- ## Tree of Thoughts (ToT) 与树状多路径探索 ### 树状多路径探索 无论是 CoT 还是 Plan-and-Execute，本质上都是**线性**的路径探索。但在写代码、解数学题或创意写作时，人类往往会设想多种方案，评估后选择最佳的，甚至在发现错误时回溯。


**ToT（思维树）** 将推理过程建模为一棵树：节点是当前的思维状态。模型会在每一个分支点生成多个候选 Thought，然后通过内部的 Evaluator（评估器）对这些节点进行打分（如：可行、可能有风险、不可行）。结合 **BFS（广度优先搜索）** 或 **DFS（深度优先搜索）** 算法，决定是继续深入还是回溯重试。


---


## 任务规划 & MCTS (蒙特卡洛树搜索)


### 复杂任务拆解与搜索


在涉及战略游戏或极高难度的推理任务（如前沿的数学验证、复杂的代码仓库重构）时，简单的 ToT 仍不够高效。业界开始将 LLM 与传统的强化学习搜索算法 **MCTS（Monte Carlo Tree Search）** 结合（类似 AlphaGo 的核心逻辑）。


- **LLM 作为策略网络（Policy Network）**：提供启发式的下一步行动建议，减少无意义的分支扩展。
- **LLM/代码环境作为价值网络（Value Network）**：通过仿真执行（Rollout）预判某个行动序列的最终胜率或成功率。
- **优势**：在庞大的解空间中，能够找到最具有全局最优潜力的规划路径。


---


## Reflexion：自我反思与纠错


人类在执行任务时，如果第一次失败了，会总结经验教训并在下一次尝试中规避错误。**Reflexion** 框架赋予了 Agent 类似的能力。


在 Reflexion 闭环中，当 Agent 的输出被判定为失败（例如：测试用例未通过、API 报错）时，会触发一个 **Reviewer 机制**。LLM 被要求根据"历史动作"和"失败的反馈"写一段口语化的反思（Reflection），例如：*"我刚才使用了错误的 API 参数格式，下一次我应该查阅文档后再传递 JSON"*。这段反思会被存入情景记忆（Episodic Memory）中，作为下一次尝试的上下文提示，从而大幅提升 Agent 的自愈合能力。


## 实例：Reflexion 的反思提示词设计


```
reflection_prompt = """
你是一个正在尝试编写 Python 爬虫的 AI 助手。
这是你刚才执行的代码：{previous_code}
这是运行环境返回的错误信息：{error_traceback}

请深刻反思：
1. 错误发生的根本原因是什么？
2. 在下一次尝试中，你具体的修改策略是什么？

请将反思记录下来，以指导后续的行动。
"""
```


---


## 任务分解策略与工程化实践


在实际生产级的 AI 智能体开发中，纯靠 LLM "零样本"进行复杂规划是不稳定的。常用的混合干预策略包括：


| 干预策略 | 核心做法 | 适用场景 |
| --- | --- | --- |
| 子任务模板化 (SOP) | 不让 LLM 自由规划，而是预先定义好标准操作程序（SOP），让 LLM 在固定的状态机（State Machine）中流转。 | 客服系统、标准化的数据清洗流水线。 |
| HITL (Human-in-the-Loop) | 在 Planner 生成任务列表后，中断执行，要求人类用户进行确认、修改或审批（Approve），然后再交由 Executor 执行。 | 高风险操作：如删除数据库记录、发送群发邮件、大额资金转账。 |
| RLHF 引导规划 | 利用强化学习和人类偏好反馈，专门微调大模型的规划能力，使其更倾向于生成安全、高效的步骤组合。 | 底层大语言模型基座的训练阶段（如 OpenAI 的 o1 模型训练）。 |


### 框架对比总结


| 模式 | 核心机制 | 优点 | 缺点 |
| --- | --- | --- | --- |
| CoT | Step-by-Step 线性推理 | 实现极简，显著提升基础推理准确度 | 无法调用外部工具，容易一条道走到黑 |
| ReAct | 交替思考与行动闭环 | 动态适应环境，能通过观测实时调整 | 上下文容易随步骤累积而爆炸，迷失初衷 |
| Plan-and-Execute | 先拆解为子任务，再隔离执行 | 极其适合长线复杂任务，上下文清晰 | 面对突发变化（规划本身出错时）不够灵活 |
| ToT / MCTS | 树状搜索，评估回溯 | 能解决最高难度的复杂逻辑问题 | 计算成本极其高昂，Token 消耗呈指数级 |
| Reflexion | 基于失败反馈生成反思记忆 | 具备自我纠错和持续进化的能力 | 依赖明确的反馈信号（如代码编译器报错） |








	  AI 思考中...





			** [AI 开发平台 MonkeyCode](https://www.runoob.com/ai-monkeycode.html)
			[RAG 与知识检索](https://www.runoob.com/retrieval-augmented-generation.html) **













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