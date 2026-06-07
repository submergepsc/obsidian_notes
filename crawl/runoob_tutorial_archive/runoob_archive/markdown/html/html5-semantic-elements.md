# HTML5 语义元素

- Source: https://www.runoob.com/html/html5-semantic-elements.html

---


语义= 意义


语义元素 = 有意义的元素


---


## 什么是语义元素?


一个语义元素能够清楚的描述其意义给浏览器和开发者。


**无语义** 元素实例:  和  - 无需考虑内容.


**语义**元素实例: , , and  - 清楚的定义了它的内容.


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9+, Firefox, Chrome, Safari 和 Opera 支持语义元素。


**注意:** Internet Explorer 8 及更早版本不支持该元素。 但是文章底部提供了兼容的解决方法.


---


## HTML5中新的语义元素


许多现有网站都包含以下HTML代码： , , 或者 , 来指明导航链接, 头部, 以及尾部.


HTML5 提供了新的语义元素来明确一个Web页面的不同部分:


-
-
-
-
-
-
-
-


![](https://www.runoob.com/wp-content/uploads/2013/07/html5-layout.jpg)

---


## HTML5 元素


 标签定义文档中的节（section、区段）。比如章节、页眉、页脚或文档中的其他部分。


根据W3C HTML5文档: section 包含了一组内容及其标题。


## 实例


```html
<section>
  <h1>WWF</h1>
  <p>The World Wide Fund for Nature (WWF) is....</p>
</section>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_section)


---


## HTML5 元素


 标签定义独立的内容。.


 元素使用实例:


- Forum post
- Blog post
- News story
- Comment


## 实例


```html
<article>
  <h1>Internet Explorer 9</h1>
  <p>Windows Internet Explorer 9(缩写为 IE9 )在2011年3月14日21:00 发布。</p>
</article>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_article)


---


## HTML5 元素


 标签定义导航链接的部分。


 元素用于定义页面的导航链接部分区域，但是，不是所有的链接都需要包含在  元素中!


## 实例


```html
<nav>
    <a href="/html/">HTML</a> |
    <a href="/css/">CSS</a> |
    <a href="/js/">JavaScript</a> |
    <a href="/jquery/">jQuery</a>
</nav>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_nav)


---


## HTML5 元素


 标签定义页面主区域内容之外的内容（比如侧边栏）。


aside 标签的内容应与主区域的内容相关.


## 实例


```html
<p>My family and I visited The Epcot center this summer.</p>

<aside>
  <h4>Epcot Center</h4>
  <p>The Epcot Center is a theme park in Disney World, Florida.</p>
</aside>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_aside)


---


## HTML5 元素


元素描述了文档的头部区域


元素主要用于定义内容的介绍展示区域.


在页面中你可以使用多个 元素.


以下实例定义了文章的头部:


## 实例


```html
<article>
  <header>
    <h1>Internet Explorer 9</h1>
    <p><time pubdate datetime="2011-03-15"></time></p>
  </header>
  <p>Windows Internet Explorer 9(缩写为 IE9 )是在2011年3月14日21:00发布的</p>
</article>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_header)


---


## HTML5 元素


 元素描述了文档的底部区域.


 元素应该包含它的包含元素


一个页脚通常包含文档的作者，著作权信息，链接的使用条款，联系信息等


文档中你可以使用多个 元素.


## 实例


```html
<footer>
  <p>Posted by: Hege Refsnes</p>
  <p><time pubdate datetime="2012-03-01"></time></p>
</footer>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_footer)


---


## HTML5 和 元素


标签规定独立的流内容（图像、图表、照片、代码等等）。


 元素的内容应该与主内容相关，但如果被删除，则不应对文档流产生影响。


 标签定义  元素的标题.


元素应该被置于 "figure" 元素的第一个或最后一个子元素的位置。


## 实例


```html
<figure>
  <img src="img_pulpit.jpg" alt="The Pulpit Rock" width="304" height="228">
  <figcaption>Fig1. - The Pulpit Pock, Norway.</figcaption>
</figure>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_figcaption)


---


## 我们可以开始使用这些语义元素吗?


以上的元素都是块元素(除了).


为了让这些块级元素在所有版本的浏览器中生效，你需要在样式表文件中设置一下属性 (以下样式代码可以让旧版本浏览器支持本章介绍的块级元素):


header, section, footer, aside, nav, article, figure

{

    display: block;

}


## Internet Explorer 8 及更早IE版本中的问题


IE8 及更早IE版本无法在这些元素中渲染CSS效果，以至于你不能使用 , , , , , , , 或者其他的HTML5 elements.


解决办法:** 你可以使用HTML5 Shiv Javascript脚本来解决IE的兼容问题。HTML5 Shiv下载地址：[https://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/html5shiv/3.7.3/html5shiv.min.js](https://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/html5shiv/3.7.3/html5shiv.min.js)


下载后，将以下代码放入到网页中：


<!--[if lt IE 9]>**<script src="html5shiv.js"></script>

<![endif]-->

以上代码在浏览器小于IE9版本时会加载html5shiv.js文件. 你必须将其放置于 元素中，因为 IE浏览器需要在头部加载后渲染这些HTML5的新元素








	  AI 思考中...





			** [HTML5 表单属性](https://www.runoob.com/html5-form-attributes.html)
			[HTML5 Web 存储](https://www.runoob.com/html5-webstorage.html) **













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