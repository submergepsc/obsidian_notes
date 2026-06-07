# 

- Source: https://www.runoob.com/maven/maven-start.html

Maven 第一个项目


## 创建 Maven 项目


### 使用 Maven Archetype 生成项目

Maven 提供了项目模板（Archetype），可以快速生成标准项目结构。最常用的是 maven-archetype-quickstart（基础 Java 项目模板）。


执行命令：


```
mvn archetype:generate \
    -DgroupId=com.example \
    -DartifactId=my-first-app \
    -DarchetypeArtifactId=maven-archetype-quickstart \
    -DinteractiveMode=false
```


**参数说明：**


| 参数 | 说明 |
| --- | --- |
| -DgroupId | 组织名（如公司域名倒写） |
| -DartifactId | 项目名称（会成为项目文件夹名） |
| -DarchetypeArtifactId | 使用的模板（quickstart 是基础 Java 项目） |
| -DinteractiveMode=false | 非交互模式（避免手动确认） |


执行后生成的项目结构：


```
my-first-app/
├── pom.xml           # Maven 项目配置文件
├── src/
│   ├── main/         # 主代码目录
│   │   └── java/     # Java 源代码
│   │       └── com/example/App.java  # 自动生成的示例类
│   └── test/        # 测试代码目录
│       └── java/     # 测试类
│           └── com/example/AppTest.java  # 自动生成的测试类
```


---


## 项目结构解析


### pom.xml 详解

这是 Maven 的核心配置文件，定义了项目的基本信息和依赖。


生成的 pom.xml 示例：


```
<project>
    <!-- POM 模型版本，固定 4.0.0 -->
    <modelVersion>4.0.0</modelVersion>

    <!-- 项目坐标（唯一标识） -->
    <groupId>com.example</groupId>
    <artifactId>my-first-app</artifactId>
    <version>1.0-SNAPSHOT</version>

    <!-- 项目打包方式（默认 jar，也可以是 war、pom 等） -->
    <packaging>jar</packaging>

    <!-- 项目名称和 URL（可选） -->
    <name>my-first-app</name>
    <url>http://www.example.com</url>

    <!-- 依赖管理 -->
    <dependencies>
        <!-- JUnit 测试依赖 -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
            <scope>test</scope>  <!-- 仅用于测试 -->
        </dependency>
    </dependencies>
</project>
```


### 源代码结构

| 目录 | 作用 |
| --- | --- |
| src/main/java | 主 Java 源代码 |
| src/main/resources | 配置文件（如 application.properties） |
| src/test/java | 测试代码 |
| src/test/resources | 测试资源文件 |


### 示例代码：


**主类 App.java**


## 实例


```java
package com.example;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello Maven!");
    }
}
```


**测试类 AppTest.java:**


## 实例


```java
package com.example;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {
    @Test
    public void testApp() {
        assertTrue(true);  // 示例测试
    }
}
```


---


## 构建与运行


### 常用 Maven 命令

| 命令 | 作用 |
| --- | --- |
| mvn compile | 编译源代码 |
| mvn test | 运行测试 |
| mvn package | 打包（生成 .jar 文件） |
| mvn install | 安装到本地仓库（供其他项目依赖） |
| mvn clean | 清理 target 目录 |


### 完整构建流程


1、编译项目：


```
mvn compile
```


编译后的 .class 文件会放在 target/classes 目录。


2、运行测试：


```
mvn test
```


执行 src/test/java 下的测试类。


测试报告生成在 target/surefire-reports。

3、打包：


```
mvn package
```


生成 target/my-first-app-1.0-SNAPSHOT.jar。


4、运行程序：


```
java -cp target/my-first-app-1.0-SNAPSHOT.jar com.example.App
```


5、输出：


```
Hello Maven!
```


---


## 扩展：修改项目


### 添加依赖

例如，添加 [Gson](https://www.runoob.com/../java/java-gson-lib.html) 用于 JSON 处理：


修改 pom.xml：


```
<dependencies>
    <!-- 原有 JUnit 依赖 -->
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.12</version>
        <scope>test</scope>
    </dependency>

    <!-- 新增 Gson 依赖 -->
    <dependency>
        <groupId>com.google.code.gson</groupId>
        <artifactId>gson</artifactId>
        <version>2.8.9</version>
    </dependency>
</dependencies>
```


运行 mvn compile，Maven 会自动下载 Gson。


### 修改主类使用 Gson


## 实例


```java
package com.example;

import com.google.gson.Gson;

public class App {
    public static void main(String[] args) {
        Gson gson = new Gson();
        String json = gson.toJson("Hello Maven with Gson!");
        System.out.println(json);
    }
}
```


重新打包并运行：


```
mvn package
java -cp target/my-first-app-1.0-SNAPSHOT.jar com.example.App
```


输出：


```
"Hello Maven with Gson!"
```


---


## 常见问题


### 依赖下载失败


原因：网络问题或仓库不可用。


**解决方案：**


检查网络连接。


配置国内镜像仓库（如阿里云）：


```
<!-- 在 settings.xml 或 pom.xml 中配置 -->
<mirror>
    <id>aliyun</id>
    <url>https://maven.aliyun.com/repository/public</url>
    <mirrorOf>central</mirrorOf>
</mirror>
```


阿里云仓库介绍：[https://developer.aliyun.com/mvn/guide](https://developer.aliyun.com/mvn/guide)。


### 编译版本问题

错误：javac: invalid target release: 11


解决方案：在 pom.xml 中指定 Java 版本：


```
<properties>
    <maven.compiler.source>11</maven.compiler.source>
    <maven.compiler.target>11</maven.compiler.target>
</properties>
```


---


## 总结


- **创建项目**：`mvn archetype:generate` 生成标准结构。
- **项目结构**： - `pom.xml` 定义依赖和配置。 - `src/main/java` 放主代码，`src/test/java` 放测试代码。
- **构建命令**： - `mvn compile` → `mvn test` → `mvn package`。
- **运行**：`java -jar` 或 `java -cp` 执行 `.jar` 文件。








	  AI 思考中...





			** [Maven 简介](https://www.runoob.com/maven-intro.html)
			[Maven 常用命令](https://www.runoob.com/maven-commands.html) **













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