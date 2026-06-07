# JavaScript HTML DOM 事件

- Source: https://www.runoob.com/js/js-htmldom-events.html

---


HTML DOM 使 JavaScript 有能力对 HTML 事件做出反应。


## 实例


```javascript
Mouse Over Me
```


	Click Me




**
---


## 对事件做出反应


我们可以在事件发生时执行 JavaScript，比如当用户在 HTML 元素上点击时。


如需在用户点击某个元素时执行代码，请向一个 HTML 事件属性添加 JavaScript 代码：


onclick=*JavaScript*


HTML 事件的例子：


- 当用户点击鼠标时
- 当网页已加载时
- 当图像已加载时
- 当鼠标移动到元素上时
- 当输入字段被改变时
- 当提交 HTML 表单时
- 当用户触发按键时


在本例中，当用户在  元素上点击时，会改变其内容：


## 实例


```javascript
<!DOCTYPE html><html>
<body>
<h1 onclick="this.innerHTML='Ooops!'">点击文本!</h1>
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trydhtml_event_onclick2)


本例从事件处理器调用一个函数：


## 实例


```javascript
<!DOCTYPE html><html>
<head>
<script>
function changetext(id)
{
    id.innerHTML="Ooops!";
}
</script>
</head>
<body>
<h1 onclick="changetext(this)">点击文本!</h1>
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trydhtml_event_onclick3)


---


## HTML 事件属性


如需向 HTML 元素分配 事件，您可以使用事件属性。


## 实例


向 button 元素分配 onclick 事件：


```javascript
<button
	onclick="displayDate()">点这里</button>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_events1)


在上面的例子中，名为 displayDate 的函数将在按钮被点击时执行。


---


## 使用 HTML DOM 来分配事件


HTML DOM 允许您使用 JavaScript 来向 HTML 元素分配事件：


## 实例


向 button 元素分配 onclick 事件：



```javascript
<script>document.getElementById("myBtn").onclick=function(){displayDate()};
	</script>
```




	[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_events2)


在上面的例子中，名为 displayDate 的函数被分配给 id="myBtn" 的 HTML 元素。


按钮点击时Javascript函数将会被执行。


---


## onload 和 onunload 事件


onload 和 onunload 事件会在用户进入或离开页面时被触发。


onload 事件可用于检测访问者的浏览器类型和浏览器版本，并基于这些信息来加载网页的正确版本。


onload 和 onunload 事件可用于处理 cookie。


## 实例


```javascript
<body onload="checkCookies()">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_events_onload)


---


## onchange 事件


onchange 事件常结合对输入字段的验证来使用。


下面是一个如何使用 onchange 的例子。当用户改变输入字段的内容时，会调用 upperCase() 函数。


## 实例


```javascript
<input type="text" id="fname"
onchange="upperCase()">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_onchange)


---


## onmouseover 和 onmouseout 事件


onmouseover 和 onmouseout 事件可用于在用户的鼠标移至 HTML 元素上方或移出元素时触发函数。


## 实例


一个简单的 onmouseover-onmouseout 实例：


```javascript
Mouse Over Me
```





[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_events_mouseover)


---


## onmousedown、onmouseup 以及 onclick 事件


onmousedown, onmouseup 以及 onclick 构成了鼠标点击事件的所有部分。首先当点击鼠标按钮时，会触发 onmousedown 事件，当释放鼠标按钮时，会触发 onmouseup 事件，最后，当完成鼠标点击时，会触发 onclick 事件。


## 实例


一个简单的 onmousedown-onmouseup 实例：


```javascript
Thank You
```





---


## 更多实例


[onmousedown 和onmouseup](https://www.runoob.com/try/try.php?filename=trydhtml_event_onmousedown) 当用户按下鼠标按钮时，更换一幅图像。


[onload](https://www.runoob.com/try/try.php?filename=trydhtml_event_onload) 当页面完成加载时，显示一个提示框。



[onfocus](https://www.runoob.com/try/try.php?filename=tryjsref_onfocus) 当输入字段获得焦点时，改变其背景色。


[鼠标事件](https://www.runoob.com/try/try.php?filename=trydhtml_event_onmouse) 当指针移动到元素上方时，改变其颜色；当指针移出文本后，会再次改变其颜色。








	  AI 思考中...





			** [JavaScript HTML DOM 改变 CSS](https://www.runoob.com/js-htmldom-css.html)
			[JavaScript HTML DOM 元素 (节点)](https://www.runoob.com/js-htmldom-elements.html) **













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