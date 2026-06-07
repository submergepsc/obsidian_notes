# jQuery Mobile 主题

- Source: https://www.runoob.com/jquerymobile/jquerymobile-themes.html

jQuery Mobile 提供了 2 种不同的主题样式, 从 "a" 到 "b" - 每一种主题的按钮，工具条，内容块等等颜色都不一致，每个主题的视觉效果也不一样。


通过设置元素的data-theme属性可以自定义应用的外观:


```
<a href="#" class="ui-btn ui-btn-a|b">按钮</a>
```


**

| 值 | 描述 | 实例 |
| --- | --- | --- |
| a | 页面为灰色背景黑色文字 头部与底部均为灰色背景黑色文字 按钮为灰色背景黑色文字 激活的按钮和链接为白色文本蓝色背景 input 输入框中 placeholder 属性值为浅灰色，value 值为黑色 | 尝试一下 |
| b | 页面为黑色背景白色文字 头部与底部均为黑色背景白色文字 按钮为白色文字木炭背景 激活的按钮和链接为白色文本蓝色背景 input 输入框中 placeholder 属性值为浅灰色，value 值为白色 | 尝试一下 |


按钮样式使用 class="ui-btn",使用 "ui-btn-a|b" 类设置按钮为灰色（默认）或黑色：


```
<a href="#" class="ui-btn ui-btn-a|b">按钮</a>
```


|  | "a" 主题的样式用于大多数元素，子元素通常继承父元素的样式。 |
| --- | --- |


---


## 主题头部和底部


## 实例


```javascript
<div data-role="header" data-theme="b"></div><div data-role="footer"
		data-theme="b"></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_bars)


---


## 主题对话框的头部底部


## 实例


```javascript
<div data-role="page" data-dialog="true" id="pagetwo">  <div
		data-role="header" data-theme="b"></div>  <div
		data-role="footer" data-theme="b"></div></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_dialog)


---


## 主题按钮


## 实例


```javascript
<a href="#" class="ui-btn ui-btn-b">黑色按钮</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_buttons)


---


## 主题图标


## 实例


```javascript
<a href="#" class="ui-btn ui-btn-b ui-icon-search
		ui-btn-icon-notext">Search</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_icons)


---


## 主题弹窗


## 实例


```javascript
<div data-role="popup" id="myPopup" data-theme="b">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_popups)


---


## 头部和底部的主题按钮


## 实例


```javascript
<div data-role="header">  <a href="#" class="ui-btn
		ui-btn-b">主页</a>  <h1>欢迎访问我的主页</h1>
		<a href="#" class="ui-btn">搜索</a></div><div data-role="footer">
		  <a href="#" class="ui-btn ui-btn-b">在Facebook上关注我</a>
		<a href="#" class="ui-btn">在Twitter上关注我</a>  <a href="#"
		class="ui-btn ui-btn-b">在Instagram上关注我</a></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_toolbars_buttons)


---


## 主题导航栏


## 实例


```javascript
<div data-role="footer" data-theme="b">  <h1>文本头部</h1>  <div data-role="navbar">    <ul>
		<li><a href="#" data-icon="home" data-theme="a">Button 1</a></li>
		<li><a href="#" data-icon="arrow-r">Button 2</a></li>
		<li><a href="#" data-icon="arrow-r">Button 3</a></li>
		<li><a href="#" data-icon="search" data-theme="a">Button 4</a></li>
		</ul>  </div> </div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_navbars)


---


## 主题面板


## 实例


```javascript
<div data-role="panel" id="myPanel" data-theme="b">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_panels)


---


## 主题可折叠按钮和内容


## 实例


```javascript
<div data-role="collapsible" data-theme="b" data-content-theme="b">
		<h1>Click me - I'm collapsible!</h1>  <p>I'm the expanded
		content.</p></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_collapsibles)


---


## 主题列表


## 实例


```javascript
<ul data-role="listview" data-theme="b">  <li><a href="#">List
		Item</a></li>  <li><a href="#">List
		Item</a></li>  <li data-theme="a"><a href="#">List
		Item</a></li>  <li><a href="#">List Item</a></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_lists)


---


## 主题分割按钮


## 实例


```javascript
<ul data-role="listview" data-split-theme="b">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_split)


---


## 主题可折叠列表


## 实例


```javascript
<div data-role="collapsible" data-theme="b"
		data-content-theme="b">  <ul data-role="listview">
		<li><a href="#">Agnes</a></li>  </ul></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_collapsible_lists)


---


## 主题表单


## 实例


```javascript
<label for="name">Full Name:</label><input type="text" name="text"
		id="name" data-theme="b"><label for="colors">Choose Favorite
		Color:</label><select id="colors"
		name="colors" data-theme="b">  <option value="red">Red</option>
		<option value="green">Green</option>  <option
		value="blue">Blue</option></select>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_forms)


---


## 主题可折叠表单


## 实例


```javascript
<fieldset data-role="collapsible" data-theme="b" data-content-theme="b">
		<legend>Click me - I'm collapsible!</legend>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_collapsible_forms)


---


## 添加新主题


jQuery Mobile 可以在移动页面添加新主题。


通过修改 CSS 文件来添加或编辑新主题(如果你已经下载了 jQuery Mobile)。你只需要拷贝样式模块，然后重命令字母类名（c-z）,并在样式中添加你喜欢的颜色和字体。


你也可以在 HTML 文档中添加主题的新样式， 工具条添加类： ui-bar-(a-z) ，文本内容添加类: ui-body-(a-z) ,页面添加类：ui-page-theme-(a-z) 。


## 实例


```javascript
<style>.ui-bar-f {    color: red;    background-color: yellow;}
		.ui-body-f {    font-weight: bold;    color: white;

		background-color: purple;}.ui-page-theme-f {

		font-weight: bold;    background-color: green;}</style>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_themes_custom)


|  | 在之前的 jQuery Mobile 版本中, 使用 JavaScript 来为元素继承父主题样式。到了 1.4 版本后，框架更注重性能上的提升，已不再使用 JavaScript 来继承，而是使用纯 CSS。 jQuery Mobile 团队为此已经创建了一个工具，地址为 ThemeRoller。你可以使用该工具来升级旧的主题，使其兼容新的版本。 |
| --- | --- |








	  AI 思考中...





			** [jQuery Mobile 网格](https://www.runoob.com/jquerymobile-grids.html)
			[jQuery Mobile 事件](https://www.runoob.com/jquerymobile-events.html) **













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