# Scala 数据类型

- Source: https://www.runoob.com/scala/scala-data-types.html

Scala 支持的主要数据类型包括基本类型、集合类型、和特殊类型。


下表列出了 Scala 支持的数据类型：


| 类型类别 | 数据类型 | 描述 | Scala标准库中的实际类 |
| --- | --- | --- | --- |
| 基本类型 | Byte | 8位有符号整数，数值范围为 -128 到 127 | scala.Byte |
| 基本类型 | Short | 16位有符号整数，数值范围为 -32768 到 32767 | scala.Short |
| 基本类型 | Int | 32位有符号整数，数值范围为 -2147483648 到 2147483647 | scala.Int |
| 基本类型 | Long | 64位有符号整数，数值范围为 -9223372036854775808 到 9223372036854775807 | scala.Long |
| 基本类型 | Float | 32位IEEE 754单精度浮点数 | scala.Float |
| 基本类型 | Double | 64位IEEE 754双精度浮点数 | scala.Double |
| 基本类型 | Char | 16位无符号Unicode字符，数值范围为 U+0000 到 U+FFFF | scala.Char |
| 基本类型 | String | 字符串类型，表示字符序列 | java.lang.String |
| 基本类型 | Boolean | 布尔类型，值为 true 或 false | scala.Boolean |
| 集合类型 | List | 不可变链表 | scala.collection.immutable.List |
| 集合类型 | Set | 不可变集合 | scala.collection.immutable.Set |
| 集合类型 | Map | 不可变键值对集合 | scala.collection.immutable.Map |
| 集合类型 | Array | 可变数组 | scala.Array |
| 集合类型 | Tuple | 可包含不同类型元素的不可变容器 | scala.TupleN |
| 集合类型 | Option | 代表有可能含有值或为空的容器 | scala.Option |
| 集合类型 | Either | 表示两种可能的值类型之一 | scala.util.Either |
| 集合类型 | Try | 处理操作结果可能成功或失败的容器 | scala.util.Try |
| 特殊类型 | Unit | 表示无值，相当于Java中的 void | scala.Unit |
| 特殊类型 | Null | 单例对象，表示所有引用类型的空值 | scala.Null |
| 特殊类型 | Nothing | 表示无返回值类型，是所有类型的子类型 | scala.Nothing |
| 特殊类型 | Any | 所有类型的超类型 | scala.Any |
| 特殊类型 | AnyRef | 所有引用类型的超类型，等价于Java中的 Object | scala.AnyRef |


在 Scala 中，所有数据类型都是对象。


Scala 没有像 Java 中的原生类型（primitive types）那样的概念。尽管 Scala 的基本数据类型（如 Int、Double 等）在语法上看起来类似于 Java 的原生类型，但它们实际上是对象。这意味着你可以在这些类型上调用方法。


例如，Int 类型在 Scala 中实际上是 scala.Int 类的一个实例，而 scala.Int 是一个最终类，继承自 AnyVal。AnyVal 是 Scala 中的一个特殊类，表示值类型。


下面是一个完整的 Scala 程序，展示了各种数据类型的使用：


## DataTypeExamples.scala 文件代码：


```scala
object DataTypeExamples {
  def main(args: Array[String]): Unit = {
    // 基本类型
    val byteValue: Byte = 127
    val shortValue: Short = 32767
    val intValue: Int = 2147483647
    val longValue: Long = 9223372036854775807L
    val floatValue: Float = 3.14f
    val doubleValue: Double = 3.141592653589793
    val charValue: Char = 'A'
    val stringValue: String = "Hello, Scala!"
    val booleanValue: Boolean = true

    // 集合类型
    val listValue: List[Int] = List(1, 2, 3)
    val setValue: Set[String] = Set("Scala", "Java", "Python")
    val mapValue: Map[String, Int] = Map("one" -> 1, "two" -> 2, "three" -> 3)
    val arrayValue: Array[Int] = Array(4, 5, 6)
    val tupleValue: (Int, String, Boolean) = (42, "Answer", true)
    val optionValue: Option[String] = Some("I am here")
    val eitherValue: Either[String, Int] = Right(42)
    val tryValue: Try[Int] = Try(10 / 2)

    // 特殊类型
    val unitValue: Unit = ()
    val nullValue: String = null
    val nothingValue: Nothing = throw new RuntimeException("Nothing value")

    // 输出所有值
    println(s"Byte Value: $byteValue")
    println(s"Short Value: $shortValue")
    println(s"Int Value: $intValue")
    println(s"Long Value: $longValue")
    println(s"Float Value: $floatValue")
    println(s"Double Value: $doubleValue")
    println(s"Char Value: $charValue")
    println(s"String Value: $stringValue")
    println(s"Boolean Value: $booleanValue")

    println(s"List Value: $listValue")
    println(s"Set Value: $setValue")
    println(s"Map Value: $mapValue")
    println(s"Array Value: ${arrayValue.mkString(", ")}")
    println(s"Tuple Value: $tupleValue")
    println(s"Option Value: $optionValue")
    println(s"Either Value: $eitherValue")
    println(s"Try Value: $tryValue")

    println(s"Unit Value: $unitValue")
    println(s"Null Value: $nullValue")

    // nothingValue is not printed because it throws an exception
  }
}
```


使用 scalac 编译器进行编译，使用 scala 命令运行：


```
scalac DataTypeExamples.scala
scala DataTypeExamples
```


输出结果:


```
Byte Value: 127
Short Value: 32767
Int Value: 2147483647
Long Value: 9223372036854775807
Float Value: 3.14
Double Value: 3.141592653589793
Char Value: A
String Value: Hello, Scala!
Boolean Value: true
List Value: List(1, 2, 3)
Set Value: Set(Scala, Java, Python)
Map Value: Map(one -> 1, two -> 2, three -> 3)
Array Value: 4, 5, 6
Tuple Value: (42,Answer,true)
Option Value: Some(I am here)
Either Value: Right(42)
Try Value: Success(5)
Unit Value: ()
Null Value: null
```










	  AI 思考中...





			** [Scala 基础语法](https://www.runoob.com/scala-basic-syntax.html)
			[Scala 变量](https://www.runoob.com/scala-variables.html) **













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