# SVG 模糊效果

- Source: https://www.runoob.com/svg/svg-fegaussianblur.html

SVG 中的模糊效果可以通过 `` 元素实现，该元素使用高斯模糊算法来模糊图像。

模糊效果可以用于创建柔和的阴影、景深效果、模糊背景等各种视觉效果。


### 元素：


`` 元素用于对图像进行高斯模糊处理，它有两个主要参数：

- `stdDeviation`：指定高斯模糊的标准差。标准差越大，模糊程度越高。可以使用一个或两个数字，分别表示水平和垂直方向的标准差。如果只提供一个数字，则水平和垂直方向的标准差相同。
- `in`：指定输入图像，通常为 `SourceGraphic`，表示应用滤镜效果的目标元素本身。


以下代码定义了一个模糊滤镜，然后将其应用于一个红色填充的矩形，使矩形呈现出模糊的效果，stdDeviation="5" 表示水平和垂直方向的标准差均为 5，即模糊程度为 5 个像素。


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


### 实例 1


 元素是用于创建模糊效果：

![fegaussianblur](https://www.runoob.com/images/svg_fegaussianblur.jpg)
下面是SVG代码：


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
  <defs>
    <filter id="f1" x="0" y="0">
      <feGaussianBlur in="SourceGraphic" stdDeviation="15"
/>
    </filter>
  </defs>
  <rect width="90" height="90" stroke="green" stroke-width="3"
  fill="yellow" filter="url(#f1)" />
</svg>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_fegaussianblur)


点击查看：[查看 SVG 文件](https://www.runoob.com/try/demo_source/fegaussianblur1.svg)。


代码解析：**


- 元素id属性定义一个滤镜的唯一名称
- 元素定义模糊效果
- in="SourceGraphic"这个部分定义了由整个图像创建效果
- stdDeviation属性定义模糊量
- 元素的滤镜属性用来把元素链接到"f1"滤镜


### 注意事项

- 可以将模糊效果应用于任何SVG图形元素，包括矩形、圆形、路径等。
- 模糊效果的参数 `stdDeviation` 可以根据需要进行调整，以获得适合的模糊程度。
- 模糊效果可以与其他滤镜效果组合使用，例如阴影、混合模式等。

通过使用 `` 元素，你可以为SVG图形元素添加模糊效果，使其呈现出柔和、模糊的外观，从而实现各种视觉效果。








	  AI 思考中...





			** [SVG 滤镜](https://www.runoob.com/svg-filters-intro.html)
			[SVG 阴影](https://www.runoob.com/svg-feoffset.html) **













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