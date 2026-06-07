# Scala 异常处理

- Source: https://www.runoob.com/scala/scala-exception-handling.html

Scala 的异常处理和其它语言比如 Java 类似。


Scala 的方法可以通过抛出异常的方法的方式来终止相关代码的运行，不必通过返回值。


---


## 抛出异常


Scala 抛出异常的方法和 Java一样，使用 throw 方法，例如，抛出一个新的参数异常：


```
throw new IllegalArgumentException
```


---


## 捕获异常


异常捕捉的机制与其他语言中一样，如果有异常发生，catch 字句是按次序捕捉的。因此，在 catch 字句中，越具体的异常越要靠前，越普遍的异常越靠后。 如果抛出的异常不在 catch 字句中，该异常则无法处理，会被升级到调用者处。

捕捉异常的 catch 子句，语法与其他语言中不太一样。在 Scala 里，借用了模式匹配的思想来做异常的匹配，因此，在 catch 的代码里，是一系列 case 字句，如下例所示：


## 实例


```scala
import java.io.FileReader
import java.io.FileNotFoundException
import java.io.IOException

object Test {
   def main(args: Array[String]) {
      try {
         val f = new FileReader("input.txt")
      } catch {
         case ex: FileNotFoundException =>{
            println("Missing file exception")
         }
         case ex: IOException => {
            println("IO Exception")
         }
      }
   }
}
```


执行以上代码，输出结果为：


```
$ scalac Test.scala
$ scala Test
Missing file exception
```


catch字句里的内容跟match里的case是完全一样的。由于异常捕捉是按次序，如果最普遍的异常，Throwable，写在最前面，则在它后面的case都捕捉不到，因此需要将它写在最后面。


---


## finally 语句


finally 语句用于执行不管是正常处理还是有异常发生时都需要执行的步骤，实例如下：


## 实例


```scala
import java.io.FileReader
import java.io.FileNotFoundException
import java.io.IOException

object Test {
   def main(args: Array[String]) {
      try {
         val f = new FileReader("input.txt")
      } catch {
         case ex: FileNotFoundException => {
            println("Missing file exception")
         }
         case ex: IOException => {
            println("IO Exception")
         }
      } finally {
         println("Exiting finally...")
      }
   }
}
```


执行以上代码，输出结果为：


```
$ scalac Test.scala
$ scala Test
Missing file exception
Exiting finally...
```









	  AI 思考中...





			** [Scala 正则表达式](https://www.runoob.com/scala-regular-expressions.html)
			[Scala 提取器(Extractor)](https://www.runoob.com/scala-extractors.html) **













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