# PostgreSQL ORDER BY 语句

- Source: https://www.runoob.com/postgresql/postgresql-order-by.html

在 PostgreSQL 中，**ORDER BY** 用于对一列或者多列数据进行升序（ASC）或者降序（DESC）排列。


### 语法


**ORDER BY** 子句的基础语法如下：


```
SELECT column-list
FROM table_name
[WHERE condition]
[ORDER BY column1, column2, .. columnN] [ASC | DESC];
```


您可以在 ORDER BY 中使用一列或者多列，但是必须保证要排序的列必须存在。


**ASC** 表示升序，**DESC** 表示降序。


### 实例


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


下面实例将对结果根据 AGE 字段值进行升序排列：


```
runoobdb=# SELECT * FROM COMPANY ORDER BY AGE ASC;
```


得到以下结果：


```
id | name  | age |                      address                       | salary
----+-------+-----+----------------------------------------------------+--------
  6 | Kim   |  22 | South-Hall                                         |  45000
  3 | Teddy |  23 | Norway                                             |  20000
  7 | James |  24 | Houston                                            |  10000
  4 | Mark  |  25 | Rich-Mond                                          |  65000
  2 | Allen |  25 | Texas                                              |  15000
  5 | David |  27 | Texas                                              |  85000
  1 | Paul  |  32 | California                                         |  20000
(7 rows)
```


下面实例将对结果根据 NAME 字段值和 SALARY 字段值进行升序排序：


```
runoobdb=# SELECT * FROM COMPANY ORDER BY NAME, SALARY ASC;
```


得到以下结果：


```
id | name  | age |                      address                       | salary
----+-------+-----+----------------------------------------------------+--------
  2 | Allen |  25 | Texas                                              |  15000
  5 | David |  27 | Texas                                              |  85000
  7 | James |  24 | Houston                                            |  10000
  6 | Kim   |  22 | South-Hall                                         |  45000
  4 | Mark  |  25 | Rich-Mond                                          |  65000
  1 | Paul  |  32 | California                                         |  20000
  3 | Teddy |  23 | Norway                                             |  20000
(7 rows)
```


下面实例将对结果根据NAME字段值进行降序排列：


```
runoobdb=# SELECT * FROM COMPANY ORDER BY NAME DESC;
```


得到以下结果：


```
id | name  | age |                      address                       | salary
----+-------+-----+----------------------------------------------------+--------
  3 | Teddy |  23 | Norway                                             |  20000
  1 | Paul  |  32 | California                                         |  20000
  4 | Mark  |  25 | Rich-Mond                                          |  65000
  6 | Kim   |  22 | South-Hall                                         |  45000
  7 | James |  24 | Houston                                            |  10000
  5 | David |  27 | Texas                                              |  85000
  2 | Allen |  25 | Texas                                              |  15000
(7 rows)
```










	  AI 思考中...





			** [PostgreSQL LIMIT 子句](https://www.runoob.com/postgresql-limit.html)
			[PostgreSQL GROUP BY 语句](https://www.runoob.com/postgresql-group-by.html) **













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