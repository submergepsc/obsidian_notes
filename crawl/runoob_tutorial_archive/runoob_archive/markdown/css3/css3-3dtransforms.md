# CSS3 3D 转换

- Source: https://www.runoob.com/css3/css3-3dtransforms.html

---


## 3D 转换


CSS3 允许您使用 3D 转换来对元素进行格式化。


在本章中，您将学到其中的一些 3D 转换方法：


- rotateX()
- rotateY()


点击下面的元素，来查看 2D 转换与 3D 转换之间的不同之处：


	2D rotate
	3D rotate


**
---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


紧跟在 -webkit-, -ms- 或 -moz- 前的数字为支持该前缀属性的第一个浏览器版本号。


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| transform | 36.012.0 -webkit- | 10.0 | 16.010.0 -moz- | 4.0 -webkit- | 23.015.0 -webkit- |
| transform-origin(three-value syntax) | 36.012.0 -webkit- | 10.0 | 16.010.0 -moz- | 4.0 -webkit- | 23.015.0 -webkit- |
| transform-style | 36.012.0 -webkit- | 11.0 | 16.010.0 -moz- | 4.0 -webkit- | 23.015.0 -webkit- |
| perspective | 36.012.0 -webkit- | 10.0 | 16.010.0 -moz- | 4.0 -webkit- | 23.015.0 -webkit- |
| perspective-origin | 36.012.0 -webkit- | 10.0 | 16.010.0 -moz- | 4.0 -webkit- | 23.015.0 -webkit- |
| backface-visibility | 36.012.0 -webkit- | 10.0 | 16.010.0 -moz- | 4.0 -webkit- | 23.015.0 -webkit- |


## rotateX() 方法


![Rotate X](https://www.runoob.com/images/transform_rotatex.gif)
rotateX()方法，围绕其在一个给定度数X轴旋转的元素。


![Opera](https://www.runoob.com/images/incompatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


```css
div
{
    transform: rotateX(120deg);
    -webkit-transform: rotateX(120deg); /* Safari 与 Chrome */
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_transform_rotateX)


---


## rotateY() 方法

![Rotate Y](https://www.runoob.com/images/transform_rotatey.gif)
rotateY()方法，围绕其在一个给定度数Y轴旋转的元素。

![Opera](https://www.runoob.com/images/incompatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


```css
div
{
    transform: rotateY(130deg);
    -webkit-transform: rotateY(130deg); /* Safari 与 Chrome */
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_transform_rotateY)


---


## 转换属性


下表列出了所有的转换属性：


| 属性 | 描述 | CSS |
| --- | --- | --- |
| transform | 向元素应用 2D 或 3D 转换。 | 3 |
| transform-origin | 允许你改变被转换元素的位置。 | 3 |
| transform-style | 规定被嵌套元素如何在 3D 空间中显示。 | 3 |
| perspective | 规定 3D 元素的透视效果。 | 3 |
| perspective-origin | 规定 3D 元素的底部位置。 | 3 |
| backface-visibility | 定义元素在不面对屏幕时是否可见。 | 3 |


## 3D 转换方法


| 函数 | 描述 |
| --- | --- |
| matrix3d(n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n) | 定义 3D 转换，使用 16 个值的 4x4 矩阵。 |
| translate3d(x,y,z) | 定义 3D 转化。 |
| translateX(x) | 定义 3D 转化，仅使用用于 X 轴的值。 |
| translateY(y) | 定义 3D 转化，仅使用用于 Y 轴的值。 |
| translateZ(z) | 定义 3D 转化，仅使用用于 Z 轴的值。 |
| scale3d(x,y,z) | 定义 3D 缩放转换。 |
| scaleX(x) | 定义 3D 缩放转换，通过给定一个 X 轴的值。 |
| scaleY(y) | 定义 3D 缩放转换，通过给定一个 Y 轴的值。 |
| scaleZ(z) | 定义 3D 缩放转换，通过给定一个 Z 轴的值。 |
| rotate3d(x,y,z,angle) | 定义 3D 旋转。 |
| rotateX(angle) | 定义沿 X 轴的 3D 旋转。 |
| rotateY(angle) | 定义沿 Y 轴的 3D 旋转。 |
| rotateZ(angle) | 定义沿 Z 轴的 3D 旋转。 |
| perspective(n) | 定义 3D 转换元素的透视视图。 |








	  AI 思考中...





			** [CSS3 2D 转换](https://www.runoob.com/css3-2dtransforms.html)
			[CSS3 过渡](https://www.runoob.com/css3-transitions.html) **













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