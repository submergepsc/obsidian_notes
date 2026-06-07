# Maven 常用命令

- Source: https://www.runoob.com/maven/maven-commands.html

Maven 命令遵循以下模式：


```
mvn [选项] [生命周期阶段] [目标]
```


### 检查 Maven 版本


## 实例


```java
mvn -v
```


这个命令会显示已安装的 Maven 版本、Java 版本等信息。


---


## Maven 生命周期命令


Maven 基于构建生命周期的概念，包含三个主要的生命周期：


- clean：清理项目
- default (build)：项目构建
- site：生成项目文档


### 清理项目


## 实例


```java
mvn clean
```


这个命令会删除 `target` 目录，即删除所有构建生成的文件。


### 编译项目


## 实例


```java
mvn compile
```


编译源代码，编译后的 class 文件会放在 `target/classes` 目录下。


### 运行测试


## 实例


```java
mvn test
```


运行项目中的所有测试用例。


### 打包项目


## 实例


```java
mvn package
```


根据 POM 文件中指定的打包类型（如 jar、war）打包项目。


### 安装到本地仓库


## 实例


```java
mvn install
```


将项目构建并安装到本地 Maven 仓库，供其他项目依赖使用。


### 部署到远程仓库


## 实例


```java
mvn deploy
```


将最终的项目包复制到远程仓库，供其他开发人员和项目使用。


---


## 依赖管理命令


### 查看项目依赖树


## 实例


```java
mvn dependency:tree
```


显示项目的依赖树，有助于分析依赖关系和解决依赖冲突。


### 下载源代码


## 实例


```java
mvn dependency:sources
```


下载项目依赖的源代码。


### 分析依赖


## 实例


```java
mvn dependency:analyze
```


分析项目中使用但未声明的依赖，以及声明但未使用的依赖。


---


## 项目创建命令


### 创建简单项目


## 实例


```java
mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```


使用 Maven 原型系统创建一个简单的 Java 项目。


### 创建 Web 项目


## 实例


```java
mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-web-app -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
```


创建一个简单的 Web 应用程序项目。


---


## 其他实用命令


### 跳过测试


## 实例


```java
mvn install -DskipTests
```


构建项目并安装到本地仓库，但跳过测试阶段。


### 运行特定测试


## 实例


```java
mvn test -Dtest=TestClassName
```


只运行指定的测试类。


## 实例


```java
mvn test -Dtest=TestClassName#testMethodName
```


只运行指定测试类中的特定测试方法。


### 更新依赖


## 实例


```java
mvn versions:display-dependency-updates
```


检查项目中哪些依赖有更新的版本可用。


### 生成站点文档


## 实例


```java
mvn site
```


生成项目的站点文档，包括各种报告。


### 运行特定阶段


## 实例


```java
mvn clean package
```


先执行 clean 生命周期，然后执行 default 生命周期到 package 阶段。


---


## Maven 命令组合使用


Maven 命令可以组合使用以提高效率：


## 实例


```java
mvn clean install
```


先清理项目，然后编译、测试并安装到本地仓库。


## 实例


```java
mvn clean package -DskipTests
```


清理项目，打包但不运行测试。


---


## 常见问题解决


### 强制更新快照依赖


## 实例


```java
mvn clean install -U
```


`-U` 参数强制 Maven 检查远程仓库中依赖的更新版本。


### 离线模式


## 实例


```java
mvn -o package
```


`-o` 参数让 Maven 在离线模式下运行，只使用本地仓库中的依赖。


### 调试模式


## 实例


```java
mvn -X clean install
```


`-X` 参数启用调试输出，显示详细的执行信息。


---


## 基础构建命令


| 命令 | 作用 | 执行的生命周期阶段 |
| --- | --- | --- |
| mvn clean | 删除target/目录 | clean |
| mvn validate | 验证项目是否正确 | validate |
| mvn compile | 编译主源代码 | compile |
| mvn test-compile | 编译测试代码 | test-compile |
| mvn test | 运行单元测试 | test |
| mvn package | 打包项目 | package |
| mvn verify | 运行集成测试 | verify |
| mvn install | 安装到本地仓库 | install |
| mvn deploy | 部署到远程仓库 | deploy |


典型开发流程:


```
mvn clean compile test package
```


---


## 依赖管理命令


| 命令 | 作用 |
| --- | --- |
| mvn dependency:tree | 显示依赖树 |
| mvn dependency:analyze | 分析依赖问题 |
| mvn dependency:copy-dependencies | 复制依赖到目录 |
| mvn dependency:purge-local-repository | 清除本地依赖缓存 |
| mvn versions:display-dependency-updates | 检查依赖更新 |


```
# 查看依赖树
mvn dependency:tree

# 检查可用更新
mvn versions:display-dependency-updates
```


---


## 插件相关命令

| 命令 | 作用 |
| --- | --- |
| mvn help:describe -Dplugin=插件名 | 查看插件信息 |
| mvn help:effective-pom | 查看最终生效的POM |
| mvn 插件前缀:目标 | 直接运行插件目标 |


```
# 查看compiler插件信息
mvn help:describe -Dplugin=compiler

# 直接运行compiler插件的compile目标
mvn compiler:compile
```


---


## 测试相关命令

| 命令 | 作用 |
| --- | --- |
| mvn test | 运行所有测试 |
| mvn -Dtest=测试类名 test | 运行指定测试类 |
| mvn -Dtest=测试类名#方法名 test | 运行指定测试方法 |
| mvn -DskipTests=true package | 跳过测试 |


```
# 只运行UserServiceTest类
mvn -Dtest=UserServiceTest test

# 只运行UserServiceTest中的testCreate方法
mvn -Dtest=UserServiceTest#testCreate test
```


---


## 多模块项目命令

| 命令 | 作用 |
| --- | --- |
| mvn -pl 模块名 命令 | 对指定模块执行命令 |
| mvn -am -pl 模块名 命令 | 执行命令并处理依赖模块 |
| mvn -rf 模块名 命令 | 从指定模块继续执行 |


```
# 只编译service模块
mvn -pl service compile

# 编译web模块及其依赖的模块
mvn -am -pl web compile
```


---


## 高级用法

| 命令 | 作用 |
| --- | --- |
| mvn -T 4 install | 使用4个线程并行构建 |
| mvn -o package | 离线模式运行 |
| mvn -X clean install | 开启调试输出 |
| mvn -U clean install | 强制更新snapshot依赖 |
| mvn release:prepare | 准备项目发布 |
| mvn release:perform | 执行项目发布 |


```
# 并行构建(4线程)
mvn -T 4 clean install

# 强制更新snapshot依赖
mvn -U clean install
```


---


## 常用命令组合

| 组合命令 | 作用 |
| --- | --- |
| mvn clean install | 清理后重新安装 |
| mvn clean package -DskipTests | 清理后打包并跳过测试 |
| mvn clean test | 清理后运行测试 |
| mvn clean deploy | 清理后部署 |


---


## 实用技巧


快速查看项目信息：


```
mvn help:effective-pom
mvn help:describe -Dcmd=compile
```


调试构建问题：


```
mvn -X clean install
```


跳过检查：


```
mvn install -Dcheckstyle.skip=true -Dpmd.skip=true
```


指定配置文件：


```
mvn install -P production
```


查看构建时间：


```
mvn install --batch-mode | grep "Total time"
```









	  AI 思考中...





			** [Maven 第一个项目](https://www.runoob.com/maven-start.html)
			[Maven 依赖机制](https://www.runoob.com/maven-dependencies.html) **













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