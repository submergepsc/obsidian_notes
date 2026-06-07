# RDF 实例

- Source: https://www.runoob.com/rdf/rdf-example.html

---


## RDF 实例


这是一个 CD 列表的其中几行:


| 标题 | 艺术家 | 国家 | 公司 | 价格 | 年份 |
| --- | --- | --- | --- | --- | --- |
| Empire Burlesque | Bob Dylan | USA | Columbia | 10.90 | 1985 |
| Hide your heart | Bonnie Tyler | UK | CBS Records | 9.90 | 1988 |


这是一个 RDF 文档的其中几行：


<?xml version="1.0"?>**

<rdf:RDF

xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"

xmlns:cd="http://www.recshop.fake/cd#">


<rdf:Description

 rdf:about="http://www.recshop.fake/cd/Empire Burlesque">


  <cd:artist>Bob Dylan</cd:artist>


  <cd:country>USA</cd:country>


  <cd:company>Columbia</cd:company>


  <cd:price>10.90</cd:price>


  <cd:year>1985</cd:year>

</rdf:Description>


<rdf:Description

 rdf:about="http://www.recshop.fake/cd/Hide your heart">


  <cd:artist>Bonnie Tyler</cd:artist>


  <cd:country>UK</cd:country>


  <cd:company>CBS Records</cd:company>


  <cd:price>9.90</cd:price>


  <cd:year>1988</cd:year>

</rdf:Description>

.

.

.

</rdf:RDF>


此 RDF 文档的第一行是 XML 声明。这个 XML 声明之后是 RDF 文档的根元素：**。


*xmlns:rdf* 命名空间，规定了带有前缀 rdf 的元素来自命名空间 "http://www.w3.org/1999/02/22-rdf-syntax-ns#"。


*xmlns:cd* 命名空间，规定了带有前缀 cd 的元素来自命名空间 "http://www.recshop.fake/cd#"。


** 元素包含了对被 *rdf:about* 属性标识的资源的描述。


元素：**、**、** 等是此资源的属性。


---


## RDF 在线验证器


[W3C 的 RDF 验证服务](http://www.w3.org/RDF/Validator/)在您学习 RDF 时是很有帮助的。在此您可对 RDF 文件进行试验。


RDF 在线验证器可解析您的 RDF 文档，检查其中的语法，并为您的 RDF 文档生成表格和图形视图。


把下面这个例子拷贝粘贴到 W3C 的 RDF 验证器：


<?xml version="1.0"?>


<rdf:RDF

xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"

xmlns:si="http://www.runoob.com/rdf/">

  <rdf:Description rdf:about="http://www.runoob.com">


    <si:title>runoob.com</si:title>


    <si:author>Jan Egil Refsnes</si:author>

  </rdf:Description>

</rdf:RDF>


在您对上面的例子进行解析后，结果将是类似这样的。









	  AI 思考中...





			** [RDF 规则](https://www.runoob.com/rdf/rdf-rules.html)
			[RDF 主要元素](https://www.runoob.com/rdf/rdf-main.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#ee8f8a838780ae9c9b8081818cc08d8183)

      : · [免责声明](https://www.runoob.com/disclaimer)

      : · [关于我们](https://www.runoob.com/aboutus)

      : · [文章归档](https://www.runoob.com/archives)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/)**
    **[runoob.com](https://www.runoob.com/)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **