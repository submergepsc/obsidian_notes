# Maven 多模块项目管理

- Source: https://www.runoob.com/maven/maven-multi-module.html

Maven 多模块项目(Multi-module Project)是指一个父项目(parent project)包含多个子模块(submodules)的项目结构。这种结构允许我们将一个大型项目拆分成多个逻辑上独立但又相互关联的模块，每个模块可以单独构建，也可以作为整体一起构建。


### 多模块项目的优势


- **代码复用**：公共代码可以提取到单独的模块中供其他模块使用
- **职责分离**：不同团队可以专注于不同模块的开发
- **构建效率**：只构建发生变化的模块，减少构建时间
- **依赖管理**：统一管理所有模块的依赖关系
- **版本控制**：所有模块使用统一的版本号，便于管理


### 适用场景


- 大型项目分层（如 `web`、`service`、`dao`）
- 微服务架构（每个服务一个模块）
- 共享通用代码（如 `common` 模块）


### 标准目录结构


```
parent-project/          # 父项目根目录
├── pom.xml             # 父POM（packaging=pom）
├── module-a/           # 子模块A
│   ├── src/
│   └── pom.xml         # 子模块A的POM
├── module-b/           # 子模块B
│   ├── src/
│   └── pom.xml         # 子模块B的POM
└── module-web/         # Web模块
    ├── src/
    └── pom.xml
```


**关键特征：**


- **父POM**： - 必须设置 `pom` - 通过 `` 管理子模块
- **子模块**： - 通过 `` 继承父POM - 可以有自己的依赖和构建配置


---


## 创建 Maven 多模块项目


### 1. 创建父项目


父项目本身通常不包含任何代码，它主要用来管理子模块和公共配置。

创建父项目的 pom.xml 文件需要设置 packaging 为 pom：


```java
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>parent-project</artifactId>
    <version>1.0.0</version>
    <packaging>pom</packaging>

    <modules>
        <module>module1</module>
        <module>module2</module>
    </modules>
</project>
```


### 2. 创建子模块


子模块是实际的代码模块，可以是普通的 Java 项目、Web 应用等。每个子模块都有自己的 pom.xml 文件，但需要声明父项目：


```java
<project>
    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent-project</artifactId>
        <version>1.0.0</version>
    </parent>

    <modelVersion>4.0.0</modelVersion>
    <artifactId>module1</artifactId>
</project>
```


---


## 多模块项目依赖管理


在多模块项目中，模块之间可以相互依赖。例如 module2 依赖 module1：


```java
<project>
    <!-- module2 的 pom.xml -->
    <dependencies>
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>module1</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>
</project>
```


### 依赖继承


父项目可以定义公共依赖，子模块会自动继承这些依赖：


```java
<project>
    <!-- 父项目 pom.xml -->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>junit</groupId>
                <artifactId>junit</artifactId>
                <version>4.12</version>
                <scope>test</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
</project>
```


子模块只需声明依赖的 groupId 和 artifactId，无需指定版本：


```java
<project>
    <!-- 子模块 pom.xml -->
    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
        </dependency>
    </dependencies>
</project>
```


---


## 多模块项目构建


### 1. 构建整个项目


在父项目目录下执行：


```java
mvn clean install
```


这会按照依赖顺序构建所有子模块。


### 2. 构建单个模块


进入特定模块目录执行：


```java
cd module1
mvn clean install
```


或者从父项目目录指定模块：


```java
mvn -pl module1 clean install
```


### 3. 构建模块及其依赖


```java
mvn -pl module1 -am clean install
```


---


## 多模块项目最佳实践


### 1. 合理的模块划分


- 按功能划分模块
- 按层次划分模块(如 dao, service, web)
- 公共工具提取到单独模块


### 2. 版本管理


- 使用父项目统一管理版本号
- 考虑使用 Maven 的版本插件管理版本升级


### 3. 构建优化


- 配置适当的构建顺序
- 使用 profile 管理不同环境的构建
- 考虑并行构建提高效率


### 4. 依赖管理


- 在父项目中集中管理公共依赖
- 使用 dependencyManagement 统一版本
- 避免循环依赖


---


## 常见问题与解决方案


### 1. 循环依赖问题


**问题**：模块 A 依赖模块 B，模块 B 又依赖模块 A**解决方案**：


- 重新设计模块结构，提取公共代码到第三个模块
- 使用接口解耦


### 2. 构建顺序问题


**问题**：Maven 不能正确识别模块间的依赖顺序**解决方案**：


- 显式声明模块依赖关系
- 使用 reactor 插件分析构建顺序


### 3. 版本不一致问题


**问题**：不同模块使用不同版本的依赖**解决方案**：


- 在父项目中统一管理依赖版本
- 使用 dependencyManagement


通过合理使用 Maven 多模块项目管理，可以显著提高大型项目的可维护性和构建效率。掌握这些技巧将帮助你更好地组织和管理复杂的 Java 项目。








	  AI 思考中...





			** [Maven 依赖机制](https://www.runoob.com/maven-dependencies.html)














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