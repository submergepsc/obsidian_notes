# Bootstrap5 输入框组

- Source: https://www.runoob.com/bootstrap5/bootstrap5-form-input-group.html

我们可以使用 **.input-group** 类来向表单输入框中添加更多的样式，如图标、文本或者按钮。


**.input-group-text** 类来设置文本的样式。。


![](https://www.runoob.com/wp-content/uploads/2018/06/F42CE8CE-7FFF-4979-B1DA-6A03015C0A77.png)


## Bootstrap 实例


```css
<form>
  <div class="input-group mb-3">
    <span class="input-group-text">@</span>
    <input type="text" class="form-control" placeholder="Username">
  </div>

  <div class="input-group">
    <input type="text" class="form-control" placeholder="Your Email">
    <span class="input-group-text">@runoob.com</span>
  </div>
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_input_group)


---


## 输入框大小


使用 **.input-group-sm** 类来设置小的输入框， **.input-group-lg** 类设置大的输入框：


## Bootstrap 实例


```css
<div class="input-group mb-3 input-group-sm">
   <span class="input-group-text">Small</span>
  <input type="text" class="form-control">
</div>

<div class="input-group mb-3">
  <span class="input-group-text">Default</span>
  <input type="text" class="form-control">>
</div>

<div class="input-group mb-3 input-group-lg">
  <span class="input-group-text">Large</span>
  <input type="text" class="form-control">
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_input_group_size)


---


## 多个输入框和文本


## Bootstrap 实例


```css
<!-- 多个输入框 -->
<div class="input-group mb-3">
  <span class="input-group-text">Person</span>
  <input type="text" class="form-control" placeholder="First Name">
  <input type="text" class="form-control" placeholder="Last Name">
</div>

<!-- 多个文本信息 -->
<div class="input-group mb-3">
  <span class="input-group-text">One</span>
  <span class="input-group-text">Two</span>
  <span class="input-group-text">Three</span>
  <input type="text" class="form-control">
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_input_group_multiple)


---


## 复选框与单选框


文本信息可以使用复选框与单选框替代：


![](https://www.runoob.com/wp-content/uploads/2018/06/214FC0E4-82F0-4597-826B-E1C7B0B5F356.jpg)


## Bootstrap 实例


```css
<div class="input-group mb-3">
  <div class="input-group-text">
    <input type="checkbox">
  </div>
  <input type="text" class="form-control" placeholder="RUNOOB">
</div>

<div class="input-group mb-3">
  <div class="input-group-text">
    <input type="radio">
  </div>
  <input type="text" class="form-control" placeholder="GOOGLE">
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_input_group_check)


---


## 输入框添加按钮组


## Bootstrap 实例


```css
<div class="input-group mb-3">
  <button class="btn btn-outline-primary" type="button">Basic Button</button>
  <input type="text" class="form-control" placeholder="Some text">
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Search">
  <button class="btn btn-success" type="submit">Go</button>
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Something clever..">
  <button class="btn btn-primary" type="button">OK</button>
  <button class="btn btn-danger" type="button">Cancel</button>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_input_group_btn)


---


## 设置下拉菜单


输入框中添加下拉菜单不需要使用 .dropdown 类。


![](https://www.runoob.com/wp-content/uploads/2018/06/CE65025A-B840-45FA-BA3B-5173634CE5F2.jpg)


## Bootstrap 实例


```css
<div class="input-group mt-3 mb-3">
  <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown">
    选择网站
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="https://www.google.com">GOOGLE</a></li>
    <li><a class="dropdown-item" href="https://www.runoob.com">RUNOOB</a></li>
    <li><a class="dropdown-item" href="https://www.taobao.com">TAOBAO</a></li>
  </ul>
  <input type="text" class="form-control" placeholder="网站地址">
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_input_group_dropdown)


---

## 输入框组标签


在输入框组通过在输入框组外围的 label 来设置标签，标签的 for 属性需要与输入框组的 id 对应，点击标签后可以聚焦输入框：


![](https://www.runoob.com/wp-content/uploads/2018/06/9F8A9143-892B-4A8A-901A-37C1E4E55941.jpg)


## Bootstrap 实例


```css
<form>
    <label for="demo">这里输入您的邮箱:</label>
    <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Email" id="demo" name="email">
         <span class="input-group-text">@runoob.com</span>
    </div>
</form>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_input_group_labels)









	  AI 思考中...





			** [Bootstrap5 选择区间](https://www.runoob.com/bootstrap5-form-range.html)
			[Bootstrap5 表单浮动标签](https://www.runoob.com/bootstrap5-form-floating-labels.html) **













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