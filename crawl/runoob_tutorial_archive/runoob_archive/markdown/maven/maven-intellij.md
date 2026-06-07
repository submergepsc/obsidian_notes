# Maven IntelliJ

- Source: https://www.runoob.com/maven/maven-intellij.html

IntelliJ IDEA 已经内建了对 Maven 的支持。我们在此例中使用的是 IntelliJ IDEA 社区版 11.1。


IntelliJ IDEA 的一些特性列出如下：


- 可以通过 IntelliJ IDEA 来运行 Maven 目标。
- 可以在 IntelliJ IDEA 自己的终端里查看 Maven 命令的输出结果。
- 可以在 IDE 里更新 Maven 的依赖关系。
- 可以在 IntelliJ IDEA 中启动 Maven 的构建。
- IntelliJ IDEA 基于 Maven 的 pom.xml 来实现自动化管理依赖关系。
- IntelliJ IDEA 可以通过自己的工作区解决 Maven 的依赖问题，而无需安装到本地的 Maven 仓库，虽然需要依赖的项目在同一个工作区。
- IntelliJ IDEA 可以自动从远程 Maven 仓库上下载需要的依赖和源码。
- IntelliJ IDEA 提供了创建 Maven 项目，pom.xml 文件的向导。


## 在 IntelliJ IDEA 里创建一个新的项目


使用新建项目向导来导入一个 Maven 项目。


- 打开 IntelliJ IDEA。
- 选择 **File Menu > New Project** 选项。
- 选择 **import project from existing model** 选项。![](https://www.runoob.com/wp-content/uploads/2018/09/1536322987-1263-ij-new-project-step1.jpg)
- 选择 **Maven** 选项。![](https://www.runoob.com/wp-content/uploads/2018/09/1536322987-2379-ij-new-project-step2.jpg)
- 选择项目路径，即使用 Maven 创建一个项目时的存储路径。 假设我们创建了一个项目 **consumerBanking**。 通过 [Maven 构建 Java 项目](https://www.runoob.com/maven-creating-project.html) 查看如何使用 Maven 创建一个项目。![](https://www.runoob.com/wp-content/uploads/2018/09/1536322987-9205-ij-new-project-step3.jpg)
- 选择要导入的 Maven 项目。![](https://www.runoob.com/wp-content/uploads/2018/09/1536322987-5394-ij-new-project-step4.jpg)
- 输入项目名称，点击 "finish"。![](https://www.runoob.com/wp-content/uploads/2018/09/1536322987-5945-ij-new-project-step5.jpg)


现在，我们可以在 IntelliJ IDEA 里看到 Maven 项目了。看一下 consumerBanking 项目的 Libraries 和 Test Libraries，你可以发现 IntelliJ IDEA 已经将 Maven 所依赖的都添加到了它的构建路径里了。


![](https://www.runoob.com/wp-content/uploads/2018/09/1536322987-5486-ij-project-structure.jpg)


## 在 IntelliJ IDEA 里构建一个 Maven 项目


好了，接下来我们来使用 IntelliJ IDEA 的编译功能来构建这个 Maven 项目 。


- 选中 consumerBanking 项目。
- 选择 **Buid menu > Rebuild Project** 选项。


你可以在 IntelliJ IDEA 的终端里看到构建过程输出的log：


```
4:01:56 PM Compilation completed successfully
```


## 在 IntelliJ IDEA 里运行应用程序


- 选中 consumerBanking 项目。
- 右键点击 App.java 弹出上下文菜单。
- 选择 **Run App.main()** 。


![](https://www.runoob.com/wp-content/uploads/2018/09/1536322989-1775-ij-run-app.jpg)


你将会在 IntelliJ IDEA 的终端下看到如下运行结果：


```
"C:\Program Files\Java\jdk1.6.0_21\bin\java"
-Didea.launcher.port=7533
"-Didea.launcher.bin.path=
C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 11.1.2\bin"
-Dfile.encoding=UTF-8
-classpath "C:\Program Files\Java\jdk1.6.0_21\jre\lib\charsets.jar;
C:\Program Files\Java\jdk1.6.0_21\jre\lib\deploy.jar;
C:\Program Files\Java\jdk1.6.0_21\jre\lib\javaws.jar;
C:\Program Files\Java\jdk1.6.0_21\jre\lib\jce.jar;
C:\Program Files\Java\jdk1.6.0_21\jre\lib\jsse.jar;
C:\Program Files\Java\jdk1.6.0_21\jre\lib\management-agent.jar;
C:\Program Files\Java\jdk1.6.0_21\jre\lib\plugin.jar;
C:\Program Files\Java\jdk1.6.0_21\jre\lib\resources.jar;
C:\Program Files\Java\jdk1.6.0_21\jre\lib\rt.jar;
C:\Program Files\Java\jdk1.6.0_21\jre\lib\ext\dnsns.jar;
C:\Program Files\Java\jdk1.6.0_21\jre\lib\ext\localedata.jar;
C:\Program Files\Java\jdk1.6.0_21\jre\lib\ext\sunjce_provider.jar;
C:\Program Files\Java\jdk1.6.0_21\jre\lib\ext\sunmscapi.jar;
C:\Program Files\Java\jdk1.6.0_21\jre\lib\ext\sunpkcs11.jar
C:\MVN\consumerBanking\target\classes;
C:\Program Files\JetBrains\
IntelliJ IDEA Community Edition 11.1.2\lib\idea_rt.jar"
com.intellij.rt.execution.application.AppMain com.companyname.bank.App
Hello World!
Process finished with exit code 0
```









	  AI 思考中...





			** [Maven NetBeans](https://www.runoob.com/maven-netbeans.html)
			[Maven 简介](https://www.runoob.com/maven-intro.html) **













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