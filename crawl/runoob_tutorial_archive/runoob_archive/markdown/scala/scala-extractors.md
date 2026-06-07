# Scala 提取器(Extractor)

- Source: https://www.runoob.com/scala/scala-extractors.html

提取器是从传递给它的对象中提取出构造该对象的参数。


Scala 标准库包含了一些预定义的提取器，我们会大致的了解一下它们。


Scala 提取器是一个带有unapply方法的对象。unapply方法算是apply方法的反向操作：unapply接受一个对象，然后从对象中提取值，提取的值通常是用来构造该对象的值。


以下实例演示了邮件地址的提取器对象：


## 实例


```scala
object Test {
   def main(args: Array[String]) {

      println ("Apply 方法 : " + apply("Zara", "gmail.com"));
      println ("Unapply 方法 : " + unapply("[email protected]"));
      println ("Unapply 方法 : " + unapply("Zara Ali"));

   }
   // 注入方法 (可选)
   def apply(user: String, domain: String) = {
      user +"@"+ domain
   }

   // 提取方法（必选）
   def unapply(str: String): Option[(String, String)] = {
      val parts = str split "@"
      if (parts.length == 2){
         Some(parts(0), parts(1))
      }else{
         None
      }
   }
}
```


执行以上代码，输出结果为：


```
$ scalac Test.scala
$ scala Test
Apply 方法 : [email protected]
Unapply 方法 : Some((Zara,gmail.com))
Unapply 方法 : None
```


以上对象定义了两个方法： **apply** 和 **unapply** 方法。通过 apply 方法我们无需使用 new 操作就可以创建对象。所以你可以通过语句 Test("Zara", "gmail.com") 来构造一个字符串 "[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"。


unapply方法算是apply方法的反向操作：unapply接受一个对象，然后从对象中提取值，提取的值通常是用来构造该对象的值。实例中我们使用 Unapply 方法从对象中提取用户名和邮件地址的后缀。


实例中 unapply 方法在传入的字符串不是邮箱地址时返回 None。代码演示如下：


```
unapply("[email protected]") 相等于 Some("Zara", "gmail.com")
unapply("Zara Ali") 相等于 None
```


---


## 提取器使用模式匹配


在我们实例化一个类的时，可以带上0个或者多个的参数，编译器在实例化的时会调用 apply 方法。我们可以在类和对象中都定义 apply 方法。


就像我们之前提到过的，unapply 用于提取我们指定查找的值，它与 apply 的操作相反。 当我们在提取器对象中使用 match 语句是，unapply 将自动执行，如下所示：


## 实例


```scala
object Test {
   def main(args: Array[String]) {

      val x = Test(5)
      println(x)

      x match
      {
         case Test(num) => println(x + " 是 " + num + " 的两倍！")
         //unapply 被调用
         case _ => println("无法计算")
      }

   }
   def apply(x: Int) = x*2
   def unapply(z: Int): Option[Int] = if (z%2==0) Some(z/2) else None
}
```


执行以上代码，输出结果为：


```
$ scalac Test.scala
$ scala Test
10
10 是 5 的两倍！
```









	  AI 思考中...





			** [Scala 异常处理](https://www.runoob.com/scala-exception-handling.html)
			[Scala 文件 I/O](https://www.runoob.com/scala-file-io.html) **













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