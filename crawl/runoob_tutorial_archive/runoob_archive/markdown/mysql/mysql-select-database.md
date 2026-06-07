# MySQL 选择数据库

- Source: https://www.runoob.com/mysql/mysql-select-database.html

在你连接到 MySQL 数据库后，可能有多个可以操作的数据库，所以你需要选择你要操作的数据库。


---


## 从命令提示窗口中选择 MySQL 数据库


在 **mysql>** 提示窗口中可以很简单的选择特定的数据库。


在 MySQL 中，要选择要使用的数据库，可以使用 **USE** 语句，以下是基本的语法：


```
USE database_name;
```


**参数说明：**


- **database_name** 是你要选择的数据库的名称。


选择来数据库后，你的后续 SQL 查询和操作在指定的数据库 **database_name** 上执行。


### 实例

以下实例选取了数据库 RUNOOB:


```
[root@host]# mysql -u root -p
Enter password:******
mysql> use RUNOOB;
Database changed
mysql>
```



执行以上命令后，你就已经成功选择了 RUNOOB 数据库，在后续的操作中都会在 RUNOOB 数据库中执行。


在命令行中，你可以通过以下方式选择数据库：


```
mysql -u your_username -p -D your_database
```



- **-D** 参数用于指定要选择的数据库。


例如：


```
mysql -u root -p -D RUNOOB
```


在输入密码后，你将进入 MySQL 提示符，并且任何后续的查询和操作都将在 RUNOOB 数据库上执行。


**
请确保选择的数据库存在，否则你将收到错误消息。你可以使用 **SHOW DATABASES;** 查询可用的数据库，确保你要选择的数据库在列表中。


---


## 使用 PHP 脚本选择 MySQL 数据库


PHP 提供了函数 mysqli_select_db 来选取一个数据库。函数在执行成功后返回 TRUE ，否则返回 FALSE 。


### 语法


```
mysqli_select_db(connection,dbname);
```


| 参数 | 描述 |
| --- | --- |
| connection | 必需。规定要使用的 MySQL 连接。 |
| dbname | 必需，规定要使用的默认数据库。 |


### 实例


以下实例展示了如何使用 mysqli_select_db 函数来选取一个数据库：


## 选择数据库



```sql
<?php
$dbhost = 'localhost';  // mysql服务器主机地址
$dbuser = 'root';            // mysql用户名
$dbpass = '123456';          // mysql用户名密码
$conn = mysqli_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
    die('连接失败: ' . mysqli_error($conn));
}
echo '连接成功';
mysqli_select_db($conn, 'RUNOOB' );
mysqli_close($conn);
?>
```










	  AI 思考中...





			** [MySQL 删除数据库](https://www.runoob.com/mysql-drop-database.html)
			[MySQL 数据类型](https://www.runoob.com/mysql-data-types.html) **













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