# PHP 5 Calendar 函数

- Source: https://www.runoob.com/php/php-ref-calendar.html

---


## PHP Calendar 简介


日历扩展包含了简化不同日历格式间的转换的函数。


**它是基于 Julian Day Count（儒略日计数），是从公元前 4713 年 1 月 1 日开始计算的。**


**注释：**如需在日历格式之间转换，必须首先转换为 Julian Day Count，然后再转换为您需要的日历格式。


**注释：**Julian Day Count（儒略日计数）与 Julian Calendar（儒略历法） 不是一回事！


---


## 安装


为了让这些函数能够工作，您必须通过 --enable-calendar 编译 PHP。


PHP 的 Windows 版本已内建了对日历扩展的支持。因此，Calendar 函数会自动工作。


---


## PHP 5 Calendar 函数


| 函数 | 描述 |
| --- | --- |
| cal_days_in_month() | 针对指定的年份和历法，返回一个月中的天数。 |
| cal_from_jd() | 把儒略日计数转换为指定历法的日期。 |
| cal_info() | 返回有关指定历法的信息。 |
| cal_to_jd() | 把指定历法的日期转换为儒略日计数。 |
| easter_date() | 返回指定年份的复活节午夜的 Unix 时间戳。 |
| easter_days() | 返回指定年份的复活节与 3 月 21 日之间的天数。 |
| frenchtojd() | 把法国共和历法的日期转换成为儒略日计数。 |
| gregoriantojd() | 把格利高里历法的日期转换成为儒略日计数。 |
| jddayofweek() | 返回日期在周几。 |
| jdmonthname() | 返回月的名称。 |
| jdtofrench() | 把儒略日计数转换为法国共和历法的日期。 |
| jdtogregorian() | 把儒略日计数转换为格利高里历法的日期。 |
| jdtojewish() | 把儒略日计数转换为犹太历法的日期。 |
| jdtojulian() | 把儒略日计数转换为儒略历法的日期。 |
| jdtounix() | 把儒略日计数转换为 Unix 时间戳。 |
| jewishtojd() | 把犹太历法的日期转换为儒略日计数。 |
| juliantojd() | 把儒略历法的日期转换为儒略日计数。 |
| unixtojd() | 把 Unix 时间戳转换为儒略日计数。 |


## PHP 5 预定义的 Calendar 常量


| 常量 | 类型 | PHP 版本 |
| --- | --- | --- |
| CAL_GREGORIAN | Integer | PHP 4 |
| CAL_JULIAN | Integer | PHP 4 |
| CAL_JEWISH | Integer | PHP 4 |
| CAL_FRENCH | Integer | PHP 4 |
| CAL_NUM_CALS | Integer | PHP 4 |
| CAL_DOW_DAYNO | Integer | PHP 4 |
| CAL_DOW_SHORT | Integer | PHP 4 |
| CAL_DOW_LONG | Integer | PHP 4 |
| CAL_MONTH_GREGORIAN_SHORT | Integer | PHP 4 |
| CAL_MONTH_GREGORIAN_LONG | Integer | PHP 4 |
| CAL_MONTH_JULIAN_SHORT | Integer | PHP 4 |
| CAL_MONTH_JULIAN_LONG | Integer | PHP 4 |
| CAL_MONTH_JEWISH | Integer | PHP 4 |
| CAL_MONTH_FRENCH | Integer | PHP 4 |
| CAL_EASTER_DEFAULT | Integer | PHP 4.3 |
| CAL_EASTER_ROMAN | Integer | PHP 4.3 |
| CAL_EASTER_ALWAYS_GREGORIAN | Integer | PHP 4.3 |
| CAL_EASTER_ALWAYS_JULIAN | Integer | PHP 4.3 |
| CAL_JEWISH_ADD_ALAFIM_GERESH | Integer | PHP 5.0 |
| CAL_JEWISH_ADD_ALAFIM | Integer | PHP 5.0 |
| CAL_JEWISH_ADD_GERESHAYIM | Integer | PHP 5.0 |








	  AI 思考中...





			** [PHP 5 Array 函数](https://www.runoob.com/php-ref-array.html)
			[PHP 5 Date/Time 函数](https://www.runoob.com/php-ref-date.html) **













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