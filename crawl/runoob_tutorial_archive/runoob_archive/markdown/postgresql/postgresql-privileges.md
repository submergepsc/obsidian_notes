# PostgreSQL PRIVILEGES（权限）

- Source: https://www.runoob.com/postgresql/postgresql-privileges.html

无论何时创建数据库对象，都会为其分配一个所有者，所有者通常是执行 create 语句的人。


对于大多数类型的对象，初始状态是只有所有者(或超级用户)才能修改或删除对象。要允许其他角色或用户使用它，必须为该用户设置权限。


在 PostgreSQL 中，权限分为以下几种：


- SELECT
- INSERT
- UPDATE
- DELETE
- TRUNCATE
- REFERENCES
- TRIGGER
- CREATE
- CONNECT
- TEMPORARY
- EXECUTE
- USAGE


根据对象的类型(表、函数等)，将指定权限应用于该对象。


要向用户分配权限，可以使用 GRANT 命令。


### GRANT 语法


GRANT 命令的基本语法如下：


```
GRANT privilege [, ...]
ON object [, ...]
TO { PUBLIC | GROUP group | username }
```


- privilege − 值可以为：SELECT，INSERT，UPDATE，DELETE， RULE，ALL。
- object − 要授予访问权限的对象名称。可能的对象有： table， view，sequence。
- PUBLIC − 表示所有用户。
- GROUP group − 为用户组授予权限。
- username − 要授予权限的用户名。PUBLIC 是代表所有用户的简短形式。


另外，我们可以使用 REVOKE 命令取消权限，REVOKE 语法：


```
REVOKE privilege [, ...]
ON object [, ...]
FROM { PUBLIC | GROUP groupname | username }
```


### 实例


为了理解权限，创建一个用户：


```
runoobdb=# CREATE USER runoob WITH PASSWORD 'password';
CREATE ROLE
```


信息 CREATE ROLE 表示创建了一个用户 "runoob"。


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


现在给用户 "runoob" 分配权限：


```
runoobdb=# GRANT ALL ON COMPANY TO runoob;
GRANT
```


信息 GRANT 表示所有权限已经分配给了 "runoob"。


下面撤销用户 "runoob" 的权限：


```
runoobdb=# REVOKE ALL ON COMPANY FROM runoob;
REVOKE
```


信息 REVOKE 表示已经将用户的权限撤销。


你也可以删除用户：


```
runoobdb=# DROP USER runoob;
DROP ROLE
```


信息 DROP ROLE 表示用户 "runoob" 已经从数据库中删除。








	  AI 思考中...





			** [PostgreSQL AUTO INCREMENT（自动增长）](https://www.runoob.com/postgresql-autoincrement.html)
			[PostgreSQL 时间/日期函数和操作符](https://www.runoob.com/postgresql-datetime.html) **













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