# Bootstrap4 表单控件

- Source: https://www.runoob.com/bootstrap4/bootstrap4-forms-inputs.html

Bootstrap4 支持以下表单控件：


- input
- textarea
- checkbox
- radio
- select


## Bootstrap Input


Bootstrap 支持所有的 HTML5 输入类型: text, password, datetime, datetime-local, date, month, time, week, number, email, url, search, tel, 以及 color。


**注意：:** 如果 input 的 type 属性未正确声明，输入框的样式将不会显示。


以下实例使用两个 input 元素，一个是 text，一个是 password ：


## 实例


```css
<div class="form-group">
  <label for="usr">用户名:</label>
  <input type="text" class="form-control" id="usr">
</div>
<div class="form-group">
  <label for="pwd">密码:</label>
  <input type="password" class="form-control" id="pwd">
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_form_input)

---


## Bootstrap textarea


以下实例演示了 textarea 的样式。


## 实例


```css
<div class="form-group">
  <label for="comment">评论:</label>
  <textarea class="form-control" rows="5" id="comment"></textarea>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_form_textarea)


---


## Bootstrap 复选框(checkbox)


复选框用于让用户从一系列预设置的选项中进行选择，可以选一个或多个。


以下实例包含了三个选项。最后一个是禁用的：


## 实例


```css
<div class="form-check">
  <label class="form-check-label">
    <input type="checkbox" class="form-check-input" value="">Option 1
  </label>
</div>
<div class="form-check">
  <label class="form-check-label">
    <input type="checkbox" class="form-check-input" value="">Option 2
  </label>
</div>
<div class="form-check disabled">
  <label class="form-check-label">
    <input type="checkbox" class="form-check-input" value="" disabled>Option 3
  </label>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_form_checkbox)


使用 **.form-check-inline** 类可以让选项显示在同一行上：


## 实例


```css
<div class="form-check form-check-inline">
  <label class="form-check-label">
    <input type="checkbox" class="form-check-input" value="">Option 1
  </label>
</div>
<div class="form-check form-check-inline">
  <label class="form-check-label">
    <input type="checkbox" class="form-check-input" value="">Option 2
  </label>
</div>
<div class="form-check form-check-inline disabled">
  <label class="form-check-label">
    <input type="checkbox" class="form-check-input" value="" disabled>Option 3
  </label>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_form_checkbox_inline)


---


## Bootstrap 单选框(Radio)


单选框用于让用户从一系列预设置的选项中进行选择，只能选一个。


以下实例包含了三个选项。最后一个是禁用的：


## 实例


```css
<div class="radio">
  <label><input type="radio" name="optradio">Option 1</label>
</div>
<div class="radio">
  <label><input type="radio" name="optradio">Option 2</label>
</div>
<div class="radio disabled">
  <label><input type="radio" name="optradio" disabled>Option 3</label>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_form_radio)

使用 **.radio-inline** 类可以让选项显示在同一行上：


## 实例


```css
<label class="radio-inline"><input type="radio" name="optradio">Option 1</label>
<label class="radio-inline"><input type="radio" name="optradio">Option 2</label>
<label class="radio-inline"><input type="radio" name="optradio" disabled>Option 3</label>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_form_radio_inline)


---


## Bootstrap select 下拉菜单


当您想让用户从多个选项中进行选择，但是默认情况下只能选择一个选项时，则使用选择框。


以下实例包含了两个下拉菜单：


## 实例


```css
<div class="form-group">
  <label for="sel1">下拉菜单:</label>
  <select class="form-control" id="sel1">
    <option>1</option>
    <option>2</option>
    <option>3</option>
    <option>4</option>
  </select>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_form_select)







	  AI 思考中...





			** [Bootstrap4 表单](https://www.runoob.com/bootstrap4-forms.html)
			[Bootstrap4 轮播](https://www.runoob.com/bootstrap4-carousel.html) **













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