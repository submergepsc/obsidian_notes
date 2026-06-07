# PostgreSQL 时间/日期函数和操作符

- Source: https://www.runoob.com/postgresql/postgresql-datetime.html

### 日期/时间操作符


下表演示了基本算术操作符的行为(+,*, 等)：


| 操作符 | 例子 | 结果 |
| --- | --- | --- |
| + | date '2001-09-28' + integer '7' | date '2001-10-05' |
| + | date '2001-09-28' + interval '1 hour' | timestamp '2001-09-28 01:00:00' |
| + | date '2001-09-28' + time '03:00' | timestamp '2001-09-28 03:00:00' |
| + | interval '1 day' + interval '1 hour' | interval '1 day 01:00:00' |
| + | timestamp '2001-09-28 01:00' + interval '23 hours' | timestamp '2001-09-29 00:00:00' |
| + | time '01:00' + interval '3 hours' | time '04:00:00' |
| - | - interval '23 hours' | interval '-23:00:00' |
| - | date '2001-10-01' - date '2001-09-28' | integer '3' (days) |
| - | date '2001-10-01' - integer '7' | date '2001-09-24' |
| - | date '2001-09-28' - interval '1 hour' | timestamp '2001-09-27 23:00:00' |
| - | time '05:00' - time '03:00' | interval '02:00:00' |
| - | time '05:00' - interval '2 hours' | time '03:00:00' |
| - | timestamp '2001-09-28 23:00' - interval '23 hours' | timestamp '2001-09-28 00:00:00' |
| - | interval '1 day' - interval '1 hour' | interval '1 day -01:00:00' |
| - | timestamp '2001-09-29 03:00' - timestamp '2001-09-27 12:00' | interval '1 day 15:00:00' |
| * | 900 * interval '1 second' | interval '00:15:00' |
| * | 21 * interval '1 day' | interval '21 days' |
| * | double precision '3.5' * interval '1 hour' | interval '03:30:00' |
| / | interval '1 hour' / double precision '1.5' | interval '00:40:00' |


### 日期/时间函数


| 函数 | 返回类型 | 描述 | 例子 | 结果 |
| --- | --- | --- | --- | --- |
| age(timestamp, timestamp) | interval | 减去参数后的"符号化"结果，使用年和月，不只是使用天 | age(timestamp '2001-04-10', timestamp '1957-06-13') | 43 years 9 mons 27 days |
| age(timestamp) | interval | 从current_date减去参数后的结果（在午夜） | age(timestamp '1957-06-13') | 43 years 8 mons 3 days |
| clock_timestamp() | timestamp with time zone | 实时时钟的当前时间戳（在语句执行时变化） |  |  |
| current_date | date | 当前的日期； |  |  |
| current_time | time with time zone | 当日时间； |  |  |
| current_timestamp | timestamp with time zone | 当前事务开始时的时间戳； |  |  |
| date_part(text, timestamp) | double precision | 获取子域(等效于extract)； | date_part('hour', timestamp '2001-02-16 20:38:40') | 20 |
| date_part(text, interval) | double precision | 获取子域(等效于extract)； | date_part('month', interval '2 years 3 months') | 3 |
| date_trunc(text, timestamp) | timestamp | 截断成指定的精度； | date_trunc('hour', timestamp '2001-02-16 20:38:40') | 2001-02-16 20:00:00 |
| date_trunc(text, interval) | interval | 截取指定的精度， | date_trunc('hour', interval '2 days 3 hours 40 minutes') | 2 days 03:00:00 |
| extract(field from timestamp) | double precision | 获取子域； | extract(hour from timestamp '2001-02-16 20:38:40') | 20 |
| extract(field from interval) | double precision | 获取子域； | extract(month from interval '2 years 3 months') | 3 |
| isfinite(date) | boolean | 测试是否为有穷日期(不是 +/-无穷) | isfinite(date '2001-02-16') | true |
| isfinite(timestamp) | boolean | 测试是否为有穷时间戳(不是 +/-无穷) | isfinite(timestamp '2001-02-16 21:28:30') | true |
| isfinite(interval) | boolean | 测试是否为有穷时间间隔 | isfinite(interval '4 hours') | true |
| justify_days(interval) | interval | 按照每月 30 天调整时间间隔 | justify_days(interval '35 days') | 1 mon 5 days |
| justify_hours(interval) | interval | 按照每天 24 小时调整时间间隔 | justify_hours(interval '27 hours') | 1 day 03:00:00 |
| justify_interval(interval) | interval | 使用justify_days和justify_hours调整时间间隔的同时进行正负号调整 | justify_interval(interval '1 mon -1 hour') | 29 days 23:00:00 |
| localtime | time | 当日时间； |  |  |
| localtimestamp | timestamp | 当前事务开始时的时间戳； |  |  |
| make_date(year int, month int, day int) | date | 为年、月和日字段创建日期 | make_date(2013, 7, 15) | 2013-07-15 |
| make_interval(years int DEFAULT 0, months int DEFAULT 0, weeks int DEFAULT 0, days int DEFAULT 0, hours int DEFAULT 0, mins int DEFAULT 0, secs double precision DEFAULT 0.0) | interval | 从年、月、周、天、小时、分钟和秒字段中创建间隔 | make_interval(days := 10) | 10 days |
| make_time(hour int, min int, sec double precision) | time | 从小时、分钟和秒字段中创建时间 | make_time(8, 15, 23.5) | 08:15:23.5 |
| make_timestamp(year int, month int, day int, hour int, min int, sec double precision) | timestamp | 从年、月、日、小时、分钟和秒字段中创建时间戳 | make_timestamp(2013, 7, 15, 8, 15, 23.5) | 2013-07-15 08:15:23.5 |
| make_timestamptz(year int, month int, day int, hour int, min int, sec double precision, [ timezone text ]) | timestamp with time zone | 从年、月、日、小时、分钟和秒字段中创建带有时区的时间戳。 没有指定timezone时，使用当前的时区。 | make_timestamptz(2013, 7, 15, 8, 15, 23.5) | 2013-07-15 08:15:23.5+01 |
| now() | timestamp with time zone | 当前事务开始时的时间戳； |  |  |
| statement_timestamp() | timestamp with time zone | 实时时钟的当前时间戳； |  |  |
| timeofday() | text | 与clock_timestamp相同，但结果是一个text 字符串； |  |  |
| transaction_timestamp() | timestamp with time zone | 当前事务开始时的时间戳； |  |  |








	  AI 思考中...





			** [PostgreSQL PRIVILEGES（权限）](https://www.runoob.com/postgresql-privileges.html)
			[PostgreSQL 常用函数](https://www.runoob.com/postgresql-functions.html) **













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