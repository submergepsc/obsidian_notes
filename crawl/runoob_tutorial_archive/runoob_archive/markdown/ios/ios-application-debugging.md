# IOS应用程序调试

- Source: https://www.runoob.com/ios/ios-application-debugging.html

---


## 简介


当我们做应用程序的时候，可能会犯各种错误，这可能会导致各种不同的错误。因此，为了修复这些错误或缺陷，我们需要来调试应用程序。


### 选择一个调试器


Xcode中调试器即 GDB 和 LLDB 调试器，GDB 是默认的。 LLDB是一个调试器是LLVM开源的编译器项目的一部分。您可以更改调试，编辑活动计划选项。


### 如何查找编码错误？


我们只需要建立我们的应用程序，代码被编译器编译，所有的消息，错误和警告将显示以及错误的原因，我们可以纠正他们。可以点击 product，然后点击"分析"，将在应用程序中可能发生的问题。


### 设置断点


断点帮助我们了解我们的应用程序对象，帮助我们找出许多缺陷，包括逻辑问题的不同状态。我们只需要点击创建一个断点的行号。我们可以通过点击并拖动它删除断点。如下所示


![debug_Breakpoint](https://www.runoob.com/wp-content/uploads/2013/11/debug_Breakpoint.jpg)


当我们运行应用程序并选择playVideo，按钮的应用程序将被暂停，我们来分析一下我们的应用程序的状态。当断点被触发时，我们将得到一个输出，如下图所示


![debug_BreakpointStop](https://www.runoob.com/wp-content/uploads/2013/11/debug_BreakpointStop.jpg)


可以轻松地确定哪个线程触发断点。在底部可以看到对象，如self，sender等，这些持有相应的对象的值，我们可以展开一些这些对象，看看他们每个的状态是什么。


要继续应用程序，我们在调试区选择继续按钮（最左边的按钮），如下图所示。其他选项包括步骤和单步跳过 ![](http://www.tutorialspoint.com/ios/images/breakpointBar.jpg)


### 异常断点


我们也有异常断点，触发应用程序停止发生异常的位置。通过选择调试导航后选择"+"按钮，我们可以创建异常断点。将得到下面的窗口


![debug_ExceptionBreakpoint](https://www.runoob.com/wp-content/uploads/2013/11/debug_ExceptionBreakpoint.jpg)


然后，我们需要选择" Exception Breakpoint (添加异常)"断点，它会显示下面的窗口


![debug_ExceptionBreakpointAll](https://www.runoob.com/wp-content/uploads/2013/11/debug_ExceptionBreakpointAll.jpg)


### 下一步是什么？


你可以在 [Xcode 4 用户指南](http://developer.apple.com/library/ios/#documentation/ToolsLanguages/Conceptual/Xcode4UserGuide/Introduction/Introduction.html) 知道更多关于调试和其他Xcode功能的知识。








	  AI 思考中...





			** [iOS内存管理](https://www.runoob.com/ios-memory.html)














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