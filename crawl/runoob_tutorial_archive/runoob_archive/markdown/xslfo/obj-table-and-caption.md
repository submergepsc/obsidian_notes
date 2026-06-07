# XSL-FO table-and-caption 对象

- Source: https://www.runoob.com/xslfo/obj-table-and-caption.html

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)

---


## 定义和用法


下面列举了 9 个可以用来创建表格的 XSL-FO 对象：


- fo:table-and-caption
- fo:table
- fo:table-caption
- fo:table-column
- fo:table-header
- fo:table-footer
- fo:table-body
- fo:table-row
- fo:table-cell


 对象是一个包含所有表格对象的容器，它用于格式化表格及其标题。


 对象包含了一个  对象和一个可选的  对象。


---


## 语法


<fo:table-and-caption>**
  <!--

    Contents:(table-caption?,table)

  -->

</fo:table-and-caption>


## 属性


| 属性 [A-J] | 属性 [K-Z] |
| --- | --- |
| azimuth | keep-together |
| background-attachment | keep-with-next |
| background-color | keep-with-previous |
| background-image | left |
| background-repeat | margin-bottom |
| background-position-horizontal | margin-left |
| background-position-vertical | margin-right |
| border-after-color | margin-top |
| border-after-style | padding-after |
| border-after-width | padding-before |
| border-before-color | padding-bottom |
| border-before-style | padding-end |
| border-before-width | padding-left |
| border-bottom-color | padding-right |
| border-bottom-style | padding-start |
| border-bottom-width | padding-top |
| border-end-color | pause-after |
| border-end-style | pause-before |
| border-end-width | pitch |
| border-left-color | pitch-range |
| border-left-style | play-during |
| border-left-width | relative-position |
| border-right-color | richness |
| border-right-style | right |
| border-right-width | role |
| border-start-color | source-document |
| border-start-style | space-after |
| border-start-width | space-before |
| border-top-color | speak |
| border-top-style | speak-header |
| border-top-width | speak-numeral |
| bottom | speak-punctuation |
| break-after | speech-rate |
| break-before | start-indent |
| caption-side | stress |
| cue-after | text-align |
| cue-before | top |
| elevation | voice-family |
| end-indent | volume |
| id |  |
| intrusion-displace |  |


### 实例 1


一个简单的表格：


<fo:table-and-caption>


<fo:table>


<fo:table-column column-width="25mm"/>

<fo:table-column column-width="25mm"/>


<fo:table-header>

  <fo:table-cell>

    <fo:block font-weight="bold">Car</fo:block>

  </fo:table-cell>

  <fo:table-cell>

    <fo:block font-weight="bold">Price</fo:block>

  </fo:table-cell>

</fo:table-header>


<fo:table-body>

  <fo:table-row>

    <fo:table-cell>

      <fo:block>Volvo</fo:block>

    </fo:table-cell>

    <fo:table-cell>

      <fo:block>$50000</fo:block>

    </fo:table-cell>

  </fo:table-row>

  <fo:table-row>

    <fo:table-cell>

      <fo:block>SAAB</fo:block>

    </fo:table-cell>

    <fo:table-cell>

      <fo:block>$48000</fo:block>

    </fo:table-cell>

  </fo:table-row>

</fo:table-body>


</fo:table>


</fo:table-and-caption>


上面代码的输出如下所示：


| Car | Price |
| --- | --- |
| Volvo | $50000 |
| SAAB | $48000 |


---

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)







	  AI 思考中...





			** [XSL-FO table 对象](https://www.runoob.com/obj-table.html)
			[XSL-FO table-body 对象](https://www.runoob.com/obj-table-body.html) **













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