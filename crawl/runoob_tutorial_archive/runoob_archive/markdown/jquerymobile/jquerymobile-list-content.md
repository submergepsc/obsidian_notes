# jQuery Mobile 列表内容

- Source: https://www.runoob.com/jquerymobile/jquerymobile-list-content.html

---

*

---


## jQuery Mobile 列表图标


默认情况下每个列表项都会包含一个箭头图标 "carat-r" (右箭头)。如果要修改这个图标可以使用 data-icon 属性:


## 实例


```javascript
<ul data-role="listview">   <li><a href="#">Default is right
	arrow</a></li>  <li data-icon="plus"><a href="#">data-icon="plus"</a></li>
	<li data-icon="minus"><a href="#">data-icon="minus"</a></li>  <li
	data-icon="delete"><a href="#">data-icon="delete"</a></li>  <li
	data-icon="location"><a href="#">data-icon="location"</a></li>
	<li data-icon="false"><a href="#">data-icon="false"</a></li></ul>
```

 **[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_change_icons)


|  | data-icon="false" 将会移除图标。 |
| --- | --- |


更完整的 jQuery Mobile 按钮图标，请访问我们的 [jQuery Mobile 图标参考手册](https://www.runoob.com/jquerymobile-ref-icons.html)。


---


## 16x16 图标


如果你想在你的列表添加标准的 16x16px 的图标, 可以在列表项中添加  元素，并使用 "ui-li-icon" 类:


## 实例


```javascript
<ul data-role="listview">
	<li><a href="#"><img src="us.png" alt="USA" class="ui-li-icon">USA</a></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_icons)

---


## jQuery Mobile 列表缩略图


大于 16x16px 的图像，请在链接中添加  元素。


jQuery Mobile 将自动缩放图像到 80x80px:


## 实例


```javascript
<ul data-role="listview">  <li><a href="#"><img src="chrome.png"></a></li>
	</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_thumbs)


使用标准的HTML添加列表信息：


## 实例


```javascript
<ul data-role="listview">  <li>
	<a href="#">    <img src="chrome.png">
	<h2>Google Chrome</h2>    <p>Google Chrome 免费的开源 web 浏览器。发布于 2008 年。</p>    </a>
	</li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_thumbs2)


---


## jQuery Mobile 列表图标


在列表  元素使用 class="ui-li-icon" 添加 16x16px 图标：


## 实例


```javascript
<li><a href="#"><img src="us.png" alt="USA" class="ui-li-icon">USA</a></li>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_icons)


---


## 分割按钮


在JQuery Mobile的列表中，有时需要对选项内容做两个不同的操作，这时，需要对选项中的链接按钮进行分割。实现分割的方法是在元素中再增加一个元素，便可以在页面实现分割效果。


jQuery Mobile 会自动设置第二个链接为蓝色箭头的图标，图标的链接文字（如果有的话）将在用户将鼠标悬停在 图标时显示:


## 实例


```javascript
<ul data-role="listview">  <li>
	<a href="#"><img src="chrome.png"></a>    <a href="#">Some
	Text</a>  </li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_split)


添加一些页面和对话框使链接功能更加丰富：


## 实例


```javascript
<ul data-role="listview">  <li>
	<a href="#"><img src="chrome.png"></a>    <a href="#download"
	data-rel="dialog">下载浏览器</a>  </li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_split2)


---


## 气泡数字


气泡数字是用来显示列表项相关的数字，如在一个邮箱的邮件：


如需添加气泡数字，请使用行内元素，比如 ，设置 class "ui-li-count" 属性并添加数字：


## 实例


```javascript
<ul data-role="listview">  <li><a href="#">收件箱<span class="ui-li-count">25</span></a></li>
	<li><a href="#">发件箱<span class="ui-li-count">432</span></a></li>
	<li><a href="#">垃圾箱<span class="ui-li-count">7</span></a></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_count)


注意：**显示一个正确的气泡数字，必须修改编程方式。 这将在以后的章节解释。


---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[弹窗列表](https://www.runoob.com/try/tryit.php?filename=tryjqmob_lists_popup)** 如何创建弹窗列表


[改变列表项的默认链接图标](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_change_icons) 如何设置列表项的默认链接图标(默认是右箭头).


[可折叠弹窗列表](https://www.runoob.com/try/tryit.php?filename=tryjqmob_lists_collapsible_popup) 如何创建可折叠弹窗列表。


[可折叠的列表](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_collapsible) 如何创建显示/隐藏的列表。


[更多内容格式](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_formatting) 如何制作一个日历。








	  AI 思考中...





			* [jQuery Mobile 列表视图](https://www.runoob.com/jquerymobile-list-views.html)
			[jQuery Mobile 过渡](https://www.runoob.com/jquerymobile-transitions.html) **













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