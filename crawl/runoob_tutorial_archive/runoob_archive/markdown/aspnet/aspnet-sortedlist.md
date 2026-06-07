# ASP.NET Web Forms - SortedList 对象

- Source: https://www.runoob.com/aspnet/aspnet-sortedlist.html

---


SortedList 对象结合了 ArrayList 对象和 Hashtable 对象的特性。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[SortedList RadiobuttonList 1](https://www.runoob.com/try/showaspx.php?filename=demo_sortedlist_radio1)


[SortedList RadiobuttonList 2](https://www.runoob.com/try/showaspx.php?filename=demo_sortedlist_radio2)


[SortedList DropDownList](https://www.runoob.com/try/showaspx.php?filename=demo_sortedlist_drop1)


---


## SortedList 对象


SortedList 对象包含用键/值对表示的项目。SortedList 对象按照字母顺序或者数字顺序自动地对项目进行排序。


通过 Add() 方法向 SortedList 添加项目。通过 TrimToSize() 方法把 SortedList 调整为最终尺寸。


下面的代码创建了一个名为 mycountries 的 SortedList 对象，并添加了四个元素：


<script runat="server">**
sub Page_Load

if Not Page.IsPostBack then


  dim mycountries=New SortedList


  mycountries.Add("N","Norway")


  mycountries.Add("S","Sweden")


  mycountries.Add("F","France")


  mycountries.Add("I","Italy")

end if

end sub

</script>


---


## 数据绑定


SortedList 对象可为下列的控件自动生成文本和值：


- asp:RadioButtonList
- asp:CheckBoxList
- asp:DropDownList
- asp:Listbox


为了绑定数据到 RadioButtonList 控件，首先要在 .aspx 页面中创建一个 RadioButtonList 控件（不带任何 asp:ListItem 元素）：


<html>

<body>


<form runat="server">

<asp:RadioButtonList id="rb" runat="server"
AutoPostBack="True" />

</form>


</body>

</html>


然后添加创建列表的脚本，并且绑定列表中的值到 RadioButtonList 控件：


<script runat="server">

sub Page_Load

if Not Page.IsPostBack then


  dim mycountries=New SortedList


  mycountries.Add("N","Norway")


  mycountries.Add("S","Sweden")


  mycountries.Add("F","France")


  mycountries.Add("I","Italy")


  rb.DataSource=mycountries


  rb.DataValueField="Key"


  rb.DataTextField="Value"


  rb.DataBind()

end if

end sub

</script>


<html>

<body>


<form runat="server">

<asp:RadioButtonList id="rb" runat="server"
AutoPostBack="True" />

</form>


</body>

</html>


然后我们添加一个子例程，当用户点击 RadioButtonList 控件中的某个项目时，该子例程会被执行。当某个单选按钮被点击时，label 中会出现一行文本：


## 实例


```csharp
<script runat="server">
sub Page_Load
if Not Page.IsPostBack then
  dim mycountries=New SortedList
  mycountries.Add("N","Norway")
  mycountries.Add("S","Sweden")
  mycountries.Add("F","France")
  mycountries.Add("I","Italy")
  rb.DataSource=mycountries
  rb.DataValueField="Key"
  rb.DataTextField="Value"
  rb.DataBind()
end if
end sub
sub displayMessage(s as Object,e As EventArgs)
lbl1.text="Your favorite country is: " & rb.SelectedItem.Text
end sub
</script>
<html>
<body>
<form runat="server">
<asp:RadioButtonList id="rb" runat="server"
AutoPostBack="True" onSelectedIndexChanged="displayMessage" />
<p><asp:label id="lbl1" runat="server" /></p>
</form>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_sortedlist_radio1)










	  AI 思考中...





			** [ASP.NET Hashtable](https://www.runoob.com/aspnet-hashtable.html)
			[ASP.NET XML 数据绑定](https://www.runoob.com/aspnet-xml.html) **













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