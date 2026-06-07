# JavaScript - 测试 jQuery

- Source: https://www.runoob.com/js/js-lib-jquery.html

---


测试 JavaScript 框架库 - jQuery


---


## 引用 jQuery


如需测试 JavaScript 库，您需要在网页中引用它。


为了引用某个库，请使用  标签，其 src 属性设置为库的 URL：


## 引用 jQuery


```javascript
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.staticfile.org/jquery/1.8.3/jquery.min.js">
</script>
</head>
<body>
</body>
</html>
```


**
---


## jQuery 描述


主要的 jQuery 函数是 $() 函数（jQuery 函数）。如果您向该函数传递 DOM 对象，它会返回 jQuery 对象，带有向其添加的 jQuery 功能。


jQuery 允许您通过 CSS 选择器来选取元素。


在 JavaScript 中，您可以分配一个函数以处理窗口加载事件：


## JavaScript 方式：


```javascript
function myFunction()
{
    var obj=document.getElementById("h01");
    obj.innerHTML="Hello jQuery";
}
onload=myFunction;
```


等价的 jQuery 是不同的：


## jQuery 方式：


```javascript
function myFunction()
{
    $("#h01").html("Hello jQuery");
}
$(document).ready(myFunction);
```


上面代码的最后一行，HTML DOM 文档对象被传递到 jQuery ：$(document)。


当您向 jQuery 传递 DOM 对象时，jQuery 会返回以 HTML DOM 对象包装的 jQuery 对象。


jQuery 函数会返回新的 jQuery 对象，其中的 ready() 是一个方法。


由于在 JavaScript 中函数就是变量，因此可以把 myFunction 作为变量传递给 jQuery 的 ready 方法。


|  | jQuery 返回 jQuery 对象，与已传递的 DOM 对象不同。jQuery 对象拥有的属性和方法，与 DOM 对象的不同。您不能在 jQuery 对象上使用 HTML DOM 的属性和方法。 |
| --- | --- |


---


## 测试 jQuery


请试一下下面这个例子：


## 实例


```javascript
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.staticfile.org/jquery/1.8.3/jquery.min.js">
</script>
<script>
function myFunction()
{
    $("#h01").html("Hello jQuery")
}
$(document).ready(myFunction);
</script>
</head>
<body>
<h1 id="h01"></h1>
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_lib_jquery)


请再试一下这个例子：


## 实例


```javascript
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.staticfile.org/jquery/1.8.3/jquery.min.js">
</script>
<script>
function myFunction()
{
    $("#h01").attr("style","color:red").html("Hello jQuery")
}
$(document).ready(myFunction);
</script>
</head>
<body>
<h1 id="h01"></h1>
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_lib_jquery2)


正如您在上面的例子中看到的，jQuery 允许链接（链式语法）。


链接（Chaining）是一种在同一对象上执行多个任务的便捷方法。


需要学习更多内容吗？菜鸟教程为您提供了非常棒的 [jQuery 教程](https://www.runoob.com/../jquery/index.html)。








	  AI 思考中...





			** [JavaScript 库](https://www.runoob.com/js-libraries.html)
			[JavaScript 测试 Prototype](https://www.runoob.com/js-lib-prototype.html) **













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

      : ·[JavaScript 实例](https://www.runoob.com/js-examples.html)

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