# Maven 简介

- Source: https://www.runoob.com/maven/maven-intro.html

Maven 是一个 项目管理与构建自动化工具，主要用于 Java 项目，但也可用于其他语言（如 Kotlin、Scala）。


Maven 解决了软件构建的两方面问题：

- 一是软件是如何构建的。
- 二是软件的依赖关系。


![](https://www.runoob.com/wp-content/uploads/2025/05/Apache_Maven_logo.svg.png)


Maven 的核心功能包括：


- **项目构建**（编译、测试、打包、部署）
- **依赖管理**（自动下载和管理第三方库）
- **标准化项目结构**（约定优于配置）
- **插件扩展**（支持自定义构建流程）


### Maven 的发展历史


- **2002年**：Maven 由 **Jason van Zyl** 创建，用于替代 Apache Ant（Ant 需要手动编写构建脚本，而 Maven 提供标准化流程）。
- **2004年**：Maven 1.0 发布。
- **2005年**：Maven 2.0 引入 **POM（Project Object Model）** 和 **依赖管理**。
- **2010年**：Maven 3.0 发布，优化性能并改进 API。
- **现在**：Maven 仍然是 Java 生态中最流行的构建工具之一，与 Gradle 共同主导市场。


### Maven 的主要功能和优势


| 功能 | 说明 |
| --- | --- |
| 依赖管理 | 自动下载和管理 .jar 文件，避免手动管理依赖 |
| 标准化构建流程 | 提供 clean、compile、test、package 等标准生命周期 |
| 项目模板（Archetype） | 快速生成项目结构（如 maven-archetype-quickstart） |
| 多模块支持 | 适用于大型项目，可以拆分为多个子模块 |
| 插件扩展 | 支持自定义构建任务（如 maven-compiler-plugin 指定 Java 版本） |


**优势：**


- **减少配置**：约定优于配置，减少 `build.xml`（Ant）这样的手动配置。
- **依赖自动管理**：只需声明依赖，Maven 自动下载并处理冲突。
- **跨平台**：基于 Java，可在 Windows、Linux、macOS 上运行。
- **与 IDE 集成**：Eclipse、IntelliJ IDEA、VS Code 都支持 Maven。


### Maven vs. 其他构建工具


| 工具 | 特点 | 适用场景 |
| --- | --- | --- |
| Maven | 基于 XML 配置，依赖管理强，标准化构建流程 | 传统 Java 项目，需要稳定依赖管理 |
| Gradle | 基于 Groovy/Kotlin DSL，构建脚本更灵活，性能更好 | Android、Kotlin 项目，需要自定义构建流程 |
| Ant | 基于 XML，手动编写构建步骤，灵活性高 | 遗留项目，需要精细控制构建过程 |








	  AI 思考中...





			** [Maven IntelliJ](https://www.runoob.com/maven-intellij.html)
			[Maven 第一个项目](https://www.runoob.com/maven-start.html) **













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