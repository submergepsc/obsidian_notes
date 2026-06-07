# ASP.NET Web Forms - Repeater 控件

- Source: https://www.runoob.com/aspnet/aspnet-repeater.html

---


Repeater 控件用于显示被绑定在该控件上的项目的重复列表。


---


## 绑定 DataSet 到 Repeater 控件


Repeater 控件用于显示被绑定在该控件上的项目的重复列表。Repeater 控件可被绑定到数据库表、XML 文件或者其他项目列表。在这里，我们将演示如何绑定 XML 文件到 Repeater 控件。


在我们的实例中，我们将使用下面的 XML 文件（"cdcatalog.xml"）：


<?xml version="1.0" encoding="ISO-8859-1"?>**

<catalog>

<cd>


<title>Empire Burlesque</title>


<artist>Bob Dylan</artist>


<country>USA</country>


<company>Columbia</company>


<price>10.90</price>


<year>1985</year>

</cd>

<cd>


<title>Hide your heart</title>


<artist>Bonnie Tyler</artist>


<country>UK</country>


<company>CBS Records</company>


<price>9.90</price>


<year>1988</year>

</cd>

<cd>


<title>Greatest Hits</title>


<artist>Dolly Parton</artist>


<country>USA</country>


<company>RCA</company>


<price>9.90</price>


<year>1982</year>

</cd>

<cd>


<title>Still got the blues</title>


<artist>Gary Moore</artist>


<country>UK</country>


<company>Virgin records</company>


<price>10.20</price>


<year>1990</year>

</cd>

<cd>


<title>Eros</title>


<artist>Eros Ramazzotti</artist>


<country>EU</country>


<company>BMG</company>


<price>9.90</price>


<year>1997</year>

</cd>

</catalog>


查看这个 XML 文件：[cdcatalog.xml](https://www.runoob.com/try/demo_source/cdcatalog.xml)


首先，导入 "System.Data" 命名空间。我们需要该命名空间与 DataSet 对象一起工作。 把下面这条指令包含在 .aspx 页面的顶部：


<%@ Import Namespace="System.Data" %>


接着，为 XML 文件创建一个 DataSet，并在页面第一次加载时把这个 XML 文件载入 DataSet：


<script runat="server">

sub Page_Load

if Not Page.IsPostBack then


  dim mycdcatalog=New DataSet


  mycdcatalog.ReadXml(MapPath("cdcatalog.xml"))

end if

end sub


然后我们在 .aspx 页面中创建一个 Repeater 控件。 元素中的内容被首先呈现，并且在输出中仅出现一次，而  元素中的内容会对应 DataSet 中的每条 "record" 重复出现，最后， 元素中的内容在输出中仅出现一次：


<html>

<body>


<form runat="server">

<asp:Repeater id="cdcatalog" runat="server">


<HeaderTemplate>

...

</HeaderTemplate>


<ItemTemplate>

...

</ItemTemplate>


<FooterTemplate>

...

</FooterTemplate>


</asp:Repeater>

</form>


</body>

</html>


然后我们添加创建 DataSet 的脚本，并且绑定 mycdcatalog DataSet 到 Repeater 控件。然后 使用 HTML 标签来填充 Repeater 控件，并通过  绑定数据项目到  区域内的单元格中：


## 实例


```csharp
<%@ Import Namespace="System.Data" %>
<script runat="server">
sub Page_Load
if Not Page.IsPostBack then
  dim mycdcatalog=New DataSet
  mycdcatalog.ReadXml(MapPath("cdcatalog.xml"))
  cdcatalog.DataSource=mycdcatalog
  cdcatalog.DataBind()
end if
end sub
</script>
<html>
<body>
<form runat="server">
<asp:Repeater id="cdcatalog" runat="server">
<HeaderTemplate>
<table border="1" width="100%">
<tr>
<th>Title</th>
<th>Artist</th>
<th>Country</th>
<th>Company</th>
<th>Price</th>
<th>Year</th>
</tr>
</HeaderTemplate>
<ItemTemplate>
<tr>
<td><%#Container.DataItem("title")%></td>
<td><%#Container.DataItem("artist")%></td>
<td><%#Container.DataItem("country")%></td>
<td><%#Container.DataItem("company")%></td>
<td><%#Container.DataItem("price")%></td>
<td><%#Container.DataItem("year")%></td>
</tr>
</ItemTemplate>
<FooterTemplate>
</table>
</FooterTemplate>
</asp:Repeater>
</form>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_repeater1)


---


## 使用


您可以在  元素后添加  元素，用来描述输出中交替行的外观。在下面的实例中，表格每隔一行就会显示为浅灰色的背景：


## 实例


```csharp
<%@ Import Namespace="System.Data" %>
<script runat="server">
sub Page_Load
if Not Page.IsPostBack then
  dim mycdcatalog=New DataSet
  mycdcatalog.ReadXml(MapPath("cdcatalog.xml"))
  cdcatalog.DataSource=mycdcatalog
  cdcatalog.DataBind()
end if
end sub
</script>
<html>
<body>
<form runat="server">
<asp:Repeater id="cdcatalog" runat="server">
<HeaderTemplate>
<table border="1" width="100%">
<tr>
<th>Title</th>
<th>Artist</th>
<th>Country</th>
<th>Company</th>
<th>Price</th>
<th>Year</th>
</tr>
</HeaderTemplate>
<ItemTemplate>
<tr>
<td><%#Container.DataItem("title")%></td>
<td><%#Container.DataItem("artist")%></td>
<td><%#Container.DataItem("country")%></td>
<td><%#Container.DataItem("company")%></td>
<td><%#Container.DataItem("price")%></td>
<td><%#Container.DataItem("year")%></td>
</tr>
</ItemTemplate>
<AlternatingItemTemplate>
<tr bgcolor="#e8e8e8">
<td><%#Container.DataItem("title")%></td>
<td><%#Container.DataItem("artist")%></td>
<td><%#Container.DataItem("country")%></td>
<td><%#Container.DataItem("company")%></td>
<td><%#Container.DataItem("price")%></td>
<td><%#Container.DataItem("year")%></td>
</tr>
</AlternatingItemTemplate>
<FooterTemplate>
</table>
</FooterTemplate>
</asp:Repeater>
</form>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_repeater2)


---


## 使用


 元素用于描述每个记录之间的分隔符。在下面的实例中，每个表格行之间插入了一条水平线：


## 实例


```csharp
<%@ Import Namespace="System.Data" %>
<script runat="server">
sub Page_Load
if Not Page.IsPostBack then
  dim mycdcatalog=New DataSet
  mycdcatalog.ReadXml(MapPath("cdcatalog.xml"))
  cdcatalog.DataSource=mycdcatalog
  cdcatalog.DataBind()
end if
end sub
</script>
<html>
<body>
<form runat="server">
<asp:Repeater id="cdcatalog" runat="server">
<HeaderTemplate>
<table border="0" width="100%">
<tr>
<th>Title</th>
<th>Artist</th>
<th>Country</th>
<th>Company</th>
<th>Price</th>
<th>Year</th>
</tr>
</HeaderTemplate>
<ItemTemplate>
<tr>
<td><%#Container.DataItem("title")%></td>
<td><%#Container.DataItem("artist")%></td>
<td><%#Container.DataItem("country")%></td>
<td><%#Container.DataItem("company")%></td>
<td><%#Container.DataItem("price")%></td>
<td><%#Container.DataItem("year")%></td>
</tr>
</ItemTemplate>
<SeparatorTemplate>
<tr>
<td colspan="6"><hr /></td>
</tr>
</SeparatorTemplate>
<FooterTemplate>
</table>
</FooterTemplate>
</asp:Repeater>
</form>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_repeater3)










	  AI 思考中...





			** [ASP.NET XML 数据绑定](https://www.runoob.com/aspnet-xml.html)
			[ASP.NET DataList 控件](https://www.runoob.com/aspnet-datalist.html) **













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