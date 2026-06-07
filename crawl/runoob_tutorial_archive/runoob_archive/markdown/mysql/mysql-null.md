# MySQL NULL 值处理

- Source: https://www.runoob.com/mysql/mysql-null.html

我们已经知道 MySQL 使用 **SELECT** 命令及 **WHERE** 子句来读取数据表中的数据，但是当提供的查询条件字段为 NULL 时，该命令可能就无法正常工作。


在 MySQL 中，NULL 用于表示缺失的或未知的数据，处理 NULL 值需要特别小心，因为在数据库中它可能会导致不同于预期的结果。


为了处理这种情况，MySQL提供了三大运算符:


- **IS NULL:** 当列的值是 NULL,此运算符返回 true。
- **IS NOT NULL:** 当列的值不为 NULL, 运算符返回 true。
- **:** 比较操作符（不同于 = 运算符），当比较的的两个值相等或者都为 NULL 时返回 true。


关于 NULL 的条件比较运算是比较特殊的。你不能使用 = NULL 或 != NULL 在列中查找 NULL 值 。

在 MySQL 中，NULL 值与任何其它值的比较（即使是 NULL）永远返回 NULL，即 NULL = NULL 返回 NULL 。

MySQL 中处理 NULL 使用 IS NULL 和 IS NOT NULL 运算符。


**

注意：**


```
select * , columnName1+ifnull(columnName2,0) from tableName;
```


columnName1，columnName2 为 int 型，当 columnName2 中，有值为 null 时，columnName1+columnName2=null， ifnull(columnName2,0) 把 columnName2 中 null 值转为 0。


### MySQL 中处理 NULL 值的常见注意事项和技巧


1. 检查是否为 NULL：

要检查某列是否为 NULL，可以使用 IS NULL 或 IS NOT NULL 条件。


```
SELECT * FROM employees WHERE department_id IS NULL;
SELECT * FROM employees WHERE department_id IS NOT NULL;
```


2. 使用 COALESCE 函数处理 NULL：

COALESCE 函数可以用于替换为 NULL 的值，它接受多个参数，返回参数列表中的第一个非 NULL 值：


```
SELECT product_name, COALESCE(stock_quantity, 0) AS actual_quantity
FROM products;
```


以上 SQL 语句中，如果 stock_quantity 列为 NULL，则 COALESCE 将返回 0。


3. 使用 IFNULL 函数处理 NULL：


IFNULL 函数是 COALESCE 的 MySQL 特定版本，它接受两个参数，如果第一个参数为 NULL，则返回第二个参数。


```
SELECT product_name, IFNULL(stock_quantity, 0) AS actual_quantity
FROM products;
```


4. NULL 排序：

在使用 ORDER BY 子句进行排序时，NULL 值默认会被放在排序的最后。如果希望将 NULL 值放在最前面，可以使用 ORDER BY column_name ASC NULLS FIRST，反之使用 ORDER BY column_name DESC NULLS LAST。


```
SELECT product_name, price
FROM products
ORDER BY price ASC NULLS FIRST;
```


5. 使用 操作符进行 NULL 比较：

 操作符是 MySQL 中用于比较两个表达式是否相等的特殊操作符，对于 NULL 值的比较也会返回 TRUE。它可以用于处理 NULL 值的等值比较。


```
SELECT * FROM employees WHERE commission <=> NULL;
```


6. 注意聚合函数对 NULL 的处理：

在使用聚合函数（如 COUNT, SUM, AVG）时，它们会忽略 NULL 值，因此可能会得到不同于预期的结果。如果希望将 NULL 视为 0，可以使用 COALESCE 或 IFNULL。


```
SELECT AVG(COALESCE(salary, 0)) AS avg_salary FROM employees;
```


这样即使 salary 为 NULL，聚合函数也会将其视为 0。


**

处理 NULL 值时，要特别小心确保查询和操作的语义符合预期。在设计表结构时，也需要考虑 NULL 值的使用场景和合理性。


---


## 在命令提示符中使用 NULL 值


以下实例中假设数据库 RUNOOB 中的表 runoob_test_tbl 含有两列 runoob_author 和 runoob_count, runoob_count 中设置插入NULL值。


### 实例


尝试以下实例:


## 创建数据表 runoob_test_tbl


```sql
root@host# mysql -u root -p password;
Enter password:*******
mysql> use RUNOOB;
Database changed
mysql> create table runoob_test_tbl
    -> (
    -> runoob_author varchar(40) NOT NULL,
    -> runoob_count  INT
    -> );
Query OK, 0 rows affected (0.05 sec)
mysql> INSERT INTO runoob_test_tbl (runoob_author, runoob_count) values ('RUNOOB', 20);
mysql> INSERT INTO runoob_test_tbl (runoob_author, runoob_count) values ('菜鸟教程', NULL);
mysql> INSERT INTO runoob_test_tbl (runoob_author, runoob_count) values ('Google', NULL);
mysql> INSERT INTO runoob_test_tbl (runoob_author, runoob_count) values ('FK', 20);

mysql> SELECT * from runoob_test_tbl;
+---------------+--------------+
| runoob_author | runoob_count |
+---------------+--------------+
| RUNOOB        | 20           |
| 菜鸟教程  | NULL         |
| Google        | NULL         |
| FK            | 20           |
+---------------+--------------+
4 rows in set (0.01 sec)
```


以下实例中你可以看到 = 和 != 运算符是不起作用的：


```sql
mysql> SELECT * FROM runoob_test_tbl WHERE runoob_count = NULL;
Empty set (0.00 sec)
mysql> SELECT * FROM runoob_test_tbl WHERE runoob_count != NULL;
Empty set (0.01 sec)
```


查找数据表中 runoob_test_tbl 列是否为 NULL，必须使用 IS NULL** 和 **IS NOT NULL**，如下实例：


```sql
mysql> SELECT * FROM runoob_test_tbl WHERE runoob_count IS NULL;
+---------------+--------------+
| runoob_author | runoob_count |
+---------------+--------------+
| 菜鸟教程  | NULL         |
| Google        | NULL         |
+---------------+--------------+
2 rows in set (0.01 sec)

mysql> SELECT * from runoob_test_tbl WHERE runoob_count IS NOT NULL;
+---------------+--------------+
| runoob_author | runoob_count |
+---------------+--------------+
| RUNOOB        | 20           |
| FK            | 20           |
+---------------+--------------+
2 rows in set (0.01 sec)
```


---


## 使用 PHP 脚本处理 NULL 值


PHP 脚本中你可以在 if...else 语句来处理变量是否为空，并生成相应的条件语句。


以下实例中 PHP 设置了 $runoob_count 变量，然后使用该变量与数据表中的 runoob_count 字段进行比较：


## MySQL ORDER BY 测试：



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
mysqli_query($conn , "set names utf8");

if( isset($runoob_count ))
{
   $sql = "SELECT runoob_author, runoob_count
           FROM  runoob_test_tbl
           WHERE runoob_count = $runoob_count";
}
else
{
   $sql = "SELECT runoob_author, runoob_count
           FROM  runoob_test_tbl
           WHERE runoob_count IS NULL";
}
mysqli_select_db( $conn, 'RUNOOB' );
$retval = mysqli_query( $conn, $sql );
if(! $retval )
{
    die('无法读取数据: ' . mysqli_error($conn));
}
echo '<h2>菜鸟教程 IS NULL 测试<h2>';
echo '<table border="1"><tr><td>作者</td><td>登陆次数</td></tr>';
while($row = mysqli_fetch_array($retval, MYSQL_ASSOC))
{
    echo "<tr>".
         "<td>{$row['runoob_author']} </td> ".
         "<td>{$row['runoob_count']} </td> ".
         "</tr>";
}
echo '</table>';
mysqli_close($conn);
?>
```


输出结果如下图所示：


```sql

```










	  AI 思考中...





			** [MySQL 连接的使用](https://www.runoob.com/mysql-join.html)
			[MySQL 正则表达式](https://www.runoob.com/mysql-regexp.html) **













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