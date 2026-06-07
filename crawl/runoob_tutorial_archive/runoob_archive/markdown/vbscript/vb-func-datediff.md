# VBScript DateDiff 函数

- Source: https://www.runoob.com/vbscript/vb-func-datediff.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


DateDiff 函数返回两个日期之间的时间间隔数。


### 语法


DateDiff(interval,date1,date2[,firstdayofweek[,firstweekofyear]])


**
| 参数 | 描述 |
| --- | --- |
| interval | 必需。计算 date1 和 date2 之间的时间间隔的单位。可采用下面的值： yyyy - 年 q - 季度 m - 月 y - 当年的第几天 d - 日 w - 当周的第几天 ww - 当年的第几周 h - 小时 n - 分 s - 秒 |
| date1,date2 | 必需。日期表达式。在计算中需要使用的两个日期。 |
| firstdayofweek | 可选。规定一周的日数，即当周的第几天。可采用下面的值： 0 = vbUseSystemDayOfWeek - 使用区域语言支持（NLS）API 设置 1 = vbSunday - 星期日（默认） 2 = vbMonday - 星期一 3 = vbTuesday - 星期二 4 = vbWednesday - 星期三 5 = vbThursday - 星期四 6 = vbFriday - 星期五 7 = vbSaturday - 星期六 |
| firstweekofyear | 可选。规定一年中的第一周。可采用下面的值： 0 = vbUseSystem - 使用区域语言支持（NLS）API 设置 1 = vbFirstJan1 - 由 1 月 1 日所在的星期开始（默认） 2 = vbFirstFourDays - 由在新的一年中至少有四天的第一周开始 3 = vbFirstFullWeek - 由在新的一年中第一个完整的周开始 |


## 实例


## 实例 1


2009 年 1 月 31 日和 2010 年 1 月 31 日之间的区别：


```
<script type="text/vbscript">
fromDate="31-Jan-09 00:00:00"
toDate="31-Jan-10 23:59:00"
document.write(DateDiff("yyyy",fromDate,toDate) & "<br />")
document.write(DateDiff("q",fromDate,toDate) & "<br />")
document.write(DateDiff("m",fromDate,toDate) & "<br />")
document.write(DateDiff("y",fromDate,toDate) & "<br />")
document.write(DateDiff("d",fromDate,toDate) & "<br />")
document.write(DateDiff("w",fromDate,toDate) & "<br />")
document.write(DateDiff("ww",fromDate,toDate) & "<br />")
document.write(DateDiff("h",fromDate,toDate) & "<br />")
document.write(DateDiff("n",fromDate,toDate) & "<br />")
document.write(DateDiff("s",fromDate,toDate) & "<br />")
</script>
```


以上实例输出结果：


```
1
4
12
365
365
52
53
8783
527039
31622340
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_datediff_func)


## 实例 2


2009 年 12 月 31 日和 2012 年 12 月 31 日之间有多少周（在星期一开始）：


```
<script type="text/vbscript">
fromDate=CDate("2009/12/31")
toDate=CDate("2012/12/31")
document.write(DateDiff("w",fromDate,toDate,vbMonday))
</script>
```


以上实例输出结果：


```
156
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_datediff_func2)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript DateAdd 函数](https://www.runoob.com/vb-func-dateadd.html)
			[VBScript DatePart 函数](https://www.runoob.com/vb-func-datepart.html) **













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