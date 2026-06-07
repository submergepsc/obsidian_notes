# HTML5 简介

- Source: https://www.runoob.com/html/html5-intro.html

![HTML](https://www.runoob.com/wp-content/uploads/2013/07/pic_html5.gif)

HTML5是HTML最新的修订版本，2014年10月由万维网联盟（W3C）完成标准制定。


HTML5的设计目的是为了在移动设备上支持多媒体。


HTML5 简单易学。


---

## 什么是 HTML5?


HTML5 是下一代 HTML 标准。


HTML , HTML 4.01的上一个版本诞生于 1999 年。自从那以后，Web 世界已经经历了巨变。


HTML5 仍处于完善之中。然而，大部分现代浏览器已经具备了某些 HTML5 支持。


---

## HTML5 是如何起步的？


HTML5 是 W3C 与 WHATWG 合作的结果,WHATWG 指 Web Hypertext Application Technology Working Group。


WHATWG 致力于 web 表单和应用程序，而 W3C 专注于 XHTML 2.0。在 2006 年，双方决定进行合作，来创建一个新版本的 HTML。


HTML5 中的一些有趣的新特性：


- 用于绘画的 canvas 元素
- 用于媒介回放的 video 和 audio 元素
- 对本地离线存储的更好的支持
- 新的特殊内容元素，比如 article、footer、header、nav、section
- 新的表单控件，比如 calendar、date、time、email、url、search


---

## HTML5


 声明必须位于 HTML5 文档中的第一行,使用非常简单:


```html
<!DOCTYPE html>
```


---

## 最小的HTML5文档


下面是一个简单的HTML5文档：


```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>文档标题</title>
</head>

<body>
文档内容......
</body>

</html>
```


**
注意：**对于中文网页需要使用 **** 声明编码，否则会出现乱码。


---


## HTML5 的改进


- 新元素
- 新属性
- 完全支持 CSS3
- Video 和 Audio
- 2D/3D 制图
- 本地存储
- 本地 SQL 数据
- Web 应用


---


## HTML5 多媒体


使用 HTML5 你可以简单的在网页中播放 视频(video)与音频 (audio) 。


- HTML5
- HTML5


---


## HTML5 应用


使用 HTML5 你可以简单地开发应用


- 本地数据存储
- 访问本地文件
- 本地 SQL 数据
- 缓存引用
- Javascript 工作者
- XHTMLHttpRequest 2


---


## HTML5 图形


使用 HTML5 你可以简单的绘制图形:


- 使用 元素。
- 使用内联 [SVG](https://www.runoob.com/html5-svg.html)。
- 使用 [CSS3 2D 转换](https://www.runoob.com/../css3/css3-2dtransforms.html)、[CSS3 3D 转换](https://www.runoob.com/../css3/css3-3dtransforms.html)。


---


## HTML5 使用 CSS3


- 新选择器
- 新属性
- 动画
- 2D/3D 转换
- 圆角
- 阴影效果
- 可下载的字体


了解更多CSS3知识请查看本站的 [CSS3 教程。](https://www.runoob.com/../css3/css3-tutorial.html)


---


## 语义元素


HTML5 添加了很多语义元素如下所示：


| 标签 | 描述 |
| --- | --- |
|  | 定义页面独立的内容区域。 |
|  | 定义页面的侧边栏内容。 |
|  | 允许您设置一段文本，使其脱离其父元素的文本方向设置。 |
|  | 定义命令按钮，比如单选按钮、复选框或按钮 |
|  | 用于描述文档或文档某个部分的细节 |
|  | 定义对话框，比如提示框 |
|  | 标签包含 details 元素的标题 |
|  | 规定独立的流内容（图像、图表、照片、代码等等）。 |
|  | 定义 元素的标题 |
|  | 定义 section 或 document 的页脚。 |
|  | 定义了文档的头部区域 |
|  | 定义带有记号的文本。 |
|  | 定义度量衡。仅用于已知最大和最小值的度量。 |
|  | 定义导航链接的部分。 |
|  | 定义任何类型的任务的进度。 |
|  | 定义 ruby 注释（中文注音或字符）。 |
|  | 定义字符（中文注音或字符）的解释或发音。 |
|  | 在 ruby 注释中使用，定义不支持 ruby 元素的浏览器所显示的内容。 |
|  | 定义文档中的节（section、区段）。 |
|  | 定义日期或时间。 |
|  | 规定在文本中的何处适合添加换行符。 |


## HTML5 表单


新表单元素, 新属性，新输入类型，自动验证。


---


## 已移除元素


以下的 HTML 4.01 元素在HTML5中已经被删除:


-
-
- **
-
-
-
-
-
-
-
-


---


## 每一章中的实例


通过我们的 HTML 编辑器，您能够编辑 HTML，然后点击按钮来查看结果。


## 实例


```html
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
  你的浏览器不支持 video 标签。
</video>

</body>
</html>
```


	[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_video_bear)

点击 "尝试一下" 按钮查看在线运行结果。**


---

## HTML5 浏览器支持


最新版本的 Safari、Chrome、Firefox 以及 Opera 支持某些 HTML5 特性。Internet Explorer 9 将支持某些 HTML5 特性。


![](https://www.runoob.com/wp-content/uploads/2013/07/browsers_say.png)


IE9 以下版本浏览器兼容HTML5的方法，使用本站的静态资源的html5shiv包：


```html
<!--[if lt IE 9]>
    <script src="https://lf9-cdn-tos.bytecdntp.com/cdn/expire-1-M/html5shiv/3.7.3/html5shiv.min.js"></script>
<![endif]-->
```


载入后，初始化新标签的CSS：


```html
/*html5*/
article,aside,dialog,footer,header,section,nav,figure,menu{display:block}
```


**

## HTML5 参考手册


在本站中你可以找到关于HTML5 的标签及属性描述，详细请点击 [HTML5参考手册](https://www.runoob.com/tags/html-reference.html)。









	  AI 思考中...





			** [XHTML 简介](https://www.runoob.com/html-xhtml.html)
			[HTML5 新元素](https://www.runoob.com/html5-new-element.html) **













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