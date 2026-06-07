# VBScript MsgBox 函数

- Source: https://www.runoob.com/vbscript/func-msgbox.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


MsgBox 函数显示一个消息框，等待用户点击某个按钮，然后返回指示被点击按钮的值。


MsgBox 函数返回下面的值：


- 1 = vbOK - OK 按钮被点击
- 2 = vbCancel - Cancel 按钮被点击
- 3 = vbAbort - Abort 按钮被点击
- 4 = vbRetry - Retry 按钮被点击
- 5 = vbIgnore - Ignore 按钮被点击
- 6 = vbYes - Yes 按钮被点击
- 7 = vbNo - No 按钮被点击


**注意：**当 helpfile 和 context 参数均被规定后，用户可按 F1 键来查看帮助。


**提示：**请参阅 InputBox 函数。


### 语法


MsgBox(prompt[,buttons][,title][,helpfile,context])


**
| 参数 | 描述 |
| --- | --- |
| prompt | 必需。作为消息显示在对话框中的字符串表达式。prompt 的最大长度大约是 1024 个字符，这取决于所使用的字符的宽度。如果 prompt 中包含多个行，则可在各行之间用回车符（Chr(13)）、换行符（Chr(10)）或回车换行符的组合（Chr(13) & Chr(10)）分隔各行。 |
| buttons | 可选，是表示指定显示按钮的数目和类型、使用的图标样式，默认按钮的标识以及消息框样式的数值的总和。默认值为 0。 0 = vbOKOnly - 只显示 OK 按钮 1 = vbOKCancel - 显示 OK 和 Cancel 按钮 2 = vbAbortRetryIgnore - 显示 Abort、Retry 和 Ignore 按钮 3 = vbYesNoCancel - 显示 Yes、No 和 Cancel 按钮 4 = vbYesNo - 显示 Yes 和 No 按钮 5 = vbRetryCancel - 显示 Retry 和 Cancel 按钮 16 = vbCritical - 显示临界信息图标 32 = vbQuestion - 显示警告查询图标 48 = vbExclamation - 显示警告消息图标 64 = vbInformation - 显示信息消息图标 0 = vbDefaultButton1 - 第一个按钮为默认按钮 256 = vbDefaultButton2 - 第二个按钮为默认按钮 512 = vbDefaultButton3 - 第三个按钮为默认按钮 768 = vbDefaultButton4 - 第四个按钮为默认按钮 0 = vbApplicationModal - 应用程序模式（用户必须响应消息框才能继续在当前应用程序中工作） 4096 = vbSystemModal - 系统模式（在用户响应消息框前，所有应用程序都被挂起） 我们可以把按钮分成四组：第一组值(0-5)用于描述对话框中显示的按钮类型与数目；第二组值(16,32,48,64)用于描述图标的样式；第三组值(0,256,512,768)用于确定默认按钮；而第四组值(0,4096)则决定消息框的样式。在将这些数字相加以生成 buttons 参数值时，只能从每组值中取用一个数字。 |
| title | 可选。消息框的标题。默认是应用程序的名称。 |
| helpfile | 可选。字符串表达式，用于标识为对话框提供上下文相关帮助的帮助文件。必须与 context 参数一起使用。 |
| context | 可选。数值表达式，用于标识由帮助文件的作者指定给某个帮助主题的上下文编号。必须与 helpfile 参数一起使用。 |


## 实例


## 实例 1


```
<script type="text/vbscript">

MsgBox("Hello world")

</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_msgbox_func)


## 实例 2


带有换行符的消息框：


```
<script type="text/vbscript">

MsgBox("Hello" & chr(13) & "world")

</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_msgbox_func2)


## 实例 3


不同的 buttonsets 和不同的图标。返回点击的按钮的值：


```
<script type="text/vbscript">

x=MsgBox("Hello world",n)
document.getElementById("myDiv").innerHTML="You clicked: " & x

</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_msgbox_func3)


## 实例 4


带有标题的消息框：


```
<script type="text/vbscript">

x=MsgBox("Are you a programmer",4,"Please answer")

</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_msgbox_func4)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript LoadPicture 函数](https://www.runoob.com/func-loadpicture.html)
			[VBScript RGB 函数](https://www.runoob.com/func-rgb.html) **













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