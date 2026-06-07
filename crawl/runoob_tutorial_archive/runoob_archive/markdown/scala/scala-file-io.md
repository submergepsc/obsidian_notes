# Scala 文件 I/O

- Source: https://www.runoob.com/scala/scala-file-io.html

Scala 进行文件写操作，直接用的都是 java中 的 I/O 类 （**java.io.File**)：


## 实例


```scala
import java.io._

object Test {
   def main(args: Array[String]) {
      val writer = new PrintWriter(new File("test.txt" ))

      writer.write("菜鸟教程")
      writer.close()
   }
}
```


执行以上代码，会在你的当前目录下生产一个 test.txt 文件，文件内容为"菜鸟教程":


```
$ scalac Test.scala
$ scala Test
$ cat test.txt
菜鸟教程
```


---


## 从屏幕上读取用户输入


有时候我们需要接收用户在屏幕输入的指令来处理程序。实例如下：


## 实例


```scala
import scala.io._
object Test {
   def main(args: Array[String]) {
      print("请输入菜鸟教程官网 : " )
      val line = StdIn.readLine()

      println("谢谢，你输入的是: " + line)
   }
}
```


**
Scala2.11 后的版本 Console.readLine** 已废弃，使用 **scala.io.StdIn.readLine()** 方法代替。


执行以上代码，屏幕上会显示如下信息:


```
$ scalac Test.scala
$ scala Test
请输入菜鸟教程官网 : www.runoob.com
谢谢，你输入的是: www.runoob.com
```


---


## 从文件上读取内容


从文件读取内容非常简单。我们可以使用 Scala 的 **Source** 类及伴生对象来读取文件。以下实例演示了从 "test.txt"(之前已创建过) 文件中读取内容:


## 实例


```scala
import scala.io.Source

object Test {
   def main(args: Array[String]) {
      println("文件内容为:" )

      Source.fromFile("test.txt" ).foreach{
         print
      }
   }
}
```


执行以上代码，输出结果为:


```
$ scalac Test.scala
$ scala Test
文件内容为:
菜鸟教程
```









	  AI 思考中...





			** [Scala 提取器(Extractor)](https://www.runoob.com/scala-extractors.html)
			[Scala 字面量](https://www.runoob.com/scala-literals.html) **













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