# jQuery Mobile 按钮

- Source: https://www.runoob.com/jquerymobile/jquerymobile-buttons.html

---


Mobile 应用程序是建立在您想要显示的简单的点击事物上。


---

**
*


---


## 在 jQuery Mobile 中创建按钮


在 jQuery Mobile 中，按钮可通过三种方式创建：


- 使用  元素
- 使用  元素
- 使用带有 data-role="button" 的  元素


##


```javascript
<button>按钮</button>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_button_button)


##


```javascript
<input type="button" value="按钮">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_button_input)


##


```javascript
<a href="#" data-role="button">按钮</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_button_a)


|  | 在 jQuery Mobile 中，按钮会自动样式化，让它们在移动设备上更具吸引力和可用性。我们推荐您使用带有 data-role="button" 的 元素在页面间进行链接，使用 或 元素进行表单提交。 |
| --- | --- |


---


## 导航按钮


如需通过按钮在页面间进行链接，请使用带有 data-role="button" 属性的  元素：


## 实例


```javascript
<a href="#pagetwo" data-role="button">访问第二个页面</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_button)


---


## 内联按钮


默认情况下，按钮占满整个屏幕宽度。如果你想要一个仅是与内容一样宽的按钮，或者如果您想要并排显示两个或多个按钮，请添加 data-inline="true"：


## 实例


```javascript
<a href="#pagetwo" data-role="button" data-inline="true">访问第二个页面</a>
```



[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_button_inline)


---


## 组合按钮


jQuery Mobile 提供了一个简单的方法来将按钮组合在一起。


请把 data-role="controlgroup" 属性和 data-type="horizontal|vertical" 一起使用来规定是否水平或垂直组合按钮：


## 实例


```javascript
<div data-role="controlgroup" data-type="horizontal">
	<a href="#anylink" data-role="button">按钮 1</a>  <a href="#anylink"
	data-role="button">按钮 2</a>  <a href="#anylink"
	data-role="button">按钮 3</a></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_button_group)


|  | 默认情况下，组合按钮是垂直组合，它们之间没有外边距和空间。并且只有第一个和最后一个按钮是圆角，以便它们组合在一起的时候创建一个漂亮的外观。 |
| --- | --- |


---


## 后退按钮


如需创建后退按钮，请使用 data-rel="back" 属性（这会忽略锚的 href 值）：


## 实例


```javascript
<a href="#" data-role="button" data-rel="back">返回</a>
```



[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_button_back)


---


## 更多链接按钮实例


| 类 | 描述 | 实例 |
| --- | --- | --- |
| ui-btn-b | 修改按钮颜色为黑色，字体为白色(默认为灰色背景，黑色字体)。 | 尝试一下 |
| ui-corner-all | 为按钮添加圆角 | 尝试一下 |
| ui-mini | 制作小按钮 | 尝试一下 |
| ui-shadow | 为按钮添加阴影 | 尝试一下 |


|  | 如果你需要使用更多的样式，每个样式类使用空格隔开，如： class="ui-btn ui-btn-inline ui-btn-corner-all ui-shadow" 默认情况下 按钮有圆角及阴影效果。 和 元素没有。 |
| --- | --- |


更完整的CSS类，请查看我们的 [jQuery Mobile CSS 类参考手册](https://www.runoob.com/jquerymobile-ref-css.html)。


下一章演示如何在按钮上加上图标。








	  AI 思考中...





			* [jQuery Mobile 过渡](https://www.runoob.com/jquerymobile-transitions.html)
			[jQuery Mobile 按钮图标](https://www.runoob.com/jquerymobile-icons.html) **













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