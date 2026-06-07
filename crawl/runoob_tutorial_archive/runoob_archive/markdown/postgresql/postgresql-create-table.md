# PostgreSQL 创建表格

- Source: https://www.runoob.com/postgresql/postgresql-create-table.html

PostgreSQL 使用 CREATE TABLE 语句来创建数据库表格。


### 语法


**CREATE TABLE** 语法格式如下：


```
CREATE TABLE table_name(
   column1 datatype,
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
   PRIMARY KEY( 一个或多个列 )
);
```


**CREATE TABLE** 是一个关键词，用于告诉数据库系统将创建一个数据表。


表名字必需在同一模式中的其它表、 序列、索引、视图或外部表名字中唯一。


**CREATE TABLE** 在当前数据库创建一个新的空白表，该表将由发出此命令的用户所拥有。


表格中的每个字段都会定义数据类型，如下：


### 实例


以下创建了一个表，表名为 **COMPANY** 表格，主键为 **ID**，**NOT NULL** 表示字段不允许包含 **NULL** 值：


```
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
```


接下来我们再创建一个表格，在后面章节会用到：


```
CREATE TABLE DEPARTMENT(
   ID INT PRIMARY KEY      NOT NULL,
   DEPT           CHAR(50) NOT NULL,
   EMP_ID         INT      NOT NULL
);
```


我们可以使用 **\d** 命令来查看表格是否创建成功：


```
runoobdb=# \d
           List of relations
 Schema |    Name    | Type  |  Owner
--------+------------+-------+----------
 public | company    | table | postgres
 public | department | table | postgres
(2 rows)
```


**\d tablename** 查看表格信息：


```
runoobdb=# \d company
                  Table "public.company"
 Column  |     Type      | Collation | Nullable | Default
---------+---------------+-----------+----------+---------
 id      | integer       |           | not null |
 name    | text          |           | not null |
 age     | integer       |           | not null |
 address | character(50) |           |          |
 salary  | real          |           |          |
Indexes:
    "company_pkey" PRIMARY KEY, btree (id)
```










	  AI 思考中...





			** [PostgreSQL 删除数据库](https://www.runoob.com/postgresql-drop-database.html)
			[PostgreSQL 删除表格](https://www.runoob.com/postgresql-drop-table.html) **













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