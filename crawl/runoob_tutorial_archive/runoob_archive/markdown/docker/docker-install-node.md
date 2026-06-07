# Docker 安装 Node.js

- Source: https://www.runoob.com/docker/docker-install-node.html

Node.js 是一个基于 Chrome V8 引擎的 JavaScript 运行环境，是一个让 JavaScript 运行在服务端的开发平台。


### 1、查看可用的 Node 版本


访问 Node 镜像库地址： [https://hub.docker.com/_/node?tab=tags](https://hub.docker.com/_/node?tab=tags)。


可以通过 Sort by 查看其他版本的 Node，默认是最新版本 **node:latest**。


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-node1.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-node1.png)


你也可以在下拉列表中找到其他你想要的版本：


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-node2.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-node2.png)


此外，我们还可以用 **docker search node** 命令来查看可用版本：


```
$ docker search node
```


### 2、取最新版的 node 镜像


这里我们拉取官方的最新版本的镜像：


```
$ docker pull node:latest
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-node3.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-node3.png)


### 3、查看本地镜像


使用以下命令来查看是否已安装了 node


```
$ docker images
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-node4.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-node4.png)


在上图中可以看到我们已经安装了最新版本（latest）的 node 镜像。


### 4、运行容器


安装完成后，我们可以使用以下命令来运行 node 容器：


```
$ docker run -itd --name node-test node
```


参数说明：


- **--name node-test**：容器名称。


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-node5.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-node5.png)


### 5、安装成功


最后进入查看容器运行的 node 版本:


```
$ docker exec -it node-test /bin/bash
root@6c5d265c68a6:/# node -v
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-node6.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-node6.png)








	  AI 思考中...





			** [Docker 安装 CentOS](https://www.runoob.com/docker-install-centos.html)
			[Docker stats 命令](https://www.runoob.com/docker-stats-command.html) **













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