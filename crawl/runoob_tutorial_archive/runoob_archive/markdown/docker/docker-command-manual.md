# Docker 命令大全

- Source: https://www.runoob.com/docker/docker-command-manual.html

---


### 容器生命周期管理

- [run - 创建并启动一个新的容器。](https://www.runoob.com/docker-run-command.html)
- [start/stop/restart - 这些命令主要用于启动、停止和重启容器。](https://www.runoob.com/docker-start-stop-restart-command.html)
- [kill - 立即终止一个或多个正在运行的容器](https://www.runoob.com/docker-kill-command.html)
- [rm - 于删除一个或多个已经停止的容器。](https://www.runoob.com/docker-rm-command.html)
- [pause/unpause - 暂停和恢复容器中的所有进程。](https://www.runoob.com/docker-pause-unpause-command.html)
- [create - 创建一个新的容器，但不会启动它。](https://www.runoob.com/docker-create-command.html)
- [exec - 在运行中的容器内执行一个新的命令。](https://www.runoob.com/docker-exec-command.html)
- [rename - 重命名容器。](https://www.runoob.com/docker-rename-command.html)


### 容器操作

- [ps - 列出 Docker 容器](https://www.runoob.com/docker-ps-command.html)
- [inspect - 获取 Docker 对象（容器、镜像、卷、网络等）的详细信息。](https://www.runoob.com/docker-inspect-command.html)
- [top - 显示指定容器中的正在运行的进程。](https://www.runoob.com/docker-top-command.html)
- [attach - 允许用户附加到正在运行的容器并与其交互。](https://www.runoob.com/docker-attach-command.html)
- [events - 获取 Docker 守护进程生成的事件。](https://www.runoob.com/docker-events-command.html)
- [logs - 获取和查看容器的日志输出。](https://www.runoob.com/docker-logs-command.html)
- [wait - 允许用户等待容器停止并获取其退出代码。](https://www.runoob.com/docker-wait-command.html)
- [export - 将容器的文件系统导出为 tar 归档文件。](https://www.runoob.com/docker-export-command.html)
- [port - 显示容器的端口映射信息。](https://www.runoob.com/docker-port-command.html)
- [stats - 实时显示 Docker 容器的资源使用情况。](https://www.runoob.com/docker-stats-command.html)
- [update - 更新 Docker 容器的资源限制，包括内存、CPU 等。](https://www.runoob.com/docker-update-command.html)


### 容器的root文件系统（rootfs）命令

- [commit - 允许用户将容器的当前状态保存为新的 Docker 镜像。](https://www.runoob.com/docker-commit-command.html)
- [cp - 用于在容器和宿主机之间复制文件或目录。](https://www.runoob.com/docker-cp-command.html)
- [diff - 显示 Docker 容器文件系统的变更。](https://www.runoob.com/docker-diff-command.html)


### 镜像仓库

- [login/logout - 管理 Docker 客户端与 Docker 注册表的身份验证。](https://www.runoob.com/docker-login-command.html)
- [pull - 从 Docker 注册表（例如 Docker Hub）中拉取（下载）镜像到本地。](https://www.runoob.com/docker-pull-command.html)
- [push - 将本地构建的 Docker 镜像推送（上传）到 Docker 注册表（如 Docker Hub 或私有注册表）。](https://www.runoob.com/docker-push-command.html)
- [search - 用于在 Docker Hub 或其他注册表中搜索镜像。](https://www.runoob.com/docker-search-command.html)


### 本地镜像管理

- [images - 列出本地的 Docker 镜像。](https://www.runoob.com/docker-images-command.html)
- [rmi - 删除不再需要的镜像。](https://www.runoob.com/docker-rmi-command.html)
- [tag - 创建本地镜像的别名（tag）。](https://www.runoob.com/docker-tag-command.html)
- [build - 从 Dockerfile 构建 Docker 镜像。](https://www.runoob.com/docker-build-command.html)
- [history - 查看指定镜像的历史层信息。](https://www.runoob.com/docker-history-command.html)
- [save - 将一个或多个 Docker 镜像保存到一个 tar 归档文件中。](https://www.runoob.com/docker-save-command.html)
- [load - 从由 docker save 命令生成的 tar 文件中加载 Docker 镜像。](https://www.runoob.com/docker-load-command.html)
- [import - 从一个 tar 文件或 URL 导入容器快照，从而创建一个新的 Docker 镜像。](https://www.runoob.com/docker-import-command.html)


### info|version

- [info - 显示 Docker 的系统级信息，包括当前的镜像和容器数量。](https://www.runoob.com/docker-info-command.html)
- [version - 显示 Docker 客户端和服务端的版本信息。](https://www.runoob.com/docker-version-command.html)


### Docker Compose

- [docker compose run - 启动一个新容器并运行一个特定的应用程序。](https://www.runoob.com/docker-compose-run-command.html)
- [docker compose rm - 启动一个新容器并删除一个特定的应用程序。](https://www.runoob.com/docker-compose-rm-command.html)
- [docker compose ps - 从 docker compose 检查 docker 容器状态。](https://www.runoob.com/docker-compose-ps-command.html)
- [docker compose build - 构建 docker compose 文件。](https://www.runoob.com/docker-compose-bulid-command.html)
- [docker compose up - 运行 docker compose 文件。](https://www.runoob.com/docker-compose-up-command.html)
- [docker compose ls - 列出 docker compose 服务。](https://www.runoob.com/docker-compose-ls-command.html)
- [docker compose start - 启动 docker compose 文件创建的容器。](https://www.runoob.com/docker-compose-start-command.html)
- [docker compose restart - 重启 docker compose 文件创建的容器。](https://www.runoob.com/docker-compose-restart-command.html)


### 网络命令


- **`docker network ls`**: 列出所有网络。
- **`docker network create `**: 创建一个新的网络。
- **`docker network rm `**: 删除指定的网络。
- **`docker network connect  `**: 连接容器到网络。
- **`docker network disconnect  `**: 断开容器与网络的连接。


详细内容查看：[docker network 命令](https://www.runoob.com/docker-network-command.html)


### 卷命令


- **`docker volume ls`**: 列出所有卷。
- **`docker volume create `**: 创建一个新的卷。
- **`docker volume rm `**: 删除指定的卷。
- **`docker volume inspect `**: 显示卷的详细信息。


详细内容查看：[docker volume 命令](https://www.runoob.com/docker-volume-command.html)








	  AI 思考中...





			** [Docker 安装 Apache](https://www.runoob.com/docker-install-apache.html)
			[Docker run 命令](https://www.runoob.com/docker-run-command.html) **













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