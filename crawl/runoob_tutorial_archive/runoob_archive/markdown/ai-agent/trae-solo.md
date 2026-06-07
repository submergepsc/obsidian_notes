# Trae Solo

- Source: https://www.runoob.com/ai-agent/trae-solo.html

Trae 是字节跳动推出的一款面向开发者的 AI 集成开发环境（IDE），基于 VS Code，提供智能问答、代码自动补全以及基于 Agent 的 AI 自动编程能力。


简单说就是写代码、做开发的 AI 工具，支持多种编程语言和开发场景。


  **


    **访问 Trae 国内官网：**
    [Trae 官网](https://www.trae.com.cn/?utm_source=advertising&utm_medium=runoob_ug_cpa&utm_term=hw_trae_runoob)



默认情况，下载按钮会自动匹配我们的电脑系统，我们也可以找到适合自己电脑操作系统的 Trae 安装包，进行下载。


[![](https://www.runoob.com/wp-content/uploads/2026/02/dc3b43f9-53f0-412d-ab29-e2bffdfd4cf7.png)](https://www.trae.com.cn/?utm_source=advertising&utm_medium=runoob_ug_cpa&utm_term=hw_trae_runoob)


Trae 安装可以参考：[https://www.runoob.com/w3cnote/trae-tutorial.html](https://www.runoob.com/w3cnote/trae-tutorial.html)


SOLO 模式 是 Trae 的核心功能之一，由 AI 主导开发全流程。


在 SOLO 模式下我们只需用自然语言说清需求（比如：写一个获取低价商品的函数），AI 会自动拆解任务、生成代码、甚至帮你检查变更，无需手动完成复杂操作。


---


## SOLO 模式


SOLO 模式以 AI 为核心主导，全程自动规划与执行从需求理解、代码生成、测试到成果预览的全开发流程。

在 SOLO 模式下， 我们只需通过自然语言描述、语音沟通或上传本地文件等灵活方式提交需求，AI 会快速自主拆解任务、高效推进执行，让开发过程变得极度简化、全程智能化。


访问官网下载安装：** [https://www.trae.cn/](https://www.trae.com.cn/?utm_source=advertising&utm_medium=runoob_ug_cpa&utm_term=hw_trae_runoob)**


### 开启 SOLO 模式

安装完 Trae 后，打开 Trae，点击界面左上角的模式切换按钮，即可将 TRAE 切换至 SOLO 模式。


![](https://www.runoob.com/wp-content/uploads/2026/02/db08ad06-5a97-4d62-bb7e-0580860ba084.png)


### 用户界面

SOLO 模式采用三栏式布局，从左到右依次为：任务管理面板、AI 对话面板、工具面板。


![](https://www.runoob.com/wp-content/uploads/2026/02/465c519c-c7a9-458d-8590-d9949b2b3104.png)


---

## SOLO Coder 介绍

SOLO Coder 是面向复杂项目开发的智能体，能帮你高效完成从需求迭代到架构重构的全流程开发。


SOLO Coder 具备智能任务规划与精准执行能力，确认计划后会自动推进开发进度；你还能自主编排多个智能体，组建专属 AI 团队，实现多角色协同，加速项目落地。


**注意：**SOLO Coder 默认启用 Auto 模式且不可修改，该模式会综合权衡问答速度、性能与资源占用，智能匹配合适模型，带来更流畅的 AI 交互体验。


### 启用 SOLO Coder

进入 SOLO 模式后，点击 AI 对话输入框左下角的 @ 符号，在智能体菜单中选择 SOLO Coder 即可。


![](https://www.runoob.com/wp-content/uploads/2026/02/a37a0b7e-8e25-4599-bbf0-487acf639473.png)


### 编辑 SOLO Coder

你可为 SOLO Coder 配置可调用的自定义智能体、MCP Server 及内置工具。

将鼠标悬浮至 SOLO Coder 右侧的配置图标，点击面板中的「编辑工具」按钮，进入 SOLO Coder 配置面板，完成对应配置即可。


![](https://www.runoob.com/wp-content/uploads/2026/02/0wc-quality_q75.webp)


### 调用自定义智能体

SOLO Coder 支持调用自定义智能体，完成模块化任务处理。

其默认内置 Search 智能体，可检索与查看文件，辅助精准调度其他智能体协同完成任务。

为 SOLO Coder 配置好可用智能体后，它可作为主控智能体，在处理长上下文、高复杂度任务时，自动拆分并隔离任务，按需调用对应智能体，使各智能体在独立上下文内专注执行，提升整体执行效率与结果质量。

你也可在提示词中直接指定目标智能体，SOLO Coder 会结合上下文，在合适时机完成调用。


![](https://www.runoob.com/wp-content/uploads/2026/02/quality_q75.webp)


### Plan 模式


Plan 模式适用于复杂长任务，开关位于对话框右上角，也可通过快捷键快速开启：macOS 为 `Option + P`，Windows 为 `Alt + P`。


![](https://www.runoob.com/wp-content/uploads/2026/02/fda2159b100743789quality_q75.webp)


开启后，SOLO Coder 收到需求会先进行分析与任务规划，经你确认后再逐步骤执行。


![](https://www.runoob.com/wp-content/uploads/2026/02/101fa9ca26a242d3b0q75.webp)


若生成计划不符合预期，可通过两种方式修改：


- 直接手动编辑计划内容，完成后点击「执行」按钮；
- 向 SOLO Coder 发送修改指令，由其自动调整规划内容。


---


## 启用 SOLO Builder

SOLO Builder 是 TRAE 的 SOLO 模式内置的两大核心智能体之一，主打从 0 到 1 快速落地完整 Web 应用，不用开发者手动编写大量代码，就能高效实现创意原型或全新项目的搭建，适配原型验证、快速落地创意等场景。


### 启用 SOLO Builder


进入 SOLO 模式后，点击 AI 对话输入框左下角的 **@** 符号，在智能体菜单中选择 SOLO Builder 即可。


![](https://www.runoob.com/wp-content/uploads/2026/02/a37a0b7e-8e25-4599-bbf0-487acf639473.png)










	  AI 思考中...





			** [OpenClaw 一键部署](https://www.runoob.com/openclaw-cloud.html)
			[OpenCode skills 使用](https://www.runoob.com/opencode-skills-intro.html) **













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