# Docker 教程

- Source: https://www.runoob.com/docker/docker-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2016/04/docker01.png)

Docker 是一个开源的应用容器引擎，基于 [Go 语言](https://www.runoob.com/../go/go-tutorial.html) 并遵从 Apache2.0 协议开源。

Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。


容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。


Docker 从 17.03 版本之后分为 CE（Community Edition: 社区版） 和 EE（Enterprise Edition: 企业版），我们用社区版就可以了。


---


## 谁适合阅读本教程？


本教程适合运维工程师及后端开发人员，通过本教程你可以一步一步了解 Docker 的使用。


---


## 阅读本教程前，您需要了解的知识


在阅读本教程前，你需要掌握 Linux 的常用命令。你可以通过本站的 [Linux 教程](https://www.runoob.com/../linux/linux-tutorial.html) 来学习相关命令。


---


## Docker 的应用场景


- **微服务架构：**每个服务独立容器化，便于管理和扩展。
- **CI/CD流水线：**与 Jenkins/GitLab CI 集成，实现自动化构建和测试。
- ** 开发环境标准化：**新成员一键启动全套依赖服务（如数据库、消息队列）。
- **云原生基础：**Kubernetes 等编排工具基于 Docker 管理容器集群。


---


## 核心优势

- **跨平台一致性：**解决"在我机器上能跑"的问题，确保开发、测试、生产环境一致。
- **资源高效：**容器直接共享主机内核，无需虚拟化整个操作系统，节省内存和 CPU。
- **快速部署：**秒级启动容器，支持自动化扩缩容。
- **隔离性：**每个容器拥有独立的文件系统、网络和进程空间。


---


## 核心概念

- **容器（Container）：**轻量化的运行实例，包含应用代码、运行时环境和依赖库。基于镜像创建，与其他容器隔离，共享主机操作系统内核（比虚拟机更高效）。
- **镜像（Image）：**只读模板，定义了容器的运行环境（如操作系统、软件配置等）。通过分层存储（Layer）优化空间和构建速度。
- **Dockerfile：**文本文件，描述如何自动构建镜像（例如指定基础镜像、安装软件、复制文件等）。
- ** 仓库（Registry）：**存储和分发镜像的平台，如 Docker Hub（官方公共仓库）或私有仓库（如 Harbor）。

---


## 基本命令


## 实例


```docker
# 拉取镜像（如官方Nginx镜像）
docker pull nginx

# 运行容器（-d 后台运行，-p 映射端口）
docker run -d -p 80:80 nginx

# 查看运行中的容器
docker ps

# 构建镜像（基于当前目录的Dockerfile）
docker build -t my-app .

# 进入容器内部
docker exec -it <容器ID> /bin/bash
```


---


## 相关链接


Docker 官网：[https://www.docker.com](https://www.docker.com)


Github Docker 源码：[https://github.com/docker](https://github.com/docker)








	  AI 思考中...






			[CentOS Docker 安装](https://www.runoob.com/centos-docker-install.html) **













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