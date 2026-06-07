# ASP.NET Web Pages - Chart 帮助器

- Source: https://www.runoob.com/aspnet/webpages-chart.html

---


Chart 帮助器 - 众多有用的 ASP.NET Web 帮助器之一。


---


## Chart 帮助器


在前面的章节中，您已经学习了如何使用 ASP.NET 的 "帮助器"。


前面已经介绍了如何使用 "WebGrid 帮助器" 在网格中显示数据。


本章介绍如何使用 "Chart 帮助器" 以图形化的形式显示数据。


"Chart 帮助器" 可以创建不同类型的带有多种格式化选项和标签的图表图像。它可以创建面积图、条形图、柱形图、折线图、饼图等标准图表，也可以创建像股票图表这样的更专业的图表。


![chart](https://www.runoob.com/wp-content/uploads/2013/07/06.jpg)![chart](https://www.runoob.com/wp-content/uploads/2013/07/07.jpg)


在图表中显示的数据可以是来自一个数组，一个数据库，或者一个文件中的数据。


---


## 根据数组创建图表


下面的实例显示了根据数组数据显示图表所需的代码：


## 实例


```csharp
@{
var myChart = new Chart(width: 600, height: 400)

.AddTitle("Employees")

.AddSeries(chartType: "column",
      xValue: new[] {  "Peter", "Andrew", "Julie", "Mary", "Dave" },
      yValues: new[] { "2", "6", "4", "5", "3" })

.Write();
}
```


**[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_webpages_cs_005)


- new Chart** 创建一个新的图表对象并且设置它的宽度和高度


- **AddTitle** 方法指定了图表的标题


- **AddSeries** 方法向图表中增加数据


- **chartType** 参数定义图表的类型


- **xValue** 参数定义 x 轴的名称


- **yValues** 参数定义 y 轴的名称


- **Write()** 方法显示图表


---


## 根据数据库创建图表


您可以执行一个数据库查询，然后使用查询结果中的数据来创建一个图表：


## 实例


```csharp
@{
var db = Database.Open("SmallBakery");
var dbdata = db.Query("SELECT Name, Price FROM Product");
var myChart = new Chart(width: 600, height: 400)
   .AddTitle("Product Sales")
   .DataBindTable(dataSource: dbdata, xField: "Name")
   .Write();
}
```


**[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_webpages_cs_006)


- var db = Database.Open** 打开数据库（将数据库对象赋值给变量 db）


- **var dbdata = db.Query** 执行数据库查询并保存结果在 dbdata 中


- **new Chart** 创建一个新的图表对象并且设置它的宽度和高度


- **AddTitle** 方法指定了图表的标题


- **DataBindTable** 方法将数据源绑定到图表


- **Write()** 方法显示图表


除了使用 DataBindTable 方法之外，另一种方法是使用 AddSeries（见前面的实例）。DataBindTable 更容易使用，但是 AddSeries 更加灵活，因为您可以更明确地指定图表和数据：


## 实例


```csharp
@{
var db = Database.Open("SmallBakery");
var dbdata = db.Query("SELECT Name, Price FROM Product");
var myChart = new Chart(width: 600, height: 400)
   .AddTitle("Product Sales")
   .AddSeries(chartType:"Pie",
      xValue: dbdata, xField: "Name",
      yValues: dbdata, yFields: "Price")
   .Write();
}
```


**[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_webpages_cs_007)


---


## 根据 XML 数据创建图表


第三种创建图表的方法是使用 XML 文件作为图表的数据：


## 实例


```csharp
@using System.Data;
@{
var dataSet = new DataSet();
dataSet.ReadXmlSchema(Server.MapPath("data.xsd"));
dataSet.ReadXml(Server.MapPath("data.xml"));
var dataView = new DataView(dataSet.Tables[0]);
var myChart = new Chart(width: 600, height: 400)

.AddTitle("Sales Per Employee")

.AddSeries("Default", chartType: "Pie",

xValue: dataView, xField: "Name",

yValues: dataView, yFields: "Sales")

.Write();}
}
```


[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_webpages_cs_008)









	  AI 思考中...





			** [ASP.NET Web Pages WebGrid](https://www.runoob.com/webpages-webgrid.html)
			[ASP.NET Web Pages Email](https://www.runoob.com/webpages-email.html) **













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