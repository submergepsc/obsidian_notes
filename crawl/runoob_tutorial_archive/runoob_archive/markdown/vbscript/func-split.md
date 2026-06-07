# VBScript Split 函数

- Source: https://www.runoob.com/vbscript/func-split.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


Split 函数返回基于 0 的一维数组，此数组包含指定数量的子字符串。


### 语法


Split(expression[,delimiter[,count[,compare]]])


**
| 参数 | 描述 |
| --- | --- |
| expression | 必需。包含子字符串和分隔符的字符串表达式。 |
| delimiter | 可选。用于识别子字符串界限的字符。默认是空格字符。 |
| count | 可选。需被返回的子字符串的数目。-1 指示返回所有的子字符串。 |
| compare | 可选。规定要使用的字符串比较类型。可采用下列的值： 0 = vbBinaryCompare - 执行二进制比较 1 = vbTextCompare - 执行文本比较 |


## 实例


## 实例 1


```
<script type="text/vbscript">
a=Split("RUNOOB is my favourite website")
for each x in a
    document.write(x & "<br />")
next
</script>
```


以上实例输出结果：


```
RUNOOB
is
my
favourite
website
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_split_func)


## 实例 2


使用 delimeter 参数分割文本：


```
<script type="text/vbscript">
a=Split("Brown cow, White horse, Yellow chicken",",")
for each x in a
    document.write(x & "<br />")
next
</script>
```


以上实例输出结果：


```
Brown cow
White horse
Yellow chicken
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_split_func2)


## 实例 3


使用 delimeter 参数和 count 参数分割文本：


```
<script type="text/vbscript">
a=Split("RUNOOB is my favourite website"," ",2)
for each x in a
    document.write(x & "<br />")
next
</script>
```


以上实例输出结果：


```
RUNOOB
is my favourite website
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_split_func3)


## 实例 4


使用文本比较的 delimeter 参数分割文本：


```
<script type="text/vbscript">
a=Split("SundayMondayTuesdayWEDNESDAYThursdayFridaySaturday","day",-1,1)
for each x in a
    document.write(x & "<br />")
next
</script>
```


以上实例输出结果：


```
Sun
Mon
Tues
WEDNES
Thurs
Fri
Satur
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_split_func4)


## 实例 5


使用二进制比较的 delimeter 参数分割文本：


```
<script type="text/vbscript">
a=Split("SundayMondayTuesdayWEDNESDAYThursdayFridaySaturday","day",-1,0)
for each x in a
    document.write(x & "<br />")
next
</script>
```


以上实例输出结果：


```
Sun
Mon
Tues
WEDNESDAYThurs
Fri
Satur
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_split_func5)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript LBound 函数](https://www.runoob.com/func-lbound.html)
			[VBScript UBound 函数](https://www.runoob.com/func-ubound.html) **













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