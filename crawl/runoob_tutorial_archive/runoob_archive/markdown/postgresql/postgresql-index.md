# PostgreSQL 索引

- Source: https://www.runoob.com/postgresql/postgresql-index.html

索引是加速搜索引擎检索数据的一种特殊表查询。简单地说，索引是一个指向表中数据的指针。一个数据库中的索引与一本书的索引目录是非常相似的。


拿汉语字典的目录页（索引）打比方，我们可以按拼音、笔画、偏旁部首等排序的目录（索引）快速查找到需要的字。


索引有助于加快 SELECT 查询和 WHERE 子句，但它会减慢使用 UPDATE 和 INSERT 语句时的数据输入。索引可以创建或删除，但不会影响数据。


使用 CREATE INDEX 语句创建索引，它允许命名索引，指定表及要索引的一列或多列，并指示索引是升序排列还是降序排列。


索引也可以是唯一的，与 UNIQUE 约束类似，在列上或列组合上防止重复条目。


### CREATE INDEX 命令


CREATE INDEX （创建索引）的语法如下：


```
CREATE INDEX index_name ON table_name;
```


### 索引类型


**单列索引**


单列索引是一个只基于表的一个列上创建的索引，基本语法如下：


```
CREATE INDEX index_name
ON table_name (column_name);
```


**组合索引**


组合索引是基于表的多列上创建的索引，基本语法如下：


```
CREATE INDEX index_name
ON table_name (column1_name, column2_name);
```


不管是单列索引还是组合索引，该索引必须是在 WHERE 子句的过滤条件中使用非常频繁的列。


如果只有一列被使用到，就选择单列索引，如果有多列就使用组合索引。


**唯一索引**


使用唯一索引不仅是为了性能，同时也为了数据的完整性。唯一索引不允许任何重复的值插入到表中。基本语法如下：


```
CREATE UNIQUE INDEX index_name
on table_name (column_name);
```


**局部索引**


局部索引 是在表的子集上构建的索引；子集由一个条件表达式上定义。索引只包含满足条件的行。基础语法如下：


```
CREATE INDEX index_name
ON table_name(column_list)
WHERE condition;
```


在这里，index_name 是你想要创建的索引的名称，table_name 是包含你想要索引的列的表的名称，column_list 是你想要索引的列的列表，而 condition 是一个布尔表达式，用于定义哪些行将被包含在索引中。


**隐式索引**


在 PostgreSQL 中，隐式索引是在创建对象时，由数据库服务器自动创建的索引。这类索引通常为主键约束和唯一约束自动创建。当在创建表时声明一个列为主键、唯一约束或外键时，PostgreSQL 会自动为该列创建一个隐式索引。这样做的好处是简化了索引管理，并且提高了数据库的性能。


例如，如果在创建一个名为 "users" 的表时，声明了一个名为 "userid" 的列为主键，PostgreSQL会自动为 "userid" 列创建一个隐式索引，这意味着在插入新记录时，数据库会自动为 "userid" 列生成一个唯一的索引值。


隐式索引的创建和管理是由 PostgreSQL 自动完成的，用户不需要手动干预，这使得数据库管理变得更加简单和高效。


### 实例


下面实例将在 COMPANY 表的 SALARY 列上创建索引：


```
# CREATE INDEX salary_index ON COMPANY (salary);
```


现在，用 **\d company** 命令列出 COMPANY 表的所有索引：


```
# \d company
```


得到的结果如下，company_pkey 是隐式索引 ，是表创建表时创建的：


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
    "salary_index" btree (salary)
```


你可以使用 **\di** 命令列出数据库中所有索引：


```
runoobdb=# \di
                    List of relations
 Schema |      Name       | Type  |  Owner   |   Table
--------+-----------------+-------+----------+------------
 public | company_pkey    | index | postgres | company
 public | department_pkey | index | postgres | department
 public | salary_index    | index | postgres | company
(3 rows)
```


### DROP INDEX （删除索引）


一个索引可以使用 PostgreSQL 的 DROP 命令删除。


```
DROP INDEX index_name;
```


您可以使用下面的语句来删除之前创建的索引：


```
# DROP INDEX salary_index;
```


删除后，可以看到 salary_index 已经在索引的列表中被删除：


```
runoobdb=# \di
                    List of relations
 Schema |      Name       | Type  |  Owner   |   Table
--------+-----------------+-------+----------+------------
 public | company_pkey    | index | postgres | company
 public | department_pkey | index | postgres | department
(2 rows)
```


### 什么情况下要避免使用索引？


虽然索引的目的在于提高数据库的性能，但这里有几个情况需要避免使用索引。


使用索引时，需要考虑下列准则：


- 索引不应该使用在较小的表上。
- 索引不应该使用在有频繁的大批量的更新或插入操作的表上。
- 索引不应该使用在含有大量的 NULL 值的列上。
- 索引不应该使用在频繁操作的列上。








	  AI 思考中...





			** [PostgreSQL 触发器](https://www.runoob.com/postgresql-trigger.html)
			[PostgreSQL ALTER TABLE 命令](https://www.runoob.com/postgresql-alter-table.html) **













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