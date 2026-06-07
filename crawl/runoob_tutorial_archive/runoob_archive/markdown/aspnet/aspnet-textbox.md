# ASP.NET Web Forms - TextBox 控件

- Source: https://www.runoob.com/aspnet/aspnet-textbox.html

---


TextBox 控件用于创建用户可输入文本的文本框。


---


## TextBox 控件


TextBox 控件用于创建用户可输入文本的文本框。


TextBox 控件的特性和属性列在我们的 [WebForms 控件参考手册页面](https://www.runoob.com/aspnet-ref-webcontrols.html)。


下面的实例演示了您可能会用到的 TextBox 控件的一些属性：


## 实例


```csharp
<html>
<body>
<form runat="server">
A basic TextBox:
<asp:TextBox id="tb1" runat="server" />
<br /><br />
A password TextBox:
<asp:TextBox id="tb2" TextMode="password" runat="server" />
<br /><br />
A TextBox with text:
<asp:TextBox id="tb4" Text="Hello World!" runat="server" />
<br /><br />
A multiline TextBox:
<asp:TextBox id="tb3" TextMode="multiline" runat="server" />
<br /><br />
A TextBox with height:
<asp:TextBox id="tb6" rows="5" TextMode="multiline"
runat="server" />
<br /><br />
A TextBox with width:
<asp:TextBox id="tb5" columns="30" runat="server" />
</form>
</body>
</html>
```


**[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_textbox_ex1)


---


## 添加脚本


当表单被提交时，TextBox 控件的内容和设置可能会被服务器脚本修改。表单可通过点击一个按钮或当用户修改 TextBox 控件的值的时候进行提交。


在下面的实例中，我们在 .aspx 文件中声明了一个 TextBox 控件、一个 Button 控件和一个 Label 控件。当提交按钮被触发时，submit 子例程将被执行。submit 子例程将写入一行文本到 Label 控件中：


## 实例


```csharp
<script runat="server">
Sub submit(sender As Object, e As EventArgs)
lbl1.Text="Your name is " & txt1.Text
End Sub
</script>
<html>
<body>
<form runat="server">
Enter your name:
<asp:TextBox id="txt1" runat="server" />
<asp:Button OnClick="submit" Text="Submit" runat="server" />
<p><asp:Label id="lbl1" runat="server" /></p>
</form>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_textbox)


在下面的实例中，我们在 .aspx 文件中声明了一个 TextBox 控件和一个 Label 控件。当您修改了 TextBox 中的值，并且在 TextBox 外部点击（或者按下了 Tab 键）时，change 子例程将会被执行。change 子例程将写入一行文本到 Label 控件中：


## 实例


```csharp
<script runat="server">
Sub change(sender As Object, e As EventArgs)
lbl1.Text="You changed text to " & txt1.Text
End Sub
</script>
<html>
<body>
<form runat="server">
Enter your name:
<asp:TextBox id="txt1" runat="server"
text="Hello World!"
ontextchanged="change" autopostback="true"/>
<p><asp:Label id="lbl1" runat="server" /></p>
</form>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_textbox3)










	  AI 思考中...





			** [ASP.NET ViewState](https://www.runoob.com/aspnet-viewstate.html)
			[ASP.NET Button 控件](https://www.runoob.com/aspnet-button.html) **













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