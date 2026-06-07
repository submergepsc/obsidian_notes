# ASP Cookies 集合

- Source: https://www.runoob.com/asp/coll-cookies-response.html

---

[![Response 对象参考手册](https://www.runoob.com/images/up.gif) 完整的 Response 对象参考手册](https://www.runoob.com/asp-ref-response.html)

---


Cookies 集合用于设置或取得 cookie 的值。如果 cookie 不存在，就创建它，并赋予它规定的值。


**注意：**Response.Cookies 命令必须位于  标签之前。


## 语法


Response.Cookies(name)[(key)|.attribute]=value**

variablename=Request.Cookies(name)[(key)|.attribute]


| 参数 | 描述 |
| --- | --- |
| name | 必需。cookie 的名称。 |
| value | 必需（对于 Response.Cookies 命令）。cookie 的值。 |
| attribute | 可选。规定有关 cookie 的信息。可以是下面的参数之一： Domain - 只写。cookie 仅送往到达该域的请求。 Expires - 只写。cookie 的失效日期。如果没有规定日期，cookie 会在 session 结束时失效。 HasKeys - 只读。规定 cookie 是否拥有 key（这是唯一一个可与 Request.Cookies 命令使用的属性）。 Path - 只写。如果设置，cookie 仅送往到达此路径的请求。如果没有设置，则使用应用程序的路径。 Secure - 只写。指示 cookie 是否安全。 |
| key | 可选。规定在何处赋值的 key。 |


---


## 实例


"Response.Cookies" 命令用于创建 cookie 或者设置 cookie 的值：


<%

Response.Cookies("firstname")="Alex"

%>


在上面的代码中，我们创建了一个名为 "firstname" 的 cookie，并为它赋值 "Alex"。


也可以为 cookie 设置属性，比如设置 cookie 的失效时间：


<%

Response.Cookies("firstname")="Alex"

Response.Cookies("firstname").Expires=#May 10,2002#

%>


现在，名为 "firstname" 的 cookie 的值是 "Alex"，同时它在用户电脑中的失效日期是 2002 年 5 月 10 日。


"Request.Cookies" 命令用于取回 cookie 的值。


在下面的实例中，我们取回了 cookie "firstname" 的值，并把它显示到页面上：


<%

fname=Request.Cookies("firstname")

response.write("Firstname=" & fname)

%>


输出：


Firstname=Alex


一个 cookie 可以包含一个多值的集合。我们称之为 cookie 拥有 key 。


在下面的实例中，我们要创建一个名为 "user" 的 cookie 集合。"user" cookie 拥有包含有关用户信息的 key ：


<%

Response.Cookies("user")("firstname")="John"

Response.Cookies("user")("lastname")="Smith"

Response.Cookies("user")("country")="Norway"

Response.Cookies("user")("age")="25"

%>


下面的代码可读出所有服务器已向用户发送的 cookie 。请注意，我们使用了 HasKeys 属性来判断 cookie 是否拥有 key ：


<html>

<body>


<%

dim x,y


for each x in Request.Cookies

  response.write("<p>")

  if Request.Cookies(x).HasKeys then

    for each y in Request.Cookies(x)

      response.write(x & ":" & y & "=" & Request.Cookies(x)(y))

      response.write("<br /")

    next

  else

    Response.Write(x & "=" & Request.Cookies(x) & "<br>")

  end if

  response.write "</p>"

next

%>


</body>

</html>

%>


输出：


firstname=Alex

user:firstname=John user:lastname=Smith user: country=Norway user: age=25


---

[![Response 对象参考手册](https://www.runoob.com/images/up.gif) 完整的 Response 对象参考手册](https://www.runoob.com/asp-ref-response.html)







	  AI 思考中...





			** [ASP 实例](https://www.runoob.com/asp-examples.html)
			[ASP Buffer 属性](https://www.runoob.com/prop-buffer.html) **













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