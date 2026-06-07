# Kotlin 使用命令行编译

- Source: https://www.runoob.com/kotlin/kotlin-command-line.html

Kotlin 命令行编译工具下载地址：[https://github.com/JetBrains/kotlin/releases/tag/v1.1.2-2](https://github.com/JetBrains/kotlin/releases/tag/v1.1.2-2)，目前最新为 1.1.2-2。


你可以选择一个最新的稳定版下载。


下载完成后，解压到指定目录，然后将 **bin** 目录添加到系统环境变量。bin 目录包含编译和运行 Kotlin 所需的脚本。


---


## SDKMAN!


在 OS X、Linux、Cygwin、FreeBSD 和 Solaris 系统上也可以使用更简单的安装方法，命令如下：


```
$ curl -s https://get.sdkman.io | bash

$ sdk install kotlin
```


### Homebrew

在 OS X 下，你可以使用 Homebrew 安装：


```
$ brew update
$ brew install kotlin
```


### MacPorts


如果你是 MacPorts 用户，可以使用以下命令安装：


```
$ sudo port install kotlin
```


---


## 创建和运行第一个程序


创建一个名为 hello.kt 文件，代码如下：


## hello.kt



```kotlin
fun main(args: Array<String>) {
    println("Hello, World!")
}
```


使用 Kotlin 编译器编译应用:


```
$ kotlinc hello.kt -include-runtime -d hello.jar
```


- ** -d**: 用来设置编译输出的名称，可以是 class 或 .jar 文件，也可以是目录。 - ** -include-runtime** : 让 .jar 文件包含 Kotlin 运行库，从而可以直接运行。 如果你想看所有的可用选项，运行:


```
$ kotlinc -help
```


运行应用


```
$ java -jar hello.jar
Hello, World!
```


### 编译成库

若需要将生成的 jar 包供其他 Kotlin 程序使用，可无需包含 Kotlin 的运行库：


```
$ kotlinc hello.kt -d hello.jar
```


由于这样生成的 .jar 文件不包含 Kotlin 运行库，所以你应该确保当它被使用时，运行时在你的 classpath 上。

你也可以使用 kotlin 命令来运行 Kotlin 编译器生成的 .jar 文件


```
$ kotlin -classpath hello.jar HelloKt
```


HelloKt 为编译器为 hello.kt 文件生成的默认类名。


---

## 运行 REPL（交互式解释器）


我们可以运行如下命令得到一个可交互的 shell，然后输入任何有效的 Kotlin 代码，并立即看到结果


![](https://www.runoob.com/wp-content/uploads/2017/05/1495788947-5293-kotlin-shell.png)


---

## 使用命令行执行脚本


Kotlin 也可以作为一个脚本语言使用，文件后缀名为 .kts 。

例如我们创建一个名为 list_folders.kts，代码如下：


```
import java.io.File

val folders = File(args[0]).listFiles { file -> file.isDirectory() }
folders?.forEach { folder -> println(folder) }
```


执行时通过 -script 选项设置相应的脚本文件。


```
$ kotlinc -script list_folders.kts <path_to_folder>
```


$ kotlinc -script list_folders.kts
AI 思考中... ** [Kotlin Eclipse 环境搭建](https://www.runoob.com/kotlin-eclipse-setup.html) [Kotlin Android 环境搭建](https://www.runoob.com/otlin-android-setup.html) ** ### 点我分享笔记 笔记需要是本篇文章的内容扩展！
**

[文章投稿，可点击这里](https://www.runoob.com/tougao)


[注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)


### 分享笔记前必须登录！


[注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)
-->





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