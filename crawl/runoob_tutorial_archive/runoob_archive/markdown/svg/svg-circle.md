# SVG 圆形

- Source: https://www.runoob.com/svg/svg-circle.html

SVG 中的 `` 元素用于绘制圆形，它是SVG中常用的基本形状之一。

使用 `` 元素可以创建圆形的图形，并可以通过设置属性来控制圆形的位置、大小和样式。


### 基本语法


```
<circle
  cx="x-coordinate"      <!-- 圆心的 x 坐标 -->
  cy="y-coordinate"      <!-- 圆心的 y 坐标 -->
  r="radius"             <!-- 圆的半径 -->
  fill="fill-color"      <!-- 圆的填充颜色 -->
  stroke="stroke-color"  <!-- 圆的描边颜色 -->
  stroke-width="width"   <!-- 圆的描边宽度 -->
/>
```


**属性解析：**

- `cx` 和 `cy` 属性定义了圆心的坐标，即圆的中心点的位置。
- `r` 属性定义了圆的半径，以确定圆的大小。
- `fill` 属性定义了圆的填充颜色。
- `stroke` 属性定义了圆的描边颜色。
- `stroke-width` 属性定义了圆的描边宽度。

以下代码绘制了一个蓝色填充、黑色描边、半径为 50 像素的圆形，圆心坐标为 (100, 100)。


```
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="100" r="50" fill="blue" stroke="black" stroke-width="2" />
</svg>
```


### 实例


下面是 SVG 代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">

<circle cx="100" cy="50" r="40" stroke="black"

stroke-width="2" fill="red"/>
</svg>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_circle)

点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/circle1.svg)。


代码解析：**


- cx 和 cy 属性定义圆点的 x 和 y 坐标。如果省略 cx 和 cy，圆的中心会被设置为 (0, 0)
- r 属性定义圆的半径








	  AI 思考中...





			** [SVG 矩形](https://www.runoob.com/svg-rect.html)
			[SVG 椭圆](https://www.runoob.com/svg-ellipse.html) **













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