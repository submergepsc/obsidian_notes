# Kotlin 教程

- Source: https://www.runoob.com/kotlin/kotlin-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2017/05/kotlin_250x250.png)

Kotlin 是一种在 Java 虚拟机上运行的静态类型编程语言，被称之为 Android 世界的Swift，由 JetBrains 设计开发并开源。

Kotlin 可以编译成Java字节码，也可以编译成 JavaScript，方便在没有 JVM 的设备上运行。

在Google I/O 2017中，Google 宣布 Kotlin 成为 Android 官方开发语言。


---

## 我的第一个 Kotlin 程序


Kotlin 程序文件以 **.kt** 结尾，如：hello.kt 、app.kt。


## 最简版



```kotlin
package hello                      //  可选的包头

fun main(args: Array<String>) {    // 包级可见的函数，接受一个字符串数组作为参数
   println("Hello World!")         // 分号可以省略
}
```


**[运行实例 »](https://www.runoob.com/try/runcode.php?filename=hello&type=kotlin)


## 面向对象



```kotlin
class Greeter(val name: String) {
   fun greet() {
      println("Hello, $name")
   }
}

fun main(args: Array<String>) {
   Greeter("World!").greet()          // 创建一个对象不用 new 关键字
}
```


[运行实例 »](https://www.runoob.com/try/runcode.php?filename=hello_class&type=kotlin)


---


## 为什么选择 Kotlin？


- 简洁: 大大减少样板代码的数量。
- 安全: 避免空指针异常等整个类的错误。
- 互操作性: 充分利用 JVM、Android 和浏览器的现有库。
- 工具友好: 可用任何 Java IDE 或者使用命令行构建。


---


## 参考链接


- [官方网站](http://www.kotlinlang.org)
- [官方示例](http://try.kotlinlang.org)
- [官方网站 - 中文翻译](https://www.kotlincn.net)
- [Kotlin 官方在线工具](https://play.kotlinlang.org/)
- [Kotlin 在线工具](https://c.runoob.com/compile/2960)









	  AI 思考中...






			[Kotlin IntelliJ IDEA 环境搭建](https://www.runoob.com/kotlin-setup.html) **













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