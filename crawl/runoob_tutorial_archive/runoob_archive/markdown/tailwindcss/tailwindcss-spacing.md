# Tailwind CSS 间距

- Source: https://www.runoob.com/tailwindcss/tailwindcss-spacing.html

Tailwind CSS 中，间距（Spacing）是布局的重要组成部分。


间距指的是元素之间的距离，包括内边距（Padding）、外边距（Margin）、行间距（Line-Height）、字间距（Letter-Spacing）等。

Tailwind CSS 提供了一些常用的工具类，使得这些间距的设置变得更加简便且直观。


---


## 外边距（Margin）

外边距用于控制元素与其他元素之间的距离。Tailwind 提供了简洁的工具类来设置外边距，常用的格式为 `m-{size}`，其中 `m` 表示外边距，`{size}` 为具体的值。

- `m-{size}`: 设置四个方向的外边距。
- `mt-{size}`: 设置上外边距（margin-top）。
- `mr-{size}`: 设置右外边距（margin-right）。
- `mb-{size}`: 设置下外边距（margin-bottom）。
- `ml-{size}`: 设置左外边距（margin-left）。
- `mx-{size}`: 设置水平外边距（左右外边距）。
- `my-{size}`: 设置垂直外边距（上下外边距）。


常见的外边距值:

- `m-0`: 设置外边距为 0。
- `m-1` 到 `m-64`: 设置不同大小的外边距，默认是根据 `rem` 单位来设置的。
- `m-px`: 设置外边距为 1px。
- `m-auto`: 设置外边距为自动，常用于居中对齐。

使用 `mt-*`、`mr-*`、`mb-*` 和 `ml-*` 工具类来控制元素某一侧的外边距。

例如，`mt-6` 会在元素的顶部添加 1.5rem 的外边距，`mr-4` 会在元素的右侧添加 1rem 的外边距，`mb-8` 会在元素的底部添加 2rem 的外边距，而 `ml-2` 会在元素的左侧添加 0.5rem 的外边距。


## 实例


```css
<div class="mt-6 ...">mt-6</div>
<div class="mr-4 ...">mr-4</div>
<div class="mb-8 ...">mb-8</div>
<div class="ml-2 ...">ml-2</div>
```

**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_spacing1)
在这个例子中，`mt-6` 设置了元素顶部的外边距，`mr-4` 设置了右侧外边距，`mb-8` 设置了底部外边距，`ml-2` 设置了左侧外边距。


使用 **mx-*** 实用工具来控制一个元素的水平外边距。


```
<div class="mx-8 ...">mx-8</div>
```


使用 **my-*** 实用工具来控制一个元素的垂直外边距。


```
<div class="my-8 ...">my-8</div>
```


使用 **m-*** 实用工具来控制一个元素所有边的外边距。


```
<div class="m-8 ...">m-8</div>
```


---


## 内边距（Padding）

内边距用于控制元素内容与边框之间的距离。

与外边距一样，Tailwind 也为内边距提供了丰富的工具类。


- `p-{size}`: 设置四个方向的内边距。
- `pt-{size}`: 设置上内边距（padding-top）。
- `pr-{size}`: 设置右内边距（padding-right）。
- `pb-{size}`: 设置下内边距（padding-bottom）。
- `pl-{size}`: 设置左内边距（padding-left）。
- `px-{size}`: 设置水平内边距（左右内边距）。
- `py-{size}`: 设置垂直内边距（上下内边距）。

- `p-0`: 设置内边距为 0。
- `p-1` 到 `p-64`: 设置不同大小的内边距。
- `p-px`: 设置内边距为 1px。


## 实例


```css
<div class="pt-6 ...">pt-6</div>
<div class="pr-4 ...">pr-4</div>
<div class="pb-8 ...">pb-8</div>
<div class="pl-2 ...">pl-2</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_spacing2)


使用 **px-*** 实用工具来控制一个元素的水平内边距。


```
<div class="px-8 ...">px-8</div>
```


使用 **py-*** 实用工具来控制一个元素的垂直内边距。


```
<div class="py-8 ...">py-8</div>
```


使用 **p-*** 实用工具来控制一个元素所有边的内边距。


```
<div class="p-8 ...">p-8</div>
```


使用 **ps-*** 和 **pe-*** 实用工具来设置 padding-inline-start 和 padding-inline-end 逻辑属性，这些属性根据文本方向映射到左侧或右侧。


## 实例


```css
<div dir="ltr">
  <div class="ps-8 ...">ps-8</div>
  <div class="pe-8 ...">pe-8</div>
</div>

<div dir="rtl">
  <div class="ps-8 ...">ps-8</div>
  <div class="pe-8 ...">pe-8</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_spacing3)

---


## 行间距（Line Height）

行间距控制文本行之间的垂直间距。

Tailwind 提供了 leading-{size} 工具类来调整行间距。


常见的行间距值:


- `leading-none`: 设置行间距为 1（无间距）。
- `leading-tight`: 设置行间距为更紧凑的值。
- `leading-snug`, `leading-normal`, `leading-loose`: 提供不同的行间距值。
- `leading-{size}`: 使用指定的单位设置精确的行间距。


## 实例


```css
<p class="leading-tight">这是紧凑的文本。</p>
<p class="leading-loose">这是较松散的文本。</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_spacing4)

---


## 字间距（Letter Spacing）

字间距控制文本字符之间的水平间距。

Tailwind 使用 tracking-{size} 工具类来调整字间距。


常见的字间距值:

- `tracking-tight`: 缩小字间距。
- `tracking-normal`: 设置正常的字间距。
- `tracking-wide`: 增大字间距。
- `tracking-{size}`: 使用指定的单位设置字间距。


## 实例


```css
<p class="tracking-tight">紧凑的文本</p>
<p class="tracking-wide">宽松的文本</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_spacing5)
---


## 空间（Gap）

gap 用于设置网格布局（Grid）或 Flexbox 布局中的元素间距。

它会在所有的子元素之间添加间距，尤其适用于在布局中创建一致的间隔。


常见的 gap 值:


- `gap-0`: 设置间距为 0。
- `gap-1` 到 `gap-64`: 设置不同的间距值。


## 实例


```css
<div class="grid gap-4 grid-cols-2">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_spacing6)








	  AI 思考中...





			** [Tailwind CSS Flexbox 和 Grid 布局](https://www.runoob.com/tailwindcss-flexbox-and-grid.html)
			[Tailwind CSS 尺寸控制](https://www.runoob.com/tailwindcss-sizing.html) **













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