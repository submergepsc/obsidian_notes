# AI Agent(智能体) 教程

- Source: https://www.runoob.com/ai-agent/ai-agent-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2025/12/1745211719204.jpeg)


AI Agent 称为智能体，本质是自动执行任务的程序，核心在于让模型不只回答问题，而是按步骤完成动作。


**AI Agent（人工智能代理）** 是一个能够感知环境、进行决策并执行行动，以达成特定目标的智能软件实体，它不仅仅是回答问题的聊天机器人，更是能够动手做事的智能执行者。


Agent = LLM (大脑) + Planning (规划) + Tool use (执行) + Memory (记忆)。


快速体验 0 代码，一句话生成应用：[**https://www.miaoda.cn/**](https://www.miaoda.cn/?invitecode=user-93thly701s00)。桌面级 AI Agent：[**QoderWork**](https://www.runoob.com/qoderwork.html)


---


## 谁适合阅读本教程？


- 想使用 AI 自动化日常任务的人
- 对编程不熟但想用 AI 做实际工作的新人
- 已会基本电脑操作、但对 Agent/工作流 等概念零基础的人
- 想把 AI 从聊天提升到真正干活的人


---


## 课程内容


---


## 什么是 Agent？


Agent 就是一个能干活的智能助手。


Agent = LLM (大脑) + Planning (规划) + Tool use (执行) + Memory (记忆)。

学习 Agent 需要思维转变： 从**对话框问答**进化为**目标驱动的任务执行**。


![](https://www.runoob.com/wp-content/uploads/2025/12/0_0_ezapX2F_7BOysP.png)


传统的软件程序遵循固定的指令流程：**输入 → 处理 → 输出**，而 AI Agent 则更像一个有自主性的**员工**，它能够：


- **理解任务目标**：明白你想要什么结果
- **制定计划**：思考如何达成目标
- **使用工具**：调用各种资源和 API
- **自我调整**：根据反馈优化策略
- **持续执行**：直到完成任务或遇到无法解决的问题


**类比理解：**


- 传统程序 = 自动售货机：投币 → 按按钮→ 出商品
- AI Agent = 私人助理：告诉需求 → 助理规划 → 完成任务并汇报


---


## AI Agent 结构组成


**结构由三块组成:**


- **目标：**明确任务意图
- **逻辑：**按规则拆成可执行步骤
- **工具：**通过代码或 API 让步骤落地


**运行方式:**


- 接收输入
- 判断当前任务
- 调用对应工具执行
- 返回结果
- 保留必要上下文
- 支持多轮连续操作
- 遇阻时调整执行步骤


![](https://www.runoob.com/wp-content/uploads/2025/12/ai-agent-1-runoob-scaled.png)


**与普通大模型的差异点:**


- 普通大模型：生成文本
- Agent：生成行动并执行行动，能完成实际工作


**举例：**


- 给出目标：如 "规划三天北京行程，预算 5000"。
- 自动检索机票、酒店与价格。
- 自动收集景点信息并做对比。
- 自动生成可执行行程表。
- 具备条件时可继续执行预订操作。


---


## AI Agent 的工作原理：一个简单的代码示例


让我们通过一个 Python 伪代码示例，直观感受一下 AI Agent 的工作流程。假设我们要创建一个能自动查询天气并给出穿衣建议的简单 Agent。


## 实例


```
# 伪代码示例：简易天气穿衣助手Agent
import requests

class WeatherAgent:
    def __init__(self):
        self.memory = []  # 简单的记忆存储
        self.tools = {
            'get_weather': self.get_weather_api,
            'give_advice': self.generate_advice
        }

    # 工具1: 调用天气API
    def get_weather_api(self, city):
        """调用外部天气API获取数据"""
        # 这里模拟一个API调用
        print(f"[Agent 行动] 正在查询{city}的天气...")
        # 假设返回的数据
        mock_data = {'city': city, 'temp': 22, 'condition': '晴朗', 'wind': '3级'}
        return mock_data

    # 工具2: 根据天气生成建议
    def generate_advice(self, weather_data):
        """根据天气数据生成穿衣建议"""
        temp = weather_data['temp']
        condition = weather_data['condition']
        advice = f"当前{weather_data['city']}气温{temp}℃，天气{condition}。"
        if temp > 25:
            advice += "建议穿短袖、短裤。"
        elif temp > 15:
            advice += "建议穿长袖T恤、薄外套。"
        else:
            advice += "建议穿毛衣、厚外套。"
        return advice

    # 规划与执行核心
    def run(self, user_input):
        """解析用户目标并执行任务"""
        print(f"[用户指令] {user_input}")

        # 步骤1: 规划 - 从指令中提取关键信息（城市）
        # 这里简化处理，实际会用更复杂的NLP模型
        if "天气" in user_input and "北京" in user_input:
            city = "北京"
        else:
            return "请告诉我您想查询哪个城市的天气？"

        # 步骤2: 行动 - 调用工具获取天气
        weather_info = self.tools['get_weather'](city)
        self.memory.append({'step': 'fetched_weather', 'data': weather_info})  # 存入记忆

        # 步骤3: 行动 - 调用工具生成建议
        final_advice = self.tools['give_advice'](weather_info)
        self.memory.append({'step': 'generated_advice', 'data': final_advice})  # 存入记忆

        # 步骤4: 输出结果
        return final_advice

# 使用Agent
agent = WeatherAgent()
result = agent.run("我想知道北京的天气，该怎么穿衣服？")
print(f"[Agent 回复] {result}")

# 输出示例：
# [用户指令] 我想知道北京的天气，该怎么穿衣服？
# [Agent 行动] 正在查询北京的天气...
# [Agent 回复] 当前北京气温22℃，天气晴朗。建议穿长袖T恤、薄外套。
```


**代码解读**：


- `WeatherAgent` 类定义了一个简单的 Agent 框架。
- `tools` 字典定义了 Agent 可以使用的两种"工具"（函数）。
- `run` 方法是核心流程：它**解析**用户指令，**规划**出需要调用 `get_weather_api` 和 `generate_advice` 两个工具，然后**按顺序执行**，并将中间结果存入 `memory`，最后**输出**整合后的答案。


---


## 学习资源

Google 5 天智能体课程：[https://www.kaggle.com/learn-guide/5-day-agents](https://www.kaggle.com/learn-guide/5-day-agents)


微软的课程：[https://github.com/microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)

Hello-Agents：[https://github.com/datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents)

500 个智能体案例：[https://github.com/ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects)

智能体资源库：[https://github.com/NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents)

HF 智能体课程：[https://github.com/huggingface/agents-course](https://github.com/huggingface/agents-course)








	  AI 思考中...






			[AI Agent 简介](https://www.runoob.com/ai-agent-intro.html) **













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