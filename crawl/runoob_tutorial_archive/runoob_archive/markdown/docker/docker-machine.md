# Docker Machine

- Source: https://www.runoob.com/docker/docker-machine.html

**
Docker Machine 是 Docker 早期为创建和管理 Docker 主机而生的工具，但随着 Docker Desktop、Terraform 和 Kubernetes 的成熟，它已经完成历史使命，被全面替代。


Docker Desktop 在本地开发场景中 完全替代** 了 Docker Machine，不再适合实际使用。


| 对比项 | Docker Machine | Docker Desktop |
| --- | --- | --- |
| 产品定位 | Docker 主机创建与管理工具 | 本地 Docker 一体化开发环境 |
| 主要用途 | 创建 VM 并安装 Docker Engine | 在本地直接运行 Docker |
| 典型使用时代 | Docker 早期（1.x ～ 18.x） | 当前主流 |
| macOS / Windows 支持 | 间接（依赖 VirtualBox） | 原生支持 |
| 是否需要额外虚拟化软件 | 是（VirtualBox / VMware） | 否（内置） |
| Docker Engine 管理 | 手动/半自动 | 全自动 |
| 使用复杂度 | 高 | 低 |
| 是否提供 GUI | 否 | 是 |
| Kubernetes 支持 | 不支持 | 可选内置 |
| 多 Docker Host 管理 | 支持 | 不支持（侧重单机） |
| 适合生产环境 | 不适合 | 不适合 |
| 官方维护状态 | 基本停止更新 | 持续活跃 |
| 当前推荐度 | ❌ 不推荐 | ✅ 强烈推荐 |


### 简介


Docker Machine 是一种可以让您在虚拟主机上安装 Docker 的工具，并可以使用 docker-machine 命令来管理主机。


Docker Machine 也可以集中管理所有的 docker 主机，比如快速的给 100 台服务器安装上 docker。


![](https://www.runoob.com/wp-content/uploads/2019/11/68747470733a2f2f646f63732e646f63.png)


Docker Machine 管理的虚拟主机可以是机上的，也可以是云供应商，如阿里云，腾讯云，AWS，或 DigitalOcean。


使用 docker-machine 命令，您可以启动，检查，停止和重新启动托管主机，也可以升级 Docker 客户端和守护程序，以及配置 Docker 客户端与您的主机进行通信。


![](https://www.runoob.com/wp-content/uploads/2019/11/machine.png)


---


## 安装


安装 Docker Machine 之前你需要先安装 Docker。


Docker Machine 可以在多种平台上安装使用，包括 Linux 、MacOS 以及 windows。


### Linux 安装命令


```
$ base=https://github.com/docker/machine/releases/download/v0.16.0 &&
  curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
  sudo mv /tmp/docker-machine /usr/local/bin/docker-machine &&
  chmod +x /usr/local/bin/docker-machine
```


### macOS 安装命令


```
$ base=https://github.com/docker/machine/releases/download/v0.16.0 &&
  curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/usr/local/bin/docker-machine &&
  chmod +x /usr/local/bin/docker-machine
```


### Windows 安装命令


如果你是 Windows 平台，可以使用 [Git BASH](https://git-for-windows.github.io/)，并输入以下命令：


```
$ base=https://github.com/docker/machine/releases/download/v0.16.0 &&
  mkdir -p "$HOME/bin" &&
  curl -L $base/docker-machine-Windows-x86_64.exe > "$HOME/bin/docker-machine.exe" &&
  chmod +x "$HOME/bin/docker-machine.exe"
```


查看是否安装成功：


```
$ docker-machine version
docker-machine version 0.16.0, build 9371605
```


**
注意：**各版本更新日志里面也有安装说明：[https://github.com/docker/machine/releases](https://github.com/docker/machine/releases)


---


## 使用


本章通过 virtualbox 来介绍 docker-machine 的使用方法。其他云服务商操作与此基本一致。具体可以参考每家服务商的指导文档。


### 1、列出可用的机器


可以看到目前只有这里默认的 default 虚拟机。


```
$ docker-machine ls
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-machine1.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-machine1.png)


### 2、创建机器


创建一台名为 test 的机器。


```
$ docker-machine create --driver virtualbox test
```


- **--driver**：指定用来创建机器的驱动类型，这里是 virtualbox。


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-machine2.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-machine2.png)


### 3、查看机器的 ip


```
$ docker-machine ip test
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-machine3.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-machine3.png)


### 4、停止机器


```
$ docker-machine stop test
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-machine4.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-machine4.png)

### 5、启动机器


```
$ docker-machine start test
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-machine5.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-machine5.png)


### 6、进入机器


```
$ docker-machine ssh test
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-machine6.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-machine6.png)


### docker-machine 命令参数说明


- **docker-machine active**：查看当前激活状态的 Docker 主机。
```
$ docker-machine ls

NAME      ACTIVE   DRIVER         STATE     URL
dev       -        virtualbox     Running   tcp://192.168.99.103:2376
staging   *        digitalocean   Running   tcp://203.0.113.81:2376

$ echo $DOCKER_HOST
tcp://203.0.113.81:2376

$ docker-machine active
staging
```

- **config**：查看当前激活状态 Docker 主机的连接信息。
- **create**：创建 Docker 主机
- **env**：显示连接到某个主机需要的环境变量
- **inspect**： 以 json 格式输出指定Docker的详细信息
- **ip**： 获取指定 Docker 主机的地址
- **kill**： 直接杀死指定的 Docker 主机
- **ls**： 列出所有的管理主机
- **provision**： 重新配置指定主机
- **regenerate-certs**： 为某个主机重新生成 TLS 信息
- **restart**： 重启指定的主机
- **rm**： 删除某台 Docker 主机，对应的虚拟机也会被删除
- **ssh**： 通过 SSH 连接到主机上，执行命令
- **scp**： 在 Docker 主机之间以及 Docker 主机和本地主机之间通过 scp 远程复制数据
- **mount**： 使用 SSHFS 从计算机装载或卸载目录
- **start**： 启动一个指定的 Docker 主机，如果对象是个虚拟机，该虚拟机将被启动
- **status**： 获取指定 Docker 主机的状态(包括：Running、Paused、Saved、Stopped、Stopping、Starting、Error)等
- **stop**： 停止一个指定的 Docker 主机
- **upgrade**： 将一个指定主机的 Docker 版本更新为最新
- **url**： 获取指定 Docker 主机的监听 URL
- **version**： 显示 Docker Machine 的版本或者主机 Docker 版本
- **help**： 显示帮助信息








	  AI 思考中...





			** [Docker Compose](https://www.runoob.com/docker-compose.html)
			[Swarm 集群管理](https://www.runoob.com/docker-swarm.html) **













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