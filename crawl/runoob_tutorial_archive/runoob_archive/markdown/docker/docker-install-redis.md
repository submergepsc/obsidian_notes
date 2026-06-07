# Docker 安装 Redis

- Source: https://www.runoob.com/docker/docker-install-redis.html

Redis 是一个开源的使用 ANSI C 语言编写、支持网络、可基于内存亦可持久化的日志型、Key-Value 的 NoSQL 数据库，并提供多种语言的 API。


### 1、查看可用的 Redis 版本


访问 Redis 镜像库地址： [https://hub.docker.com/_/redis?tab=tags](https://hub.docker.com/_/redis?tab=tags)。


可以通过 Sort by 查看其他版本的 Redis，默认是最新版本 **redis:latest**。


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis1.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis1.png)


你也可以在下拉列表中找到其他你想要的版本：


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis2.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis2.png)


此外，我们还可以用 **docker search redis** 命令来查看可用版本：


```
$ docker search  redis
NAME                      DESCRIPTION                   STARS  OFFICIAL  AUTOMATED
redis                     Redis is an open source ...   2321   [OK]
sameersbn/redis                                         32                   [OK]
torusware/speedus-redis   Always updated official ...   29             [OK]
bitnami/redis             Bitnami Redis Docker Image    22                   [OK]
anapsix/redis             11MB Redis server image ...   6                    [OK]
webhippie/redis           Docker images for redis       4                    [OK]
clue/redis-benchmark      A minimal docker image t...   3                    [OK]
williamyeh/redis          Redis image for Docker        3                    [OK]
unblibraries/redis        Leverages phusion/baseim...   2                    [OK]
greytip/redis             redis 3.0.3                   1                    [OK]
servivum/redis            Redis Docker Image            1                    [OK]
...
```


### 2、取最新版的 Redis 镜像


这里我们拉取官方的最新版本的镜像：


```
$ docker pull redis:latest
```


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis3.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis3.png)


### 3、查看本地镜像


使用以下命令来查看是否已安装了 redis：


```
$ docker images
```


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis4.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis4.png)


在上图中可以看到我们已经安装了最新版本（latest）的 redis 镜像。


### 4、运行容器


安装完成后，我们可以使用以下命令来运行 redis 容器：


```
$ docker run -itd --name redis-test -p 6379:6379 redis
```


参数说明：


- **-p 6379:6379**：映射容器服务的 6379 端口到宿主机的 6379 端口。外部可以直接通过宿主机ip:6379 访问到 Redis 的服务。


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis5.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis5.png)


### 5、安装成功


最后我们可以通过 **docker ps** 命令查看容器的运行信息：


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis6.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis6.png)


接着我们通过 redis-cli 连接测试使用 redis 服务。


```
$ docker exec -it redis-test /bin/bash
```


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis7.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-redis7.png)








	  AI 思考中...





			** [Docker 安装 Python](https://www.runoob.com/docker-install-python.html)
			[Docker 安装 MongoDB](https://www.runoob.com/docker-install-mongodb.html) **













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