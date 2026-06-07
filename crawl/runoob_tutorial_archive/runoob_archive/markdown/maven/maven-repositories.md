# Maven 仓库

- Source: https://www.runoob.com/maven/maven-repositories.html

在 Maven 的术语中，仓库是一个位置（place）。


Maven 仓库是项目中依赖的第三方库，这个库所在的位置叫做仓库。


在 Maven 中，任何一个依赖、插件或者项目构建的输出，都可以称之为构件。


Maven 仓库能帮助我们管理构件（主要是 JAR），它就是放置所有 JAR 文件（WAR，ZIP，POM 等等）的地方。


Maven 仓库类型：


| 仓库类型 | 存储位置 | 作用 | 访问优先级 |
| --- | --- | --- | --- |
| 本地仓库 | 用户目录下的.m2/repository | 缓存远程下载的依赖 | 1 |
| 远程仓库 | 网络服务器 | 提供依赖和插件的集中存储 | 2 |
| - 中央仓库 | repo.maven.apache.org | Maven官方维护的默认仓库 | 2.1 |
| - 私服仓库 | 公司内部搭建（如Nexus） | 托管私有依赖，加速构建 | 2.2 |
| - 其他公共仓库 | 如阿里云、JCenter等 | 镜像或补充中央仓库 | 2.3 |


---

## 本地仓库


Maven 的本地仓库，在安装 Maven 后并不会创建，它是在第一次执行 maven 命令的时候才被创建。


运行 Maven 的时候，Maven 所需要的任何构件都是直接从本地仓库获取的。如果本地仓库没有，它会首先尝试从远程仓库下载构件至本地仓库，然后再使用本地仓库的构件。


默认情况下，不管 Linux 还是 Windows，每个用户在自己的用户目录下都有一个路径名为 .m2/repository/ 的仓库目录。


- Windows: `C:\Users\\.m2\repository`
- Linux/macOS: `~/.m2/repository`


Maven 本地仓库默认被创建在 %USER_HOME% 目录下。要修改默认位置，在 %M2_HOME%\conf 目录中的 Maven 的 settings.xml 文件中定义另一个路径。


```java
<settings>
      <localRepository>C:/MyLocalRepository</localRepository>
</settings>
```


当你运行 Maven 命令，Maven 将下载依赖的文件到你指定的路径中。


清理本地仓库:


```
mvn dependency:purge-local-repository
# 或手动删除~/.m2/repository目录
```


---

## 中央仓库


Maven 中央仓库是由 Maven 社区提供的仓库，其中包含了大量常用的库。


中央仓库包含了绝大多数流行的开源 Java 构件，以及源码、作者信息、SCM、信息、许可证信息等。一般来说，简单的 Java 项目依赖的构件都可以在这里下载到。


中央仓库的关键概念：


- 这个仓库由 Maven 社区管理。
- 不需要配置。
- 需要通过网络才能访问。

中央仓库（无需显式配置）默认地址：[https://repo.maven.apache.org/maven2/](https://repo.maven.apache.org/maven2/)


---

## 远程仓库


### 自定义仓库配置


如果 Maven 在中央仓库中也找不到依赖的文件，它会停止构建过程并输出错误信息到控制台。为避免这种情况，Maven 提供了远程仓库的概念，它是开发人员自己定制仓库，包含了所需要的代码库或者其他工程中用到的 jar 文件。


举例说明，使用下面的 pom.xml，Maven 将从远程仓库中下载该 pom.xml 中声明的所依赖的（在中央仓库中获取不到的）文件。


## 实例


```java
<repositories>
    <repository>
        <id>aliyun</id>
        <name>Aliyun Maven</name>
        <url>https://maven.aliyun.com/repository/public</url>
        <releases>
            <enabled>true</enabled>
        </releases>
        <snapshots>
            <enabled>false</enabled> <!-- 禁用SNAPSHOT版本 -->
        </snapshots>
    </repository>
</repositories>
```


### 镜像仓库（推荐）


在 settings.xml 中配置：


## 实例


```java
<mirrors>
    <mirror>
        <id>aliyun</id>
        <name>Aliyun Mirror</name>
        <url>https://maven.aliyun.com/repository/public</url>
        <mirrorOf>central</mirrorOf> <!-- 覆盖中央仓库 -->
    </mirror>
</mirrors>
```


---

## Maven 阿里云(Aliyun)仓库


Maven 仓库默认在国外， 国内使用难免很慢，我们可以更换为阿里云的仓库。


修改 maven 根目录下的 conf 文件夹中的 settings.xml 文件，在 mirrors 节点上，添加内容如下：


```java
<mirror>
  <id>aliyunmaven</id>
  <mirrorOf>*</mirrorOf>
  <name>阿里云公共仓库</name>
  <url>https://maven.aliyun.com/repository/public</url>
</mirror>
```


如果想使用其它代理仓库，可在 **** 节点中加入对应的仓库使用地址。以使用 spring 代理仓为例：


```java
<repository>
  <id>spring</id>
  <url>https://maven.aliyun.com/repository/spring</url>
  <releases>
    <enabled>true</enabled>
  </releases>
  <snapshots>
    <enabled>true</enabled>
  </snapshots>
</repository>
```


在你的 pom.xml 文件 **** 节点中加入你要引用的文件信息：


```java
<dependency>
  <groupId>[GROUP_ID]</groupId>
  <artifactId>[ARTIFACT_ID]</artifactId>
  <version>[VERSION]</version>
</dependency>
```


执行拉取命令：


```
mvn install
```


### gradle 配置指南


在 build.gradle 文件中加入以下代码:


```java
allprojects {
  repositories {
    maven {
      url 'https://maven.aliyun.com/repository/public/'
    }
    mavenLocal()
    mavenCentral()
  }
}
```


如果想使用其它代理仓，以使用spring仓为例，代码如下:


```java
allProjects {
  repositories {
    maven {
      url 'https://maven.aliyun.com/repository/public/'
    }
    maven {
      url 'https://maven.aliyun.com/repository/spring/'
    }
    mavenLocal()
    mavenCentral()
  }
}
```


加入你要引用的文件信息：


```java
dependencies {
  compile '[GROUP_ID]:[ARTIFACT_ID]:[VERSION]'
}
```


执行以下命令安装依赖：


```
gradle dependencies
或
./gradlew dependencies
```


---


## 私服仓库


仓库类型：


| 仓库类型 | 用途 |
| --- | --- |
| hosted | 存放私有构件 |
| proxy | 代理远程仓库 |
| group | 聚合多个仓库 |


### 发布到私服


在 pom.xml 中配置：


```
<distributionManagement>
    <repository>
        <id>nexus-releases</id>
        <url>http://your-nexus/repository/maven-releases</url>
    </repository>
    <snapshotRepository>
        <id>nexus-snapshots</id>
        <url>http://your-nexus/repository/maven-snapshots</url>
    </snapshotRepository>
</distributionManagement>
```


在 settings.xml 中配置认证：


```
<servers>
    <server>
        <id>nexus-releases</id>
        <username>deploy-user</username>
        <password>deploy-pwd</password>
    </server>
</servers>
```


发布命令：


```
mvn deploy
```


---


## Maven 依赖搜索顺序


当我们执行 Maven 构建命令时，Maven 开始按照以下顺序查找依赖的库：


- **步骤 1** － 在本地仓库中搜索，如果找不到，执行步骤 2，如果找到了则执行其他操作。
- **步骤 2** － 在中央仓库中搜索，如果找不到，并且有一个或多个远程仓库已经设置，则执行步骤 4，如果找到了则下载到本地仓库中以备将来引用。
- **步骤 3** － 如果远程仓库没有被设置，Maven 将简单的停滞处理并抛出错误（无法找到依赖的文件）。
- **步骤 4** － 在一个或多个远程仓库中搜索依赖的文件，如果找到则下载到本地仓库以备将来引用，否则 Maven 将停止处理并抛出错误（无法找到依赖的文件）。


### 常用命令

| 命令 | 作用 |
| --- | --- |
| mvn dependency:resolve | 解析依赖 |
| mvn dependency:tree | 查看依赖树 |
| mvn dependency:purge-local-repository | 清理本地仓库 |
| mvn deploy | 发布到远程仓库 |


### 常见问题解决


**1、依赖下载失败现象：**Could not transfer artifact...


**解决：**

- 检查网络连接
- 验证仓库URL是否正确
- 临时关闭防火墙测试


**2、认证失败现象：**401 Unauthorized


**解决：**


- 检查 settings.xml 中的  配置
- 确认用户名/密码是否有仓库访问权限


**3、依赖冲突**


** 排查：**


```
mvn dependency:tree -Dverbose
```


**解决：在  中统一版本**








	  AI 思考中...





			** [Maven 构建配置文件](https://www.runoob.com/maven-build-profiles.html)
			[Maven 插件](https://www.runoob.com/maven-plugins.html) **













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