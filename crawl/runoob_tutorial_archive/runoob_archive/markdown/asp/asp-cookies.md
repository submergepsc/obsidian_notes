# ASP Cookies

- Source: https://www.runoob.com/asp/asp-cookies.html

---


cookie 常用于识别用户。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[Welcome cookie](https://www.runoob.com/try/showasp.php?filename=demo_cookies)** 本例演示如何创建 Welcome cookie。


---


## Cookie 是什么？


cookie 常用用于识别用户。cookie 是一种服务器留在用户计算机上的小文件。每当同一台计算机通过浏览器请求页面时，这台计算机将会发送 cookie。通过 ASP，您能够创建并取回 cookie 的值。


---


## 如何创建 Cookie？


"Response.Cookies" 命令用于创建 cookie。


注释：**Response.Cookies 命令必须出现在  标签之前。


在下面的实例中，我们将创建一个名为 "firstname" 的 cookie，并将其赋值为 "Alex"：


<%**
Response.Cookies("firstname")="Alex"

%>


向 cookie 分配属性也是可以的，比如设置 cookie 的失效时间：


<%

Response.Cookies("firstname")="Alex"

Response.Cookies("firstname").Expires=#May 10,2012#

%>


---


## 如何取回 Cookie 的值？


"Request.Cookies" 命令用于取回 cookie 的值。


在下面的实例中，我们取回了名为 "firstname" 的 cookie 的值，并把值显示到了页面上：


<%

fname=Request.Cookies("firstname")

response.write("Firstname=" & fname)

%>


输出：** Firstname=Alex


---


## 带有键的 Cookie


如果一个 cookie 包含多个值的集合，我们就可以说 cookie 带有键（Keys）。


在下面的实例中，我们将创建一个名为 "user" 的 cookie 集合。"user" cookie 带有包含用户信息的键：


<%**
Response.Cookies("user")("firstname")="John"

Response.Cookies("user")("lastname")="Smith"

Response.Cookies("user")("country")="Norway"

Response.Cookies("user")("age")="25"

%>


---


## 读取所有的 Cookie


请阅读下面的代码：


<%

Response.Cookies("firstname")="Alex"

Response.Cookies("user")("firstname")="John"

Response.Cookies("user")("lastname")="Smith"

Response.Cookies("user")("country")="Norway"

Response.Cookies("user")("age")="25"

%>


假设您的服务器将上面所有的 cookie 传给了某个用户。


现在，我们需要读取这些传给某个用户的所有的 cookie。下面的实例向您演示了如何做到这一点（请注意，下面的代码通过 HasKeys 属性检查 cookie 是否带有键）：


	<!DOCTYPE html>
<html>

<body>


<%

dim x,y

for each x in Request.Cookies


  response.write("<p>")


  if Request.Cookies(x).HasKeys then


    for each y in Request.Cookies(x)


      response.write(x & ":" & y & "=" & Request.Cookies(x)(y))


      response.write("<br>")


    next


  else


    Response.Write(x & "=" & Request.Cookies(x) & "<br>")


  end if


  response.write "</p>"

next

%>


</body>

</html>


输出：**


firstname=Alex


user:firstname=John** user:lastname=Smith user:country=Norway user:age=25


---


## 如果浏览器不支持 Cookie 该怎么办？


如果您的应用程序需要与不支持 cookie 的浏览器打交道，那么您不得不使用其他的办法在您的应用程序中的页面之间传递信息。这里有两种办法：


### 1. 向 URL 添加参数


您可以向 URL 添加参数：


<a href="welcome.asp?fname=John&lname=Smith">Go to Welcome Page</a>


然后在 "welcome.asp" 文件中取回这些值，如下所示：


<%

fname=Request.querystring("fname")

lname=Request.querystring("lname")

response.write("<p>Hello " & fname & " " & lname & "!</p>")

response.write("<p>Welcome to my Web site!</p>")

%>


### 2. 使用表单


您可以使用表单。当用户点击 Submit 按钮时，表单会把用户输入传给 "welcome.asp" ：


<form method="post" action="welcome.asp">

First Name:  <input type="text" name="fname" value="">

Last Name: <input type="text" name="lname" value="">

<input type="submit" value="Submit">

</form>


然后在 "welcome.asp" 文件中取回这些值，如下所示：


<%

fname=Request.form("fname")

lname=Request.form("lname")

response.write("<p>Hello " & fname & " " & lname & "!</p>")

response.write("<p>Welcome to my Web site!</p>")

%>









	  AI 思考中...





			** [ASP 表单](https://www.runoob.com/asp-inputforms.html)
			[ASP Session 对象](https://www.runoob.com/asp-sessions.html) **













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