# Maven 环境配置

- Source: https://www.runoob.com/maven/maven-setup.html

Maven 是一个基于 Java 的工具，所以要做的第一件事情就是安装 JDK。


下载 JDK（推荐 JDK 8/11/17）：


- [Oracle JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [OpenJDK](https://adoptium.net/)


如果你还未安装 JDK，可以参考我们的 [Java 开发环境配置](https://www.runoob.com/../java/java-environment-setup.html)。


### 系统要求


| 项目 | 要求 |
| --- | --- |
| JDK | Maven 3.3 要求 JDK 1.7 或以上Maven 3.2 要求 JDK 1.6 或以上Maven 3.0/3.1 要求 JDK 1.5 或以上 |
| 内存 | 没有最低要求 |
| 磁盘 | Maven 自身安装需要大约 10 MB 空间。除此之外，额外的磁盘空间将用于你的本地 Maven 仓库。你本地仓库的大小取决于使用情况，但预期至少 500 MB |
| 操作系统 | 没有最低要求 |


### 检查 Java 安装


| 操作系统 | 任务 | 命令 |
| --- | --- | --- |
| Windows | 打开命令控制台 |
```
c:\> java -version
```
 |
| Linux | 打开命令终端 |
```
# java -version
```
 |
| Mac | 打开终端 |
```
$ java -version
```
 |


### Maven 下载


Maven 下载地址：[http://maven.apache.org/download.cgi](http://maven.apache.org/download.cgi)


![](https://www.runoob.com/wp-content/uploads/2018/09/750D721E-0624-4C16-AD4B-9EA5D7F6289A.png)


不同平台下载对应的包：


| 系统 | 包名 |
| --- | --- |
| Windows | apache-maven-3.3.9-bin.zip |
| Linux | apache-maven-3.3.9-bin.tar.gz |
| Mac | apache-maven-3.3.9-bin.tar.gz |


下载包后解压到对应目录：


| 系统 | 存储位置 (可根据自己情况配置) |
| --- | --- |
| Windows | E:\Maven\apache-maven-3.3.9 |
| Linux | /usr/local/apache-maven-3.3.9 |
| Mac | /usr/local/apache-maven-3.3.9 |


### 设置 Maven 环境变量


添加环境变量 MAVEN_HOME：


| 系统 | 配置 |
| --- | --- |
| Windows | 右键 "计算机"，选择 "属性"，之后点击 "高级系统设置"，点击"环境变量"，来设置环境变量，有以下系统变量需要配置： 新建系统变量 MAVEN_HOME，变量值：E:\Maven\apache-maven-3.3.9 编辑系统变量 Path，添加变量值：;%MAVEN_HOME%\bin 注意：注意多个值之间需要有分号隔开，然后点击确定。 |
| Linux | 下载解压：
```
# wget http://mirrors.hust.edu.cn/apache/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz
# tar -xvf  apache-maven-3.3.9-bin.tar.gz
# sudo mv -f apache-maven-3.3.9 /usr/local/
```
 编辑 /etc/profile 文件 sudo vim /etc/profile，在文件末尾添加如下代码：
```
export MAVEN_HOME=/usr/local/apache-maven-3.3.9
export PATH=${PATH}:${MAVEN_HOME}/bin
```
 保存文件，并运行如下命令使环境变量生效：
```
# source /etc/profile
```
 在控制台输入如下命令，如果能看到 Maven 相关版本信息，则说明 Maven 已经安装成功：
```
# mvn -v
```
 |
| Mac | 下载解压：
```
$ curl -O http://mirrors.hust.edu.cn/apache/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz
$ tar -xvf  apache-maven-3.3.9-bin.tar.gz
$ sudo mv -f apache-maven-3.3.9 /usr/local/
```
 编辑 /etc/profile 文件 sudo vim /etc/profile，在文件末尾添加如下代码：
```
export MAVEN_HOME=/usr/local/apache-maven-3.3.9
export PATH=${PATH}:${MAVEN_HOME}/bin
```
 保存文件，并运行如下命令使环境变量生效：
```
$ source /etc/profile
```
 在控制台输入如下命令，如果能看到 Maven 相关版本信息，则说明 Maven 已经安装成功：
```
$ mvn -v
Apache Maven 3.3.9 (bb52d8502b132ec0a5a3f4c09453c07478323dc5; 2015-11-11T00:41:47+08:00)
Maven home: /usr/local/apache-maven-3.3.9
Java version: 1.8.0_31, vendor: Oracle Corporation
Java home: /Library/Java/JavaVirtualMachines/jdk1.8.0_31.jdk/Contents/Home/jre
Default locale: zh_CN, platform encoding: ISO8859-1
OS name: "mac os x", version: "10.13.4", arch: "x86_64", family: "mac"
```
 |


### 验证安装


```
mvn -v  # 应输出 Maven 版本和 Java 信息
```


### 配置 Maven 本地仓库

Maven 默认从远程仓库下载依赖，并存储在本地：


默认本地仓库路径：


- Windows: `C:\Users\\.m2\repository`
- Linux/macOS: `~/.m2/repository`


修改仓库位置（可选）：

在 MAVEN_HOME/conf/settings.xml 中修改：


```
<localRepository>/path/to/your/repo</localRepository>
```


---


## 第一个 Maven 项目


### 使用 Maven 创建项目

运行以下命令生成标准 Java 项目：


```
mvn archetype:generate \
    -DgroupId=com.example \
    -DartifactId=my-first-app \
    -DarchetypeArtifactId=maven-archetype-quickstart \
    -DinteractiveMode=false
```


这会生成一个标准 Maven 项目结构：


```
my-first-app/
├── pom.xml           # 项目配置文件
├── src/
│   ├── main/         # 主代码
│   │   └── java/     # Java 源代码
│   └── test/         # 测试代码
│       └── java/     # 测试类
```


### 解读 pom.xml

生成的 pom.xml 示例：


```
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>      <!-- 组织名 -->
    <artifactId>my-first-app</artifactId>  <!-- 项目名 -->
    <version>1.0-SNAPSHOT</version>     <!-- 版本号 -->

    <dependencies>
        <dependency>
            <groupId>junit</groupId>    <!-- 测试依赖 -->
            <artifactId>junit</artifactId>
            <version>4.12</version>
            <scope>test</scope>         <!-- 仅用于测试 -->
        </dependency>
    </dependencies>
</project>
```


### 编译和运行


```
mvn compile    # 编译项目
mvn test       # 运行测试
mvn package    # 打包成 .jar 文件
java -jar target/my-first-app-1.0-SNAPSHOT.jar  # 运行（如果可执行）
```










	  AI 思考中...





			** [Maven 教程](https://www.runoob.com/maven-tutorial.html)
			[Maven POM](https://www.runoob.com/maven-pom.html) **













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