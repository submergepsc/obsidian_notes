# XSL-FO simple-page-master 对象

- Source: https://www.runoob.com/xslfo/obj-simple-page-master.html

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)

---


## 定义和用法


The  对象定义了一个页面的尺寸和形状。对于每个页面布局来说，都包含一个指定的 simple-page-master。


一个页面最多可以包含五个区域：region-body、region-before、region-after、region-start、region-end。


 对象将从  对象或 对象中引用。


---


## 语法


<fo:simple-page-master>**
  <!--

    Contents:(region-body,region-before?,

    region-after?,region-start?,region-end?)

  -->

</fo:simple-page-master>


## 属性


| 属性 |
| --- |
| end-indent |
| margin-bottom |
| margin-left |
| margin-right |
| margin-top |
| master-name |
| page-height |
| page-width |
| reference-orientation |
| space-after |
| space-before |
| start-indent |
| writing-mode |


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


### 实例 2


一个"真实的" XSL-FO 实例：


<?xml version="1.0" encoding="ISO-8859-1"?>


<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">


<fo:layout-master-set>

<fo:simple-page-master master-name="A4">

</fo:simple-page-master>

</fo:layout-master-set>


<fo:page-sequence master-reference="A4">

<fo:flow flow-name="xsl-region-body">

<fo:block>Hello RUNOOB</fo:block>

</fo:flow>

</fo:page-sequence>


</fo:root>


上面代码的输出如下所示：


| Hello RUNOOB |
| --- |


---

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)







	  AI 思考中...





			** [XSL-FO root 对象](https://www.runoob.com/obj-root.html)
			[XSL-FO single-page-master-reference 对象](https://www.runoob.com/obj-single-page-master-reference.html) **













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