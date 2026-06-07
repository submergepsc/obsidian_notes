# HTML5 参考手册

- Source: https://www.runoob.com/tags/ref-canvas.html

---


## 描述


HTML5  标签用于绘制图像（通过脚本，通常是 JavaScript）。


不过， 元素本身并没有绘制能力（它仅仅是图形的容器） - 您必须使用脚本来完成实际的绘图任务。


getContext() 方法可返回一个对象，该对象提供了用于在画布上绘图的方法和属性。


本手册提供完整的 getContext("2d") 对象的属性和方法，可用于在画布上绘制文本、线条、矩形、圆形等等。


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif) ![Firefox](https://www.runoob.com/images/compatible_firefox.gif) ![Opera](https://www.runoob.com/images/compatible_opera.gif) ![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif) ![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持  标签的属性及方法。


**注意:**Internet Explorer 8 及更早的IE版本不支持  元素。


---


## 颜色、样式和阴影


| 属性 | 描述 |
| --- | --- |
| fillStyle | 设置或返回用于填充绘画的颜色、渐变或模式。 |
| strokeStyle | 设置或返回用于笔触的颜色、渐变或模式。 |
| shadowColor | 设置或返回用于阴影的颜色。 |
| shadowBlur | 设置或返回用于阴影的模糊级别。 |
| shadowOffsetX | 设置或返回阴影与形状的水平距离。 |
| shadowOffsetY | 设置或返回阴影与形状的垂直距离。 |

**


| 方法 | 描述 |
| --- | --- |
| createLinearGradient() | 创建线性渐变（用在画布内容上）。 |
| createPattern() | 在指定的方向上重复指定的元素。 |
| createRadialGradient() | 创建放射状/环形的渐变（用在画布内容上）。 |
| addColorStop() | 规定渐变对象中的颜色和停止位置。 |


## 线条样式


| 属性 | 描述 |
| --- | --- |
| lineCap | 设置或返回线条的结束端点样式。 |
| lineJoin | 设置或返回两条线相交时，所创建的拐角类型。 |
| lineWidth | 设置或返回当前的线条宽度。 |
| miterLimit | 设置或返回最大斜接长度。 |


## 矩形


| 方法 | 描述 |
| --- | --- |
| rect() | 创建矩形。 |
| fillRect() | 绘制"被填充"的矩形。 |
| strokeRect() | 绘制矩形（无填充）。 |
| clearRect() | 在给定的矩形内清除指定的像素。 |


## 路径


| 方法 | 描述 |
| --- | --- |
| fill() | 填充当前绘图（路径）。 |
| stroke() | 绘制已定义的路径。 |
| beginPath() | 起始一条路径，或重置当前路径。 |
| moveTo() | 把路径移动到画布中的指定点，不创建线条。 |
| closePath() | 创建从当前点回到起始点的路径。 |
| lineTo() | 添加一个新点，然后在画布中创建从该点到最后指定点的线条。 |
| clip() | 从原始画布剪切任意形状和尺寸的区域。 |
| quadraticCurveTo() | 创建二次贝塞尔曲线。 |
| bezierCurveTo() | 创建三次贝塞尔曲线。 |
| arc() | 创建弧/曲线（用于创建圆形或部分圆）。 |
| arcTo() | 创建两切线之间的弧/曲线。 |
| isPointInPath() | 如果指定的点位于当前路径中，则返回 true，否则返回 false。 |


## 转换


| 方法 | 描述 |
| --- | --- |
| scale() | 缩放当前绘图至更大或更小。 |
| rotate() | 旋转当前绘图。 |
| translate() | 重新映射画布上的 (0,0) 位置。 |
| transform() | 替换绘图的当前转换矩阵。 |
| setTransform() | 将当前转换重置为单位矩阵。然后运行 transform()。 |


## 文本


| 属性 | 描述 |
| --- | --- |
| font | 设置或返回文本内容的当前字体属性。 |
| textAlign | 设置或返回文本内容的当前对齐方式。 |
| textBaseline | 设置或返回在绘制文本时使用的当前文本基线。 |


| 方法 | 描述 |
| --- | --- |
| fillText() | 在画布上绘制"被填充的"文本。 |
| strokeText() | 在画布上绘制文本（无填充）。 |
| measureText() | 返回包含指定文本宽度的对象。 |


## 图像绘制


| 方法 | 描述 |
| --- | --- |
| drawImage() | 向画布上绘制图像、画布或视频。 |



## 像素操作


| 属性 | 描述 |
| --- | --- |
| width | 返回 ImageData 对象的宽度。 |
| height | 返回 ImageData 对象的高度。 |
| data | 返回一个对象，其包含指定的 ImageData 对象的图像数据。 |


| 方法 | 描述 |
| --- | --- |
| createImageData() | 创建新的、空白的 ImageData 对象。 |
| getImageData() | 返回 ImageData 对象，该对象为画布上指定的矩形复制像素数据。 |
| putImageData() | 把图像数据（从指定的 ImageData 对象）放回画布上。 |



## 合成


| 属性 | 描述 |
| --- | --- |
| globalAlpha | 设置或返回绘图的当前 alpha 或透明值。 |
| globalCompositeOperation | 设置或返回新图像如何绘制到已有的图像上。 |


## 其他


| 方法 | 描述 |
| --- | --- |
| save() | 保存当前环境的状态。 |
| restore() | 返回之前保存过的路径状态和属性。 |
| createEvent() |  |
| getContext() |  |
| toDataURL() |  |








	  AI 思考中...





			** [HTML 事件](https://www.runoob.com/ref-eventattributes.html)
			[HTML 音频/视频](https://www.runoob.com/ref-av-dom.html) **













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

      : · [HTML ASCII 字符集](https://www.runoob.com/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/html-colorpicker.html)

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