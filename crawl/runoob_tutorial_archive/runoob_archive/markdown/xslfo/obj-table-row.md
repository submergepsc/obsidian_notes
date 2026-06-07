# XSL-FO table-row 对象

- Source: https://www.runoob.com/xslfo/obj-table-row.html

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)

---


## 定义和用法


 对象定义表格行。


---


## 语法


<fo:table-row>**
  <!--

    Contents:(table-cell+)

  -->

</fo:table-row>


## 属性


注意：**只有在表格的 border-collapse 值为 "collapse" 或 "collapse-with-precedence" 时，才允许使用 border 属性。


| 属性 [A-B] | 属性 [C-Z] |
| --- | --- |
| azimuth | cue-after |
| background-attachment | cue-before |
| background-color | elevation |
| background-image | height |
| background-repeat | id |
| background-position-horizontal | keep-together |
| background-position-vertical | keep-with-next |
| block-progression-dimension | keep-with-previous |
| border-after-color | left |
| border-after-precedence | pause-after |
| border-after-style | pause-before |
| border-after-width | pitch |
| border-before-color | pitch-range |
| border-before-precedence | play-during |
| border-before-style | relative-position |
| border-before-width | richness |
| border-bottom-color | right |
| border-bottom-style | role |
| border-bottom-width | source-document |
| border-collapse | speak |
| border-end-color | speak-header |
| border-end-precedence | speak-numeral |
| border-end-style | speak-punctuation |
| border-end-width | speech-rate |
| border-left-color | stress |
| border-left-style | top |
| border-left-width | visibility |
| border-right-color | voice-family |
| border-right-style | volume |
| border-right-width |  |
| border-separation |  |
| border-start-color |  |
| border-start-precedence |  |
| border-start-style |  |
| border-start-width |  |
| border-top-color |  |
| border-top-style |  |
| border-top-width |  |
| bottom |  |
| break-after |  |
| break-before |  |


### 实例


一个简单的表格：


<fo:table-and-caption>**

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





			** [XSL-FO table-header 对象](https://www.runoob.com/obj-table-header.html)
			[XSL-FO title 对象](https://www.runoob.com/obj-title.html) **













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