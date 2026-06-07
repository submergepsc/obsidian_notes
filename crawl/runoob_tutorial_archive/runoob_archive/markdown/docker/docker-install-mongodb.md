# Docker 安装 MongoDB

- Source: https://www.runoob.com/docker/docker-install-mongodb.html

MongoDB 是一个免费的开源跨平台面向文档的 NoSQL 数据库程序。


### 1、查看可用的 MongoDB 版本


访问 MongoDB 镜像库地址： [https://hub.docker.com/_/mongo?tab=tags&page;=1](https://hub.docker.com/_/mongo?tab=tags&page=1)。


可以通过 Sort by 查看其他版本的 MongoDB，默认是最新版本 **mongo:latest**。


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-mongo1.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-mongo1.png)


你也可以在下拉列表中找到其他你想要的版本：


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-mongo2.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-mongo2.png)


此外，我们还可以用 **docker search mongo** 命令来查看可用版本：


```
$ docker search mongo
NAME                              DESCRIPTION                      STARS     OFFICIAL   AUTOMATED
mongo                             MongoDB document databases ...   1989      [OK]
mongo-express                     Web-based MongoDB admin int...   22        [OK]
mvertes/alpine-mongo              light MongoDB container          19                   [OK]
mongooseim/mongooseim-docker      MongooseIM server the lates...   9                    [OK]
torusware/speedus-mongo           Always updated official Mon...   9                    [OK]
jacksoncage/mongo                 Instant MongoDB sharded cluster  6                    [OK]
mongoclient/mongoclient           Official docker image for M...   4                    [OK]
jadsonlourenco/mongo-rocks        Percona Mongodb with Rocksd...   4                    [OK]
asteris/apache-php-mongo          Apache2.4 + PHP + Mongo + m...   2                    [OK]
19hz/mongo-container              Mongodb replicaset for coreos    1                    [OK]
nitra/mongo                       Mongo3 centos7                   1                    [OK]
ackee/mongo                       MongoDB with fixed Bluemix p...  1                    [OK]
kobotoolbox/mongo                 https://github.com/kobotoolb...  1                    [OK]
valtlfelipe/mongo                 Docker Image based on the la...  1                    [OK]
```


### 2、取最新版的 MongoDB 镜像


这里我们拉取官方的最新版本的镜像：


```
$ docker pull mongo:latest
```


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-mongo3.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-mongo3.png)


### 3、查看本地镜像


使用以下命令来查看是否已安装了 mongo：


```
$ docker images
```


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-mongo4.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-mongo4.png)


在上图中可以看到我们已经安装了最新版本（latest）的 mongo 镜像。


### 4、运行容器


安装完成后，我们可以使用以下命令来运行 mongo 容器：


```
docker run -d -p 27017:27017 --name my-mongo-container mongo
```


参数说明：


- `-d`: 后台运行容器。
- `-p 27017:27017`: 将主机的27017端口映射到容器的27017端口。
- `--name my-mongo-container`: 为容器指定一个名字，这里是`my-mongo-container`，你可以根据需要更改。


### 5、安装成功


最后我们可以通过 **docker ps** 命令查看容器的运行信息：


```
# docker ps
CONTAINER ID   IMAGE      ...   PORTS                    NAMES
d53e5d57668b   mongo      ...  :::27017->27017/tcp   my-mongo-container
```


你应该能够看到名为 **my-mongo-container** 的 MongoDB 容器正在运行。


接下来我们可以使用 MongoDB 客户端（例如 mongo shell）连接到运行中的 MongoDB 容器。


你可以使用以下命令连接到 MongoDB：


```
$ mongosh --host 127.0.0.1 --port 27017
Current Mongosh Log ID: 656d34911ff5455b0c3afdc0
Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.0
Using MongoDB:          7.0.4
Using Mongosh:          2.1.0

For mongosh info see: https://docs.mongodb.com/mongodb-shell/
...
```


这将连接到本地主机的 27017 端口，你可以根据之前映射的端口进行调整。


进入 MongoDB 容器的 bash shell 命令如下：


```
docker exec -it my-mongo-container bash
```


记得在不再需要时停止和删除容器，可以使用以下命令：


```
docker stop my-mongo-container
docker rm my-mongo-container
```










	  AI 思考中...





			** [Docker 安装 Redis](https://www.runoob.com/docker-install-redis.html)
			[Docker 安装 Apache](https://www.runoob.com/docker-install-apache.html) **













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