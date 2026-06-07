# SQL SELECT INTO 语句

- Source: https://www.runoob.com/sql/sql-select-into.html

---


通过 SQL，您可以从一个表复制信息到另一个表。


SELECT INTO 语句从一个表复制数据，然后把数据插入到另一个新表中。


---


## SQL SELECT INTO 语句


SELECT INTO 语句从一个表复制数据，然后把数据插入到另一个新表中。


**

注意：**


MySQL 数据库不支持 SELECT ... INTO 语句，但支持 [INSERT INTO ... SELECT](https://www.runoob.com/sql-insert-into-select.html) 。


当然你可以使用以下语句来拷贝表结构及数据：


```
CREATE TABLE 新表
AS
SELECT * FROM 旧表
```


### SQL SELECT INTO 语法

假设有一个名为 employees 的表，包含以下数据：


| EmployeeID | FirstName | LastName | Age | Department |
| --- | --- | --- | --- | --- |
| 1 | John | Doe | 30 | Sales |
| 2 | Jane | Smith | 25 | HR |
| 3 | Sam | Brown | 28 | IT |

要创建一个名为 `employees_backup` 的新表，并将 `employees` 表中的所有数据插入到新表中，可以使用以下 SQL 语句：


```
SELECT *
INTO employees_backup
FROM employees;
```


执行此语句后，新的 `employees_backup` 表将仅包含年龄大于 25 岁的员工的数据。


```
SELECT EmployeeID, FirstName, LastName, Age, Department
INTO employees_backup
FROM employees
WHERE Age > 25;
```


### 使用注意事项



**表结构**：


- `SELECT INTO` 会创建一个新表，并且新表的结构将基于选择的列和数据类型。
- 如果新表已经存在，`SELECT INTO` 语句将失败。在这种情况下，可以使用 `INSERT INTO ... SELECT` 语句。



**数据库支持**：


- `SELECT INTO` 语句在 SQL Server 中非常常用，但在 MySQL 和 PostgreSQL 中通常使用 `CREATE TABLE ... AS SELECT` 语句。


---


## 在其他数据库中的替代方案


### MySQL 和 PostgreSQL


在 MySQL 和 PostgreSQL 中，可以使用 `CREATE TABLE ... AS SELECT` 来实现类似的功能：


```
CREATE TABLE employees_backup AS
SELECT EmployeeID, FirstName, LastName, Age, Department
FROM employees
WHERE Age > 25;
```










	  AI 思考中...





			** [SQL UNION 操作符](https://www.runoob.com/sql-union.html)
			[SQL INSERT INTO SELECT 语句](https://www.runoob.com/sql-insert-into-select.html) **













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