# Maven 依赖机制

- Source: https://www.runoob.com/maven/maven-dependencies.html

Maven 依赖机制是 Apache Maven 构建工具的核心功能之一，它能够自动下载和管理项目所需的外部库（JAR 文件）及其依赖关系。


Maven 依赖机制极大地简化了 Java 项目的构建过程，使开发者无需手动下载和管理各种第三方库。


Maven 通过中央仓库（Maven Central Repository）存储了数百万个开源库，当你在项目中声明某个依赖时，Maven 会自动从仓库中下载该库及其所有依赖项。


### 依赖声明方式

在 pom.xml 中通过  标签声明：


```
<dependencies>
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.12</version>
    </dependency>
</dependencies>
```


---


## Maven 依赖的基本概念


### 1. 坐标系统 (Coordinates)


Maven 使用三个基本坐标来唯一标识一个依赖项：


- **groupId**：定义项目所属的组织或公司（如 `org.apache`）
- **artifactId**：定义项目的名称（如 `commons-lang3`）
- **version**：定义项目的版本（如 `3.12.0`）


这三个元素组合起来形成了 Maven 依赖的唯一标识符。


### 2. 依赖范围 (Scope)


Maven 定义了不同的依赖范围，决定了依赖在哪些阶段可用：


- **compile**（默认）：编译、测试和运行时都可用
- **provided**：编译和测试时可用，但运行时由 JDK 或容器提供
- **runtime**：只在测试和运行时需要
- **test**：仅在测试编译和执行阶段需要
- **system**：类似于 provided，但需要显式指定 JAR 路径


### 3. 传递性依赖 (Transitive Dependencies)


当项目 A 依赖项目 B，而项目 B 又依赖项目 C 时，Maven 会自动将项目 C 也作为项目 A 的依赖引入。这种自动处理依赖关系的特性称为传递性依赖。


传递规则取决于 Scope：

| 当前依赖Scope \ 传递依赖Scope | compile | provided | runtime | test |
| --- | --- | --- | --- | --- |
| compile | compile | - | runtime | - |
| provided | provided | provided | provided | - |
| runtime | runtime | - | runtime | - |
| test | - | - | - | - |


---


## 如何在项目中使用 Maven 依赖


### 1. 在 pom.xml 中添加依赖


在 Maven 项目的 `pom.xml` 文件中，`` 部分用于声明项目依赖：


## 实例


```java
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-lang3</artifactId>
        <version>3.12.0</version>
    </dependency>
</dependencies>
```


### 2. 依赖排除 (Exclusions)


有时你可能需要排除某个传递性依赖，可以使用 `` 标签：


## 实例


```java
<dependency>
    <groupId>com.example</groupId>
    <artifactId>example-library</artifactId>
    <version>1.0</version>
    <exclusions>
        <exclusion>
            <groupId>org.unwanted</groupId>
            <artifactId>unwanted-dependency</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```


### 3. 依赖管理 (Dependency Management)


在多模块项目中，可以在父 POM 中使用 `` 统一管理依赖版本：


## 实例


```java
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <version>5.3.20</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```


子模块引用时只需声明 groupId 和 artifactId，无需指定版本。


---


## 依赖管理高级特性


### 依赖版本管理

使用 **dependencyManagement** 统一管理版本：


```
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <version>5.3.18</version>
        </dependency>
    </dependencies>
</dependencyManagement>

<!-- 子模块使用时无需指定版本 -->
<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-core</artifactId>
    </dependency>
</dependencies>
```


### BOM 导入

管理一组相关依赖的版本：


```
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-dependencies</artifactId>
            <version>2.6.4</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```


### 可选依赖（Optional）

标记依赖为可选，不传递：


```
<dependency>
    <groupId>com.example</groupId>
    <artifactId>optional-lib</artifactId>
    <version>1.0</version>
    <optional>true</optional>
</dependency>
```


---


## Maven 依赖解析机制


### 1. 依赖调解 (Dependency Mediation)


当出现版本冲突时，Maven 使用以下规则解决：


- 最近定义优先（在依赖树中路径最短的版本被选中）
- 如果路径长度相同，则先声明的依赖优先


### 2. 依赖范围影响


不同范围的依赖会影响传递性：


- compile 范围的依赖会传递
- provided 和 test 范围的依赖不会传递
- runtime 范围的依赖会以 runtime 范围传递


不同 Scope 的依赖最终打包结果：


| Scope | 是否打包 | 典型应用 |
| --- | --- | --- |
| compile | 是 | 核心依赖 |
| provided | 否 | 容器提供 |
| runtime | 是 | 运行时需要 |
| test | 否 | 单元测试 |


### 3. 可选依赖 (Optional Dependencies)


标记为 optional 的依赖不会传递：


## 实例


```java
<dependency>
    <groupId>com.example</groupId>
    <artifactId>optional-lib</artifactId>
    <version>1.0</version>
    <optional>true</optional>
</dependency>
```


---


## 依赖相关命令

查看依赖树:


```
mvn dependency:tree
```


分析依赖问题:


```
mvn dependency:analyze
```


下载依赖到目录:


```
mvn dependency:copy-dependencies
```


---


## Maven 仓库 (Repository)


### 1. 仓库类型


- **本地仓库**：位于用户主目录下的 `.m2/repository` 目录
- **中央仓库**：Maven 默认的公共仓库
- **远程仓库**：公司或组织搭建的私有仓库


### 2. 仓库配置


可以在 `pom.xml` 或 `settings.xml` 中配置仓库：


## 实例


```java
<repositories>
    <repository>
        <id>my-repo</id>
        <url>http://repo.example.com/maven2</url>
    </repository>
</repositories>
```


---


## 最佳实践


- **明确指定依赖版本**：避免使用 LATEST 或 RELEASE 等动态版本
- **定期更新依赖**：使用 `mvn versions:display-dependency-updates` 检查可用更新
- **使用 BOM**：对于大型框架（如 Spring），使用 Bill of Materials 统一管理版本
- **清理无用依赖**：定期运行 `mvn dependency:analyze` 检查未使用的依赖









	  AI 思考中...





			** [Maven 常用命令](https://www.runoob.com/maven-commands.html)
			[Maven 多模块项目管理](https://www.runoob.com/maven-multi-module.html) **













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