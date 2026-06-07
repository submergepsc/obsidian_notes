# SVG 文本

- Source: https://www.runoob.com/svg/svg-text.html

SVG 中的 `` 元素用于在 SVG 图像中添加文本内容，它允许你在指定的位置显示文本，并可以通过设置属性来控制文本的样式、字体、大小等。


### 基本语法


```
<text
  x="x-coordinate"          <!-- 文本左上角的 x 坐标 -->
  y="y-coordinate"          <!-- 文本左上角的 y 坐标 -->
  font-family="font"        <!-- 字体名称 -->
  font-size="size"          <!-- 字体大小 -->
  fill="fill-color"         <!-- 文本颜色 -->
  text-anchor="anchor"      <!-- 文本锚点 -->
>
  Text content              <!-- 文本内容 -->
</text>
```


**属性解析：**

- `x` 和 `y` 属性定义了文本左上角的坐标，即文本的起始点位置。
- `font-family` 属性定义了文本的字体名称，可以是系统字体或自定义字体。
- `font-size` 属性定义了文本的字体大小，以像素为单位。
- `fill` 属性定义了文本的颜色。
- `text-anchor` 属性定义了文本锚点，即文本相对于指定坐标的对齐方式，常用取值有 "start"（默认，左对齐）、"middle"（居中对齐）和 "end"（右对齐）。


以下代码在 SVG 图像中绘制了一段文本，文本内容为 "Hello, SVG!"，字体为 Arial，大小为 20 像素，颜色为蓝色，居中对齐，并且文本左上角的坐标为 (100, 100)。


```
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <text x="100" y="100" font-family="Arial" font-size="20" fill="blue" text-anchor="middle">Hello, SVG!</text>
</svg>
```


### 实例 1


写一个文本：


*

下面是 SVG 代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">

<text x="0" y="15" fill="red">I
love SVG</text>
</svg>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_text)


点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/text1.svg)。

---


## 实例 2


旋转的文字：


下面是 SVG 代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">

<text x="0" y="15" fill="red"
transform="rotate(30 20,40)">I
love SVG</text>
</svg>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_text2)


点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/text2.svg)。

---


### 实例 3


路径上的文字：


下面是 SVG 代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1"
xmlns:xlink="http://www.w3.org/1999/xlink">
   <defs>
    <path id="path1" d="M75,20 a1,1 0 0,0 100,0" />
  </defs>
  <text x="10" y="100" style="fill:red;">
    <textPath xlink:href="#path1">I love SVG I love SVG</textPath>
  </text>
</svg>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_text3)


点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/text3.svg)。

---


### 实例 4


元素可以安排任何分小组与 元素的数量。每个 元素可以包含不同的格式和位置。几行文本(与  元素):


下面是 SVG 代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
  <text x="10" y="20" style="fill:red;">Several lines:
    <tspan x="10" y="45">First line</tspan>
    <tspan x="10" y="70">Second line</tspan>
  </text>
</svg>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_text4)


点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/text4.svg)。

---


## 实例 5


作为链接文本（  元素）：


下面是 SVG 代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1"
xmlns:xlink="http://www.w3.org/1999/xlink">
  <a xlink:href="http://www.w3schools.com/svg/"
target="_blank">
    <text x="0" y="15" fill="red">I love SVG</text>
  </a>
</svg>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_text5)


点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/text5.svg)。








	  AI 思考中...





			* [SVG 多段线](https://www.runoob.com/svg-polyline.html)
			[SVG Stroke 属性](https://www.runoob.com/svg-stroke.html) **













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