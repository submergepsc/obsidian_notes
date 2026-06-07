# SVG 多段

- Source: https://www.runoob.com/svg/svg-polyline.html

SVG 中的 `` 元素用于绘制多段线，它是 SVG 中常用的基本形状之一。

与 `` 元素不同， `` 绘制的线条是未封闭的，即起点和终点不会自动连接。使用 `` 元素可以创建多个连接的线段，并可以通过设置属性来控制线段的顶点坐标、填充颜色、边框颜色等。


### 基本语法


```
<polyline
  points="x1,y1 x2,y2 x3,y3 ..."   <!-- 多段线各个顶点的坐标 -->
  fill="none"                      <!-- 多段线的填充颜色，使用 "none" 表示不填充 -->
  stroke="stroke-color"            <!-- 多段线的边框颜色 -->
  stroke-width="width"             <!-- 多段线的边框宽度 -->
/>
```


**属性解析：**


- `points` 属性定义了多段线各个顶点的坐标，多个顶点的坐标以空格或逗号分隔，并且每对坐标使用逗号分隔。
- `fill` 属性用于定义多段线的填充颜色，通常设置为 "none" 表示不填充。
- `stroke` 属性定义了多段线的边框颜色。
- `stroke-width` 属性定义了多段线的边框宽度。


以下代码绘制了一个黑色描边、宽度为 2 像素的多段线，其顶点坐标分别为 (50, 50)、(100, 150)、(150, 100) 和 (200, 200)，形成了多个连接的线段。


```
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <polyline points="50,50 100,150 150,100 200,200" fill="none" stroke="black" stroke-width="2" />
</svg>
```


### 实例 1


 元素是用于创建任何只有直线的形状：



Sorry, your browser does not support inline SVG. 下面是SVG代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
  <polyline points="20,20 40,25 60,40 80,120 120,140 200,180"
  style="fill:none;stroke:black;stroke-width:3" />
</svg>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_polyline)


点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/polyline1.svg)。


### 实例 2


只有直线的另一个例子：



Sorry, your browser does not support inline SVG. 下面是 SVG 代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
  <polyline points="0,40 40,40 40,80 80,80 80,120 120,120 120,160" style="fill:white;stroke:red;stroke-width:4" />
</svg>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_polyline2)


点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/polyline2.svg)。








	  AI 思考中...





			** [SVG 路径](https://www.runoob.com/svg-path.html)
			[SVG 文本](https://www.runoob.com/svg-text.html) **













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