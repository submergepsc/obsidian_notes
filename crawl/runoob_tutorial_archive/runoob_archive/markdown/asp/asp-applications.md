# ASP Application 对象

- Source: https://www.runoob.com/asp/asp-applications.html

---


在一起协同工作以完成某项任务的一组 ASP 文件称为一个应用程序。


---


## Application 对象


Web 上的一个应用程序可以是一组 ASP 文件。这些 ASP 文件一起协同工作来完成某项任务。ASP 中的 Application 对象用于把这些文件捆绑在一起。


Application 对象用于存储和访问来自任何页面的变量，类似于 Session 对象。不同之处在于，所有的用户分享一个 Application 对象，而 Session 对象和用户的关系是一一对应的。


Application 对象存有会被应用程序中的许多页面使用的信息（比如数据库连接信息）。可以从任何的页面访问这些信息。同时您也可以在一个地方改变这些信息，随后这些改变会自动反映在所有的页面上。


---


## 存储和取回 Application 变量


Application 变量可被应用程序中的任何页面访问和改变。


您可以在 "Global.asa" 中创建 Application 变量，如下所示：


<script language="vbscript" runat="server">**

Sub Application_OnStart

application("vartime")=""

application("users")=1

End Sub


</script>


在上面的实例中，我们创建了两个 Application 变量："vartime" 和 "users"。


您可以访问 Application 变量的值，如下所示：


There are

<%

Response.Write(Application("users"))

%>

active connections.


---


## 遍历 Contents 集合


Contents 集合包含着所有的 application 变量。您可以通过遍历 Contents 集合，来查看其中存储的变量：


<%

dim i

For Each i in Application.Contents


  Response.Write(i & "<br>")

Next

%>


如果您不知道 Contents 集合中的项目数量，您可以使用 Count 属性：


<%

dim i

dim j

j=Application.Contents.Count

For i=1 to j


  Response.Write(Application.Contents(i) & "<br>")

Next

%>


---


## 遍历 StaticObjects 集合


您可以通过遍历 StaticObjects 集合，来查看存储在 Application 对象中的所有对象的值：


<%

dim i

For Each i in Application.StaticObjects


  Response.Write(i & "<br>")

Next

%>


---


## 锁定和解锁


您可以使用 "Lock" 方法来锁定应用程序。当应用程序锁定后，用户们就无法改变 Application 变量了（除了正在访问 Application 变量的用户）。您还可以使用 "Unlock" 方法来解锁应用程序。这个方法会移除对 Application 变量的锁定：


<%

Application.Lock

  'do some application object operations

Application.Unlock

%>









	  AI 思考中...





			** [ASP Session 对象](https://www.runoob.com/asp-sessions.html)
			[ASP 引用文件](https://www.runoob.com/asp-incfiles.html) **













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