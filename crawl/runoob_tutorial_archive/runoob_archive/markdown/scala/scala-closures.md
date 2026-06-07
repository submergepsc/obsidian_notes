# Scala 闭包

- Source: https://www.runoob.com/scala/scala-closures.html

在 Scala 中，闭包（Closure）是一种函数，它能够捕获并包含其定义环境中的自由变量。


闭包是一个函数，返回值依赖于声明在函数外部的一个或多个变量。


闭包可以访问函数外部的变量并在函数内部使用这些变量，即使在变量的作用域已经超出其定义环境时，闭包仍然可以访问这些变量。


闭包的关键在于它可以"关闭"函数外部的变量，使得这些变量在函数内仍然可用。


如下面这段匿名的函数：


```
val multiplier = (i:Int) => i * 10
```


函数体内有一个变量 i，它作为函数的一个参数。如下面的另一段代码：


```
val multiplier = (i:Int) => i * factor
```


在 multiplier 中有两个变量：i 和 factor。其中的一个 i 是函数的形式参数，在 multiplier 函数被调用时，i 被赋予一个新的值。然而，factor不是形式参数，而是自由变量，考虑下面代码：
```
var factor = 3
val multiplier = (i:Int) => i * factor
```
 这里我们引入一个自由变量 factor，这个变量定义在函数外面。


这样定义的函数变量 multiplier 成为一个"闭包"，因为它引用到函数外面定义的变量，定义这个函数的过程是将这个自由变量捕获而构成一个封闭的函数。


完整实例


## 实例


```scala
object Test {
   def main(args: Array[String]) {
      println( "muliplier(1) value = " +  multiplier(1) )
      println( "muliplier(2) value = " +  multiplier(2) )
   }
   var factor = 3
   val multiplier = (i:Int) => i * factor
}
```

**[运行实例 »](https://www.runoob.com/try/runcode.php?filename=TestClosures&type=scala)


执行以上代码，输出结果为：


```
$ scalac Test.scala
$  scala Test
muliplier(1) value = 3
muliplier(2) value = 6
```


以下实例，closure 函数捕获了外部变量 externalVar，当 externalVar 的值改变时，闭包内的计算结果也相应改变。


## 实例


```scala
object ClosureExample1 {
  def main(args: Array[String]): Unit = {
    var externalVar = 10

    val closure = (x: Int) => x + externalVar

    println(closure(5))  // 输出 15

    externalVar = 20

    println(closure(5))  // 输出 25
  }
}
```


执行以上代码，输出结果为：


```
15
25
```


### 闭包作为返回值


以下实例，makeAdder 函数返回一个闭包。不同的闭包实例捕获了不同的 adder 值。


## 实例


```scala
object ClosureExample2 {
  def main(args: Array[String]): Unit = {
    def makeAdder(adder: Int): Int => Int = {
      (x: Int) => x + adder
    }

    val addFive = makeAdder(5)
    val addTen = makeAdder(10)

    println(addFive(3))  // 输出 8
    println(addTen(3))   // 输出 13
  }
}
```


执行以上代码，输出结果为：


```
8
13
```


---


## 闭包捕获变量的类型

闭包可以捕获不同类型的变量，包括值类型和引用类型。

以下实例，addMessage 闭包捕获了 messages 变量，并且可以修改它。


## 实例


```scala
object ClosureExample3 {
  def main(args: Array[String]): Unit = {
    var messages = List("Hello", "World")

    val addMessage = (msg: String) => messages = messages :+ msg

    addMessage("Scala")
    println(messages)  // 输出 List(Hello, World, Scala)
  }
}
```


执行以上代码，输出结果为：


```
List(Hello, World, Scala)
```


---


## 闭包与函数式编程

闭包在函数式编程中是一个重要的概念，广泛用于高阶函数、柯里化等技术中。

以下实例，highOrderFunction 函数接受一个函数作为参数。传递的闭包捕获了外部变量 externalVar。


## 实例


```scala
object ClosureExample4 {
  def main(args: Array[String]): Unit = {
    def highOrderFunction(f: Int => Int, x: Int): Int = f(x)

    val externalVar = 5
    val closure = (x: Int) => x + externalVar

    println(highOrderFunction(closure, 10))  // 输出 15
  }
}
```


执行以上代码，输出结果为：


```
15
```









	  AI 思考中...





			** [Scala 函数柯里化(Currying)](https://www.runoob.com/currying-functions.html)
			[Scala 字符串](https://www.runoob.com/scala-strings.html) **













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