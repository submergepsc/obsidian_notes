# Linux平台安装MongoDB

- Source: https://www.runoob.com/mongodb/mongodb-linux-install.html

MongoDB 提供了 Linux 各个发行版本 64 位的安装包，你可以在官网下载安装包。


安装前我们需要根据自己的系统版本安装对应的依赖包，**三选一执行**：


**Red Hat/CentOS：**


```
sudo yum install libcurl openssl
```


**Ubuntu 18.04 LTS ("Bionic")/Debian 10 "Buster"：**


```
sudo apt-get install libcurl4 openssl
```


**Ubuntu 16.04 LTS ("Xenial")/Debian 9 "Stretch"：**


```
sudo apt-get install libcurl3 openssl
```


MongoDB 源码下载地址：[https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)


![](https://www.runoob.com/wp-content/uploads/2013/10/0D72BC20-1D77-437E-972C-286EB5EFB183.jpg)


![](https://www.runoob.com/wp-content/uploads/2013/10/558D36F2-01AF-49C3-BA07-F2728B216C87.jpg)


这里我们选择 tgz 下载，下载完安装包，并解压 **tgz**（以下演示的是 64 位 Linux上的安装） 。


```
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-4.2.8.tgz    # 下载
tar -zxvf mongodb-linux-x86_64-ubuntu1604-4.2.8.tgz                                # 解压

mv mongodb-linux-x86_64-ubuntu1604-4.2.8  /usr/local/mongodb4                      # 将解压包拷贝到指定目录
```


MongoDB 的可执行文件位于 bin 目录下，所以可以将其添加到 **PATH** 路径中，这样就可以在任意目录执行 MongoDB 命令，而不需要每次切换到安装目录：


```
export PATH=<mongodb-install-directory>/bin:$PATH
```


**** 为你 MongoDB 的安装路径。如本文的 **/usr/local/mongodb4** 。


```
export PATH=/usr/local/mongodb4/bin:$PATH
```


注意：以上 export 命令只在当前终端会话中有效，关闭终端后会失效。如需永久生效，请将该命令追加到 `~/.bashrc` 或 `~/.profile` 文件中，然后执行 `source ~/.bashrc` 使其立即生效。

**
---

## 创建数据库目录


默认情况下 MongoDB 启动后会初始化以下两个目录：


- 数据存储目录：/var/lib/mongodb
- 日志文件目录：/var/log/mongodb


我们在启动前可以先创建这两个目录并设置当前用户有读写权限：


```
sudo mkdir -p /var/lib/mongodb
sudo mkdir -p /var/log/mongodb
sudo chown `whoami` /var/lib/mongodb     # 设置权限，whoami 会自动替换为当前登录的用户名
sudo chown `whoami` /var/log/mongodb     # 设置权限
```


接下来启动 Mongodb 服务：


```
mongod --dbpath /var/lib/mongodb --logpath /var/log/mongodb/mongod.log --fork
```


参数说明：


- `--dbpath`：指定数据库文件的存储目录
- `--logpath`：指定日志文件的路径（注意是文件路径，不是目录）
- `--fork`：让 MongoDB 在后台运行（即以守护进程方式启动），不加此参数则会占用当前终端


打开 /var/log/mongodb/mongod.log 文件看到以下信息，说明启动成功。


```
tail -10f /var/log/mongodb/mongod.log
2020-07-09T12:20:17.391+0800 I  NETWORK  [listener] Listening on /tmp/mongodb-27017.sock
2020-07-09T12:20:17.392+0800 I  NETWORK  [listener] Listening on 127.0.0.1
2020-07-09T12:20:17.392+0800 I  NETWORK  [listener] waiting for connections on port 27017
```


---

## MongoDB 后台管理 Shell


> MongoDB6.0 以后做出了重大改变，MongoDB 已经不再默认安装 shell 工具，你需要安装一个额外的 shell 工具：[MongoDB Shell](https://www.runoob.com/mongodb-shell.html)


如果你需要进入 mongodb 后台管理，你需要先打开 mongodb 安装目录的下的 bin 目录，然后执行 mongo 命令文件。


MongoDB Shell 是 MongoDB 自带的交互式 Javascript shell，用来对 MongoDB 进行操作和管理的交互式环境。


当你进入 mongoDB 后台后，它默认会连接到 test 文档（数据库）：


```
$ cd /usr/local/mongodb4/bin
$ ./mongo
MongoDB shell version v4.2.8
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("2cfdafc4-dd56-4cfc-933a-187b887119b3") }
MongoDB server version: 4.2.8
Welcome to the MongoDB shell.
……
```


由于它是一个JavaScript shell，您可以运行一些简单的算术运算:


```
> 2+2
4
> 3+6
9
```


现在让我们插入一些简单的数据，并对插入的数据进行检索：


```
> db.runoob.insert({x:10})
WriteResult({ "nInserted" : 1 })
> db.runoob.find()
{ "_id" : ObjectId("5f069bdb4e02f8baf90f1184"), "x" : 10 }
>
```


第一个命令将数字 10 插入到 runoob 集合的 x 字段中。

如果要停止 mongodb 可以使用以下命令：


```
mongod --dbpath /var/lib/mongodb --logpath /var/log/mongodb/mongod.log --shutdown
```


也可以在 mongo 的命令行中实现：


```
> use admin
switched to db admin
> db.shutdownServer()
```


更多安装方法可以参考官网：[https://docs.mongodb.com/manual/administration/install-on-linux/](https://docs.mongodb.com/manual/administration/install-on-linux/)








	  AI 思考中...





			** [Windows 平台安装 MongoDB](https://www.runoob.com/mongodb-window-install.html)
			[MongoDB 概念解析](https://www.runoob.com/mongodb-databases-documents-collections.html) **













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