# XML 树结构

- Source: https://www.runoob.com/xml/xml-tree.html

---


XML 文档形成了一种树结构，它从"根部"开始，然后扩展到"枝叶"。


---


## 一个 XML 文档实例


XML 文档使用简单的具有自我描述性的语法：


```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>
```


第一行是 XML 声明。它定义 XML 的版本（1.0）和所使用的编码（UTF-8 : 万国码, 可显示各种语言）。


下一行描述文档的**根元素**（像在说："本文档是一个便签"）：


```
<note>
```


接下来 4 行描述根的 4 个**子元素**（to, from, heading 以及 body）：


```xml
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
```


最后一行定义根元素的结尾：


```
</note>
```


您可以假设，从这个实例中，XML 文档包含了一张 Jani 写给 Tove 的便签。


XML 具有出色的自我描述性，您同意吗？


---


## XML 文档形成一种树结构


XML 文档必须包含**根元素**。该元素是所有其他元素的父元素。


XML 文档中的元素形成了一棵文档树。这棵树从根部开始，并扩展到树的最底端。


所有的元素都可以有子元素：


```xml
<root>
<child>
<subchild>.....</subchild>
</child>
</root>
```


父、子以及同胞等术语用于描述元素之间的关系。父元素拥有子元素。相同层级上的子元素成为同胞（兄弟或姐妹）。


所有的元素都可以有文本内容和属性（类似 HTML 中）。


---


## 实例：

![DOM node tree](https://www.runoob.com/wp-content/uploads/2013/09/nodetree.gif)
上图表示下面的 XML 中的一本书：


## XML 文档实例


```xml
<bookstore>
    <book category="COOKING">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>
    <book category="CHILDREN">
        <title lang="en">Harry Potter</title>
        <author>J K. Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>
    <book category="WEB">
        <title lang="en">Learning XML</title>
        <author>Erik T. Ray</author>
        <year>2003</year>
        <price>39.95</price>
    </book>
</bookstore>
```


实例中的根元素是 。文档中的所有  元素都被包含在  中。


 元素有 4 个子元素：、、、。










	  AI 思考中...





			** [XML 用途](https://www.runoob.com/xml-usage.html)
			[XML 语法](https://www.runoob.com/xml-syntax.html) **