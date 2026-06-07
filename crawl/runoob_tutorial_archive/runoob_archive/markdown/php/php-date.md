# PHP date() 函数

- Source: https://www.runoob.com/php/php-date.html

---


PHP date() 函数用于格式化时间/日期。


---


## PHP date() 函数


PHP date() 函数可把时间戳格式化为可读性更好的日期和时间。


![Tip](https://www.runoob.com/images/lamp.gif)时间戳是一个字符序列，表示一定的事件发生的日期/时间。


### 语法


```
string date ( string $format [, int $timestamp ] )
```


**
| 参数 | 描述 |
| --- | --- |
| format | 必需。规定时间戳的格式。 |
| timestamp | 可选。规定时间戳。默认是当前的日期和时间。 |


---


## PHP Date() - 格式化日期


date() 函数的第一个必需参数 *format* 规定了如何格式化日期/时间。


这里列出了一些可用的字符：


- d - 代表月中的天 (01 - 31)
- m - 代表月 (01 - 12)
- Y - 代表年 (四位数)


如需了解 *format* 参数中可用的所有字符列表，请查阅我们的 PHP Date 参考手册，[date() 函数](https://www.runoob.com/func-date-date.html)。


可以在字母之间插入其他字符，比如 "/"、"." 或者 "-"，这样就可以增加附加格式了：


```
<?php
echo date("Y/m/d") . "<br>";
echo date("Y.m.d") . "<br>";
echo date("Y-m-d");
?>
```


上面代码的输出如下所示：


```
2016/10/21
2016.10.21
2016-10-21
```


| format 字符 | 说明 | 返回值例子 |
| --- | --- | --- |
| 日 | --- | --- |
| d | 月份中的第几天，有前导零的 2 位数字 | 01 到 31 |
| D | 星期中的第几天，文本表示，3 个字母 | Mon 到 Sun |
| j | 月份中的第几天，没有前导零 | 1 到 31 |
| l（"L"的小写字母） | 星期几，完整的文本格式 | Sunday 到 Saturday |
| N | ISO-8601 格式数字表示的星期中的第几天（PHP 5.1.0 新加） | 1（表示星期一）到 7（表示星期天） |
| S | 每月天数后面的英文后缀，2 个字符 | st，nd，rd 或者 th。可以和 j 一起用 |
| w | 星期中的第几天，数字表示 | 0（表示星期天）到 6（表示星期六） |
| z | 年份中的第几天 | 0 到 365 |
| 星期 | --- | --- |
| W | ISO-8601 格式年份中的第几周，每周从星期一开始（PHP 4.1.0 新加的） | 例如：42（当年的第 42 周） |
| 月 | --- | --- |
| F | 月份，完整的文本格式，例如 January 或者 March | January 到 December |
| m | 数字表示的月份，有前导零 | 01 到 12 |
| M | 三个字母缩写表示的月份 | Jan 到 Dec |
| n | 数字表示的月份，没有前导零 | 1 到 12 |
| t | 给定月份所应有的天数 | 28 到 31 |
| 年 | --- | --- |
| L | 是否为闰年 | 如果是闰年为 1，否则为 0 |
| o | ISO-8601 格式年份数字。这和 Y 的值相同，只除了如果 ISO 的星期数（W）属于前一年或下一年，则用那一年。（PHP 5.1.0 新加） | Examples: 1999 or 2003 |
| Y | 4 位数字完整表示的年份 | 例如：1999 或 2003 |
| y | 2 位数字表示的年份 | 例如：99 或 03 |
| 时间 | --- | --- |
| a | 小写的上午和下午值 | am 或 pm |
| A | 大写的上午和下午值 | AM 或 PM |
| B | Swatch Internet 标准时 | 000 到 999 |
| g | 小时，12 小时格式，没有前导零 | 1 到 12 |
| G | 小时，24 小时格式，没有前导零 | 0 到 23 |
| h | 小时，12 小时格式，有前导零 | 01 到 12 |
| H | 小时，24 小时格式，有前导零 | 00 到 23 |
| i | 有前导零的分钟数 | 00 到 59> |
| s | 秒数，有前导零 | 00 到 59> |
| u | 毫秒 （PHP 5.2.2 新加）。需要注意的是 date() 函数总是返回 000000 因为它只接受 integer 参数， 而 DateTime::format() 才支持毫秒。 | 示例: 654321 |
| 时区 | --- | --- |
| e | 时区标识（PHP 5.1.0 新加） | 例如：UTC，GMT，Atlantic/Azores |
| I | 是否为夏令时 | 如果是夏令时为 1，否则为 0 |
| O | 与格林威治时间相差的小时数 | 例如：+0200 |
| P | 与格林威治时间（GMT）的差别，小时和分钟之间有冒号分隔（PHP 5.1.3 新加） | 例如：+02:00 |
| T | 本机所在的时区 | 例如：EST，MDT（【译者注】在 Windows 下为完整文本格式，例如"Eastern Standard Time"，中文版会显示"中国标准时间"）。 |
| Z | 时差偏移量的秒数。UTC 西边的时区偏移量总是负的，UTC 东边的时区偏移量总是正的。 | -43200 到 43200 |
| 完整的日期／时间 | --- | --- |
| c | ISO 8601 格式的日期（PHP 5 新加） | 2004-02-12T15:19:21+00:00 |
| r | RFC 822 格式的日期 | 例如：Thu, 21 Dec 2000 16:01:07 +0200 |
| U | 从 Unix 纪元（January 1 1970 00:00:00 GMT）开始至今的秒数 | 参见 time() |


## 完整的 PHP Date 参考手册


如需查看所有日期函数的完整参考手册，请访问我们的 [完整的 PHP Date 参考手册](https://www.runoob.com/php-ref-date.html)。


该参考手册提供了每个函数的简要描述和应用实例！








	  AI 思考中...





			** [PHP 多维数组](https://www.runoob.com/php-arrays-multi.html)
			[PHP include 和 require](https://www.runoob.com/php-includes.html) **













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