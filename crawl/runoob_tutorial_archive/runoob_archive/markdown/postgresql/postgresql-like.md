# PostgreSQL LIKE 子句

- Source: https://www.runoob.com/postgresql/postgresql-like.html

在 PostgreSQL 数据库中，我们如果要获取包含某些字符的数据，可以使用 **LIKE** 子句。


在 LIKE 子句中，通常与通配符结合使用，通配符表示任意字符，在 PostgreSQL 中，主要有以下两种通配符：


- 百分号 **%**
- 下划线 **_**


如果没有使用以上两种通配符，LIKE 子句和等号 **=** 得到的结果是一样的。


### 语法


以下是使用 LIKE 子句搭配百分号 **%** 和下划线 **_** 从数据库中获取数据的通用语法：


```
SELECT FROM table_name WHERE column LIKE 'XXXX%';
或者
SELECT FROM table_name WHERE column LIKE '%XXXX%';
或者
SELECT FROM table_name WHERE column LIKE 'XXXX_';
或者
SELECT FROM table_name WHERE column LIKE '_XXXX';
或者
SELECT FROM table_name WHERE column LIKE '_XXXX_';
```


你可以在 WHERE 子句中指定任何条件。


你可以使用 AND 或者 OR 指定一个或多个条件。


**XXXX** 可以是任何数字或者字符。


### 实例


下面是 LIKE 语句中演示了 **%** 和 **_** 的一些差别:


| 实例 | 描述 |
| --- | --- |
| WHERE SALARY::text LIKE '200%' | 找出 SALARY 字段中以 200 开头的数据。 |
| WHERE SALARY::text LIKE '%200%' | 找出 SALARY 字段中含有 200 字符的数据。 |
| WHERE SALARY::text LIKE '_00%' | 找出 SALARY 字段中在第二和第三个位置上有 00 的数据。 |
| WHERE SALARY::text LIKE '2_%_%' | 找出 SALARY 字段中以 2 开头的字符长度大于 3 的数据。 |
| WHERE SALARY::text LIKE '%2' | 找出 SALARY 字段中以 2 结尾的数据 |
| WHERE SALARY::text LIKE '_2%3' | 找出 SALARY 字段中 2 在第二个位置上并且以 3 结尾的数据 |
| WHERE SALARY::text LIKE '2___3' | 找出 SALARY 字段中以 2 开头，3 结尾并且是 5 位数的数据 |


在 PostgreSQL 中，LIKE 子句是只能用于对字符进行比较，因此在上面例子中，我们要将整型数据类型转化为字符串数据类型。


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


下面实例将找出 AGE 以 2 开头的数据：


```
runoobdb=# SELECT * FROM COMPANY WHERE AGE::text LIKE '2%';
```


得到以下结果：


```
id | name  | age | address     | salary
----+-------+-----+-------------+--------
  2 | Allen |  25 | Texas       |  15000
  3 | Teddy |  23 | Norway      |  20000
  4 | Mark  |  25 | Rich-Mond   |  65000
  5 | David |  27 | Texas       |  85000
  6 | Kim   |  22 | South-Hall  |  45000
  7 | James |  24 | Houston     |  10000
  8 | Paul  |  24 | Houston     |  20000
(7 rows)
```


下面实例将找出 address 字段中含有 **-** 字符的数据：


```
runoobdb=# SELECT * FROM COMPANY WHERE ADDRESS  LIKE '%-%';
```


得到结果如下：


```
id | name | age |                      address              | salary
----+------+-----+-------------------------------------------+--------
  4 | Mark |  25 | Rich-Mond                                 |  65000
  6 | Kim  |  22 | South-Hall                                |  45000
(2 rows)
```










	  AI 思考中...





			** [PostgreSQL DELETE 语句](https://www.runoob.com/postgresql-delete.html)
			[PostgreSQL LIMIT 子句](https://www.runoob.com/postgresql-limit.html) **













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