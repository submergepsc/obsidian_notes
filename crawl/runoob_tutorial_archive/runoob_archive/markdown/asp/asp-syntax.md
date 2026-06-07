# ASP 基本语法规则

- Source: https://www.runoob.com/asp/asp-syntax.html

---


在我们的 ASP 教程中，每个实例都提供隐藏的 ASP 源代码。这样会使您更容易理解它们的工作原理。


---


## 向浏览器写输出


ASP 文件通常包含 HTML 标签，就像 HTML 文件。然而，ASP 文件也能包含服务器脚本，这些脚本被分隔符  包围起来。


服务器脚本**在服务器上执行**，可包含你所选用的脚本语言的合法的表达式、语句、程序或者运算符。


### response.write 命令


response.write 命令用来向浏览器写输出。下面的实例向浏览器传送了一段文本："Hello World"：


## 实例


```
<!DOCTYPE html><html>
<body><%
response.write("Hello World!")
%>
</body>
</html>
```


**[演示实例 »](https://www.runoob.com/try/showasp.php?filename=demo_text)


还有一种 response.write 命令的简写方法。下面的实例也是向浏览器传送了一段文本："Hello World"：


## 实例


```
<!DOCTYPE html><html>
<body><%
="Hello World!"
%>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showasp.php?filename=demo_text_sh)


---


## 在 ASP 中使用 VBScript


您可以在 ASP 中使用若干种脚本语言。然而，默认的脚本语言是 VBScript：


	<!DOCTYPE html>
<html>

<body>

<%

response.write("Hello World!")

%>

</body>

</html>


上面的实例向文档的 body 部分写入了文本 "Hello World!"。


---


## 在 ASP 中使用 JavaScript


如果需要设置 JavaScript 为某个特定页面的默认脚本语言，您必须在页面的顶部插入一行语言说明：


<%@ language="javascript"%>

	<!DOCTYPE html>
<html>

<body>

<%

Response.Write("Hello World!")

%>

</body>

</html>

注释：**与 VBScript 不同，JavaScript 对大小写敏感！你必须根据 JavaScript 的需要使用不同的大小写字母编写您的 ASP 代码。


---


## 其他的脚本语言


ASP 与 VBScript 和 JScript（JScript 是微软的 JavaScript 实现）的配合是原生性的。如果您想要使用其他语言编写脚本，比如 PERL、REXX 或者 Python，您必须安装相应的脚本引擎。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[给文本添加一些 HTML 标签](https://www.runoob.com/try/showasp.php?filename=demo_formatting)

**







	  AI 思考中...





			** [在自己的 PC 上运行 ASP](https://www.runoob.com/asp-install.html)
			[ASP 变量](https://www.runoob.com/asp-variables.html) **













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