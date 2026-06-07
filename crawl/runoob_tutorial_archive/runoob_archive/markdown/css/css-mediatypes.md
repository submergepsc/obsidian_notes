# CSS 媒体类型

- Source: https://www.runoob.com/css/css-mediatypes.html

---


媒体类型允许你指定文件将如何在不同媒体呈现。该文件可以以不同的方式显示在屏幕上，在纸张上，或听觉浏览器等等。


---


## 媒体类型


一些 CSS 属性只设计了某些媒体。例如 **voice-family** 属性是专为听觉用户代理。其他一些属性可用于不同的媒体类型。例如， **font-size** 属性可用于屏幕和印刷媒体，但有不同的值。屏幕和纸上的文件不同，通常需要一个更大的字体，**sans-serif** 字体比较适合在屏幕上阅读，而 **serif** 字体更容易在纸上阅读。


---


## @media 规则


@media 规则允许在相同样式表为不同媒体设置不同的样式。


在下面的例子告诉我们浏览器屏幕上显示一个 14 像素的 Verdana 字体样式。但是如果页面打印，将是 10 个像素的 Times 字体。请注意，font-weight 在屏幕上和纸上设置为粗体：


## 实例


```css
@media screen
{
    p.test {font-family:verdana,sans-serif;font-size:14px;}
}
@media print
{
    p.test {font-family:times,serif;font-size:10px;}
}
@media screen,print
{
    p.test {font-weight:bold;}
}
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_mediatypes)


你可以自己尝试看看 !** 如果您使用的是 **Mozilla / Firefox** 或 IE5+ 打印此页，你会看到，媒体类型将使用另一种比其他文本字体大小小点的字体显示。


---


## 其他媒体类型


**注意：**媒体类型名称不区分大小写。


| 媒体类型 | 描述 |
| --- | --- |
| all | 用于所有的媒体设备。 |
| aural | 用于语音和音频合成器。 |
| braille | 用于盲人用点字法触觉回馈设备。 |
| embossed | 用于分页的盲人用点字法打印机。 |
| handheld | 用于小的手持的设备。 |
| print | 用于打印机。 |
| projection | 用于方案展示，比如幻灯片。 |
| screen | 用于电脑显示器。 |
| tty | 用于使用固定密度字母栅格的媒体，比如电传打字机和终端。 |
| tv | 用于电视机类型的设备。 |








	  AI 思考中...





			** [CSS 图像拼合技术](https://www.runoob.com/css-image-sprites.html)
			[CSS 属性选择器](https://www.runoob.com/css-attribute-selectors.html) **













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

      : ·[CSS 实例](https://www.runoob.com/css-examples.html)

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