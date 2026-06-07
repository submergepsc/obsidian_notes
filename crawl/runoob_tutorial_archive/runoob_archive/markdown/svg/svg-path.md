# SVG 路径

- Source: https://www.runoob.com/svg/svg-path.html

SVG 中的 `` 元素用于创建路径，它是 SVG 中最强大和最灵活的基本形状之一。

使用 `` 元素可以绘制直线、曲线、弧线等各种复杂的图形，并且可以通过设置路径命令来控制路径的形状和样式。


### 基本语法


```
<path
  d="path-data"            <!-- 定义路径的路径数据 -->
  fill="fill-color"        <!-- 路径的填充颜色 -->
  stroke="stroke-color"    <!-- 路径的描边颜色 -->
  stroke-width="width"     <!-- 路径的描边宽度 -->
/>
```


**属性解析：**


- `d` 属性定义了路径的路径数据，即路径命令序列。路径数据由一系列的路径命令组成，每个路径命令以字母开头，后面跟随一组数字参数。常用的路径命令包括：M（移动到）、L（直线到）、H（水平线到）、V（垂直线到）、C（三次贝塞尔曲线）、S（光滑曲线）、Q（二次贝塞尔曲线）、T（光滑二次贝塞尔曲线）、A（圆弧）、Z（闭合路径）等。
- `fill` 属性定义了路径的填充颜色。
- `stroke` 属性定义了路径的描边颜色。
- `stroke-width` 属性定义了路径的描边宽度。

以下代码绘制了一个橙色填充、黑色描边、宽度为 2 像素的路径，其路径数据为移动到 (50, 50)，然后依次连接到 (150, 50) 和 (100, 150)，最后闭合路径。


```
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <path d="M 50 50 L 150 50 L 100 150 Z" fill="orange" stroke="black" stroke-width="2" />
</svg>
```


### 实例 1


下面的例子定义了一条路径，它开始于位置 150 0，到达位置 75 200，然后从那里开始到 225 200，最后在 150 0 关闭路径。


*


下面是SVG代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    <path d="M150 0 L75 200 L225 200 Z" />
</svg>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_path)


点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/path1.svg)。 ### 实例 2 下面的例子创建了一个二次方贝塞尔曲线，A 和 C 分别是起点和终点，B 是控制点：


下面是SVG代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
  <path id="lineAB" d="M 100 350 l 150 -300" stroke="red"
  stroke-width="3" fill="none" />
  <path id="lineBC" d="M 250 50 l 150 300" stroke="red"
  stroke-width="3" fill="none" />
  <path d="M 175 200 l 150 0" stroke="green" stroke-width="3"
  fill="none" />
  <path d="M 100 350 q 150 -300 300 0" stroke="blue"
  stroke-width="5" fill="none" />
  <!-- Mark relevant points -->
  <g stroke="black" stroke-width="3" fill="black">
    <circle id="pointA" cx="100" cy="350" r="3" />
    <circle id="pointB" cx="250" cy="50" r="3" />
    <circle id="pointC" cx="400" cy="350" r="3" />
  </g>
  <!-- Label the points -->
  <g font-size="30" font="sans-serif" fill="black" stroke="none"
  text-anchor="middle">
    <text x="100" y="350" dx="-30">A</text>
    <text x="250" y="50" dy="-10">B</text>
    <text x="400" y="350" dx="30">C</text>
  </g>
</svg>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_path2)


点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/path2.svg)。

### 注意事项


- `
` 元素的路径数据是 SVG 中最复杂的部分，需要一定的学习和实践才能熟练掌握各种路径命令的使用方式。 - 路径数据可以包含多个路径命令，每个路径命令都可以有不同的参数来控制路径的形状和方向。 通过使用 `` 元素，你可以在 SVG 中绘制各种复杂的图形和路径，并通过设置属性来控制路径的外观和样式。








	  AI 思考中...





			* [SVG 多边形](https://www.runoob.com/svg-polygon.html)
			[SVG 多段线](https://www.runoob.com/svg-polyline.html) **













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