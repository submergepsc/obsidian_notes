# XML 注意事项

- Source: https://www.runoob.com/xml/xml-dont.html

---


这里列出了您在使用 XML 时应该尽量避免使用的技术。


---


## Internet Explorer - XML 数据岛


**它是什么？**XML 数据岛是嵌入到 HTML 页面中的 XML 数据。


**为什么要避免使用它？**XML 数据岛只在 Internet Explorer 浏览器中有效。


**用什么代替它？**您应当在 HTML 中使用 JavaScript 和 XML DOM 来解析并显示 XML。


如需更多有关 JavaScript 和 XML DOM 的信息，请访问我们的 [XML DOM 教程](https://www.runoob.com/../dom/dom-tutorial.html)。


---


## XML 数据岛实例


本例使用 XML 文档 "[cd_catalog.xml](https://www.runoob.com/try/xml/cd_catalog.xml)"。


把 XML 文档绑定到 HTML 文档中的一个  标签。id 属性定义数据岛的标识符，而 src 属性指向 XML 文件：


## 实例


本实例只适用于 IE 浏览器


```xml
<html>
<body>
<xml id="cdcat" src="cd_catalog.xml"></xml>
<table border="1" datasrc="#cdcat">
<tr>
<td><span datafld="ARTIST"></span></td>
<td><span datafld="TITLE"></span></td>
</tr>
</table>
</body>
</html>
```


**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=cd_catalog_island)


 标签的 datasrc 属性把 HTML 表格绑定到 XML 数据岛。


 标签允许 datafld 属性引用要显示的 XML 元素。在这个实例中，要引用的是 "ARTIST" 和 "TITLE"。当读取 XML 时，会为每个  元素创建相应的表格行。


---


## Internet Explorer - 行为


它是什么？**Internet Explorer 5 引入了行为。行为是通过使用 CSS 样式向 XML （或 HTML ）元素添加行为的一种方法。


**为什么要避免使用它？**只有 Internet Explorer 支持 behavior 属性。


**使用什么代替它？**使用 JavaScript 和 XML DOM（或 HTML DOM）来代替它。


## 实例 1 - 鼠标悬停突出


下面的 HTML 文件中的  元素为  元素定义了一个行为：


```xml
<html>
<head>
<style type="text/css">
h1 { behavior: url(behave.htc) }
</style>
</head>
<body>
<h1>Mouse over me!!!</h1>
</body>
</html>
```


下面显示的是 XML 文档 "behave.htc"（该文件包含了一段 JavaScript 和针对元素的事件句柄）：


```xml
<attach for="element" event="onmouseover" handler="hig_lite" />
<attach for="element" event="onmouseout" handler="low_lite" />
<script>
function hig_lite()
{
element.style.color='red';
}
function low_lite()
{
element.style.color='blue';
}
</script>
```


**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=behave)


## 实例 2 - 打字机模拟


下面的 HTML 文件中的  元素为 id 为 "typing" 的元素定义了一个行为：


```xml
<html>
<head>
<style type="text/css">
#typing
{
behavior:url(typing.htc);
font-family:'courier new';
}
</style>
</head>
<body>
<span id="typing" speed="100">IE5 introduced DHTML behaviors.
Behaviors are a way to add DHTML functionality to HTML elements
with the ease of CSS.<br /><br />How do behaviors work?<br />
By using XML we can link behaviors to any element in a web page
and manipulate that element.</p>v
</span>
</body>
</html>
```


下面显示的是 XML 文档 "typing.htc"：


```xml
<attach for="window" event="onload" handler="beginTyping" />
<method name="type" />
<script>
var i,text1,text2,textLength,t;
function beginTyping()
{
i=0;
text1=element.innerText;
textLength=text1.length;
element.innerText="";
text2="";
t=window.setInterval(element.id+".type()",speed);
}
function type()
{
text2=text2+text1.substring(i,i+1);
element.innerText=text2;
i=i+1;
if (i==textLength)
  {
  clearInterval(t);
  }
}
</script>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=behave_typing)










	  AI 思考中...





			** [XML DOM 高级](https://www.runoob.com/xml-dom-advanced.html)
			[XML 技术](https://www.runoob.com/xml-technologies.html) **













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

      : ·[XML 实例](https://www.runoob.com/xml-examples.html)

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