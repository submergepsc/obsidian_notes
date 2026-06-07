# SQL Date 函数

- Source: https://www.runoob.com/sql/sql-dates.html

---


## SQL 日期（Dates）


![Note](https://www.runoob.com/images/lamp.gif)当我们处理日期时，最难的任务恐怕是确保所插入的日期的格式，与数据库中日期列的格式相匹配。


只要您的数据包含的只是日期部分，运行查询就不会出问题。但是，如果涉及时间部分，情况就有点复杂了。


在讨论日期查询的复杂性之前，我们先来看看最重要的内建日期处理函数。


---


## MySQL Date 函数


下面的表格列出了 MySQL 中最重要的内建日期函数：


| 函数 | 描述 |
| --- | --- |
| NOW() | 返回当前的日期和时间 |
| CURDATE() | 返回当前的日期 |
| CURTIME() | 返回当前的时间 |
| DATE() | 提取日期或日期/时间表达式的日期部分 |
| EXTRACT() | 返回日期/时间的单独部分 |
| DATE_ADD() | 向日期添加指定的时间间隔 |
| DATE_SUB() | 从日期减去指定的时间间隔 |
| DATEDIFF() | 返回两个日期之间的天数 |
| DATE_FORMAT() | 用不同的格式显示日期/时间 |

**
---


## SQL Server Date 函数


下面的表格列出了 SQL Server 中最重要的内建日期函数：


| 函数 | 描述 |
| --- | --- |
| GETDATE() | 返回当前的日期和时间 |
| DATEPART() | 返回日期/时间的单独部分 |
| DATEADD() | 在日期中添加或减去指定的时间间隔 |
| DATEDIFF() | 返回两个日期之间的时间 |
| CONVERT() | 用不同的格式显示日期/时间 |


---


## SQL Date 数据类型


MySQL** 使用下列数据类型在数据库中存储日期或日期/时间值：


- DATE - 格式：YYYY-MM-DD
- DATETIME - 格式：YYYY-MM-DD HH:MM:SS
- TIMESTAMP - 格式：YYYY-MM-DD HH:MM:SS
- YEAR - 格式：YYYY 或 YY


**SQL Server** 使用下列数据类型在数据库中存储日期或日期/时间值：


- DATE - 格式：YYYY-MM-DD
- DATETIME - 格式：YYYY-MM-DD HH:MM:SS
- SMALLDATETIME - 格式：YYYY-MM-DD HH:MM:SS
- TIMESTAMP - 格式：唯一的数字


**注释：**当您在数据库中创建一个新表时，需要为列选择数据类型！


如需了解所有可用的数据类型，请访问我们完整的 [数据类型参考手册](https://www.runoob.com/sql-datatypes.html)。


---


## SQL 日期处理


![Note](https://www.runoob.com/images/lamp.gif)如果不涉及时间部分，那么我们可以轻松地比较两个日期！


假设我们有如下的 "Orders" 表：


| OrderId | ProductName | OrderDate |
| --- | --- | --- |
| 1 | Geitost | 2008-11-11 |
| 2 | Camembert Pierrot | 2008-11-09 |
| 3 | Mozzarella di Giovanni | 2008-11-11 |
| 4 | Mascarpone Fabioli | 2008-10-29 |


现在，我们希望从上表中选取 OrderDate 为 "2008-11-11" 的记录。


我们使用下面的 SELECT 语句：


SELECT * FROM Orders WHERE OrderDate='2008-11-11'


结果集如下所示：


| OrderId | ProductName | OrderDate |
| --- | --- | --- |
| 1 | Geitost | 2008-11-11 |
| 3 | Mozzarella di Giovanni | 2008-11-11 |


现在，假设 "Orders" 表如下所示（请注意 "OrderDate" 列中的时间部分）：


| OrderId | ProductName | OrderDate |
| --- | --- | --- |
| 1 | Geitost | 2008-11-11 13:23:44 |
| 2 | Camembert Pierrot | 2008-11-09 15:45:21 |
| 3 | Mozzarella di Giovanni | 2008-11-11 11:12:01 |
| 4 | Mascarpone Fabioli | 2008-10-29 14:56:59 |


如果我们使用和上面一样的 SELECT 语句：


```
SELECT * FROM Orders WHERE OrderDate='2008-11-11'

或

SELECT * FROM Orders WHERE OrderDate='2008-11-11 00：00：00'
```


那么我们将得不到结果！因为表中没有"2008-11-11 00:00:00"日期。如果没有时间部分，默认时间为 00:00:00。


**提示：**如果您希望使查询简单且更易维护，那么请不要在日期中使用时间部分！

**







	  AI 思考中...





			** [SQL CREATE VIEW、REPLACE VIEW、 DROP VIEW 语句](https://www.runoob.com/sql-view.html)
			[SQL NULL 值 – IS NULL 和 IS NOT NULL](https://www.runoob.com/sql-null-values.html) **













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