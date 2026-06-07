# CentOS Docker 安装

- Source: https://www.runoob.com/docker/centos-docker-install.html

Docker 支持以下的 64 位 CentOS 版本：


- CentOS 9 (stream)
- 更高版本...

必须启用 centos-extras 仓库，该仓库默认启用，如果您禁用了它，需要重新启用。


---


## 使用官方安装脚本自动安装


安装命令如下：


```
$ curl -fsSL https://get.docker.com -o install-docker.sh
$ sudo sh install-docker.sh
```


---


## 手动安装


### 卸载旧版本


较旧的 Docker 版本称为 docker 或 docker-engine，如果已安装这些程序，请卸载它们以及相关的依赖项。


运行以下命令卸载旧版本：


```docker
sudo dnf remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
```


### 安装


### 使用 Docker 仓库进行安装


在新主机上首次安装 Docker 之前，需要设置 Docker 仓库。之后，您可以从仓库安装和更新 Docker。


**设置仓库**


安装 dnf-plugins-core 包（提供管理 DNF 仓库的命令），并设置仓库。


```docker
sudo dnf -y install dnf-plugins-core
```


使用以下命令来设置稳定的仓库。


## 使用官方源地址（比较慢）


```docker
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```


可以执行以下命令换成清华大学的镜像源：


## 清华大学镜像源


```docker
sed -i 's+https://download.docker.com+https://mirrors.tuna.tsinghua.edu.cn/docker-ce+' /etc/yum.repos.d/docker-ce.repo
```


参考地址：[https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/](https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/)


### 安装


运行以下命令安装Docker：：


```
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```


如果提示接受 GPG 密钥，验证指纹是否与 060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35 匹配，如果匹配则接受。


安装成功后，启动 Docker 引擎：


```
sudo systemctl start docker
```


如果希望 Docker 在系统启动时也启动可以使用以下命令：


```
sudo systemctl enable --now docker
```


以上命令会配置 Docker 的 systemd 服务，在系统启动时自动启动 Docker。


Docker 安装完默认未启动。并且已经创建好 docker 用户组，但该用户组下没有用户。


运行以下命令来验证安装是否成功：


```
sudo docker run hello-world
```


此命令会下载一个测试镜像，并在容器中运行，当容器运行时，会打印确认消息并退出。


### 卸载 docker


删除安装包：


```
yum remove docker-ce
```


删除镜像、容器、配置文件等内容：


```
rm -rf /var/lib/docker
```









	  AI 思考中...





			** [Docker 教程](https://www.runoob.com/docker-tutorial.html)
			[Windows Docker 安装](https://www.runoob.com/windows-docker-install.html) **













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