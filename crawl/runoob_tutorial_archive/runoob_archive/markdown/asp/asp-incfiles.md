# ASP 引用文件

- Source: https://www.runoob.com/asp/asp-incfiles.html

---


## #include 指令


通过使用 #include 指令，您可以在服务器执行 ASP 文件之前，把另一个 ASP 文件的内容插入到这个 ASP 文件中。


#include 指令用于创建函数、页眉、页脚或者其他多个页面上需要重复使用的元素等。


---


## 如何使用 #include 指令


这里有一个名为 "mypage.asp" 的文件：


	<!DOCTYPE html>**<html>

<body>

<h3>Words of Wisdom:</h3>

<p><!--#include file="wisdom.inc"--></p>

<h3>The time is:</h3>

<p><!--#include file="time.inc"--></p>

</body>

</html>


这是 "wisdom.inc" 文件：


"One should never increase, beyond what is necessary,

the number of entities required to explain anything."


这是 "time.inc" 文件：


<%

Response.Write(Time)

%>


如果您在浏览器中查看源代码，它将如下所示：


	<!DOCTYPE html>
<html>

<body>

<h3>Words of Wisdom:</h3>

<p>"One should never increase, beyond what is necessary,

the number of entities required to explain anything."</p>

<h3>The time is:</h3>

<p>11:33:42 AM</p>

</body>

</html>


---


## 引用文件的语法


如需在 ASP 页面中引用文件，请把 #include 指令放在注释标签中：


<!--#include virtual="somefilename"-->


or


<!--#include file ="somefilename"-->


### Virtual 关键词


请使用关键词 virtual 来指示以虚拟目录开始的路径。


如果一个名为 "header.inc" 的文件位于虚拟目录 /html 中，下面这行代码会插入 "header.inc" 文件中的内容：


<!-- #include virtual ="/html/header.inc" -->


### File 关键词


请使用关键词 file 来指示一个相对路径。相对路径是以含有引用文件的目录开始的。


如果您在 html 目录中有一个文件，且 "header.inc" 文件位于 html 头部，下面这行代码将在您的文件中插入 "header.inc" 文件中的内容：


<!-- #include file ="headersheader.inc" -->


请注意被引用文件 (headersheader.inc) 的路径是相对于引用文件的。如果包含 #include 声明的文件不在 html 目录中，这个声明就不会生效。


---


## 提示和注释


在上面的一部分中，我们已经使用 ".inc" 来作为被被引用文件的文件扩展名。请注意：如果用户尝试直接浏览 INC 文件，这个文件中内容将会被显示出来。如果您的被引用文件中的内容包含机密的信息或者是您不想让任何用户看到的信息，那么最好还是使用 ".asp" 作为扩展名。ASP 文件中的源代码被编译后是不可见的。被引用的文件也可引用其他文件，同时一个 ASP 文件可以对同一个文件引用多次。


重要事项：**在脚本执行前，被引用的文件就会被处理和插入。下面的脚本无法执行，这是由于 ASP 会在为变量赋值之前执行 #include 指令：


<%**
fname="header.inc"

%>

<!--#include file="<%fname%>"-->


您不能在脚本分隔符之间包含文件引用。下面的脚本无法执行：


<%

For i = 1 To n


  <!--#include file="count.inc"-->

Next

%>


但是这段脚本可以执行：


<% For i = 1 to n %>


<!--#include file="count.inc" -->

<% Next %>









	  AI 思考中...





			** [ASP Application 对象](https://www.runoob.com/asp-applications.html)
			[ASP Global.asa](https://www.runoob.com/asp-globalasa.html) **













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