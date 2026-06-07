# Tailwind CSS 尺寸控制

- Source: https://www.runoob.com/tailwindcss/tailwindcss-sizing.html

Tailwind CSS 提供了一组简洁的工具类，帮助开发者在 HTML 中快速控制元素的尺寸。

以下是一些常见的尺寸控制工具类及其用法。


---


## 宽度 - w-*


**w-*** 用于设置元素的宽度。

Tailwind 提供了一些预定义的宽度，支持像素、百分比、视口单位等。


| 类名 | 含义 | 示例 |
| --- | --- | --- |
| w-1/2 | 设置宽度为父元素的一半 | Content |
| w-1/4 | 设置宽度为父元素的四分之一 | Content |
| w-full | 设置宽度为父元素的 100% | Content |
| w-screen | 设置宽度为视口宽度 | Content |
| w-64 | 设置宽度为 16rem（256px） | Content |
| w-auto | 宽度根据内容自适应 | Content |


使用 w-px、w-1、w-64 等工具类来设置元素的固定宽度。


## 实例


```css
<div class="w-96 ...">w-96</div>
<div class="w-80 ...">w-80</div>
<div class="w-64 ...">w-64</div>
<div class="w-48 ...">w-48</div>
<div class="w-40 ...">w-40</div>
<div class="w-32 ...">w-32</div>
<div class="w-24 ...">w-24</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_sizing1)


使用 w-full、w-1/2、w-2/5 等工具类来设置基于百分比的元素宽度。


## 实例


```css
<div class="flex ...">
  <div class="w-1/2 ... ">w-1/2</div>
  <div class="w-1/2 ... ">w-1/2</div>
</div>
<div class="flex ...">
  <div class="w-2/5 ...">w-2/5</div>
  <div class="w-3/5 ...">w-3/5</div>
</div>
<div class="flex ...">
  <div class="w-1/3 ...">w-1/3</div>
  <div class="w-2/3 ...">w-2/3</div>
</div>
<div class="flex ...">
  <div class="w-1/4 ...">w-1/4</div>
  <div class="w-3/4 ...">w-3/4</div>
</div>
<div class="flex ...">
  <div class="w-1/5 ...">w-1/5</div>
  <div class="w-4/5 ...">w-4/5</div>
</div>
<div class="flex ...">
  <div class="w-1/6 ...">w-1/6</div>
  <div class="w-5/6 ...">w-5/6</div>
</div>
<div class="w-full ...">w-full</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_sizing2)


使用 w-screen 使元素跨越整个视口的宽度。


```
<div class="w-screen">
  <!-- ... -->
</div>
```


如果需要在特定条件下（例如，在特定的断点）去除元素的指定宽度，w-auto 实用工具可能会很有用：


```
<div class="w-full md:w-auto">
  <!-- ... -->
</div>
```


## 高度 - h-*


高度类用于设置元素的高度，同样支持像素、百分比和视口单位等。常用的高度工具类包括：


| 类名 | 含义 | 示例 |
| --- | --- | --- |
| h-16 | 设置高度为 4rem（64px） | Content |
| h-1/2 | 设置高度为父元素的一半 | Content |
| h-screen | 设置高度为视口高度 | Content |
| h-auto | 高度根据内容自适应 | Content |

使用 h-px、h-1、h-64 等工具类来设置元素的固定高度。


## 实例


```css
<div class="h-96 ...">h-96</div>
<div class="h-80 ...">h-80</div>
<div class="h-64 ...">h-64</div>
<div class="h-48 ...">h-48</div>
<div class="h-40 ...">h-40</div>
<div class="h-32 ...">h-32</div>
<div class="h-24 ...">h-24</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_sizing3)

使用 h-full 将元素的高度设置为其父元素的 100%，前提是父元素有一个定义的高度。


```
<div class="h-48">
  <div class="h-full ...">
    <!-- 这个元素的高度将是 `12rem`（h-48） -->
  </div>
</div>
```


使用 h-screen 使元素跨越整个视口的高度。


```
<div class="h-screen">
  <!-- ... -->
</div>
```


使用 h-dvh 使元素跨越整个视口的高度，当浏览器用户界面扩展或收缩时，高度也会随之变化。


在视口中上下滚动以隐藏/显示浏览器用户界面：


## 实例


```css
<div class="h-dvh">
  <!-- ... -->
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_sizing4)

使用 h-lvh 将元素的高度设置为视口可能的最大高度。这与 100vh 的行为相同。


在视口中上下滚动以隐藏/显示浏览器用户界面：


## 实例


```css
<div class="h-lvh">
  <!-- ... -->
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_sizing5)


使用 h-svh 将元素的高度设置为视口可能的最小高度。


```
<div class="h-svh">
  <!-- ... -->
</div>
```


---


## Size 工具类


在 Tailwind CSS 中，`size` 工具类可以让你同时设置元素的宽度（`width`）和高度（`height`）。这些工具类通常用于需要固定宽高比例的场景，比如创建正方形、圆形或某些具有固定比例的容器。


### size-* 类


Tailwind 提供了一些 `size` 工具类，可以设置一个元素的 宽度和高度** 为相同的值。

常用的工具类包括：


| 类名 | 含义 | 示例 |
| --- | --- | --- |
| size-0 | 设置宽度和高度为 0 | Content |
| size-1 | 设置宽度和高度为 0.25rem | Content |
| size-2 | 设置宽度和高度为 0.5rem | Content |
| size-4 | 设置宽度和高度为 1rem | Content |
| size-8 | 设置宽度和高度为 2rem | Content |
| size-16 | 设置宽度和高度为 4rem | Content |
| size-32 | 设置宽度和高度为 8rem | Content |
| size-64 | 设置宽度和高度为 16rem | Content |
| size-auto | 设置宽度和高度自动适应 | Content |


这些 `size` 工具类会同时为元素的宽度和高度设置相同的值，通常用于需要等宽高的场景，如：


- 圆形图片
- 卡片组件
- 按钮等固定尺寸的元素

使用 size-px、size-1、size-64 等工具类同时设置元素的固定宽度和高度。


## 实例


```css
<div class="size-16 ...">size-16</div>
<div class="size-20 ...">size-20</div>
<div class="size-24 ...">size-24</div>
<div class="size-32 ...">size-32</div>
<div class="size-40 ...">size-40</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_sizing6)


使用 size-full 将元素的宽度和高度设置为父容器宽度和高度的 100%。


```
<div class="h-56 p-2 ...">
  <div class="size-full ...">size-full</div>
</div>
```


如果需要在特定条件下（例如，在特定的断点）去除元素的指定宽度和高度，size-auto 实用工具可能会很有用：


```
<div class="size-full md:size-auto">
  <!-- ... -->
</div>
```


size-auto 类非常适用于那些尺寸不固定、根据内容大小自适应的元素。


Tailwind CSS 还支持响应式设计，可以在不同屏幕尺寸下使用不同的 `size` 工具类。你可以在不同的屏幕宽度下为元素设置不同的宽度和高度。


```
<div class="size-16 md:size-32 lg:size-64">
  This box's size will change based on the screen size.
</div>
```


在上面的代码中，size-16 是默认大小，在中等屏幕（md:）时会变为 size-32，在大屏幕（lg:）时会变为 size-64。


---


## 最小宽度 - min-w-*


`min-w-*` 用于设置元素的最小宽度，确保元素在其内容不足时不小于指定的宽度。


| 类名 | 含义 | 示例 |
| --- | --- | --- |
| min-w-full | 设置最小宽度为 100% | Content |
| min-w-0 | 设置最小宽度为 0 | Content |
| min-w-max | 设置最小宽度为内容的最大宽度 | Content |


---


## 最小高度 - min-h-*
`min-h-*` 用于设置元素的最小高度，确保元素的高度不会小于指定的值。

| 类名 | 含义 | 示例 |
| --- | --- | --- |
| min-h-0 | 设置最小高度为 0 | Content |
| min-h-full | 设置最小高度为父元素的 100% | Content |
| min-h-screen | 设置最小高度为视口高度 | Content |

---


## 最大宽度（Max Width） - max-w-*


`max-w-*` 用于设置元素的最大宽度，当元素的内容宽度超过此值时，元素宽度不会继续增加。


| 类名 | 含义 | 示例 |
| --- | --- | --- |
| max-w-xs | 设置最大宽度为 20rem（320px） | Content |
| max-w-sm | 设置最大宽度为 24rem（384px） | Content |
| max-w-full | 设置最大宽度为父容器的 100% | Content |


---


## 最大高度（Max Height） - max-h-*


`max-h-*` 用于设置元素的最大高度，当元素的内容高度超过此值时，元素高度将不会继续增加。


| 类名 | 含义 | 示例 |
| --- | --- | --- |
| max-h-32 | 设置最大高度为 8rem（128px） | Content |
| max-h-screen | 设置最大高度为视口高度 | Content |


---


## 自动尺寸（Auto） - auto


`w-auto` 和 `h-auto` 类用于让元素的宽度或高度根据其内容自适应。


| 类名 | 含义 | 示例 |
| --- | --- | --- |
| w-auto | 宽度自动调整 | Content |
| h-auto | 高度自动调整 | Content |








	  AI 思考中...





			** [Tailwind CSS 间距](https://www.runoob.com/tailwindcss-spacing.html)
			[Tailwind CSS 表格](https://www.runoob.com/tailwindcss-table.html) **













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