# Bootstrap5 小工具

- Source: https://www.runoob.com/bootstrap5/bootstrap5-utilities.html

Bootstrap 5 提供了很多有用的类来帮组我们快速实现效果，不需要重复写一些 CSS 代码。


---


## 背景颜色


设置不同元素的背景颜色时，需要通过 **.text-*** 类来设置匹配的文本颜色：


![](https://www.runoob.com/wp-content/uploads/2021/10/3F24FFA6-04D7-4701-89A6-4248236D7723.jpeg)


## 实例


```css
<div class="p-3 mb-2 bg-primary text-white">.bg-primary</div>
<div class="p-3 mb-2 bg-secondary text-white">.bg-secondary</div>
<div class="p-3 mb-2 bg-success text-white">.bg-success</div>
<div class="p-3 mb-2 bg-danger text-white">.bg-danger</div>
<div class="p-3 mb-2 bg-warning text-dark">.bg-warning</div>
<div class="p-3 mb-2 bg-info text-dark">.bg-info</div>
<div class="p-3 mb-2 bg-light text-dark">.bg-light</div>
<div class="p-3 mb-2 bg-dark text-white">.bg-dark</div>
<div class="p-3 mb-2 bg-body text-dark">.bg-body</div>
<div class="p-3 mb-2 bg-white text-dark">.bg-white</div>
<div class="p-3 mb-2 bg-transparent text-dark">.bg-transparent</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_utilities1)

**.bg-gradient** 类可以设置背景颜色渐变的效果：


## 实例


```css
<div class="p-3 mb-2 bg-primary bg-gradient text-white">.bg-primary</div>
<div class="p-3 mb-2 bg-secondary bg-gradient text-white">.bg-secondary</div>
<div class="p-3 mb-2 bg-success bg-gradient text-white">.bg-success</div>
<div class="p-3 mb-2 bg-danger bg-gradient text-white">.bg-danger</div>
<div class="p-3 mb-2 bg-warning bg-gradient text-dark">.bg-warning</div>
<div class="p-3 mb-2 bg-info bg-gradient text-dark">.bg-info</div>
<div class="p-3 mb-2 bg-light bg-gradient text-dark">.bg-light</div>
<div class="p-3 mb-2 bg-dark bg-gradient text-white">.bg-dark</div>
<div class="p-3 mb-2 bg-body bg-gradient text-dark">.bg-body</div>
<div class="p-3 mb-2 bg-white bg-gradient text-dark">.bg-white</div>
<div class="p-3 mb-2 bg-transparent bg-gradient text-dark">.bg-transparent</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_utilities2)


---


## 边框

我们可以使用 **border** 相关类根据需要显示边框：


![](https://www.runoob.com/wp-content/uploads/2021/10/F0F3CCC1-7F10-47EB-BE2A-28CD2AD2E560.jpg)


## 实例


```css
<span class="border"></span>
<span class="border border-0"></span>
<span class="border border-top-0"></span>
<span class="border border-end-0"></span>
<span class="border border-bottom-0"></span>
<span class="border border-start-0"></span>
<br>

<span class="border-top"></span>
<span class="border-end"></span>
<span class="border-bottom"></span>
<span class="border-start"></span>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_utilities3)

**.border-1** 到 **.border-5** 类用于设置边框线条的宽度：


## 实例


```css
<span class="border border-1"></span>
<span class="border border-2"></span>
<span class="border border-3"></span>
<span class="border border-4"></span>
<span class="border border-5"></span>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_utilities4)

以下设置了边框的不同颜色：


## 实例


```css
<span class="border border-primary"></span>
<span class="border border-secondary"></span>
<span class="border border-success"></span>
<span class="border border-danger"></span>
<span class="border border-warning"></span>
<span class="border border-info"></span>
<span class="border border-light"></span>
<span class="border border-dark"></span>
<span class="border border-white"></span>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_utilities5)

rounded** 相关类用于设置圆角：


![](https://www.runoob.com/wp-content/uploads/2021/10/E27B807D-2658-447A-96CF-6F0D1DD05CCE.jpg)


## 实例


```css
<img src="..." class="rounded" alt="...">
<img src="..." class="rounded-top" alt="...">
<img src="..." class="rounded-end" alt="...">
<img src="..." class="rounded-bottom" alt="...">
<img src="..." class="rounded-start" alt="...">
<img src="..." class="rounded-circle" alt="...">
<img src="..." class="rounded-pill" alt="...">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_utilities6)


**rounded-0** 到 **rounded-3** 类用于设置圆角的大小：


## 实例


```css
<img src="..." class="rounded-0" alt="...">
<img src="..." class="rounded-1" alt="...">
<img src="..." class="rounded-2" alt="...">
<img src="..." class="rounded-3" alt="...">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_utilities7)

---


## 浮动与清除浮动

元素向右浮动使用 .float-end 类，向左浮动使用 .float-start 类， .clearfix 类用于清除浮动:


## 实例


```css
<div class="clearfix">
  <span class="float-start">Float left</span>
  <span class="float-end">Float right</span>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_utilities8)


也可以根据屏幕尺寸来设置浮动效果(.float-*-left|right - * 表示 sm (>=576px), md (>=768px), lg (>=992px), xl (>=1200px) or xxl (>=1400px)):


## 实例


```css
<div class="float-sm-end">小屏幕向右浮动</div><br>
<div class="float-md-end">中等屏幕向右浮动</div><br>
<div class="float-lg-end">大屏幕向右浮动</div><br>
<div class="float-xl-end">超大屏幕向右浮动</div><br>
<div class="float-xxl-end">特大屏幕向右浮动</div><br>
<div class="float-none">没有浮动</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_utilities9)


---


## 居中对齐

使用 **.mx-auto** 类来设置元素居中对齐 (添加 margin-left 和 margin-right 为 auto):


## 实例


```css
<div class="mx-auto bg-warning" style="width:150px">居中对齐</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_utilities10)


---


## 宽度与高度

宽度使用 **w-* (.w-25, .w-50, .w-75, .w-100, .mw-auto, .mw-100)** 类来设置。


## 实例


```css
<div class="w-25 bg-warning">宽度为 25%</div>
<div class="w-50 bg-warning">宽度为 50%</div>
<div class="w-75 bg-warning">宽度为 75%</div>
<div class="w-100 bg-warning">宽度为 100%</div>
<div class="w-auto bg-warning">自动设置宽度</div>
<div class="mw-100 bg-warning">最大宽度为 100%</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_utilities11)


高度使用 **h-* (.h-25, .h-50, .h-75, .h-100, .mh-auto, .mh-100)** 类来设置。


## 实例


```css
<div style="height:200px;background-color:#ddd">
    <div class="h-25 d-inline-block p-2 bg-warning">高度为 25%</div>
    <div class="h-50 d-inline-block p-2 bg-warning">高度为 50%</div>
    <div class="h-75 d-inline-block p-2 bg-warning">高度为 75%</div>
    <div class="h-100 d-inline-block p-2 bg-warning">高度为 100%</div>
    <div class="h-auto d-inline-block p-2 bg-warning">自动设置高度</div>
    <div class="mh-100 d-inline-block p-2 bg-warning" style="height:500px">最大高度为 100%</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_utilities12)

---


## 间距

间距设置语法如下:


```
{property}{sides}-{size}  // 适用 xs(<=576px)
{property}{sides}-{breakpoint}-{size} // 适用 sm (>=576px), md (>=768px), lg (>=992px), xl (>=1200px) 或 xxl (>=1400px)
```


> breakpoints 指的是屏幕宽度: xs (=576px), md (>=768px), lg (>=992px), xl (>=1200px) 或 xxl (>=1400px)。


**property** 代表属性，包含：


- `m` - 用来设置 `margin`
- `p` - 用来设置 `padding`


**sides** 主要指方向：


- `t` - 用来设置 `margin-top` 或 `padding-top`
- `b` - 用来设置 `margin-bottom` 或 `padding-bottom`
- `s` - 用来设置 `margin-left` 或 `padding-left`
- `e` - 用来设置 `margin-right` 或 `padding-right`
- `x` - 用来设置 `*-left` 和 `*-right`
- `y` - 用来设置 `*-top` 和 `*-bottom`
- blank - 用来设置元素在四个方向的 `margin` 或 `padding`


**size** 指的是边距的大小：


- `0` - 设置 `margin` 或 `padding` 为 `0`
- `1` - 设置 `margin` 或 `padding` 为 `$spacer * .25`
- `2` - 设置 `margin` 或 `padding` 为 `$spacer * .5`
- `3` - 设置 `margin` 或 `padding` 为 `$spacer`
- `4` - 设置`margin` 或 `padding` 为 `$spacer * 1.5`
- `5` - 设置 `margin` 或 `padding` 为 `$spacer * 3`
- `auto` - 设置 `margin` 为 auto


看下部分边距的源码设置：


```
.mt-0 {
  margin-top: 0 !important;
}

.ml-1 {
  margin-left: ($spacer * .25) !important;
}

.px-2 {
  padding-left: ($spacer * .5) !important;
  padding-right: ($spacer * .5) !important;
}

.p-3 {
  padding: $spacer !important;
}
```


## 实例


```css
<div class="mx-auto" style="width: 200px;">
  元素设置居中
</div>

<form >
    <div class="form-row">
        <div class="form-group">

        <label for="text" class="mt-2">设置 margin-top：</label>
        <input type="text" class="form-control" id="text" placeholder="email">

        <label for="color" class="mt-2">颜色：</label>
        <input type="color" id="color" class="form-control" style="width: 60px;padding: 4px;" autocomplete="off" value="#656565">
        </div>
    </div>
</form>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_utilities13)

### 更多实例


| .m-# / m-*-# | 设置所有边的外边距 | 尝试一下 |
| --- | --- | --- |
| .mt-# / mt-*-# | margin top | 尝试一下 |
| .mb-# / mb-*-# | margin bottom | 尝试一下 |
| .ms-# / ms-*-# | margin left | 尝试一下 |
| .me-# / me-*-# | margin right | 尝试一下 |
| .mx-# / mx-*-# | margin left 与 right | 尝试一下 |
| .my-# / my-*-# | margin top 与 bottom | 尝试一下 |
| .p-# / p-*-# | 使用边设置 padding | 尝试一下 |
| .pt-# / pt-*-# | padding top | 尝试一下 |
| .pb-# / pb-*-# | padding bottom | 尝试一下 |
| .ps-# / ps-*-# | padding left | 尝试一下 |
| .pe-# / pe-*-# | padding right | 尝试一下 |
| .py-# / py-*-# | padding top 与 bottom | 尝试一下 |
| .px-# / px-*-# | padding left 与 right | 尝试一下 |








	  AI 思考中...





			** [Bootstrap5 侧边栏导航(Offcanvas)](https://www.runoob.com/bootstrap5-offcanvas.html)
			[Bootstrap5 Flex（弹性）布局](https://www.runoob.com/bootstrap5-flex.html) **













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