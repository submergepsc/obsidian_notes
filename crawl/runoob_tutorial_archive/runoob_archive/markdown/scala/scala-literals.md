# Scala 字面量

- Source: https://www.runoob.com/scala/scala-literals.html

在 Scala 中，字面量（Literals）是直接表示固定值的表达式。

Scala支持各种类型的字面量，涵盖了数值、字符、字符串、布尔值等。


### 整型字面量


整型字面量用于 Int 类型，如果表示 Long，可以在数字后面添加 L 或者小写 l 作为后缀。


整型字面量可以是十进制、十六进制和八进制。


- 十进制：`42`, `0`, `-99`
- 十六进制：以`0x`或`0X`开头，如`0x2A`, `0x0`, `0XFF`
- 八进制：Scala 2.10 之前支持八进制字面量，以 `0` 开头，但在 Scala 2.10 及之后的版本中，八进制字面量被移除。


```
val decimal = 42
val hex = 0x2A
```


### 浮点型字面量


如果浮点数后面有 f 或者 F 后缀时，表示这是一个 Float 类型，否则就是一个 Double 类型的。


- 双精度：`3.14`, `-0.001`, `1.0e-10`
- 单精度：`3.14f`, `-0.001F`


```
val doubleValue = 3.14
val floatValue = 3.14f
```


### 布尔型字面量


布尔型字面量有 true 和 false。


```
val isScalaFun = true
val isSkyGreen = false
```


### 符号字面量


符号字面量被写成： **'** ，这里 **** 可以是任何字母或数字的标识（注意：不能以数字开头）。这种字面量被映射成预定义类 scala.Symbol 的实例。

如：符号字面量 **'x** 是表达式 **scala.Symbol("x")** 的简写，符号字面量定义如下：


```
package scala
final case class Symbol private (name: String) {
   override def toString: String = "'" + name
}
```


### 字符字面量

在 Scala 字符变量使用单引号 **'** 来定义，如下：


```
'a'
'\u0041'
'\n'
'\t'
```


其中 **\** 表示转义字符，其后可以跟 **u0041** 数字或者 **\r\n** 等固定的转义字符。


### 字符串字面量


在 Scala 字符串字面量使用双引号 **"** 来定义，如下：


```
"Hello,\nWorld!"
"菜鸟教程官网：www.runoob.com"
```


- 普通字符串：`"Hello, World!"`
- 多行字符串：使用三重引号 `"""` 括起来，可以包含换行符和引号。


### 多行字符串的表示方法


多行字符串用三个双引号来表示分隔符，格式为：**""" ... """**。


实例如下：


```
val foo = """菜鸟教程
www.runoob.com
www.runnoob.com
以上三个地址都能访问"""
```


### Null 值

Null是一个特殊的字面量，表示所有引用类型的空值。


空值是 scala.Null 类型。


Scala.Null 和 scala.Nothing 是用统一的方式处理 Scala 面向对象类型系统的某些"边界情况"的特殊类型。

Null 类是 null 引用对象的类型，它是每个引用类（继承自AnyRef的类）的子类。Null不兼容值类型。


```
val nullValue: String = null
```


### Unit

Unit 类型只有一个实例值，用字面量 **()** 表示，类似于 Java 中的 void。


```
val unitValue: Unit = ()
```


### 实例


以下是使用不同类型字面量的示例代码：


## 实例


```scala
object LiteralsExample {
  def main(args: Array[String]): Unit = {
    // 数值字面量
    val decimal = 42
    val hex = 0x2A
    val doubleValue = 3.14
    val floatValue = 3.14f

    // 字符字面量
    val charA = 'A'
    val charNewLine = '\n'

    // 字符串字面量
    val greeting = "Hello, World!"
    val multilineString = """This is
                            |a multi-line
                            |string""".stripMargin

    // 布尔字面量
    val isScalaFun = true
    val isSkyGreen = false

    // 特殊字面量
    val nullValue: String = null
    val unitValue: Unit = ()

    // 输出示例
    println(s"Decimal: $decimal, Hex: $hex")
    println(s"Double: $doubleValue, Float: $floatValue")
    println(s"Char: $charA, New Line: $charNewLine")
    println(s"Greeting: $greeting")
    println(s"Multiline String: $multilineString")
    println(s"Is Scala Fun: $isScalaFun, Is Sky Green: $isSkyGreen")
    println(s"Null Value: $nullValue, Unit Value: $unitValue")
  }
}
```


以上代码编译执行结果为：


```
Decimal: 42, Hex: 42
Double: 3.14, Float: 3.14
Char: A, New Line:

Greeting: Hello, World!
Multiline String: This is
a multi-line
string
Is Scala Fun: true, Is Sky Green: false
Null Value: null, Unit Value: ()
```










	  AI 思考中...





			** [Scala 文件 I/O](https://www.runoob.com/scala-file-io.html)
			[Scala 转义字符](https://www.runoob.com/scala-escape-char.html) **













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