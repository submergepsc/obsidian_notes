# Debian Docker 安装

- Source: https://www.runoob.com/docker/debian-docker-install.html

Docker 支持以下的 64 位 Debian 版本：


- Debian Bookworm 12 （稳定版）
- Debian Bullseye 11 （旧稳定版）


支持的架构包括 x86_64（amd64）、armhf、arm64 和 ppc64le。


### 卸载旧版本

如果你之前安装过 Docker Engine 之前，你需要卸载旧版本，避免冲突：


```
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```


---


## 使用官方安装脚本自动安装


安装命令如下：


```
curl -fsSL https://get.docker.com -o get-docker.sh
 sudo sh get-docker.sh
```


---

---


## 手动安装


### 1. 更新软件包

首先，更新现有的软件包和包缓存：


```
sudo apt update
sudo apt upgrade
```


### 2. 安装依赖包

安装一些需要的依赖包，这些包允许 apt 使用 HTTPS 协议来访问 Docker 仓库：


```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```


### 3. 添加 Docker 官方 GPG 密钥

使用下面的命令来添加 Docker 官方的 GPG 密钥：


```
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```


### 4. 添加 Docker 仓库

添加 Docker 官方的 APT 软件源：


```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# 更新
sudo apt-get update
```


### 5. 更新 APT 软件包缓存

添加仓库后，更新 APT 包索引：


```
sudo apt update
```


确保你现在从 Docker 官方仓库安装 Docker 而不是 Debian 默认仓库：


```
apt-cache policy docker-ce
```


你应该看到它指向 https://download.docker.com/，确保这就是官方的 Docker 仓库。


### 6. 安装 Docker

现在，你可以安装 Docker：


```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```


### 7. 启动并验证 Docker

启动 Docker 并设置为开机自启：


```
sudo systemctl start docker
sudo systemctl enable docker
```


你可以使用以下命令来验证 Docker 是否安装成功：


```
sudo docker --version
```


运行以下测试命令确保 Docker 正常工作：


```
sudo docker run hello-world
```


### 卸载 docker


删除安装包：


```
sudo apt-get purge docker-ce
```


删除镜像、容器、配置文件等内容：


```
sudo rm -rf /var/lib/docker
```









	  AI 思考中...





			** [Docker load 命令](https://www.runoob.com/docker-load-command.html)
			[Docker 镜像加速](https://www.runoob.com/docker-mirror-acceleration.html) **













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