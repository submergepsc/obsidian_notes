# Foundation 表单

- Source: https://www.runoob.com/foundation/foundation-forms.html

Foundation 表单控制会自动设置为全局样式:


所有 ``, ` ` 及 `` 元素宽度都为 100%，且带有外边距、内边距、阴影和鼠标移动效果。


### 实例


```
<form>
	Input:  <input type="text" placeholder="Name">  Textarea:  <textarea
	rows="4" placeholder="Address"></textarea>  Select:  <select>
	<option>1</option>    <option>2</option>    <option>3</option>    <option>4</option>  </select>
	</form>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_forms)


---


## 标签

在表单中使用 `` 元素来设置标签，标签可以添加 for 属性和 id 属性。用户在点击标签或输入域时获取输入框焦点：


### 实例


```
<form>
	<label for="name">Input    <input type="text" placeholder="Name"
	id="name">  </label>  <label
	for="adr">Label    <textarea
	rows="4" placeholder="Address" id="adr"></textarea>  </label>  <label
	for="num">Select    <select id="num">      <option>1</option>      <option>2</option>      <option>3</option>      <option>4</option>    </select>  </label>
	</form>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_forms_label)


如果需要设置标签右对齐，可以使用 `.right` 类:


### 实例


```
<label class="right">
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_forms_label_right)


---


## Fieldset


Foundation 渲染 `` 元素的样式如下：


### 实例


```
<form>
	<fieldset>    <legend>Fieldset Legend</legend>    <label>Name
	<input type="text" placeholder="First Name..">    </label>
	<label>Email      <input type="text" placeholder="Enter
	email..">    </label>  </fieldset>
	</form>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_forms_fieldset)


---


## 错误状态


使用 `.error` 类来设置错误的标签、输入框、文本框样式:


### 实例


```
<form>
	<label class="error">Error    <input type="text"
	placeholder="Name..">  </label>  <small class="error">Wrong
	input</small>  <textarea rows="4" placeholder="Address"></textarea>

	<small class="error">Wrong input</small></form>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_forms_error)


|  | 你需要使用 JavaScript 来更新用户输入的错误状态。 |
| --- | --- |








	  AI 思考中...





			** [Foundation 麦哲伦（Magellan）导航](https://www.runoob.com/foundation-magellan.html)
			[Foundation 输入框尺寸](https://www.runoob.com/foundation-input-sizing.html) **













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