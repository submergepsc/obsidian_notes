# SQL CREATE TABLE 语句

- Source: https://www.runoob.com/sql/sql-create-table.html

---


## SQL CREATE TABLE 语句


CREATE TABLE 语句用于创建数据库中的表。


表由行和列组成，每个表都必须有个表名。


### SQL CREATE TABLE 语法


CREATE TABLE *table_name***
(
*column_name1 data_type*(*size*),
*column_name2 data_type*(*size*),
*column_name3 data_type*(*size*),

....

);


column_name 参数规定表中列的名称。


data_type 参数规定列的数据类型（例如 varchar、integer、decimal、date 等等）。


size 参数规定表中列的最大长度。


提示：**如需了解 MS Access、MySQL 和 SQL Server 中可用的数据类型，请访问我们完整的 [数据类型参考手册](https://www.runoob.com/sql-datatypes.html)。


---


## SQL CREATE TABLE 实例


现在我们想要创建一个名为 "Persons" 的表，包含五列：PersonID、LastName、FirstName、Address 和 City。


我们使用下面的 CREATE TABLE 语句：


## 实例


```sql
CREATE TABLE Persons
(
PersonID int,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255)
);
```


PersonID 列的数据类型是 int，包含整数。


LastName、FirstName、Address 和 City 列的数据类型是 varchar，包含字符，且这些字段的最大长度为 255 个字符。


空的 "Persons" 表如下所示：


| PersonID | LastName | FirstName | Address | City |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


**提示：**可使用 INSERT INTO 语句向空表写入数据。








	  AI 思考中...





			** [SQL CREATE DATABASE 语句](https://www.runoob.com/sql-create-db.html)
			[SQL 约束](https://www.runoob.com/sql-constraints.html) **













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