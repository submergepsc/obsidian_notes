# VBScript 条件语句

- Source: https://www.runoob.com/vbscript/vbscript-conditionals.html

---


## 条件语句


条件语句用于根据不同的情况执行不同的操作。


在 VBScript 中，我们可以使用四种条件语句：


- **If 语句** - 假如您希望在条件为 true 时执行一系列的代码，可以使用这个语句
- **If...Then...Else 语句** - 假如您希望执行两套代码其中之一，可以使用这个语句
- **If...Then...ElseIf 语句** - 假如您希望选择多套代码之一来执行，可以使用这个语句
- **Select Case 语句** - 假如您希望选择多套代码之一来执行，可以使用这个语句


---


## If...Then...Else


在下面的情况中，您可以使用 If...Then...Else 语句：


- 在条件为 true 时，执行某段代码
- 选择两段代码之一来执行


如果在条件为 true 时只执行**一条**语句，可以把代码写为一行：


If i=10 Then alert("Hello")


在上面的代码中，没有 ..Else.. 语句。我们仅仅让代码在条件为 true 时（当 i=10 时）执行**一项操作**。


如果在条件为 true 时执行**不止一条**语句，那么就必须在一行写一条语句，然后使用关键词 "End If" 来结束这个语句：


If i=10 Then**
   alert("Hello")

   i = i+1

End If


在上面的代码中，同样没有 ..Else.. 语句。我们仅仅让代码在条件为 true 时执行了多项操作**。


假如您想要在条件为 true 时执行某条语句，并在条件不为 true 时执行另一条语句，就必须添加关键词 "Else"：


## 实例（仅适用于 IE）


```
<script type="text/vbscript">
i=hour(time)
If i < 10 Then
document.write("Good morning!")
Else
document.write("Have a nice day!")
End If
</script>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_ifthen)


在上面的代码中，当条件为 true 时会执行第一段代码，当条件不成立时执行第二段代码（当 i 大于 10 时）。


---


## If...Then...ElseIf


如果您想要选择多套代码之一来执行，可以使用 If...Then...ElseIf 语句：


## 实例（仅适用于 IE）


```
<script type="text/vbscript">
i=hour(time)
If i = 10 Then
document.write("Just started...!")
ElseIf i = 11 Then
document.write("Hungry!")
ElseIf i = 12 Then
document.write("Ah, lunch-time!")
ElseIf i = 16 Then
document.write("Time to go home!")
Else
document.write("Unknown")
End If
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_elseif)


---


## Select Case


如果您想要选择多套代码之一来执行，可以使用 "Select Case" 语句：


## 实例（仅适用于 IE）


```
<script type="text/vbscript">
d=weekday(date)Select Case d

Case 1

document.write("Sleepy Sunday")

Case 2

document.write("Monday again!")

Case 3

document.write("Just Tuesday!")

Case 4

document.write("Wednesday!")

Case 5

document.write("Thursday...")

Case 6

document.write("Finally Friday!")

Case else

document.write("Super Saturday!!!!")
End Select
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_selectcase)


以上代码的工作原理：首先，我们需要一个简单的表达式（常常是一个变量），并且这个表达式会被做一次求值运算。然后，表达式的值会与每个 Case 中的值作比较。如果匹配，被匹配的 Case 所对应的代码会被执行。










	  AI 思考中...





			** [VBScript 程序](https://www.runoob.com/vbscript-procedures.html)
			[VBScript 循环语句](https://www.runoob.com/vbscript-looping.html) **













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