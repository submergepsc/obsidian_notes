# jQuery Mobile 导航栏

- Source: https://www.runoob.com/jquerymobile/jquerymobile-navbars.html

导航栏是由一组水平排列的链接组成，通常包含在头部或尾部内。

*

默认情况下，导航栏中的链接将自动变成按钮（不需要 data-role="button"）。


使用 data-role="navbar" 属性来定义导航栏：


## 实例



```javascript
<div data-role="header">
		<div data-role="navbar">    <ul>      <li><a href="#anylink">首页</a></li>      <li><a href="#anylink">页面二</a></li>
		<li><a href="#anylink">搜索</a></li>    </ul>

		</div></div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_navbars)


|  | 默认情况下，按钮的宽度与它的内容一样。使用一个无序列表来平均地划分按钮的宽度：1 个按钮占 100% 宽度，2 个按钮则各占 50% 的宽度，3 个按钮则每个占 33.3% 的宽度，依此类推。然而，如果您在导航栏中指定了超过 5 个按钮，将会拆成多行（查看"更多实例"）。 |
| --- | --- |


---


## 导航按钮图标


我们可以使用 data-icon 属性为导航按钮添加图标:


## 实例



```javascript
<a href="#anylink" data-icon="search">搜索</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_navbars2)


data-icon 属性与在图标章节中的 CSS 类使用相同的值。CSS 类使用方法 class="ui-icon-value*", data-icon 属性使用方法 data-icon="*value*"。


|  |  |  |
| --- | --- | --- |
| 属性值 | 描述 | 图标 |
| data-icon="home" | 首页 |  |
| data-icon="arrow-r" | 右边箭头 |  |
| data-icon="search" | 搜索 |  |


如需查看所有 jQuery Mobile 按钮图标的完整参考手册，请访问我们的 [jQuery Mobile 图标参考手册](https://www.runoob.com/jquerymobile-ref-icons.html)。


---


## 定位图标


就像 "ui-btn-icon-*position*" 类一样 (图标章节有详细说明), 你可以设置图标显示的位置： top（头部）, right（右侧）, bottom（底部） 或 left（左侧）。


图标位置在导航栏容器上设置，使用 data-iconpos** 属性来指定位置：


| 属性值 | 描述 | 实例 |
| --- | --- | --- |
| data-iconpos="top" | 图标顶部对齐 | 尝试一下 |
| data-iconpos="right" | 图标右侧对齐 | 尝试一下 |
| data-iconpos="bottom" | 图标底部对齐 | 尝试一下 |
| data-iconpos="left" | 图标左侧对齐 | 尝试一下 |


|  | 默认情况， 导航按钮的图标位于文本之上 (data-iconpos="top")。 |
| --- | --- |


---


## 激活按钮


当导航栏中的某个链接被点击，它将获得被选中（按下）的外观。


如果想在不点击链接时获得这种外观，请使用 class="ui-btn-active"：


## 实例



```javascript
<li><a href="#anylink" class="ui-btn-active">首页</a></li>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_navbars_class_active)


对于多个页面，您可能想要每个按钮的选中外观代表当前用户所在的页面。要做到这一点，请添加 "ui-state-persist" 和 "ui-btn-active" 到链接的 class：


## 实例



```javascript
<li><a href="#anylink"
		class="ui-btn-active ui-state-persist">首页</a></li>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_navbars_class_persist)


---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[内容中的导航栏](https://www.runoob.com/try/try.php?filename=tryjqmob_navbars_content) 如何在 data-role="content" 内添加导航栏。


[尾部中的导航栏](https://www.runoob.com/try/try.php?filename=tryjqmob_navbars_footer) 如何在尾部内添加导航栏。


[导航栏中的定位图标](https://www.runoob.com/try/try.php?filename=tryjqmob_navbars_footer_icons) 如何在尾部内的导航栏中定位图标。


[超过 5 个按钮](https://www.runoob.com/try/try.php?filename=tryjqmob_navbars_wrap) 导航栏中 10 个按钮的演示。








	  AI 思考中...





			** [jQuery Mobile 工具栏](https://www.runoob.com/jquerymobile-toolbars.html)
			[jQuery Mobile 可折叠块](https://www.runoob.com/jquerymobile-collapsibles.html) **













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