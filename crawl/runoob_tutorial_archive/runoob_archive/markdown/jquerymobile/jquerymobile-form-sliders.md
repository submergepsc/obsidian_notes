# jQuery Mobile 表单滑动条

- Source: https://www.runoob.com/jquerymobile/jquerymobile-form-sliders.html

---


## jQuery Mobile 滑动条控件


滑动条允许您从一个范围的数字中选择一个值：
**
*

如需创建滑动条，请使用 ：


## 实例


```javascript
<form method="post" action="demoform.php">  <label for="points">进度:</label>
		  <input type="range" name="points" id="points" value="50" min="0"
		max="100"></form>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_slider)


使用以下属性来规定限制：


- max - 规定允许的最大值
- min - 规定允许的最小值
- step - 规定合法的数字间隔
- value - 规定默认值


提示:** 如果你想在按钮中显示进度的值可以添加 data-show-value="true" 属性:


## 实例


```javascript
<input type="range" data-show-value="true">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_slider_showvalue)


提示:** 如果你想在滑动按钮上显示进度（类似一个小弹窗）可以使用 data-popup-enabled="true" 属性:


## 实例


```javascript
<input type="range" data-popup-enabled="true">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_slider_tooltip)


提示：**如果您想要高亮突出显示滑动条的值，请添加 data-highlight="true"：


## 实例


```javascript
<input type="range" data-highlight="true">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_slider_highlight)


---


## 拨动开关


拨动开关通常用于 on/off 或 true/false 按钮：


我们可以使用  元素并指定 data-role 为 "flipswitch" 来创建开关:


## 实例


```javascript
<form method="post" action="demoform.php">
		  <label for="switch">切换开关：</label>
		<input type="checkbox" data-role="flipswitch" name="switch" id="switch"></form>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_select_switch)


默认情况下，开关切换的文本为 "On" 和 "Off"。你可以使用 data-on-text 和 data-off-text 属性来修改它：


### 实例


```javascript
<input type="checkbox" data-role="flipswitch" name="switch" id="switch"
		data-on-text="True" data-off-text="False">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_select_switch_text)


提示:**开关复选框可以使用 "checked" 属性来设置默认的选项：


## 实例


```javascript
<input type="checkbox" data-role="flipswitch" name="switch" id="switch"
		checked>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_select_switch_selected)


---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[区间滑块](https://www.runoob.com/try/tryit.php?filename=tryjqmob_forms_slider_range) 制作一个区间值的滑块。


[滑块样式](https://www.runoob.com/try/tryit.php?filename=tryjqmob_forms_select_switch_css) 为滑块开关设置样式。








	  AI 思考中...





			* [jQuery Mobile 表单选择](https://www.runoob.com/jquerymobile-form-select.html)
			[jQuery Mobile 滚屏事件](https://www.runoob.com/jquerymobile-events-scroll.html) **













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