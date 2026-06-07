# HTML canvas ImageData data 属性

- Source: https://www.runoob.com/tags/canvas-imagedata-data.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


创建 100*100 像素的 ImageData 对象，其中每个像素均被设置为红色：


## 画布


YourbrowserdoesnotsupporttheHTML5canvastag.



JavaScript：


```
var c=document.getElementById("myCanvas");
	var ctx=c.getContext("2d");
	var imgData=ctx.createImageData(100,100);
	for (var i=0;i<imgData.data.length;i+=4)
  {
  imgData.data[i+0]=255;
  imgData.data[i+1]=0;
  imgData.data[i+2]=0;
  imgData.data[i+3]=255;
  }
	ctx.putImageData(imgData,10,10);
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_createimagedata)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 ImageData data 属性。


注意：**Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


data 属性返回一个对象，该对象包含指定的 ImageData 对象的图像数据。


对于 ImageData 对象中的每个像素，都存在着四方面的信息，即 RGBA 值：


R - 红色（0-255）** G - 绿色（0-255） B - 蓝色（0-255） A - alpha 通道（0-255; 0 是透明的，255 是完全可见的）


color/alpha 信息以数组形式存在，并存储于 ImageData 对象的 data 属性中。


实例：**


把 ImageData 对象中的第一个像素变为红色的语法：


```
imgData=ctx.createImageData(100,100);
imgData.data[0]=255;
imgData.data[1]=0;
imgData.data[2]=0;
imgData.data[3]=255;
```


把 ImageData 对象中的第二个像素变为绿色的语法：


```
imgData=ctx.createImageData(100,100);
imgData.data[4]=0;
imgData.data[5]=255;
imgData.data[6]=0;
imgData.data[7]=255;
```


**提示：**请参阅 [createImageData()](https://www.runoob.com/canvas-createimagedata.html)、 [getImageData()](https://www.runoob.com/canvas-getimagedata.html) 和 [putImageData()](https://www.runoob.com/canvas-putimagedata.html) 方法，以获得更多关于 ImageData 对象的知识。


---


## JavaScript 语法


| JavaScript 语法： | imageData.data; |
| --- | --- |

**
---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas ImageData height 属性](https://www.runoob.com/canvas-imagedata-height.html)
			[HTML canvas createImageData() 方法](https://www.runoob.com/canvas-createimagedata.html) **













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