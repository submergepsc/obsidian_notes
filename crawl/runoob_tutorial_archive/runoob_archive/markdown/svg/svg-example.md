# SVG 基本语法

- Source: https://www.runoob.com/svg/svg-example.html

SVG 文档由一个或多个 SVG 元素组成，它们定义了图形的内容和属性。


```
<svg
  width="200"     <!-- 指定SVG画布的宽度 -->
  height="200"    <!-- 指定SVG画布的高度 -->
  xmlns="http://www.w3.org/2000/svg">   <!-- 指定SVG命名空间 -->
  <!-- SVG图形内容 -->
</svg>
```


- `width` 和 `height` 属性定义了SVG画布的宽度和高度。
- `xmlns` 属性指定 SVG 文档的 XML 命名空间。


**SVG 的基本语法：**


- SVG文档以 `` 标签开始，以 `` 标签结束。
- SVG元素使用标签来描述不同的图形，例如 `` 表示圆形，`` 表示矩形等。
- SVG元素可以包含属性，用于指定图形的各种特性，如位置、大小、颜色等。


**绘制基本图形：**

SVG 提供了一系列的图形元素来绘制各种形状的图形，如矩形、圆形、直线、多边形等。


- ``：绘制矩形
- ``：绘制圆形
- ``：绘制椭圆
- ``：绘制直线
- `
`：绘制折线 - ``：绘制多边形 - ``：绘制路径 **矩形（Rectangles）：**使用  元素绘制矩形，可以指定矩形的位置、大小、圆角等属性。


```
<rect x="50" y="50" width="100" height="50" rx="10" ry="10" fill="blue" />
```


**圆形（Circles）：**使用  元素绘制圆形，可以指定圆心坐标和半径。


```
<circle cx="100" cy="100" r="50" fill="red" />
```


**椭圆（Ellipses）：**使用  元素绘制椭圆，可以指定椭圆的中心坐标和长短轴的半径。


```
<ellipse cx="100" cy="100" rx="80" ry="50" fill="green" />
```


**直线（Lines）：**使用  元素绘制直线，需要指定起点和终点坐标。


```
<line x1="50" y1="50" x2="150" y2="150" stroke="black" stroke-width="2" />
```


**多边形（Polygons）：**使用  元素绘制多边形，需要指定多个顶点的坐标。


```
<polygon points="100,50 150,150 50,150" fill="orange" />
```


**折线（Polylines）：**使用  元素绘制折线，需要指定多个点的坐标。


```
<polyline points="100,50 150,150 50,150" fill="none" stroke="blue" stroke-width="2" />
```


**路径（Paths）：**使用  元素绘制路径，可以通过指定一系列的路径命令来绘制各种形状。


```
<path d="M10 10 L90 10 L90 90 Z" fill="none" stroke="black" stroke-width="2" />
```


**渐变和填充：**


- 使用 `` 或 `` 定义渐变。
- 使用 `fill` 和 `stroke` 属性指定填充和描边样式。


**文本和字体：**


- 使用 `` 元素插入文本。
- 使用 `font-family`、`font-size` 等属性控制文本样式。


动画和交互：


- 使用CSS或JavaScript创建动画效果。
- 添加事件处理器实现交互功能，如鼠标点击、悬停等。


**SVG 元素属性：**

SVG元素可以具有各种属性，用于指定图形的位置、大小、颜色等特性。


```
<circle
  cx="100"       <!-- 圆心的x坐标 -->
  cy="100"       <!-- 圆心的y坐标 -->
  r="50"         <!-- 圆的半径 -->
  fill="red"     <!-- 填充颜色 -->
  stroke="black" <!-- 描边颜色 -->
  stroke-width="2" <!-- 描边宽度 -->
/>
```


- `cx` 和 `cy` 属性定义了圆心的x和y坐标。
- `r` 属性定义了圆的半径。
- `fill` 属性定义了填充颜色。
- `stroke` 属性定义了描边颜色。
- `stroke-width` 属性定义了描边宽度。


**嵌套和分组：**

SVG 元素可以嵌套和分组，以便更好地组织和管理图形元素。


```
<g id="group1">   <!-- 定义一个分组 -->
  <!-- 分组内的图形元素 -->
  <rect x="10" y="10" width="50" height="50" />
  <circle cx="100" cy="100" r="30" />
</g>
```


- `` 元素用于创建一个分组。
- `id` 属性用于为分组指定一个唯一的标识符。


---


## 简单的 SVG 实例


SVG 文件推荐使用 **.svg**（全部小写）作为此类文件的扩展名。


1、以下是一个简单的 SVG 文件示例，创建一个包含一个圆形的 SVG 图像：


## test.svg 文件


```svg
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="100" r="80" fill="blue" />
</svg>
```


这段代码描述了一个 SVG 画布，宽度为 200 个单位，高度也为 200 个单位。在画布上绘制了一个圆形，圆心坐标为(100, 100)，半径为80个单位，填充颜色为蓝色。


预览效果：


![](https://www.runoob.com/wp-content/uploads/2024/04/aa53148fd36c78446804395198799706.png)


2、另一个简单的 SVG 图形例子：


## test.svg 文件


```svg
<svg version="1.1"
   baseProfile="full"
   width="300" height="200"
   xmlns="http://www.w3.org/2000/svg">

  <rect width="100%" height="100%" stroke="red" stroke-width="4" fill="yellow" />

  <circle cx="150" cy="100" r="80" fill="green" />

  <text x="150" y="115" font-size="16" text-anchor="middle" fill="white">RUNOOB SVG TEST</text>

</svg>
```

**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_myfirst1)

显示结果如下：






  RUNOOB SVG TEST


SVG 代码解析：**


- ``：这是SVG文档的开始标签，指定了SVG的版本、基本配置（full），以及画布的宽度和高度。xmlns属性定义了SVG文档的XML命名空间。
- ``：这是一个矩形元素，使用``标签表示。它的宽度和高度都设置为画布的宽度和高度（100%），stroke属性指定了矩形的边框颜色为红色，stroke-width属性设置了边框的宽度为4个单位，fill属性指定了矩形的填充颜色为黄色。
- ``：这是一个圆形元素，使用``标签表示。它的圆心坐标(cx, cy)分别为(150, 100)，半径r为80个单位，fill属性指定了圆形的填充颜色为绿色。
- `RUNOOB SVG TEST`：这是一个文本元素，使用``标签表示。它的起始坐标(x, y)为(150, 115)，font-size属性设置了字体大小为16个单位，text-anchor属性设置了文本的水平对齐方式为居中，fill属性指定了文本的颜色为白色。文本内容为"RUNOOB SVG TEST"。
- ``：这是SVG文档的结束标签，标志着SVG文档的结束。








	  AI 思考中...





			** [SVG 简介](https://www.runoob.com/svg-intro.html)
			[SVG 在 HTML 中](https://www.runoob.com/svg-inhtml.html) **













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