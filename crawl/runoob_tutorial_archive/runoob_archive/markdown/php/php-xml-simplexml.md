# PHP SimpleXML

- Source: https://www.runoob.com/php/php-xml-simplexml.html

---


PHP SimpleXML 处理最普通的 XML 任务，其余的任务则交由其它扩展处理。


---


## 什么是 PHP SimpleXML？


SimpleXML 是 PHP 5 中的新特性。


SimpleXML 扩展提供了一种获取 XML 元素的名称和文本的简单方式。


与 DOM 或 Expat 解析器相比，SimpleXML 仅仅用几行代码就可以从 XML 元素中读取文本数据。


SimpleXML 可把 XML 文档（或 XML 字符串）转换为对象，比如：


- 元素被转换为 SimpleXMLElement 对象的单一属性。当同一级别上存在多个元素时，它们会被置于数组中。
- 属性通过使用关联数组进行访问，其中的索引对应属性名称。
- 元素内部的文本被转换为字符串。如果一个元素拥有多个文本节点，则按照它们被找到的顺序进行排列。


当执行类似下列的基础任务时，SimpleXML 使用起来非常快捷：


- 读取/提取 XML 文件/字符串的数据
- 编辑文本节点或属性


然而，在处理高级 XML 时，比如命名空间，最好使用 Expat 解析器或 XML DOM。


---


## 安装


从 PHP 5 开始，SimpleXML 函数是 PHP 核心的组成部分。无需安装就可以使用这些函数。


---


## PHP SimpleXML 实例


假设我们有如下的 XML 文件，"[note.xml](https://www.runoob.com/try/demo_source/note.xml)"：


```php
<?xml version="1.0" encoding="ISO-8859-1"?>
<note>
<to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
</note>
```


现在我们想要输出上面的 XML 文件的不同信息：


## 实例 1


输出 $xml 变量（是 SimpleXMLElement 对象）的键和元素：


```php
<?php
$xml=simplexml_load_file("note.xml");
print_r($xml);
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_simplexml)


以上代码将输出：


```
SimpleXMLElement Object ( [to] => Tove [from] => Jani [heading] => Reminder [body] => Don't forget me this weekend! )
```


## 实例 2


输出 XML 文件中每个元素的数据：


```php
<?php
$xml=simplexml_load_file("note.xml");
echo $xml->to . "<br>";
echo $xml->from . "<br>";
echo $xml->heading . "<br>";
echo $xml->body;
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_simplexml2)


以上代码将输出：


```
Tove
Jani
Reminder
Don't forget me this weekend!
```


## 实例 3


输出每个子节点的元素名称和数据：


```php
<?php
$xml=simplexml_load_file("note.xml");
echo $xml->getName() . "<br>";

foreach($xml->children() as $child)
{
    echo $child->getName() . ": " . $child . "<br>";
}
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_simplexml3)


以上代码将输出：


```
note
to: Tove
from: Jani
heading: Reminder
body: Don't forget me this weekend!
```


---


## 更多 PHP SimpleXML 的信息


如需了解更多关于 PHP SimpleXML 函数的信息，请访问我们的 [PHP SimpleXML 参考手册](https://www.runoob.com/php-ref-simplexml.html)。








	  AI 思考中...





			** [PHP XML DOM](https://www.runoob.com/php-xml-dom.html)
			[AJAX 简介](https://www.runoob.com/php-ajax-intro.html) **













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