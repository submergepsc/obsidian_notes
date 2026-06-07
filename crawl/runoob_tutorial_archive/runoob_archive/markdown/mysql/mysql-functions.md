# MySQL 函数

- Source: https://www.runoob.com/mysql/mysql-functions.html

MySQL 有很多内置的函数，以下列出了这些函数的说明。


---


## MySQL 字符串函数


| 函数 | 描述 | 实例 |
| --- | --- | --- |
| ASCII(s) | 返回字符串 s 的第一个字符的 ASCII 码。 | 返回 CustomerName 字段第一个字母的 ASCII 码：
```
SELECT ASCII(CustomerName) AS NumCodeOfFirstChar
FROM Customers;
```
 |
| CHAR_LENGTH(s) | 返回字符串 s 的字符数 | 返回字符串 RUNOOB 的字符数
```
SELECT CHAR_LENGTH("RUNOOB") AS LengthOfString;
```
 |
| CHARACTER_LENGTH(s) | 返回字符串 s 的字符数，等同于 CHAR_LENGTH(s) | 返回字符串 RUNOOB 的字符数
```
SELECT CHARACTER_LENGTH("RUNOOB") AS LengthOfString;
```
 |
| CONCAT(s1,s2...sn) | 字符串 s1,s2 等多个字符串合并为一个字符串 | 合并多个字符串
```
SELECT CONCAT("SQL ", "Runoob ", "Gooogle ", "Facebook") AS ConcatenatedString;
```
 |
| CONCAT_WS(x, s1,s2...sn) | 同 CONCAT(s1,s2,...) 函数，但是每个字符串之间要加上 x，x 可以是分隔符 | 合并多个字符串，并添加分隔符：
```
SELECT CONCAT_WS("-", "SQL", "Tutorial", "is", "fun!")AS ConcatenatedString;
```
 |
| FIELD(s,s1,s2...) | 返回第一个字符串 s 在字符串列表(s1,s2...)中的位置 | 返回字符串 c 在列表值中的位置：
```
SELECT FIELD("c", "a", "b", "c", "d", "e");
```
 |
| FIND_IN_SET(s1,s2) | 返回在字符串s2中与s1匹配的字符串的位置 | 返回字符串 c 在指定字符串中的位置：
```
SELECT FIND_IN_SET("c", "a,b,c,d,e");
```
 |
| FORMAT(x,n) | 函数可以将数字 x 进行格式化 "#,###.##", 将 x 保留到小数点后 n 位，最后一位四舍五入。 | 格式化数字 "#,###.##" 形式：
```
SELECT FORMAT(250500.5634, 2);     -- 输出 250,500.56
```
 |
| INSERT(s1,x,len,s2) | 字符串 s2 替换 s1 的 x 位置开始长度为 len 的字符串 | 从字符串第一个位置开始的 6 个字符替换为 runoob：
```
SELECT INSERT("google.com", 1, 6, "runoob");  -- 输出：runoob.com
```
 |
| LOCATE(s1,s) | 从字符串 s 中获取 s1 的开始位置 | 获取 b 在字符串 abc 中的位置：
```
SELECT LOCATE('st','myteststring');  -- 5
```
 返回字符串 abc 中 b 的位置：
```
SELECT LOCATE('b', 'abc') -- 2
```
 |
| LCASE(s) | 将字符串 s 的所有字母变成小写字母 | 字符串 RUNOOB 转换为小写：
```
SELECT LCASE('RUNOOB') -- runoob
```
 |
| LEFT(s,n) | 返回字符串 s 的前 n 个字符 | 返回字符串 runoob 中的前两个字符：
```
SELECT LEFT('runoob',2) -- ru
```
 |
| LOWER(s) | 将字符串 s 的所有字母变成小写字母 | 字符串 RUNOOB 转换为小写：
```
SELECT LOWER('RUNOOB') -- runoob
```
 |
| LPAD(s1,len,s2) | 在字符串 s1 的开始处填充字符串 s2，使字符串长度达到 len | 将字符串 xx 填充到 abc 字符串的开始处：
```
SELECT LPAD('abc',5,'xx') -- xxabc
```
 |
| LTRIM(s) | 去掉字符串 s 开始处的空格 | 去掉字符串 RUNOOB开始处的空格：
```
SELECT LTRIM("    RUNOOB") AS LeftTrimmedString;-- RUNOOB
```
 |
| MID(s,n,len) | 从字符串 s 的 n 位置截取长度为 len 的子字符串，同 SUBSTRING(s,n,len) | 从字符串 RUNOOB 中的第 2 个位置截取 3个 字符：
```
SELECT MID("RUNOOB", 2, 3) AS ExtractString; -- UNO
```
 |
| POSITION(s1 IN s) | 从字符串 s 中获取 s1 的开始位置 | 返回字符串 abc 中 b 的位置：
```
SELECT POSITION('b' in 'abc') -- 2
```
 |
| REPEAT(s,n) | 将字符串 s 重复 n 次 | 将字符串 runoob 重复三次：
```
SELECT REPEAT('runoob',3) -- runoobrunoobrunoob
```
 |
| REPLACE(s,s1,s2) | 将字符串 s2 替代字符串 s 中的字符串 s1 | 将字符串 abc 中的字符 a 替换为字符 x：
```
SELECT REPLACE('abc','a','x') --xbc
```
 |
| REVERSE(s) | 将字符串s的顺序反过来 | 将字符串 abc 的顺序反过来：
```
SELECT REVERSE('abc') -- cba
```
 |
| RIGHT(s,n) | 返回字符串 s 的后 n 个字符 | 返回字符串 runoob 的后两个字符：
```
SELECT RIGHT('runoob',2) -- ob
```
 |
| RPAD(s1,len,s2) | 在字符串 s1 的结尾处添加字符串 s2，使字符串的长度达到 len | 将字符串 xx 填充到 abc 字符串的结尾处：
```
SELECT RPAD('abc',5,'xx') -- abcxx
```
 |
| RTRIM(s) | 去掉字符串 s 结尾处的空格 | 去掉字符串 RUNOOB 的末尾空格：
```
SELECT RTRIM("RUNOOB     ") AS RightTrimmedString;   -- RUNOOB
```
 |
| SPACE(n) | 返回 n 个空格 | 返回 10 个空格：
```
SELECT SPACE(10);
```
 |
| STRCMP(s1,s2) | 比较字符串 s1 和 s2，如果 s1 与 s2 相等返回 0 ，如果 s1>s2 返回 1，如果 s1d2 之间相隔的天数 |
```
SELECT DATEDIFF('2001-01-01','2001-02-02')
-> -32
```
 |
| DATE_ADD(d，INTERVAL expr type) | 计算起始日期 d 加上一个时间段后的日期，type 值可以是： MICROSECOND SECOND MINUTE HOUR DAY WEEK MONTH QUARTER YEAR SECOND_MICROSECOND MINUTE_MICROSECOND MINUTE_SECOND HOUR_MICROSECOND HOUR_SECOND HOUR_MINUTE DAY_MICROSECOND DAY_SECOND DAY_MINUTE DAY_HOUR YEAR_MONTH |
```
SELECT DATE_ADD("2017-06-15", INTERVAL 10 DAY);
-> 2017-06-25

SELECT DATE_ADD("2017-06-15 09:34:21", INTERVAL 15 MINUTE);
-> 2017-06-15 09:49:21

SELECT DATE_ADD("2017-06-15 09:34:21", INTERVAL -3 HOUR);
->2017-06-15 06:34:21

SELECT DATE_ADD("2017-06-15 09:34:21", INTERVAL -3 MONTH);
->2017-03-15 09:34:21
```
 |
| DATE_FORMAT(d,f) | 按表达式 f的要求显示日期 d |
```
SELECT DATE_FORMAT('2011-11-11 11:11:11','%Y-%m-%d %r')
-> 2011-11-11 11:11:11 AM
```
 |
| DATE_SUB(date,INTERVAL expr type) | 函数从日期减去指定的时间间隔。 | Orders 表中 OrderDate 字段减去 2 天：
```
SELECT OrderId,DATE_SUB(OrderDate,INTERVAL 2 DAY) AS OrderPayDate
FROM Orders
```
 |
| DAY(d) | 返回日期值 d 的日期部分 |
```
SELECT DAY("2017-06-15");
-> 15
```
 |
| DAYNAME(d) | 返回日期 d 是星期几，如 Monday,Tuesday |
```
SELECT DAYNAME('2011-11-11 11:11:11')
->Friday
```
 |
| DAYOFMONTH(d) | 计算日期 d 是本月的第几天 |
```
SELECT DAYOFMONTH('2011-11-11 11:11:11')
->11
```
 |
| DAYOFWEEK(d) | 日期 d 今天是星期几，1 星期日，2 星期一，以此类推 |
```
SELECT DAYOFWEEK('2011-11-11 11:11:11')
->6
```
 |
| DAYOFYEAR(d) | 计算日期 d 是本年的第几天 |
```
SELECT DAYOFYEAR('2011-11-11 11:11:11')
->315
```
 |
| EXTRACT(type FROM d) | 从日期 d 中获取指定的值，type 指定返回的值。 type可取值为： MICROSECOND SECOND MINUTE HOUR DAY WEEK MONTH QUARTER YEAR SECOND_MICROSECOND MINUTE_MICROSECOND MINUTE_SECOND HOUR_MICROSECOND HOUR_SECOND HOUR_MINUTE DAY_MICROSECOND DAY_SECOND DAY_MINUTE DAY_HOUR YEAR_MONTH |
```
SELECT EXTRACT(MINUTE FROM '2011-11-11 11:11:11')
-> 11
```
 |
| FROM_DAYS(n) | 计算从 0000 年 1 月 1 日开始 n 天后的日期 |
```
SELECT FROM_DAYS(1111)
-> 0003-01-16
```
 |
| HOUR(t) | 返回 t 中的小时值 |
```
SELECT HOUR('1:2:3')
-> 1
```
 |
| LAST_DAY(d) | 返回给给定日期的那一月份的最后一天 |
```
SELECT LAST_DAY("2017-06-20");
-> 2017-06-30
```
 |
| LOCALTIME() | 返回当前日期和时间 |
```
SELECT LOCALTIME()
-> 2018-09-19 20:57:43
```
 |
| LOCALTIMESTAMP() | 返回当前日期和时间 |
```
SELECT LOCALTIMESTAMP()
-> 2018-09-19 20:57:43
```
 |
| MAKEDATE(year, day-of-year) | 基于给定参数年份 year 和所在年中的天数序号 day-of-year 返回一个日期 |
```
SELECT MAKEDATE(2017, 3);
-> 2017-01-03
```
 |
| MAKETIME(hour, minute, second) | 组合时间，参数分别为小时、分钟、秒 |
```
SELECT MAKETIME(11, 35, 4);
-> 11:35:04
```
 |
| MICROSECOND(date) | 返回日期参数所对应的微秒数 |
```
SELECT MICROSECOND("2017-06-20 09:34:00.000023");
-> 23
```
 |
| MINUTE(t) | 返回 t 中的分钟值 |
```
SELECT MINUTE('1:2:3')
-> 2
```
 |
| MONTHNAME(d) | 返回日期当中的月份名称，如 November |
```
SELECT MONTHNAME('2011-11-11 11:11:11')
-> November
```
 |
| MONTH(d) | 返回日期d中的月份值，1 到 12 |
```
SELECT MONTH('2011-11-11 11:11:11')
->11
```
 |
| NOW() | 返回当前日期和时间 |
```
SELECT NOW()
-> 2018-09-19 20:57:43
```
 |
| PERIOD_ADD(period, number) | 为 年-月 组合日期添加一个时段 |
```
SELECT PERIOD_ADD(201703, 5);
-> 201708
```
 |
| PERIOD_DIFF(period1, period2) | 返回两个时段之间的月份差值 |
```
SELECT PERIOD_DIFF(201710, 201703);
-> 7
```
 |
| QUARTER(d) | 返回日期d是第几季节，返回 1 到 4 |
```
SELECT QUARTER('2011-11-11 11:11:11')
-> 4
```
 |
| SECOND(t) | 返回 t 中的秒钟值 |
```
SELECT SECOND('1:2:3')
-> 3
```
 |
| SEC_TO_TIME(s) | 将以秒为单位的时间 s 转换为时分秒的格式 |
```
SELECT SEC_TO_TIME(4320)
-> 01:12:00
```
 |
| STR_TO_DATE(string, format_mask) | 将字符串转变为日期 |
```
SELECT STR_TO_DATE("August 10 2017", "%M %d %Y");
-> 2017-08-10
```
 |
| SUBDATE(d,n) | 日期 d 减去 n 天后的日期 |
```
SELECT SUBDATE('2011-11-11 11:11:11', 1)
->2011-11-10 11:11:11 (默认是天)
```
 |
| SUBTIME(t,n) | 时间 t 减去 n 秒的时间 |
```
SELECT SUBTIME('2011-11-11 11:11:11', 5)
->2011-11-11 11:11:06 (秒)
```
 |
| SYSDATE() | 返回当前日期和时间 |
```
SELECT SYSDATE()
-> 2018-09-19 20:57:43
```
 |
| TIME(expression) | 提取传入表达式的时间部分 |
```
SELECT TIME("19:30:10");
-> 19:30:10
```
 |
| TIME_FORMAT(t,f) | 按表达式 f 的要求显示时间 t |
```
SELECT TIME_FORMAT('11:11:11','%r')
11:11:11 AM
```
 |
| TIME_TO_SEC(t) | 将时间 t 转换为秒 |
```
SELECT TIME_TO_SEC('1:12:00')
-> 4320
```
 |
| TIMEDIFF(time1, time2) | 计算时间差值 |
```
mysql> SELECT TIMEDIFF("13:10:11", "13:10:10");
-> 00:00:01
mysql> SELECT TIMEDIFF('2000:01:01 00:00:00',
    ->                 '2000:01:01 00:00:00.000001');
        -> '-00:00:00.000001'
mysql> SELECT TIMEDIFF('2008-12-31 23:59:59.000001',
    ->                 '2008-12-30 01:01:01.000002');
        -> '46:58:57.999999'
```
 |
| TIMESTAMP(expression, interval) | 单个参数时，函数返回日期或日期时间表达式；有2个参数时，将参数加和 |
```
mysql> SELECT TIMESTAMP("2017-07-23",  "13:10:11");
-> 2017-07-23 13:10:11
mysql> SELECT TIMESTAMP('2003-12-31');
        -> '2003-12-31 00:00:00'
mysql> SELECT TIMESTAMP('2003-12-31 12:00:00','12:00:00');
        -> '2004-01-01 00:00:00'
```
 |
| TIMESTAMPDIFF(unit,datetime_expr1,datetime_expr2) | 计算时间差，返回 datetime_expr2 − datetime_expr1 的时间差 |
```
mysql> SELECT TIMESTAMPDIFF(DAY,'2003-02-01','2003-05-01');   // 计算两个时间相隔多少天
        -> 89
mysql> SELECT TIMESTAMPDIFF(MONTH,'2003-02-01','2003-05-01');   // 计算两个时间相隔多少月
        -> 3
mysql> SELECT TIMESTAMPDIFF(YEAR,'2002-05-01','2001-01-01');    // 计算两个时间相隔多少年
        -> -1
mysql> SELECT TIMESTAMPDIFF(MINUTE,'2003-02-01','2003-05-01 12:05:55');  // 计算两个时间相隔多少分钟
        -> 128885
```
 |
| TO_DAYS(d) | 计算日期 d 距离 0000 年 1 月 1 日的天数 |
```
SELECT TO_DAYS('0001-01-01 01:01:01')
-> 366
```
 |
| WEEK(d) | 计算日期 d 是本年的第几个星期，范围是 0 到 53 |
```
SELECT WEEK('2011-11-11 11:11:11')
-> 45
```
 |
| WEEKDAY(d) | 日期 d 是星期几，0 表示星期一，1 表示星期二 |
```
SELECT WEEKDAY("2017-06-15");
-> 3
```
 |
| WEEKOFYEAR(d) | 计算日期 d 是本年的第几个星期，范围是 0 到 53 |
```
SELECT WEEKOFYEAR('2011-11-11 11:11:11')
-> 45
```
 |
| YEAR(d) | 返回年份 |
```
SELECT YEAR("2017-06-15");
-> 2017
```
 |
| YEARWEEK(date, mode) | 返回年份及第几周（0到53），mode 中 0 表示周天，1表示周一，以此类推 |
```
SELECT YEARWEEK("2017-06-15");
-> 201724
```
 |


---


## MySQL 高级函数


| 函数名 | 描述 | 实例 |
| --- | --- | --- |
| BIN(x) | 返回 x 的二进制编码，x 为十进制数 | 15 的 2 进制编码:
```
SELECT BIN(15); -- 1111
```
 |
| BINARY(s) | 将字符串 s 转换为二进制字符串 |
```
SELECT BINARY "RUNOOB";
-> RUNOOB
```
 |
|
```
CASE expression
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
   ...
    WHEN conditionN THEN resultN
    ELSE result
END
```
 | CASE 表示函数开始，END 表示函数结束。如果 condition1 成立，则返回 result1, 如果 condition2 成立，则返回 result2，当全部不成立则返回 result，而当有一个成立之后，后面的就不执行了。 |
```
SELECT CASE
　　WHEN 1 > 0
　　THEN '1 > 0'
　　WHEN 2 > 0
　　THEN '2 > 0'
　　ELSE '3 > 0'
　　END
->1 > 0
```
 |
| CAST(x AS type) | 转换数据类型 | 字符串日期转换为日期：
```
SELECT CAST("2017-08-29" AS DATE);
-> 2017-08-29
```
 |
| COALESCE(expr1, expr2, ...., expr_n) | 返回参数中的第一个非空表达式（从左向右） |
```
SELECT COALESCE(NULL, NULL, NULL, 'runoob.com', NULL, 'google.com');
-> runoob.com
```
 |
| CONNECTION_ID() | 返回唯一的连接 ID |
```
SELECT CONNECTION_ID();
-> 4292835
```
 |
| CONV(x,f1,f2) | 返回 f1 进制数变成 f2 进制数 |
```
SELECT CONV(15, 10, 2);
-> 1111
```
 |
| CONVERT(s USING cs) | 函数将字符串 s 的字符集变成 cs |
```
SELECT CHARSET('ABC')
->utf-8

SELECT CHARSET(CONVERT('ABC' USING gbk))
->gbk
```
 |
| CURRENT_USER() | 返回当前用户 |
```
SELECT CURRENT_USER();
-> guest@%
```
 |
| DATABASE() | 返回当前数据库名 |
```
SELECT DATABASE();
-> runoob
```
 |
| IF(expr,v1,v2) | 如果表达式 expr 成立，返回结果 v1；否则，返回结果 v2。 |
```
SELECT IF(1 > 0,'正确','错误')
->正确
```
 |
| IFNULL(v1,v2) | 如果 v1 的值不为 NULL，则返回 v1，否则返回 v2。 |
```
SELECT IFNULL(null,'Hello Word')
->Hello Word
```
 |
| ISNULL(expression) | 判断表达式是否为 NULL |
```
SELECT ISNULL(NULL);
->1
```
 |
| LAST_INSERT_ID() | 返回最近生成的 AUTO_INCREMENT 值 |
```
SELECT LAST_INSERT_ID();
->6
```
 |
| NULLIF(expr1, expr2) | 比较两个字符串，如果字符串 expr1 与 expr2 相等 返回 NULL，否则返回 expr1 |
```
SELECT NULLIF(25, 25);
->
```
 |
| SESSION_USER() | 返回当前用户 |  |
| SYSTEM_USER() | 返回当前用户 |  |
| USER() | 返回当前用户 |  |
| VERSION() | 返回数据库的版本号 |
```
SELECT VERSION()
-> 5.6.34
```
 |


以下是 MySQL 8.0 版本新增的一些常用函数：


| 函数 | 描述 | 实例 |
| --- | --- | --- |
| JSON_OBJECT() | 将键值对转换为 JSON 对象 |
```
SELECT JSON_OBJECT('key1', 'value1', 'key2', 'value2')
```
 |
| JSON_ARRAY() | 将值转换为 JSON 数组 |
```
SELECT JSON_ARRAY(1, 2, 'three')
```
 |
| JSON_EXTRACT() | 从 JSON 字符串中提取指定的值 |
```
SELECT JSON_EXTRACT('{"name": "John", "age": 30}', '$.name')
```
 |
| JSON_CONTAINS() | 检查一个 JSON 字符串是否包含指定的值 |
```
SELECT JSON_CONTAINS('{"name": "John", "age": 30}', 'John', '$.name')
```
 |
| ROW_NUMBER() | 为查询结果中的每一行分配一个唯一的数字 |
```
SELECT ROW_NUMBER() OVER(ORDER BY id) AS row_number, name FROM users
```
 |
| RANK() | 为查询结果中的每一行分配一个排名 |
```
SELECT RANK() OVER(ORDER BY score DESC) AS rank, name, score FROM students
```
 |








	  AI 思考中...





			** [MySQL UNION 操作符](https://www.runoob.com/mysql-union-operation.html)
			[MySQL IFNULL() 函数](https://www.runoob.com/mysql-func-ifnull.html) **