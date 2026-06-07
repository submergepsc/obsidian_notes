# XSL-FO block 对象

- Source: https://www.runoob.com/xslfo/obj-block.html

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)

---


## 定义和用法


 对象定义一个输出块。块是矩形框中的输出序列。


 对象用于格式化段落、标题、大字标题，等等。


---


## 语法


<fo:block>**
  <!--

    Contents:(#PCDATA|bidi-override|character|

    external-graphic|instream-foreign-object|

    inline|inline-container|leader|page-number|

    page-number-citation|basic-link|multi-toggle|

    block|block-container|table-and-caption|

    table|list-block)*

  -->

</fo:block>


## 属性


| 属性 [A-J] | 属性 [K-Z] |
| --- | --- |
| azimuth | keep-together |
| background-attachment | keep-with-next |
| background-color | keep-with-previous |
| background-image | language |
| background-repeat | last-line-end-indent |
| background-position-horizontal | left |
| background-position-vertical | linefeed-treatment |
| border-after-color | line-height |
| border-after-style | line-height-shift-adjustment |
| border-after-width | line-stacking-strategy |
| border-before-color | margin-bottom |
| border-before-style | margin-left |
| border-before-width | margin-right |
| border-bottom-color | margin-top |
| border-bottom-style | orphans |
| border-bottom-width | padding-after |
| border-end-color | padding-before |
| border-end-style | padding-bottom |
| border-end-width | padding-end |
| border-left-color | padding-left |
| border-left-style | padding-right |
| border-left-width | padding-start |
| border-right-color | padding-top |
| border-right-style | pause-after |
| border-right-width | pause-before |
| border-start-color | pitch |
| border-start-style | pitch-range |
| border-start-width | play-during |
| border-top-color | relative-position |
| border-top-style | richness |
| border-top-width | right |
| bottom | role |
| break-after | script |
| break-before | source-document |
| color | space-after |
| country | space-before |
| cue-after | span |
| cue-before | speak |
| elevation | speak-header |
| end-indent | speak-numeral |
| font-family | speak-punctuation |
| font-selection-strategy | speech-rate |
| font-size | start-indent |
| font-size-adjust | stress |
| font-stretch | text-align |
| font-style | text-align-last |
| font-variant | text-altitude |
| font-weight | text-depth |
| hyphenate | text-indent |
| hyphenation-character | top |
| hyphenation-keep | visibility |
| hyphenation-ladder-count | voice-family |
| hyphenation-push-character-count | volume |
| hyphenation-remain-character-count | white-space-collapse |
| id | white-space-treatment |
| intrusion-displace | widows |
|  | wrap-option |


### 实例 1


块是矩形框中的输出序列：


<fo:block

  border-width="1mm">

This block of output will have a one millimeter border around it.

</fo:block>


### 实例 2


块是可独立样式化的输出序列：


<fo:block

  font-size="12pt"

  font-family="sans-serif">

This block of output will be written in a 12pt sans-serif font.

</fo:block>


### 实例 3


<fo:block

  font-size="14pt" font-family="verdana" color="red"

  space-before="5mm" space-after="5mm">

RUNOOB

</fo:block>


<fo:block

  text-indent="5mm"

  font-family="verdana" font-size="12pt"

  space-before="5mm" space-after="5mm">

At RUNOOB you will find all the Web-building tutorials you

need, from basic HTML and XHTML to advanced XML, XSL, Multimedia

and WAP.

</fo:block>


结果：


| RUNOOB At RUNOOB you will find all the Web-building tutorials you need, from basic HTML and XHTML to advanced XML, XSL, Multimedia and WAP. |
| --- |


---

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)







	  AI 思考中...





			** [XSL-FO bidi-override 对象](https://www.runoob.com/obj-bidi-override.html)
			[XSL-FO block-container 对象](https://www.runoob.com/obj-block-container.html) **













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