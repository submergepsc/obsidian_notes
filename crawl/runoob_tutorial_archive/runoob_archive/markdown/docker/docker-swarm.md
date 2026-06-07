# Swarm 集群管理

- Source: https://www.runoob.com/docker/docker-swarm.html

### 简介


Docker Swarm 是 Docker 的集群管理工具。它将 Docker 主机池转变为单个虚拟 Docker 主机。 Docker Swarm 提供了标准的 Docker API，所有任何已经与 Docker 守护程序通信的工具都可以使用 Swarm 轻松地扩展到多个主机。


支持的工具包括但不限于以下各项：


- Dokku
- Docker Compose
- Docker Machine
- Jenkins


### 原理


如下图所示，swarm 集群由管理节点（manager）和工作节点（work node）构成。


- **swarm mananger**：负责整个集群的管理工作包括集群配置、服务管理等所有跟集群有关的工作。
- **work node**：即图中的 available node，主要负责运行相应的服务来执行任务（task）。


[![](https://www.runoob.com/wp-content/uploads/2019/11/services-diagram.png)](https://www.runoob.com/wp-content/uploads/2019/11/services-diagram.png)


---


## 使用


以下示例，均以 Docker Machine 和 virtualbox 进行介绍，确保你的主机已安装 virtualbox。


### 1、创建 swarm 集群管理节点（manager）


创建 docker 机器：


```
$ docker-machine create -d virtualbox swarm-manager
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm1.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm1.png)


初始化 swarm 集群，进行初始化的这台机器，就是集群的管理节点。


```
$ docker-machine ssh swarm-manager
$ docker swarm init --advertise-addr 192.168.99.107 #这里的 IP 为创建机器时分配的 ip。
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm2.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm2.png)


以上输出，证明已经初始化成功。需要把以下这行复制出来，在增加工作节点时会用到：


```
docker swarm join --token SWMTKN-1-4oogo9qziq768dma0uh3j0z0m5twlm10iynvz7ixza96k6jh9p-ajkb6w7qd06y1e33yrgko64sk 192.168.99.107:2377
```


### 2、创建 swarm 集群工作节点（worker）


这里直接创建好俩台机器，swarm-worker1 和 swarm-worker2 。


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm3.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm3.png)


分别进入两个机器里，指定添加至上一步中创建的集群，这里会用到上一步复制的内容。


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm4.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm4.png)


以上数据输出说明已经添加成功。


上图中，由于上一步复制的内容比较长，会被自动截断，实际上在图运行的命令如下：


```
docker@swarm-worker1:~$ docker swarm join --token SWMTKN-1-4oogo9qziq768dma0uh3j0z0m5twlm10iynvz7ixza96k6jh9p-ajkb6w7qd06y1e33yrgko64sk 192.168.99.107:2377
```


### 3、查看集群信息


进入管理节点，执行：docker info 可以查看当前集群的信息。


```
$ docker info
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm5.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm5.png)


通过画红圈的地方，可以知道当前运行的集群中，有三个节点，其中有一个是管理节点。


### 4、部署服务到集群中


**注意**：跟集群管理有关的任何操作，都是在管理节点上操作的。


以下例子，在一个工作节点上创建一个名为 helloworld 的服务，这里是随机指派给一个工作节点：


```
docker@swarm-manager:~$ docker service create --replicas 1 --name helloworld alpine ping docker.com
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm6.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm6.png)


### 5、查看服务部署情况


查看 helloworld 服务运行在哪个节点上，可以看到目前是在 swarm-worker1 节点：


```
docker@swarm-manager:~$ docker service ps helloworld
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm7.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm7.png)


查看 helloworld 部署的具体信息：


```
docker@swarm-manager:~$ docker service inspect --pretty helloworld
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm8.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm8.png)


### 6、扩展集群服务


我们将上述的 helloworld 服务扩展到俩个节点。


```
docker@swarm-manager:~$ docker service scale helloworld=2
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm9.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm9.png)


可以看到已经从一个节点，扩展到两个节点。


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm10.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm10.png)


### 7、删除服务


```
docker@swarm-manager:~$ docker service rm helloworld
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm11.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm11.png)


查看是否已删除：


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm12.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm12.png)


### 8、滚动升级服务


以下实例，我们将介绍 redis 版本如何滚动升级至更高版本。


创建一个 3.0.6 版本的 redis。


```
docker@swarm-manager:~$ docker service create --replicas 1 --name redis --update-delay 10s redis:3.0.6
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm13.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm13.png)


滚动升级 redis 。


```
docker@swarm-manager:~$ docker service update --image redis:3.0.7 redis
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm14.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm14.png)


看图可以知道 redis 的版本已经从 3.0.6 升级到了 3.0.7，说明服务已经升级成功。


### 9、停止某个节点接收新的任务


查看所有的节点：


```
docker@swarm-manager:~$ docker node ls
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm16.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm16.png)


可以看到目前所有的节点都是 Active, 可以接收新的任务分配。


停止节点 swarm-worker1：


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm17.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm17.png)


**注意**：swarm-worker1 状态变为 Drain。不会影响到集群的服务，只是 swarm-worker1 节点不再接收新的任务，集群的负载能力有所下降。


可以通过以下命令重新激活节点：


```
docker@swarm-manager:~$  docker node update --availability active swarm-worker1
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/swarm19.png)](https://www.runoob.com/wp-content/uploads/2019/11/swarm19.png)








	  AI 思考中...





			** [Docker Machine](https://www.runoob.com/docker-machine.html)
			[Docker 安装 Ubuntu](https://www.runoob.com/docker-install-ubuntu.html) **













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