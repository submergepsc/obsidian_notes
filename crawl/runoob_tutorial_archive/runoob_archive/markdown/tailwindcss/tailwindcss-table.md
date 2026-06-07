# Tailwind CSS 表格

- Source: https://www.runoob.com/tailwindcss/tailwindcss-table.html

Tailwind CSS 提供了一套方便的工具类，用于创建和自定义表格。

通过这些工具类，你可以轻松地对表格进行样式控制，包括边框、间距、对齐方式、字体样式等。

接下来，我们将详细介绍如何使用 Tailwind CSS 来创建和自定义表格。


---


## 基础表格样式


Tailwind CSS 提供了一些基础类，用于控制表格的外观和布局。常用的工具类包括 table-auto 和 table-fixed，这两个类用来设置表格的布局。


- `table-auto`：默认布局，表格的列宽由内容自动决定。
- `table-fixed`：表格列宽固定。所有列的宽度都会根据表格的总宽度平分，适用于具有统一列宽的表格。


使用 table-auto 允许表格自动调整列宽以适应单元格内容。


## 实例


```css
<table class="table-auto">
  <thead>
    <tr>
      <th>Song</th>
      <th>Artist</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>The Sliding Mr. Bones (Next Stop, Pottersville)</td>
      <td>Malcolm Lockyer</td>
      <td>1961</td>
    </tr>
    <tr>
      <td>Witchy Woman</td>
      <td>The Eagles</td>
      <td>1972</td>
    </tr>
    <tr>
      <td>Shining Star</td>
      <td>Earth, Wind, and Fire</td>
      <td>1975</td>
    </tr>
  </tbody>
</table>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_table1)


使用 table-fixed 允许表格忽略内容，对列使用固定宽度。第一行的宽度将为整个表格设置列宽。


## 实例


```css
<table class="table-fixed">
  <thead>
    <tr>
      <th>Song</th>
      <th>Artist</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>The Sliding Mr. Bones (Next Stop, Pottersville)</td>
      <td>Malcolm Lockyer</td>
      <td>1961</td>
    </tr>
    <tr>
      <td>Witchy Woman</td>
      <td>The Eagles</td>
      <td>1972</td>
    </tr>
    <tr>
      <td>Shining Star</td>
      <td>Earth, Wind, and Fire</td>
      <td>1975</td>
    </tr>
  </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_table2)


---


## 边框和间距

Tailwind 提供了许多工具类来控制表格的边框、内外边距以及其他布局细节。


你可以使用 border, border-collapse, border-spacing 等类来控制表格的边框样式。


- `border`：为表格添加边框。
- `border-collapse`：控制表格单元格的边框是否合并。
- `border-spacing`：设置单元格之间的间距。


## 实例


```css
<table class="table-auto border-collapse w-full">
  <thead>
    <tr>
      <th class="border px-4 py-2">Header 1</th>
      <th class="border px-4 py-2">Header 2</th>
      <th class="border px-4 py-2">Header 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border px-4 py-2">Row 1, Col 1</td>
      <td class="border px-4 py-2">Row 1, Col 2</td>
      <td class="border px-4 py-2">Row 1, Col 3</td>
    </tr>
    <tr>
      <td class="border px-4 py-2">Row 2, Col 1</td>
      <td class="border px-4 py-2">Row 2, Col 2</td>
      <td class="border px-4 py-2">Row 2, Col 3</td>
    </tr>
  </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_table3)

### 内外边距

你可以使用 px-*, py-* 类来设置表格单元格的 内边距，以及 m-* 和 p-* 类来设置表格的外边距。


## 实例


```css
<!-- 设置表格单元格内边距 -->
<table class="table-auto w-full border-collapse">
  <thead>
    <tr>
      <th class="border px-6 py-4">Header 1</th>
      <th class="border px-6 py-4">Header 2</th>
      <th class="border px-6 py-4">Header 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border px-6 py-4">Row 1, Col 1</td>
      <td class="border px-6 py-4">Row 1, Col 2</td>
      <td class="border px-6 py-4">Row 1, Col 3</td>
    </tr>
  </tbody>
</table>

<!-- 设置表格外边距 -->
<table class="table-auto w-full border-collapse mt-8">
  <thead>
    <tr>
      <th class="border px-4 py-2">Header 1</th>
      <th class="border px-4 py-2">Header 2</th>
      <th class="border px-4 py-2">Header 3</th>
    </tr>
  </thead>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_table4)

---


## 对齐和文字样式

Tailwind 提供了一些类来控制表格单元格内容的对齐和字体样式，如：

- `text-left`, `text-center`, `text-right`：控制文本对齐。
- `font-semibold`, `font-bold`：控制字体粗细。
- `uppercase`, `lowercase`, `capitalize`：控制文本的大小写。


## 实例


```css
<!-- 设置文字居中对齐 -->
<table class="table-auto border-collapse w-full">
  <thead>
    <tr>
      <th class="border px-4 py-2 text-center font-bold">Header 1</th>
      <th class="border px-4 py-2 text-center font-bold">Header 2</th>
      <th class="border px-4 py-2 text-center font-bold">Header 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border px-4 py-2 text-center">Row 1, Col 1</td>
      <td class="border px-4 py-2 text-center">Row 1, Col 2</td>
      <td class="border px-4 py-2 text-center">Row 1, Col 3</td>
    </tr>
  </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_table5)

---


## 合并单元格

Tailwind CSS 支持通过 HTML 属性来设置 合并单元格，如 **colspan** 和 **rowspan**。


## 实例


```css
<!-- 合并列 -->
<table class="table-auto w-full border-collapse">
  <thead>
    <tr>
      <th class="border px-4 py-2" colspan="2">Header 1 & 2</th>
      <th class="border px-4 py-2">Header 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border px-4 py-2" colspan="2">Row 1, Col 1 & 2</td>
      <td class="border px-4 py-2">Row 1, Col 3</td>
    </tr>
  </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_table6)

---

## 响应式表格

你还可以使用 Tailwind CSS 的响应式设计类，来在不同屏幕尺寸下控制表格的布局。

例如，使用 sm:, md:, lg: 前缀来设置不同屏幕下的显示方式。


## 实例


```css
<!-- 在小屏幕下隐藏列 -->
<table class="table-auto w-full border-collapse">
  <thead>
    <tr>
      <th class="border px-4 py-2">Header 1</th>
      <th class="border px-4 py-2 hidden md:table-cell">Header 2</th>
      <th class="border px-4 py-2">Header 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border px-4 py-2">Row 1, Col 1</td>
      <td class="border px-4 py-2 hidden md:table-cell">Row 1, Col 2</td>
      <td class="border px-4 py-2">Row 1, Col 3</td>
    </tr>
  </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_table7)

---


## 表格标题

使用 **caption-top** 将标题元素定位在表格的顶部。


## 实例


```css
<table>
  <caption class="caption-top">
    Table 3.1: Professional wrestlers and their signature moves.
  </caption>
  <thead>
    <tr>
      <th>Wrestler</th>
      <th>Signature Move(s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Stone Cold" Steve Austin</td>
      <td>Stone Cold Stunner, Lou Thesz Press</td>
    </tr>
    <tr>
      <td>Bret "The Hitman" Hart</td>
      <td >The Sharpshooter</td>
    </tr>
    <tr>
      <td>Razor Ramon</td>
      <td>Razor's Edge, Fallaway Slam</td>
    </tr>
  </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_table8)


使用 **caption-bottom** 将标题元素定位在表格的底部。


## 实例


```css
<table>
  <caption class="caption-bottom">
    Table 3.1: Professional wrestlers and their signature moves.
  </caption>
  <thead>
    <tr>
      <th>Wrestler</th>
      <th>Signature Move(s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Stone Cold" Steve Austin</td>
      <td>Stone Cold Stunner, Lou Thesz Press</td>
    </tr>
    <tr>
      <td>Bret "The Hitman" Hart</td>
      <td >The Sharpshooter</td>
    </tr>
    <tr>
      <td>Razor Ramon</td>
      <td>Razor's Edge, Fallaway Slam</td>
    </tr>
  </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_table9)








	  AI 思考中...





			** [Tailwind CSS 尺寸控制](https://www.runoob.com/tailwindcss-sizing.html)
			[Tailwind CSS 排版](https://www.runoob.com/tailwindcss-typography.html) **













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