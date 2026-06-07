# Docker 仓库管理

- Source: https://www.runoob.com/docker/docker-repository.html

仓库（Repository）是集中存放镜像的地方。以下介绍一下 [Docker Hub](https://hub.docker.com/)。当然不止 docker hub，只是远程的服务商不一样，操作都是一样的。


## Docker Hub


目前 Docker 官方维护了一个公共仓库 [Docker Hub](https://hub.docker.com/)。

大部分需求都可以通过在 Docker Hub 中直接下载镜像来实现。


### 注册


在 [https://hub.docker.com](https://hub.docker.com) 免费注册一个 Docker 账号。


### 登录和退出


登录需要输入用户名和密码，登录成功后，我们就可以从 docker hub 上拉取自己账号下的全部镜像。


```
$ docker login
```

[![](https://www.runoob.com/wp-content/uploads/2019/10/5974B2AE-945F-4DD0-A7C8-9D9B01BDAF62.jpg)](https://www.runoob.com/wp-content/uploads/2019/10/5974B2AE-945F-4DD0-A7C8-9D9B01BDAF62.jpg)


**退出**


退出 docker hub 可以使用以下命令：


```
$ docker logout
```


拉取镜像

你可以通过 docker search 命令来查找官方仓库中的镜像，并利用 docker pull 命令来将它下载到本地。


以 ubuntu 为关键词进行搜索：


```
$ docker search ubuntu
```


[![](https://www.runoob.com/wp-content/uploads/2019/10/docker-search22.png)](https://www.runoob.com/wp-content/uploads/2019/10/docker-search22.png)


使用 docker pull 将官方 ubuntu 镜像下载到本地：


```
$ docker pull ubuntu
```


[![](https://www.runoob.com/wp-content/uploads/2019/10/docker-pull22.png)](https://www.runoob.com/wp-content/uploads/2019/10/docker-pull22.png)


### 推送镜像


用户登录后，可以通过 docker push 命令将自己的镜像推送到 Docker Hub。


以下命令中的 username 请替换为你的 Docker 账号用户名。


```
$ docker tag ubuntu:18.04 username/ubuntu:18.04
$ docker image ls

REPOSITORY      TAG        IMAGE ID            CREATED           ...
ubuntu          18.04      275d79972a86        6 days ago        ...
username/ubuntu 18.04      275d79972a86        6 days ago        ...
$ docker push username/ubuntu:18.04
$ docker search username/ubuntu

NAME             DESCRIPTION       STARS         OFFICIAL    AUTOMATED
username/ubuntu
```










	  AI 思考中...





			** [Docker 镜像加速](https://www.runoob.com/docker-mirror-acceleration.html)
			[Docker Dockerfile](https://www.runoob.com/docker-dockerfile.html) **













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