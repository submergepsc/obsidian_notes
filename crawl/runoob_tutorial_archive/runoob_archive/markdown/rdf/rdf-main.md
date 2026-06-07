# RDF 主要 元素

- Source: https://www.runoob.com/rdf/rdf-main.html

---


**RDF 的主要元素是  以及可表示某个资源的  元素。**


---


## 元素


 是 RDF 文档的根元素。它把 XML 文档定义为一个 RDF 文档。它也包含了对 RDF 命名空间的引用：


<?xml version="1.0"?>**

<rdf:RDF

xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">


...*Description goes here...*

</rdf:RDF>


---


## 元素


 元素可通过 about 属性标识一个资源。


 元素可包含描述资源的那些元素：    Bob Dylan USA Columbia 10.90 1985   artist、country、company、price 以及 year 这些元素被定义在命名空间 http://www.recshop.fake/cd# 中。此命名空间在 RDF 之外（并非 RDF 的组成部分）。RDF 仅仅定义了这个框架。而 artist、country、company、price 以及 year 这些元素必须被其他人（公司、组织或个人等）进行定义。


---


## 属性（property）来定义属性（attribute）


属性元素（property elements）也可作为属性（attributes）来被定义（取代元素）：


<?xml version="1.0"?>


<rdf:RDF

xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"

xmlns:cd="http://www.recshop.fake/cd#">


<rdf:Description

 rdf:about="http://www.recshop.fake/cd/Empire Burlesque"

  cd:artist="Bob Dylan"  cd:country="USA"

  cd:company="Columbia"  cd:price="10.90"

  cd:year="1985" />


</rdf:RDF>


---


## 属性（property）来定义属性（attribute）


属性元素（property elements）也可作为属性（attributes）来被定义（取代元素）：


<?xml version="1.0"?>


<rdf:RDF

xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"

xmlns:cd="http://www.recshop.fake/cd#">


<rdf:Description

 rdf:about="http://www.recshop.fake/cd/Empire Burlesque">


  <cd:artist rdf:resource="http://www.recshop.fake/cd/dylan" />


  ...


  ...

</rdf:Description>


</rdf:RDF>


上面的例子中，属性 artist 没有值，但是却引用了一个对包含有关艺术家的信息的资源。








	  AI 思考中...





			** [RDF 实例](https://www.runoob.com/rdf-example.html)
			[RDF 容器](https://www.runoob.com/rdf-containers.html) **













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