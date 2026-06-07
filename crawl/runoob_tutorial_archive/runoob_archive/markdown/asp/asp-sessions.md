# ASP Session 对象

- Source: https://www.runoob.com/asp/asp-sessions.html

---


Session 对象用于存储关于用户会话（session）的信息，或者更改用户会话（session）的设置。


---


## Session 对象


当您在计算机上操作某个应用程序时，您打开它，做些更改，然后关闭它。这很像一次对话（Session）。计算机知道您是谁。它清楚您在何时打开和关闭应用程序。然而，在因特网上问题出现了：由于 HTTP 地址无法保持状态，Web 服务器并不知道您是谁以及您做了什么。


ASP 通过为每个用户创建一个唯一的 cookie 来解决这个问题。cookie 被传送至用户的计算机上，它含有可识别用户的信息。这种接口被称作 Session 对象。


Session 对象用于存储关于用户会话（session）的信息，或者更改用户会话（session）的设置。


存储于 Session 对象中的变量存储单一用户的信息，并且对于应用程序中的所有页面都是可用的。存储于 session 变量中的公共信息通常是 name、id 和参数。服务器会为每个新的用户创建一个新的 Session，并在 session 失效时撤销掉这个 Session 对象。


---


## Session 何时开始？


Session 开始于：


- 某个新用户请求了一个 ASP 文件，并且 Global.asa 文件引用了 Session_OnStart 子程序
- 某个值存储在 Session 变量中
- 某个用户请求了一个 ASP 文件，并且 Global.asa 使用  标签通过 session 的 scope 来实例化某个对象


---


## Session 何时结束？


如果用户没有在规定的时间内在应用程序中请求或者刷新页面，session 就会结束。默认值为 20 分钟。


如果您想要将超时的时间间隔设置为比默认值更短或更长，可以使用 **Timeout** 属性。


下面的实例设置了一个 5 分钟的超时时间间隔：


<%**
Session.Timeout=5

%>


要立即结束 session，请使用 Abandon** 方法：


<%**
Session.Abandon

%>


注释：**使用 session 时主要的问题是它们该在何时结束。我们不会知道用户最近的请求是否是最后的请求。因此我们不清楚该让 session "存活"多久。为某个空闲的 session 等待太久会耗尽服务器的资源。然而如果 session 被过早地删除，用户就不得不一遍又一遍地重新开始，这是因为服务器已经删除了所有的信息。寻找合适的超时间隔时间是很困难的！


![Tip](https://www.runoob.com/images/lamp.gif)**提示：**在 session 变量中仅存储少量的数据！


---


## 存储和取回 Session 变量


Session 对象最大的优点是可在其中存储变量，以供后续的网页读取，其应用范围是很广的。


下面的实例把 "Donald Duck" 赋值给名为 *username* 的 Session 变量，并把 "50" 赋值给名为 *age* 的 Session 变量：


<%**
Session("username")="Donald Duck"

Session("age")=50

%>


当值被存储在 session 变量中，它就能被 ASP 应用程序中的任何页面使用：


Welcome <%Response.Write(Session("username"))%>


上面这行代码返回的结果是: "Welcome Donald Duck"。


您也可以在 Session 对象中存储用户参数，然后通过访问这些参数来决定向用户返回什么页面。


下面的实例规定，假如用户使用低显示器分辨率，则返回纯文本版本的页面：


<%If Session("screenres")="low" Then%>


  This is the text version of the page

<%Else%>


  This is the multimedia version of the page

<%End If%>


---


## 移除 Session 变量


Contents 集合包含所有的 session 变量。


可通过 Remove 方法来移除 session 变量。


在下面的实例中，如果 session 变量 "age" 的值小于 18，则移除 session 变量 "sale"：


<%

If Session.Contents("age")<18 then


  Session.Contents.Remove("sale")

End If

%>


如需移除 session 中的所有变量，请使用 RemoveAll 方法：


<%

Session.Contents.RemoveAll()

%>


---


## 遍历 Contents 集合


Contents 集合包含所有的 session 变量。您可以通过遍历 Contents 集合，来查看其中存储的变量：


<%

Session("username")="Donald Duck"

Session("age")=50


dim i

For Each i in Session.Contents


  Response.Write(i & "<br>")

Next

%>


结果：


username

age


如果您不知道 Contents 集合中的项目数量，您可以使用 Count 属性：


<%

dim i

dim j

j=Session.Contents.Count

Response.Write("Session variables: " & j)

For i=1 to j


  Response.Write(Session.Contents(i) & "<br>")

Next

%>


结果：


Session variables: 2

Donald Duck

50


---


## 遍历 StaticObjects 集合


您可以通过遍历 StaticObjects 集合，来查看存储在 Session 对象中的所有对象的值：


<%

dim i

For Each i in Session.StaticObjects


  Response.Write(i & "<br>")

Next

%>









	  AI 思考中...





			** [ASP Cookies](https://www.runoob.com/asp-cookies.html)
			[ASP Application 对象](https://www.runoob.com/asp-applications.html) **













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