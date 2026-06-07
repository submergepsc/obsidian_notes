# XML 语法规则

- Source: https://www.runoob.com/xml/xml-syntax.html

---


XML 的语法规则很简单，且很有逻辑。

这些规则很容易学习，也很容易使用。


---


## XML 声明

XML 声明文件的可选部分，如果存在需要放在文档的第一行，如下所示：


```
<?xml version="1.0" encoding="utf-8"?>
```


**
以上实例包含 XML 版本（version="1.0"），甚至包含字符编码（encoding="utf-8"）。

UTF-8 也是 HTML5, CSS, JavaScript, PHP, 和 SQL 的默认编码。


---


## XML 文档必须有根元素


XML 必须包含根元素，它是所有其他元素的父元素，比如以下实例中 root 就是根元素：


```xml
<root>
  <child>
    <subchild>.....</subchild>
  </child>
</root>
```


以下实例中 note 是根元素：


```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```


XML文档由元素构成，每个元素包括开始标签、结束标签和元素内容。


---


## 属性

元素可以包含属性，属性提供有关元素的附加信息。

属性位于开始标签中，例如：


```
<person age="30" gender="male">John Doe</person>
```


---


## XML 单标签


所有的 XML 元素一般都有一个关闭标签，但也允许单标签的使用的。


单标签的写法如下：


```
<elementName attribute="value" />
```


单标签是指在一个标签中同时包含了开始和结束标签，形式类似于 HTML 中的空元素标签。

在XML中，你可以使用以下两种方式表示单标签：


使用空元素标签：


```
<exampleTag />
```


使用开始和结束标签，但是不包含任何内容：


```
<exampleTag></exampleTag>
```


这两种表示方式是等效的，你可以根据个人或项目的约定选择使用其中之一。

在许多XML解析器中，它们都会将这两种形式解释为相同的结构。


### 实例


```
<lineBreak />
```


这里 `` 是一个单标签，表示一个换行的操作。


带属性的单标签：


```
<image src="logo.png" alt="Logo" />
```


这个标签表示一个图像元素，它包含 src 和 alt 属性，表示图像的路径和替代文本。


XML 文件示例：


## 实例


```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <note to="Tove" from="Jani" heading="Reminder" body="Don't forget me this weekend!" />
    <emptyElement attribute="value" />
</root>
```


在这个示例中，`` 和 `` 都是单标签。`` 标签的用途是传递信息，而 `` 是一个没有子元素的空标签。


---


## XML 标签对大小写敏感


XML 标签对大小写敏感。标签  与标签  是不同的。


必须使用相同的大小写来编写打开标签和关闭标签：


```
<Message>这是错误的</message>
<message>这是正确的</message>
```


注释：**打开标签和关闭标签通常被称为开始标签和结束标签。不论您喜欢哪种术语，它们的概念都是相同的。


---


## XML 必须正确嵌套


在 HTML 中，常会看到没有正确嵌套的元素：


```
<b><i>This text is bold and italic</b></i>
```


在 XML 中，所有元素都**必须**彼此正确地嵌套：


```
<b><i>This text is bold and italic</i></b>
```


在上面的实例中，正确嵌套的意思是：由于  元素是在  元素内打开的，那么它必须在  元素内关闭。


---


## XML 属性值必须加引号


与 HTML 类似，XML 元素也可拥有属性（名称/值的对）。


在 XML 中，XML 的属性值必须加引号。


请研究下面的两个 XML 文档。 第一个是错误的，第二个是正确的：


```
<note date=12/11/2007>
<to>Tove</to>
<from>Jani</from>
</note>
```


```
<note date="12/11/2007">
<to>Tove</to>
<from>Jani</from>
</note>
```


在第一个文档中的错误是，note 元素中的 date 属性没有加引号。


---


## 实体引用


在 XML 中，一些字符拥有特殊的意义。


如果您把字符 " | greater than |
| & | & | ampersand |
| ' | ' | apostrophe |
| " | " | quotation mark |


**注释：**在 XML 中，只有字符 "







	  AI 思考中...





			** [XML 树结构](https://www.runoob.com/xml-tree.html)
			[XML 元素](https://www.runoob.com/xml-elements.html) **