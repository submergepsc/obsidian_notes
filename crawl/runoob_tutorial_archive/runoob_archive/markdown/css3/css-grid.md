# CSS 网格布局

- Source: https://www.runoob.com/css3/css-grid.html

网格是一组相交的水平线和垂直线，它定义了网格的列和行。


CSS 提供了一个基于网格的布局系统，带有行和列，可以让我们更轻松地设计网页，而无需使用浮动和定位。


以下是一个简单的网页布局，使用了网格布局，包含六列和三行：


![](https://www.runoob.com/wp-content/uploads/2021/10/DE5DE2B3-1C7A-42B4-AD5F-07211CC54D75.jpeg)


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid3)


---


## 浏览器支持


目前最新的一些浏览器版本都支持网格布局。


|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 57.0 | 16.0 | 52.0 | 10 | 44 |


---


## 网格元素


网格布局由一个父元素及一个或多个子元素组成。


## 实例


```css
<div class="grid-container">
  <div class="grid-item">1</div>
  <div class="grid-item">2</div>
  <div class="grid-item">3</div>
  <div class="grid-item">4</div>
  <div class="grid-item">5</div>
  <div class="grid-item">6</div>
  <div class="grid-item">7</div>
  <div class="grid-item">8</div>
  <div class="grid-item">9</div>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_layout_grid)


---


## display 属性

当一个 HTML 元素将 display 属性设置为 grid 或 inline-grid 后，它就变成了一个网格容器，这个元素的所有直系子元素将成为网格元素。


## 实例


```css
.grid-container {
  display: grid;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_layout_grid2)


## 实例


```css
.grid-container {
  display: inline-grid;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_layout_grid3)


---

## 网格轨道


我们通过 **grid-template-columns** 和 **grid-template-rows** 属性来定义网格中的列和行。


这些属性定义了网格的轨道，一个网格轨道就是网格中任意两条线之间的空间。


在下图中你可以看到一个绿色框的轨道——网格的第一个行轨道。第二行有三个白色框轨道。


![](https://www.runoob.com/wp-content/uploads/2021/10/1_Grid_Track.png)


以下实例我们使用 **grid-template-columns** 属性在网格容器中创建四个列:


## 实例


```css
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto auto;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid-template-columns)


以下实例我们使用 **grid-template-rows** 属性在网格容器中设置行的高度:


## 实例


```css
.grid-container {
  display: grid;
  grid-template-rows: 100px 300px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid-template-rows)


### fr 单位


轨道可以使用任何长度单位进行定义。


网格引入了 **fr** 单位来帮助我们创建灵活的网格轨道。一个 fr 单位代表网格容器中可用空间的一等份。


以下实例定义了一个网格定义将创建三个相等宽度的轨道，这些轨道会随着可用空间增长和收缩。


## 实例


```css
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid-template-rows-fr)


### 网格单元

一个网格单元是在一个网格元素中最小的单位， 从概念上来讲其实它和表格的一个单元格很像。现在再看回我们前面的一个例子, 一旦一个网格元素被定义在一个父级元素当中，那么他的子级元素将会排列在每个事先定义好的网格单元中。在下面的图中，我会将第一个网格单元作高亮处理。


![](https://www.runoob.com/wp-content/uploads/2021/10/1_Grid_Cell.png)


### 网格区域


网格元素可以向行或着列的方向扩展一个或多个单元，并且会创建一个网格区域。网格区域的形状应该是一个矩形 - 也就是说你不可能创建出一个类似于"L"形的网格区域。下图高亮的网格区域扩展了2列以及2行。

![](https://www.runoob.com/wp-content/uploads/2021/10/1_Grid_Area.png)


---


## 网格列

网格元素的垂直线方向称为列（Column）。


![](https://www.runoob.com/wp-content/uploads/2021/10/grid_columns.png)


---


## 网格行

网格元素的水平线方向称为行（Row）。


![](https://www.runoob.com/wp-content/uploads/2021/10/grid_rows.png)


---


## 网格间距


网格间距（Column Gap）指的是两个网格单元之间的网格横向间距或网格纵向间距。


![](https://www.runoob.com/wp-content/uploads/2021/10/grid_gaps.png)


您可以使用以下属性来调整间隙大小：


- grid-column-gap
- grid-row-gap
- grid-gap


以下实例使用 **grid-column-gap** 属性来设置列之间的网格间距：


## 实例


```css
.grid-container {
  display: grid;
  grid-column-gap: 50px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-column-gap)


以下实例使用 **grid-row-gap** 属性来设置行之间的网格间距：


## 实例


```css
.grid-container {
  display: grid;
  grid-row-gap: 50px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-row-gap)


**grid-gap** 属性是 grid-row-gap 和 the grid-column-gap 属性的简写:


## 实例


```css
.grid-container {
  display: grid;
  grid-gap: 50px 100px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-gap2)


**grid-gap** 属性可以同时设置行间距和列间距:


## 实例


```css
.grid-container {
  display: grid;
  grid-gap: 50px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-gap)


---

## 网格线

列与列，行与行之间的交接处就是网格线。

Grid 会为我们创建编号的网格线来让我们来定位每一个网格元素。

例如下面这个三列两行的网格中，就拥有四条纵向的网格线（灰色圆圈标记），以及三条横向的网格线（黑色圆圈标记）。


![](https://www.runoob.com/wp-content/uploads/2021/10/1_diagram_numbered_grid_lines.png)


网格元素设置时可以参考这些行号。


下图则定义了四条纵向的网格线，以及四条横向的网格线：


![](https://www.runoob.com/wp-content/uploads/2021/10/grid_lines.png)


网格线的编号顺序取决于文章的书写模式。在从左至右书写的语言中，编号为 1 的网格线位于最左边。在从右至左书写的语言中，编号为 1 的网格线位于最右边。


接下来我使用了 grid-column-start, grid-column-end, grid-row-start 和 grid-row-end 属性来演示如何使用网格线。


以下实例我们设置一个网格元素的网格线从第一列开始，第三列结束：


## 实例


```css
.item1 {
  grid-column-start: 1;
  grid-column-end: 3;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_lines)


以下实例我们设置一个网格元素的网格线从第一行开始，第三行结束：


## 实例


```css
.item1 {
  grid-row-start: 1;
  grid-row-end: 3;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_lines2)


---


## CSS 网格属性


| 属性 | 描述 |
| --- | --- |
| column-gap | 指定列之间的间隙 |
| gap | row-gap 和 column-gap 的简写属性 |
| grid | grid-template-rows, grid-template-columns, grid-template-areas, grid-auto-rows, grid-auto-columns, 以及 grid-auto-flow 的简写属性 |
| grid-area | 指定网格元素的名称，或者也可以是 grid-row-start, grid-column-start, grid-row-end, 和 grid-column-end 的简写属性 |
| grid-auto-columns | 指的默认的列尺寸 |
| grid-auto-flow | 指定自动布局算法怎样运作，精确指定在网格中被自动布局的元素怎样排列。 |
| grid-auto-rows | 指的默认的行尺寸 |
| grid-column | grid-column-start 和 grid-column-end 的简写属性 |
| grid-column-end | 指定网格元素列的结束位置 |
| grid-column-gap | 指定网格元素的间距大小 |
| grid-column-start | 指定网格元素列的开始位置 |
| grid-gap | grid-row-gap 和 grid-column-gap 的简写属性 |
| grid-row | grid-row-start 和 grid-row-end 的简写属性 |
| grid-row-end | 指定网格元素行的结束位置 |
| grid-row-gap | 指定网格元素的行间距 |
| grid-row-start | 指定网格元素行的开始位置 |
| grid-template | grid-template-rows, grid-template-columns 和 grid-areas 的简写属性 |
| grid-template-areas | 指定如何显示行和列，使用命名的网格元素 |
| grid-template-columns | 指定列的大小，以及网格布局中设置列的数量 |
| grid-template-rows | 指定网格布局中行的大小 |
| row-gap | 指定两个行之间的间距 |


> 接下来我们可以通过 [**CSS 网格布局小游戏**](https://www.runoob.com/try/gridgarden/index.html)来检验我们的学习成果。










	  AI 思考中...





			** [CSS3 rotation-point](https://www.runoob.com/css3-pr-rotation-point.html)
			[CSS 网格容器](https://www.runoob.com/css-grid-container.html) **













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