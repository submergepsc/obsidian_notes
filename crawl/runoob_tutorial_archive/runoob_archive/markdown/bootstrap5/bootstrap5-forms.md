# Bootstrap5 表单

- Source: https://www.runoob.com/bootstrap5/bootstrap5-forms.html

在本章中，我们将学习如何使用 Bootstrap 创建表单。Bootstrap 通过一些简单的 HTML 标签和扩展的类即可创建出不同样式的表单。


表单元素 ****, ****, 和 **** elements 在使用 **.form-control** 类的情况下，宽度都是设置为 100%。


### Bootstrap5 表单布局


- 堆叠表单 (全屏宽度)：垂直方向
- 内联表单：水平方向


Bootstrap 提供了两种类型的表单布局:


---


## 堆叠表单


以下实例使用两个输入框，一个复选框，一个提交按钮来创建堆叠表单：


## 实例


```css
<form>
  <div class="mb-3 mt-3">
    <label for="email" class="form-label">Email:</label>
    <input type="email" class="form-control" id="email" placeholder="Enter email" name="email">
  </div>
  <div class="mb-3">
    <label for="pwd" class="form-label">Password:</label>
    <input type="password" class="form-control" id="pwd" placeholder="Enter password" name="pswd">
  </div>
  <div class="form-check mb-3">
    <label class="form-check-label">
      <input class="form-check-input" type="checkbox" name="remember"> Remember me
    </label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_form_basic)


显示效果：


![](https://www.runoob.com/wp-content/uploads/2017/10/BE33BCD9-4AE4-4349-B4FD-BEC4D7669670.jpg)


实例中我们使用 **.form-label** 类来确保标签元素有一定的内边距。


复选框（checkboxe）使用不同的标记。 它们使用 **.form-check** 包裹在容器元素周围。复选框和单选按钮使用 **.form-check-input**，它的标签可以使用 **.form-check-label** 类。


---


## 内联表单


如果您希望表单元素并排显示，请使用 **.row** 和 **.col**：


以下实例的两个输入框并排显示，创建内联表单：


## 实例


```css
<form>
  <div class="row">
    <div class="col">
      <input type="text" class="form-control" placeholder="Enter email" name="email">
    </div>
    <div class="col">
      <input type="password" class="form-control" placeholder="Enter password" name="pswd">
    </div>
  </div>
</form>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_inline)

显示效果：


![](https://www.runoob.com/wp-content/uploads/2022/02/0E325572-E93C-4D6B-9B0C-9CD3EAFA13AE.jpg)


## 文本框

使用 textarea 标签创建文本框提交表单，使用 **.form-control** 类渲染文本框 textareas 标签:


## 实例


```css
<label for="comment">请输入评论：</label>
<textarea class="form-control" rows="5" id="comment" name="text"></textarea>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_textarea)

显示效果：


![](https://www.runoob.com/wp-content/uploads/2022/02/9CDDC54C-1D77-494B-AAFC-577061A71BA7.jpg)


---


## 输入框大小


我们可以通过在 .form-control** 输入框中使用 **.form-control-lg** 或 **.form-control-sm** 类来设置输入框的大小:


## 实例


```css
<input type="text" class="form-control form-control-lg" placeholder="大号输入框">
<input type="text" class="form-control" placeholder="正常大小输入框">
<input type="text" class="form-control form-control-sm" placeholder="小号输入框">
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_input_size)

显示效果：


![](https://www.runoob.com/wp-content/uploads/2022/02/8E3EA52C-96A7-49BB-AC23-F10C6E9090FF.jpg)


---

## 禁用/只读表单


使用 **disabled/readonly** 属性设置输入框禁用/只读：


## 实例


```css
<input type="text" class="form-control" placeholder="Normal input">
<input type="text" class="form-control" placeholder="Disabled input" disabled>
<input type="text" class="form-control" placeholder="Readonly input" readonly>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_disabled)


---

## 纯文本输入

使用 **.form-control-plaintext** 类可以删除输入框的边框：：


## 实例


```css
<input type="text" class="form-control-plaintext" placeholder="Plaintext input">
<input type="text" class="form-control" placeholder="Normal input">
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_plaintext)


---

## 取色器

使用 **.form-control-color** 类可以创建一个取色器：


## 实例


```css
<input type="color" class="form-control form-control-color" value="#CCCCCC">
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_color)

显示效果：


![](https://www.runoob.com/wp-content/uploads/2022/02/F8EC32AE-BF20-4CB7-A9FB-53EA8897B423.jpg)








	  AI 思考中...





			** [Bootstrap5 Flex（弹性）布局](https://www.runoob.com/bootstrap5-flex.html)
			[Bootstrap5 下拉菜单](https://www.runoob.com/bootstrap5-form-select.html) **













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