# ASP 表单和用户输入

- Source: https://www.runoob.com/asp/asp-inputforms.html

---


Request.QueryString 和 Request.Form 命令用于从表单取回信息，比如用户的输入。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[使用 method="get" 的表单](https://www.runoob.com/try/showasp.php?filename=demo_reqquery)** 本例演示如何使用 Request.QueryString 命令与用户进行交互。


[使用 method="post" 的表单](https://www.runoob.com/try/showasp.php?filename=demo_simpleform) 本例演示如何使用 Request.Form 命令与用户进行交互。


[使用单选按钮的表单](https://www.runoob.com/try/showasp.php?filename=demo_radiob) 本例演示如何使用 Request.Form 命令通过单选按钮与用户进行交互。


---


## 用户输入


Request 对象可用于从表单取回用户信息。


### HTML 表单实例


<form method="get" action="simpleform.asp">

First Name: <input type="text" name="fname"><br>

Last Name: <input type="text" name="lname"><br><br>

<input type="submit" value="Submit">

</form>


用户输入可通过 Request.QueryString 或 Request.Form 命令取回。


---


## Request.QueryString


Request.QueryString 命令用于收集使用 method="get" 的表单中的值。


使用 GET 方法从表单传送的信息对所有的用户都是可见的（出现在浏览器的地址栏），并且对所发送信息的量也有限制。


如果用户在上面的 HTML 表单中输入 "Bill" 和 "Gates"，发送至服务器的 URL 会类似这样：


http://www.w3cschool.cc/simpleform.asp?fname=Bill&lname=Gates


假设 "simpleform.asp" 文件包含下面的 ASP 脚本：


<body>

Welcome

<%

response.write(request.querystring("fname"))

response.write(" " & request.querystring("lname"))

%>

</body>


浏览器将把文档的 body 部分显示如下：


Welcome Bill Gates


---


## Request.Form


Request.Form 命令用于收集使用 method="post" 的表单中的值。


使用 POST 方法从表单传送的信息对用户是不可见的，并且对所发送信息的量没有限制。


如果用户在上面的 HTML 表单中输入 "Bill" 和 "Gates"，发送至服务器的 URL 会类似这样：


http://www.w3cschool.cc/simpleform.asp


假设 "simpleform.asp" 文件包含下面的 ASP 脚本：


<body>

Welcome

<%

response.write(request.form("fname"))

response.write(" " & request.form("lname"))

%>

</body>


浏览器将把文档的 body 部分显示如下：


Welcome Bill Gates


---


## 表单验证


只要有可能，就尽量在浏览器上对用户的输入进行验证（通过客户端脚本）。浏览器的验证速度更快，并可以减少服务器的负载。


如果用户输入会保存到数据库中，那么您应该考虑使用服务器端验证。有一种在服务器端验证表单的好方法，就是将（验证过的）表单传回表单页面，而不是转至不同的页面。用户随后就可以在同一个页面中得到错误的信息。这样做更易于用户发现错误。










	  AI 思考中...





			** [ASP 程序](https://www.runoob.com/asp-procedures.html)
			[ASP Cookies](https://www.runoob.com/asp-cookies.html) **













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