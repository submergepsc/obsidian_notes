# CSS 表单

- Source: https://www.runoob.com/css/css-form.html

一个表单案例，我们使用 CSS 来渲染 HTML 的表单元素：


## CSS 实例


```css
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_forms)


---


## 输入框(input) 样式


使用 width 属性来设置输入框的宽度：


## CSS 实例


```css
input {
  width: 100%;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_form_width)


以上实例中设置了所有  元素的宽度为 100%，如果你只想设置指定类型的输入框可以使用以下属性选择器：


- `input[type=text]` - 选取文本输入框
- `input[type=password]` - 选择密码的输入框
- `input[type=number]` - 选择数字的输入框
- ...


---


## 输入框填充


使用 padding** 属性可以在输入框中添加内边距。


## CSS 实例


```css
input[type=text] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_form_padding)



注意我们设置了 `box-sizing` 属性为 `border-box`。这样可以确保浏览器呈现出带有指定宽度和高度的输入框是把边框和内边距一起计算进去的。 更多内容可以阅读 [CSS3 框大小](https://www.runoob.com/../css3/css3-box-sizing.html) 。


---


## 输入框(input) 边框


使用 `border` 属性可以修改 input 边框的大小或颜色，使用 `border-radius` 属性可以给 input 添加圆角：


## CSS 实例


```css
input[type=text] {
  border: 2px solid red;
  border-radius: 4px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_form_border)


如果你只想添加底部边框可以使用 `border-bottom` 属性:


## CSS 实例


```css
input[type=text] {
  border: none;
  border-bottom: 2px solid red;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_form_border2)


---


## 输入框(input) 颜色


可以使用 `background-color` 属性来设置输入框的背景颜色，`color` 属性用于修改文本颜色：


## CSS 实例


```css
input[type=text] {
  background-color: #3CBC8D;
  color: white;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_form_color)


---


## 输入框(input) 聚焦


默认情况下，一些浏览器在输入框获取焦点时（点击输入框）会有一个蓝色轮廓。我们可以设置 input 样式为 `outline: none;` 来忽略该效果。


使用 `:focus` 选择器可以设置输入框在获取焦点时的样式：


## CSS 实例


```css
input[type=text]:focus {
  background-color: lightblue;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_form_focus)


## CSS 实例


```css
input[type=text]:focus {
  border: 3px solid #555;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_form_focus2)

---


## 输入框(input) 图标


如果你想在输入框中添加图标，可以使用 `background-image` 属性和用于定位的`background-position` 属性。注意设置图标的左边距，让图标有一定的空间：


## CSS 实例


```css
input[type=text] {
  background-color: white;
  background-image: url('searchicon.png');
  background-position: 10px 10px;
  background-repeat: no-repeat;
  padding-left: 40px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_form_icon)


---


## 带动画的搜索框


以下实例使用了 CSS `transition` 属性，该属性设置了输入框在获取焦点时会向右延展。你可以在 [CSS 动画](https://www.runoob.com/../css3/css3-animations.html) 章节查看更多内容。


## CSS 实例


```css
input[type=text] {
  -webkit-transition: width 0.4s ease-in-out;
  transition: width 0.4s ease-in-out;
}

input[type=text]:focus {
  width: 100%;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_form_search_anim)

---


## 文本框（textarea）样式


注意:** 使用 `resize` 属性来禁用文本框可以重置大小的功能（一般拖动右下角可以重置大小）。


## CSS 实例


```css
textarea {
  width: 100%;
  height: 150px;
  padding: 12px 20px;
  box-sizing: border-box;
  border: 2px solid #ccc;
  border-radius: 4px;
  background-color: #f8f8f8;
  resize: none;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_form_textarea)


---


## 下拉菜单（select）样式


## CSS 实例


```css
select {
  width: 100%;
  padding: 16px 20px;
  border: none;
  border-radius: 4px;
  background-color: #f1f1f1;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_form_select)


---


## 按钮样式


## CSS 实例


```css
input[type=button], input[type=submit], input[type=reset] {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 16px 32px;
  text-decoration: none;
  margin: 4px 2px;
  cursor: pointer;
}

/* 提示: 使用 width: 100% 设置全宽按钮 */
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_form_button)


更多内容可以参考我们的 [CSS 按钮](https://www.runoob.com/../css3/css3-buttons.html) 教程。


---


## 响应式表单


响应式表单可以根据浏览器窗口的大小重新布局各个元素，我们可以通过重置浏览器窗口大小来查看效果：


高级:** 以下实例使用了[CSS3 多媒体查询](https://www.runoob.com/../css3/css3-mediaqueries.html) 来创建一个响应式表单。


## CSS 实例


```css
* {
  box-sizing: border-box;
}

input[type=text], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
}

label {
  padding: 12px 12px 12px 0;
  display: inline-block;
}

input[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  float: right;
}

input[type=submit]:hover {
  background-color: #45a049;
}

.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}

.col-25 {
  float: left;
  width: 25%;
  margin-top: 6px;
}

.col-75 {
  float: left;
  width: 75%;
  margin-top: 6px;
}

/* 清除浮动 */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* 响应式布局 layout - 在屏幕宽度小于 600px 时， 设置为上下堆叠元素 */
@media screen and (max-width: 600px) {
  .col-25, .col-75, input[type=submit] {
    width: 100%;
    margin-top: 0;
  }
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_form_responsive)










	  AI 思考中...





			** [CSS 布局 Overflow](https://www.runoob.com/css-overflow.html)
			[CSS 计数器](https://www.runoob.com/css-counters.html) **













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

      : ·[CSS 实例](https://www.runoob.com/css-examples.html)

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