# SQL BETWEEN 操作符

- Source: https://www.runoob.com/sql/sql-between.html

---


BETWEEN 操作符选取介于两个值之间的数据范围内的值，这些值可以是数值、文本或者日期。


### SQL BETWEEN 语法


```
SELECT column1, column2, ...
FROM table_name
WHERE column BETWEEN value1 AND value2;
```


参数说明：


- column1, column2, ...：要选择的字段名称，可以为多个字段。如果不指定字段名称，则会选择所有字段。
- table_name：要查询的表名称。
- column：要查询的字段名称。
- value1：范围的起始值。
- value2：范围的结束值。

**
---


## 演示数据库


在本教程中，我们将使用 RUNOOB 样本数据库。


下面是选自 "Websites" 表的数据：


```
mysql> SELECT * FROM Websites;
+----+---------------+---------------------------+-------+---------+
| id | name          | url                       | alexa | country |
+----+---------------+---------------------------+-------+---------+
|  1 | Google        | https://www.google.cm/    |     1 | USA     |
|  2 | 淘宝          | https://www.taobao.com/   |    13 | CN      |
|  3 | 菜鸟教程       | http://www.runoob.com/    |  5000 | USA     |
|  4 | 微博           | http://weibo.com/         |    20 | CN      |
|  5 | Facebook      | https://www.facebook.com/ |     3 | USA     |
|  7 | stackoverflow | http://stackoverflow.com/ |     0 | IND     |
+----+---------------+---------------------------+-------+---------+
```


---


## BETWEEN 操作符实例


下面的 SQL 语句选取 alexa 介于 1 和 20 之间的所有网站：


## 实例


```sql
SELECT * FROM WebsitesWHERE alexa BETWEEN 1 AND 20;
```


执行输出结果：


```sql

```


---


## NOT BETWEEN 操作符实例


如需显示不在上面实例范围内的网站，请使用 NOT BETWEEN：


## 实例


```sql
SELECT * FROM WebsitesWHERE alexa NOT BETWEEN 1 AND 20;
```


执行输出结果：


```sql

```


---


## 带有 IN 的 BETWEEN 操作符实例


下面的 SQL 语句选取 alexa 介于 1 和 20 之间但 country 不为 USA 和 IND 的所有网站：


## 实例


```sql
SELECT * FROM WebsitesWHERE (alexa BETWEEN 1 AND 20)AND country NOT
 IN ('USA', 'IND');
```


执行输出结果：


```sql

```


---


## 带有文本值的 BETWEEN 操作符实例


下面的 SQL 语句选取 name 以介于 'A' 和 'H' 之间字母开始的所有网站：


## 实例


```sql
SELECT * FROM WebsitesWHERE name BETWEEN 'A' AND 'H';
```


执行输出结果：


```sql

```


---


## 带有文本值的 NOT BETWEEN 操作符实例


下面的 SQL 语句选取 name 不介于 'A' 和 'H' 之间字母开始的所有网站：


## 实例


```sql
SELECT * FROM WebsitesWHERE name NOT BETWEEN 'A' AND 'H';
```


执行输出结果：


```sql

```


---


## 示例表


下面是 "access_log" 网站访问记录表的数据，其中：


- **aid：**为自增 id。
- **site_id**：为对应 websites表的网站 id。
- **count**：访问次数。
- **date：**为访问日期。


```
mysql> SELECT * FROM access_log;
+-----+---------+-------+------------+
| aid | site_id | count | date       |
+-----+---------+-------+------------+
|   1 |       1 |    45 | 2016-05-10 |
|   2 |       3 |   100 | 2016-05-13 |
|   3 |       1 |   230 | 2016-05-14 |
|   4 |       2 |    10 | 2016-05-14 |
|   5 |       5 |   205 | 2016-05-14 |
|   6 |       4 |    13 | 2016-05-15 |
|   7 |       3 |   220 | 2016-05-15 |
|   8 |       5 |   545 | 2016-05-16 |
|   9 |       3 |   201 | 2016-05-17 |
+-----+---------+-------+------------+
9 rows in set (0.00 sec)
```


本教程使用到的 access_log 表 SQL 文件：[access_log.sql](https://static.jyshare.com/download/access_log.sql)。


---


## 带有日期值的 BETWEEN 操作符实例


下面的 SQL 语句选取 date 介于 '2016-05-10' 和 '2016-05-14' 之间的所有访问记录：


## 实例


```sql
SELECT * FROM access_log
WHERE date BETWEEN '2016-05-10' AND '2016-05-14';
```


执行输出结果：


```sql

```


|  | 请注意，在不同的数据库中，BETWEEN 操作符会产生不同的结果！在某些数据库中，BETWEEN 选取介于两个值之间但不包括两个测试值的字段。在某些数据库中，BETWEEN 选取介于两个值之间且包括两个测试值的字段。在某些数据库中，BETWEEN 选取介于两个值之间且包括第一个测试值但不包括最后一个测试值的字段。 因此，请检查您的数据库是如何处理 BETWEEN 操作符！ |
| --- | --- |








	  AI 思考中...





			** [SQL IN 操作符](https://www.runoob.com/sql-in.html)
			[SQL 别名](https://www.runoob.com/sql-alias.html) **













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