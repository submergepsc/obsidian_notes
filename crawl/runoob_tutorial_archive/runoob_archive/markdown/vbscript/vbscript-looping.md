# VBScript 循环

- Source: https://www.runoob.com/vbscript/vbscript-looping.html

---


## 循环语句


循环语句用于运行相同的代码块指定的次数。Looping statements are used to run the same block of code a specified number of times.


在 VBScript 中，我们可以使用四种循环语句：


- **For...Next 语句 **- 运行一段代码指定的次数
- **For Each...Next 语句 **- 针对集合中的每个项目或者数组中的每个元素来运行某段代码
- **Do...Loop 语句 **- 运行循环，当条件为 true 或者直到条件为 true 时
- **While...Wend 语句 **- 不要使用这个语句 - 请使用 Do...Loop 语句代替它


---


## For...Next 循环


请使用 **For...Next** 语句运行一段代码指定的次数。


**For** 语句规定计数变量（**i**）以及它的初始值和结束值。**Next** 语句会以 1 作为步进值来递增变量（**i**）。


## 实例


```
<html>
<body>
<script type="text/vbscript">
For i = 0 To 5
  document.write("The number is " & i & "<br />")
Next
</script>
</body>
</html>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_fornext)


### Step 关键词


通过 Step** 关键词，您可以规定计数变量递增或递减的步进值。


在下面的实例中，计数变量（**i**）每次循环的递增步进值为 2。


For i=2 To 10 Step 2**
  some code

Next


如果要递减计数变量，您就必须使用负的 Step** 值。并且必须规定小于开始值的结束值。


在下面的实例中，计数变量（**i**）每次循环的递减步进值为 2。


For i=10 To 2 Step -2**
  some code

Next


### 退出 For...Next


您可以通过 Exit For 关键词退出 For...Next 语句。


For i=1 To 10

  If i=5 Then Exit For

  some code

Next


---


## For Each...Next 循环


For Each...Next** 针对集合中的每个项目或者数组中的每个元素来重复运行某段代码。


## 实例


```
<html>
<body>
<script type="text/vbscript">
Dim cars(2)
cars(0)="Volvo"
cars(1)="Saab"
cars(2)="BMW"
For Each x In cars
  document.write(x & "<br />")
Next
</script>
</body>
</html>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_foreach)


---


## Do...Loop


如果你不知道重复多少次，可以使用 Do...Loop 语句。


Do...Loop 语句重复执行某段代码直到条件是 true 或条件变成 true。


### 重复执行代码直到条件是 true


您可以使用 While 关键字来检查 Do... Loop 语句的条件。


Do While i>10

  some code

Loop


如果 i** 等于 9，上述循环内的代码将终止执行。


Do**
  some code

Loop While i>10


这个循环内的代码将被执行至少一次，即使 i** 小于 10。


### 重复执行代码直到条件变成 true


您可以使用 Until 关键字来检查 Do...Loop 语句的条件。


Do Until i=10**
  some code

Loop


如果 i** 等于 10，上述循环内的代码将终止执行。


Do**
  some code

Loop Until i=10


这个循环内的代码将被执行至少一次，即使 i** 等于 10。


### 退出 Do...Loop


您可以通过 Exit Do 关键词退出 Do...Loop 语句。


Do Until i=10**
  i=i-1

  If i<10 Then Exit Do

Loop


这个循环内的代码，只要 i** 不为 10 且 **i** 大于 10 时都将被执行。


---


![实例s](https://www.runoob.com/images/tryitimg.gif)
## 更多实例（仅适用于 IE）


[循环遍历标题](https://www.runoob.com/try/try.php?filename=vbdemo_fornext2)** 如何循环遍历 html 中的六个标题。


[Do...While loop](https://www.runoob.com/try/try.php?filename=vbdemo_dowhile) 如何做一个简单的 Do...While** 循环。

**







	  AI 思考中...





			** [VBScript 条件语句](https://www.runoob.com/vbscript-conditionals.html)
			[VBScript 总结](https://www.runoob.com/vbscript-summary.html) **













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