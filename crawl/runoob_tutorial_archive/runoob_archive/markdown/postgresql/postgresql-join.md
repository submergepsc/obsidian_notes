# PostgreSQL 连接(JOIN)

- Source: https://www.runoob.com/postgresql/postgresql-join.html

PostgreSQL JOIN 子句用于把来自两个或多个表的行结合起来，基于这些表之间的共同字段。


在 PostgreSQL 中，JOIN 有五种连接类型：


- CROSS JOIN ：交叉连接
- INNER JOIN：内连接
- LEFT OUTER JOIN：左外连接
- RIGHT OUTER JOIN：右外连接
- FULL OUTER JOIN：全外连接


接下来让我们创建两张表 **COMPANY** 和 **DEPARTMENT**。


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


我们往表里添加几条数据：


```
INSERT INTO COMPANY VALUES (8, 'Paul', 24, 'Houston', 20000.00);
INSERT INTO COMPANY VALUES (9, 'James', 44, 'Norway', 5000.00);
INSERT INTO COMPANY VALUES (10, 'James', 45, 'Texas', 5000.00);
```


此时，COMPANY 表的记录如下：


```
id | name  | age | address      | salary
 ----+-------+-----+--------------+--------
   1 | Paul  |  32 | California   |  20000
   2 | Allen |  25 | Texas        |  15000
   3 | Teddy |  23 | Norway       |  20000
   4 | Mark  |  25 | Rich-Mond    |  65000
   5 | David |  27 | Texas        |  85000
   6 | Kim   |  22 | South-Hall   |  45000
   7 | James |  24 | Houston      |  10000
   8 | Paul  |  24 | Houston      |  20000
   9 | James |  44 | Norway       |   5000
  10 | James |  45 | Texas        |   5000
(10 rows)
```


创建一张 DEPARTMENT 表，添加三个字段：


```
CREATE TABLE DEPARTMENT(
   ID INT PRIMARY KEY      NOT NULL,
   DEPT           CHAR(50) NOT NULL,
   EMP_ID         INT      NOT NULL
);
```


向 DEPARTMENT 表插入三条记录：


```
INSERT INTO DEPARTMENT (ID, DEPT, EMP_ID) VALUES (1, 'IT Billing', 1 );

INSERT INTO DEPARTMENT (ID, DEPT, EMP_ID) VALUES (2, 'Engineering', 2 );

INSERT INTO DEPARTMENT (ID, DEPT, EMP_ID) VALUES (3, 'Finance', 7 );
```


此时，DEPARTMENT 表的记录如下：


```
id | dept        | emp_id
----+-------------+--------
  1 | IT Billing  |  1
  2 | Engineering |  2
  3 | Finance     |  7
```


---


## 交叉连接


交叉连接（CROSS JOIN）把第一个表的每一行与第二个表的每一行进行匹配。如果两个输入表分别有 x 和 y 行，则结果表有 x*y 行。


由于交叉连接（CROSS JOIN）有可能产生非常大的表，使用时必须谨慎，只在适当的时候使用它们。


下面是 CROSS JOIN 的基础语法：


```
SELECT ... FROM table1 CROSS JOIN table2 ...
```


基于上面的表，我们可以写一个交叉连接（CROSS JOIN），如下所示：


```
runoobdb=# SELECT EMP_ID, NAME, DEPT FROM COMPANY CROSS JOIN DEPARTMENT;
```


得到结果如下：


```
runoobdb=# SELECT EMP_ID, NAME, DEPT FROM COMPANY CROSS JOIN DEPARTMENT;
 emp_id | name  |       dept
--------+-------+--------------------
      1 | Paul  | IT Billing
      1 | Allen | IT Billing
      1 | Teddy | IT Billing
      1 | Mark  | IT Billing
      1 | David | IT Billing
      1 | Kim   | IT Billing
      1 | James | IT Billing
      1 | Paul  | IT Billing
      1 | James | IT Billing
      1 | James | IT Billing
      2 | Paul  | Engineering
      2 | Allen | Engineering
      2 | Teddy | Engineering
      2 | Mark  | Engineering
      2 | David | Engineering
      2 | Kim   | Engineering
      2 | James | Engineering
      2 | Paul  | Engineering
      2 | James | Engineering
      2 | James | Engineering
      7 | Paul  | Finance
```


---


## 内连接


内连接（INNER JOIN）根据连接谓词结合两个表（table1 和 table2）的列值来创建一个新的结果表。查询会把 table1 中的每一行与 table2 中的每一行进行比较，找到所有满足连接谓词的行的匹配对。


当满足连接谓词时，A 和 B 行的每个匹配对的列值会合并成一个结果行。


内连接（INNER JOIN）是最常见的连接类型，是默认的连接类型。


INNER 关键字是可选的。


下面是内连接（INNER JOIN）的语法：


```
SELECT table1.column1, table2.column2...
FROM table1
INNER JOIN table2
ON table1.common_filed = table2.common_field;
```


基于上面的表，我们可以写一个内连接，如下所示：


```
runoobdb=# SELECT EMP_ID, NAME, DEPT FROM COMPANY INNER JOIN DEPARTMENT ON COMPANY.ID = DEPARTMENT.EMP_ID;
 emp_id | name  |        dept
--------+-------+--------------
      1 | Paul  | IT Billing
      2 | Allen | Engineering
      7 | James | Finance
(3 rows)
```


---


## 左外连接


外部连接是内部连接的扩展。SQL 标准定义了三种类型的外部连接: LEFT、RIGHT 和 FULL, PostgreSQL 支持所有这些。

对于左外连接，首先执行一个内连接。然后，对于表 T1 中不满足表 T2 中连接条件的每一行，其中 T2 的列中有 null 值也会添加一个连接行。因此，连接的表在 T1 中每一行至少有一行。


下面是左外连接（ LEFT OUTER JOIN ）的基础语法：


```
SELECT ... FROM table1 LEFT OUTER JOIN table2 ON conditional_expression ...
```


基于上面两张表，我们可以写个左外连接，如下：


```
runoobdb=# SELECT EMP_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT ON COMPANY.ID = DEPARTMENT.EMP_ID;
 emp_id | name  |      dept
--------+-------+----------------
      1 | Paul  | IT Billing
      2 | Allen | Engineering
      7 | James | Finance
        | James |
        | David |
        | Paul  |
        | Kim   |
        | Mark  |
        | Teddy |
        | James |
(10 rows)
```


---


## 右外连接


首先，执行内部连接。然后，对于表T2中不满足表T1中连接条件的每一行，其中T1列中的值为空也会添加一个连接行。这与左联接相反;对于T2中的每一行，结果表总是有一行。


下面是右外连接（ RIGHT OUT JOIN）的基本语法：


```
SELECT ... FROM table1 RIGHT OUTER JOIN table2 ON conditional_expression ...
```


基于上面两张表，我们建立一个右外连接：


```
runoobdb=# SELECT EMP_ID, NAME, DEPT FROM COMPANY RIGHT OUTER JOIN DEPARTMENT ON COMPANY.ID = DEPARTMENT.EMP_ID;
 emp_id | name  |    dept
--------+-------+-----------------
      1 | Paul  | IT Billing
      2 | Allen | Engineering
      7 | James | Finance
(3 rows)
```


---


## 外连接


首先，执行内部连接。然后，对于表 T1 中不满足表 T2 中任何行连接条件的每一行，如果 T2 的列中有 null 值也会添加一个到结果中。此外，对于 T2 中不满足与 T1 中的任何行连接条件的每一行，将会添加 T1 列中包含 null 值的到结果中。


下面是外连接的基本语法：


```
SELECT ... FROM table1 FULL OUTER JOIN table2 ON conditional_expression ...
```


基于上面两张表，可以建立一个外连接：


```
runoobdb=# SELECT EMP_ID, NAME, DEPT FROM COMPANY FULL OUTER JOIN DEPARTMENT ON COMPANY.ID = DEPARTMENT.EMP_ID;
 emp_id | name  |      dept
--------+-------+-----------------
      1 | Paul  | IT Billing
      2 | Allen | Engineering
      7 | James | Finance
        | James |
        | David |
        | Paul  |
        | Kim   |
        | Mark  |
        | Teddy |
        | James |
(10 rows)
```










	  AI 思考中...





			** [PostgreSQL 约束](https://www.runoob.com/postgresql-constraints.html)
			[PostgreSQL UNION 操作符](https://www.runoob.com/postgresql-union.html) **













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