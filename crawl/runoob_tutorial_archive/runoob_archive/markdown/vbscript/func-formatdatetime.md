# VBScript FormatDateTime 函数

- Source: https://www.runoob.com/vbscript/func-formatdatetime.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


FormatDateTime 函数格式化并返回一个有效的日期或时间的表达式。


### 语法


FormatDateTime(date,format)


**
| 参数 | 描述 |
| --- | --- |
| date | 必需。任何有效的日期表达式（比如 Date() 或者 Now()）。 |
| format | 可选。规定所使用的日期/时间格式的格式值。 可采用下面的值： 0 = vbGeneralDate - 默认。返回日期：mm/dd/yy 及如果指定时间：hh:mm:ss PM/AM。 1 = vbLongDate - 返回日期：weekday, monthname, year 2 = vbShortDate - 返回日期：mm/dd/yy 3 = vbLongTime - 返回时间：hh:mm:ss PM/AM 4 = vbShortTime - 返回时间：hh:mm |


## 实例


## 实例


用不同的格式显示日期：


```
<script type="text/vbscript">
d=CDate("2010-02-16 13:45")
document.write(FormatDateTime(d) & "<br />")
document.write(FormatDateTime(d,1) & "<br />")
document.write(FormatDateTime(d,2) & "<br />")
document.write(FormatDateTime(d,3) & "<br />")
document.write(FormatDateTime(d,4) & "<br />")
</script>
```


以上实例输出结果：


```
2/16/2010 1:45:00 PM
Tuesday, February 16, 2010
2/16/2010
1:45:00 PM
13:45
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_formatdatetime_func)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript Day 函数](https://www.runoob.com/func-day.html)
			[VBScript Hour 函数](https://www.runoob.com/func-hour.html) **













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