# jQuery Mobile 面板

- Source: https://www.runoob.com/jquerymobile/jquerymobile-panels.html

jQuery Mobile 中的面板会在屏幕的左侧向右侧划出。

*

通过向指定 id 的  元素添加 data-role="panel" 属性来创建面板。


在  中添加 HTML 标记来显示你的面板内容：


```
<div data-role="panel" id="myPanel">
  <h2>面板标题..</h2>
  <p>文本内容..</p>
</div>
```


**注意：** panel 标记必须置于头部、内容、底部组成的页面之前或之后。


要访问面板，需要创建一个指向面板  id 的链接，点击该链接即可打开面板:


```
<a href="#myPanel" class="ui-btn ui-btn-inline">打开面板</a>
```


简单的面板实例


## 实例



```javascript
<div data-role="page" id="pageone">  <div
	data-role="panel" id="myPanel">
	    <h2>面板头部..</h2>    <p>面板内容..</p>  </div>   <div
	data-role="header">    <h1>标准页面头部</h1>
	</div>  <div data-role="main" class="ui-content">
	<p>点击下面按钮打开面板。</p>    <a
	href="#myPanel" class="ui-btn ui-btn-inline">打开面板</a>  </div>  <div data-role="footer">
	<h1>底部文本</h1>  </div> </div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_panels_basic)


---


## 关闭面板


你可以通过点击面板外部区域或按下 Esc 键或滑动来关闭面板。你可以通过使用 data-* 属性来禁用滑动和点击来关闭面板：


| 属性 | 值 | 描述 | 实例 |
| --- | --- | --- | --- |
| data-dismissible | true \| false | 指定面板是否可以通过点击面板外部区域来关闭。 | 尝试一下 |
| data-swipe-close | true \| false | 指定是否可以通过滑动来关闭。 | 尝试一下 |


你可以使用按钮来关闭面板：仅需要在面板的  中添加 data-rel="close" 属性。 从性能上考虑，我们需要键关闭链接的 href 属性指向页面的 ID 。


## 实例



```javascript
<div
	data-role="panel" id="myPanel">
	  <h2>面板头部..</h2>  <p>面板中的一些文本内容..</p>  <a
	href="#pageone" data-rel="close" class="ui-btn ui-btn-inline">关闭面板</a></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_panels_closebtn)


---


## 面板展示


你可以通过使用 data-display 属性来控制面板的展示方式:


| 属性值 | 描述 |
| --- | --- |
| data-display="overlay" | 在内容上显示面板 |
| data-display="push" | 是同时"推动"面板和页面。 |
| data-display="reveal" | 默认值，将页面像幻灯片一样从屏幕划出，将面板显示出来 |


## 实例



```javascript
<div data-role="panel" id="overlayPanel" data-display="overlay"><div
	data-role="panel" id="revealPanel" data-display="reveal"><div
	data-role="panel" id="pushPanel" data-display="push">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_panels_display)


---


## 面板定位


默认情况下，面板会显示在屏幕的左侧。如果想让面板出现在屏幕的右侧，可以指定 data-position="right" 属性。


## 实例



```javascript
<div
	data-role="panel" id="myPanel"
	data-position="right">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_panels_rightpos)


你可以指定面板的内容根据页面滚动而滚动。默认情况下面板是随着页面一起滚动的（但是面板的内容仍然位于页面顶部）。如果你需要实现面板内容固定不随页面滚动而滚动，可以在面板添加 the data-position-fixed="true" 属性:


## 实例



```javascript
<div
	data-role="panel" id="myPanel"
	data-position-fixed="true">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_panels_fixed)









	  AI 思考中...





			* [jQuery Mobile 弹窗](https://www.runoob.com/jquerymobile-popups.html)
			[jQuery Mobile 表格](https://www.runoob.com/jquerymobile-tables.html) **













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