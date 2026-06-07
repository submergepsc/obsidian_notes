# C# AI 编程助手

- Source: https://www.runoob.com/csharp/fitten-code-csharp.html

AI 技术的飞速发展正在深刻改变开发者的工作方式。在后端项目开发中，我们常常被分析项目功能和排查项目问题降低效率。因此，AI 的出现可以改变我们的编程方式与提高效率。


AI 对我们来说就是一个可靠的编程助手，给我们提供了实时的建议和解决方案，无论是代码补全、快速修复错误，或者查找关键文档和资源，AI 作为编程助手都能让你事半功倍。


今天为大家推荐一款 VSCode 的插件 Fitten Code，Fitten Code 是由非十大模型驱动的 AI 编程助手，它可以通过智能体自动完成大型项目中的功能、自动生成代码，提升开发效率，帮您调试 Bug，节省您的时间，另外还可以对话聊天，解决您编程碰到的问题。


Fitten Code 免费且还支持 80 多种语言：Python、C++、Javascript、Typescript、Java 等，能够满足不同身份背景的开发者使用。


### 1、安装


点击上方工具栏拓展选项，选择管理拓展选项


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image1.png)


接着在联机页面中搜索"Fitten Code"，并点击下载，下载完成后重启 Visual Studio


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image2.png)


在扩展选项中选中 fitten，选择 Open Chat Window 进入登录界面，完成注册登录


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image3.png)


### 2、智能补全


首先请按照上方提示关掉 IntelliCode 的补全功能，防止冲突：


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image4.png)


打开代码文件，输入一段代码，Fitten Code 就会为您自动补全代码：


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image5.png)


按下 `tab` 键接受所有补全建议：


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image6.png)


按下 `Ctrl + →` 键接收单个词补全建议：


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image7.png)


按下 `Esc` 键取消补全建议


代码智能补全分为三种：普通补全、整项目感知补全、编辑式补全。


具体更详细的补全用法的技巧可详见以下视频：


*


### 3、AI 问答


用户可通过点击左上角工具栏中的"Fitten Code — 开始新对话"打开对话窗口进行对话：


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image8.png)


当用户选中代码段再进行对话时，Fitten Code 会自动引用用户所选中的代码段，此时可直接针对该代码段进行问询等操作：


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image9.png)


### 4、生成代码


可在 Fitten Code 工具栏中选择"Fitten Code - 生成代码"，然后在输入框中输入指令即可生成代码


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image10.png)


### 利用注释后的自动补全功能生成代码


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image11.png)


也可以利用对话功能生成代码


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image12.png)


### 5、代码翻译


Fitten Code 可以实现代码的语义级翻译，并支持多种编程语言之间的互译。有以下两种方法可以实现。


（1）选中需要进行翻译的代码段，右键选择"Fitten Code — 重构选择代码"，然后在输入框中输入需求即可完成转换


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image13.png)


（2）选中需要进行翻译的代码段，点击左侧工具栏中的"Fitten Code — 开始新对话"。然后在输入框中输入需求即可完成转换


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image14.png)


### 6、生成注释


Fitten Code 能够根据您的代码自动生成相关注释，通过分析您的代码逻辑和结构，为您的代码提供清晰易懂的解释和文档，不仅提高代码的可读性，还方便其他开发人员理解和使用您的代码。先选中需要生成注释的代码段，然后右键选择 "Fitten Code — 生成注释"：


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image15.png)


也可以通过对话功能实现


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image16.png)


### 7、解释代码


Fitten Code 可以对一段代码进行解释，可以通过选中代码段然后右键选择 "Fitten Code — 解释代码" 进行解释，如下图所示：


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image17.png)


也可以通过对话功能实现


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image18.png)


### 8、生成测试


Fitten Code 拥有自动生成单元测试的功能，可以根据代码自动产生相应的测试用例，提高代码质量和可靠性。通过选中代码段后右键选择 "Fitten Code — 生成函数单元测试" 来实现，如下图所示：


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image19.png)


也可以通过对话功能实现


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image20.png)


### 9、检查 BUG


Fitten Code 可以对一段代码检查可能的 bug，并给出修复建议。选中对应代码段，然后右键选择 "Fitten Code — 查找选中代码中的 bug" ，如下图所示：


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image21.png)


或者在开始新对话窗口向 Fitten Code 提问代码 bug 查找后，Fitten Code 可以智能完成 debug 工作


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image22.png)


### 10、编辑代码


Fitten Code 可根据用户指示对选定的代码块进行编辑。选中代码段右键选择 "Fitten Code — 重构选中代码"，随后用户可在输入框中输入指示，如下图所示：


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image23.png)


也可以在开始新对话窗口向 Fitten Code 提供需要编辑的代码段，并输入需求，Fitten 可以完成代码编辑工作：


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image24.png)


### 11、图片问答


Fitten Code 的图片问答功能，为用户实现了可以在对话时使用图像问答的功能，用户可通过图像快速生成 HTML 代码、也可以通过图像查找 bug 等等。


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image25.png)


用户上传了一张包含红色波浪线的网页截图，并询问这条红色波浪线表示什么问题和解决方法。


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image26.png)


用户上传了一张贪吃蛇游戏的截图，并询问如何用代码实现该游戏设计。


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image27.png)


用户上传了一张描述登录页面设计的图像，并询问如何使用 HTML 复刻此网页。


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image28.png)


Fitten Code 分析图像并且根据分析结果，生成相应的 HTML 代码。


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image29.png)


用户上传了一张色调板的图像，并询问如何使用 HTML 制作类似色调的个人介绍页面。


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image30.png)


Fitten Code 生成的个人介绍网页效果，可以看到该网页色调与输入的图像色调一致。


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image31.png)


![](https://static.jyshare.com/images/re/fittencode/202509/csharp/image32.png)


更多内容参考官网：[https://code.fittentech.com/](https://code.fittentech.com/)


支持以下 4 种编辑器与开发环境：


- [VS Code](https://code.fittentech.com/desc-vscode)：本文会详细介绍
- [JetBrains IDE 系列（包括 PyCharm）](https://code.fittentech.com/tutor_jetbrains_zh#1)
- [Visual Studio](https://code.fittentech.com/tutor_vs_zh#1)：本文会详细介绍
- [Vim](https://code.fittentech.com/tutor_vim_zh#1)








	  AI 思考中...





			* [C# 变量作用域](https://www.runoob.com/csharp-variable-scope.html)
			[C# Null 条件运算符](https://www.runoob.com/csharp-null-condition.html) **













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