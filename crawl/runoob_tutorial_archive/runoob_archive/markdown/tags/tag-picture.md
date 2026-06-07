# HTML 元素

- Source: https://www.runoob.com/tags/tag-picture.html

## 实例


根据屏幕匹配的不同尺寸显示不同图片，如果没有匹配到或浏览器不支持 picture 属性则使用 img 元素：


```
<picture>
  <source media="(min-width: 650px)" srcset="demo1.jpg">
  <source media="(min-width: 465px)" srcset="demo2.jpg">
  <img src="img_girl.jpg">
</picture>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_picture)


---


## 定义


picture 元素允许我们在不同的设备上显示不同的图片，一般用于响应式。


HTML5 引入了  元素，该元素可以让图片资源的调整更加灵活。


 元素零或多个  元素和一个  元素，每个  元素匹配不同的设备并引用不同的图像源，如果没有匹配的，就选择  元素的 src 属性中的 url。


注意:**`` 元素是放在最后一个 `` 元素之后，如果浏览器不支持该属性则显示  元素的的图片。


---


## 浏览器支持


表格中的数字表示支持该元素的第一个浏览器版本号。


| 元素 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 38.0 | 13.0 | 38.0 | 9.1 | 25.0 |


---


## HTML 4.01 与 HTML5 之间的差异


 属性是 HTML5 新定义的。


---


## 全局属性


 标签支持 [HTML 的全局属性](https://www.runoob.com/ref-standardattributes.html)。


---


## 事件属性


 标签支持 [HTML 的事件属性](https://www.runoob.com/ref-eventattributes.html)。








	  AI 思考中...





			** [HTML 颜色混搭](https://www.runoob.com/colors-mixer.html)
			[HTML main 标签](https://www.runoob.com/tag-main.html) **













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