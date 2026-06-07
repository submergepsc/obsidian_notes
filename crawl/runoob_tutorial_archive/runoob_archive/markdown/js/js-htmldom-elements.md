# JavaScript HTML DOM 元素 (节点)

- Source: https://www.runoob.com/js/js-htmldom-elements.html

本章节介绍如何向文档中添加和移除元素(节点)。


---


## 创建新的 HTML 元素 (节点) - appendChild()


要创建新的 HTML 元素 (节点)需要先创建一个元素，然后在已存在的元素中添加它。


## 实例


```javascript
<div id="div1">
<p id="p1">这是一个段落。</p>
<p id="p2">这是另外一个段落。</p>
</div>

<script>
var para = document.createElement("p");
var node = document.createTextNode("这是一个新的段落。");
para.appendChild(node);

var element = document.getElementById("div1");
element.appendChild(para);
</script>
```


**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_dom_elementcreate)


---


### 实例解析


以下代码是用于创建  元素:


```
var para = document.createElement("p");
```


为  元素创建一个新的文本节点：


```
var node = document.createTextNode("这是一个新的段落。");
```


将文本节点添加到  元素中：


```
para.appendChild(node);
```


最后，在一个已存在的元素中添加 p 元素。


查找已存在的元素：


```
var element = document.getElementById("div1");
```


添加到已存在的元素中:


```
element.appendChild(para);
```


---


## 创建新的 HTML 元素 (节点) - insertBefore()


以上的实例我们使用了 **appendChild()** 方法，它用于添加新元素到尾部。


如果我们需要将新元素添加到开始位置，可以使用 **insertBefore()** 方法:


## 实例


```javascript
<div id="div1">
<p id="p1">这是一个段落。</p>
<p id="p2">这是另外一个段落。</p>
</div>

<script>
var para = document.createElement("p");
var node = document.createTextNode("这是一个新的段落。");
para.appendChild(node);

var element = document.getElementById("div1");
var child = document.getElementById("p1");
element.insertBefore(para, child);
</script>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_dom_elementcreate2)


---


## 移除已存在的元素


要移除一个元素，你需要知道该元素的父元素。


## 实例


```javascript
<div id="div1">
<p id="p1">这是一个段落。</p>
<p id="p2">这是另外一个段落。</p>
</div>

<script>
var parent = document.getElementById("div1");
var child = document.getElementById("p1");
parent.removeChild(child);
</script>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_dom_elementremove)


注意：**早期的 Internet Explorer 浏览器不支持 node.remove() 方法。


### 实例解析


HTML 文档中  元素包含两个子节点 (两个  元素):


```
<div id="div1">
<p id="p1">这是一个段落。</p>
<p id="p2">这是另外一个段落。</p>
</div>
```


查找 id="div1" 的元素:


```
var parent = document.getElementById("div1");
```


查找 id="p1" 的  元素:


```
var child = document.getElementById("p1");
```


从父元素中移除子节点：


```
parent.removeChild(child);
```


|  | 如果能够在不引用父元素的情况下删除某个元素，就太好了。不过很遗憾。DOM 需要清楚您需要删除的元素，以及它的父元素。 |
| --- | --- |


以下代码是已知要查找的子元素，然后查找其父元素，再删除这个子元素（删除节点必须知道父节点）：


```
var child = document.getElementById("p1");
child.parentNode.removeChild(child);
```


---


## 替换 HTML 元素 - replaceChild()


我们可以使用 replaceChild() 方法来替换 HTML DOM 中的元素。


## 实例


```javascript
<div id="div1">
<p id="p1">这是一个段落。</p>
<p id="p2">这是另外一个段落。</p>
</div>

<script>
var para = document.createElement("p");
var node = document.createTextNode("这是一个新的段落。");
para.appendChild(node);

var parent = document.getElementById("div1");
var child = document.getElementById("p1");
parent.replaceChild(para, child);
</script>
```


**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_dom_elementreplace)


---


## HTML DOM 教程


在我们的 JavaScript 教程的 HTML DOM 部分，您已经学到了：


- 如何改变 HTML 元素的内容 (innerHTML)
- 如何改变 HTML 元素的样式 (CSS)
- 如何对 HTML DOM 事件作出反应
- 如何添加或删除 HTML 元素


如果您希望学到更多有关使用 JavaScript 访问 HTML DOM 的知识，请访问我们完整的 [HTML DOM 教程](https://www.runoob.com/../htmldom/htmldom-tutorial.html)。









	  AI 思考中...





			** [JavaScript HTML DOM 事件](https://www.runoob.com/js-htmldom-events.html)
			[JavaScript 对象](https://www.runoob.com/js-objects.html) **













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