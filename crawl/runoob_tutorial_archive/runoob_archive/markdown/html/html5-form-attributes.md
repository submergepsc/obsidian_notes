# HTML5 表单属性

- Source: https://www.runoob.com/html/html5-form-attributes.html

---


## HTML5 新的表单属性


HTML5 的  和 标签添加了几个新属性.


新属性：


- autocomplete
- novalidate


新属性：


- autocomplete
- autofocus
- form
- formaction
- formenctype
- formmethod
- formnovalidate
- formtarget
- height 与 width
- list
- min 与 max
- multiple
- pattern (regexp)
- placeholder
- required
- step


---


## / autocomplete 属性


autocomplete 属性规定 form 或 input 域应该拥有自动完成功能。


当用户在自动完成域中开始输入时，浏览器应该在该域中显示填写的选项。


**提示:** autocomplete 属性有可能在 form元素中是开启的，而在input元素中是关闭的。


**注意:** autocomplete 适用于  标签，以及以下类型的  标签：text, search, url, telephone, email, password, datepickers, range 以及 color。

![Opera](https://www.runoob.com/images/incompatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


HTML form 中开启 autocomplete (一个 input 字段关闭 autocomplete ):


```html
<form action="demo-form.php" autocomplete="on">
  First name:<input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  E-mail: <input type="email" name="email" autocomplete="off"><br>
  <input type="submit">
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_autocomplete)


提示:**某些浏览器中，您可能需要启用自动完成功能，以使该属性生效。


---


## novalidate 属性


novalidate 是一个布尔（true 或 false）属性。


novalidate 属性是 HTML 表单元素的一个布尔属性，用于设置浏览器不对表单进行验证。

当该属性被添加到  元素上时，浏览器将不会执行默认的表单验证，不会检查输入字段是否符合指定的验证规则。


使用 novalidate 属性可以让开发者完全控制表单验证的逻辑，可以通过 JavaScript 或其他方式来自定义表单验证的行为。


![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/incompatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


无需验证提交的表单数据


```html
<form action="demo-form.php" novalidate>
  E-mail: <input type="email" name="user_email">
  <input type="submit">
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_form_novalidate)


---


## autofocus 属性


autofocus 属性是一个布尔属性。


autofocus 属性规定在页面加载时，域自动地获得焦点。

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


让 "First name" input 输入域在页面载入时自动聚焦：


```html
First name:<input type="text" name="fname" autofocus>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_autofocus)


---


## form 属性


form 属性规定输入域所属的一个或多个表单。


提示:**如需引用一个以上的表单，请使用空格分隔的列表。

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/incompatible_ie2020.gif)
## 实例


位于form表单外的 input 字段引用了 HTML form (该 input 表单仍然属于form表单的一部分):


```html
<form action="demo-form.php" id="form1">
  First name: <input type="text" name="fname"><br>
  <input type="submit" value="提交">
</form>

Last name: <input type="text" name="lname" form="form1">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_form)


---


## formaction 属性


The formaction 属性用于描述表单提交的URL地址.


The formaction 属性会覆盖 元素中的action属性.


注意: **The formaction 属性用于 type="submit" 和 type="image".

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


以下HTMLform表单包含了两个不同地址的提交按钮：


```html
<form action="demo-form.php">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit" value="提交"><br>
  <input type="submit" formaction="demo-admin.php"
  value="提交">
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_formaction)


---


## formenctype 属性


formenctype 属性描述了表单提交到服务器的数据编码 (只对form表单中 method="post" 表单)


formenctype 属性覆盖 form 元素的 enctype 属性。


主要: **该属性与 type="submit" 和 type="image" 配合使用。

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


第一个提交按钮以默认编码发送表单数据，第二个提交按钮以 "multipart/form-data" 编码格式发送表单数据:


```html
<form action="demo-post_enctype.php" method="post">
  First name: <input type="text" name="fname"><br>
  <input type="submit" value="提交">
  <input type="submit" formenctype="multipart/form-data"
  value="以 Multipart/form-data 提交">
</form>
```




**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_formenctype)


---


## formmethod 属性


formmethod 属性定义了表单提交的方式。


formmethod 属性覆盖了  元素的 method 属性。


注意:** 该属性可以与 type="submit" 和 type="image" 配合使用。

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


重新定义表单提交方式实例:


```html
<form action="demo-form.php" method="get">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit" value="提交">
  <input type="submit" formmethod="post" formaction="demo-post.php"
  value="使用 POST 提交">
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_formmethod)


---


## formnovalidate 属性


novalidate 属性是一个 boolean 属性.


novalidate属性描述了  元素在表单提交时无需被验证。


formnovalidate 属性会覆盖  元素的novalidate属性.


注意:** formnovalidate 属性与 **type="submit"** 一起使用 ![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/incompatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif) ## 实例 两个提交按钮的表单(使用与不适用验证 ):


```html
<form action="demo-form.php">
  E-mail: <input type="email" name="userid"><br>
  <input type="submit" value="提交"><br>
  <input type="submit" formnovalidate value="不验证提交">
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_formnovalidate)


---


## formtarget 属性


formtarget 属性指定一个名称或一个关键字来指明表单提交数据接收后的展示。


formtarget 属性覆盖 元素的target属性.


注意:** formtarget 属性与 **type="submit"** 和 **type="image"** 配合使用。

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


两个提交按钮的表单, 在不同窗口中显示:


```html
<form action="demo-form.php">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit" value="正常提交">
  <input type="submit" formtarget="_blank"
  value="提交到一个新的页面上">
</form>
```


**[尝试一下 »](https://www.runoob.com/try/demo_source/tryhtml5_input_formtarget.htm)


---


## height 和 width 属性


height 和 width 属性规定用于 image 类型的  标签的图像高度和宽度。


注意:** height 和 width 属性只适用于 image 类型的 标签。


**提示:**图像通常会同时指定高度和宽度属性。如果图像设置高度和宽度，图像所需的空间 在加载页时会被保留。如果没有这些属性， 浏览器不知道图像的大小，并不能预留 适当的空间。图片在加载过程中会使页面布局效果改变 （尽管图片已加载）。

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


定义了一个图像提交按钮, 使用了 height 和 width 属性:


```html
<input type="image" src="img_submit.gif" alt="Submit" width="48"
	height="48">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_height_width)


---


## list 属性


list 属性规定输入域的 datalist。datalist 是输入域的选项列表。

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/incompatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


在 中预定义  值:


```html
<input list="browsers">
	<datalist id="browsers">
	  <option value="Internet Explorer">
  <option value="Firefox">
  <option value="Chrome">
  <option value="Opera">
  <option value="Safari">
	</datalist>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_datalist)


---


## min 和 max 属性


min、max 和 step 属性用于为包含数字或日期的 input 类型规定限定（约束）。


注意:** min、max 和 step 属性适用于以下类型的  标签：date pickers、number 以及 range。

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/incompatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


 元素最小值与最大值设置:


```html
Enter a date before 1980-01-01:
<input type="date" name="bday" max="1979-12-31">
Enter a date after 2000-01-01:
<input type="date" name="bday" min="2000-01-02">
Quantity (between 1 and 5):
<input type="number" name="quantity" min="1" max="5">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_max_min)


---


## multiple 属性


multiple 属性是一个 boolean 属性.


multiple 属性规定 元素中可选择多个值。


注意:** multiple 属性适用于以下类型的  标签：email 和 file:

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


上传多个文件:


```html
Select images: <input type="file" name="img" multiple>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_multiple)


---


## pattern 属性


pattern 属性描述了一个正则表达式用于验证  元素的值。


注意:**pattern 属性适用于以下类型的  标签: text, search, url, tel, email, 和 password。


**提示：** 是用来全局 [title](https://www.runoob.com/../tags/tag-title.html) 属性来描述模式。


**提示：** 您可以在我们的 [JavaScript 教程](https://www.runoob.com/../js/js-tutorial.html)中学习到有关正则表达式的内容。

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/incompatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


下面的例子显示了一个只能包含三个字母的文本域（不含数字及特殊字符）：


```html
Country code: <input type="text" name="country_code" pattern="[A-Za-z]{3}"
	title="Three letter country code">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_pattern)


---


## placeholder 属性


placeholder 属性提供一种提示（hint），描述输入域所期待的值。


简短的提示在用户输入值前会显示在输入域上。


注意:** placeholder 属性适用于以下类型的  标签：text, search, url, telephone, email 以及 password。

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


input 字段提示文本t:


```html
<input type="text" name="fname" placeholder="First name">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_placeholder)


---


## required 属性


required 属性是一个 boolean 属性.


required 属性规定必须在提交之前填写输入域（不能为空）。


注意:**required 属性适用于以下类型的  标签：text, search, url, telephone, email, password, date pickers, number, checkbox, radio 以及 file。

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/incompatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


不能为空的input字段:


```html
Username: <input type="text" name="usrname" required>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_required)


---


## step 属性


step 属性为输入域规定合法的数字间隔。


如果 step="3"，则合法的数是 -3,0,3,6 等


提示：** step 属性可以与 max 和 min 属性创建一个区域值.


**注意:** step 属性与以下type类型一起使用: number, range, date, datetime, datetime-local, month, time 和 week.

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/incompatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


规定input step步长为3:


```html
<input type="number" name="points" step="3">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_input_step)


---


## HTML5 标签


| 标签 | 描述 |
| --- | --- |
|  | 定义一个form表单 |
|  | 定义一个 input 域 |








	  AI 思考中...





			** [HTML5 表单元素](https://www.runoob.com/html5-form-elements.html)
			[HTML5 语义元素](https://www.runoob.com/html5-semantic-elements.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/html-examples.html)

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