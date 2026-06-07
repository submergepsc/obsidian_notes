# Skills 工作原理

- Source: https://www.runoob.com/skills/how-skills-work.html

你可能会好奇：智能体又不是人，它怎么知道某个 Skill 能做什么、该怎么做？


** 答案很简单——靠读文件。**


每个 Skill 背后，都有一个描述文件，通常叫 **SKILL.md**，就像一份说明书。


### Skills 的工作原理


Skills 使用渐进式披露（Progressive Disclosure）的方式，让代理在不同的阶段加载不同详细程度的信息。这种设计使得代理可以同时管理大量技能，而不会耗尽上下文空间。


### 三个阶段


代理加载技能分为以下三个阶段：


- **1. 发现阶段（Discovery）：**当对话开始时，代理会扫描所有可用的技能文件夹，只读取每个技能的名称（name）和描述（description）。这是最轻量的信息，足以让代理判断某个技能是否可能与当前任务相关。
- ** 2. 激活阶段（Activation）：**当代理判断某个技能的描述与用户请求相匹配时，会将完整的 SKILL.md 文件内容加载到上下文中。这时代理会读取完整的指令和说明。
- **3. 执行阶段（Execution）：**代理按照 SKILL.md 中的指令执行任务。在这个过程中，代理可能会调用技能附带的脚本、读取参考资料或使用其他资源。


### 渐进式加载的优势


| 阶段 | 加载内容 | 典型大小 |
| --- | --- | --- |
| 发现阶段 | name + description | 约 100 tokens |
| 激活阶段 | 完整 SKILL.md | 建议不超过 5000 tokens |
| 执行阶段 | 脚本、参考资料等 | 按需加载 |


智能体在执行任务之前，会先读这份说明书，搞清楚三件事：


- 这个 Skill 能干什么？（能力描述）
- 要用它，我需要提供什么？（输入参数）
- 做这件事有什么规矩？（环境约束和注意事项）


读完之后，智能体就知道：哦，这个 Skill 适合用来解决当前的问题，我来调用它。


下面这张图展示了这个过程：





























智能体如何"读懂"一个 Skill？ 🧠 智能体大脑 "我需要找一个能完成任务的技能" 读取 📄 SKILL.md ① 能做什么（描述） ② 需要什么（参数） ③ 有什么规矩（约束） ↓ 读完就全懂了 理解 ✅ 懂了！ 可以调用了 💡 打个比方 想象你新入职一家公司，拿到一本《岗位操作手册》： 📖 岗位说明 "你是客服，负责处理退款" 📋 操作流程 "先核实订单号，再提交退款" ⚠️ 注意事项 "超过500元需主管审批" 读完手册，你就知道自己该干什么、怎么干、什么不能干了。 SKILL.md 对智能体来说，就是这本"操作手册"。 ### Skill 执行流程 - 从用户指令开始，先进行 Skill 意图识别，决定是否进入受控执行路径。 - 命中 Skill 后，系统加载 SKILL.md，建立工具权限与行为边界，再结合上下文进行推理。 - 只有在确实需要时才调用被允许的外部工具，否则在规则内完成逻辑。 - 最终结果经过约束整合后输出，用户的下一次输入触发新一轮完整流程。 ![](https://www.runoob.com/wp-content/uploads/2026/01/claude-agent-skills-runoob.png)









	  AI 思考中...





			** [第一个 Skill](https://www.runoob.com/skills-first.html)
			[使用现有 Skills](https://www.runoob.com/use-existing-skills.html) **













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