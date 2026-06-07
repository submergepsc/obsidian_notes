# HTML 视频（Video）

- Source: https://www.runoob.com/html/html-videos.html

---


在 HTML 中播放视频的方法有很多种。


---


## HTML视频（Videos）播放


## 实例


```html
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
  <source src="movie.webm" type="video/webm">
  <object data="movie.mp4" width="320" height="240">
    <embed src="movie.swf" width="320" height="240">
  </object>
</video>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_video_html5_4)


---


## 问题以及解决方法


在 HTML 中播放视频并不容易！


您需要谙熟大量技巧，以确保您的视频文件在所有浏览器中（Internet Explorer, Chrome, Firefox, Safari, Opera）和所有硬件上（PC, Mac , iPad, iPhone）都能够播放。


在本章，菜鸟教程为您总结了问题和解决方法。


---


## 使用 标签


 标签的作用是在 HTML 页面中嵌入多媒体元素。


下面的 HTML 代码显示嵌入网页的 Flash 视频：


## 实例


```html
<embed src="intro.swf" height="200" width="200">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_videoembed)


问题**


- HTML4 无法识别 * 标签。您的页面无法通过验证。
- 如果浏览器不支持 Flash，那么视频将无法播放
- iPad 和 iPhone 不能显示 Flash 视频。
- 如果您将视频转换为其他格式，那么它仍然不能在所有浏览器中播放。


---


## 使用 标签


 标签的作用是在 HTML 页面中嵌入多媒体元素。


下面的 HTML 片段显示嵌入网页的一段 Flash 视频：


## 实例


```html
<object data="intro.swf" height="200" width="200"></object>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_videoobject)


问题:**


- 如果浏览器不支持 Flash，将无法播放视频。
- iPad 和 iPhone 不能显示 Flash 视频。
- 如果您将视频转换为其他格式，那么它仍然不能在所有浏览器中播放。


---


## 使用 HTML5 元素


HTML5  标签定义了一个视频或者影片.


 元素在所有现代浏览器中都支持。


以下 HTML 片段会显示一段嵌入网页的 ogg、mp4 或 webm 格式的视频：


## 实例


```html
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
  <source src="movie.webm" type="video/webm">
	您的浏览器不支持 video 标签。
	</video>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_video_html5)


问题:**


- 您必须把视频转换为很多不同的格式。
-  元素在老式浏览器中无效。


---


## 最好的 HTML 解决方法


以下实例中使用了 4 种不同的视频格式。HTML 5  元素会尝试播放以 mp4、ogg 或 webm 格式中的一种来播放视频。如果均失败，则回退到  元素。


## HTML 5 + +


```html
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
  <source src="movie.webm" type="video/webm">

	<object data="movie.mp4"
	width="320" height="240">
	    <embed src="movie.swf" width="320"
	height="240">

	</object>
	</video>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_video_html5_4)


问题:**


- 您必须把视频转换为很多不同的格式


---


## 使用超链接


如果网页包含指向媒体文件的超链接，大多数浏览器会使用"辅助应用程序"来播放文件。


以下代码片段显示指向 AVI 文件的链接。如果用户点击该链接，浏览器会启动"辅助应用程序"，比如 Windows Media Player 来播放这个 AVI 文件：


## 实例


```html
<a href="intro.swf">Play a video file</a>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_videolink)


---


## 关于内联视频的说明


当视频被包含在网页中时，它被称为内联视频。


如果您打算在 web 应用程序中使用内联视频，您需要意识到很多人都觉得内联视频令人恼火。


同时请注意，用户可能已经关闭了浏览器中的内联视频选项。


我们最好的建议是只在用户希望看到内联视频的地方包含它们。一个正面的例子是，在用户需要看到视频并点击某个链接时，会打开页面然后播放视频。


---


## HTML 多媒体标签


New : HTML5新标签.


| 标签 | 描述 |
| --- | --- |
|  | 定义内嵌对象。HTML4 中不赞成，HTML5 中允许。 |
|  | 定义内嵌对象。 |
|  | 定义对象的参数。 |
| New | 定义了声音内容 |
| New | 定义一个视频或者影片 |
| New | 定义了media元素的多媒体资源( 和 ) |
| New | 规定media元素的字幕文件或其他包含文本的文件 ( 和) |








	  AI 思考中...





			* [HTML 音频(Audio)](https://www.runoob.com/html-sounds.html)
			[HTML 实例](https://www.runoob.com/html-examples.html) **













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