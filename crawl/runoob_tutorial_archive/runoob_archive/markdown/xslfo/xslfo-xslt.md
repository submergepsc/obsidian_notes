# XSL-FO 与 XSLT

- Source: https://www.runoob.com/xslfo/xslfo-xslt.html

---


XSL-FO 与 XSLT 可彼此互助。


---


## 还记得这个实例吗？


<fo:block
    font-size="14pt" font-family="verdana" color="red"**
    space-before="5mm" space-after="5mm">


RUNOOB

</fo:block>


<fo:block
    text-indent="5mm"
    font-family="verdana" font-size="12pt">


At RUNOOB you will find all the Web-building tutorials you


need, from basic HTML and XHTML to advanced XML, XSL, Multimedia and WAP.

</fo:block>


结果：


| RUNOOB At RUNOOB you will find all the Web-building tutorials you need, from basic HTML and XHTML to advanced XML, XSL, Multimedia and WAP. |
| --- |


上面的实例来自于有关 XSL-FO 块区域的那一章节。


---


## 来自 XSLT 的帮助


从文档移除 XSL-FO 信息：


<header>RUNOOB</header>


<paragraph>At RUNOOB you will find all the Web-building tutorials you

need, from basic HTML and XHTML to advanced XML, XSL, Multimedia and WAP.

</paragraph>


添加 XSLT 转换：


<xsl:template match="header">


<fo:block
    font-size="14pt" font-family="verdana" color="red"


    space-before="5mm" space-after="5mm">


    <xsl:apply-templates/>


</fo:block>

</xsl:template>


<xsl:template match="paragraph">


<fo:block
    text-indent="5mm"
    font-family="verdana" font-size="12pt">


    <xsl:apply-templates/>


</fo:block>

</xsl:template>


产生的结果是相同的：


| RUNOOB At RUNOOB you will find all the Web-building tutorials you need, from basic HTML and XHTML to advanced XML, XSL, Multimedia and WAP. |
| --- |










	  AI 思考中...





			** [XSL-FO 表格](https://www.runoob.com/xslfo-tables.html)
			[XSL-FO 软件](https://www.runoob.com/xslfo-software.html) **













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