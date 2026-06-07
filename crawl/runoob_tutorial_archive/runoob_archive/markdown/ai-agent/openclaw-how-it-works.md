# OpenClaw 工作原理

- Source: https://www.runoob.com/ai-agent/openclaw-how-it-works.html

OpenClaw 不是一个普通的聊天机器人，而是一个住在你电脑里的私人秘书，它能通过微信、WhatsApp、Telegram 等聊天软件接收指令，帮你发邮件、查日历、打开浏览器、运行命令，甚至 24 小时自动做事！


![](https://www.runoob.com/wp-content/uploads/2026/03/1_eZX31-3n0KTJ2MY1RB0JBg.png)


### 核心概念


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-2.png)


| 概念 | 类比 | 作用 |
| --- | --- | --- |
| Gateway（网关） | 大楼的前台接待 | 接收所有外部消息，分发到正确的工作空间 |
| Workspace（工作空间） | 你的私人办公室 | 处理具体任务，管理对话历史和技能 |
| LLM（大语言模型） | AI顾问大脑 | 理解你的意图，生成回复 |
| Skills（技能） | 工具箱里的工具 | 执行特定功能（查天气、写代码、管理日程等） |
| Channels（渠道） | 通信设备 | 连接不同的消息平台 |


### OpenClaw 到底是什么？


OpenClaw 是一个**完全开源、自己运行在你电脑上的 AI 助手**（以前叫 Clawdbot，后来改名）。**它不像 ChatGPT 那样只聊天，而是真正动手做事：


- 你在 WhatsApp 里说："帮我查一下明天航班"，它就能自动打开浏览器、登录航空公司网站、截图给你。
- 它支持几百个技能（Skills），社区还在不断增加。
- 它有长期记忆（记得你喜欢什么），还能自己生成新技能。
- 最重要的是：**数据全在你电脑里，不上传云端，隐私安全**。


核心思想：把 AI 大模型（大脑） + 本地工具（手脚） + 聊天软件（嘴巴耳朵）连接起来**，让 AI 真正成为你的电脑管家。


### 整体架构：Gateway 是大脑指挥中心


OpenClaw 最核心的部分叫 **Gateway（网关）**。它就像你家里的总控台，所有东西都围绕它转。


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-2.svg)


**各部分简单解释：**


- **Channel Bridge（通道桥接器）**：负责跟 WhatsApp、Telegram 等聊天软件"握手"。比如用 Baileys 库连接 WhatsApp。
- **Gateway**：唯一运行的进程（占用一个端口，默认 18789），像总机接线员，把消息转发给 AI。
- **AI 大脑**：真正思考的是外部大模型（你提供 API Key），Gateway 只负责"叫它来干活"。
- **工具 & 技能**：AI 的手脚，比如打开浏览器、读写文件、发邮件。
- **记忆系统**：像笔记本，AI 不会忘掉你上次说的话。


---


## 一条消息是怎么变成行动的？


我们用一个真实例子："在 WhatsApp 里说：帮我把今天的邮件整理成总结发给我"。


流程图如下：


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-3.svg)


**详细拆解：**


- **接收指令**：你发消息 → 聊天软件的 Bridge 把消息推给 Gateway。
- **查找记忆**：Gateway 打开你的"个人档案"（Session + Memory），知道你是老用户、上次喜欢什么语气。
- **AI 思考**：把消息 + 记忆打包发给 AI 大脑。AI 像聪明秘书："嗯，需要先读邮件，再总结。"
- **调用工具**：AI 说"我要用 Gmail 技能"。Gateway 在安全沙箱里执行（防止 AI 乱改文件）。
- **执行 + 反馈**：工具把结果给 AI，AI 写出总结。
- **回复用户**：Gateway 把总结发回 WhatsApp。你就收到了！


---


## 整体架构


### 三层架构设计


OpenClaw 采用经典的三层架构，让我们从外到内逐层理解：


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-4.svg)


### 为什么要这样设计？


**类比**：想象一个大型公司


- **外层（用户接口）** = 客户可以通过电话、邮件、微信等多种方式联系公司
- **中层（Gateway）** = 前台接待，统一接待所有客户，然后分配到合适的部门
- **内层（Workspace）** = 不同的业务部门，各自负责不同的事务
- **底层（能力层）** = 公司的资源（专家顾问、工具设备等）


---


## 核心组件详解


### Gateway：统一的门户


**Gateway 是什么？**


Gateway（网关）是 OpenClaw 的大门，所有外部消息都必须先经过这里。


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-5.svg)


**Gateway 的三大职责：**


#### 1. 认证（Authentication）


确保只有你授权的平台才能连接


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-6.svg)


#### 2. 路由（Routing）


把消息送到正确的工作空间


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-7.svg)


#### 3. 日志记录（Logging）


记录所有交互，方便调试和审计


**启动 Gateway 的命令：**


```
# 启动网关，监听 18789 端口
openclaw gateway --port 18789 --verbose
```


### Workspace：你的私人办公室


**Workspace 是什么？**


Workspace（工作空间）是实际处理任务的地方。你可以有多个工作空间，每个负责不同的事情。


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-8.svg)


**一个典型的 Workspace 配置示例：**


```
# workspace-personal.yaml
name: "个人助理"
llm:
  provider: "anthropic"  # 使用 Claude
  model: "claude-sonnet-4"
  apiKey: "sk-ant-xxx"

skills:
  - weather        # 查天气
  - calendar       # 管理日程
  - email          # 处理邮件
  - web-search     # 网页搜索

settings:
  language: "zh-CN"
  temperature: 0.7
  max_tokens: 4000
```


**多工作空间使用场景：**


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-9.svg)


### LLM：AI 的大脑


**LLM 是什么？**


LLM（Large Language Model，大语言模型）是 OpenClaw 的智能大脑，负责理解你的意图和生成回复。


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-10.svg)


**OpenClaw 支持的 LLM：**


| 提供商 | 模型示例 | 特点 | 适用场景 |
| --- | --- | --- | --- |
| Anthropic | Claude Sonnet 4 | 平衡、安全、多语言好 | 日常对话、写作 |
| OpenAI | GPT-4 | 专业、知识广 | 专业任务、分析 |
| DeepSeek | DeepSeek-V3 | 代码能力强、便宜 | 编程辅助 |
| 本地部署 | Ollama | 完全私有、免费 | 隐私敏感场景 |


### Channels：连接外部世界


**Channels 是什么？**


Channels（渠道）是连接各种消息平台的"适配器"。


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-11.svg)


**每个 Channel 的工作：**


- **接收消息**：从平台获取用户消息
- **格式转换**：统一转换为 OpenClaw 内部格式
- **发送回复**：把 OpenClaw 的回复发回平台


**示例：Telegram Channel 的工作流程**


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-12.svg)


---


## 消息流转过程


现在让我们看看一条完整的消息是如何在 OpenClaw 中流转的：


### 完整消息流程图


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-13.svg)


### 详细步骤解析


**步骤 1-3：消息接收与标准化**


用户在 Telegram 发送消息后，Telegram Channel 会将其转换为 OpenClaw 的标准格式：


```
{
  "platform": "telegram",
  "channel_id": "telegram_123",
  "user": {
    "id": "user_456",
    "name": "Alice"
  },
  "message": {
    "type": "text",
    "content": "上海明天天气?",
    "timestamp": "2024-03-09T10:30:00Z"
  }
}
```


**步骤 4-5：认证与路由**


Gateway 检查这个消息：


- 来源是否已授权？
- 应该路由到哪个 Workspace？
- 用户是否有权限？

**步骤 6-8：AI 理解与决策**


Workspace 准备完整的上下文发送给 LLM：


```
[系统提示]
你是一个个人助理，可以使用以下技能：
- weather: 查询天气
- calendar: 管理日程
- ...

[对话历史]
用户: 你好
助理: 你好！有什么可以帮你的？

[当前消息]
用户: 上海明天天气?
```


**步骤 9-12：技能执行**


LLM 决定调用 weather skill，Workspace 执行并获取结果：


```
{
  "location": "上海",
  "date": "2024-03-10",
  "weather": "晴转多云",
  "temperature": "18-26°C",
  "humidity": "60%",
  "wind": "东风 3-4级"
}
```


**步骤 13-17：生成回复并返回**


LLM 根据天气数据生成自然语言回复，通过原路返回给用户。


---


## 技能系统


### 什么是技能（Skills）？


技能是 OpenClaw 执行特定任务的"能力模块"。如果把 OpenClaw 比作一个人，技能就是这个人学会的各种本领。


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-14.svg)


### 技能的结构


每个技能包含：


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-15.svg)


**示例：天气技能的定义**


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-16.svg)


### 技能的调用流程


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-17.svg)


### 技能的安全机制


OpenClaw 对技能有严格的安全控制：


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-18.svg)


**权限类型：**


| 权限 | 说明 | 示例 |
| --- | --- | --- |
| network | 网络访问 | 查天气、搜索网页 |
| filesystem | 文件系统 | 读写文件 |
| email | 邮箱访问 | 发送/接收邮件 |
| calendar | 日历访问 | 管理日程 |
| system | 系统操作 | 执行命令 |


---


## 完整工作流程


让我们通过一个真实场景，串联所有概念：


### 场景：定时发送每日天气报告


**需求**：每天早上 8 点，通过 Telegram 收到今日天气 + 日程提醒


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-19.svg)


### 配置代码


```
# workspace-daily-report.yaml
name: "每日报告助理"

# 定时任务
cron_jobs:
  - name: "早间报告"
    schedule: "0 8 * * *"  # 每天早上8点
    action:
      type: "send_message"
      channel: "telegram"
      template: |
        请生成今日报告：
        1. 查询我所在城市的天气
        2. 列出今天的所有日程
        3. 以友好的方式呈现

# 可用技能
skills:
  - weather
  - calendar

# LLM 配置
llm:
  provider: "anthropic"
  model: "claude-sonnet-4"
```


### 用户收到的消息


```
早安！今日简报

天气情况
上海今天多云，气温 15-23°C
建议穿着：薄外套
降雨概率：10%

今日日程
- 09:00 - 10:00  团队晨会
- 14:00 - 15:30  客户演示
- 16:00 - 17:00  代码评审

温馨提示
今天有 3 个会议，建议提前准备演示材料。
```


---


## 数据流与状态管理


### 数据如何存储？


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-20.svg)


**数据类型及存储方式：**


| 数据类型 | 存储方式 | 保留时间 | 示例 |
| --- | --- | --- | --- |
| 当前会话状态 | 内存 | 直到会话结束 | 正在进行的对话上下文 |
| 对话历史 | 本地数据库 | 可配置（如30天） | 过去的聊天记录 |
| 用户配置 | 配置文件 | 永久 | API密钥、偏好设置 |
| 技能数据 | 技能自己管理 | 取决于技能 | 日程、邮件草稿 |
| 系统日志 | 日志文件 | 可配置 | 错误、调试信息 |

---


## 扩展性与插件生态


### 如何添加新功能？


OpenClaw 的设计允许轻松扩展：


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-21.svg)


### 技能安装流程


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-how-it-works-runoob-22.svg)








	  AI 思考中...





			** [OpenCode Coding Plan](https://www.runoob.com/opencode-coding-plan.html)
			[OpenClaw 配置目录](https://www.runoob.com/openclaw-setup.html) **













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