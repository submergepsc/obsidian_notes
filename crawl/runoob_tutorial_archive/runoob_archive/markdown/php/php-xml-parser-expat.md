# PHP XML Expat 解析器

- Source: https://www.runoob.com/php/php-xml-parser-expat.html

---


内建的 Expat 解析器使在 PHP 中处理 XML 文档成为可能。


---


## XML 是什么？


XML 用于描述数据，其焦点是数据是什么。XML 文件描述了数据的结构。


在 XML 中，没有预定义的标签。您必须定义自己的标签。


如需学习更多关于 XML 的知识，请访问我们的 [XML 教程](https://www.runoob.com/../xml/xml-tutorial.html)。


---


## Expat 是什么？


如需读取和更新 - 创建和处理 - 一个 XML 文档，您需要 XML 解析器。


有两种基本的 XML 解析器类型：


- 基于树的解析器：这种解析器把 XML 文档转换为树型结构。它分析整篇文档，并提供了对树中元素的访问，例如文档对象模型 (DOM)。
- 基于事件的解析器：将 XML 文档视为一系列的事件。当某个具体的事件发生时，解析器会调用函数来处理。


Expat 解析器是基于事件的解析器。


基于事件的解析器集中在 XML 文档的内容，而不是它们的结构。正因为如此，基于事件的解析器能够比基于树的解析器更快地访问数据。


请看下面的 XML 片段：


<from>Jani</from>


基于事件的解析器把上面的 XML 报告为一连串的三个事件：


- 开始元素：from
- 开始 CDATA 部分，值：Jani
- 关闭元素：from


上面的 XML 实例包含了形式良好的 XML。不过这个实例是无效的 XML，因为没有与它关联的文档类型声明 (DTD)。


然而，在使用 Expat 解析器时，这没有区别。Expat 是不检查有效性的解析器，忽略任何 DTD。


作为一款基于事件、非验证的 XML 解析器，Expat 快速且轻巧，十分适合 PHP 的 Web 应用程序。


**注释：**XML 文档必须形式良好，否则 Expat 会生成错误。


---


## 安装


XML Expat 解析器函数是 PHP 核心的组成部分。无需安装就可以使用这些函数。


---


## XML 文件


下面的 XML 文件将应用在我们的实例中：


<?xml version="1.0" encoding="ISO-8859-1"?>**
<note>

<to>Tove</to>

<from>Jani</from>

<heading>Reminder</heading>

<body>Don't forget me this weekend!</body>

</note>


---


## 初始化 XML 解析器


我们要在 PHP 中初始化 XML 解析器，为不同的 XML 事件定义处理器，然后解析这个 XML 文件。


### 实例


<?php

//Initialize the XML parser

$parser=xml_parser_create();


//Function to use at the start of an element

function start($parser,$element_name,$element_attrs)

  {

  switch($element_name)

    {

    case "NOTE":

    echo "-- Note --<br>";

    break;

    case "TO":

    echo "To: ";

    break;

    case "FROM":

    echo "From: ";

    break;

    case "HEADING":

    echo "Heading: ";

    break;

    case "BODY":

    echo "Message: ";

    }

  }


//Function to use at the end of an element

function stop($parser,$element_name)

  {

  echo "<br>";

  }


//Function to use when finding character data

function char($parser,$data)

  {

  echo $data;

  }


//Specify element handler

xml_set_element_handler($parser,"start","stop");


//Specify data handler

xml_set_character_data_handler($parser,"char");


//Open XML file

$fp=fopen("test.xml","r");


//Read data

while ($data=fread($fp,4096))

  {

  xml_parse($parser,$data,feof($fp)) or

  die (sprintf("XML Error: %s at line %d",

  xml_error_string(xml_get_error_code($parser)),

  xml_get_current_line_number($parser)));

  }


//Free the XML parser

xml_parser_free($parser);

?>


以上代码将输出：


-- Note --

To: Tove

From: Jani

Heading: Reminder

Message: Don't forget me this weekend!


工作原理：


- 通过 xml_parser_create() 函数初始化 XML 解析器
- 创建配合不同事件处理程序的的函数
- 添加 xml_set_element_handler() 函数来定义，当解析器遇到开始和结束标签时执行哪个函数
- 添加 xml_set_character_data_handler() 函数来定义，当解析器遇到字符数据时执行哪个函数
- 通过 xml_parse() 函数来解析文件 "test.xml"
- 万一有错误的话，添加 xml_error_string() 函数把 XML 错误转换为文本说明
- 调用 xml_parser_free() 函数来释放分配给 xml_parser_create() 函数的内存


---


## 更多 PHP Expat 解析器的信息


如需了解更多关于 PHP Expat 函数的信息，请访问我们的 [PHP XML Parser 参考手册](https://www.runoob.com/php-ref-xml.html)。








	  AI 思考中...





			** [PHP 数据库 ODBC](https://www.runoob.com/php-db-odbc.html)
			[PHP XML DOM](https://www.runoob.com/php-xml-dom.html) **













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