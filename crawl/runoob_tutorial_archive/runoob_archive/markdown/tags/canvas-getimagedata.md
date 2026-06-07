# HTML canvas getImageData() 方法

- Source: https://www.runoob.com/tags/canvas-getimagedata.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


下面的代码通过 getImageData() 复制画布上指定矩形的像素数据，然后通过 putImageData() 将图像数据放回画布：


```
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
ctx.fillStyle = "red";
ctx.fillRect(10, 10, 50, 50);

function copy() {
  const imgData = ctx.getImageData(10, 10, 50, 50);
  ctx.putImageData(imgData, 10, 70);
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_getimagedata)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 getImageData() 方法。


注意：** Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


getImageData() 方法返回 ImageData 对象，该对象拷贝了画布指定矩形的像素数据。


**注意：**ImageData 对象不是图像，它规定了画布上一个部分（矩形），并保存了该矩形内每个像素的信息。


对于 ImageData 对象中的每个像素，都存在着四方面的信息，即 RGBA 值：


R - 红色（0-255）** G - 绿色（0-255） B - 蓝色（0-255） A - alpha 通道（0-255; 0 是透明的，255 是完全可见的）


color/alpha 信息以数组形式存在，并存储于 ImageData 对象的 [data](https://www.runoob.com/canvas-imagedata-data.html) 属性中。


提示：**在操作完成数组中的 color/alpha 信息之后，您可以使用 [putImageData()](https://www.runoob.com/canvas-putimagedata.html) 方法将图像数据拷贝回画布上。


**实例：**


以下代码可获得被返回的 ImageData 对象中第一个像素的 color/alpha 信息：


```
red=imgData.data[0];
green=imgData.data[1];
blue=imgData.data[2];
alpha=imgData.data[3];
```


[尝试一下](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_getimagedata_firstpx)


**提示：**您也可以使用 getImageData() 方法来反转画布上某个图像的每个像素的颜色。


使用该公式遍历所有的像素，并改变其颜色值：


```
red=255-old_red;
green=255-old_green;
blue=255-old_blue;
```


请看下面的"尝试一下"实例！


---


## JavaScript 语法


| JavaScript 语法： | context.getImageData(x,y,width,height); |
| --- | --- |


## 参数值


| 参数 | 描述 |
| --- | --- |
| x | 开始复制的左上角位置的 x 坐标（以像素计）。 |
| y | 开始复制的左上角位置的 y 坐标（以像素计）。 |
| width | 要复制的矩形区域的宽度。 |
| height | 要复制的矩形区域的高度。 |

**
---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


## 要使用的图像：


![The Scream](https://www.runoob.com/wp-content/uploads/2013/11/img_the_scream.jpg)


## 实例


使用 getImageData() 来反转画布上的图像的每个像素的颜色：


YourbrowserdoesnotsupporttheHTML5canvastag.



JavaScript：


```
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
var img=document.getElementById("scream");
ctx.drawImage(img,0,0);
var imgData=ctx.getImageData(0,0,c.width,c.height);
// invert colors
for (var i=0;i<imgData.data.length;i+=4)
  {
  imgData.data[i]=255-imgData.data[i];
  imgData.data[i+1]=255-imgData.data[i+1];
  imgData.data[i+2]=255-imgData.data[i+2];
  imgData.data[i+3]=255;
  }
ctx.putImageData(imgData,0,0);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_getimagedata2)


---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas createImageData() 方法](https://www.runoob.com/canvas-createimagedata.html)
			[HTML canvas putImageData() 方法](https://www.runoob.com/canvas-putimagedata.html) **













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