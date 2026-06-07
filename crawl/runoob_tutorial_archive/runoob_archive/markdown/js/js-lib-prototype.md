# JavaScript - 测试 Prototype

- Source: https://www.runoob.com/js/js-lib-prototype.html

---


测试 JavaScript 框架库 - Prototype


---


## 引用 Prototype


如需测试 JavaScript 库，您需要在网页中引用它。


为了引用某个库，请使用  标签，其 src 属性设置为库的 URL：


## 引用 Prototype


```javascript
<!DOCTYPE html>
<html>
<head>
<script
src="https://cdn.staticfile.org/prototype/1.7.3/prototype.min.js">
</script>
</head>
<body>
</body>
</html>
```


**
---


## Prototype 描述


Prototype 提供的函数可使 HTML DOM 编程更容易。


与 jQuery 类似，Prototype 也有自己的 $() 函数。


$() 函数接受 HTML DOM 元素的 id 值（或 DOM 元素），并会向 DOM 对象添加新的功能。


与 jQuery 不同，Prototype 没有用以取代 window.onload() 的 ready() 方法。相反，Prototype 会向浏览器及 HTML DOM 添加扩展。


在 JavaScript 中，您可以分配一个函数以处理窗口加载事件：


## JavaScript 方式：


```javascript
function myFunction()
{
    var obj=document.getElementById("h01");
    obj.innerHTML="Hello Prototype";
}
onload=myFunction;
```


等价的 Prototype 是不同的：


## Prototype 方式：


```javascript
function myFunction()
{
    $("h01").insert("Hello Prototype!");
}
Event.observe(window,"load",myFunction);
```


Event.observe() 接受三个参数：


- 您希望处理的 HTML DOM 或 BOM（浏览器对象模型）对象
- 您希望处理的事件
- 您希望调用的函数


---


## 测试 Prototype


请试一下下面这个例子：


## Example


```javascript
<!DOCTYPE html>
<html>
<script src="https://cdn.staticfile.org/prototype/1.7.3/prototype.min.js">
</script>
<script>
function myFunction()
{
    $("h01").insert("Hello Prototype!");
}
Event.observe(window,"load",myFunction);
</script>
</head>
<body>
<h1 id="h01"></h1>
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_lib_prototype)


请再试一下这个例子：


## Example


```javascript
<!DOCTYPE html>
<html>
<script src="https://cdn.staticfile.org/prototype/1.7.3/prototype.min.js">
</script>
<script>
function myFunction()
{
    $("h01").writeAttribute("style","color:red").insert("Hello Prototype!");
}
Event.observe(window,"load",myFunction);
</script>
</head>
<body>
<h1 id="h01"></h1>
</body>
</html>
```


[测试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_lib_prototype2)


正如您在上面的例子中看到的，与 jQuery 相同，Prototype 允许链式语法。


链接（Chaining）是一种在同一对象上执行多个任务的便捷方法。








	  AI 思考中...





			** [JavaScript 测试 jQuery](https://www.runoob.com/js-lib-jquery.html)
			[JavaScript 实例](https://www.runoob.com/js-examples.html) **













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