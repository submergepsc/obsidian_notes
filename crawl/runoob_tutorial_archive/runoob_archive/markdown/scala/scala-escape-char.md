# Scala 转义字符

- Source: https://www.runoob.com/scala/scala-escape-char.html

在 Scala 中，转义字符用于表示无法直接在字符串字面量中书写的特殊字符。


转义字符以反斜杠 **\** 开头，紧跟一个特定的字符，表示某种特殊含义或效果。


下表列出了常见的转义字符：


| 转义字符 | 描述 |
| --- | --- |
| \b | 退格符 |
| \t | 制表符 (Tab) |
| \n | 换行符 (Line Feed) |
| \f | 换页符 (Form Feed) |
| \r | 回车符 (Carriage Return) |
| \" | 双引号 |
| \' | 单引号 |
| \\ | 反斜杠 |


在字符或字符串中，0 到 255 间的 Unicode 字符可以用一个八进制转义序列来表示，即反斜杠 **\** 后跟最多三位八进制数字。

如果反斜杠 **\** 后面的字符序列不能构成一个合法的转义序列，将会导致编译错误。


以下实例演示了一些转义字符的使用：


## 实例


```scala
object Test {
   def main(args: Array[String]) {
      println("Hello\tWorld\n\n" );
   }
}
```

**[运行实例 »](https://www.runoob.com/try/runcode.php?filename=Test&type=scala)


执行以上代码输出结果如下所示：


```
$ scalac Test.scala
$ scala Test
Hello    World
```


以下是一个展示各种转义字符使用的 Scala 程序示例：


## 实例


```scala
object EscapeCharacterExamples {
  def main(args: Array[String]): Unit = {
    val backspace = "Hello\bWorld"     // "HelloWorld"
    val tab = "Hello\tWorld"           // "Hello    World"
    val newline = "Hello\nWorld"       // "Hello
                                       // World"
    val formFeed = "Hello\fWorld"      // "HelloWorld"
    val carriageReturn = "Hello\rWorld"// "World"
    val doubleQuote = "He said, \"Hello, World!\""  // "He said, "Hello, World!""
    val singleQuote = '\"'             // '"'
    val backslash = "This is a backslash: \\"  // "This is a backslash: \"

    // 输出示例
    println(s"Backspace: $backspace")
    println(s"Tab: $tab")
    println(s"Newline: $newline")
    println(s"FormFeed: $formFeed")
    println(s"CarriageReturn: $carriageReturn")
    println(s"DoubleQuote: $doubleQuote")
    println(s"SingleQuote: $singleQuote")
    println(s"Backslash: $backslash")
  }
}
```


执行上述代码，输出结果如下：
、


```
Backspace: HelloWorld
Tab: Hello    World
Newline: Hello
World
FormFeed: HelloWorld
CarriageReturn: World
DoubleQuote: He said, "Hello, World!"
SingleQuote: "
Backslash: This is a backslash: \
```


实例说明：**


- **`\b` (退格符)**: 使光标回退一个位置，但不会删除字符。例如，`"Hello\bWorld"` 结果为 `HelloWorld`，这里的并不删除 "o"，所以实际显示效果取决于终端或输出设备。
- **`\t` (制表符)**: 插入一个水平制表符，相当于一定数量的空格。`"Hello\tWorld"` 会在 "Hello" 和 "World" 之间插入一个制表符，通常是四个或八个空格。
- **`\n` (换行符)**: 移动到下一行开始新的输出。`"Hello\nWorld"` 会把 "Hello" 和 "World" 分成两行显示。
- **`\f` (换页符)**: 插入一个换页符，通常用来控制打印机换页，但在控制台输出中一般没有明显效果。
- **`\r` (回车符)**: 回到当前行的开头。`"Hello\rWorld"` 会覆盖掉当前行的内容，显示 "World"。
- **`\"` (双引号)**: 插入一个双引号。`"He said, \"Hello, World!\""` 显示 `He said, "Hello, World!"`。
- **`\'` (单引号)**: 插入一个单引号。通常用在字符字面量中，如 `'\'\''` 表示一个单引号字符。
- **`\\` (反斜杠)**: 插入一个反斜杠。`"This is a backslash: \\"` 显示 `This is a backslash: \`。








	  AI 思考中...





			** [Scala 字面量](https://www.runoob.com/scala-literals.html)














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