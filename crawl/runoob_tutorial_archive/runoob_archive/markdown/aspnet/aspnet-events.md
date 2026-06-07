# ASP.NET Web Forms - 事件

- Source: https://www.runoob.com/aspnet/aspnet-events.html

---


事件句柄是一种针对给定事件来执行代码的子例程。


---


## ASP.NET - 事件句柄


请看下面的代码：


<%**
lbl1.Text="The date and time is " & now()

%>


<html>

<body>

<form runat="server">

<h3><asp:label id="lbl1" runat="server" /></h3>

</form>

</body>

</html>


上面的代码将在何时被执行？答案是："不知道..."。


---


## Page_Load 事件


Page_Load 事件是 ASP.NET 可理解的众多事件之一。Page_Load 事件会在页面加载时被触发， ASP.NET 将自动调用 Page_Load 子例程，并执行其中的代码：


## 实例


```csharp
<script runat="server">
Sub Page_Load
lbl1.Text="The date and time is " & now()
End Sub
</script>
<html>
<body>
<form runat="server">
<h3><asp:label id="lbl1" runat="server" /></h3>
</form>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_pageload)


注释：**Page_Load 事件不包含对象引用或事件参数！


---


## Page.IsPostBack 属性


Page_Load 子例程会在页面每次加载时运行。如果您只想在页面第一次加载时执行 Page_Load 子例程中的代码，那么您可以使用 Page.IsPostBack 属性。如果 Page.IsPostBack 属性设置为 false，则页面第一次被载入，如果设置为 true，则页面被传回到服务器（比如，通过点击表单上的按钮）：


## 实例


```csharp
<script runat="server">
Sub Page_Load
if Not Page.IsPostBack then
  lbl1.Text="The date and time is " & now()
end if
End Sub
Sub submit(s As Object, e As EventArgs)
lbl2.Text="Hello World!"
End Sub
</script>
<html>
<body>
<form runat="server">
<h3><asp:label id="lbl1" runat="server" /></h3>
<h3><asp:label id="lbl2" runat="server" /></h3>
<asp:button text="Submit" onclick="submit" runat="server" />
</form>
</body>
</html>
```


**[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_pageispostback)


上面的实例仅在页面第一次加载时显示 "The date and time is...." 消息。当用户点击 Submit 按钮是，submit 子例程将会在第二个 label 中写入 "Hello World!"，但是第一个 label 中的日期和时间不会改变。










	  AI 思考中...





			** [ASP.NET 服务器控件](https://www.runoob.com/aspnet-controls.html)
			[ASP.NET Web 表单](https://www.runoob.com/aspnet-forms.html) **













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