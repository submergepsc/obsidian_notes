# HTML canvas beginPath() 方法

- Source: https://www.runoob.com/tags/canvas-beginpath.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


在画布上绘制两条路径；绿色和紫色：


YourbrowserdoesnotsupporttheHTML5canvastag.



JavaScript：


```
var c=document.getElementById("myCanvas");var ctx=c.getContext("2d");
	ctx.beginPath();
	ctx.lineWidth="5";
	ctx.strokeStyle="green"; // Green path
	ctx.moveTo(0,75);
	ctx.lineTo(250,75);
	ctx.stroke(); // Draw it
	ctx.beginPath();
	ctx.strokeStyle="purple"; // Purple path
	ctx.moveTo(50,0);
	ctx.lineTo(150,130);
	ctx.stroke(); // Draw it
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_beginpath)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 beginPath() 方法。


注意：**Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


beginPath() 方法开始一条路径，或重置当前的路径。


**提示：**请使用这些方法来创建路径 moveTo()、lineTo()、quadricCurveTo()、bezierCurveTo()、arcTo() 和 arc()。


**提示：**请使用 [stroke()](https://www.runoob.com/canvas-stroke.html) 方法在画布上绘制确切的路径。


| JavaScript 语法： | context.beginPath(); |
| --- | --- |


---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas stroke() 方法](https://www.runoob.com/canvas-stroke.html)
			[HTML canvas moveTo() 方法](https://www.runoob.com/canvas-moveto.html) **