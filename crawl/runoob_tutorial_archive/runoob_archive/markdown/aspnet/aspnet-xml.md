# ASP.NET Web Forms - XML 文件

- Source: https://www.runoob.com/aspnet/aspnet-xml.html

---


我们可以绑定 XML 文件到列表控件。


---


## 一个 XML 文件


这里有一个名为 "countries.xml" 的 XML 文件：


<?xml version="1.0" encoding="ISO-8859-1"?>**

<countries>


<country>


<text>Norway</text>


<value>N</value>

</country>


<country>


<text>Sweden</text>


<value>S</value>

</country>


<country>


<text>France</text>


<value>F</value>

</country>


<country>


<text>Italy</text>


<value>I</value>

</country>


</countries>


查看这个 XML 文件：countries.xml


---


## 绑定 DataSet 到 List 控件


首先，导入 "System.Data" 命名空间。我们需要该命名空间与 DataSet 对象一起工作。把下面这条指令包含在 .aspx 页面的顶部：


<%@ Import Namespace="System.Data" %>


接着，为 XML 文件创建一个 DataSet，并在页面第一次加载时把这个 XML 文件载入 DataSet：


<script runat="server">

sub Page_Load

if Not Page.IsPostBack then


  dim mycountries=New DataSet


  mycountries.ReadXml(MapPath("countries.xml"))

end if

end sub


为了绑定数据到 RadioButtonList 控件，首先要在 .aspx 页面中创建一个 RadioButtonList 控件（不带任何 asp:ListItem 元素）：


<html>

<body>


<form runat="server">

<asp:RadioButtonList id="rb" runat="server"
AutoPostBack="True" />

</form>


</body>

</html>


然后添加创建 XML DataSet 的脚本，并且绑定 XML DataSet 中的值到 RadioButtonList 控件：


<%@ Import Namespace="System.Data" %>


<script runat="server">

sub Page_Load

if Not Page.IsPostBack then


  dim mycountries=New DataSet


  mycountries.ReadXml(MapPath("countries.xml"))


  rb.DataSource=mycountries


  rb.DataValueField="value"


  rb.DataTextField="text"


  rb.DataBind()

end if

end sub

</script>


<html>

<body>


<form runat="server">

<asp:RadioButtonList id="rb" runat="server"

AutoPostBack="True" onSelectedIndexChanged="displayMessage" />

</form>


</body>

</html>


然后我们添加一个子例程，当用户点击 RadioButtonList 控件中的某个项目时，该子例程会被执行。当某个单选按钮被点击时，label 中会出现一行文本：


## 实例


```csharp
<%@ Import Namespace="System.Data" %>
<script runat="server">
sub Page_Load
if Not Page.IsPostBack then
  dim mycountries=New DataSet
  mycountries.ReadXml(MapPath("countries.xml"))
  rb.DataSource=mycountries
  rb.DataValueField="value"
  rb.DataTextField="text"
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


[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_xml_radio1)










	  AI 思考中...





			** [ASP.NET SortedList](https://www.runoob.com/aspnet-sortedlist.html)
			[ASP.NET Repeater 控件](https://www.runoob.com/aspnet-repeater.html) **













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