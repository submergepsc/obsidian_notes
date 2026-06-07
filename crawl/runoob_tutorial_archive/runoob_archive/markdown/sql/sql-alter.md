# SQL ALTER TABLE 语句

- Source: https://www.runoob.com/sql/sql-alter.html

---


## ALTER TABLE 语句


ALTER TABLE 语句用于在已有的表中添加、删除或修改列。


### SQL ALTER TABLE 语法


如需在表中添加列，请使用下面的语法:


ALTER TABLE table_name**
ADD column_name datatype


如需删除表中的列，请使用下面的语法（请注意，某些数据库系统不允许这种在数据库表中删除列的方式）：


ALTER TABLE table_name

DROP COLUMN column_name


要改变表中列的数据类型，请使用下面的语法：


SQL Server / MS Access：**


ALTER TABLE table_name**
ALTER COLUMN column_name datatype


My SQL / Oracle：**


ALTER TABLE table_name**
MODIFY COLUMN column_name datatype

Oracle 10G 之后版本:


```
ALTER TABLE table_name
MODIFY column_name datatype;
```


---


## SQL ALTER TABLE 实例


请看 "Persons" 表：


| P_Id | LastName | FirstName | Address | City |
| --- | --- | --- | --- | --- |
| 1 | Hansen | Ola | Timoteivn 10 | Sandnes |
| 2 | Svendson | Tove | Borgvn 23 | Sandnes |
| 3 | Pettersen | Kari | Storgt 20 | Stavanger |


现在，我们想在 "Persons" 表中添加一个名为 "DateOfBirth" 的列。


我们使用下面的 SQL 语句：


ALTER TABLE Persons

ADD DateOfBirth date


请注意，新列 "DateOfBirth" 的类型是 date，可以存放日期。数据类型规定列中可以存放的数据的类型。如需了解 MS Access、MySQL 和 SQL Server 中可用的数据类型，请访问我们完整的 [数据类型参考手册](https://www.runoob.com/sql-datatypes.html)。


现在，"Persons" 表将如下所示：


| P_Id | LastName | FirstName | Address | City | DateOfBirth |
| --- | --- | --- | --- | --- | --- |
| 1 | Hansen | Ola | Timoteivn 10 | Sandnes |  |
| 2 | Svendson | Tove | Borgvn 23 | Sandnes |  |
| 3 | Pettersen | Kari | Storgt 20 | Stavanger |  |


---


## 改变数据类型实例


现在，我们想要改变 "Persons" 表中 "DateOfBirth" 列的数据类型。


我们使用下面的 SQL 语句：


ALTER TABLE Persons

ALTER COLUMN DateOfBirth year


请注意，现在 "DateOfBirth" 列的类型是 year，可以存放 2 位或 4 位格式的年份。


---


## DROP COLUMN 实例


接下来，我们想要删除 "Person" 表中的 "DateOfBirth" 列。


我们使用下面的 SQL 语句：


ALTER TABLE Persons

DROP COLUMN DateOfBirth


现在，"Persons" 表将如下所示：


| P_Id | LastName | FirstName | Address | City |
| --- | --- | --- | --- | --- |
| 1 | Hansen | Ola | Timoteivn 10 | Sandnes |
| 2 | Svendson | Tove | Borgvn 23 | Sandnes |
| 3 | Pettersen | Kari | Storgt 20 | Stavanger |










	  AI 思考中...





			** [SQL 撤销索引、表以及数据库](https://www.runoob.com/sql-drop.html)
			[SQL AUTO INCREMENT 字段](https://www.runoob.com/sql-autoincrement.html) **













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