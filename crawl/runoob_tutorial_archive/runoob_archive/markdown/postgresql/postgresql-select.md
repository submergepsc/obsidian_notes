# PostgreSQL SELECT 语句

- Source: https://www.runoob.com/postgresql/postgresql-select.html

PostgreSQL SELECT 语句用于从数据库中选取数据。


结果被存储在一个结果表中，称为结果集。


### 语法


SELECT 语句语法格式如下：


```
SELECT column1, column2,...columnN FROM table_name;
```


- column1, column2,...columnN 为表中字段名。
- table_name 为表名。


如果我们想读取表中的所有数据可以使用以下 SQL 语句：


```
SELECT * FROM table_name;
```


在上一章节 [INSERT INTO 语句](https://www.runoob.com/postgresql-insert-into.html) 中，我们已经向表 company 插入了一些数据，使用 ***** 号可以读取该表的所有数据：


```
runoobdb=# SELECT * FROM company;

ID        NAME        AGE        ADDRESS     SALARY   JOIN_DATE
----      ----------  -----      ----------  -------      --------
1         Paul        32         California  20000.0      2001-07-13
2         Allen       25         Texas                    2007-12-13
3         Teddy       23         Norway      20000.0
4         Mark        25         Rich-Mond   65000.0      2007-12-13
5         David       27         Texas       85000.0      2007-12-13
```


我们也可以读取指定字段 ID 和 NAME：


```
runoobdb=# SELECT ID,NAME FROM company;
 id | name
----+-------
  1 | Paul
  2 | Allen
  3 | Teddy
  4 | Mark
  5 | David
(5 rows)
```










	  AI 思考中...





			** [PostgreSQL INSERT INTO 语句](https://www.runoob.com/postgresql-insert-into.html)
			[PostgreSQL 运算符](https://www.runoob.com/postgresql-operators.html) **













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