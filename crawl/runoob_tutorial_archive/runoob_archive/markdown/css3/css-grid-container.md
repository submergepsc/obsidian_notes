# CSS 网格容器

- Source: https://www.runoob.com/css3/css-grid-container.html

![](https://www.runoob.com/wp-content/uploads/2021/10/D2C0E0B9-6910-46C8-819A-AB7EB045552C.jpeg)


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_container)


---


## 网格容器


要使 HTML 元素变成一个网格容器，可以将 **display** 属性设置为 **grid** 或 **inline-grid**。


网格容器内放置着由列和行内组成的网格元素。


### grid-template-columns 属性


grid-template-columns 属性定义了网格布局中的列的数量，它也可以设置每个列的宽度。


属性值是一个以空格分隔的列表，其中每个值定义相对应列的宽度。


如果您希望网格布局包含 4 列，则需要设置 4 列的宽度，如果所有列的宽度都是一样的，可以设置为 **auto**。


以下实例设置了 4 列的网格布局：


## 实例


```css
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto auto;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-template-columns1)


注意：**如果您在 4 列网格中有 4 个以上的网格元素，网格布局会生成新的一行放置该元素。


**grid-template-columns** 属性也可用于指定列的宽度。


## 实例


```css
.grid-container {
  display: grid;
  grid-template-columns: 80px 200px auto 40px;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-template-columns2)


### grid-template-rows 属性


grid-template-rows 属性设置每一行的高度。


属性值是一个以空格分隔的列表，其中每个值定义相对应行的高度：


## 实例


```css
.grid-container {
  display: grid;
  grid-template-rows: 80px 200px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_grid-template-rows)


### justify-content 属性


justify-content 属性用于对齐容器内的网格，设置如何分配顺着弹性容器主轴(或者网格行轴) 的元素之间及其周围的空间。


注意：**网格的总宽度必须小于容器的宽度才能使 justify-content 属性生效。


**
justify-content** 详细内容参考：[CSS justify-content 属性](https://www.runoob.com/../cssref/css3-pr-justify-content.html)


## 实例


```css
.grid-container {
  display: grid;
  justify-content: space-evenly;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_justify-content_space-evenly)


## 实例


```css
.grid-container {
  display: grid;
  justify-content: space-around;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_justify-content_space-around)


## 实例


```css
.grid-container {
  display: grid;
  justify-content: space-between;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_justify-content_space-between)


## 实例


```css
.grid-container {
  display: grid;
  justify-content: center;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_justify-content_center)


## 实例


```css
.grid-container {
  display: grid;
  justify-content: start;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_justify_start)


## 实例


```css
.grid-container {
  display: grid;
  justify-content: end;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_justify_end)


### align-content 属性

**align-content** 属性用于设置垂直方向上的网格元素在容器中的对齐方式。


注意：**网格元素的总高度必须小于容器的高度才能使 align-content 属性生效。


## 实例


```css
.grid-container {
  display: grid;
  height: 400px;
  align-content: center;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_align-content_center)


## 实例


```css
.grid-container {
  display: grid;
  height: 400px;
  align-content: space-evenly;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_align-content_space-evenly)


## 实例


```css
.grid-container {
  display: grid;
  height: 400px;
  align-content: space-around;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_align-content_space-around)


## 实例


```css
.grid-container {
  display: grid;
  height: 400px;
  align-content: space-between;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_align-content_space-between)


## 实例


```css
.grid-container {
  display: grid;
  height: 400px;
  align-content: start;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_align-content_start)


## 实例


```css
.grid-container {
  display: grid;
  height: 400px;
  align-content: end;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_grid_align-content_end)








	  AI 思考中...





			** [CSS 网格布局](https://www.runoob.com/css-grid.html)
			[CSS 网格元素](https://www.runoob.com/css-grid-item.html) **













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