# PostgreSQL 删除数据库

- Source: https://www.runoob.com/postgresql/postgresql-drop-database.html

PostgreSQL 删除数据库可以用以下三种方式：


- 1、使用 **DROP DATABASE** SQL 语句来删除。
- 2、使用 **dropdb** 命令来删除。
- 3、使用 **pgAdmin** 工具。


**注意：**删除数据库要谨慎操作，一旦删除，所有信息都会消失。


### DROP DATABASE 删除数据库


DROP DATABASE 会删除数据库的系统目录项并且删除包含数据的文件目录。


DROP DATABASE 只能由超级管理员或数据库拥有者执行。


DROP DATABASE 命令需要在 PostgreSQL 命令窗口来执行，语法格式如下：


```
DROP DATABASE [ IF EXISTS ] name
```


**参数说明：**


- **IF EXISTS**：如果数据库不存在则发出提示信息，而不是错误信息。
- **name**：要删除的数据库的名称。


例如，我们删除一个 runoobdb 的数据库：


```
postgres=# DROP DATABASE runoobdb;
```


### dropdb 命令删除数据库


dropdb 是 DROP DATABASE 的包装器。


dropdb 用于删除 PostgreSQL 数据库。


dropdb 命令只能由超级管理员或数据库拥有者执行。


dropdb 命令语法格式如下：


```
dropdb [connection-option...] [option...] dbname
```


**参数说明：**


**dbname**：要删除的数据库名。


**options**：参数可选项，可以是以下值：


| 序号 | 选项 & 描述 |
| --- | --- |
| 1 | -e 显示 dropdb 生成的命令并发送到数据库服务器。 |
| 2 | -i 在做删除的工作之前发出一个验证提示。 |
| 3 | -V 打印 dropdb 版本并退出。 |
| 4 | --if-exists 如果数据库不存在则发出提示信息，而不是错误信息。 |
| 5 | --help 显示有关 dropdb 命令的帮助信息。 |
| 6 | -h host 指定运行服务器的主机名。 |
| 7 | -p port 指定服务器监听的端口，或者 socket 文件。 |
| 8 | -U username 连接数据库的用户名。 |
| 9 | -w 连接时忽略输入密码。 |
| 10 | -W 连接时强制要求输入密码。 |
| 11 | --maintenance-db=dbname 删除数据库时指定连接的数据库，默认为 postgres，如果它不存在则使用 template1。 |


接下来我们打开一个命令窗口，进入到 PostgreSQL 的安装目录，并进入到 bin 目录，dropdb 名位于 **PostgreSQL安装目录/bin** 下，执行删除数据库的命令：


```
$ cd /Library/PostgreSQL/11/bin/
$ dropdb -h localhost -p 5432 -U postgres runoobdb
password ******
```


以上命令我们使用了超级用户 postgres 登录到主机地址为 localhost，端口号为 5432 的 PostgreSQL 数据库中并删除 runoobdb 数据库。


### pgAdmin 工具删除据库


pgAdmin 工具提供了完整操作数据库的功能：


![](https://www.runoob.com/wp-content/uploads/2019/05/ABFD169B-E677-4061-AF1E-DB3CCF1B0010.jpg)









	  AI 思考中...





			** [PostgreSQL 选择数据库](https://www.runoob.com/postgresql-select-database.html)
			[PostgreSQL 创建表格](https://www.runoob.com/postgresql-create-table.html) **













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