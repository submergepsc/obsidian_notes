# SVG 渐变- 放射性

- Source: https://www.runoob.com/svg/svg-grad-radial.html

SVG 中的 `` 元素用于创建径向渐变，它可以从一个中心点向外扩散形成渐变效果，使图形呈现出环形、放射状等丰富的颜色变化。

径向渐变可以应用于填充或描边 SVG 图形元素，为其添加立体感和视觉效果。


### 基本语法


```
<radialGradient id="gradient_id" cx="cx" cy="cy" r="r" fx="fx" fy="fy">
  <stop offset="offset1" stop-color="color1" />
  <stop offset="offset2" stop-color="color2" />
  <!-- 更多的 <stop> 元素 -->
</radialGradient>
```


**参数说明：**


- `id` 属性定义了径向渐变的唯一标识符，用于在SVG图像中引用该渐变。
- `cx` 和 `cy` 属性定义了渐变的中心点坐标。
- `r` 属性定义了渐变的半径。
- `fx` 和 `fy` 属性定义了渐变焦点的坐标（可选），用于控制渐变的形状和方向。
- `` 元素用于指定渐变中的颜色和颜色的位置。

以下代码定义了一个从红色到蓝色的径向渐变，然后将其应用于一个填充的圆形，使圆形呈现出渐变的填充效果。


## 实例


```svg
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- 定义径向渐变 -->
  <radialGradient id="gradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
    <stop offset="0%" stop-color="red" />
    <stop offset="100%" stop-color="blue" />
  </radialGradient>

  <!-- 应用径向渐变的圆形 -->
  <circle cx="100" cy="100" r="80" fill="url(#gradient)" />
</svg>
```


### 实例 1


定义一个放射性渐变从白色到蓝色椭圆：


下面是SVG代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">

<defs>

<radialGradient id="grad1" cx="50%" cy="50%" r="50%"
fx="50%" fy="50%">

<stop offset="0%" style="stop-color:rgb(255,255,255);
      stop-opacity:0" />

<stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />

</radialGradient>

</defs>

<ellipse cx="200" cy="70" rx="85" ry="55"
fill="url(#grad1)" />
</svg>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_radial)


点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/radial1.svg)。


代码解析：**


- 标签的 id 属性可为渐变定义一个唯一的名称
- CX，CY和r属性定义的最外层圆和Fx和Fy定义的最内层圆
- 渐变颜色范围可以由两个或两个以上的颜色组成。每种颜色用一个标签指定。offset属性用来定义渐变色开始和结束
- 填充属性把ellipse元素链接到此渐变


### 实例 2


定义放射性渐变从白色到蓝色的另一个椭圆：


下面是 SVG 代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">

<defs>

<radialGradient id="grad1" cx="20%" cy="30%" r="30%"
fx="50%" fy="50%">

<stop offset="0%" style="stop-color:rgb(255,255,255);
      stop-opacity:0" />

<stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />

</radialGradient>

</defs>

<ellipse cx="200" cy="70" rx="85" ry="55" fill="url(#grad1)" />
</svg>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_radial2)


点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/radial2.svg)。

### 注意事项

- 渐变中可以包含多个 `` 元素，每个 `` 元素表示渐变中的一个颜色和位置。
- `cx`、`cy` 和 `r` 属性确定了渐变的中心和半径，而 `fx` 和 `fy` 属性则用于控制渐变焦点，可以调整渐变的形状和方向。
- 渐变的坐标值可以使用百分比或具体的长度值，百分比值相对于图形元素的大小。
- 可以将径向渐变应用于填充或描边 SVG 图形元素。

通过使用 `` 元素，你可以创建丰富多彩的径向渐变效果，为SVG图形元素添加立体感和视觉吸引力。








	  AI 思考中...





			** [SVG 渐变 – 线性](https://www.runoob.com/svg-grad-linear.html)
			[SVG 实例](https://www.runoob.com/svg-examples.html) **













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