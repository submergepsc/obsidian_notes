# XSL-FO 文档

- Source: https://www.runoob.com/xslfo/xslfo-documents.html

---


## XSL-FO 文档


XSL-FO 文档是带有输出信息的 XML 文件。


XSL-FO 文档存储在以 .fo 或 .fob 为文件扩展名的文件中。您也可以把 XSL-FO 文档存储为以 .xml 为扩展名的文件，这样做的话可以使 XSL-FO 文档更易被 XML 编辑器存取。


---


## XSL-FO 文档结构


XSL-FO 的文档结构如下所示：


<?xml version="1.0" encoding="ISO-8859-1"?>**

<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">


<fo:layout-master-set>


  <fo:simple-page-master master-name="A4">


    <!-- Page template goes here -->


  </fo:simple-page-master>

</fo:layout-master-set>


<fo:page-sequence master-reference="A4">


  <!-- Page content goes here -->

</fo:page-sequence>


</fo:root>


## 结构解释


XSL-FO 文档属于 XML 文档，因此也需要以 XML 声明来起始：


<?xml version="1.0" encoding="ISO-8859-1"?>


 元素是 XSL-FO 文档的根元素。这个根元素也要声明 XSL-FO 的命名空间：


<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">


  <!-- The full XSL-FO document goes here -->

</fo:root>


 元素包含一个或多个页面模板：


<fo:layout-master-set>


  <!-- All page templates go here -->

</fo:layout-master-set>


每个  元素包含一个单一的页面模板。每个模板必须有一个唯一的名称（master-name）：


<fo:simple-page-master master-name="A4">


  <!-- One page template goes here -->

</fo:simple-page-master>


一个或多个  元素可描述页面内容。master-reference 属性使用相同的名称来引用 simple-page-master 模板：


<fo:page-sequence master-reference="A4">


  <!-- Page content goes here -->

</fo:page-sequence>


注释：**master-reference 的值 "A4" 实际上并没有描述某个预定义的页面格式。它仅仅是一个名称。您可以使用任何名称，比如 "MyPage"、"MyTemplate" 等等。

**







	  AI 思考中...





			** [XSL-FO 简介](https://www.runoob.com/xslfo-intro.html)
			[XSL-FO 区域属性](https://www.runoob.com/xslfo-areas.html) **













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