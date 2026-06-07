# jQuery Mobile 工具栏

- Source: https://www.runoob.com/jquerymobile/jquerymobile-toolbars.html

工具栏元素通常位于头部和尾部内 - 让导航易于访问：

*
**
---


## 头部栏


头部栏一般包含页面标题/logo 或一两个按钮（通常是首页、选项或搜索）。


您可以添加按钮到头部的左侧或右侧。


下面的代码，将添加一个按钮到头部标题文本的左侧，添加一个按钮到头部标题文本的右侧：


## 实例


```javascript
<div data-role="header">  <a href="#"
	class="ui-btn ui-icon-home ui-btn-icon-left">主页</a>  <h1>欢迎访问我的主页</h1>
	<a href="#" class="ui-btn ui-icon-search ui-btn-icon-left">搜索</a></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_header)


下面的代码，将添加一个按钮到头部标题文本的左侧：


## 实例



```javascript
<div data-role="header">  <a href="#"
	class="ui-btn ui-btn-left ui-icon-home ui-btn-icon-left">主页</a>  <h1>欢迎访问我的主页</h1></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_header_left)


但是，如果您把按钮链接放置在  元素之后，将无法显示右侧的文本。要添加一个按钮到头部标题的右侧，请指定 class 为 "ui-btn-right"：


## 实例


```javascript
<div data-role="header">  <h1>欢迎访问我的主页</h1>
	<a href="#"
	class="ui-btn ui-btn-right ui-icon-home ui-btn-icon-left">搜索</a></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_header_class)


|  | 头部可以包含一个或两个按钮，而尾部没有限制。 |
| --- | --- |


---


## 尾部栏


尾部栏比头部栏更灵活 - 在整个页面中它们更具功能性和可变性，因此可以包含尽可能多的按钮：


## 实例


```javascript
<div data-role="footer">  <a href="#"
	class="ui-btn ui-icon-plus ui-btn-icon-left">在Facebook上关注我</a>  <a href="#" class="ui-btn ui-icon-plus ui-btn-icon-left">在Twitter上关注我</a>
	<a href="#" class="ui-btn ui-icon-plus ui-btn-icon-left">在Instagram上关注我</a></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_footer)


注意：**尾部的样式与头部不同（没有内边距和空间，且按钮不居中）。我们可以使用简单的样式来解决这个问题：


## 实例



```javascript
<div data-role="footer" style="text-align:center;">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_footer_class)


您还可以将尾部中的按钮进行水平或垂直组合：


## 实例


```javascript
<div data-role="footer" style="text-align:center;">  <div data-role="controlgroup"
	data-type="horizontal">    <a href="#"
	class="ui-btn ui-icon-plus ui-btn-icon-left">在Facebook上关注我</a>    <a href="#" class="ui-btn ui-icon-plus ui-btn-icon-left">在Twitter上关注我</a>    <a href="#"
	class="ui-btn ui-icon-plus ui-btn-icon-left">在Instagram上关注我</a>
	</div></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_footer_grouped_horizontal)


---


## 定位头部栏和尾部栏


头部和尾部可以通过三种方式进行定位：


- Inline - 默认。头部栏和尾部栏与页面内容内联。
- Fixed - 头部栏和尾部栏固定在页面的顶部和底部。
- Fullscreen - 与 Fixed 定位模式基本相同，头部栏和尾部栏固定在页面的顶部和底部。但是当他工具栏滚动出屏幕之外时，不会自动重新显示，除非点击屏幕，这对于图片或视频类有提升代入感的应用是非常有用的。注意这种模式下工具栏会遮住页面内容，所以最好用在比较特殊的场合下。


使用 data-position 属性来定位头部栏和尾部栏：


## Inline 定位（默认）


```javascript
<div data-role="header" data-position="inline"></div><div data-role="footer"
	data-position="inline"></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_toolbars_inline)


## Fixed 定位


```javascript
<div data-role="header" data-position="fixed"></div><div data-role="footer"
	data-position="fixed"></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_toolbars_fixed)


要启用全屏定位，请使用 data-position="fixed"，并添加 data-fullscreen 属性到元素：


## Fullscreen 定位


```javascript
<div data-role="header"
	data-position="fixed" data-fullscreen="true"></div><div data-role="footer"
	data-position="fixed" data-fullscreen="true"></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_toolbars_fullscreen)


提示：**全屏定位适用于照片、图像和视频。


**提示：**固定定位和全屏定位中，通过点击屏幕将隐藏和显示头部栏和尾部栏。


---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[在工具栏上只显示图标](https://www.runoob.com/try/tryit.php?filename=tryjqmob_header_footer_icons)** 在工具栏上只显示图标可以使用 ui-btn-icon-notext 类。









	  AI 思考中...





			* [jQuery Mobile 按钮图标](https://www.runoob.com/jquerymobile-icons.html)
			[jQuery Mobile 导航栏](https://www.runoob.com/jquerymobile-navbars.html) **













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