# jQuery Mobile 可折叠块

- Source: https://www.runoob.com/jquerymobile/jquerymobile-collapsibles.html

---


## 可折叠内容块


可折叠块允许您隐藏或显示内容 - 对于存储部分信息很有用。

*

如需创建一个可折叠的内容块，需要为容器添加 data-role="collapsible" 属性。在容器（div）内，添加一个标题元素（H1-H6），后跟您想要进行扩展的 HTML 标记：


## 实例



```javascript
<div data-role="collapsible">
		<h1>点击我 - 我可以折叠!</h1>  <p>我是可折叠的内容。</p>
		</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_collapsible)


默认情况下，内容是被折叠起来的。如需在页面加载时展开内容，请使用 data-collapsed="false"：


## 实例



```javascript
<div data-role="collapsible" data-collapsed="false">
		<h1>点击我 - 我可以折叠!</h1>  <p>I'm
		现在我默认是展开的。</p>
		</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_collapsible_false)


---


## 嵌套可折叠块


可折叠的内容块是可以彼此嵌套的：


## 实例



```javascript
<div data-role="collapsible">  <h1>点击我 - 我可以折叠!</h1>
		  <p>我是被展开的内容。</p>  <div
		data-role="collapsible">    <h1>点击我 - 我是嵌套的可折叠块！</h1>    <p>我是嵌套的可折叠块中被展开的内容。</p>  </div></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_collapsible_nested)


|  | 可折叠的内容块可以根据您的需要进行多次嵌套。 |
| --- | --- |


---


## 可折叠集合


可折叠集合是将可折叠块组合在一起（就像手风琴一样）。当一个新的块被展开时，所有其他的块都会被折叠起来。


创建若干个可折叠的内容块，然后把可折叠内容块用带有 data-role="collapsible-set" 的新容器包围起来：


## 实例



```javascript
<div data-role="collapsible-set">  <div
		data-role="collapsible">    <h1>点击我 - 我可以折叠！</h1>    <p>我是被展开的内容。</p>
		</div>  <div data-role="collapsible">
		<h1>点击我 - 我可以折叠!</h1>    <p>我是被展开的内容。</p>  </div></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_collapsible_sets)


---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[通过 data-inset 属性取消圆角与外边距](https://www.runoob.com/try/try.php?filename=tryjqmob_collapsible_inset) 如何取消可折叠块上的圆角与外边距。


[通过 data-mini 属性迷你化可折叠块](https://www.runoob.com/try/try.php?filename=tryjqmob_collapsible_mini) 如何让可折叠块更小。


[通过 data-collapsed-icon 和 data-expanded-icon 改变图标](https://www.runoob.com/try/try.php?filename=tryjqmob_collapsible_icons) 如何改变可折叠块的图标（默认是 + 和 -）。


[弹窗中使用折叠](https://www.runoob.com/try/tryit.php?filename=tryjqmob_collapsible_popup) 在弹窗中创建折叠项。


[修改图标位置](https://www.runoob.com/try/tryit.php?filename=tryjqmob_collapsible_iconpos) 在折叠项中如何修改图标的位置 (默认为在左边)。








	  AI 思考中...





			* [jQuery Mobile 导航栏](https://www.runoob.com/jquerymobile-navbars.html)
			[jQuery Mobile 网格](https://www.runoob.com/jquerymobile-grids.html) **













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