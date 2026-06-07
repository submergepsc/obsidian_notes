# Bootstrap5 Flex（弹性）布局

- Source: https://www.runoob.com/bootstrap5/bootstrap5-flex.html

Bootstrap5 通过 flex 类来控制页面的布局。


---

## 弹性盒子(flexbox)


Bootstrap 3 与 Bootstrap 4/5 最大的区别就是 Bootstrap 4/5 使用弹性盒子来布局，而不是使用浮动来布局。


弹性盒子是 CSS3 的一种新的布局模式，更适合响应式的设计，如果你还不了解 flex，可以阅读我们的 [CSS3 弹性盒子(Flex Box)](https://www.runoob.com/../css3/css3-flexbox.html) 教程


**
注意：IE9 及其以下版本不支持弹性盒子，所以如果你需要兼容 IE8-9，请使用 [Bootstrap 3](https://www.runoob.com/../bootstrap/bootstrap-tutorial.html)。


以下实例使用 d-flex 类创建一个弹性盒子容器，并设置三个弹性子元素：


## 实例


```css
<div class="d-flex p-3 bg-secondary text-white">
  <div class="p-2 bg-info">Flex item 1</div>
  <div class="p-2 bg-warning">Flex item 2</div>
  <div class="p-2 bg-primary">Flex item 3</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_flex)


创建显示在同一行上的弹性盒子容器可以使用 d-inline-flex 类:


## 实例


```css
<div class="d-inline-flex p-3 bg-secondary text-white">
  <div class="p-2 bg-info">Flex item 1</div>
  <div class="p-2 bg-warning">Flex item 2</div>
  <div class="p-2 bg-primary">Flex item 3</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_flex-inline)


---

## 水平方向


**.flex-row** 可以设置弹性子元素水平显示，这是默认的。


使用 **.flex-row-reverse** 类用于设置右对齐显示，即与 **.flex-row** 方向相反。


## 实例


```css
<div class="d-flex flex-row bg-secondary">
  <div class="p-2 bg-info">Flex item 1</div>
  <div class="p-2 bg-warning">Flex item 2</div>
  <div class="p-2 bg-primary">Flex item 3</div>
</div>

<div class="d-flex flex-row-reverse bg-secondary">
  <div class="p-2 bg-info">Flex item 1</div>
  <div class="p-2 bg-warning">Flex item 2</div>
  <div class="p-2 bg-primary">Flex item 3</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_flex-direction)


---


## 垂直方向


**.flex-column** 类用于设置弹性子元素垂直方向显示, **.flex-column-reverse** 用于翻转子元素：


## 实例


```css
<div class="d-flex flex-column">
  <div class="p-2 bg-info">Flex item 1</div>
  <div class="p-2 bg-warning">Flex item 2</div>
  <div class="p-2 bg-primary">Flex item 3</div>
</div>

<div class="d-flex flex-column-reverse">
  <div class="p-2 bg-info">Flex item 1</div>
  <div class="p-2 bg-warning">Flex item 2</div>
  <div class="p-2 bg-primary">Flex item 3</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_flex-direction2)


---


## 内容排列


**.justify-content-*** 类用于修改弹性子元素的排列方式，***** 号允许的值有：start (默认), end, center, between 或 around**:


## 实例


```css
<div class="d-flex justify-content-start">...</div>
<div class="d-flex justify-content-end">...</div>
<div class="d-flex justify-content-center">...</div>
<div class="d-flex justify-content-between">...</div>
<div class="d-flex justify-content-around">...</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_flex-justify)


---

## 等宽


.flex-fill 类强制设置各个弹性子元素的宽度是一样的:


## 实例


```css
<div class="d-flex">
  <div class="p-2 bg-info flex-fill">Flex item 1</div>
  <div class="p-2 bg-warning flex-fill">Flex item 2</div>
  <div class="p-2 bg-primary flex-fill">Flex item 3</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_flex-fill)


---

## 扩展


.flex-grow-1 用于设置子元素使用剩下的空间。以下实例中前面两个子元素只设置了它们所需要的空间，最后一个获取剩余空间。 :


## 实例


```css
<div class="d-flex">
  <div class="p-2 bg-info">Flex item 1</div>
  <div class="p-2 bg-warning">Flex item 2</div>
  <div class="p-2 bg-primary flex-grow-1">Flex item 3</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_flex-grow)


提示:** 使用 **.flex-shrink-1** 用于设置子元素的收缩规则。


---

## 排序


**.order** 类可以设置弹性子元素的排序，从 **.order-1** 到 **.order-12**，数字越低权重越高( **.order-1** 排在 **.order-2** 之前) :


## 实例


```css
<div class="d-flex bg-secondary">
  <div class="p-2 bg-info order-3">Flex item 1</div>
  <div class="p-2 bg-warning order-2">Flex item 2</div>
  <div class="p-2 bg-primary order-1">Flex item 3</div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_flex-order)


---

## 外边距


**.ms-auto** 类可以设置子元素右外边距为 auto**，即 **margin-right: auto!important;**，**.me-auto** 类可以设置子元素左外边距为 **auto**，即 **margin-left: auto!important;**:


## 实例


```css
<div class="d-flex mb-3 bg-secondary">
  <div class="p-2 ms-auto bg-info">Flex item 1</div>
  <div class="p-2 bg-warning">Flex item 2</div>
  <div class="p-2 bg-primary">Flex item 3</div>
</div>
<div class="d-flex mb-3 bg-secondary">
  <div class="p-2  bg-info">Flex item 1</div>
  <div class="p-2 bg-warning">Flex item 2</div>
  <div class="p-2 me-auto bg-primary">Flex item 3</div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_flex-auto-margins)


---

## 包裹


弹性容器中包裹子元素可以使用以下三个类： .flex-nowrap (默认), .flex-wrap 或 .flex-wrap-reverse。设置 flex 容器是单行或者多行。


## 实例


```css
<div class="d-flex flex-wrap">..</div>

<div class="d-flex flex-wrap-reverse">..</div>

<div class="d-flex flex-nowrap">..</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_flex-wrap)


---

## 内容对齐


我们可以使用 .align-content-* 来控制在垂直方向上如何去堆叠子元素，包含的值有：.align-content-start (默认), .align-content-end, .align-content-center, .align-content-between, .align-content-around 和 .align-content-stretch。


这些类在只有一行的弹性子元素中是无效的。


## 实例


```css
<div class="d-flex flex-wrap align-content-start">..</div>

<div class="d-flex flex-wrap align-content-end">..</div>

<div class="d-flex flex-wrap align-content-center">..</div>

<div class="d-flex flex-wrap align-content-around">..</div>

<div class="d-flex flex-wrap align-content-stretch">..</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_flex-align-content)


---

## 子元素对齐


如果要设置单行的子元素对齐可以使用 **.align-items-*** 类来控制，包含的值有：.align-items-start, .align-items-end, .align-items-center, .align-items-baseline, 和 .align-items-stretch (默认)**。


## 实例


```css
<div class="d-flex align-items-start">..</div>

<div class="d-flex align-items-end">..</div>

<div class="d-flex align-items-center">..</div>

<div class="d-flex align-items-around">..</div>

<div class="d-flex align-items-stretch">..</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_flex-align-items)


---

## 指定子元素对齐


如果要设置指定子元素对齐对齐可以使用 .align-self-* 类来控制，包含的值有：.align-self-start, .align-self-end, .align-self-center, .align-self-baseline, 和 .align-self-stretch (默认)。


## 实例


```css
<div class="d-flex bg-light" style="height:150px">
  <div class="p-2 border">Flex item 1</div>
  <div class="p-2 border align-self-start">Flex item 2</div>
  <div class="p-2 border">Flex item 3</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_flex-align-self)


---

## 响应式 flex 类

我们可以根据不同的设备，设置 flex 类，从而实现页面响应式布局，以下表格中的 * 号可以的值有：sm, md, lg 或 xl, 对应的是小型设备、中型设备，大型设备，超大型设备。


| 类 | 实例 | 实现 |
| --- | --- | --- |
| 弹性容器 |  |  |
| .d-*-flex | 根据不同的屏幕设备创建弹性盒子容器 | 尝试一下 |
| .d-*-inline-flex | 根据不同的屏幕设备创建行内弹性盒子容器 | 尝试一下 |
| 方向 |  |  |
| .flex-*-row | 根据不同的屏幕设备在水平方向显示弹性子元素 | 尝试一下 |
| .flex-*-row-reverse | 根据不同的屏幕设备在水平方向显示弹性子元素，且右对齐 | 尝试一下 |
| .flex-*-column | 根据不同的屏幕设备在垂直方向显示弹性子元素 | 尝试一下 |
| .flex-*-column-reverse | 根据不同的屏幕设备在垂直方向显示弹性子元素，且方向相反 | 尝试一下 |
| 内容对齐 |  |  |
| .justify-content-*-start | 根据不同屏幕设备在开始位置显示弹性子元素 (左对齐) | 尝试一下 |
| .justify-content-*-end | 根据不同屏幕设备在尾部显示弹性子元素 (右对齐) | 尝试一下 |
| .justify-content-*-center | 根据不同屏幕设备在 flex 容器中居中显示子元素 | 尝试一下 |
| .justify-content-*-between | 根据不同屏幕设备使用 "between" 显示弹性子元素 | 尝试一下 |
| .justify-content-*-around | 根据不同屏幕设备使用 "around" 显示弹性子元素 | 尝试一下 |
| 等宽 |  |  |
| .flex-*-fill | 根据不同的屏幕设备强制等宽 | 尝试一下 |
| 扩展 |  |  |
| .flex-*-grow-0 | 不同的屏幕设备不设置扩展 |  |
| .flex-*-grow-1 | 不同的屏幕设备设置扩展 |  |
| 收缩 |  |  |
| .flex-*-shrink-0 | 不同的屏幕设备不设置收缩 |  |
| .flex-*-shrink-1 | 不同的屏幕设备设置收缩 |  |
| 包裹 |  |  |
| .flex-*-nowrap | 不同的屏幕设备不设置包裹元素 | 尝试一下 |
| .flex-*-wrap | 不同的屏幕设备设置包裹元素 | 尝试一下 |
| .flex-*-wrap-reverse | 不同的屏幕设备反转包裹元素 | 尝试一下 |
| 内容排列 |  |  |
| .align-content-*-start | 根据不同屏幕设备在起始位置堆叠元素 | 尝试一下 |
| .align-content-*-end | 根据不同屏幕设备在结束位置堆叠元素 | 尝试一下 |
| .align-content-*-center | 根据不同屏幕设备在中间位置堆叠元素 | 尝试一下 |
| .align-content-*-around | 根据不同屏幕设备，使用 "around" 堆叠元素 | 尝试一下 |
| .align-content-*-stretch | 根据不同屏幕设备，通过伸展元素来堆叠 | 尝试一下 |
| 排序 |  |  |
| .order-*-0-12 | 在小屏幕尺寸上修改排序 | 尝试一下 |
| 元素对齐 |  |  |
| .align-items-*-start | 根据不同屏幕设备，让元素在头部显示在同一行。 | 尝试一下 |
| .align-items-*-end | 根据不同屏幕设备，让元素在尾部显示在同一行。 | 尝试一下 |
| .align-items-*-center | 根据不同屏幕设备，让元素在中间位置显示在同一行。 | 尝试一下 |
| .align-items-*-baseline | 根据不同屏幕设备，让元素在基线上显示在同一行。 | 尝试一下 |
| .align-items-*-stretch | 根据不同屏幕设备，让元素延展高度并显示在同一行。 | 尝试一下 |
| 单独一个子元素的对齐方式 |  |  |
| .align-self-*-start | 据不同屏幕设备，让单独一个子元素显示在头部。 | 尝试一下 |
| .align-self-*-end | 据不同屏幕设备，让单独一个子元素显示在尾部 | 尝试一下 |
| .align-self-*-center | 据不同屏幕设备，让单独一个子元素显示在居中位置 | 尝试一下 |
| .align-self-*-baseline | 据不同屏幕设备，让单独一个子元素显示在基线位置 | 尝试一下 |
| .align-self-*-stretch | 据不同屏幕设备，延展一个单独子元素 | 尝试一下 |








	  AI 思考中...





			** [Bootstrap5 小工具](https://www.runoob.com/bootstrap5-utilities.html)
			[Bootstrap5 表单](https://www.runoob.com/bootstrap5-forms.html) **













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