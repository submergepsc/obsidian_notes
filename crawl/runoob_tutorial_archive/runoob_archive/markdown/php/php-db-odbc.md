# PHP 数据库 ODBC

- Source: https://www.runoob.com/php/php-db-odbc.html

---


ODBC 是一种应用程序编程接口（Application Programming Interface，API），使我们有能力连接到某个数据源（比如一个 MS Access 数据库）。


---


## 创建 ODBC 连接


通过一个 ODBC 连接，您可以连接到您的网络中的任何计算机上的任何数据库，只要 ODBC 连接是可用的。


这是创建到达 MS Access 数据库的 ODBC 连接的方法：


- 在控制面板中打开**管理工具**图标。
- 双击其中的**数据源(ODBC)**图标。
- 选择**系统 DSN** 选项卡。
- 点击系统 DSN 选项卡中的**添加**。
- 选择**Microsoft Access Driver**。点击**完成**。
- 在下一个界面，点击**选择**来定位数据库。
- 为数据库起一个**数据源名(DSN)**。
- 点击**确定**。


请注意，必须在您的网站所在的计算机上完成这个配置。如果您的计算机上正在运行 Internet 信息服务(IIS)，上面的指令将会生效，但是如果您的网站位于远程服务器，您必须拥有对该服务器的物理访问权限，或者请您的主机提供商为您建立 DSN。


---


## 连接到 ODBC


odbc_connect() 函数用于连接到 ODBC 数据源。该函数有四个参数：数据源名、用户名、密码以及可选的指针类型。


odbc_exec() 函数用于执行 SQL 语句。


### 实例


下面的实例创建了到达名为 northwind 的 DSN 的连接，没有用户名和密码。然后创建并执行一条 SQL 语句：


```
$conn=odbc_connect('northwind','','');
$sql="SELECT * FROM customers";
$rs=odbc_exec($conn,$sql);
```


**
---


## 取回记录


odbc_fetch_row() 函数用于从结果集中返回记录。如果能够返回行，则函数返回 true，否则返回 false。


该函数有两个参数：ODBC 结果标识符和可选的行号：


```
odbc_fetch_row($rs)
```


---


## 从记录中取回字段


odbc_result() 函数用于从记录中读取字段。该函数有两个参数：ODBC 结果标识符和字段编号或名称。


下面的代码行从记录中返回第一个字段的值：


```
$compname=odbc_result($rs,1);
```


下面的代码行返回名为 "CompanyName" 的字段的值：


```
$compname=odbc_result($rs,"CompanyName");
```


---


## 关闭 ODBC 连接


odbc_close() 函数用于关闭 ODBC 连接。


```
odbc_close($conn);
```


---


## ODBC 实例


下面的实例展示了如何首先创建一个数据库连接，接着创建一个结果集，然后在 HTML 表格中显示数据。


```
<html>
<body>

<?php
$conn=odbc_connect('northwind','','');
if (!$conn)
{
    exit("连接失败: " . $conn);
}

$sql="SELECT * FROM customers";
$rs=odbc_exec($conn,$sql);

if (!$rs)
{
    exit("SQL 语句错误");
}
echo "<table><tr>";
echo "<th>Companyname</th>";
echo "<th>Contactname</th></tr>";

while (odbc_fetch_row($rs))
{
    $compname=odbc_result($rs,"CompanyName");
    $conname=odbc_result($rs,"ContactName");
    echo "<tr><td>$compname</td>";
    echo "<td>$conname</td></tr>";
}
odbc_close($conn);
echo "</table>";
?>

</body>
</html>
```









	  AI 思考中...





			** [PHP MySQL Delete](https://www.runoob.com/php-mysql-delete.html)
			[PHP XML Expat 解析器](https://www.runoob.com/php-xml-parser-expat.html) **













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