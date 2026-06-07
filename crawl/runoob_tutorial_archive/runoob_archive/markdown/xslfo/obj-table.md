# XSL-FO table 对象

- Source: https://www.runoob.com/xslfo/obj-table.html

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)

---


## 定义和用法


 对象用于格式化表格的表格式材料。


 对象包含了可选的  对象、一个可选的  对象、一个  对象，以及一个可选的  对象。上述对象中的每个对象都包含一个或多个  对象（该对象中同样包含一个或多个  对象）。


---


## 语法


<fo:table>**
  <!--

    Contents:(table-column*,table-header?,

    table-footer?,table-body+)

  -->

</fo:table>


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
| block-progression-dimension | margin-top |
| border-after-color | padding-after |
| border-after-precedence | padding-before |
| border-after-style | padding-bottom |
| border-after-width | padding-end |
| border-before-color | padding-left |
| border-before-precedence | padding-right |
| border-before-style | padding-start |
| border-before-width | padding-top |
| border-bottom-color | pause-after |
| border-bottom-style | pause-before |
| border-bottom-width | pitch |
| border-collapse | pitch-range |
| border-end-color | play-during |
| border-end-precedence | relative-position |
| border-end-style | richness |
| border-end-width | right |
| border-left-color | role |
| border-left-style | source-document |
| border-left-width | space-after |
| border-right-color | space-before |
| border-right-style | speak |
| border-right-width | speak-header |
| border-separation | speak-numeral |
| border-start-color | speak-punctuation |
| border-start-precedence | speech-rate |
| border-start-style | start-indent |
| border-start-width | stress |
| border-top-color | table-layout |
| border-top-style | table-omit-footer-at-break |
| border-top-width | table-omit-header-at-break |
| bottom | top |
| break-after | voice-family |
| break-before | volume |
| cue-after | width |
| cue-before | writing-mode |
| elevation |  |
| end-indent |  |
| height |  |
| id |  |
| inline-progression-dimension |  |
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





			** [XSL-FO static-content 对象](https://www.runoob.com/obj-static-content.html)
			[XSL-FO table-and-caption 对象](https://www.runoob.com/obj-table-and-caption.html) **













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