# SVG 滤镜

- Source: https://www.runoob.com/svg/svg-filters-intro.html

---


SVG 滤镜是一种强大的图形效果技术，可以用来实现各种视觉效果，例如模糊、阴影、光照等。

滤镜可以应用于 SVG 图形元素，例如矩形、圆形、路径等，以及 SVG 文本元素，使它们呈现出不同的外观和效果。


### 基本语法

SVG 滤镜通常使用 `` 元素定义，并通过 `filter` 属性将其应用于目标元素。


```
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- 定义滤镜 -->
  <filter id="filter_id">
    <!-- 滤镜效果 -->
  </filter>

  <!-- 应用滤镜的目标元素 -->
  <rect x="50" y="50" width="100" height="80" filter="url(#filter_id)" />
</svg>
```


### 滤镜效果

SVG 滤镜可以实现多种效果，常见的滤镜效果包括：

- **模糊（Blur）**：使图像产生模糊效果，通过 `` 元素实现。
- **阴影（Shadow）**：为图像添加阴影效果，通过 `` 元素实现。
- **亮度、对比度调整（Brightness, Contrast）**：调整图像的亮度和对比度，通过 `` 元素实现。
- **颜色矩阵（Color Matrix）**：通过颜色矩阵操作修改图像的颜色，通过 `` 元素实现。
- **混合模式（Blend Mode）**：将两个图像混合在一起，通过 `` 元素实现。


以下代码定义了一个模糊滤镜，然后将其应用于一个红色填充的矩形，使矩形呈现出模糊的效果。


## 实例


```svg
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- 定义模糊滤镜 -->
  <filter id="blur_filter">
    <feGaussianBlur in="SourceGraphic" stdDeviation="5" />
  </filter>

  <!-- 应用模糊滤镜的矩形 -->
  <rect x="50" y="50" width="100" height="80" fill="red" filter="url(#blur_filter)" />
</svg>
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_filters)


SVG 可用的滤镜是：


- feBlend - 与图像相结合的滤镜
- feColorMatrix - 用于彩色滤光片转换
- feComponentTransfer
- feComposite
- feConvolveMatrix
- feDiffuseLighting
- feDisplacementMap
- feFlood
- feGaussianBlur
- feImage
- feMerge
- feMorphology
- feOffset - 过滤阴影
- feSpecularLighting
- feTile
- feTurbulence
- feDistantLight - 用于照明过滤
- fePointLight - 用于照明过滤
- feSpotLight - 用于照明过滤


![Remark](https://www.runoob.com/images/lamp.gif) 除此之外，您可以在每个 SVG 元素上使用多个滤镜！


### 注意事项

- SVG 滤镜可以组合使用，可以在一个 `` 元素中定义多个滤镜效果。
- 每种滤镜效果都有不同的参数可以调整，例如模糊滤镜的标准差参数、阴影滤镜的偏移量和模糊半径等。
- SVG 滤镜可以与 CSS 样式表一起使用，也可以直接在SVG元素上使用 `style` 属性进行定义。

通过使用 SVG 滤镜，你可以为 SVG 图形元素添加各种视觉效果，使其呈现出更加生动、多样化的外观。








	  AI 思考中...





			** [SVG Stroke 属性](https://www.runoob.com/svg-stroke.html)
			[SVG 模糊效果 – 高斯模糊](https://www.runoob.com/svg-fegaussianblur.html) **













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