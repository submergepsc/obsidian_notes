# ASP Global.asa 文件

- Source: https://www.runoob.com/asp/asp-globalasa.html

---


## Global.asa 文件


Global.asa 文件是一个可选的文件，它可包含被 ASP 应用程序中每个页面访问的对象、变量和方法的声明。


所有合法的浏览器脚本（JavaScript、VBScript、JScript、PerlScript 等等）都能在 Global.asa 中使用。


Global.asa 文件只能包含下列内容：


- Application 事件
- Session 事件
-  声明
- TypeLibrary 声明
- #include 指令


**注释：**Global.asa 文件必须存放在 ASP 应用程序的根目录中，而且每个应用程序只能有一个 Global.asa 文件。


---


## Global.asa 中的事件


在 Global.asa 中，您可以告诉 application 和 session 对象当 application/session 开始时做什么，当 application/session 结束时做什么。完成这项任务的代码被放置在事件句柄中。Global.asa 文件能包含四种类型的事件：

**Application_OnStart** - 此事件会在第一个用户调用 ASP 应用程序的第一个页面时发生。此事件会在 Web 服务器重启或者 Global.asa 文件被编辑之后发生。"Session_OnStart" 事件会在此事件发生之后立即发生。

**Session_OnStart** - 此事件会在每当新用户请求他（她）在 ASP 应用程序中的第一个页面时发生。


**Session_OnEnd** - 此事件会在每当用户结束 session 时发生。在规定的时间（默认的时间为 20 分钟）内如果用户没有请求任何页面，用户 session 就会结束。


**Application_OnEnd** - 此事件会在最后一个用户结束其 session 之后发生。典型的情况是，此事件会在 Web 服务器停止时发生。这个子程序用于在应用程序停止后清除设置，比如删除记录或者向文本文件中写入信息。


一个 Global.asa 文件可能如下所示：


<script language="vbscript" runat="server">**

sub Application_OnStart

  '*some code*

end sub


sub Application_OnEnd

  '*some code*

end sub


sub Session_OnStart

  '*some code*

end sub


sub Session_OnEnd

  '*some code*

end sub


</script>


注释：**由于我们无法在 Global.asa 文件中使用 ASP 的脚本分隔符 () 插入脚本，我们需要把子例程放置在 HTML 的  元素内部。


---


## 声明


可通过使用  标签在 Global.asa 文件中创建带有 session 或者 application 作用域的对象。


**注释：** 标签应位于  标签外部！


### 语法


<object runat="server" scope="*scope*" id="*id*"
{progid="*progID*"|classid="*classID*"}>**
....

</object>


| 参数 | 描述 |
| --- | --- |
| scope | 设置对象（Session 或 Application）的作用域。 |
| id | 为对象指定一个唯一的 id。 |
| ProgID | 与 ClassID 关联的 id。ProgID 的格式是：[Vendor.]Component[.Version]。 ProgID 或 ClassID 必需被指定。 |
| ClassID | 为 COM 类对象指定一个唯一的 id。ProgID 或 ClassID 必需被指定。 |


### 实例


第一个实例通过使用 ProgID 参数创建了一个名为 "MyAd" 的 session 作用域对象：


<object runat="server" scope="session" id="MyAd"
progid="MSWC.AdRotator">

</object>


第二个实例通过使用 ClassID 参数创建了一个名为 "MyConnection" 的 application 作用域对象：


<object runat="server" scope="application" id="MyConnection"

classid="Clsid:8AD3067A-B3FC-11CF-A560-00A0C9081C21">

</object>


在 Global.asa 文件中声明的对象可被应用程序中的任何脚本使用：


GLOBAL.ASA:


<object runat="server" scope="session" id="MyAd"
progid="MSWC.AdRotator">

</object>


您可以从 ASP 应用程序中的任意页面引用 "MyAd" 对象：


某个 .ASP 文件：


<%=MyAd.GetAdvertisement("/banners/adrot.txt")%>


---


## TypeLibrary 声明


TypeLibrary（类型库）是一个容器，其中装有对应于 COM 对象的 DLL 文件。通过在 Global.asa 文件中包含对 TypeLibrary 的调用，可以访问 COM 对象的常量，同时 ASP 代码也能更好地报告错误。如果您的 Web 应用程序依赖于已在类型库中声明的数据类型的 COM 对象，您可以在 Global.asa 中对类型库进行声明。


### 语法


<!--METADATA TYPE="TypeLib"

file="*filename*"
uuid="*id*"
version="*number*"
lcid="*localeid*"

-->


| 参数 | 描述 |
| --- | --- |
| file | 规定指向类型库的绝对路径。 file 参数或者 uuid 参数，两者缺一不可。 |
| uuid | 规定了类型库的唯一的标识符。 file 参数或者 uuid 参数，两者缺一不可。 |
| version | 可选。用于选择版本。如果没有找到需要的版本，将使用最接近的版本。 |
| lcid | 可选。用于类型库的地区标识符。 |


### 错误值


服务器会返回以下的错误消息之一：


| 错误代码 | 描述 |
| --- | --- |
| ASP 0222 | 无效的类型库规范 |
| ASP 0223 | 没有找到类型库 |
| ASP 0224 | 无法加载类型库 |
| ASP 0225 | 无法包装类型库 |


注释：**METADATA 标签可出现在 Global.asa 文件中的任何位置（在  标签的内外皆可）。然而，我们还是推荐将 METADATA 标签放置于 Global.asa 文件的顶部。


---


## 限定


关于可以在 Global.asa 文件中引用的内容的限定：


- 您无法显示 Global.asa 文件中的文本。此文件无法显示信息。
- 您只能在 Application_OnStart 和 Application_OnEnd 子例程中使用 Server 和 Application 对象。在 Session_OnEnd 子例程中，您可以使用 Server、Application 和 Session 对象。在 Session_OnStart 子例程中，您可以使用任何内建的对象。


---


## 如何使用子例程


Global.asa 常用于初始化变量。


下面的实例演示了如何检测访客首次到达 Web 站点的确切时间。时间存储在名为 "started" 的 Session 对象中，并且 "started" 变量的值可被应用程序中的任何 ASP 页面访问：


<script language="vbscript" runat="server">**
sub Session_OnStart

Session("started")=now()

end sub

</script>


Global.asa 也可用于控制页面访问。


下面的实例演示了如何把每个新的访客重定向到另一个页面，在这个例子中会定向到一个名为 "newpage.asp" 的页面：


<script language="vbscript" runat="server">

sub Session_OnStart

Response.Redirect("newpage.asp")

end sub

</script>


您可以在 Global.asa 文件中包含函数。


在下面的实例中，当 Web 服务器启动时，Application_OnStart 子例程也会启动。然后，Application_OnStart 子例程会调用另一个名为 "getcustomers" 的子例程。"getcustomers" 子例程会打开一个数据库，然后从 "customers" 表中取回一个记录集。此记录集会赋值给一个数组，在不查询数据库的情况下，任何 ASP 页面都能够访问这个数组：


<script language="vbscript" runat="server">


sub Application_OnStart

getcustomers

end sub


sub getcustomers

set conn=Server.CreateObject("ADODB.Connection")

conn.Provider="Microsoft.Jet.OLEDB.4.0"

conn.Open "c:/webdata/northwind.mdb"

set rs=conn.execute("select name from customers")

Application("customers")=rs.GetRows

rs.Close

conn.Close

end sub


</script>


---


## Global.asa 实例


在这个实例中，我们将创建一个计算当前访客数量的 Global.asa 文件。


- 当服务器启动时，Application_OnStart 设置 Application 变量 "visitors" 的值为 0。
- 每当有新的访客来访时，Session_OnStart 子例程就会给变量 "visitors" 加 1。
- 每当 Session_OnEnd 子例程被触发时，该子例程就会从变量 "visitors" 减 1。


Global.asa 文件：


<script language="vbscript" runat="server">


Sub Application_OnStart

Application("visitors")=0

End Sub


Sub Session_OnStart

Application.Lock

Application("visitors")=Application("visitors")+1

Application.UnLock

End Sub


Sub Session_OnEnd

Application.Lock

Application("visitors")=Application("visitors")-1

Application.UnLock

End Sub


</script>


在 ASP 文件中，显示当前访客的数量：


	<!DOCTYPE html>
<html>

<head>

</head>

<body>

<p>There are <%response.write(Application("visitors"))%>
online now!</p>

</body>

</html>









	  AI 思考中...





			** [ASP 引用文件](https://www.runoob.com/asp-incfiles.html)
			[ASP 使用 CDOSYS 发送电子邮件](https://www.runoob.com/asp-send-email.html) **













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