# ASP.NET Web Forms - 数据库连接

- Source: https://www.runoob.com/aspnet/aspnet-dbconnection.html

---


ADO.NET 也是 .NET 框架的组成部分。ADO.NET 用于处理数据访问。通过 ADO.NET，您可以操作数据库。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[数据库连接 - 绑定到 DataList 控件](https://www.runoob.com/try/showaspx.php?filename=demo_dbconn_datalist)


[数据库连接 - 绑定到 Repeater 控件](https://www.runoob.com/try/showaspx.php?filename=demo_dbconn_repeater)


---


## 什么是 ADO.NET？


- ADO.NET 是 .NET 框架的组成部分
- ADO.NET 由一系列用于处理数据访问的类组成
- ADO.NET 完全基于 XML
- ADO.NET 没有 Recordset 对象，这一点与 ADO 不同


---


## 创建数据库连接


在我们的实例中，我们将使用 Northwind 数据库。


首先，导入 "System.Data.OleDb" 命名空间。我们需要这个命名空间来操作 Microsoft Access 和其他 OLE DB 数据库提供商。我们将在 Page_Load 子例程中创建这个数据库的连接。我们创建一个 dbconn 变量，并为其赋值一个新的 OleDbConnection 类，这个类带有指示 OLE DB 提供商和数据库位置的连接字符串。然后我们打开数据库连接：


<%@ Import Namespace="System.Data.OleDb" %>**

<script runat="server">

sub Page_Load

dim dbconn

dbconn=New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;

data source=" & server.mappath("northwind.mdb"))

dbconn.Open()

end sub

</script>


注释：**这个连接字符串必须是没有折行的连续字符串！


---


## 创建数据库命令


为了指定需从数据库取回的记录，我们将创建一个 dbcomm 变量，并为其赋值一个新的 OleDbCommand 类。这个 OleDbCommand 类用于发出针对数据库表的 SQL 查询：


<%@ Import Namespace="System.Data.OleDb" %>**

<script runat="server">

sub Page_Load

dim dbconn,sql,dbcomm

dbconn=New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;

data source=" & server.mappath("northwind.mdb"))

dbconn.Open()

sql="SELECT * FROM customers"

dbcomm=New OleDbCommand(sql,dbconn)

end sub

</script>


---


## 创建 DataReader


OleDbDataReader 类用于从数据源中读取记录流。DataReader 是通过调用 OleDbCommand 对象的 ExecuteReader 方法来创建的：


<%@ Import Namespace="System.Data.OleDb" %>


<script runat="server">

sub Page_Load

dim dbconn,sql,dbcomm,dbread

dbconn=New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;

data source=" & server.mappath("northwind.mdb"))

dbconn.Open()

sql="SELECT * FROM customers"

dbcomm=New OleDbCommand(sql,dbconn)

dbread=dbcomm.ExecuteReader()

end sub

</script>


---


## 绑定到 Repeater 控件


然后，我们绑定 DataReader 到 Repeater 控件：


## 实例


```csharp
<%@ Import Namespace="System.Data.OleDb" %>
<script runat="server">
sub Page_Load
dim dbconn,sql,dbcomm,dbread
dbconn=New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;
data source=" & server.mappath("northwind.mdb"))
dbconn.Open()
sql="SELECT * FROM customers"
dbcomm=New OleDbCommand(sql,dbconn)
dbread=dbcomm.ExecuteReader()
customers.DataSource=dbread
customers.DataBind()
dbread.Close()
dbconn.Close()
end sub
</script>
<html>
<body>
<form runat="server">
<asp:Repeater id="customers" runat="server">
<HeaderTemplate>
<table border="1" width="100%">
<tr>
<th>Companyname</th>
<th>Contactname</th>
<th>Address</th>
<th>City</th>
</tr>
</HeaderTemplate>
<ItemTemplate>
<tr>
<td><%#Container.DataItem("companyname")%></td>
<td><%#Container.DataItem("contactname")%></td>
<td><%#Container.DataItem("address")%></td>
<td><%#Container.DataItem("city")%></td>
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


[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_dbconn_repeater)


---


## 关闭数据库连接


如果不再需要访问数据库，请记得关闭 DataReader 和数据库连接：


dbread.Close()

dbconn.Close()









	  AI 思考中...





			** [ASP.NET DataList 控件](https://www.runoob.com/aspnet-datalist.html)
			[ASP.NET 母版页](https://www.runoob.com/aspnet-masterpages.html) **













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