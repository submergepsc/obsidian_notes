# XSLT 函数

- Source: https://www.runoob.com/xsl/xsl-functions.html

---


XQuery 1.0、XPath 2.0 以及 XSLT 2.0 共享相同的函数库。


---


## XSLT 函数


XSLT 含有超过 100 个内建的函数。这些函数用于字符串值、数值、日期和时间比较、节点和 QName 操作、序列操作、布尔值，等等。


![Note](https://www.runoob.com/images/lamp.gif)函数命名空间的默认前缀是 fn。


![Note](https://www.runoob.com/images/lamp.gif)函数命名空间的 URI 是： http://www.w3.org/2005/xpath-functions


**提示：**函数在被调用时常带有 fn: 前缀，比如 fn:string()。 不过，既然 fn: 是命名空间的默认前缀，那么在被调用时，函数的名称不必使用前缀。


[您可以在我们的 XPath 教程中访问所有内建的 XSLT 2.0 函数的参考手册。](https://www.runoob.com/../xpath/xpath-functions.html)


此外，下面列出了内建的 XSLT 函数：


| 名称 | 描述 |
| --- | --- |
| current() | 返回当前节点。 |
| document() | 用于访问外部 XML 文档中的节点。 |
| element-available() | 检测 XSLT 处理器是否支持指定的元素。 |
| format-number() | 把数字转换为字符串。 |
| function-available() | 检测 XSLT 处理器是否支持指定的函数。 |
| generate-id() | 返回唯一标识指定节点的字符串值。 |
| key() | 通过使用由 元素规定的索引号返回节点集。 |
| system-property() | 返回系统属性的值。 |
| unparsed-entity-uri() | 返回未解析实体的 URI。 |

**







	  AI 思考中...





			** [XSLT unparsed-entity-uri() 函数](https://www.runoob.com/func-unparsedentityuri.html)














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