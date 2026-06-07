# CSS 网格元素

- Source: https://www.runoob.com/css3/css-grid-item.html

![](https://www.runoob.com/wp-content/uploads/2021/10/CFCBEAF6-D02D-459F-87E7-94DED0ECF9BF.jpeg)


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_item)


---


## CSS 网格元素


网格容器包含了一个或多个网格元素。


默认情况下，网格容器的每一列和每一行都有一个网格元素，我们也可以设置网格元素跨越多个列或行，行和列为行号。


### grid-column 属性

grid-column 属性定义了网格元素列的开始和结束位置。


**注意：** grid-column 是 grid-column-start 和 grid-column-end 属性的简写属性。


我们可以参考行号来设置网格元素，也可以使用关键字 "span" 来定义元素将跨越的列数。


以下实例设置 "item1" 在第 1 列开始，在第 5 列前结束：


## 实例


```css
.item1 {
  grid-column: 1 / 5;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-column_line)


以下实例设置 "item1" 跨越 3 列：


## 实例


```css
.item1 {
  grid-column: 1 / span 3;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-column)


以下实例设置 "item2" 跨越 3 列：


## 实例


```css
.item2 {
  grid-column: 2 / span 3;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-column2)


### grid-row 属性


grid-row 属性定义了网格元素行的开始和结束位置。


注意：** grid-row 是 grid-row-start 和 grid-row-end 属性的简写属性。


我们可以参考行号来设置网格元素，也可以使用关键字 "span" 来定义元素将跨越的行数。


以下实例设置 "item1" 在第 1 行开始，在第 4 行前结束：


## 实例


```css
.item1 {
  grid-row: 1 / 4;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-row)


以下实例设置 "item1" 跨越两行：


## 实例


```css
.item1 {
  grid-row: 1 / span 2;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-row2)


### grid-area 属性


grid-area 属性是 grid-row-start, grid-column-start, grid-row-end 以及 grid-column-end 属性的简写。


以下实例设置 "item8" 从第 1 行开始和第 2 列开始， 第 5 行和第 6 列结束。


## 实例


```css
.item8 {
  grid-area: 1 / 2 / 5 / 6;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-area1)


以下实例设置 "item8" 从第 2 行开始和第 1 列开始， 横跨 2 行 3 列。


## 实例


```css
.item8 {
  grid-area: 2 / 1 / span 2 / span 3;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-area2)


---


## 网格元素命名 grid-area 属性可以对网格元素进行命名。 命名的网格元素可以通过容器的 grid-template-areas 属性来引用。 以下实例 item1 命名为 "myArea", 并跨越五列： 实例


```css
.item1 {
  grid-area: myArea;
}
.grid-container {
  grid-template-areas: 'myArea myArea myArea myArea myArea';
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-area_named)


每行由单引号内 **' '** 定义，以空格分隔。


**.** 号表示没有名称的网格项。


## 实例


```css
.item1 {
  grid-area: myArea;
}
.grid-container {
  grid-template-areas: 'myArea myArea . . .';
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-area_named1)


要定义两行，请在另一组单引号内 **' '** 定义第二行的列。


以下实例设置 "item1" 跨越 2 行 2 列:


## 实例


```css
.item1 {
  grid-area: myArea;
}
.grid-container {
  grid-template-areas: 'myArea myArea . . .';
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-area_named2)


命名所有网格元素，并制作一个网页模板：


## 实例


```css
.item1 { grid-area: header; }
.item2 { grid-area: menu; }
.item3 { grid-area: main; }
.item4 { grid-area: right; }
.item5 { grid-area: footer; }

.grid-container {
  grid-template-areas:
    'header header header header header header'
    'menu main main main right right'
    'menu footer footer footer footer footer';
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-area_named3)


### 网格元素的顺序

网格布局允许我们将网格元素放置在我们喜欢的任何地方。


HTML 代码中的第一元素不一定非要显示为网格中元素的第一项。


## 实例


```css
.item1 { grid-area: 1 / 3 / 2 / 4; }
.item2 { grid-area: 2 / 3 / 3 / 4; }
.item3 { grid-area: 1 / 1 / 2 / 2; }
.item4 { grid-area: 1 / 2 / 2 / 3; }
.item5 { grid-area: 2 / 1 / 3 / 2; }
.item6 { grid-area: 2 / 2 / 3 / 3; }
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_flexible_order)


您可以使用媒体查询，重新排列在指定屏幕尺寸下的顺序：


## 实例


```css
@media only screen and (max-width: 500px) {
  .item1 { grid-area: 1 / span 3 / 2 / 4; }
  .item2 { grid-area: 3 / 3 / 4 / 4; }
  .item3 { grid-area: 2 / 1 / 3 / 2; }
  .item4 { grid-area: 2 / 2 / span 2 / 3; }
  .item5 { grid-area: 3 / 1 / 4 / 2; }
  .item6 { grid-area: 2 / 3 / 3 / 4; }
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_flexible_order2)








	  AI 思考中...





			** [CSS 网格容器](https://www.runoob.com/css-grid-container.html)














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