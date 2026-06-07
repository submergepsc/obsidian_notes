# 架构

- Source: https://www.runoob.com/appml/appml-architecture.html

---


| ## MVC 架构 采用了 MVC 架构。 MVC 全名是 Model View Controller，是模型（Model）－视图（View）－控制器（Controller）的缩写，一种软件设计典范。 模型(Model) 描述你的应用。 视图(View) 显示你的数据。 制器(Controller) 控制你的应用。 Wikipedia: Model, View, Controller |  |  |
| --- | --- | --- |


---


## 模型(MODEL) - 仅仅是一个简单的XML文件


模型描述了您的应用程序，并且可在不同的硬件和软件平台（PC、iPhone、Tablets 等）重复使用。它不关心用户界面（UI）或表现形式。


模型采用xml编写，存储于web服务器中。


<appml>**

<datasource>


<database>

    <connection>Northwind</connection>
    <sql>SELECT
	CustomerName,ContactName,City,Country
FROM Customers</sql>


</database>

</datasource>


<filters>

	<query>
  <field label="Customer">CustomerName</field>

	<field>City</field>
  <field>Country</field>
</query>
<order>

	<field label="Customer">CustomerName</field>
  <field>City</field>

	<field>Country</field>
</order>
</filters>


</appml>


以上实例定义了数据源来自 Northwind 数据库。


该模型允许使用预定义的 SQL 获取数据。它还允许通过 Customer、City 和 Country 查询数据和排序。



---


## 视图（VIEW） - 仅仅是一个普通的 HTML 文件


视图即是 UI（User Interface：用户界面）。它通常是一个显示和输入数据（可选）HTML 页面：


<!DOCTYPE html>

<html>

<head>

<link rel="stylesheet" href="appml.css" />

</head>

<body>
My First Web Application


  customers=new AppML("appml.html","Customers.xml"); customers.run("Place01");





以上 HTML 页面使用通过执行脚本语言创建一个 AppML 对象，并将数据显示在 id="Place01" 的 div 中。


采用了 "appml.js" 脚本文件。


---


## CONTROLLER(控制器) - 仅仅是一个浏览器很服务端的脚本


服务端脚本通过以下方式控制应用：


- 从浏览器中接收请求数据
- 将模型和数据返回给浏览器
- 从浏览器中接收更新数据
- 在服务器上更新数据
- 数据通信过程，请进行数据安全验证。


浏览器脚本通过以下方式控制应用：


- 当页面加载时，你可以加载 控制器到页面上。
- 使用控制器，你可以在页面创建  对象。
- 当执行  对象时, 它会向服务器请求数据。
-  对象从服务器接受数据（使用数据模型）。
-  对象（或者你的代码）在页面中显示你的数据。
- （可选）web用户修改数据。
- （可选） 可以向服务器发送修改请求。


---


## 典型的 Web 文件和文件夹：


|  |  | web文件夹：Demo 数据文件夹：Data 图片文件夹：Images 模型文件夹： Models 应用：Demo.htm 样式：Demo.css 配置文件：appml_config.php (或者 .htmlx) 样式文件：appml.css 浏览器控制器：appml.js 服务器控制器：appml.php (或者 .htmlx) |
| --- | --- | --- |


---


## 快速、灵活的应用开发


快速应用开发（Rapid Application Development、RAD）不仅是一种需求抽取方法，它还是是软件开发为一体的方法。快速应用开发目的是快速发布系统方案，而技术上的优美相对发布的速度来说是次要的。


 提供超快速的原型设计，比传统的软件开发方法高100倍的速度。


应用程序原型可以直接从应用程序模型运行，无需任何编码。


[Wikipedia: Rapid Application Development](https://en.wikipedia.org/wiki/Rapid_application_development)


敏捷软件开发是基于用户和开发者相互协作的基础上一步一步的基发展而来的方法。


 应用从原型到完整的应用可以通过递增的方式一步步来编写实现。


[Wikipedia: Agile Software Development](https://en.wikipedia.org/wiki/Agile_software_development)


---


## 声明式编程


软件开发往往无法按照预期的时间和预算完成。软件编码错误也是经常出现。 这是因为计算机代码是很难开发、测试、维护。


编码已经过时了**。你应该更多描述做什么，而不是如何实现它。


使用  你需要在模型中**声明**你的应用 。


使用  可以**少写或者不用编写代码**。


**Wikipedia:** [Declarative Programming](https://en.wikipedia.org/wiki/Declarative_language)


---


## 代码先行（Code First）


Web应用程序开发可以使用以下两种不同的方式：


1. 代码先行（Code First）：使用预编程，预先测试的代码，只增加新的应用程序说明。


2. 契约优先（Contract First）：从头开始使用完整的应用程序的说明要求编写应用程序。


 采用最合理的概念： **代码先行（Code First）**。


---


## 面向服务的体系结构（service-oriented architecture，SOA）


**Web Service** 是一个数据接口，通过URL指定，就像一个web页面。 但它有别于web页面，它只是一种传达信息的方式。


一个典型的 **Web Service** 为页面提供了数据。


使用 ，HTML 显示为用户界面， 提供数据。


**Original Web Services** 设计使用了 XML 标志如 SOAP、WSDL 和 UDDI。


**Modern Web Services** 比如  应用更加简单。


- 更容易理解 - 可以被我们阅读
- 轻量级 - 没有不必要的代码或标记
- 易于实施 - 没有所需的开发工具


面向服务的体系结构（service-oriented architecture，SOA）是一个组件模型，它将应用程序的不同功能单元（称为服务）通过这些服务之间定义良好的接口和契约联系起来。接口是采用中立的方式进行定义的，它应该独立于实现服务的硬件平台、操作系统和编程语言。这使得构建在各种这样的系统中的服务可以以一种统一和通用的方式进行交互。


---


## Web Services的优势


- Web services 只需要少量的代码
- Web services 被设计来处理一组有限的任务
- Web services 使用基于HTTP的通信协议
- Web services 独立于操作系统
- Web services 独立于编程语言
- Web services 可以连接不同的应用程序，系统和设备
- Web Services 可以很容易地发布信息
- Web Services 有利于快速应用程序开发


例如一个Web services，可以设计一个小程序，提供其他最新的股票的交易价格的应用程序。


Web services使用HTTP协议与其他系统进行通信，Web服务是独立于操作系统和编程语言。


调用Web services的应用程序将始终使用HTTP协议发送请求。调用应用程序将永远不会关心其他计算机运行的操作系统或编程语言。


Web services可以为更多的企业创造新的可能性，因为它提供了一种简单的分发大量信息的方式。


比如：航班时刻表和机票预定系统。


---


## 云计算(Cloud Computing)


云计算（Cloud Computing）是SOA的扩展：应用即服务（Application-as-a service），存储即服务（Storage-as-a-service），数据即服务（Data-as-a-service）。


对于大多数人，云计算是在web上存储数据：


- 邮寄很日历
- 文档和电子表格
- 书籍、笔记、待办事项列表
- 音乐、图片和电影
- 数据库和应用程序


原因很明显：


- 有来自世界各地的访问数据
- 与他人分享我的数据
- 硬件升级或者崩溃


 可以很轻松地将数据库和应用程序放在云中。








	  AI 思考中...





			** [AppML 下载](https://www.runoob.com/appml-download.html)
			[AppML 参考手册](https://www.runoob.com/appml-reference.html) **













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