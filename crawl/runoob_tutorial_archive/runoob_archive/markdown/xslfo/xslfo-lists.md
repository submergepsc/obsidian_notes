# XSL-FO 列表

- Source: https://www.runoob.com/xslfo/xslfo-lists.html

---


XSL-FO 使用  元素来定义列表。


---


## XSL-FO 列表块（List Blocks）


有四种 XSL-FO 对象可用来创建列表：


- fo:list-block（包含整个列表） (contains the whole list)
- fo:list-item（包含列表中的每个项目） (contains each item in the list)
- fo:list-item-label（包含用于 list-item 的标签 - 典型地，包含一个数字或者字符的  ）
- fo:list-item-body（包含 list-item 的内容/主体 - 典型地，一个或多个  对象）


一个 XSL-FO 列表实例:


<fo:list-block>**

<fo:list-item>


 <fo:list-item-label>


   <fo:block>*</fo:block>


 </fo:list-item-label>


 <fo:list-item-body>


   <fo:block>Volvo</fo:block>


 </fo:list-item-body>

</fo:list-item>


<fo:list-item>


 <fo:list-item-label>


   <fo:block>*</fo:block>


 </fo:list-item-label>


 <fo:list-item-body>


   <fo:block>Saab</fo:block>


 </fo:list-item-body>

</fo:list-item>


</fo:list-block>


上面代码的输出如下所示：


| * Volvo * Saab |
| --- |










	  AI 思考中...





			** [XSL-FO 块](https://www.runoob.com/xslfo-blocks.html)
			[XSL-FO 表格](https://www.runoob.com/xslfo-tables.html) **













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