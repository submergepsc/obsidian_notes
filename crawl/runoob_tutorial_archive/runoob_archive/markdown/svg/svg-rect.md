# SVG

- Source: https://www.runoob.com/svg/svg-rect.html

SVG（可缩放矢量图形）的 `` 元素用于绘制矩形，是 SVG 中常用的基本形状之一，它允许你绘制矩形，并可以通过设置属性来控制矩形的位置、大小、圆角等样式。


### 基本语法


```
<rect
  x="x-coordinate"        <!-- 矩形左上角的 x 坐标 -->
  y="y-coordinate"        <!-- 矩形左上角的 y 坐标 -->
  width="width-value"     <!-- 矩形的宽度 -->
  height="height-value"   <!-- 矩形的高度 -->
  rx="rx-value"           <!-- 矩形的圆角半径（水平方向） -->
  ry="ry-value"           <!-- 矩形的圆角半径（垂直方向） -->
  fill="fill-color"       <!-- 矩形的填充颜色 -->
  stroke="stroke-color"   <!-- 矩形的描边颜色 -->
  stroke-width="width-value" <!-- 矩形的描边宽度 -->
/>
```


**属性解析：**


- `x` 和 `y` 属性指定了矩形左上角的坐标，即矩形的起始点。
- `width` 和 `height` 属性定义了矩形的宽度和高度。
- `rx` 和 `ry` 属性用于指定矩形的圆角半径。如果只设置 `rx`，则所有角的圆角半径都相同；如果同时设置 `rx` 和 `ry`，则可以分别指定水平和垂直方向的圆角半径。
- `fill` 属性定义了矩形的填充颜色。
- `stroke` 属性定义了矩形的描边颜色。
- `stroke-width` 属性定义了矩形的描边宽度。


下面的代码绘制了一个蓝色填充、黑色描边、宽度为 2 像素的矩形，左上角坐标为 (50, 50)，宽度为 100，高度为 80。


```
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect x="50" y="50" width="100" height="80" fill="blue" stroke="black" stroke-width="2" />
</svg>
```


---

### 实例 1


下面是 SVG 代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">

<rect width="300" height="100"

style="fill:rgb(0,0,255);stroke-width:1;stroke:rgb(0,0,0)"/>
</svg>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_rect)


点击查看： [查看 SVG 文件](https://www.runoob.com/try/demo_source/rect1.svg)。


代码解析:**


- rect 元素的 width 和 height 属性可定义矩形的高度和宽度
- style 属性用来定义 CSS 属性
- CSS 的 fill 属性定义矩形的填充颜色（rgb 值、颜色名或者十六进制值）
- CSS 的 stroke-width 属性定义矩形边框的宽度
- CSS 的 stroke 属性定义矩形边框的颜色


### 实例 2


让我们看看另一个例子，它包含一些新的属性：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">

<rect x="50" y="20" width="150" height="150"

style="fill:blue;stroke:pink;stroke-width:5;fill-opacity:0.1;
  stroke-opacity:0.9"/>
</svg>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_rect2)


点击查看： [查看SVG文件](https://www.runoob.com/try/demo_source/rect2.svg)。


代码解析：**


- x 属性定义矩形的左侧位置（例如，x="0" 定义矩形到浏览器窗口左侧的距离是 0px）
- y 属性定义矩形的顶端位置（例如，y="0" 定义矩形到浏览器窗口顶端的距离是 0px）
- CSS 的 fill-opacity 属性定义填充颜色透明度（合法的范围是：0 - 1）
- CSS 的 stroke-opacity 属性定义轮廓颜色的透明度（合法的范围是：0 - 1）


### 实例 3


定义整个元素的不透明度：


下面是SVG代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">

<rect x="50" y="20" width="150" height="150"

style="fill:blue;stroke:pink;stroke-width:5;opacity:0.5"/>
</svg>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_rect3)


对于Opera用户：[查看SVG文件](https://www.runoob.com/try/demo_source/rect2.svg)。


- CSS opacity 属性用于定义了元素的透明值 (范围: 0 到 1)。


---


## 实例 4


最后一个例子，创建一个圆角矩形：


下面是SVG代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">

<rect x="50" y="20" rx="20" ry="20" width="150"
height="150"
  style="fill:red;stroke:black;stroke-width:5;opacity:0.5"/>
</svg>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_rect4)


对于Opera用户：[查看SVG文件](https://www.runoob.com/try/demo_source/rect2.svg)。


- rx 和 ry 属性可使矩形产生圆角。








	  AI 思考中...





			** [SVG 在 HTML 中](https://www.runoob.com/svg-inhtml.html)
			[SVG 圆形](https://www.runoob.com/svg-circle.html) **













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