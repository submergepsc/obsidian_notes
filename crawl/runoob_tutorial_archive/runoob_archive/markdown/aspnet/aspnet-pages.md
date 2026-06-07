# ASP.NET Web Forms - HTML 页面

- Source: https://www.runoob.com/aspnet/aspnet-pages.html

---


简单的 ASP.NET 页面看上去就像普通的 HTML 页面。


---


## Hello RUNOOB.COM


在开始学习 ASP.NET 之前，我们先来构建一个简单的 HTML 页面，该页面将在浏览器中显示 "Hello RUNOOB.COM"：


| ## Hello RUNOOB.COM! |
| --- |

**
---


## 用 HTML 编写的 Hello RUNOOB.COM


下面的代码将以 HTML 页面的形式显示实例：


<html>

<body bgcolor="yellow">

<center>

<h2>Hello RUNOOB.COM!</h2>

</center>

</body>

</html>


如果您想亲自尝试一下，请保存上面的代码到一个名为 "firstpage.htm**" 的文件中，并创建一个到该文件的链接：firstpage.htm。


---


## 用 ASP.NET 编写的 Hello RUNOOB.COM


转换 HTML 页面为 ASP.NET 页面最简单的方法是，直接复制一个 HTML 文件，并把新文件的扩展名改成 **.aspx** 。


下面的代码将以 ASP.NET 页面的形式显示实例：


<html>**
<body bgcolor="yellow">

<center>

<h2>Hello RUNOOB.COM!</h2>

</center>

</body>

</html>


如果您想亲自尝试一下，请保存上面的代码到一个名为 "firstpage.aspx**" 的文件中，并创建一个到该文件的链接：firstpage.aspx。


---


## 它是如何工作的？


从根本上讲，ASP.NET 页面与 HTML 是完全相同的。


HTML 页面的扩展名是 .htm。如果浏览器向服务器请求一个 HTML 页面，服务器可以不进行任何修改，就直接发送页面给浏览器。


ASP.NET 页面的扩展名是 .aspx。如果浏览器向服务器请求个 ASP.NET 页面，服务器在将结果发回给浏览器之前，需要先处理页面中的可执行代码。


上面的 ASP.NET 页面不包含任何可执行的代码，所以没有执行任何东西。在下面的实例中，我们将添加一些可执行的代码到页面中，以便演示静态 HTML 页面和动态 ASP 页面的不同之处。


---


## 经典 ASP


Active Server Pages (ASP) 已经流行很多年了。通过 ASP，可以在 HTML 页面中放置可执行代码。


之前的 ASP 版本（在 ASP.NET 之前）通常被称为经典 ASP。


ASP.NET 不完全兼容经典 ASP，但是只需要经过少量的修改，大部分经典 ASP 页面就可以作为 ASP.NET 页面良好地运行。


如果您想学习更多关于经典 ASP 的知识，请访问我们的 [ASP 教程](https://www.runoob.com/../asp/asp-tutorial.html)。


---


## 用经典 ASP 编写的动态页面


为了演示 ASP 是如何显示包含动态内容的页面，我们将向上面的实例中添加一些可执行的代码（红色字体标识）：


<html>**
<body bgcolor="yellow">

<center>

<h2>Hello RUNOOB.COM!</h2>

<p>**<%Response.Write(now())%>**</p>

</center>

</body>

</html>


 标签内的代码是在服务器上执行的。


Response.Write 是用来向 HTML 输出流中写东西的 ASP 代码。


Now() 是一个返回服务器当前日期和时间的函数。


如果您想亲自尝试一下，请保存上面的代码到一个名为 "dynpage.asp**" 的文件中，并创建一个到该文件的链接：dynpage.asp。


---


## 用 ASP .NET 编写的动态页面


下面的代码将以 ASP.NET 页面的形式显示实例：


<html>**
<body bgcolor="yellow">

<center>

<h2>Hello RUNOOB.COM!</h2>

<p>**<%Response.Write(now())%>**</p>

</center>

</body>

</html>


如果您想亲自尝试一下，请保存上面的代码到一个名为 "dynpage.aspx**" 的文件中，并创建一个到该文件的链接：dynpage.aspx。


---


## ASP.NET 对比经典 ASP


上面的实例无法演示 ASP.NET 与经典 ASP 之间任何的不同之处。


正如最后的两个实例中，您看不出 ASP 页面和 ASP.NET 页面两者之间的不同之处。


在下一章中，您将看到服务器控件是如何让 ASP.NET 比经典 ASP 更强大的。

**







	  AI 思考中...





			** [ASP.NET Web Forms 教程](https://www.runoob.com/aspnet-intro.html)
			[ASP.NET 服务器控件](https://www.runoob.com/aspnet-controls.html) **













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