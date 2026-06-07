# SVG 在 HTML 页面

- Source: https://www.runoob.com/svg/svg-inhtml.html

---


SVG 文件可通过以下标签嵌入 HTML 文档：、 或者 。


SVG 的代码可以直接嵌入到 HTML 页面中，或您可以直接链接到 SVG 文件。


---


## 使用 标签


通过 **** 标签可以将 SVG 图像作为图片嵌入到 HTML 页面中，可以使用 src 属性指定 SVG 文件的路径，也可以设置 width 和 height 属性来指定图片的宽度和高度。


**语法:**


```
<img src="example.svg" alt="SVG Image" width="200" height="200">
```


---


## 使用 标签


`` 标签用于将外部资源嵌入到HTML页面中，可以使用 `data` 属性指定 SVG 文件的路径，`type` 属性指定资源的 MIME 类型。

支持 SVG 的浏览器会直接显示 SVG 图像，不支持的浏览器会显示替代内容。


**语法:**


```
<object data="example.svg" type="image/svg+xml" width="200" height="200">
  Your browser does not support SVG
</object>
```


---


## 使用 标签


`` 标签用于在 HTML 页面中嵌入另一个HTML文档。可以使用 `src` 属性指定 SVG 文件的路径，并设置 `width` 和 `height` 属性来指定 iframe 的宽度和高度。


**语法:**


```
<iframe src="example.svg" width="200" height="200"></iframe>
```


---


## 直接在 HTML 嵌入 SVG 代码


在 HTML 页面中直接嵌入 SVG 代码，SVG 代码可以放置在 `` 标签中或其他合适的位置。

这种方式使得 SVG 图像与 HTML 内容混合在一起，可以直接在 HTML 页面中编辑和调整 SVG 图像。


## 实例


```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
   <circle cx="100" cy="50" r="40" stroke="black" stroke-width="2" fill="red" />
</svg>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_circle)


---


## 链接到 SVG 文件


您还可以用 **** 标签链接到一个 SVG 文件：


```
<a href="circle1.svg">查看 SVG 文件</a>
```


结果:**[查看 SVG 文件](https://www.runoob.com/try/demo_source/circle1.svg)


---


## 使用 CSS 背景图


通过 CSS 的 `background-image` 属性，可以将 SVG 图像作为背景图嵌入到 HTML 元素中。这种方法适用于需要在 CSS 中控制背景图样式的情况。


## 实例


```svg
.svg-bg {
  width: 200px;
  height: 200px;
  background-image: url('circle1.svg');
  background-size: cover;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trysvg_css_circle)







	  AI 思考中...





			** [SVG 基本语法](https://www.runoob.com/svg-example.html)
			[SVG 矩形](https://www.runoob.com/svg-rect.html) **













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