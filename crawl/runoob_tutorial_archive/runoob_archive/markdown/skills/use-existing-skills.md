# 使用现有 Skills

- Source: https://www.runoob.com/skills/use-existing-skills.html

现在市场上其实已经有了很多大家编写好的 Skills。


比如 Anthropic 官方提供的 Claude Skills： [https://github.com/anthropics/skills](https://github.com/anthropics/skills) 。


该仓库是 Anthropic 官方 Claude 技能合集，配套 Agent Skills 开放标准，支持动态加载拓展 AI 专项能力，技能覆盖设计、开发、企业办公、全品类文档编辑，多数开源，文档底层能力仅供源码参考。


我们可以将本仓库注册为 Claude Code 的插件市场，只需在 Claude Code 中执行以下命令：


```
/plugin marketplace add anthropics/skills
```


![](https://www.runoob.com/wp-content/uploads/2026/01/780e9cce-ff89-4960-ab36-be41428a3899.png)


然后就可以使用 **/plugin **查看：


![](https://www.runoob.com/wp-content/uploads/2026/01/00814d49-4942-45b4-87e7-c14d682a7af5.png)


**安装指定技能集的步骤：**


- 浏览并安装插件（Browse and install plugins）
- 选择 anthropic-agent-skills 插件源
- 选择 document-skills（文档技能） 或 example-skills（示例技能）![](https://www.runoob.com/wp-content/uploads/2026/01/8c5a3a09-2943-49e0-b073-aa5385826510.png)
- 点击立即安装（Install now）![](https://www.runoob.com/wp-content/uploads/2026/01/45288835-7200-48a8-90f0-b9ce408a059d.png)


我们也可直接通过命令安装上述两类插件：


```
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```


**注意：**使用插件安装的 skills 目录在 **～/claude/plugins/marketplaces/** 下。


插件安装完成后，需要重启一下 Claude Code。


使用的时候只需在指令中提及技能名称即可调用，例如安装 document-skills 插件后，可向 Claude Code 下达指令：


```
使用 PDF 技能提取 path/to/some-file.pdf 文件中的表单字段
```


或者创建一个 PPT：


```
创建一个 Agent Skill 的演示文稿
```


可以看到，调用了 **/document-skills:pptx**：


![](https://www.runoob.com/wp-content/uploads/2026/01/74f0eea5-9416-4a27-a827-2378896805c5.png)


开始生成：


![](https://www.runoob.com/wp-content/uploads/2026/01/f5a9c860-9291-4d3f-b72e-7af1ad80a528.png)

之后就会告诉你生成的文件位置：


![](https://www.runoob.com/wp-content/uploads/2026/01/dc42fb40-b5ad-476d-aa64-bdec040f752e.png)

---


## Agent Skills 相关资源整理


| 资源说明 | 链接 |
| --- | --- |
| Skill 聚合入口 | https://skills.sh/ |
| Skills 市场（中文界面） | https://skillsmp.com/zh |
| Agent Skills 官方标准站点 | https://agentskills.io |
| Anthropic 官方工程文章（Agent Skills 实战理念） | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills |
| VS Code Copilot Agent Skills 文档 | https://code.visualstudio.com/docs/copilot/customization/agent-skills |
| Anthropic 官方 Skills GitHub 仓库 | https://github.com/anthropics/skills |
| Claude 技能精选列表（Awesome 系列） | https://github.com/ComposioHQ/awesome-claude-skills |
| 软件开发自动化工作流 Skills 集合 | https://github.com/obra/superpowers |
| 自动生成 Skill 的 Skill（官方示例） | https://github.com/anthropics/skills/tree/main/skills/skill-creator |








	  AI 思考中...





			** [Skills 工作原理](https://www.runoob.com/how-skills-work.html)
			[SKILL.md 文件](https://www.runoob.com/skill-md-file.html) **













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

                  : · [VS Code 创建与...](https://www.runoob.com/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/skills-first.html)




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