# Docker Desktop

- Source: https://www.runoob.com/docker/docker-desktop.html

**Docker Desktop** 是 Docker 官方推出的 **本地容器化开发环境**，用于在 **macOS / Windows（以及部分 Linux）** 上：


- 运行 Docker Engine
- 构建、运行、管理容器和镜像
- 提供图形化管理界面（GUI）
- 集成 Kubernetes（可选）


一句话概括：

**

Docker Desktop = Docker Engine + Linux VM + GUI + 开发者体验优化


Docker Desktop 已经成为 本地 Docker 开发的事实标准**。


### 为什么要使用 Docker Desktop


在没有 Docker Desktop 之前，本地使用 Docker 存在大量问题：


- macOS / Windows 不能原生运行 Docker
- 需要手动安装虚拟机（VirtualBox）
- 网络、文件挂载、端口映射配置复杂


Docker Desktop 解决了这些问题：


| 能力 | 说明 |
| --- | --- |
| 一键安装 | 自动完成虚拟化与 Docker 安装 |
| 开箱即用 | 安装完成即可使用 |
| 图形界面 | 容器、镜像、日志可视化 |
| CLI 兼容 | 与原生 docker 命令完全一致 |
| Kubernetes | 可一键启用本地 K8s |


---


## Docker Desktop 的整体架构


理解架构有助于避免常见误解。


```
宿主系统（macOS / Windows）
 └── Docker Desktop
      └── Linux 虚拟机
           └── Docker Engine
                ├── Images
                ├── Containers
                └── Volumes
```


**关键点：**


- Docker 实际运行在 **Linux VM 中**
- 本地看到的文件、端口、进程是"映射结果"
- 这也是文件挂载、性能问题的根源


![](https://www.runoob.com/wp-content/uploads/2026/01/dd-desktop-runoob.png)


---


## 安装 Docker Desktop


### 系统要求


- macOS（Apple Silicon / Intel）
- Windows 10 / 11（建议 WSL2）
- 至少 4GB 内存（推荐 8GB+）


### 安装流程（概念性说明）


- 下载 Docker Desktop 安装包，下载地址：[https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/) ![](https://www.runoob.com/wp-content/uploads/2026/01/d8535208-f233-4640-a097-719ec8fcb35b.png)
- 拖入应用目录 / 完成安装向导，Windows 用户在安装过程中确保勾选 "Use WSL 2 instead of Hyper-V"。
- 启动 Docker Desktop
- 等待 Docker Engine 启动完成


启动成功后：


- 菜单栏出现 Docker 图标
- `docker version` 能正常输出


---


## Docker Desktop 界面快速认识


Docker Desktop 的 GUI 主要分为以下模块：


| 模块 | 作用 |
| --- | --- |
| Containers | 管理正在运行的容器 |
| Images | 查看本地镜像 |
| Volumes | 管理数据卷 |
| Builds | 构建记录 |
| Settings | 配置资源、网络、K8s |


![](https://www.runoob.com/wp-content/uploads/2026/01/DD-hiroko.png)

---


## 核心概念：镜像与容器


理解 Docker 只需要记住这个简单的类比：


| 概念 | 类比 | 说明 |
| --- | --- | --- |
| 镜像 (Image) | 菜谱 | 只读的文件，包含了运行程序所需的所有代码、环境和库。 |
| 容器 (Container) | 做好的菜 | 镜像的运行实例。你可以根据一个菜谱做很多盘菜。 |
| 仓库 (Registry) | 美食广场 | 存储和分享镜像的地方，最著名的是 Docker Hub。 |








	  AI 思考中...





			** [Docker 基础概念](https://www.runoob.com/docker-intro.html)














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