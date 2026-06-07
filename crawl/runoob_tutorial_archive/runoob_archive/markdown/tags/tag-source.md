# HTML 标签

- Source: https://www.runoob.com/tags/tag-source.html

**
## 实例


带有两个源文件的音频播放器。浏览器需要选择它所支持的源文件（如果都支持则任选一个）：


```
<audio controls>
    <source src="horse.ogg" type="audio/ogg">
    <source src="horse.mp3" type="audio/mpeg">
    您的浏览器不支持 audio 元素。
</audio>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_source_src)


---


## 浏览器支持

表格中的数字表示支持该标签的第一个浏览器版本号。


| 标签 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 4.0 | 9.0 | 3.5 | 4.0 | 10.5 |


---


## 标签定义及使用说明


 标签为媒体元素（比如  和 ）定义媒体资源。


 标签允许您规定两个视频/音频文件供浏览器根据它对媒体类型或者编解码器的支持进行选择。


---


## HTML 4.01 与 HTML5之间的差异


 标签是 HTML5 中的新标签。


---


## 属性


New ：HTML5 中的新属性。


| 属性 | 值 | 描述 |
| --- | --- | --- |
| mediaNew | media_query | 规定媒体资源的类型，供浏览器决定是否下载。 |
| srcNew | URL | 规定媒体文件的 URL。 |
| type | MIME_type | 规定媒体资源的 MIME 类型。 |
| sizes |  | 不同页面布局设置不同图片大小。 |
| srcset | URL | 应用于 标签时需要使用到。指定在不同情况下使用的图像 URL。 |


---

## 更多实例


## 实例


在  标签中使用  来设置视频：


```
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
  Your browser does not support the video tag.
</video>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_video)


## 实例


在  标签中使用  来设置不同屏幕显示的图片：


```
<picture>
  <source media="(min-width:650px)" srcset="https://static.jyshare.com/images/runoob-logo.png">
  <source media="(min-width:465px)" srcset="https://static.jyshare.com/images/code-icon-script.png">
  <img src="https://static.jyshare.com/images/mix/hjkg_icon.png"  style="width:auto;">
</picture>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_picture)


## 全局属性


 标签支持 [HTML 的全局属性](https://www.runoob.com/ref-standardattributes.html)。


---


## 事件属性


 标签支持 [HTML 的事件属性](https://www.runoob.com/ref-eventattributes.html)。








	  AI 思考中...





			** [HTML  标签](https://www.runoob.com/tag-small.html)
			[HTML  标签](https://www.runoob.com/tag-span.html) **













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