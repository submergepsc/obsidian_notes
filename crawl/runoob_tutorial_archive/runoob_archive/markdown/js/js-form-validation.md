# JavaScript 表单验证

- Source: https://www.runoob.com/js/js-form-validation.html

表单验证是确保用户输入的数据符合预期格式和规则的过程。

在 Web 开发中，表单验证通常用于检查用户输入的有效性，例如电子邮件地址、密码、电话号码等。

通过表单验证，可以防止无效数据提交到服务器，从而提高数据的准确性和安全性。


---


## JavaScript 表单验证


JavaScript 可用来在数据被送往服务器前对 HTML 表单中的这些输入数据进行验证。


表单数据经常需要使用 JavaScript 来验证其正确性：


- 验证表单数据是否为空？
- 验证输入是否是一个正确的email地址？
- 验证日期是否输入正确？
- 验证表单输入内容是否为数字型？


### 为什么需要表单验证？


- **数据准确性**：确保用户输入的数据符合预期格式，避免无效数据。
- **安全性**：防止恶意用户提交有害数据，如 SQL 注入、跨站脚本攻击（XSS）等。
- **用户体验**：及时反馈用户输入错误，帮助用户快速纠正问题。


---


## JavaScript 表单验证的基本方法


JavaScript 提供了多种方法来实现表单验证。以下是几种常见的方式：


### 1. 使用 HTML5 内置验证


HTML5 提供了一些内置的表单验证功能，例如 `required`、`pattern`、`min`、`max` 等属性。这些属性可以简单地实现基本的表单验证。


## 实例


```javascript
<form>
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>
  <input type="submit" value="Submit">
</form>
```


在上面的例子中，`required` 属性确保用户必须输入电子邮件地址，而 `type="email"` 会自动验证输入是否为有效的电子邮件格式。


### 2. 使用 JavaScript 自定义验证


下面的函数用来检查用户是否已填写表单中的必填（或必选）项目。假如必填或必选项为空，那么警告框会弹出，并且函数的返回值为 false，否则函数的返回值则为 true（意味着数据没有问题）：


```javascript
function validateForm()
{
  var x=document.forms["myForm"]["fname"].value;
  if (x==null || x=="")
  {
    alert("姓必须填写");
    return false;
  }
}
```


以上函数在 form 表单提交时被调用:


## 实例


```javascript
<form name="myForm" action="demo-form.php" onsubmit="return validateForm()" method="post">
姓: <input type="text" name="fname">
<input type="submit" value="提交">
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_form_validation)


---


## E-mail 验证


下面的函数检查输入的数据是否符合电子邮件地址的基本语法。


意思就是说，输入的数据必须包含 @ 符号和点号(.)。同时，@ 不可以是邮件地址的首字符，并且 @ 之后需有至少一个点号：


```javascript
function validateForm(){
  var x=document.forms["myForm"]["email"].value;
  var atpos=x.indexOf("@");
  var dotpos=x.lastIndexOf(".");
  if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length){
    alert("不是一个有效的 e-mail 地址");
    return false;
  }
}
```


下面是连同 HTML 表单的完整代码：


## 实例


```javascript
<form name="myForm" action="demo-form.php" onsubmit="return validateForm();" method="post">
    Email: <input type="text" name="email">
    <input type="submit" value="提交">
</form>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_form_validate_email)


### 使用正则表达式进行验证


正则表达式（Regular Expression）是一种强大的工具，可以用于匹配复杂的字符串模式。

以下是一个使用正则表达式验证电子邮件地址的例子：


## 实例


```javascript
function validateEmail(email) {
  var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

var email = "[email protected]";
if (validateEmail(email)) {
  console.log('Valid email address.');
} else {
  console.log('Invalid email address.');
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_form_validate_email2)


在这个例子中，我们定义了一个正则表达式来验证电子邮件地址的格式。如果输入的电子邮件地址符合格式要求，函数会返回 `true`，否则返回 `false`。








	  AI 思考中...





			** [JavaScript 错误 – Throw、Try 和 Catch](https://www.runoob.com/js-errors.html)
			[JavaScript HTML DOM](https://www.runoob.com/js-htmldom.html) **













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

      : ·[JavaScript 实例](https://www.runoob.com/js-examples.html)

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