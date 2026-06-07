# VBScript InputBox 函数

- Source: https://www.runoob.com/vbscript/func-inputbox.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


InputBox 函数显示一个对话框，用户可在其中输入文本并/或点击一个按钮。如果用户点击点击 OK 按钮或按键盘上的 ENTER 键， 则 InputBox 函数返回文本框中的文本。如果用户点击 Cancel 按钮，函数返回一个空字符串("")。


**注意：**如果同时规定 helpfile 和 context 参数，则会向对话框添加一个 Help 按钮。


**提示：**请参阅 MsgBox 函数。


### 语法


InputBox(prompt[,title][,default][,xpos][,ypos][,helpfile,context])


**
| 参数 | 描述 |
| --- | --- |
| prompt | 必需。显示在对话框中的消息。prompt 的最大长度大约是 1024 个字符，这取决于所使用的字符的宽度。如果 prompt 中包含多个行，则可在各行之间用回车符（Chr(13)）、换行符（Chr(10)）或回车换行符的组合（Chr(13) & Chr(10)）来分隔各行。 |
| title | 可选。对话框的标题。默认是应用程序的名称。 |
| default | 可选。一个在文本框中的默认文本。 |
| xpos | 可选。数值表达式，用于指定对话框的左边缘与屏幕左边缘的水平距离（单位为 twips*）。如果省略 xpos，则对话框会在水平方向居中。 |
| ypos | 可选。数值表达式，用于指定对话框的上边缘与屏幕上边缘的垂直距离（单位为 twips*）。如果省略 ypos，则对话框显示在屏幕垂直方向距下边缘大约三分之一处。 |
| helpfile | 可选。字符串表达式，用于标识为对话框提供上下文相关帮助的帮助文件。必须与 context 参数一起使用。 |
| context | 可选。数值表达式，用于标识由帮助文件的作者指定给某个帮助主题的上下文编号。必须与 helpfile 参数一起使用。 |



* twip 是度量单位，在视觉上与系统显示的相同。

1 twip 为 1/1440 英寸。


## 实例


## 实例 1


```
<script type="text/vbscript">

Function myFunction()
fname=InputBox("Enter your name")
End Function

</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_inputbox_func)


## 实例 2


带有标题的提示框：


```
<script type="text/vbscript">

Function myFunction()
fname=InputBox("Enter your name","Userinput")

End Function

</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_inputbox_func2)


## 实例 3


带有输入框默认文本的提示框：


```
<script type="text/vbscript">

Function myFunction()
fname=InputBox("Enter your name",,"Donald Duck")
End Function

</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_inputbox_func3)


## 实例 4


一个显示在距屏幕左边缘 700 twips* 位置的提示框。


```
<script type="text/vbscript">

Function myFunction()
fname=InputBox("Enter your name",,,700)

End Function

</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_inputbox_func4)


## 实例 5


一个显示在距屏幕上边缘 500 twips* 位置的提示框。


```
<script type="text/vbscript">

Function myFunction()
fname=InputBox("Enter your name",,,,500)
End Function

</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_inputbox_func5)


---


[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript GetRef 函数](https://www.runoob.com/func-getref.html)
			[VBScript IsEmpty 函数](https://www.runoob.com/func-isempty.html) **













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