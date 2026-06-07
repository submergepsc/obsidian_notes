# XSL-FO leader 对象

- Source: https://www.runoob.com/xslfo/obj-leader.html

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)

---


## 定义和用法


 对象的作用如下：


- 生成 "." 符号来分隔内容表格中页面数字的标题
- 创建表单中的输入字段
- 创建水平规则


如果前导字符长度太长，与整个区域明显不适应，那么它将会另起一行。


只用在 leader-pattern 属性设置为 "use-content" 的情况下， 对象的子类才不会被忽略；如果  不包含子类，并且 leader-pattern 属性设置为 "use-content"，那么前导字符会被填充为空白。


如果前导字符需要在一行中填充所有的空格，那么前导字符的最大长度至少与列的宽度相同。


---


## 语法


<fo:leader>**
  <!--

    Contents:(#PCDATA|bidi-override|character|

    external-graphic|instream-foreign-object|

    inline|page-number|page-number-citation|

    basic-link|multi-toggle)*

  -->

</fo:leader>


## 属性


| 属性 [A-K] | 属性 [L-Z] |
| --- | --- |
| azimuth | leader-alignment |
| alignment-adjust | leader-length |
| alignment-baseline | leader-pattern |
| background-attachment | leader-pattern-width |
| background-color | left |
| background-image | letter-spacing |
| background-repeat | line-height |
| background-position-horizontal | margin-bottom |
| background-position-vertical | margin-left |
| baseline-shift | margin-right |
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
| border-start-color | rule-style |
| border-start-style | rule-thickness |
| border-start-width | source-document |
| border-top-color | space-end |
| border-top-style | space-start |
| border-top-width | speak |
| bottom | speak-header |
| color | speak-numeral |
| cue-after | speak-punctuation |
| cue-before | speech-rate |
| dominant-baseline | stress |
| elevation | text-altitude |
| font-family | text-depth |
| font-selection-strategy | text-shadow |
| font-size | top |
| font-size-adjust | visibility |
| font-stretch | voice-family |
| font-style | volume |
| font-variant | word-spacing |
| font-weight |  |
| id |  |
| keep-with-next |  |
| keep-with-previous |  |


---

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)







	  AI 思考中...





			** [XSL-FO layout-master-set 对象](https://www.runoob.com/obj-layout-master-set.html)
			[XSL-FO list-block 对象](https://www.runoob.com/obj-list-block.html) **













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