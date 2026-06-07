# XSL-FO 流

- Source: https://www.runoob.com/xslfo/xslfo-flow.html

---


XSL-FO 页面使用来自  元素的数据进行填充。


---


## XSL-FO 页面序列（Page Sequences）


XSL-FO 使用  元素来定义**输出页面**。


每个**输出页面**都会引用一个定义**布局**的 page master。


每个**输出页面**都有一个定义**输出**的  元素。


每个**输出页面**均会**按序列（顺序）**被打印或显示。


---


## XSL-FO 流（Flow）


XSL-FO 页面使用来自  元素的内容进行填充。


 元素包含所有被打印到页面的元素。


当页面被印满以后，相同的 page master 会被一遍又一遍地被使用，直到所有文本被打印为止。


---


## 流动到何处？


 元素有一个 "flow-name" 属性。


flow-name 属性的值定义  元素的内容会去往何处。


合法的值：


- xsl-region-body（进入 region-body）
- xsl-region-before（进入 region-before）
- xsl-region-after（进入 region-after）
- xsl-region-start（进入 region-start）
- xsl-region-end（进入 region-end）

**







	  AI 思考中...





			** [XSL-FO 输出](https://www.runoob.com/xslfo-output.html)
			[XSL-FO 页面](https://www.runoob.com/xslfo-pages.html) **













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