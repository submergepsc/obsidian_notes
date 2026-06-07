# SVG 直线

- Source: https://www.runoob.com/svg/svg-line.html

SVG 中的 `` 元素用于绘制直线，它是 SVG 中常用的基本形状之一。

使用 `` 元素可以创建两个点之间的直线，并可以通过设置属性来控制直线的位置、长度和样式。


### 基本语法


```
<line
  x1="x1-coordinate"     <!-- 起点的 x 坐标 -->
  y1="y1-coordinate"     <!-- 起点的 y 坐标 -->
  x2="x2-coordinate"     <!-- 终点的 x 坐标 -->
  y2="y2-coordinate"     <!-- 终点的 y 坐标 -->
  stroke="stroke-color"  <!-- 直线的颜色 -->
  stroke-width="width"   <!-- 直线的宽度 -->
/>
```


**属性解析:**


- `x1` 和 `y1` 属性定义了直线的起点坐标。
- `x2` 和 `y2` 属性定义了直线的终点坐标。
- `stroke` 属性定义了直线的颜色。
- `stroke-width` 属性定义了直线的宽度。


以下代码绘制了一个黑色描边、宽度为 2 像素的直线，起点坐标为 (50, 50)，终点坐标为 (150, 150)。


```
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <line x1="50" y1="50" x2="150" y2="150" stroke="black" stroke-width="2" />
</svg>
```


### 实例


下面是SVG代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">

<line x1="0" y1="0" x2="200" y2="200"

style="stroke:rgb(255,0,0);stroke-width:2"/>
</svg>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_line)


点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/line1.svg)。


- x1 属性在 x 轴定义线条的开始
- y1 属性在 y 轴定义线条的开始
- x2 属性在 x 轴定义线条的结束
- y2 属性在 y 轴定义线条的结束









	  AI 思考中...





			** [SVG 椭圆](https://www.runoob.com/svg-ellipse.html)
			[SVG 多边形](https://www.runoob.com/svg-polygon.html) **













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