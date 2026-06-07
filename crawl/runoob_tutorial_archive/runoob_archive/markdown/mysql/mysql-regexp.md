# MySQL 正则表达式

- Source: https://www.runoob.com/mysql/mysql-regexp.html

在前面的章节我们已经了解到 MySQL 可以通过 **LIKE ...%** 来进行模糊匹配。

MySQL 同样也支持其他正则表达式的匹配， MySQL 中使用 **REGEXP** 和 **RLIKE**操作符来进行正则表达式匹配。

如果您了解 PHP 或 Perl，那么操作起来就非常简单，因为 MySQL 的正则表达式匹配与这些脚本的类似。

下表中的正则模式可应用于 REGEXP 操作符中。




| 模式 | 描述 |
| --- | --- |
| ^ | 匹配输入字符串的开始位置。如果设置了 RegExp 对象的 Multiline 属性，^ 也匹配 '\n' 或 '\r' 之后的位置。 |
| $ | 匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置。 |
| . | 匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用像 '[.\n]' 的模式。 |
| [...] | 字符集合。匹配所包含的任意一个字符。例如， '[abc]' 可以匹配 "plain" 中的 'a'。 |
| [^...] | 负值字符集合。匹配未包含的任意字符。例如， '[^abc]' 可以匹配 "plain" 中的'p'。 |
| p1\|p2\|p3 | 匹配 p1 或 p2 或 p3。例如，'z\|food' 能匹配 "z" 或 "food"。'(z\|f)ood' 则匹配 "zood" 或 "food"。 |
| * | 匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。 |
| + | 匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。 |
| {n} | n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。 |
| {n,m} | m 和 n 均为非负整数，其中n

查找 name 字段中以 **'st'** 为开头的所有数据：


```
mysql> SELECT name FROM person_tbl WHERE name REGEXP '^st';
```


查找 name 字段中以 **'ok'** 为结尾的所有数据：


```
mysql> SELECT name FROM person_tbl WHERE name REGEXP 'ok$';
```


查找 name 字段中包含 **'mar'** 字符串的所有数据：


```
mysql> SELECT name FROM person_tbl WHERE name REGEXP 'mar';
```


查找 name 字段中以元音字符开头或以 **'ok'** 字符串结尾的所有数据：


```
mysql> SELECT name FROM person_tbl WHERE name REGEXP '^[aeiou]|ok$';
```


选择订单表中描述中包含 "item" 后跟一个或多个数字的记录。


```
SELECT * FROM orders WHERE order_description REGEXP 'item[0-9]+';
```


使用 **BINARY** 关键字，使得匹配区分大小写：


```
SELECT * FROM products WHERE product_name REGEXP BINARY 'apple';
```


使用 OR 进行多个匹配条件，以下将选择姓氏为 "Smith" 或 "Johnson" 的员工记录：


```
SELECT * FROM employees WHERE last_name REGEXP 'Smith|Johnson';
```


### 使用 RLIKE 进行模式匹配

RLIKE 是 MySQL 中用于进行正则表达式匹配的运算符，与 REGEXP 是一样的，RLIKE 和 REGEXP 可以互换使用，没有区别。

以下是使用 RLIKE 进行正则表达式匹配的基本语法：


```
SELECT column1, column2, ...
FROM table_name
WHERE column_name RLIKE 'pattern';
```


**参数说明：**


- `column1`, `column2`, ... 是你要选择的列的名称，如果使用 `*` 表示选择所有列。
- `table_name` 是你要从中查询数据的表的名称。
- `column_name` 是你要进行正则表达式匹配的列的名称。
- `'pattern'` 是一个正则表达式模式。


```
SELECT * FROM products WHERE product_name RLIKE '^[0-9]';
```


以上 SQL 语句选择产品名称以数字开头的所有产品。









	  AI 思考中...





			** [MySQL NULL 值处理](https://www.runoob.com/mysql-null.html)
			[MySQL 事务](https://www.runoob.com/mysql-transaction.html) **













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