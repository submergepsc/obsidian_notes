# XSL-FO root 对象

- Source: https://www.runoob.com/xslfo/obj-root.html

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)

---


## 定义和用法


 对象是 XSL-FO 文档的根（顶级）节点。


 对象的子类是一个单独的  对象（该对象保留了在文档中使用的所有页面主 [master]），一个可选的  对象，以及是一个或多个  对象。



**注意：**一个 XSL-FO 文档可以包含多个  对象（举例：文档的每个章节都可以作为一个独立的  对象 - 它允许使用chapter-specific [具体的章节]内容，如：章节的标题，它可以被放置在页眉或页脚内）。



---


## 语法


<fo:root>**
  <!--

    Children:layout-master-set,declarations?,

    page-sequence+

  -->

</fo:root>


## 属性


| 属性 |
| --- |
| media-usage |


### 实例 1


XSL-FO 文档结构如下所示：


<?xml version="1.0" encoding="ISO-8859-1"?>


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


---

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)







	  AI 思考中...





			** [XSL-FO retrieve-marker 对象](https://www.runoob.com/obj-retrieve-marker.html)
			[XSL-FO simple-page-master 对象](https://www.runoob.com/obj-simple-page-master.html) **













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