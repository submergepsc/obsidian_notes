# PostgreSQL 模式（SCHEMA）

- Source: https://www.runoob.com/postgresql/postgresql-schema.html

PostgreSQL 模式（SCHEMA）可以看着是一个表的集合。


一个模式可以包含视图、索引、数据类型、函数和操作符等。


相同的对象名称可以被用于不同的模式中而不会出现冲突，例如 schema1 和 myschema 都可以包含名为 mytable 的表。


使用模式的优势：


- 允许多个用户使用一个数据库并且不会互相干扰。
- 将数据库对象组织成逻辑组以便更容易管理。
- 第三方应用的对象可以放在独立的模式中，这样它们就不会与其他对象的名称发生冲突。


模式类似于操作系统层的目录，但是模式不能嵌套。


### 语法


我们可以使用 **CREATE SCHEMA ** 语句来创建模式，语法格式如下：


```
CREATE SCHEMA myschema (
...
);
```


上述语句将创建一个名为 myschema 的模式。

模式通常用于组织和隔离数据库对象，防止对象名称冲突。


创建表（Table）使用 CREATE TABLE 语句:


```
CREATE TABLE myschema.mytable (
    column1 datatype1,
    column2 datatype2,
    ...
);
```


上述语句将在 myschema 模式下创建一个名为 mytable 的表，并定义了一系列的列及其数据类型。

请注意，上述的 datatype1, datatype2 等应该被替换为实际的数据类型，例如 integer, varchar(255), 等等。


### 实例


接下来我们连接到 runoobdb 来创建模式 myschema：


```
runoobdb=# create schema myschema;
CREATE SCHEMA
```


输出结果 "CREATE SCHEMA" 就代表模式创建成功。


接下来我们再创建一个表格：


```
runoobdb=# create table myschema.company(
   ID   INT              NOT NULL,
   NAME VARCHAR (20)     NOT NULL,
   AGE  INT              NOT NULL,
   ADDRESS  CHAR (25),
   SALARY   DECIMAL (18, 2),
   PRIMARY KEY (ID)
);
```


以上命令创建了一个空的表格，我们使用以下 SQL 来查看表格是否创建：


```
runoobdb=# select * from myschema.company;
 id | name | age | address | salary
----+------+-----+---------+--------
(0 rows)
```


### 删除模式


删除一个为空的模式（其中的所有对象已经被删除）：


```
DROP SCHEMA myschema;
```


删除一个模式以及其中包含的所有对象：


```
DROP SCHEMA myschema CASCADE;
```










	  AI 思考中...





			** [PostgreSQL 删除表格](https://www.runoob.com/postgresql-drop-table.html)
			[PostgreSQL INSERT INTO 语句](https://www.runoob.com/postgresql-insert-into.html) **













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