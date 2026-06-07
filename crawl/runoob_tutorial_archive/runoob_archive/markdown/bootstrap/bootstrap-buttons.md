# Bootstrap 按钮

- Source: https://www.runoob.com/bootstrap/bootstrap-buttons.html

本章将通过实例讲解如何使用 Bootstrap 按钮。任何带有 class **.btn** 的元素都会继承圆角灰色按钮的默认外观。但是 Bootstrap 提供了一些选项来定义按钮的样式，具体如下表所示：


以下样式可用于, , 或  元素上：


| 类 | 描述 | 实例 |
| --- | --- | --- |
| .btn | 为按钮添加基本样式 | 尝试一下 |
| .btn-default | 默认/标准按钮 | 尝试一下 |
| .btn-primary | 原始按钮样式（未被操作） | 尝试一下 |
| .btn-success | 表示成功的动作 | 尝试一下 |
| .btn-info | 该样式可用于要弹出信息的按钮 | 尝试一下 |
| .btn-warning | 表示需要谨慎操作的按钮 | 尝试一下 |
| .btn-danger | 表示一个危险动作的按钮操作 | 尝试一下 |
| .btn-link | 让按钮看起来像个链接 (仍然保留按钮行为) | 尝试一下 |
| .btn-lg | 制作一个大按钮 | 尝试一下 |
| .btn-sm | 制作一个小按钮 | 尝试一下 |
| .btn-xs | 制作一个超小按钮 | 尝试一下 |
| .btn-block | 块级按钮(拉伸至父元素100%的宽度) | 尝试一下 |
| .active | 按钮被点击 | 尝试一下 |
| .disabled | 禁用按钮 | 尝试一下 |


下面的实例演示了上面所有的按钮 class：


## 实例


```css
<!-- 标准的按钮 -->
<button type="button" class="btn btn-default">默认按钮</button>
<!-- 提供额外的视觉效果，标识一组按钮中的原始动作 -->
<button type="button" class="btn btn-primary">原始按钮</button>
<!-- 表示一个成功的或积极的动作 -->
<button type="button" class="btn btn-success">成功按钮</button>
<!-- 信息警告消息的上下文按钮 -->
<button type="button" class="btn btn-info">信息按钮</button>
<!-- 表示应谨慎采取的动作 -->
<button type="button" class="btn btn-warning">警告按钮</button>
<!-- 表示一个危险的或潜在的负面动作 -->
<button type="button" class="btn btn-danger">危险按钮</button>
<!-- 并不强调是一个按钮，看起来像一个链接，但同时保持按钮的行为 -->
<button type="button" class="btn btn-link">链接按钮</button>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-button-options)


结果如下所示：


![按钮选项](https://www.runoob.com/wp-content/uploads/2014/06/buttonoptions_demo.jpg)


## 按钮大小


下表列出了获得各种大小按钮的 class：


| Class | 描述 |
| --- | --- |
| .btn-lg | 这会让按钮看起来比较大。 |
| .btn-sm | 这会让按钮看起来比较小。 |
| .btn-xs | 这会让按钮看起来特别小。 |
| .btn-block | 这会创建块级的按钮，会横跨父元素的全部宽度。 |


下面的实例演示了上面所有的按钮 class：


## 实例


```css
<p>
  <button type="button" class="btn btn-primary btn-lg">大的原始按钮</button>
  <button type="button" class="btn btn-default btn-lg">大的按钮</button>
</p>
<p>
  <button type="button" class="btn btn-primary">默认大小的原始按钮</button>
  <button type="button" class="btn btn-default">默认大小的按钮</button>
</p>
<p>
  <button type="button" class="btn btn-primary btn-sm">小的原始按钮</button>
  <button type="button" class="btn btn-default btn-sm">小的按钮</button>
</p>
<p>
  <button type="button" class="btn btn-primary btn-xs">特别小的原始按钮</button>
  <button type="button" class="btn btn-default btn-xs">特别小的按钮</button>
</p>
<p>
  <button type="button" class="btn btn-primary btn-lg btn-block">块级的原始按钮</button>
  <button type="button" class="btn btn-default btn-lg btn-block">块级的按钮</button>
</p>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-button-size)


结果如下所示：


![按钮大小](https://www.runoob.com/wp-content/uploads/2014/06/buttonsize_demo.jpg)


## 按钮状态


Bootstrap 提供了激活、禁用等按钮状态的 class，下面将进行详细讲解。


### 激活状态


按钮在激活时将呈现为被按压的外观（深色的背景、深色的边框、阴影）。


下表列出了让按钮元素和锚元素呈激活状态的 class：


| 元素 | Class |
| --- | --- |
| 按钮元素 | 添加 .active class 来显示它是激活的。 |
| 锚元素 | 添加 .active class 到 按钮来显示它是激活的。 |


下面的实例演示了这点：


## 实例


```css
<p>
  <button type="button" class="btn btn-default btn-lg ">默认按钮</button>
  <button type="button" class="btn btn-default btn-lg active">激活按钮</button>
</p>
<p>
  <button type="button" class="btn btn-primary btn-lg ">原始按钮</button>
  <button type="button" class="btn btn-primary btn-lg active">激活的原始按钮</button>
</p>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-button-activestate)


结果如下所示：


![按钮激活状态](https://www.runoob.com/wp-content/uploads/2014/06/buttonactivestate_demo.jpg)


### 禁用状态


当您禁用一个按钮时，它的颜色会变淡 50%，并失去渐变。


下表列出了让按钮元素和锚元素呈禁用状态的 class：


| 元素 | Class |
| --- | --- |
| 按钮元素 | 添加 disabled 属性 到 按钮。 |
| 锚元素 | 添加 disabled class 到 按钮。 |


下面的实例演示了这点：


## 实例


```css
<p>
  <button type="button" class="btn btn-default btn-lg">默认按钮</button>
  <button type="button" class="btn btn-default btn-lg" disabled="disabled">禁用按钮</button>
</p>
<p>
  <button type="button" class="btn btn-primary btn-lg ">原始按钮</button>
  <button type="button" class="btn btn-primary btn-lg" disabled="disabled">禁用的原始按钮</button>
</p>
<p>
  <a href="#" class="btn btn-default btn-lg" role="button">链接</a>
  <a href="#" class="btn btn-default btn-lg disabled" role="button">禁用链接</a>
</p>
<p>
  <a href="#" class="btn btn-primary btn-lg" role="button">原始链接</a>
  <a href="#" class="btn btn-primary btn-lg disabled" role="button">禁用的原始链接</a>
</p>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-button-disabledstate)


结果如下所示：


![按钮禁用状态](https://www.runoob.com/wp-content/uploads/2014/06/buttondisabledstate_demo.jpg)


## 按钮标签


您可以在 、 或  元素上使用按钮 class。但是建议您在  元素上使用按钮 class，避免跨浏览器的不一致性问题。


下面的实例演示了这点：


## 实例


```css
<a class="btn btn-default" href="#" role="button">链接</a>
<button class="btn btn-default" type="submit">按钮</button>
<input class="btn btn-default" type="button" value="输入">
<input class="btn btn-default" type="submit" value="提交">
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-button-tags)


结果如下所示：


![按钮标签](https://www.runoob.com/wp-content/uploads/2014/06/buttontags_demo.jpg)


---


## 按钮组


在 div 中直接使用 .btn-group 可以创建按钮组：


## 实例


```css
<div class="btn-group">
  <button type="button" class="btn btn-primary">Apple</button>
  <button type="button" class="btn btn-primary">Samsung</button>
  <button type="button" class="btn btn-primary">Sony</button>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=trybs_button_group)


使用 .btn-group-lg|sm|xs 来控制按钮组的大小：


## 实例


```css
<div class="btn-group btn-group-lg">
  <button type="button" class="btn btn-primary">Apple</button>
  <button type="button" class="btn btn-primary">Samsung</button>
  <button type="button" class="btn btn-primary">Sony</button>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=trybs_button_group_size)


如果要设置垂直方向的按钮可以通过 .btn-group-vertical 类来设置：


## 实例


```css
<div class="btn-group-vertical">
  <button type="button" class="btn btn-primary">Apple</button>
  <button type="button" class="btn btn-primary">Samsung</button>
  <button type="button" class="btn btn-primary">Sony</button>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=trybs_button_group_v)


---


## 自适应大小的按钮组


可以通过 .btn-group-justified 类来设置自适应大小的按钮组。


以下实例使用 a 标签来展示：


## 实例


```css
<div class="btn-group btn-group-justified">
  <a href="#" class="btn btn-primary">Apple</a>
  <a href="#" class="btn btn-primary">Samsung</a>
  <a href="#" class="btn btn-primary">Sony</a>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=trybs_button_group_justified)


注意:** 如果是 `` 元素, 你需要在外层使用 `.btn-group` 类来包裹:


## 实例


```css
<div class="btn-group btn-group-justified">
  <div class="btn-group">
    <button type="button" class="btn btn-primary">Apple</button>
  </div>
  <div class="btn-group">
    <button type="button" class="btn btn-primary">Samsung</button>
  </div>
  <div class="btn-group">
    <button type="button" class="btn btn-primary">Sony</button>
  </div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=trybs_button_group_justified2)


---

## 内嵌下拉菜单的按钮组


按钮组内嵌的按钮可以设置下拉菜单，如下实例：


## 实例


```css
<div class="btn-group">
  <button type="button" class="btn btn-primary">Apple</button>
  <button type="button" class="btn btn-primary">Samsung</button>
  <div class="btn-group">
    <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
    Sony <span class="caret"></span></button>
    <ul class="dropdown-menu" role="menu">
      <li><a href="#">Tablet</a></li>
      <li><a href="#">Smartphone</a></li>
    </ul>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=trybs_button_group_dropdown)


### 分割按钮


## 实例


```css
<div class="btn-group">
  <button type="button" class="btn btn-primary">Sony</button>
  <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
    <span class="caret"></span>
  </button>
  <ul class="dropdown-menu" role="menu">
    <li><a href="#">Tablet</a></li>
    <li><a href="#">Smartphone</a></li>
  </ul>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=trybs_button_group_split)









	  AI 思考中...





			** [Bootstrap 表单](https://www.runoob.com/bootstrap-forms.html)
			[Bootstrap 图片](https://www.runoob.com/bootstrap-images.html) **













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