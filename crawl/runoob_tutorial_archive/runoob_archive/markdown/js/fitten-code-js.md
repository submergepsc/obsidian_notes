# JavaScript AI 编程助手

- Source: https://www.runoob.com/js/fitten-code-js.html

这两年 AI 发展迅猛，作为开发人员，我们总是追求更快、更高效的工作方式，AI 的出现可以说改变了很多人的编程方式。


AI 对我们来说就是一个可靠的编程助手，给我们提供了实时的建议和解决方案，无论是快速修复错误、提升代码质量，或者查找关键文档和资源，AI 作为编程助手都能让你事半功倍。


今天为大家推荐一款适配了 Viusal Studio，VS Code(本文使用)，JetBrains 系列以及 Vim 等多种编译器环境的插件 Fitten Code，Fitten Code 是由非十大模型驱动的 AI 编程助手，它可以自动生成代码，提升开发效率，帮您调试 Bug，节省您的时间，另外还可以对话聊天，解决您编程碰到的问题。


![](https://static.jyshare.com/images/re/fittencode/202509/js/image1.png)


上图为 Fitten Code Agent 模式使用 JavaScript 语言生成的可预览可交互的贪吃蛇小游戏，只需要一句话就可以在很短的时间内看到想要的结果。


除此之外，Fitten Code 免费且支持 80 多种语言：Python、C++、Javascript、Typescript、Java 等。


### 安装


如果您已经安装 VS Code 且版本大于等于 1.68.0，请直接跳过此步骤，否则请点击[[下载]](https://code.visualstudio.com/download)前往官网下载安装VS Code。


打开 VS Code，点击左侧 Extensions（扩展）按钮：


![IMG_256](https://static.jyshare.com/images/re/fittencode/202509/js/image2.png)


在搜索框中搜索关键字 Fitten Code：


![IMG_256](https://static.jyshare.com/images/re/fittencode/202509/js/image3.png)


在搜索结果中点击 Install：


![IMG_256](https://static.jyshare.com/images/re/fittencode/202509/js/image4.png)


登录注册后即可开始使用：


![IMG_256](https://static.jyshare.com/images/re/fittencode/202509/js/image5.jpg)


### 智能补全


打开代码文件，输入一段代码，Fitten Code 就会为您自动补全代码：


![](https://static.jyshare.com/images/re/fittencode/202509/js/image6.png)


按下 `tab` 键接受所有补全建议：


![](https://static.jyshare.com/images/re/fittencode/202509/js/image7.png)


按下 `Ctrl + →` 键(mac 系统为 `Command + →`)接收单个词补全建议：


![](https://static.jyshare.com/images/re/fittencode/202509/js/image8.png)


按下 `Esc` 键取消补全建议


代码智能补全分为三种：普通补全、整项目感知补全、编辑式补全。


具体更详细的补全用法的技巧可详见以下视频：

*>


### Agent 自主编程智能体


自主编程智能体具备强大的主动执行能力：


- 根据任务需求智能调用工具，主动分析背景信息；
- 自主拆解复杂问题，通过多步骤迭代精准完成任务；
- 显著提升编程自动化效率与精细度。


在使用该功能时，只需要输入需要完成的开发任务，例如"将此 js 函数拆分成多个 js 文件并放入当前文件夹下"、"修改此对象，将其封装为类"等，智能体就可以根据任务调用不同工具逐步完成开发任务。


![](https://static.jyshare.com/images/re/fittencode/202509/js/agent基础用法.jpg)


在 Agent 执行的过程中，涉及到创建和修改文件、执行终端命令的操作时，点击"同意"或"拒绝"即可。


![](https://static.jyshare.com/images/re/fittencode/202509/js/同意或拒绝.jpg)


需要和智能体结束对话时，点击右上角菜单中的："回到首页" 即可。


![](https://static.jyshare.com/images/re/fittencode/202509/js/回到首页.jpg)


更多关于 Agent 的使用技巧和方法可以参考以下视频：

>


#### 添加 Rules


在开发程序时，用户项目往往有着各种各样的要求，例如 `统一使用两个空格缩进而不是四个空格`、`一律使用 const 和 let`、`优先使用数组的高阶迭代方法而不是传统for循环` 等等要求，如果 Agent 不知道用户项目定制化的特殊要求，用户可以将这些要求写入规则文件，进而增强 Agent 的代码生成规范和行为规范。


例如：在 Rules 中添加项目的背景介绍和技术栈，Agent 在执行文件创建、重命名时能够更加符合项目规范。或者在 Rules 中添加代码风格要求、Agent 在生成代码时能够更加定制化。您甚至可以告诉 Agent、每次在执行任务前都先阅读一遍指定目录下的所有 README 文档，进而更改 Agent 的行为。


![](https://static.jyshare.com/images/re/fittencode/202509/js/添加rules方法.png)


添加 rules 后，会自动出现 Rules 文件编辑界面，在此处写入文字，每次调用 Agent 智能体时，智能体将自动读取已写好的 rules 文件。进而增强对当前整个项目的理解能力，生成更规范、符合项目要求的代码和回答。


更多关于 rules 的使用方法可以参考如下视频：

>


#### 添加 MCP


用户可以使用 MCP 功能来给 Agent 增加额外的自定义工具。例如"Excel 读取工具"、"github 服务"、"bing 搜索服务"等。使得 Agent 具有自动操作并修改 Excel 等非代码文件的能力、自动调研开源框架和新技术栈的能力、联网搜索某新概念的能力等等。


关于 MCP 的详细使用方法、以及实战技巧可参考以下视频：

>


通过 MCP 和 Rules 的组合使用，可以极大地提高 Agent 的能力，使得 Agent 能够像一个智能助手一样完成庞大项目的功能开发任务。


### AI 问答


#### 基础用法


点击首页左下角的 Chat 模式，开始进行对话。


![](https://static.jyshare.com/images/re/fittencode/202509/js/chat模式.jpg)


当用户选中文件中的代码段再进行对话时，Fitten Code 会自动引用用户所选中的代码段，此时可直接针对选中代码段进行问询等操作。


#### 右键代码快速询问


用户可能选中代码后经常会进行一些高频的提问，例如"这段代码是什么意思"、"帮我给这段代码添加注释"、"帮我优化这段代码"等等。因此用户可以直接通过选中代码后右键，找到 FittenCode 右键选项点击即可立刻调用 FittenCode 智能对话。


![IMG_277](https://static.jyshare.com/images/re/fittencode/202509/js/右键菜单.png)


通过这些常用对话的右键快速调用，可以极大地提高开发效率。


#### 常用语快速输入


Fitten Code 对话框中具有一项特色功能：常用语，它可以让用户快速地在对话框中输入用户经常重复输入的内容，进而构建一个更加强效的提示词、更加全面的上下文环境。


具体关于常用语的实战技巧可以观看如下视频：

>


### 常见问题


如果 VSCode 远程服务器 remote 无法连接外网时，请点击左下角 `⚙` 按钮，再点击设置：


![IMG_277](https://static.jyshare.com/images/re/fittencode/202509/js/image29.png)


然后在设置页面点击右上角 \"打开设置(JSON)\":


![IMG_278](https://static.jyshare.com/images/re/fittencode/202509/js/image30.png)


最后只需在在弹出的 settings.json 文件中添加以下内容即可:


```
"remote.extensionKind": { "FittenTech.Fitten-Code": ["ui"] }
```


![IMG_279](https://static.jyshare.com/images/re/fittencode/202509/js/image31.png)


更多内容参考官网：[https://code.fittentech.com/](https://code.fittentech.com/)


支持以下 4 种编辑器与开发环境：


- [VS Code](https://code.fittentech.com/desc-vscode)：本文会详细介绍
- [JetBrains IDE 系列（包括 PyCharm）](https://code.fittentech.com/tutor_jetbrains_zh#1)
- [Visual Studio](https://code.fittentech.com/tutor_vs_zh#1)：本文会详细介绍
- [Vim](https://code.fittentech.com/tutor_vim_zh#1)








	  AI 思考中...





			* [JavaScript 模板字符串](https://www.runoob.com/js-string-templates.html)
			[JavaScript VScode](https://www.runoob.com/js-vscode.html) **













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

      : ·[JavaScript 实例](https://www.runoob.com/js-examples.html)

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