# ASP.NET Web Forms - 服务器控件

- Source: https://www.runoob.com/aspnet/aspnet-controls.html

---


服务器控件是服务器可理解的标签。


---


## 经典 ASP 的局限性


下面列出的代码是从上一章中复制的：


<html>**
<body bgcolor="yellow">

<center>

<h2>Hello Runoob!</h2>

<p>**<%Response.Write(now())%>**</p>

</center>

</body>

</html>


上面的代码反映出经典 ASP 的局限性：代码块必须放置在您想要输出显示的位置。


通过经典 ASP，想要把可执行代码从 HTML 页面中分离出来是不可能的。这让页面变得难以阅读，也难以维护。


---


## ASP.NET - 服务器控件


ASP.NET 通过服务器控件，已经解决了上述的"意大利面条式代码"问题。


服务器控件是服务器可理解的标签。


有三种类型的服务器控件：


- HTML 服务器控件 - 创建的 HTML 标签
- Web 服务器控件 - 新的 ASP.NET 标签
- Validation 服务器控件 - 用于输入验证


---


## ASP.NET - HTML 服务器控件


HTML 服务器控件是服务器可理解的 HTML 标签。


ASP.NET 文件中的 HTML 元素，默认是作为文本进行处理的。要想让这些元素可编程，需向 HTML 元素中添加 runat="server" 属性。这个属性表示，该元素将被作为服务器控件进行处理。同时需要添加 id 属性来标识服务器控件。id 引用可用于操作运行时的服务器控件。


注释：**所有 HTML 服务器控件必须位于带有 runat="server" 属性的  标签内。runat="server" 属性表明了该表单必须在服务器上进行处理。同时也表明了包含在它内部的控件可被服务器脚本访问。


在下面的实例中，我们在 .aspx 文件中声明了一个 HtmlAnchor 服务器控件。然后我们在一个事件句柄（事件句柄是一种针对给定事件执行代码的子例程）中操作 HtmlAnchor 控件的 HRef 属性。Page_Load 事件是 ASP.NET 可理解的多种事件中的一种：


<script runat="server">**
Sub Page_Load

link1.HRef="http://www.runoob.com"

End Sub

</script>


<html>

<body>


<form runat="server">

<a id="link1" runat="server">Visit RUNOOB!</a>

</form>


</body>

</html>


可执行代码本身已经被移到 HTML 之外了。


---


## ASP.NET - Web 服务器控件


Web 服务器控件是服务器可理解的特殊 ASP.NET 标签。


就像 HTML 服务器控件，Web 服务器控件也是在服务器上创建的，它们同样需要 runat="server" 属性才能生效。然而，Web 服务器控件没有必要映射任何已存在的 HTML 元素，它们可以表示更复杂的元素。


创建 Web 服务器控件的语法是：


<asp:control_name id="some_id" runat="server" />


在下面的实例中，我们在 .aspx 文件中声明了一个 Button 服务器控件。然后我们为 Click 事件创建一个事件句柄，用来改变按钮上的文本：


<script runat="server">

Sub submit(Source As Object, e As EventArgs)

button1.Text="You clicked me!"

End Sub

</script>


<html>

<body>


<form runat="server">

<asp:Button id="button1" Text="Click me!"

runat="server" OnClick="submit"/>

</form>


</body>

</html>


---


## ASP.NET - Validation 服务器控件


Validation 服务器控件是用来验证用户输入的。如果用户输入没有通过验证，将显示一条错误消息给用户。


每种 validation 控件执行一种指定类型的验证（比如验证某个指定的值或者某个范围的值）。


在默认情况下，当 Button、ImageButton、LinkButton 控件被点击时，会执行页面验证。您可以设置 CausesValidation 为 false ，来阻止按钮控件被点击时进行验证。


创建 Validation 服务器控件的语法是：


<asp:control_name id="some_id" runat="server" />


在下面的实例中，我们在 .aspx 文件中声明了一个 TextBox 控件、一个 Button 控件、一个 RangeValidator 控件。如果验证失败，文本 "The value must be from 1 to 100!" 将会显示在 RangeValidator 控件中：


## 实例


```csharp
<html>
<body>
<form runat="server">
<p>Enter a number from 1 to 100:
<asp:TextBox id="tbox1" runat="server" />
<br /><br />
<asp:Button Text="Submit" runat="server" />
</p>
<p>
<asp:RangeValidator
ControlToValidate="tbox1"
MinimumValue="1"
MaximumValue="100"
Type="Integer"
Text="The value must be from 1 to 100!"
runat="server" />
</p>
</form>
</body>
</html>
```










	  AI 思考中...





			** [ASP.NET Web 页面](https://www.runoob.com/aspnet-pages.html)
			[ASP.NET 事件句柄](https://www.runoob.com/aspnet-events.html) **













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