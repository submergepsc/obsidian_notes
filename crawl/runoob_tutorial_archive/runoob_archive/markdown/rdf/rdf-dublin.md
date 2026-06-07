# RDF 都柏林核心元数据倡议

- Source: https://www.runoob.com/rdf/rdf-dublin.html

---


都柏林核心元数据倡议 (DCMI) 已创建了一些供描述文档的预定义属性。


---


## Dublin 核心


RDF 是元数据（关于数据的数据）。RDF 被用于描述信息资源。


都柏林核心是一套供描述文档的预定义属性。


第一份都柏林核心属性是于1995年 在俄亥俄州的都柏林的元数据工作组被定义的，目前由都柏林元数据倡议来维护。


| 属性 | 定义 |
| --- | --- |
| Contributor | 一个负责为资源内容作出贡献的实体(如作者)。 |
| Coverage | 资源内容的氛围或作用域 |
| Creator | 一个主要负责创建资源内容的实体。 |
| Format | 物理或数字的资源表现形式。 |
| Date | 在资源生命周期中某事件的日期。 |
| Description | 对资源内容的说明。 |
| Identifier | 一个对在给定上下文中的资源的明确引用 |
| Language | 资源智力内容所用的语言。 |
| Publisher | 一个负责使得资源内容可用的实体 |
| Relation | 一个对某个相关资源的引用 |
| Rights | 有关保留在资源之内和之上的权利的信息 |
| Source | 一个对作为目前资源的来源的资源引用。 |
| Subject | 一个资源内容的主题 |
| Title | 一个给资源起的名称 |
| Type | 资源内容的种类或类型。 |


通过浏览上面这个表格，我们可以发现 RDF 是非常适合表示都柏林核心信息的。


---


## RDF 实例


下面的例子演示了都柏林核心属性在一个 RDF 文档中的使用：


<?xml version="1.0"?>**

<rdf:RDF

xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"

xmlns:dc= "http://purl.org/dc/elements/1.1/">


<rdf:Description rdf:about="http://www.runoob.com">


  <dc:description>Run Noob - 奔跑吧！菜鸟</dc:description>


  <dc:publisher>Refsnes Data as</dc:publisher>


  <dc:date>2008-09-01</dc:date>


  <dc:type>Web Development</dc:type>


  <dc:format>text/html</dc:format>


  <dc:language>en</dc:language>

</rdf:Description>


</rdf:RDF>










	  AI 思考中...





			** [RDF Schema](https://www.runoob.com/rdf-schema.html)
			[OWL 简介](https://www.runoob.com/rdf-owl.html) **













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