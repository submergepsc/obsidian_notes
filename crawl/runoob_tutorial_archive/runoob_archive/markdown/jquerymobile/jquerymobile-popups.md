# jQuery Mobile 弹窗

- Source: https://www.runoob.com/jquerymobile/jquerymobile-popups.html

弹窗是一个非常流行的对话框，弹窗可以覆盖在页面上展示。


弹窗可用于显示一段文本，图片，地图或其他内容。

*


创建一个弹窗，需要使用  和  元素。在  元素上添加 data-rel="popup" 属性，  元素添加 data-role="popup" 属性。 接着我们为  指定 id， 然后设置  的 href 值为  指定的 id。  中的内容为弹窗显示的内容。


**注意:**  弹窗与点击的  链接必须在同一个页面上。


## 实例



```javascript
<a href="#myPopup" data-rel="popup" class="ui-btn ui-btn-inline
	ui-corner-all">显示弹窗</a><div data-role="popup" id="myPopup">  <p>这是一个简单的弹窗</p></div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_popup_basic)


如果你需要为弹窗添加内边距与外边距可以在  中添加 "ui-content" 类:


## 实例



```javascript
<div
	data-role="popup" id="myPopup"
	class="ui-content">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_popup_content)


---


## 关闭弹窗


默认情况下，点击弹窗之外的区域或按下 "Esc" 键即可关闭弹窗。 如果你不想点击弹窗之外的区域关闭弹窗可以在添加上添加 data-dismissible="false" 属性（不推荐）。 你也可以在弹窗上添加关闭按钮，按钮上使用 data-rel="back" 属性，并通过样式来控制按钮的位置。


| 描述 | 实例 |
| --- | --- |
| 右侧关闭按钮 | 尝试一下 |
| 左侧关闭按钮 | 尝试一下 |
| 使用 data-dismissible 属性 | 尝试一下 |


---


## 定位弹窗

默认情况下，弹窗会直接显示在点击元素的上方，如果需要控制弹窗的位置，可以在用于打开弹窗的点击链接上使用 data-position-to 属性。

控制弹窗位置的三种方式：


| 属性值 | 描述 |
| --- | --- |
| data-position-to="window" | 弹窗在窗口居中显示 |
| data-position-to="#myId" | 弹窗显示在知道的 #id 元素上 |
| data-position-to="origin" | 默认。弹窗显示在点击的元素上。 |


## 实例



```javascript
<a href="#myPopup1" data-rel="popup" class="ui-btn" data-position-to="window">Window</a><a href="#myPopup2" data-rel="popup"
	class="ui-btn" data-position-to="#demo">id="demo"</a><a href="#myPopup3"
	data-rel="popup" class="ui-btn" data-position-to="origin">Origin</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_popup_position)


---


## 过渡


默认情况下，弹窗是没有过渡效果的。如果你需要你可以通过 data-transition="value" 属性来添加过渡效果（[jQuery Mobile 过渡](https://www.runoob.com/jquerymobile-transitions.html)）：


## 所有过渡效果实例



```javascript
<a href="#myPopup" data-rel="popup" class="ui-btn" data-transition="fade">Fade</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_popup_transitions)


---


## 弹窗方向小边框


如果需要添加弹窗方向小边框，可以使用 data-arrow 属性，并指定值 "l" (左边), "t" (顶部), "r" (右边) or "b" (底部):


## 实例



```javascript
<a href="#myPopup" data-rel="popup" class="ui-btn">打开弹窗</a><div data-role="popup" id="myPopup" class="ui-content"
	data-arrow="l">  <p>左边框的方向。</p></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_popup_arrow)


---


## 弹窗对话框

你可以将弹窗制作为一个标准的对话框 (头部, 内容和底部标记):


## 实例



```javascript
<a href="#myPopupDialog" data-rel="popup" class="ui-btn">打开对话框弹窗</a><div data-role="popup" id="myPopupDialog">  <div
	data-role="header"><h1>头部文本..</h1></div>  <div
	data-role="main" class="ui-content"><p>一些文本..</p><a href="#">一些链接..</a>  <div data-role="footer"><h1>底部文本..</h1></div>
	</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_popup_dialog)


---


## 图片弹窗

你可以在弹窗中显示图片:


## 实例



```javascript
<a href="#myPopup" data-rel="popup" data-position-to="window"><img src="/wp-content/uploads/2015/10/runoob.jpeg"
	alt="Runoob" style="width:200px;"></a><div data-role="popup"
	id="myPopup">  <img src="/wp-content/uploads/2015/10/runoob.jpeg"
	style="width:800px;height:400px;" alt="Runoob"></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_popup_image)


---


## 弹窗背景覆盖


你可以使用 data-overlay-theme 属性在弹窗后添加背景颜色。


默认情况下覆盖的背景色的透明的。使用 data-overlay-theme="a" 添加浅色背景，使用 data-overlay-theme="b" 添加深色的覆盖背景：


## 实例



```javascript
<a href="#myPopup" data-rel="popup">Show Popup</a><div data-role="popup" id="myPopup"
	data-overlay-theme="b">  <p>在我身后有个深色背景。</p></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_popup_overlay)


一般图片弹窗经常使用背景覆盖：


## 实例



```javascript
<a href="#myPopup" data-rel="popup" data-position-to="window"><img src="/wp-content/uploads/2015/10/runoob.jpeg"
	alt="Runoob" style="width:200px;"></a><div data-role="popup"
	id="myPopup"
	data-overlay-theme="b">  <img src="/wp-content/uploads/2015/10/runoob.jpeg"
	style="width:800px;height:400px;" alt="Runoob"></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_popup_image_b)


注意：** 在接下来的章节中，你将了解到如何在弹窗中使用表单。








	  AI 思考中...





			* [jQuery Mobile CSS 类](https://www.runoob.com/jquerymobile-ref-css.html)
			[jQuery Mobile 面板](https://www.runoob.com/jquerymobile-panels.html) **













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