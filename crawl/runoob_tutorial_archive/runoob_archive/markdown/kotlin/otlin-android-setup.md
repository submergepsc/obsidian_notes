# Kotlin Android 环境搭建

- Source: https://www.runoob.com/kotlin/otlin-android-setup.html

## 安装 Kotlin 插件


Android Studio 从 3.0（preview）版本开始将内置安装 Kotlin 插件。


打开 Settings ( Mac 为 Preferences) 面板，在右侧找到 Plugins 选项 (快捷键 Ctrl+, Mac 下为 command+)，搜索框输入 "Kotlin" 查找，点击 Search in repositories(仓库中搜索)，然后安装即可，安装完成之后需要重启 Android Studio。


![](https://www.runoob.com/wp-content/uploads/2017/05/1495852874-4548-qiddj00bpde497.png)


![](https://www.runoob.com/wp-content/uploads/2017/05/1495852999-3315-qqf4ub25vet500.png)


---


## 创建新工程


选择 Start a new Android Studio project 或者 File | New project，大多数选项均有默认值 ，只需要按几次"回车"键即可。

![](https://www.runoob.com/wp-content/uploads/2017/05/1495853720-4994-0-create-new-project.png)

Android Studio 3.0 在当前对话框中提供启用 Kotlin 支持的选项，勾选后可以跳过 "配置 Kotlin 工程（Configuring Kotlin in the project）"的步骤。


选择 Android 版本:


![](https://www.runoob.com/wp-content/uploads/2017/05/1495853670-8308-1-create-new-project.png)


选择需要创建的 Activity 样式:


![](https://www.runoob.com/wp-content/uploads/2017/05/1495853838-1520-0-create-new-project.png)


命名该 Activity:


![](https://www.runoob.com/wp-content/uploads/2017/05/1495853838-8955-1-create-new-project.png)


在 Android Studio 3.0 中，可以选择使用 Kotlin 创建 activity，因此也不需要"将Java 代码转换为 Kotlin（Converting Java code to Kotlin）"这一步骤。

早期版本中则会先使用 Java 创建 activity，然后再使用自动转换工具 进行转换。


---


## 将 Java 代码转换为 Kotlin


重新打开Android Studio，新建一个Android项目吧，添加一个默认的MainActivity


打开 MainActivity.java 文件，通过菜单栏依次调出 Code | Convert Java File to Kotlin File：


![](https://www.runoob.com/wp-content/uploads/2017/05/1495854751-7389-convert-java-to-kotlin.png)


转换完成后即可看到使用 Kotlin 编写的 activity。


![](https://www.runoob.com/wp-content/uploads/2017/05/1495854753-3864-converted-code.png)


### 工程中配置 Kotlin


在开始编辑此文件时，Android Studio 会提示当前工程还未配置 Kotlin，根据提示完成操作即可，或者可以在菜单栏中选择 Tools


![](https://www.runoob.com/wp-content/uploads/2017/05/1495854757-6620-kotlin-not-configured.png)


选择配置时有如下对话框，选择已安装的最新版本即可。


![](https://www.runoob.com/wp-content/uploads/2017/05/1495854752-7001-re-kotlin-in-project-details.png)


Kotlin 配置完成后，应用程序的 build.gradle 文件会更新。 你能看到新增了 apply plugin: 'kotlin-android' 及其依赖。


![](https://www.runoob.com/wp-content/uploads/2017/05/1495854750-1825-sync-project-with-gradle.png)


同步工程，在提示框中点击"立即同步（Sync Now）"或者使用 Sync Project with Gradle Files命令。

![](https://www.runoob.com/wp-content/uploads/2017/05/1495854764-6190-sync-project-with-gradle-2.png)








	  AI 思考中...





			** [Kotlin 使用命令行编译](https://www.runoob.com/kotlin-command-line.html)
			[Kotlin 基础语法](https://www.runoob.com/kotlin-basic-syntax.html) **













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