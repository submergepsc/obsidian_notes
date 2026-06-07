# Mac OSX 平台安装 MongoDB

- Source: https://www.runoob.com/mongodb/mongodb-osx-install.html

MongoDB 提供了 OSX 平台上 64 位的安装包，你可以在官网下载安装包。

下载地址：[https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)


![](https://www.runoob.com/wp-content/uploads/2017/03/F1642F2B-A395-41BD-A66D-A1446BAD2324.jpg)


**从 MongoDB 3.0 版本开始只支持 OS X 10.7 (Lion) 版本及更新版本的系统。


接下来我们使用 curl 命令来下载安装：


```
# 进入 /usr/local
cd /usr/local

# 下载
sudo curl -O https://fastdl.mongodb.org/osx/mongodb-osx-ssl-x86_64-4.0.9.tgz

# 解压
sudo tar -zxvf mongodb-osx-ssl-x86_64-4.0.9.tgz

# 重命名为 mongodb 目录

sudo mv mongodb-osx-x86_64-4.0.9/ mongodb
```


安装完成后，我们可以把 MongoDB 的二进制命令文件目录（安装目录/bin）添加到 PATH 路径中：


```
export PATH=/usr/local/mongodb/bin:$PATH
```


创建日志及数据存放的目录：


- 数据存放路径：
```
sudo mkdir -p /usr/local/var/mongodb
```

- 日志文件路径：
```
sudo mkdir -p /usr/local/var/log/mongodb
```


接下来要确保当前用户对以上两个目录有读写的权限：


```
sudo chown runoob /usr/local/var/mongodb
sudo chown runoob /usr/local/var/log/mongodb
```


创建日志文件：


```
sudo touch /usr/local/var/log/mongodb/mongo.log
sudo chown runoob /usr/local/var/log/mongodb/mongo.log
```


以上 runoob** 是我电脑上的用户，你这边需要根据你当前对用户名来修改。


接下来我们使用以下命令在后台启动 mongodb：


```
mongod --dbpath /usr/local/var/mongodb --logpath /usr/local/var/log/mongodb/mongo.log --fork
```


- **--dbpath** 设置数据存放目录
- **--logpath** 设置日志存放目录
- **--fork** 在后台运行

如果不想在后端运行，而是在控制台上查看运行过程可以直接设置配置文件启动：


```
mongod --config /usr/local/etc/mongod.conf
```


查看 mongod 服务是否启动：


```
ps aux | grep -v grep | grep mongod
```


使用以上命令如果看到有 mongod 的记录表示运行成功。


启动后我们可以使用 **mongo** 命令打开一个终端：


```
$ cd /usr/local/mongodb/bin
$ ./mongo
MongoDB shell version v4.0.9
connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("3c12bf4f-695c-48b2-b160-8420110ccdcf") }
MongoDB server version: 4.0.9
……
> 1 + 1
2
>
```


**
MongoDB6.0 以后做出了重大改变，MongoDB 已经不再默认安装 shell 工具，你需要安装一个额外的 shell 工具：[MongoDB Shell](https://www.runoob.com/mongodb-shell.html)


---


## 使用 brew 安装


此外你还可以使用 OSX 的 brew 来安装 mongodb：


```
brew tap mongodb/brew
brew install [email protected]
```


**@** 符号后面的 4.4** 是最新版本号。


安装信息：


- 配置文件：**/usr/local/etc/mongod.conf**
- 日志文件路径：**/usr/local/var/log/mongodb**
- 数据存放路径：**/usr/local/var/mongodb**


### 运行 MongoDB

我们可以使用 brew 命令或 mongod 命令来启动服务。


brew 启动：


```
brew services start [email protected]
```


brew 停止：


```
brew services stop [email protected]
```


mongod 命令后台进程方式：


```
mongod --config /usr/local/etc/mongod.conf --fork
```


这种方式启动要关闭可以进入 mongo shell 控制台来实现：


```
> db.adminCommand({ "shutdown" : 1 })
```










	  AI 思考中...





			** [PHP7 MongDB 安装与使用](https://www.runoob.com/php7-mongdb-tutorial.html)
			[MongoDB 创建集合](https://www.runoob.com/mongodb-create-collection.html) **













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