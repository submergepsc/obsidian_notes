# VBScript WeekdayName 函数

- Source: https://www.runoob.com/vbscript/func-weekdayname.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


WeekdayName 函数返回一周中指定的一天的星期名。


### 语法


WeekdayName(weekday[,abbreviate[,firstdayofweek]])


**
| 参数 | 描述 |
| --- | --- |
| weekday | 必需。一周的第几天的数字。 |
| abbreviate | 可选。布尔值，指示是否缩写星期名。 |
| firstdayofweek | 可选。规定一周的第一天。可采用下面的值： 0 = vbUseSystemDayOfWeek - 使用区域语言支持（NLS）API 设置 1 = vbSunday - 星期日（默认） 2 = vbMonday - 星期一 3 = vbTuesday - 星期二 4 = vbWednesday - 星期三 5 = vbThursday - 星期四 6 = vbFriday - 星期五 7 = vbSaturday - 星期六 |


## 实例


## 实例 1


获取一周的第 3 天的名称：


```
<script type="text/vbscript">
document.write(WeekdayName(3))
</script>
```


以上实例输出结果：


```
Tuesday
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_weekdayname_func)


## 实例 2


获取一周的第 3 天的简称：


```
<script type="text/vbscript">
document.write(WeekdayName(3,True))
</script>
```


以上实例输出结果：


```
Tue
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_weekdayname_func2)


## 实例 3


获取一周的第 3 天的名称，一周的第一天是星期一：


```
<script type="text/vbscript">
document.write(WeekdayName(3,False,2))
</script>
```


以上实例输出结果：


```
Wednesday
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_weekdayname_func3)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) Complete VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript Weekday 函数](https://www.runoob.com/func-weekday.html)
			[VBScript Year 函数](https://www.runoob.com/func-year.html) **













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