# VSCode 运行和调试代码

- Source: https://www.runoob.com/vscode/vscode-run-and-debug.html

VS Code 内置了运行和调试 Node.js 应用程序的支持。

本章节，我们将使用上一部分[安装的 Python 扩展](https://www.runoob.com/vscode-extensions.html)来调试一个 Python 程序。


接下来就让我们调试前面创建的 hello.py 程序。


调试前确保您的计算机已安装 Python 3。

如果您的计算机上未安装 Python 解释器，窗口右下角会弹出通知。

选择 Select Interpreter（选择解释器） 打开命令面板，从中选择您想使用的 Python 解释器，或安装一个新的解释器。


### 设置断点

在 hello.py 文件中，将光标放置在 print 行上，点击小红点（鼠标移动到红点位置会显示），或者按下 **F9** 键来设置断点。


编辑器左侧的边距中会出现一个红点，表示已设置断点。


断点可以让您在程序执行到某一行代码时暂停，便于调试。


![](https://www.runoob.com/wp-content/uploads/2024/12/python-set-breakpoint.png)


### 启动调试会话

按下 **F5** 启动调试会话。

系统会提示选择调试器，选择 Python 调试器。


![](https://www.runoob.com/wp-content/uploads/2024/12/python-debug-configuration.png)


选择运行当前的 Python 文件：


![](https://www.runoob.com/wp-content/uploads/2024/12/python-select-debugger.png)


### 调试代码

程序启动后，执行会在您设置的断点处暂停。


![](https://www.runoob.com/wp-content/uploads/2024/12/vscode-debugging.png)


**提示：**将鼠标悬停在编辑器中的 name 变量上，即可查看其值。在调试视图的 变量视图（Variables View） 中，您可以随时查看变量的值。


### 继续执行程序

在调试工具栏中，点击 Continue（继续） 按钮，或再次按下 F5，以继续执行程序。

![](https://www.runoob.com/wp-content/uploads/2024/12/debug-toolbar-play.png)


VS Code 提供了许多高级的调试功能，例如监视变量（Watch Variables）、条件断点（Conditional Breakpoints）和启动配置（Launch Configurations）。










	  AI 思考中...





			** [VSCode 安装扩展](https://www.runoob.com/vscode-extensions.html)
			[VSCode code 命令](https://www.runoob.com/vscode-code-command.html) **













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