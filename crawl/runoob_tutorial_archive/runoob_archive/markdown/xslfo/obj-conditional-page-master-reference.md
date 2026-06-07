# XSL-FO conditional-page-master-reference 对象

- Source: https://www.runoob.com/xslfo/obj-conditional-page-master-reference.html

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)

---


## 定义和用法


 对象对象规定一个当所定义的条件成立时使用的 page-maste。


这使得不同的页面可以使用不同的 page-masters。（比如，偶数和奇数页面、第一个页面、空白页。）


三个属性，odd-or-even、blank-or-not-blank、page-position 规定条件。所有三个条件都成立时， 成立。


- 如果生成的页面有指定的位置（first, last, rest, any）时，page-position 成立。
- 如果值为 "any" 或值的奇偶性与页码匹配时，odd-or-even 成立。
- 如果值为 "not-blank" 且页面有由  的后代生成的区域时，或者如果值为 "blank" 且页面没有来自  的区域时，或者如果值为 "any" 时，blank-or-not-blank 成立。


---


## 语法


<fo:conditional-page-master-reference>**
  <!--

    Contents:EMPTY

  -->

</fo:conditional-page-master-reference>


## 属性


| 属性 |
| --- |
| blank-or-not-blank |
| master-reference |
| odd-or-even |
| page-postion |


---

[![XSL-FO 参考手册](https://www.runoob.com/images/up.gif) XSL-FO 参考手册](https://www.runoob.com/xslfo-reference.html)







	  AI 思考中...





			** [XSL-FO color-profile 对象](https://www.runoob.com/obj-color-profile.html)
			[XSL-FO declarations 对象](https://www.runoob.com/obj-declarations.html) **













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