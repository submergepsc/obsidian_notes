# 下载

- Source: https://www.runoob.com/appml/appml-download.html

---


本章节将介绍如何下载 ，下载后我们将立即开始在你的电脑上开发 web应用。


---


## 下载


 不是一个产品。  是一个想法。 它仅仅是在浏览器上的脚本和服务器上的脚本。


任何人都可以下载  ，下载后可以修改基本来创建我们自己的专业web应用。


你可以从下载使用于PHP的  ： [AppmlPHP.zip](https://www.runoob.com/try/download/AppmlPHP.zip)


|  | 本站关于 appml 的 php 实例采用链接数据库的方式为 mysqli 及 mysqlnd 更多关于 php mysqli信息请查看：PHP 5 MySQLi 函数 更多关于 php mysqlnd 信息请查看：mysqlnd介绍 |
| --- | --- |


你也可以下载适用于ASP .NET的  ： [AppmlASP.zip](https://www.runoob.com/try/download/AppmlASP.zip)


---


## ZIP 文件内容:


| 文件名 | 描述 |
| --- | --- |
| appml.php (或者.htmlx) | 服务端脚本 |
| appml.css | 样式文件 |
| appml.js | 浏览器脚本 |
| appml_config.php (or .htmlx) | 本地配置 |
| Images (文件夹) | 图片样式 |

**
---


## 如果你有自己的web服务器


如果你已经拥有支持 ASP.NET 或 PHP 的web服务器:


1. 创建一个文件夹并命名为Demo (或者其他)。


2. 从zip中解压文件和文件夹.


3. 拷贝文件很文件夹到你新的web文件夹中。


4. 开始开发你的应用


---


## 如果你没有web服务器


如果你没有web服务器，你可以使用 Microsoft's WebMatrix (免费软件) 来开发web应用


使用 WebMatrix, 你不需要web服务器就可以在你的电脑上编辑，测试，及执行web应用。


WebMatrix 自带功能:


-  文件编辑器(HTML, CSS, 和 XML)
- 可以运行应用的web服务器 (IIS Express)
- 数据库服务器 (SQL Server Compact)
- 很好的支持服务端语言 (PHP, ASP, 和 ASP.NET)


你可以从以下地址下载WebMatrix：


[http://www.microsoft.com/web/webmatrix](http://www.microsoft.com/web/webmatrix)


当你已经安装 WebMatrix, 就可以参照以上步骤使用Appml。


---


## 如果已经有数据库


通过改变 appml.config**文件的配置信息，可以连接到你自己服务器上的数据库：


## PHP MySQL:


```
<database name="demo">
  <host>127.0.0.1</host>  <name>dbName</name>
	<user>dbUser</user>  <password>dbPass</password></database>
```


**
## ASP.NET SQL Server


```
<database name="demo">
	<connection>Provider=SQLOLEDB;data source=sName;Database=dbName;user
	id=dbUser;password=dbPass</connection></database>
```


## ASP.NET Access (完整路径)


```
<database name="demo">
<connection>Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:DemoDataDemo.mdb</connection></database>
```


## ASP.NET Access (虚拟路径;)


```
<database name="demo">
<connection>Provider=Microsoft.Jet.OLEDB.4.0;Data Source=#webroot#DataDemo.mdb</connection></database>
```


---


## 如果你没有数据库


如果你没有数据库:


你可以使用 WebMatrix 创建一个数据库。


或者从以下链接下载 Access 数据库: [Northwind.zip](https://www.runoob.com/try/download/Northwind.zip).

或者从以下链接下载 空的 Access 数据库:  [Database.zip](https://www.runoob.com/try/download/EmptyDatabase.zip)


---


## 更多下载


你可以从本周下载更多应用实例教程：


[PHP 版本](https://www.runoob.com/try/download/DemoPHP.zip)


[ASP.NET 版本](https://www.runoob.com/try/download/DemoASP.zip)


你可以下载完整的数据应用测试实例：


[PHP 版本](https://www.runoob.com/try/download/CreatePHP.zip)


[ASP.NET 版本](https://www.runoob.com/try/download/CreateASP.zip)








	  AI 思考中...





			** [如何使用 AppML](https://www.runoob.com/appml-howto.html)
			[AppML 架构](https://www.runoob.com/appml-architecture.html) **













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