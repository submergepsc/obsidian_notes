# PHP - AJAX 与 MySQL

- Source: https://www.runoob.com/php/php-ajax-database.html

---


AJAX 可用来与数据库进行交互式通信。


---


## AJAX 数据库实例


下面的实例将演示网页如何通过 AJAX 从数据库读取信息：


本教程使用到的 Websites 表 SQL 文件：[websites.sql](http://static.runoob.com/download/websites.sql)。


## 实例



选择一个网站:
Google
淘宝
菜鸟教程
微博
Facebook


**选择对应选项，用户信息会显示在这……


---


## 实例解释 - MySQL 数据库


在上面的实例中，我们使用的数据库表如下所示：


```
mysql> select * from websites;
+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 2  | 淘宝       | https://www.taobao.com/   | 13    | CN      |
| 3  | 菜鸟教程 | http://www.runoob.com/    | 4689  | CN      |
| 4  | 微博       | http://weibo.com/         | 20    | CN      |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
+----+--------------+---------------------------+-------+---------+
5 rows in set (0.01 sec)
```


---


## 实例解释 - HTML 页面


当用户在上面的下拉列表中选择某位用户时，会执行名为 "showSite()" 的函数。该函数由 "onchange" 事件触发：



## test.html 文件代码:


```php
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
<script>
```

function showSite(str)
{
    if (str=="")
    {
        document.getElementById("txtHint").innerHTML="";
        return;
    }
    if (window.XMLHttpRequest)
    {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp=new XMLHttpRequest();
    }
    else
    {
        // IE6, IE5 浏览器执行代码
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
            document.getElementById("txtHint").innerHTML=xmlhttp.responseText;
        }
    }
    xmlhttp.open("GET","getsite_mysql.php?q="+str,true);
    xmlhttp.send();
}</script>
</head>
<body>

<form>
<select name="users" onchange="showSite(this.value)">
<option value="">选择一个网站:</option>
<option value="1">Google</option>
<option value="2">淘宝</option>
<option value="3">菜鸟教程</option>
<option value="4">微博</option>
<option value="5">Facebook</option>
</select>
</form>
<br>
<div id="txtHint"><b>网站信息显示在这里……</b></div>

</body>
</html>


showSite() 函数会执行以下步骤：


- 检查是否有网站被选择
- 创建 XMLHttpRequest 对象
- 创建在服务器响应就绪时执行的函数
- 向服务器上的文件发送请求
- 请注意添加到 URL 末端的参数（q）（包含下拉列表的内容）


---


## PHP 文件


上面这段通过 JavaScript 调用的服务器页面是名为 "getsite_mysql.php" 的 PHP 文件。


"getsite_mysql.php" 中的源代码会运行一次针对 MySQL 数据库的查询，然后在 HTML 表格中返回结果：


## getsite_mysql.php 文件代码:


```php
<?php
$q = isset($_GET["q"]) ? intval($_GET["q"]) : '';

if(empty($q)) {
    echo '请选择一个网站';
    exit;
}

$con = mysqli_connect('localhost','root','123456');
if (!$con)
{
    die('Could not connect: ' . mysqli_error($con));
}
// 选择数据库
mysqli_select_db($con,"test");
// 设置编码，防止中文乱码
mysqli_set_charset($con, "utf8");

$sql="SELECT * FROM Websites WHERE id = '".$q."'";

$result = mysqli_query($con,$sql);

echo "<table border='1'>
<tr>
<th>ID</th>
<th>网站名</th>
<th>网站 URL</th>
<th>Alexa 排名</th>
<th>国家</th>
</tr>";

while($row = mysqli_fetch_array($result))
{
    echo "<tr>";
    echo "<td>" . $row['id'] . "</td>";
    echo "<td>" . $row['name'] . "</td>";
    echo "<td>" . $row['url'] . "</td>";
    echo "<td>" . $row['alexa'] . "</td>";
    echo "<td>" . $row['country'] . "</td>";
    echo "</tr>";
}
echo "</table>";

mysqli_close($con);
?>
```


解释：当查询从 JavaScript 发送到 PHP 文件时，将发生：


- PHP 打开一个到 MySQL 数据库的连接
- 找到选中的用户
- 创建 HTML 表格，填充数据，并发送回 "txtHint" 占位符








	  AI 思考中...





			** [PHP – AJAX 与 PHP](https://www.runoob.com/php-ajax-php.html)
			[PHP 实例 AJAX 与 XML](https://www.runoob.com/php-ajax-xml.html) **













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