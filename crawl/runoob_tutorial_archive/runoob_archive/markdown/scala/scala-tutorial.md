# Scala 教程

- Source: https://www.runoob.com/scala/scala-tutorial.html

![python](https://www.runoob.com/wp-content/uploads/2015/12/scala-icon.png)

Scala 是一门多范式（multi-paradigm）的编程语言，设计初衷是要集成面向对象编程和函数式编程的各种特性。


Scala 运行在 Java 虚拟机上，并兼容现有的 Java 程序。


Scala 源代码被编译成 Java 字节码，所以它可以运行于 JVM 之上，并可以调用现有的 Java 类库。


---


## 谁适合阅读本教程？


本教程适合想从零开始学习 Scala 编程语言的开发人员。当然本教程也会对一些模块进行深入，让你更好的了解 Scala 的应用。

**
---


## 学习本教程前你需要了解


在继续本教程之前，你应该了解一些基本的计算机编程术语。如果你学习过Java编程语言，将有助于你更快的了解 Scala 编程。

学习 [Java 教程](https://www.runoob.com/../java/java-tutorial.html)。



---


## 第一个 Scala 程序：Hello World


以下是用 Scala 编写的典型 Hello World 程序：


## 实例（HelloWorld.scala）


```scala
object HelloWorld {
    def main(args: Array[String]): Unit = {
        println("Hello, world!")
    }
}
```


 [运行实例 »](https://www.runoob.com/try/runcode.php?filename=HelloWorld&type=scala)


将以上代码保存为 HelloWorld.scala 文件，执行以上 scala 程序（你也可以直接在线执行）：


```
$ scalac HelloWorld.scala  // 把源码编译为字节码
$ scala HelloWorld  // 把字节码放到虚拟机中解释运行
```


输出结果为：


```
Hello, world!
```


---


## 相关文档推荐


以下是一份 [Scala语言规范.pdf](https://static.jyshare.com/download/Scala%E8%AF%AD%E8%A8%80%E8%A7%84%E8%8C%83.pdf) 文档，可作为学习参考：

*







	  AI 思考中...






			[Scala 简介](https://www.runoob.com/scala-intro.html) *













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