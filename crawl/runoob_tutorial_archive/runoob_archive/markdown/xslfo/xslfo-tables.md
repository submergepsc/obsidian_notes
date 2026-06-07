# XSL-FO 表格

- Source: https://www.runoob.com/xslfo/xslfo-tables.html

---


XSL-FO 使用  元素来定义表格。


---


## XSL-FO 表格（Tables）


XSL-FO 表格模型与 HTML 表格模型不是完全不同的。


有九种 XSL-FO 对象可用来创建表格：


- fo:table-and-caption
- fo:table
- fo:table-caption
- fo:table-column
- fo:table-header
- fo:table-footer
- fo:table-body
- fo:table-row
- fo:table-cell


XSL-FO 使用 **** 元素来定义表格。它包含一个  以及一个可选的 **** 元素。


 元素包含可选的 **** 元素，一个可选的 **** 元素，一个 **** 元素，一个可选的 **** 元素。这些元素中的每一个都可能拥有一个或多个 **** 元素，而 **** 同时会带有一个或多个 **** 元素：


<fo:table-and-caption>**
<fo:table>

<fo:table-column column-width="25mm"/>

<fo:table-column column-width="25mm"/>


<fo:table-header>


  <fo:table-row>


    <fo:table-cell>


      <fo:block font-weight="bold">Car</fo:block>


    </fo:table-cell>


    <fo:table-cell>


      <fo:block font-weight="bold">Price</fo:block>


    </fo:table-cell>


  </fo:table-row>

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


以上代码的输出如下所示：


| Car | Price |
| --- | --- |
| Volvo | $50000 |
| SAAB | $48000 |










	  AI 思考中...





			** [XSL-FO 列表](https://www.runoob.com/xslfo-lists.html)
			[XSL-FO 与 XSLT](https://www.runoob.com/xslfo-xslt.html) **













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