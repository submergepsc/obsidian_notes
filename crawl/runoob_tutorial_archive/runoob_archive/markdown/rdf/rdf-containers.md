# RDF 容器元素

- Source: https://www.runoob.com/rdf/rdf-containers.html

---


**RDF 容器用于描述一组事物。举个例子，把某本书的作者列在一起。**


**下面的 RDF 元素用于描述这些的组：、 以及 。**


---


## 元素


 元素用于描述一个规定为无序的值的列表。


 元素可包含重复的值。


### 实例


<?xml version="1.0"?>**

<rdf:RDF

xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"

xmlns:cd="http://www.recshop.fake/cd#">


<rdf:Description

 rdf:about="http://www.recshop.fake/cd/Beatles">


 <cd:artist>


   <rdf:Bag>


     <rdf:li>John</rdf:li>


     <rdf:li>Paul</rdf:li>


     <rdf:li>George</rdf:li>


     <rdf:li>Ringo</rdf:li>


   </rdf:Bag>


  </cd:artist>

</rdf:Description>


</rdf:RDF>


---


## 元素


 元素用于描述一个规定为有序的值的列表（比如一个字母顺序的排序）。


 元素可包含重复的值。


### 实例


<?xml version="1.0"?>


<rdf:RDF

xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"

xmlns:cd="http://www.recshop.fake/cd#">


<rdf:Description

 rdf:about="http://www.recshop.fake/cd/Beatles">


 <cd:artist>


   <rdf:Seq>


     <rdf:li>George</rdf:li>


     <rdf:li>John</rdf:li>


     <rdf:li>Paul</rdf:li>


     <rdf:li>Ringo</rdf:li>


   </rdf:Seq>


  </cd:artist>

</rdf:Description>


</rdf:RDF>


---


## 元素


 元素用于一个可替换的值的列表（用户仅可选择这些值的其中之一）。


### 实例


<?xml version="1.0"?>


<rdf:RDF

xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"

xmlns:cd="http://www.recshop.fake/cd#">


<rdf:Descriptio

 rdf:about="http://www.recshop.fake/cd/Beatles">


 <cd:format>


   <rdf:Alt>


     <rdf:li>CD</rdf:li>


     <rdf:li>Record</rdf:li>


     <rdf:li>Tape</rdf:li>


   </rdf:Alt>


  </cd:format>

</rdf:Descriptio>


</rdf:RDF>


---


## RDF 术语


在上面的例子中，我们在描述容器元素时已经讨论了"值的列表"。在 RDF 中，这些"值的列表"被称为成员（members）。


因此，我们可以这么说：


- 一个容器是一个包含事物的资源
- 被包含的事物被称为成员（不能称为"值的列表"）。









	  AI 思考中...





			** [RDF 主要元素](https://www.runoob.com/rdf-main.html)
			[RDF 集合](https://www.runoob.com/rdf-%e9%9b%86%e5%90%88.html) **













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