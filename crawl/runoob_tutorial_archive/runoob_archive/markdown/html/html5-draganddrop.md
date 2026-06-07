# HTML5 拖放（Drag 和 Drop）

- Source: https://www.runoob.com/html/html5-draganddrop.html

---


拖放（Drag 和 drop）是 HTML5 标准的组成部分。


---


![](https://www.runoob.com/images/logo.png)


将 **RUNOOB.COM** 图标拖动到矩形框中。


---


## 拖放


拖放是一种常见的特性，即抓取对象以后拖到另一个位置。


在 HTML5 中，拖放是标准的一部分，任何元素都能够拖放。


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9+, Firefox, Opera, Chrome, 和 Safari 支持拖动。


**注意:**Safari 5.1.2不支持拖动.


---


## HTML5 拖放实例


下面的例子是一个简单的拖放实例：


## 实例


```html
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
<style type="text/css">
#div1 {width:350px;height:70px;padding:10px;border:1px solid #aaaaaa;}
</style>
<script>
function allowDrop(ev)
{
    ev.preventDefault();
}

function drag(ev)
{
    ev.dataTransfer.setData("Text",ev.target.id);
}

function drop(ev)
{
    ev.preventDefault();
    var data=ev.dataTransfer.getData("Text");
    ev.target.appendChild(document.getElementById(data));
}
</script>
</head>
<body>

<p>拖动 RUNOOB.COM 图片到矩形框中:</p>

<div id="div1" ondrop="drop(event)" ondragover="allowDrop(event)"></div>
<br>
<img id="drag1" src="/images/logo.png" draggable="true" ondragstart="drag(event)" width="336" height="69">

</body>
</html>
```



**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_draganddrop)


它看上去也许有些复杂，不过我们可以分别研究拖放事件的不同部分。


---


## 设置元素为可拖放


首先，为了使元素可拖动，把 draggable 属性设置为 true ：


	<img draggable="true">


---


## 拖动什么 - ondragstart 和 setData()


然后，规定当元素被拖动时，会发生什么。


在上面的例子中，ondragstart 属性调用了一个函数，drag(event)，它规定了被拖动的数据。


dataTransfer.setData() 方法设置被拖数据的数据类型和值：



		function drag(ev)
{
    ev.dataTransfer.setData("Text",ev.target.id);

		}


Text 是一个 DOMString 表示要添加到 drag object 的拖动数据的类型。值是可拖动元素的 id ("drag1")。


---


## 放到何处 - ondragover


ondragover 事件规定在何处放置被拖动的数据。


默认地，无法将数据/元素放置到其他元素中。如果需要设置允许放置，我们必须阻止对元素的默认处理方式。


这要通过调用 ondragover 事件的 event.preventDefault() 方法：



		*event*.preventDefault()


---


## 进行放置 - ondrop


当放置被拖数据时，会发生 drop 事件。


在上面的例子中，ondrop 属性调用了一个函数，drop(event)：



		function drop(ev)

	{

	    ev.preventDefault();

	    var data=ev.dataTransfer.getData("Text");

	    ev.target.appendChild(document.getElementById(data));

	}


代码解释：


- 调用 preventDefault() 来避免浏览器对数据的默认处理（drop 事件的默认行为是以链接形式打开）
- 通过 dataTransfer.getData("Text") 方法获得被拖的数据。该方法将返回在 setData() 方法中设置为相同类型的任何数据。
- 被拖数据是被拖元素的 id ("drag1")
- 把被拖元素追加到放置元素（目标元素）中


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[来回拖放图片](https://www.runoob.com/try/try.php?filename=tryhtml5_draganddrop2) 如何在两个  元素之间拖放图像。








	  AI 思考中...





			** [HTML5 SVG](https://www.runoob.com/html5-svg.html)
			[HTML5 地理定位](https://www.runoob.com/html5-geolocation.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/html-examples.html)

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