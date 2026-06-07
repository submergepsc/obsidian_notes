# MySQL 元数据

- Source: https://www.runoob.com/mysql/mysql-database-info.html

MySQL 元数据是关于数据库和其对象（如表、列、索引等）的信息。

元数据存储在系统表中，这些表位于 MySQL 数据库的 information_schema 数据库中，通过查询这些系统表，你可以获取关于数据库结构、对象和其他相关信息的详细信息。


你可能想知道MySQL以下三种信息：


- **查询结果信息：** SELECT, UPDATE 或 DELETE语句影响的记录数。
- **数据库和数据表的信息：** 包含了数据库及数据表的结构信息。
- **MySQL 服务器信息：** 包含了数据库服务器的当前状态，版本号等。


在 MySQL 的命令提示符中，我们可以很容易的获取以上服务器信息，但如果使用 Perl 或 PHP 等脚本语言，你就需要调用特定的接口函数来获取，接下来我们会详细介绍。


以下是一些常用的 MySQL 元数据查询：


查看所有数据库：


```
SHOW DATABASES;
```


选择数据库：


```
USE database_name;
```


查看数据库中的所有表：


```
SHOW TABLES;
```


查看表的结构：


```
DESC table_name;
```


查看表的索引：


```
SHOW INDEX FROM table_name;
```


查看表的创建语句：


```
SHOW CREATE TABLE table_name;
```


查看表的行数：


```
SELECT COUNT(*) FROM table_name;
```


查看列的信息：


```
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_KEY
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'your_database_name'
AND TABLE_NAME = 'your_table_name';
```


以上SQL 语句中的 'your_database_name' 和 'your_table_name' 分别是你的数据库名和表名。

查看外键信息：


```
SELECT
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
    TABLE_SCHEMA = 'your_database_name'
    AND TABLE_NAME = 'your_table_name'
    AND REFERENCED_TABLE_NAME IS NOT NULL;
```


请替换上述 SQL 语句中的 'your_database_name' 和 'your_table_name' 为实际的数据库名和表名。


---


## information_schema 数据库


information_schema 是 MySQL 数据库中的一个系统数据库，它包含有关数据库服务器的元数据信息，这些信息以表的形式存储在 information_schema 数据库中。


### SCHEMATA 表


存储有关数据库的信息，如数据库名、字符集、排序规则等。


```
SELECT * FROM information_schema.SCHEMATA;
```


### TABLES 表

包含有关数据库中所有表的信息，如表名、数据库名、引擎、行数等。


```
SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'your_database_name';
```


### COLUMNS 表

包含有关表中列的信息，如列名、数据类型、是否允许 NULL 等。


```
SELECT * FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'your_database_name' AND TABLE_NAME = 'your_table_name';
```


### STATISTICS 表

提供有关表索引的统计信息，如索引名、列名、唯一性等。


```
SELECT * FROM information_schema.STATISTICS WHERE TABLE_SCHEMA = 'your_database_name' AND TABLE_NAME = 'your_table_name';
```


### KEY_COLUMN_USAGE 表

包含有关表中外键的信息，如外键名、列名、关联表等。


```
SELECT * FROM information_schema.KEY_COLUMN_USAGE WHERE TABLE_SCHEMA = 'your_database_name' AND TABLE_NAME = 'your_table_name';
```


### REFERENTIAL_CONSTRAINTS 表

存储有关外键约束的信息，如约束名、关联表等。


```
SELECT * FROM information_schema.REFERENTIAL_CONSTRAINTS WHERE CONSTRAINT_SCHEMA = 'your_database_name' AND TABLE_NAME = 'your_table_name';
```


这些表提供了丰富的元数据信息，可以用于查询数据库结构、表信息、列信息、索引信息等。

请注意，你需要将查询中的 'your_database_name' 和 'your_table_name' 替换为实际的数据库名和表名。


---


## 获取查询语句影响的记录数


### PERL 实例


在 DBI 脚本中， 语句影响的记录数通过函数 do( ) 或 execute( )返回：


```
# 方法 1
# 使用do( ) 执行  $query
my $count = $dbh->do ($query);
# 如果发生错误会输出 0
printf "%d 条数据被影响\n", (defined ($count) ? $count : 0);

# 方法 2
# 使用prepare( ) 及 execute( ) 执行  $query
my $sth = $dbh->prepare ($query);
my $count = $sth->execute ( );
printf "%d 条数据被影响\n", (defined ($count) ? $count : 0);
```


### PHP 实例


在PHP中，你可以使用 mysqli_affected_rows( ) 函数来获取查询语句影响的记录数。


```
$result_id = mysqli_query ($conn_id, $query);
# 如果查询失败返回
$count = ($result_id ? mysqli_affected_rows ($conn_id) : 0);
print ("$count 条数据被影响\n");
```


---


## 数据库和数据表列表


你可以很容易的在MySQL服务器中获取数据库和数据表列表。 如果你没有足够的权限，结果将返回 null。


你也可以使用 SHOW TABLES 或 SHOW DATABASES 语句来获取数据库和数据表列表。


### PERL 实例


```
# 获取当前数据库中所有可用的表。
my @tables = $dbh->tables ( );
foreach $table (@tables ){
   print "表名 $table\n";
}
```


### PHP 实例


以下实例输出 MySQL 服务器上的所有数据库：


## 查看所有数据库



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
// 设置编码，防止中文乱码
$db_list = mysqli_query($conn, 'SHOW DATABASES');
while ($db = mysqli_fetch_object($db_list))
{
  echo $db->Database . "<br />";
}
mysqli_close($conn);
?>
```


---


## 获取服务器元数据


以下命令语句可以在 MySQL 的命令提示符使用，也可以在脚本中 使用，如PHP脚本。


| 命令 | 描述 |
| --- | --- |
| SELECT VERSION( ) | 服务器版本信息 |
| SELECT DATABASE( ) | 当前数据库名 (或者返回空) |
| SELECT USER( ) | 当前用户名 |
| SHOW STATUS | 服务器状态 |
| SHOW VARIABLES | 服务器配置变量 |








	  AI 思考中...





			** [MySQL 复制表](https://www.runoob.com/mysql-clone-tables.html)
			[MySQL 序列使用（AUTO_INCREMENT）](https://www.runoob.com/mysql-using-sequences.html) **













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