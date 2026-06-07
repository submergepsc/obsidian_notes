# 第一个 AI Agent

- Source: https://www.runoob.com/ai-agent/first-ai-agent.html

AI Agent 平台种类繁多，但核心目的相同：让模型从回答问题升级为自动执行任务，有的主打零代码拖拽，有的强调工程化定制，也有专门做流程集成或多代理协作。


不同层级的使用场景拆成三个面向：搭建速度、系统衔接、可控深度。


| 核心需求 | 推荐工具 | 关键优势 |
| --- | --- | --- |
| 秒哒，一句话生成应用 | 秒哒官网 | 0 代码，通过一句话生成需求，并生成应用 |
| MonkeyCode，AI 应用开发平台 | MonkeyCode 官网 | 直接在平台里创建任务，让 AI 编码，在云端开发环境中使用终端、文件管理和预览 |
| 扣子，零代码搭建对话机器人 | Coze | 全托管环境，靠提示词、插件、知识库即可形成可用机器人 |
| QoderWork ，桌面级 AI Agent | QoderWork | 你说需求，它交付结果。 |
| 自动化触发与系统对接 | n8n | 集成面广，可自托管，常规内部系统都能打通 |
| 开发者可控的深度定制 | Dify / LangChain | 前者提供完整开源方案；后者适合构建复杂推理链路 |
| 多角色协作与任务分解 | AutoGen / CrewAI | 前者强调动态协作；后者以清晰角色体系驱动流程 |

---


### 0 生成应用代码


  **


    **
      我们可以先用最简单的秒哒来生成应用，
      先访问官网注册
      [秒哒官网](https://www.miaoda.cn/?invitecode=user-93thly701s00)
      ，登录后在输入框输入要生成的应用。
    **



![](https://www.runoob.com/wp-content/uploads/2025/12/3cbb89ab-9035-49cf-9d37-10d699f56608.png)

接下来秒哒就开始生成一份需求文档，还是很详细的，然后我们可以在右侧点编辑文档或生成应用按钮，它就会根据我们的需求直接开始生成应用：


![](https://www.runoob.com/wp-content/uploads/2025/12/a79f912c-ac27-499b-8dcc-5185f8ae4992.png)


接下来就会开始生成代码，整个过程，都不用写一行代码，直接生成：


![](https://www.runoob.com/wp-content/uploads/2025/12/6871e121-8c71-45b4-9733-c5d1c6bea507.png)


看下界面及使用效果，非常好用：


![](https://www.runoob.com/wp-content/uploads/2025/12/20559228-55a3-4544-896f-cab55d636178-1.png)


另外插件部分还提供了其他高级功能支持，比如视频：

![](https://www.runoob.com/wp-content/uploads/2025/12/3c692dbf-a9a1-4ba1-82cb-1eb9bd5f725e.png)


如果你还不知道能看啥，还能去应用广场看看其他人做的优秀产品：


![](https://www.runoob.com/wp-content/uploads/2025/12/5db9f27d-eaab-4984-a75c-a32f1608aa47.png)


接下来我们做一个简单的智能体--旅行规划师。


AI Agent平台有很多，我们本章节直接用字节的 **扣子 (Coze)** 来做。


---


## 1、注册账号


  **


    **第一步：**
    打开官网
    [Coze 官网](https://www.coze.cn/overview?utm_medium=daohang&utm_source=runoob&utm_term=hw_coze_runoob)
    并登录。
    **

    登录后，选择智能体开发**

      （现在 OpenClaw 也支持，不过需高级用户）




![](https://www.runoob.com/wp-content/uploads/2025/12/3735845f-34f4-4bdc-947f-a1499860d276.png)


---


## 2、开始搭建：三步走


我们要做的智能体叫 **大理旅行小助手**，它的功能：查天气、找景点、安排路线。


### 第一步：创建智能体


- 点击创建智能体。
- **智能体名称**：填 `大理旅行小助手`。
- **智能体介绍**：填 `帮用户规划去大理的旅行行程`。
- 点击 **"确认"**，进入编辑页面。


![](https://www.runoob.com/wp-content/uploads/2025/12/e565c4cc-6e2e-4800-8a7f-29e2ee3423dd.png)


### 第二步：编写人设


在左侧的 **"人设与回复逻辑"** 输入框里，填入以下内容（直接复制）：


```
# 角色
你是一个经验丰富的大理本地导游，热情、幽默，对大理的吃喝玩乐了如指掌。

# 技能
1. 根据用户的时间和预算，规划合理的行程。
2. 推荐当地的小众景点和美食，避开游客陷阱。
3. 语气要轻松活泼，多用 Emoji。

# 限制
- 只回答与大理旅行相关的问题。
- 如果不知道答案，直接说不知道，不要瞎编。
```


![](https://www.runoob.com/wp-content/uploads/2025/12/9562d18c-b231-4f2e-aa1a-e080ff1c1b20-scaled.png)


### 第三步：添加插件


光有人设它只是个陪聊的，我们要给它加工具。


- 在中间的 **"插件"** 区域，点击 `+` 号。 ![](https://www.runoob.com/wp-content/uploads/2025/12/e565c4cc-6e2e-4800-8a7f-29e2ee3423.png)
- 搜索 `博查搜索` (可以调用 bing 搜索) 或 `Google`，点击 **"添加"**。 *为什么要加这个？让它能联网查最新的天气和门票价格。![](https://www.runoob.com/wp-content/uploads/2025/12/751175d7-7dac-4c28-8e30-2b698c7b8fef.png)*
- 搜索 `墨迹天气` (或者任意天气插件)，点击 **"添加"**。![](https://www.runoob.com/wp-content/uploads/2025/12/fdb4c9eb-3d3d-41e6-8641-3debff9b512e.png)


之后就能看到已安装的搜索插件了：


![](https://www.runoob.com/wp-content/uploads/2025/12/c5723237-2cbb-4d2b-ad2f-bc2838cb891c.png)


---


## 3、见证奇迹的时刻


现在，看右侧的 **预览与调试** 区域。**试着对它说：


> "我打算下周五去大理玩3天，预算2000元，喜欢安静的地方，帮我安排一下行程。"**


![](https://www.runoob.com/wp-content/uploads/2025/12/85fc9849-c773-4870-a8ca-4fe8e9d3209d.png)


### 观察它在做什么：


你会看到它不会马上回答，而是显示 **"正在使用 博查搜索社区…"** 或者 **"正在使用 天气…"**。这就是 Agent 在**思考和行动**！


![](https://www.runoob.com/wp-content/uploads/2025/12/90f1672f-7b59-49a0-9ede-ef19bdc1452e.png)


- 它先去查了下周五大理的天气。
- 它去搜了适合"安静"的景点（比如喜洲古镇、沙溪）。
- 最后它综合信息，给你写出了一份带天气提醒的行程单。


---


## 4、发布你的 Agent


如果你觉得满意了，就可以点击右上角的 **发布** 按钮：


![](https://www.runoob.com/wp-content/uploads/2025/12/1a61ee5f-dbe3-4a73-8686-3a1c4197b91f.png)


可以发布到 **豆包**、**飞书** 或者 **微信公众号**。


![](https://www.runoob.com/wp-content/uploads/2025/12/26b955e3-0566-4a9a-a487-a3337fdbaa23.png)


也可以复制链接，把生成的链接发给朋友："看，这是我开发的 AI 导游！"


![](https://www.runoob.com/wp-content/uploads/2025/12/b376fa24-406f-424c-8383-7fe3bc31140a-1.png)









	  AI 思考中...





			** [AI Agent 核心组件](https://www.runoob.com/ai-agent-core.html)
			[Python 实现 AI Agent](https://www.runoob.com/python-ai-agent.html) **













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