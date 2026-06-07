# RDF Schema (RDFS)

- Source: https://www.runoob.com/rdf/rdf-schema.html

---


RDF Schema (RDFS) 是对 RDF 的一种扩展。


---


## RDF Schema 和 应用程序的类


RDF 通过类、属性和值来描述资源。


此外，RDF 还需要一种定义应用程序专业的类和属性的方法。应用程序专用的类和属性必须使用对 RDF 的扩展来定义。


RDF Schema 就是这样一种扩展。


---


## RDF Schema (RDFS)


RDF Schema 不提供实际的应用程序专用的类和属性，而是提供了描述应用程序专用的类和属性的框架。


RDF Schema 中的类与面向对象编程语言中的类非常相似。这就使得资源能够作为类的实例和类的子类来被定义。


---


## RDFS 实例


下面的实例演示了 RDFS 的能力的某些方面：


<?xml version="1.0"?>**

<rdf:RDF

xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"

xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"

xml:base="http://www.animals.fake/animals#">


<rdf:Description rdf:ID="animal">


  <rdf:type
   rdf:resource="http://www.w3.org/2000/01/rdf-schema#Class"/>

</rdf:Description>


<rdf:Description rdf:ID="horse">


  <rdf:type
   rdf:resource="http://www.w3.org/2000/01/rdf-schema#Class"/>


  <rdfs:subClassOf rdf:resource="#animal"/>

</rdf:Description>


</rdf:RDF>


在上面的例子中，资源 "horse" 是类 "animal" 的子类。


---


## 简写的例子


由于一个 RDFS 类就是一个 RDF 资源，我们可以通过使用 rdfs:Class 取代 rdf:Description，并去掉 rdf:type 信息，来把上面的例子简写一下：


<?xml version="1.0"?>


<rdf:RDF

xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"

xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"

xml:base="http://www.animals.fake/animals#">


<rdfs:Class rdf:ID="animal" />


<rdfs:Class rdf:ID="horse">


  <rdfs:subClassOf rdf:resource="#animal"/>

</rdfs:Class>


</rdf:RDF>


就是这样！








	  AI 思考中...





			** [RDF 集合](https://www.runoob.com/rdf-%e9%9b%86%e5%90%88.html)
			[RDF 都柏林核心](https://www.runoob.com/rdf-dublin.html) **













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