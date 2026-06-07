# JavaScript Date 对象

- Source: https://www.runoob.com/js/jsref-obj-date.html

---


## Date 对象


Date 对象用于处理日期与时间。


创建 Date 对象： **new Date()**


以下四种方法同样可以创建 Date 对象：


```
var d = new Date();
var d = new Date(milliseconds); // 参数为毫秒
var d = new Date(dateString);
var d = new Date(year, month, day, hours, minutes, seconds, milliseconds);
```


- **milliseconds** 参数是一个 Unix 时间戳（Unix Time Stamp），它是一个整数值，表示自 1970 年 1 月 1 日 00:00:00 UTC（the Unix epoch）以来的毫秒数。
- **dateString** 参数表示日期的字符串值。
- **year, month, day, hours, minutes, seconds, milliseconds** 分别表示年、月、日、时、分、秒、毫秒。


更完整的日期与实际教程请参照[JavaScript Date 对象教程](https://www.runoob.com/js-obj-date.html)。


---


## Date 对象属性


| 属性 | 描述 |
| --- | --- |
| constructor | 返回对创建此对象的 Date 函数的引用。 |
| prototype | 使您有能力向对象添加属性和方法。 |


## Date 对象方法


| 方法 | 描述 |
| --- | --- |
| getDate() | 从 Date 对象返回一个月中的某一天 (1 ~ 31)。 |
| getDay() | 从 Date 对象返回一周中的某一天 (0 ~ 6)。 |
| getFullYear() | 从 Date 对象以四位数字返回年份。 |
| getHours() | 返回 Date 对象的小时 (0 ~ 23)。 |
| getMilliseconds() | 返回 Date 对象的毫秒(0 ~ 999)。 |
| getMinutes() | 返回 Date 对象的分钟 (0 ~ 59)。 |
| getMonth() | 从 Date 对象返回月份 (0 ~ 11)。 |
| getSeconds() | 返回 Date 对象的秒数 (0 ~ 59)。 |
| getTime() | 返回 1970 年 1 月 1 日至今的毫秒数。 |
| getTimezoneOffset() | 返回本地时间与格林威治标准时间 (GMT) 的分钟差。 |
| getUTCDate() | 根据世界时从 Date 对象返回月中的一天 (1 ~ 31)。 |
| getUTCDay() | 根据世界时从 Date 对象返回周中的一天 (0 ~ 6)。 |
| getUTCFullYear() | 根据世界时从 Date 对象返回四位数的年份。 |
| getUTCHours() | 根据世界时返回 Date 对象的小时 (0 ~ 23)。 |
| getUTCMilliseconds() | 根据世界时返回 Date 对象的毫秒(0 ~ 999)。 |
| getUTCMinutes() | 根据世界时返回 Date 对象的分钟 (0 ~ 59)。 |
| getUTCMonth() | 根据世界时从 Date 对象返回月份 (0 ~ 11)。 |
| getUTCSeconds() | 根据世界时返回 Date 对象的秒钟 (0 ~ 59)。 |
| getYear() | 已废弃。 请使用 getFullYear() 方法代替。 |
| parse() | 返回1970年1月1日午夜到指定日期（字符串）的毫秒数。 |
| setDate() | 设置 Date 对象中月的某一天 (1 ~ 31)。 |
| setFullYear() | 设置 Date 对象中的年份（四位数字）。 |
| setHours() | 设置 Date 对象中的小时 (0 ~ 23)。 |
| setMilliseconds() | 设置 Date 对象中的毫秒 (0 ~ 999)。 |
| setMinutes() | 设置 Date 对象中的分钟 (0 ~ 59)。 |
| setMonth() | 设置 Date 对象中月份 (0 ~ 11)。 |
| setSeconds() | 设置 Date 对象中的秒钟 (0 ~ 59)。 |
| setTime() | setTime() 方法以毫秒设置 Date 对象。 |
| setUTCDate() | 根据世界时设置 Date 对象中月份的一天 (1 ~ 31)。 |
| setUTCFullYear() | 根据世界时设置 Date 对象中的年份（四位数字）。 |
| setUTCHours() | 根据世界时设置 Date 对象中的小时 (0 ~ 23)。 |
| setUTCMilliseconds() | 根据世界时设置 Date 对象中的毫秒 (0 ~ 999)。 |
| setUTCMinutes() | 根据世界时设置 Date 对象中的分钟 (0 ~ 59)。 |
| setUTCMonth() | 根据世界时设置 Date 对象中的月份 (0 ~ 11)。 |
| setUTCSeconds() | setUTCSeconds() 方法用于根据世界时 (UTC) 设置指定时间的秒字段。 |
| setYear() | 已废弃。请使用 setFullYear() 方法代替。 |
| toDateString() | 把 Date 对象的日期部分转换为字符串。 |
| toGMTString() | 已废弃。请使用 toUTCString() 方法代替。 |
| toISOString() | 使用 ISO 标准返回字符串的日期格式。 |
| toJSON() | 以 JSON 数据格式返回日期字符串。 |
| toLocaleDateString() | 根据本地时间格式，把 Date 对象的日期部分转换为字符串。 |
| toLocaleTimeString() | 根据本地时间格式，把 Date 对象的时间部分转换为字符串。 |
| toLocaleString() | 根据本地时间格式，把 Date 对象转换为字符串。 |
| toString() | 把 Date 对象转换为字符串。 |
| toTimeString() | 把 Date 对象的时间部分转换为字符串。 |
| toUTCString() | 根据世界时，把 Date 对象转换为字符串。 实例：
```
var today = new Date();
var UTCstring = today.toUTCString();
```
 |
| UTC() | 根据世界时返回 1970 年 1 月 1 日 到指定日期的毫秒数。 |
| valueOf() | 返回 Date 对象的原始值。 |
| now() | 返回当前时间的毫秒数。 |








	  AI 思考中...





			** [JavaScript setTime() 方法](https://www.runoob.com/../jsref/jsref-settime.html)
			[JavaScript setSeconds() 方法](https://www.runoob.com/../jsref/jsref-setseconds.html) **













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

      : ·[JavaScript 实例](https://www.runoob.com/js-examples.html)

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