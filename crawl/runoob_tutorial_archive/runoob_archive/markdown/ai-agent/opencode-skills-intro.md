# OpenCode skills 使用

- Source: https://www.runoob.com/ai-agent/opencode-skills-intro.html

在之前的内容，我们已经了解了 OpenCode 和 skills，如果还没阅读，可以参阅：


- [OpenCode 入门教程](https://www.runoob.com/opencode-coding-agent.html)
- [Skills 教程](https://www.runoob.com/skills-agent.html)


接下来我们将将介绍如何在 OpenCode 中使用 skills。


现在市面上已经有很多现成的 skills，我么可以直接拿来使用，我们可以在 [https://skills.sh/](https://skills.sh/) 查找更多的 skill。


安装方式：


```
npx skills add <owner/repo>
```


**注：**如果对 npx 不了解，可以参阅：[npx 入门教程](https://www.runoob.com/../nodejs/npx-intro.html)


---


## ui-ux-pro-max

接下来我们使用 ui-ux-pro-max 这个 skill 演示，地址：[https://skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ui-ux-pro-max](https://skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ui-ux-pro-max)。


UI/UX Pro Max 是一个 AI 设计智能技能（AI Skill），为构建专业级 用户界面（UI）和用户体验（UX） 提供结构化设计知识和自动化辅助，主要用于与 AI 编码助手集成（例如 Claude Code、Cursor、Windsurf 等）。


UI/UX Pro Max 包含一个可搜索的设计数据库，可根据自然语言提示智能推荐界面风格、配色、排版与组件实现方式。


安装命令：


```
npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max
```


安装过程，可以勾选我们需要的环境，比如 OpenCode：


![](https://www.runoob.com/wp-content/uploads/2026/02/7345bb6f-82e9-4228-8772-70e22b53c9f1.png)


接下来这里选择当前目录也就是我们之前创建的 **opencode-runoob-test**，另一个选项 **Global** 是全局安装：


![](https://www.runoob.com/wp-content/uploads/2026/02/07e6ffab-eed0-47ef-83e1-8cf1cbd37ce7.png)

接下来一路回车就好了。


使用 **opencode** 命令打开 OpenCode，输入 **/ui** 就可以看到安装的 skill：


![](https://www.runoob.com/wp-content/uploads/2026/02/94078c59-8f03-486c-9247-c61ff90de3d8.png)


接下来我们就可以直接输入需求：


```
为宠物美容服务搭建一个着陆页，风格活泼亲和，并设置预约类行动召唤按钮。
```


AI 会自动调用我们安装的 skill 来设计，一路回车就好了：


![](https://www.runoob.com/wp-content/uploads/2026/02/6740cb33-2d26-4475-b825-df49a97417b9.png)


接下来自动生成目录与文件：


![](https://www.runoob.com/wp-content/uploads/2026/02/b27e2a0f-910d-4012-8d8e-0294dbf69bdf.png)


然后查看最终效果，好看很多：

![](https://www.runoob.com/wp-content/uploads/2026/01/a9d18e1c-ae82-4dfa-bb9f-f7fe30a01cb7-scaled.png)


---


## remotion-best-practices


接下来使用 remotion-best-practices 这个 skill 来演示。


- Opencode：一个负责让 AI 写代码自动化流程
- remotion-best-practices：一个负责用 React 直接生成视频的 skills


remotion-best-practices 是针对 Remotion 的专门技能，包含数十个规则文件（基于官方最佳实践），例如：


- 三维内容（3D）
- 动画基础
- 媒体导入（图片、音频、字体）
- 字幕与字幕同步
- 序列与场景组织
- 透明视频与剪辑
- 文本动画 & 插值方法 …


skill 地址：[https://skills.sh/remotion-dev/skills/remotion-best-practices](https://skills.sh/remotion-dev/skills/remotion-best-practices)


### 安装与使用


开始前我们先创建一个目录 **opencode-runoob-test**:


```
mkdir opencode-runoob-test
cd opencode-runoob-test
```


在 opencode-runoob-test 目录下我们可以使用 npx 命令来安装：


```
npx skills add remotion-dev/skills
```


![](https://www.runoob.com/wp-content/uploads/2026/02/d20bbdce-71f0-486f-a36a-9e3d330bfe23.png)

安装过程，可以勾选我们需要的环境，比如 OpenCode：


![](https://www.runoob.com/wp-content/uploads/2026/02/7345bb6f-82e9-4228-8772-70e22b53c9f1.png)


接下来这里选择当前目录也就是我们之前创建的 **opencode-runoob-test**，另一个选项 **Global** 是全局安装：


![](https://www.runoob.com/wp-content/uploads/2026/02/07e6ffab-eed0-47ef-83e1-8cf1cbd37ce7.png)

接下来一路回车就好了，之后会显示安装目录及支持的开发工具：


![](https://www.runoob.com/wp-content/uploads/2026/02/2d9dab42-dc41-45d5-bc04-c10bc664e856.png)


用 VS Code 打开 目录 **opencode-runoob-test**就可以看到这个 skill 了：


![](https://www.runoob.com/wp-content/uploads/2026/02/e6bdede2-9a4a-4cbf-894c-abd3f6871a2d.png)

我们也可以打开 OpenCode，输入 **/remotion** 就可以看到这个 skill：


![](https://www.runoob.com/wp-content/uploads/2026/02/0058151a-0f77-483c-83de-10c0b91e74d0.png)


然后在输入框输入：


```
生成一个 Hello Runoob！的演示视频
```


接下来 AI 就会找到这个 skill（技能）：


![](https://www.runoob.com/wp-content/uploads/2026/02/777dbe1f-5d3a-48ae-8290-516813b54c40.png)


然后 AI 就会使用这个 skill 来开始设计编写：


![](https://www.runoob.com/wp-content/uploads/2026/02/92bbefa8-f6e2-403c-8f24-718ecab66613.png)









	  AI 思考中...





			** [Trae Solo](https://www.runoob.com/trae-solo.html)
			[AI Agent 工作原理](https://www.runoob.com/ai-agent-working-principle.html) **













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