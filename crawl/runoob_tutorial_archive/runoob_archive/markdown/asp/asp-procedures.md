# ASP 子程序

- Source: https://www.runoob.com/asp/asp-procedures.html

---


在 ASP 中，您可通过 VBScript 调用 JavaScript 子程序，反之亦然。


---


## 子程序


ASP 源代码可包含子程序和函数：


## 实例


```
<!DOCTYPE html><html>
<head>
<%
sub vbproc(num1,num2)
response.write(num1*num2)
end sub
%>
</head>
<body>
<p>Result: <%call vbproc(3,4)%></p>
</body>
</html>
```


**[演示实例 »](https://www.runoob.com/try/showasp.php?filename=demo_vbproc)


将  这一行写在  标签的上面，就可以使用另一种脚本语言来编写子程序或者函数：


## 实例


```
<%@ language="javascript" %>
<!DOCTYPE html><html>
<head>
<%
function jsproc(num1,num2)
{
Response.Write(num1*num2)
}
%>
</head>
<body>
<p>Result: <%jsproc(3,4)%></p>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showasp.php?filename=demo_jsproc)


---


## VBScript 与 JavaScript 的不同


当从一个用 VBScript 编写的 ASP 文件中调用 VBScript 或者 JavaScript 子程序时，可以使用 "call" 关键词，后面跟着子程序名称。假如子程序需要参数，当使用 "call" 关键词时，参数必须包含在括号内。假如您省略了 "call" 关键词，则参数不必包含在括号内。如果子程序没有参数，那么括号则是可选的。


当从一个用 JavaScript 编写的 ASP 文件中调用 VBScript 或者 JavaScript 子程序时，必须在子程序名后使用括号。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[使用 VBScript 调用子程序](https://www.runoob.com/try/showasp.php?filename=demo_vbproc2) 本例演示如何在一个 ASP 文件中调用 VBScript 子程序和 JavaScript 子程序。










	  AI 思考中...





			** [ASP 变量](https://www.runoob.com/asp-variables.html)
			[ASP 表单](https://www.runoob.com/asp-inputforms.html) **













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