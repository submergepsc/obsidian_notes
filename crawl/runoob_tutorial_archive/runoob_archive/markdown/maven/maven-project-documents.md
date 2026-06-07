# Maven 项目文档

- Source: https://www.runoob.com/maven/maven-project-documents.html

本章节我们主要学习如何创建 Maven 项目文档。


比如我们在 C:/MVN 目录下，创建了 consumerBanking 项目，Maven 使用下面的命令来快速创建 java 项目：


```
mvn archetype:generate -DgroupId=com.companyname.bank -DartifactId=consumerBanking -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```


修改 pom.xml，添加以下配置（如果没有的话）：


```java
<project>
  ...
<build>
<pluginManagement>
    <plugins>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-site-plugin</artifactId>
          <version>3.3</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-project-info-reports-plugin</artifactId>
          <version>2.7</version>
        </plugin>
    </plugins>
    </pluginManagement>
</build>
 ...
</project>
```


**
不然运行** mvn site** 命令时出现 java.lang.NoClassDefFoundError: org/apache/maven/doxia/siterenderer/DocumentContent** 的问题， 这是由于 maven-site-plugin 版本过低，升级到 3.3+ 即可。


打开 consumerBanking 文件夹并执行以下 mvn 命令。


```
C:\MVN\consumerBanking> mvn site
```


Maven 开始生成文档：


```
[INFO] Scanning for projects...
[INFO] -------------------------------------------------------------------
[INFO] Building consumerBanking
[INFO]task-segment: [site]
[INFO] -------------------------------------------------------------------
[INFO] [site:site {execution: default-site}]
[INFO] artifact org.apache.maven.skins:maven-default-skin:
checking for updates from central
[INFO] Generating "About" report.
[INFO] Generating "Issue Tracking" report.
[INFO] Generating "Project Team" report.
[INFO] Generating "Dependencies" report.
[INFO] Generating "Continuous Integration" report.
[INFO] Generating "Source Repository" report.
[INFO] Generating "Project License" report.
[INFO] Generating "Mailing Lists" report.
[INFO] Generating "Plugin Management" report.
[INFO] Generating "Project Summary" report.
[INFO] -------------------------------------------------------------------
[INFO] BUILD SUCCESSFUL
[INFO] -------------------------------------------------------------------
[INFO] Total time: 16 seconds
[INFO] Finished at: Wed Jul 11 18:11:18 IST 2012
[INFO] Final Memory: 23M/148M
[INFO] -------------------------------------------------------------------
```


![](https://www.runoob.com/wp-content/uploads/2018/09/12-site-project-structure.jpg)


打开 **C:\MVN\consumerBanking\target\site** 文件夹。点击 **index.html** 就可以看到文档了。


![](https://www.runoob.com/wp-content/uploads/2018/09/12-consumer-web-page.jpg)


Maven 使用一个名为 [Doxia](http://maven.apache.org/doxia/index.html)的文档处理引擎来创建文档，它能将多种格式的源码读取成一种通用的文档模型。要为你的项目撰写文档，你可以将内容写成下面几种常用的，可被 Doxia 转化的格式。


| 格式名 | 描述 | 参考 |
| --- | --- | --- |
| Apt | 纯文本文档格式 | http://maven.apache.org/doxia/references/apt-format.html |
| Xdoc | Maven 1.x 的一种文档格式 | http://jakarta.apache.org/site/jakarta-site2.html |
| FML | FAQ 文档适用 | http://maven.apache.org/doxia/references/fml-format.html |
| XHTML | 可扩展的 HTML 文档 | http://en.wikipedia.org/wiki/XHTML |








	  AI 思考中...





			** [Maven 项目模板](https://www.runoob.com/project-templates.html)
			[Maven 快照(SNAPSHOT)](https://www.runoob.com/maven-snapshots.html) **













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