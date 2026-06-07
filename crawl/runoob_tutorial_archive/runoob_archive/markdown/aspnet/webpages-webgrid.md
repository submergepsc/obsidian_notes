# ASP.NET Web Pages - WebGrid 帮助器

- Source: https://www.runoob.com/aspnet/webpages-webgrid.html

---


WebGrid - 众多有用的 ASP.NET Web 帮助器之一。


---


## 自己写的 HTML


在前面的章节中，您使用 Razor 代码显示数据库数据，所有的 HTML 标记都是手写的：


## 数据库实例


```csharp
@{
var db = Database.Open("SmallBakery");
var selectQueryString = "SELECT * FROM Product ORDER BY Name";
}
<html>
<body>
<h1>Small Bakery Products</h1>
<table>
<tr>
<th>Id</th>
<th>Product</th>
<th>Description</th>
<th>Price</th>
</tr>@foreach(var row in db.Query(selectQueryString))
{
<tr>
<td>@row.Id</td>
<td>@row.Name</td>
<td>@row.Description</td>
<td align="right">@row.Price</td>
</tr> }
</table>
</body>
</html>
```


**[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_webpages_cs_003)


---


## 使用 WebGrid 帮助器


WebGrid 帮助器提供了一种更简单的显示数据的方法。


WebGrid 帮助器：


- 自动创建一个 HTML 表格来显示数据
- 支持不同的格式化选项
- 支持数据分页显示
- 支持通过点击列表标题进行排序


## WebGrid 实例


```csharp
@{
var db = Database.Open("SmallBakery") ;
var selectQueryString = "SELECT * FROM Product ORDER BY Id";
var data = db.Query(selectQueryString);
var grid = new WebGrid(data);
}
<html>
<head>
<title>Displaying Data Using the WebGrid Helper</title>
</head>
<body>
<h1>Small Bakery Products</h1>
<div id="grid"> @grid.GetHtml()
</div>
</body>
</html>
```


[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_webpages_cs_004)










	  AI 思考中...





			** [ASP.NET Web Pages 帮助器](https://www.runoob.com/webpages-helpers.html)
			[ASP.NET Web Pages 图表](https://www.runoob.com/webpages-chart.html) **













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