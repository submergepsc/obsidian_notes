# VBScript 程序

- Source: https://www.runoob.com/vbscript/vbscript-procedures.html

---


VBScript 可使用两种程序：


- 子程序
- 函数程序

**
---


## VBScript 子程序


子程序：


- 是一系列的语句，被封装在 Sub 和 End Sub 语句内
- 可执行某些操作，但**不会返回**值
- 可带有参数


Sub mysub()


*some statements*

End Sub

或者


Sub mysub(argument1,argument2)


 *some statements*

End Sub


## 实例（仅适用于 IE）


```
Sub mysub()
   document.write("I was written by a sub procedure")
End Sub
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_subex)


---


## VBScript 函数程序


函数程序


- 是一系列的语句，被封装在 Function 和 End Function 语句内
- 可执行某些操作，并**会返回**值
- 可带有通过程序调用来向其传递的参数。
- 如果没有参数，必须带有空的圆括号 ()
- 通过向函数程序名赋值的方式，可使其返回值


Function myfunction()


 *some statements*


 myfunction=*some value*

End Function

或者


Function myfunction(argument1,argument2)


 *some statements*


 myfunction=*some value*

End Function


## 实例（仅适用于 IE）


```
function myfunction()
   myfunction=Date()
end function
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_functionex)


---


## 调用程序


这个简单的函数程序被调用来计算两个参数的和：


## 实例（仅适用于 IE）


```
Function myfunction(a,b)
myfunction=a+b
End Function

document.write(myfunction(5,9))
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_proc_calc)


函数 "myfunction" 将返回参数 "a" 和参数 "b" 的和。这里返回的是 14。


当您调用程序时，您可以使用 Call 语句，如下所示：


Call MyProc(argument)


或者，您可以省略 Call 语句，如下所示：


MyProc argument









	  AI 思考中...





			** [VBScript 变量](https://www.runoob.com/vbscript-variables.html)
			[VBScript 条件语句](https://www.runoob.com/vbscript-conditionals.html) **













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