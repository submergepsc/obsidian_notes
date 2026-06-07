# RDF 规则

- Source: https://www.runoob.com/rdf/rdf-rules.html

---


RDF 使用 Web 标识符 (URIs) 来标识资源。


RDF 使用属性和属性值来描述资源。


---


## RDF 资源、属性和属性值


RDF 使用 Web 标识符来标识事物，并通过属性和属性值来描述资源。


对资源、属性和属性值的解释：


- *资源*是可拥有 URI 的任何事物，比如 "https://www.runoob.com//rdf"
- *属性*是拥有名称的资源，比如 "author" 或 "homepage"
- *属性值*是某个属性的值，比如 "David" 或 "https://www.runoob.com/" （请注意一个属性值可以是另外一个资源）


下面的 RDF 文档可描述资源 "https://www.runoob.com//rdf"：


<?xml version="1.0"?>**

<RDF>


  <Description about="https://www.runoob.com//rdf">


    <author>Jan Egil Refsnes</author>


    <homepage>https://www.runoob.com/</homepage>


  </Description>

</RDF>


![lamp](https://www.runoob.com/images/lamp.gif) 上面是一个简化的例子。命名空间被忽略了。


---


## RDF 陈述


资源、属性和属性值的组合可形成一个*陈述*（被称为陈述的*主体*、*谓语*和*客体*）。


请看一些陈述的具体例子，来加深理解：


陈述："The author of https://www.runoob.com//rdf is David."


- 陈述的主体是：https://www.runoob.com//rdf
- 谓语是：author
- 客体是：David


陈述："The homepage of https://www.runoob.com//rdf is https://www.runoob.com/".


- 陈述的主体是：https://www.runoob.com//rdf
- 谓语是：homepage
- 客体是：https://www.runoob.com/









	  AI 思考中...





			** [RDF 简介](https://www.runoob.com/rdf-intro.html)
			[RDF 实例](https://www.runoob.com/rdf-example.html) **













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