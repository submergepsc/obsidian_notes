# Windows 平台安装 MongoDB

- Source: https://www.runoob.com/mongodb/mongodb-window-install.html

## MongoDB 下载


最新版本的 MongoDB 提供了可用于 64 位系统的预编译二进制包，你可以从 MongoDB 官网下载安装，MongoDB 预编译二进制包下载地址：[https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)


**
注意：在 MongoDB 2.2 版本后已经不再支持 Windows XP 系统。最新版本也已经没有了 32 位系统的安装文件。


![](https://www.runoob.com/wp-content/uploads/2013/10/win-mongo-dw.png)


- **MongoDB for Windows 64-bit** 适合 64 位的 Windows Server 2008 R2, Windows 7 , 及最新版本的 Window 系统。
- ** MongoDB for Windows 32-bit** 适合 32 位的 Window 系统及最新的 Windows Vista。 32 位系统上 MongoDB 的数据库最大为 2GB。
- **MongoDB for Windows 64-bit Legacy** 适合 64 位的 Windows Vista, Windows Server 2003, 及 Windows Server 2008 。


下载 **.msi** 文件，下载后双击该文件，按操作提示安装即可。

点击 "Next" 按钮来启动安装过程：

![](https://www.runoob.com/wp-content/uploads/2013/10/image3-5.png)

接下来，将出现一个协议窗口，选中同意的选项，然后再点击 "Next" 按钮：


![](https://www.runoob.com/wp-content/uploads/2013/10/image2-5.png)


现在，出现了两个选择：您可以以网络服务用户身份运行 MongoDB，也可以以本地或域用户身份运行它。


如果您需要简单性和基本功能，网络服务用户选项就可以了，如果您需要对权限进行更多控制，或者需要使用特定用户凭据访问和限制资源，则选择本地或域用户选项会更合适
。

我们简单测试就选第一个，然后单击"Next" 按钮：


![](https://www.runoob.com/wp-content/uploads/2013/10/image5-5.png)


接下来我们可以选择完整安装，改安装方式默认配置安装所有 MongoDB 组件和工具，当然你也可以选择自定义安装。


![](https://www.runoob.com/wp-content/uploads/2013/10/Steps-to-install-MongoDB_4.png)


![](https://www.runoob.com/wp-content/uploads/2013/10/image4-4.png)

选择安装方法后，您需要单击 "Install" 按钮来开始安装过程：


![](https://www.runoob.com/wp-content/uploads/2013/10/image7-3.png)


安装完成后，点击 "Finish" 按钮关闭安装程序：


![](https://www.runoob.com/wp-content/uploads/2013/10/image6-3.png)


设置环境变量:系统属性->环境变量->系统变量->路径->编辑环境变量：


![](https://www.runoob.com/wp-content/uploads/2013/10/image8-3.png)


创建数据目录**


MongoDB 将数据目录存储在 db 目录下，我们在安装完成后可以创建它。

请注意，数据目录应该放在根目录下 (如： C:\ 或者 D:\ 等 )。


在本教程中，我们已经在 C 盘安装了 mongodb，现在让我们创建一个 data 的目录然后在 data 目录里创建 db 目录。


```
cd C:\
md "\data\db"
```


你也可以通过 window 的资源管理器中创建这些目录，而不一定通过命令行。

**
---


## 命令行下运行 MongoDB 服务器


执行 **mongod** 命令：


```
mongod --dbpath c:\data\db
```


如果执行成功，会输出如下信息：


![](https://www.runoob.com/wp-content/uploads/2013/10/image10-3.png)


---

## 连接 MongoDB


> MongoDB6.0 以后做出了重大改变，MongoDB 已经不再默认安装 shell 工具，你需要安装一个额外的 shell 工具：[MongoDB Shell](https://www.runoob.com/mongodb-shell.html)


我们可以在命令窗口中运行 mongo 命令即可连接上 MongoDB，执行如下命令：


```
mongo
```


---


## 配置 MongoDB 服务


> 注意：**一些新版本的 MongoDB 安装时已经自行完成大部分配置，如果以下目录已经存在，你可以直接跳过这部分内容。


**管理员模式打开命令行窗口**


创建目录，执行下面的语句来创建数据库和日志文件的目录


```
mkdir c:\data\db
mkdir c:\data\log
```


**创建配置文件**


创建一个配置文件。该文件必须设置 systemLog.path 参数，包括一些附加的配置选项更好。


例如，创建一个配置文件位于 C:\mongodb\mongod.cfg，其中指定 systemLog.path 和 storage.dbPath。具体配置内容如下：


```
systemLog:
    destination: file
    path: c:\data\log\mongod.log
storage:
    dbPath: c:\data\db
```


### 安装 MongoDB服务


通过执行 mongod，使用 --install 选项来安装服务，使用 --config 选项来指定之前创建的配置文件。


```
mongod  --config "C:\mongodb\mongod.cfg" --install
```


要使用备用 dbpath，可以在配置文件（例如：C:\mongodb\mongod.cfg）或命令行中通过 --dbpath 选项指定。


如果需要，您可以安装 mongod 或 mongos 的多个实例的服务。只需要通过使用 --serviceName 和 --serviceDisplayName 指定不同的实例名。只有当存在足够的系统资源和系统的设计需要这么做。


启动 MongoDB 服务


```
net start MongoDB
```


关闭 MongoDB 服务


```
net stop MongoDB
```


移除 MongoDB 服务


```
mongod --remove
```


**
命令行下运行 MongoDB 服务器** 和 **配置 MongoDB 服务** 任选一个方式启动就可以。


任选一个操作就好

---


## MongoDB 后台管理 Shell


如果你需要进入MongoDB后台管理，你需要先打开mongodb装目录的下的bin目录，然后执行mongo.exe文件，MongoDB Shell是MongoDB自带的交互式Javascript shell,用来对MongoDB进行操作和管理的交互式环境。


当你进入mongoDB后台后，它默认会链接到 test 文档（数据库）：


```
> mongo
MongoDB shell version: 3.0.6
connecting to: test
……
```


由于它是一个JavaScript shell，您可以运行一些简单的算术运算:


```
> 2 + 2
4
>
```


**db** 命令用于查看当前操作的文档（数据库）：


```
> db
test
>
```


插入一些简单的记录并查找它：


```
> db.runoob.insert({x:10})
WriteResult({ "nInserted" : 1 })
> db.runoob.find()
{ "_id" : ObjectId("5604ff74a274a611b0c990aa"), "x" : 10 }
>
```


第一个命令将数字 10 插入到 runoob 集合的 x 字段中。








	  AI 思考中...





			** [MongoDB 简介](https://www.runoob.com/mongodb-intro.html)
			[Linux 平台安装 MongoDB](https://www.runoob.com/mongodb-linux-install.html) **













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