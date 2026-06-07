# skill-creator 使用

- Source: https://www.runoob.com/claude-code/skill-creator-usage.html

在 Claude Code 生态中，Skill（技能） 是扩展 Agent 能力的重要机制。

Skill 本质上是一个模块化知识包，可以给 Claude 添加：



- 专业领域知识
- 固定工作流程
- API / 工具使用方式
- 模板和脚本


简单理解：


```
Skill = 给 AI 写的一份操作说明书。
```


而 skill-creator 就是 Anthropic 官方提供的 Skill 开发助手，帮助开发者创建、优化和打包技能。

GitHub 地址：[https://github.com/anthropics/skills/tree/main/skills/skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)


### Skill 是什么


在 Claude Code 中，Skill 是一种 可复用的能力扩展包。


一个 Skill 通常包含：


```
skill-name/
├── SKILL.md        # 核心说明（必须）
├── scripts/        # 可执行脚本
├── references/     # 文档或知识
├── assets/         # 附加资源
```


其中最重要的是 SKILL.md。


示例：


```
---
name: video-tool
description: Video processing CLI for editing and transcribing videos
---

# Video Tool Skill

Use the video-tool CLI to process videos.

## Quick Start

video-tool video download -u URL
video-tool generate transcript -i video.mp4
```


SKILL.md 的作用就是：教 Claude 如何使用某个工具或完成某个流程。


### 安装 skill-creator


首先安装 Anthropic 的 skills 集合。


```
npx skills add https://github.com/anthropics/skills --skill skill-creator
```


或者：


```
claude install anthropics/skills/skill-creator
```


安装完成后，你就可以在 Claude 中调用：


```
/skill-creator
```


![](https://www.runoob.com/wp-content/uploads/2026/03/49085a23-ff2a-4ca5-af60-f9f1872b8f4b.png)


skill-creator 提供完整的 Skill 开发流程工具链。


安装完成后，本地会下载该 Skill，其中包含：


```
skills/skill-creator/
├── SKILL.md          ← 核心说明文件
├── agents/           ← 内置的评审助手
├── eval-viewer/      ← 测试结果可视化工具
├── references/       ← 参考文档（数据格式说明等）
└── scripts/          ← 自动化脚本（打包、测评等）
```


Skill Creator 的工作流程可以概括为一个循环：


```
想清楚需求
    ↓
起草 SKILL.md
    ↓
设计测试用例
    ↓
运行测试（有 Skill vs 没有 Skill，对比效果）
    ↓
评估结果（看报告 + 打分）
    ↓
根据反馈修改 SKILL.md
    ↓
重复，直到满意
    ↓
打包成 .skill 文件
```


---


## 用 skill-creator 创建 Skill


### 需求询问


Claude 会先问你几个问题，帮你把需求想清楚。你不需要一次说完所有细节，像聊天一样回答就行。


**Claude 通常会问：**


- 这个 Skill 具体做什么？
- 什么情况下触发（用户说什么、上传什么文件）？
- 输出是什么格式？
- 有没有特殊要求（固定模板、特定格式规范……）？


**示例对话：**


```
你：我想做一个 Skill，把会议录音的文字稿整理成结构化的会议纪要。

Claude：好的，我来问几个问题帮你确认需求：
        1. 纪要里需要包含哪些内容？（比如：时间、参与人、决议、行动事项……）
        2. 输出格式是 Word 文档、Markdown，还是直接在对话里回复？
        3. 有没有固定的纪要模板？

你：需要包含会议主题、时间、参与人、讨论要点、决议事项、
    下一步行动（含负责人和截止日期）。
    输出 Word 文档。
    有模板，我来上传。
```


![](https://www.runoob.com/wp-content/uploads/2026/03/328e2713-f38c-4079-a832-555b7a19e9f0.png)


可以按 Tab 键或方向按键切换菜单详情，并提交。


这个阶段你的目标： 把所有细节和边界情况说清楚，不要跳过，后面测试时踩的坑大多源于这里没说清楚。


也可以直接回车，它也能帮我们创建：


![](https://www.runoob.com/wp-content/uploads/2026/03/f5d438c9-dc20-4465-9d30-c22edaf87f3e.png)


之后 Claude 会写出 SKILL.md 草稿，大致长这样：


![](https://www.runoob.com/wp-content/uploads/2026/03/7d25c5a6-fba5-41ae-99f7-1421774459ee.png)


接下来还会创建参考文件：


![](https://www.runoob.com/wp-content/uploads/2026/03/6eddc6e5-d124-43ae-9fd6-3e81b2b0aa48.png)


创建完成后，会验证技能结构是否正确，等待就好了。


验证通过！就会打包 Skill，并展示目录结构：


![](https://www.runoob.com/wp-content/uploads/2026/03/4c93a5ac-6e28-48eb-82e9-a23b3568783f.png)


测试下，输入会议内容：


```
整理以下会议纪要：一、会议基本信息
  会议主题：学习平台内容优化会议
  参会人员：张三、李四、王五
  会议时间：2025-XX-XX 14:00-15:00
  记录人：张三
  二、会议内容
  讨论当前团队在编程教学中使用的案例素材，一致认为runoob教程简洁易懂，适合作为新手入门参考。
  确定后续内部培训将优先采用 runoob 上的基础语法、实战小案例进行讲解。
  安排李四整理 runoob 中 Python、Java 高频知识点，形成内部速查文档。
  下次会议检查文档完成情况。
  三、待办事项
  李四：整理 runoob 核心知识点文档，下周一前完成。
  全体：提前熟悉 runoob 对应章节，便于下次讨论。
```


![](https://www.runoob.com/wp-content/uploads/2026/03/c1fc4b18-f5d5-4c3c-8a28-d6ffc7c02410.png)








	  AI 思考中...





			** [Coding Plan](https://www.runoob.com/coding-plan.html)
			[Claude Code 项目初始化](https://www.runoob.com/claude-code-init.html) **













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