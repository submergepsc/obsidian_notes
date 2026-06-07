# ASP.NET Web Forms - 维持 ViewState

- Source: https://www.runoob.com/aspnet/aspnet-viewstate.html

---


通过在您的 Web Form 中维持对象的 ViewState（视图状态），您可以省去大量的编码工作。


---


## 维持 ViewState（视图状态）


在经典 ASP 中，当一个表单被提交时，所有的表单值都会被清空。假设您提交了一个带有大量信息的表单，而服务器返回了一个错误。您不得不回到表单改正信息。您点击返回按钮，然后发生了什么......所有表单值都被清空了，您不得不重新开始所有的一切！站点没有维持您的 ViewState。


在 ASP .NET 中，当一个表单被提交时，表单会连同表单值一起出现在浏览器窗口中。如何做到的呢？这是因为 ASP .NET 维持了您的 ViewState。 ViewState 会在页面被提交到服务器时表明它的状态。这个状态是通过在带有  控件的每个页面上放置一个隐藏域定义的。源代码如下所示：


<form name="_ctl0" method="post" action="page.aspx" id="_ctl0">**
<input type="hidden" name="__VIEWSTATE"

value="dDwtNTI0ODU5MDE1Ozs+ZBCF2ryjMpeVgUrY2eTj79HNl4Q=" />


.....some code


</form>


维持 ViewState 是 ASP.NET Web Forms 的默认设置。如果您想不维持 ViewState，请在 .aspx 页面顶部包含指令  ，或者向任意控件添加属性 EnableViewState="false" 。


请看下面的 .aspx 文件。它演示了"老"的运行方式。当您点击提交按钮，表单值将会消失：


## 实例


```csharp
<html>
<body>
<form action="demo_classicasp.aspx" method="post">
Your name: <input type="text" name="fname" size="20">
<input type="submit" value="Submit">
</form>
<%
dim fname
fname=Request.Form("fname")
If fname<>"" Then
Response.Write("Hello " & fname & "!")
End If
%>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_classicasp)


下面是新的 ASP .NET 方式。当您点击提交按钮，表单值不会消失：


## 实例


点击实例的右边框架中的查看源代码，您将看到 ASP .NET 已经在表单中添加了一个隐藏域来维持 ViewState。


```csharp
<script runat="server">
Sub submit(sender As Object, e As EventArgs)
lbl1.Text="Hello " & txt1.Text & "!"
End Sub
</script>
<html>
<body>
<form runat="server">
Your name: <asp:TextBox id="txt1" runat="server" />
<asp:Button OnClick="submit" Text="Submit" runat="server" />
<p><asp:Label id="lbl1" runat="server" /></p>
</form>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_aspnetviewstate)








	  AI 思考中...





			** [ASP.NET Web 表单](https://www.runoob.com/aspnet-forms.html)
			[ASP.NET TextBox 控件](https://www.runoob.com/aspnet-textbox.html) **













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