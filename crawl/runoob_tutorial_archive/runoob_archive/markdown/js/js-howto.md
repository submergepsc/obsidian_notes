# JavaScript 用法

- Source: https://www.runoob.com/js/js-howto.html

---


HTML 中的 Javascript 脚本代码必须位于 **** 与 **** 标签之间。


Javascript 脚本代码可被放置在 HTML 页面的 **** 和 **** 部分中。


---


## 标签


如需在 HTML 页面中插入 JavaScript，请使用  标签。


 和  会告诉 JavaScript 在何处开始和结束。


 和  之间的代码行包含了 JavaScript:


```javascript
<script>
alert("我的第一个 JavaScript");
</script>
```


您无需理解上面的代码。只需明白，浏览器会解释并执行位于  和 之间的 JavaScript 代码


|  | 那些老旧的实例可能会在 标签中使用 type="text/javascript"。现在已经不必这样做了。JavaScript 是所有现代浏览器以及 HTML5 中的默认脚本语言。 |
| --- | --- |


---


## 中的 JavaScript


在本例中，JavaScript 会在页面加载时向 HTML 的  写文本：


## 实例


```javascript
<!DOCTYPE html>
<html>
<body>
.
.
<script>
document.write("<h1>这是一个标题</h1>");
document.write("<p>这是一个段落</p>");
</script>
.
.
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_intro_document_write)


---


## JavaScript 函数和事件


上面例子中的 JavaScript 语句，会在页面加载时执行。


通常，我们需要在某个事件发生时执行代码，比如当用户点击按钮时。


如果我们把 JavaScript 代码放入函数中，就可以在事件发生时调用该函数。


您将在稍后的章节学到更多有关 JavaScript 函数和事件的知识。


---


## 在 或者 的JavaScript


您可以在 HTML 文档中放入不限数量的脚本。


脚本可位于 HTML 的  或  部分中，或者同时存在于两个部分中。


通常的做法是把函数放入  部分中，或者放在页面底部。这样就可以把它们安置到同一处位置，不会干扰页面的内容。


---


## 中的 JavaScript 函数


在本例中，我们把一个 JavaScript 函数放置到 HTML 页面的  部分。


该函数会在点击按钮时被调用：




## 实例


```javascript
<!DOCTYPE html>
<html>
<head>
<script>
function myFunction()
{
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}
</script>
</head>
<body>
<h1>我的 Web 页面</h1>
<p id="demo">一个段落</p>
<button type="button" onclick="myFunction()">尝试一下</button>
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_whereto_head)


---


## 中的 JavaScript 函数


在本例中，我们把一个 JavaScript 函数放置到 HTML 页面的  部分。


该函数会在点击按钮时被调用：




## 实例


```javascript
<!DOCTYPE html>
<html>
<body>
<h1>我的 Web 页面</h1>
<p id="demo">一个段落</p>
<button type="button" onclick="myFunction()">尝试一下</button>
<script>
function myFunction()
{
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}
</script>
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_whereto_body)


---


## 外部的 JavaScript


也可以把脚本保存到外部文件中。外部文件通常包含被多个网页使用的代码。


外部 JavaScript 文件的文件扩展名是 .js。


如需使用外部文件，请在  标签的 "src" 属性中设置该 .js 文件：


## 实例


```javascript
<!DOCTYPE html>
<html>
<body>
<script src="myScript.js"></script>
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_externalexample)


你可以将脚本放置于  或者 中，放在  标签中的脚本与外部引用的脚本运行效果完全一致。


myScript.js 文件代码如下：


```javascript
function myFunction()
{
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}
```


|  | 外部脚本不能包含 标签。 |
| --- | --- |








	  AI 思考中...





			** [JavaScript 简介](https://www.runoob.com/js-intro.html)
			[JavaScript 输出](https://www.runoob.com/js-output.html) **