# MySQL 连接

- Source: https://www.runoob.com/mysql/mysql-connection.html

安装 MySQL 后，你可以通过以下几种方式连接到 MySQL 服务端：

- 1、使用命令行客户端连接
- 2、使用图形化工具连接


常用 MySQL 图形化管理工具：


- MySQL Workbench（官方工具）：[https://www.mysql.com/cn/products/workbench/](https://www.mysql.com/cn/products/workbench/)
- Navicat（付费）：[https://www.navicat.com/](https://www.navicat.com/)
- DBeaver：[https://dbeaver.io/](https://dbeaver.io/)
- phpMyAdmin（基于Web）：[https://www.phpmyadmin.net/](https://www.phpmyadmin.net/)


---


## 使用 MySQL 二进制方式连接


您可以使用 MySQL 二进制方式进入到 mysql 命令提示符下来连接 MySQL 数据库，格式如下：


```
mysql -u your_username -p
```


**参数说明：**


- `-u` 参数用于指定用户名。
- `-p` 参数表示需要输入密码。


指定主机和端口连接（适用于远程连接）:


```
mysql -h 主机名或IP地址 -P 端口号 -u 用户名 -p
```


例如：


```
mysql -h 127.0.0.1 -P 3306 -u root -p
```


### 实例


以下是从命令行中连接 mysql 服务器的简单实例：


```
[root@host]# mysql -u root -p
Enter password:******
```


按照提示输入密码，并按下 Enter 键。


在登录成功后会出现 **mysql>** 命令提示窗口，你可以在上面执行任何 SQL 语句。

以上命令执行后，登录成功输出结果如下:


```
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2854760 to server version: 5.0.9

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.
```


在以上实例中，我们使用了 root 用户登录到 MySQL 服务器，当然你也可以使用其他 MySQL 用户登录。

如果用户权限足够，任何用户都可以在 MySQL 的命令提示窗口中进行 SQL 操作。


成功连接到 MySQL 后，你可以在命令行中直接执行 SQL 查询。


列出所有可用的数据库：


```
SHOW DATABASES;
```


选择要使用的数据库：


```
USE your_database;
```


列出所选数据库中的所有表：


```
SHOW TABLES;
```


退出 **mysql>** 命令提示窗口可以使用 **exit** 命令，如下所示：


```
mysql> EXIT;
Bye
```


或者使用：


```
mysql> QUIT;
```


或者按下 **Ctrl + D**（在 Unix/Linux 系统中）。


---


## 数据库管理工具


### 1. DBeaver


DBeaver是一款免费、开源、跨平台的数据库管理工具。


DBeaver 支持多种数据库系统，包括 MySQL、PostgreSQL、MariaDB、SQLite、Oracle、DB2、SQL Server、Sybase、MS Access、Teradata、Firebird、Derby 等。


下载地址：[https://dbeaver.io/download/](https://dbeaver.io/download/)


![](https://www.runoob.com/wp-content/uploads/2014/03/mysql-db-client-1.webp)


### 2. DbGate


DbGate 是一款跨平台的数据库管理工具，支持多种数据库系统，包括 MySQL、PostgreSQL、Microsoft SQL Server、SQLite、MongoDB 等。


DbGate 支持在 Windows、Linux 和 Mac 操作系统上运行，为用户提供了跨平台的灵活性。


DbGate 不仅仅是本地应用程序，还可以作为 Web 应用程序运行，使用户能够通过浏览器轻松访问和管理数据库。


下载地址：[https://dbgate.org/download/](https://dbgate.org/download/)


![](https://www.runoob.com/wp-content/uploads/2014/03/mysql-db-client-2.webp)








	  AI 思考中...





			** [MySQL PHP 连接与使用](https://www.runoob.com/mysql-php-syntax.html)
			[MySQL 创建数据库](https://www.runoob.com/mysql-create-database.html) **













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