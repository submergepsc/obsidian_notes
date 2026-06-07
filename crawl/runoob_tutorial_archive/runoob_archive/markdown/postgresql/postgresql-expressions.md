# PostgreSQL 表达式

- Source: https://www.runoob.com/postgresql/postgresql-expressions.html

表达式是由一个或多个的值、运算符、PostgresSQL 函数组成的。


PostgreSQL 表达式类似一个公式，我们可以将其应用在查询语句中，用来查找数据库中指定条件的结果集。


### 语法


SELECT 语句的语法格式如下：


```
SELECT column1, column2, columnN
FROM table_name
WHERE [CONDITION | EXPRESSION];
```


PostgreSQL 的表达式可以有不同类型，我们接下来会讲到。


### 布尔表达式


布尔表达式是根据一个指定条件来读取数据：


```
SELECT column1, column2, columnN
FROM table_name
WHERE SINGLE VALUE MATCHTING EXPRESSION;
```


创建 COMPANY 表（[下载 COMPANY SQL 文件](https://static.jyshare.com/download/company.sql) ），数据内容如下：


```
runoobdb# select * from COMPANY;
 id | name  | age | address   | salary
----+-------+-----+-----------+--------
  1 | Paul  |  32 | California|  20000
  2 | Allen |  25 | Texas     |  15000
  3 | Teddy |  23 | Norway    |  20000
  4 | Mark  |  25 | Rich-Mond |  65000
  5 | David |  27 | Texas     |  85000
  6 | Kim   |  22 | South-Hall|  45000
  7 | James |  24 | Houston   |  10000
(7 rows)
```


以下使用了布尔表达式（**SALARY=10000**）来查询数据：


```
runoobdb=# SELECT * FROM COMPANY WHERE SALARY = 10000;
 id | name  | age | address  | salary
----+-------+-----+----------+--------
  7 | James |  24 | Houston  |  10000
(1 row)
```


### 数字表达式


数字表达式常用于查询语句中的数学运算：


```
SELECT numerical_expression as  OPERATION_NAME
[FROM table_name WHERE CONDITION] ;
```


**numerical_expression** 是一个数学运算表达式，实例如下：


```
runoobdb=# SELECT (17 + 6) AS ADDITION ;
 addition
----------
       23
(1 row)
```


此外 PostgreSQL 还内置了一些数学函数，如：


- avg() ： 返回一个表达式的平均值
- sum() ： 返回指定字段的总和
- count() ： 返回查询的记录总数


以下实例查询 COMPANY 表的记录总数：


```
runoobdb=# SELECT COUNT(*) AS "RECORDS" FROM COMPANY;
 RECORDS
---------
       7
(1 row)
```


### 日期表达式


日期表达式返回当前系统的日期和时间，可用于各种数据操作，以下实例查询当前时间：


```
runoobdb=# SELECT CURRENT_TIMESTAMP;
       current_timestamp
-------------------------------
 2019-06-13 10:49:06.419243+08
(1 row)
```










	  AI 思考中...





			** [PostgreSQL 运算符](https://www.runoob.com/postgresql-operators.html)
			[PostgreSQL WHERE 子句](https://www.runoob.com/postgresql-where-clause.html) **













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