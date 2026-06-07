# jQuery Mobile 表单选择菜单

- Source: https://www.runoob.com/jquerymobile/jquerymobile-form-select.html

---


## jQuery Mobile 选择菜单


Iphone 上的选择菜单：
Android/SGS4 设备上的选择菜单：
**![](https://www.runoob.com/wp-content/uploads/2013/10/selectmenu.jpg)
 元素创建带有若干选项的下拉列表。


 元素内的  元素定义了列表中的可用选项：


## 实例


```javascript
<form method="post" action="demoform.html">  <fieldset
		class="ui-field-contain">    <label
		for="day">Select Day</label>    <select name="day" id="day">
		      <option value="mon">Monday</option>      <option value="tue">Tuesday</option>
		      <option value="wed">Wednesday</option>    </select>

		</fieldset>
		</form>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_select)


提示：**如果您有一个带有相关选项的很长的列表，请在  内使用  元素：


## 实例


```javascript
<select name="day" id="day">   <optgroup
		label="Weekdays">    <option value="mon">Monday</option>
		<option value="tue">Tuesday</option>    <option
		value="wed">Wednesday</option>  </optgroup>  <optgroup
		label="Weekends">    <option
		value="sat">Saturday</option>    <option
		value="sun">Sunday</option>  </optgroup></select>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_select_optgroup)


---


## 自定义选择菜单


本页顶部的图像，演示了移动平台上如何使用它们的方式展示一个选择菜单。


如果您想要让选择菜单在所有的移动设备上都显示相同，请使用 jQuery 自带的自定义选择菜单，data-native-menu="false" 属性：


## 实例


```javascript
<select name="day" id="day" data-native-menu="false">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_select_native)


---


## 多个选择


如需在选择菜单中选择多个选项，请在  元素中使用 multiple 属性：


## 实例


```javascript
<select name="day" id="day"
		multiple data-native-menu="false">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_select_multiple)


---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[使用 data-role="controlgroup"](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_select_group) 如何组合一个或多个选择菜单。


[使用 data-type="horizontal"](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_select_horizontal) 如何水平组合选择菜单。


[预选中选项](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_select_selected) 如何预选中一个选项。


[使用 data-type="mini"](https://www.runoob.com/try/tryit.php?filename=tryjqmob_forms_select_mini) 如何缩小选项菜单


[弹窗选项](https://www.runoob.com/try/tryit.php?filename=tryjqmob_forms_select_popup) 如何创建一个弹窗选项菜单。


[可折叠表单](https://www.runoob.com/try/tryit.php?filename=tryjqmob_forms_collapsible) 如何创建可折叠表单


[修改默认选择项图标](https://www.runoob.com/try/tryit.php?filename=tryjqmob_forms_select_icon) 如何修改选项菜单图标 (默认为 "arrow-d").


[修改图标位置](https://www.runoob.com/try/tryit.php?filename=tryjqmob_forms_select_iconpos) 如何修改图标显示的位置 (默认向右)。








	  AI 思考中...





			** [jQuery Mobile 表单输入](https://www.runoob.com/jquerymobile-form-inputs.html)
			[jQuery Mobile 表单滑动条](https://www.runoob.com/jquerymobile-form-sliders.html) **













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