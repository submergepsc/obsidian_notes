# XSL-FO region-before 对象

- Source: https://www.runoob.com/xslfo/obj-region-before.html

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)

---


## 定义和用法


 对象定义了页面的顶部区域（页眉）。


XSL-FO 使用下列元素来定义页面的区域：


-  定义了主体区域
-  定义了顶部区域（页眉）
-  定义了底部区域（页脚）
-  定义了左部区域（左侧栏）
-  定义了右部区域（右侧栏）


**注意：**region-before、region-after、region-start 以及 region-end 都是 region-body 的一部分。为了避免 region-body 内的文本覆盖其它区域的文本， region-body 的边距至少必须与上述四个子区域的尺寸相同。


**注意：**根据 XSL-FO 1.0 版本的推荐标准，padding 和 border-width 属性必须为 0。


---


## 语法


<fo:region-before>**
  <!--

    Contents:EMPTY

  -->

</fo:region-before>


## 属性


| 属性 [A-B] | 属性 [C-Z] |
| --- | --- |
| background-attachment | clip |
| background-color | display-align |
| background-image | extent |
| background-repeat | overflow |
| background-position-horizontal | padding-after |
| background-position-vertical | padding-before |
| border-after-color | padding-bottom |
| border-after-style | padding-end |
| border-after-width | padding-left |
| border-before-color | padding-right |
| border-before-style | padding-start |
| border-before-width | padding-top |
| border-bottom-color | precedence |
| border-bottom-style | region-name |
| border-bottom-width | reference-orientation |
| border-end-color | writing-mode |
| border-end-style |  |
| border-end-width |  |
| border-left-color |  |
| border-left-style |  |
| border-left-width |  |
| border-right-color |  |
| border-right-style |  |
| border-right-width |  |
| border-start-color |  |
| border-start-style |  |
| border-start-width |  |
| border-top-color |  |
| border-top-style |  |
| border-top-width |  |


### 实例 1


XSL-FO 使用名为 "Page Masters" 的页面模板来定义页面的布局。每个模板必须拥有一个唯一的名称：


<fo:simple-page-master master-name="intro">

  <fo:region-body margin="5in" />

</fo:simple-page-master>


<fo:simple-page-master master-name="left">

  <fo:region-body margin-left="2in" margin-right="3in" />

</fo:simple-page-master>


<fo:simple-page-master master-name="right">

  <fo:region-body margin-left="3in" margin-right="2in" />

</fo:simple-page-master>


在上面的实例中，三个  元素，定义了三个不同的模板。每个模板（page-master）都有不同的名称。


第一个模板名为 "intro"。它可作为介绍页面的模板使用。


第二个和第三个模板名为 "left" 和 "right"。它们可作为偶数和奇数页码的页面模板使用。


### 实例 2


这是从某个 XSL-FO 文档中提取的一个片断：


<fo:simple-page-master master-name="A4"

 page-width="297mm" page-height="210mm"

 margin-top="1cm"   margin-bottom="1cm"

 margin-left="1cm"  margin-right="1cm">

  <fo:region-body   margin="3cm"/>

  <fo:region-before extent="2cm"/>

  <fo:region-after  extent="2cm"/>

  <fo:region-start  extent="2cm"/>

  <fo:region-end    extent="2cm"/>

</fo:simple-page-master>


上面的代码定义了一个名称为 "A4" 的 "Simple Page Master Template"。


页面的宽度是 297 毫米，高度是 210 毫米。


页面的四个边距（上边距、下边距、左边距、右边距）均为 1 厘米。


主体的边距是 3 厘米（四个边都是）。


主体的 before、after、start 以及 end 区均为 2 厘米。


上面的实例中的主体的宽度可通过页面宽度减去左右边距以及 region-body 的边距来计算得出：


297mm - (2 x 1cm) - (2 x 3cm) = 297mm - 20mm - 60mm = 217mm


请注意，region（region-start 和 region-end）没有被计算进来。正如之前讲解过的，这些区（region）是主体的组成部分。


---

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)







	  AI 思考中...





			** [XSL-FO region-after 对象](https://www.runoob.com/obj-region-after.html)
			[XSL-FO region-body 对象](https://www.runoob.com/obj-region-body.html) **













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