# VBScript Weekday 函数

- Source: https://www.runoob.com/vbscript/func-weekday.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


Weekday 函数返回表示一周的天数的数字，介于 1 到 7 之间。


### 语法


Weekday(date[,firstdayofweek])


**
| 参数 | 描述 |
| --- | --- |
| date | 必需。要计算的日期表达式。 |
| firstdayofweek | 可选。规定一周的第一天。可采用下面的值： 0 = vbUseSystemDayOfWeek - 使用区域语言支持（NLS）API 设置 1 = vbSunday - 星期日（默认） 2 = vbMonday - 星期一 3 = vbTuesday - 星期二 4 = vbWednesday - 星期三 5 = vbThursday - 星期四 6 = vbFriday - 星期五 7 = vbSaturday - 星期六 |


## 实例


## 实例


```
<script type="text/vbscript">
document.write("document.write(Weekday(" & chr(34) & "2010-02-16" & chr(34) & ",0) & " & chr(34) & "<br />" & chr(34) & ")")

document.write(Weekday("2010-02-16",1) & "<br />")
document.write(Weekday("2010-02-16",2) & "<br />")
document.write(Weekday("2010-02-16",3) & "<br />")
document.write(Weekday("2010-02-16",4) & "<br />")
document.write(Weekday("2010-02-16",5) & "<br />")
document.write(Weekday("2010-02-16",6) & "<br />")
</script>
```


以上实例输出结果：


```
document.write(Weekday("2010-02-16",0) & "")

3
2
1
7
6
5
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_weekday_func)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript TimeValue 函数](https://www.runoob.com/func-timevalue.html)
			[VBScript WeekdayName 函数](https://www.runoob.com/func-weekdayname.html) **













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