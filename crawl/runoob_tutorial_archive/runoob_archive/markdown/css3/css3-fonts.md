# CSS3 字体

- Source: https://www.runoob.com/css3/css3-fonts.html

---

![With CSS3, web designers are no longer forced to use only web-safe fonts](https://www.runoob.com/images/font.gif)
---


## CSS3 @font-face 规则


使用以前 CSS 的版本，网页设计师不得不使用用户计算机上已经安装的字体。


使用 **CSS3**，网页设计师可以使用他/她喜欢的任何字体。


当你发现您要使用的字体文件时，只需简单的将字体文件包含在网站中，它会自动下载给需要的用户。


您所选择的字体在新的 **CSS3** 版本有关于 **@font-face** 规则描述。


您"自己的"的字体是在 **CSS3 @font-face** 规则中定义的。


---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| @font-face | 4.0 | 9.0 | 3.5 | 3.2 | 10.0 |


Internet Explorer 9+, Firefox, Chrome, Safari, 和 Opera 支持 WOFF (Web Open Font Format) 字体.


Firefox, Chrome, Safari, 和 Opera 支持 .ttf(True Type字体)和.otf(OpenType)字体字体类型）。


Chrome, Safari 和 Opera 也支持 SVG 字体/折叠.


Internet Explorer 同样支持 EOT (Embedded OpenType) 字体.


**注意：** Internet Explorer 8 以及更早的版本不支持新的 @font-face 规则。


---


## 使用您需要的字体


在新的 @font-face 规则中，您必须首先定义字体的名称（比如 myFirstFont），然后指向该字体文件。


|  | 提示：URL请使用小写字母的字体，大写字母在IE中会产生意外的结果 |
| --- | --- |


如需为 HTML 元素使用字体，请通过 font-family 属性来引用字体的名称 (myFirstFont)：


![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


```css
<style>
@font-face
{
    font-family: myFirstFont;
    src: url(sansation_light.woff);
}

div
{
    font-family:myFirstFont;
}
</style>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_font-face_rule)




---


## 使用粗体文本


您必须添加另一个包含粗体文字的@font-face规则：

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


```css
@font-face
{
    font-family: myFirstFont;
    src: url(sansation_bold.woff);
    font-weight:bold;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_font-face_rule_bold)




该文件"Sansation_Bold.ttf"是另一种字体文件，包含Sansation字体的粗体字。


浏览器使用这一文本的字体系列"myFirstFont"时应该呈现为粗体。


这样你就可以有许多相同的字体@font-face的规则。


---


## CSS3 字体描述


下表列出了所有的字体描述和里面的@font-face规则定义：


| 描述符 | 值 | 描述 |
| --- | --- | --- |
| font-family | name | 必需。规定字体的名称。 |
| src | URL | 必需。定义字体文件的 URL。 |
| font-stretch | normal condensed ultra-condensed extra-condensed semi-condensed expanded semi-expanded extra-expanded ultra-expanded | 可选。定义如何拉伸字体。默认是 "normal"。 |
| font-style | normal italic oblique | 可选。定义字体的样式。默认是 "normal"。 |
| font-weight | normal bold 100 200 300 400 500 600 700 800 900 | 可选。定义字体的粗细。默认是 "normal"。 |
| unicode-range | unicode-range | 可选。定义字体支持的 UNICODE 字符范围。默认是 "U+0-10FFFF"。 |








	  AI 思考中...





			** [CSS3 文本效果](https://www.runoob.com/css3-text-effects.html)
			[CSS3 2D 转换](https://www.runoob.com/css3-2dtransforms.html) **













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