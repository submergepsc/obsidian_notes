# HTML 表单和输入

- Source: https://www.runoob.com/html/html-forms.html

---


HTML 表单用于收集用户的输入信息。


HTML 表单表示文档中的一个区域，此区域包含交互控件，将用户收集到的信息发送到 Web 服务器。


HTML 表单通常包含各种输入字段、复选框、单选按钮、下拉列表等元素。


以下是一个简单的HTML表单的例子：


- `` 元素用于创建表单，`action` 属性定义了表单数据提交的目标 URL，`method` 属性定义了提交数据的 HTTP 方法（这里使用的是 "post"）。
- `` 元素用于为表单元素添加标签，提高可访问性。
- `*` 元素是最常用的表单元素之一，它可以创建文本输入框、密码框、单选按钮、复选框等。`type` 属性定义了输入框的类型，`id` 属性用于关联 `` 元素，`name` 属性用于标识表单字段。
- `` 元素用于创建下拉列表，而 `` 元素用于定义下拉列表中的选项。


## 实例


```html
<form action="/" method="post">
    <!-- 文本输入框 -->
    <label for="name">用户名:</label>
    <input type="text" id="name" name="name" required>

    <br>

    <!-- 密码输入框 -->
    <label for="password">密码:</label>
    <input type="password" id="password" name="password" required>

    <br>

    <!-- 单选按钮 -->
    <label>性别:</label>
    <input type="radio" id="male" name="gender" value="male" checked>
    <label for="male">男</label>
    <input type="radio" id="female" name="gender" value="female">
    <label for="female">女</label>

    <br>

    <!-- 复选框 -->
    <input type="checkbox" id="subscribe" name="subscribe" checked>
    <label for="subscribe">订阅推送信息</label>

    <br>

    <!-- 下拉列表 -->
    <label for="country">国家:</label>
    <select id="country" name="country">
        <option value="cn">CN</option>
        <option value="usa">USA</option>
        <option value="uk">UK</option>
    </select>

    <br>

    <!-- 提交按钮 -->
    <input type="submit" value="提交">
</form>
```

**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_form_demo)

---


![Examples](https://www.runoob.com/images/tryitimg.gif)

## 在线实例


## 实例

以下实例创建了一个表单，包含两个输入框：
```html
<form action="">
First name: <input type="text" name="firstname"><br>
Last name: <input type="text" name="lastname">
</form>
```
 [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_input) ## 实例 以下实例创建了一个表单，包含一个普通输入框和一个密码输入框：
```html
<form action="">
Username: <input type="text" name="user"><br>
Password: <input type="password" name="password">
</form>
```
 [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_inputpassword) （在本页底端可以找到更多实例。）


---


## HTML 表单


表单是一个包含表单元素的区域。


表单元素是允许用户在表单中输入内容，比如：文本域（textarea）、下拉列表（select）、单选框（radio-buttons）、复选框（checkbox） 等等。


我们可以使用 **** 标签来创建表单:


## 实例


```html
<form>
.
input 元素
.
</form>
```


---


## HTML 表单 - 输入元素


多数情况下被用到的表单标签是输入标签 ****。

输入类型是由 **type** 属性定义。

接下来我们介绍几种常用的输入类型。


---


## 文本域（Text Fields）


文本域通过 **** 标签来设定，当用户要在表单中键入字母、数字等内容时，就会用到文本域。


## 实例


```html
<form>
First name: <input type="text" name="firstname"><br>
Last name: <input type="text" name="lastname">
</form>
```


浏览器显示如下：


First name:

Last name:


注意:**表单本身并不可见。同时，在大多数浏览器中，文本域的默认宽度是 20 个字符。


---


## 密码字段


密码字段通过标签 **** 来定义:


## 实例


```html
<form>
Password: <input type="password" name="pwd">
</form>
```


浏览器显示效果如下:


Password:


**注意：**密码字段字符不会明文显示，而是以星号 ***** 或圆点 **.** 替代。


---


## 单选按钮（Radio Buttons）


**** 标签定义了表单的单选框选项:


## 实例


```html
<form action="">
<input type="radio" name="sex" value="male">男<br>
<input type="radio" name="sex" value="female">女
</form>
```


浏览器显示效果如下:


男**
女


---


## 复选框（Checkboxes）


**** 定义了复选框。


复选框可以选取一个或多个选项：


## 实例


```html
<form>
<input type="checkbox" name="vehicle[]" value="Bike">我喜欢自行车<br>
<input type="checkbox" name="vehicle[]" value="Car">我喜欢小汽车
</form>
```


浏览器显示效果如下:


我喜欢自行车

我喜欢小汽车


---


## 提交按钮(Submit)


**** 定义了提交按钮。


当用户单击确认按钮时，表单的内容会被传送到服务器。表单的动作属性 **action** 定义了服务端的文件名。

**action** 属性会对接收到的用户输入数据进行相关的处理:


## 实例


```html
<form name="input" action="html_form_action.php" method="get">
Username: <input type="text" name="user">
<input type="submit" value="Submit">
</form>
```


浏览器显示效果如下:


Username:


假如您在上面的文本框内键入几个字母，然后点击确认按钮，那么输入数据会传送到 html_form_action.php** 文件，该页面将显示出输入的结果。


以上实例中有一个 method 属性，它用于定义表单数据的提交方式，可以是以下值：


- **post**：指的是 HTTP POST 方法，表单数据会包含在表单体内然后发送给服务器，用于提交敏感数据，如用户名与密码等。
- **get**：默认值，指的是 HTTP GET 方法，表单数据会附加在 **action** 属性的 URL 中，并以 **?**作为分隔符，一般用于不敏感信息，如分页等。例如：https://www.runoob.com/?page=1，这里的 page=1 就是 get 方法提交的数据。


## 实例


```html
<!-- 以下表单使用 GET 请求发送数据到当前的 URL，method 默认为 GET。 -->
<form>
  <label>Name:
    <input name="submitted-name" autocomplete="name">
  </label>
  <button>Save</button>
</form>

<!-- 以下表单使用 POST 请求发送数据到当前的 URL。 -->
<form method="post">
  <label>Name:
    <input name="submitted-name" autocomplete="name">
  </label>
  <button>Save</button>
</form>

<!-- 表单使用 fieldset, legend, 和 label 标签 -->
<form method="post">
  <fieldset>
    <legend>Title</legend>
    <label><input type="radio" name="radio"> Select me</label>
  </fieldset>
</form>
```


---


## 更多实例


[单选按钮(Radio buttons)](https://www.runoob.com/try/try.php?filename=tryhtml_radio) 本例演示如何在 HTML 中创建单选按钮。


[复选框(Checkboxes)](https://www.runoob.com/try/try.php?filename=tryhtml_checkbox) 本例演示如何在 HTML 页中创建复选框。用户可以选中或取消选取复选框。


[简单的下拉列表](https://www.runoob.com/try/try.php?filename=tryhtml_select2) 本例演示如何在 HTML 页面中创建简单的下拉列表框。下拉列表框是一个可选列表。


[预选下拉列表](https://www.runoob.com/try/try.php?filename=tryhtml_select3) 本例演示如何创建一个简单的带有预选值的下拉列表。


[文本域(Textarea)](https://www.runoob.com/try/try.php?filename=tryhtml_textarea) 本例演示如何创建文本域（多行文本输入控件）。用户可在文本域中写入文本。可写入字符的字数不受限制。


[创建按钮](https://www.runoob.com/try/try.php?filename=tryhtml_button) 本例演示如何创建按钮。你可以对按钮上的文字进行自定义。


## 表单实例


[带边框的表单](https://www.runoob.com/try/try.php?filename=tryhtml_legend) 本例演示如何在数据周围绘制一个带标题的框。


[带有输入框和确认按钮的表单](https://www.runoob.com/try/try.php?filename=tryhtml_form_submit) 本例演示如何向页面添加表单。此表单包含两个输入框和一个确认按钮。


[带有复选框的表单](https://www.runoob.com/try/try.php?filename=tryhtml_form_checkbox) 此表单包含两个复选框和一个确认按钮。


[带有单选按钮的表单](https://www.runoob.com/try/try.php?filename=tryhtml_form_radio) 此表单包含两个单选框和一个确认按钮。


[从表单发送电子邮件](https://www.runoob.com/try/try.php?filename=tryhtml_form_mail) 此例演示如何从表单发送电子邮件。


---


## HTML 表单标签


New : HTML5新标签


| 标签 | 描述 |
| --- | --- |
|  | 定义供用户输入的表单 |
|  | 定义输入域 |
|  | 定义文本域 (一个多行的输入控件) |
|  | 定义了 元素的标签，一般为输入标题 |
|  | 定义了一组相关的表单元素，并使用外框包含起来 |
|  | 定义了 元素的标题 |
|  | 定义了下拉选项列表 |
|  | 定义选项组 |
|  | 定义下拉列表中的选项 |
|  | 定义一个点击按钮 |
| New | 指定一个预先定义的输入控件选项列表 |
| New | 定义了表单的密钥对生成器字段 |
| New | 定义一个计算结果 |








	  AI 思考中...





			* [HTML 布局](https://www.runoob.com/html-layouts.html)
			[HTML 框架](https://www.runoob.com/html-iframes.html) **