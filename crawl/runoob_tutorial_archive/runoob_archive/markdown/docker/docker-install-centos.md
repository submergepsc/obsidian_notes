# Docker 安装 CentOS

- Source: https://www.runoob.com/docker/docker-install-centos.html

CentOS（Community Enterprise Operating System）是 Linux 发行版之一，它是来自于 Red Hat Enterprise Linux(RHEL) 依照开放源代码规定发布的源代码所编译而成。由于出自同样的源代码，因此有些要求高度稳定性的服务器以 CentOS 替代商业版的 Red Hat Enterprise Linux 使用。


### 1、查看可用的 CentOS 版本


访问 CentOS 镜像库地址：[https://hub.docker.com/_/centos?tab=tags&page;=1](https://hub.docker.com/_/centos?tab=tags&page=1)。


可以通过 Sort by 查看其他版本的 CentOS 。默认是最新版本 centos:latest 。


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-centos1.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-centos1.png)


你也可以在下拉列表中找到其他你想要的版本：


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-centos2.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-centos2.png)


### 2、拉取指定版本的 CentOS 镜像，这里我们安装指定版本为例(centos7):


```
$ docker pull centos:centos7
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-centos3.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-centos3.png)


### 3、查看本地镜像


使用以下命令来查看是否已安装了 centos7：


```
$ docker images
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-centos4.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-centos4.png)


### 4、运行容器，并且可以通过 exec 命令进入 CentOS 容器。


```
$ docker run -itd --name centos-test centos:centos7
```


[![](https://www.runoob.com/wp-content/uploads/2019/11/dcoker-centos6.png)](https://www.runoob.com/wp-content/uploads/2019/11/dcoker-centos6.png)


### 5、安装成功


最后我们可以通过 **docker ps** 命令查看容器的运行信息：


[![](https://www.runoob.com/wp-content/uploads/2019/11/docker-centos7.png)](https://www.runoob.com/wp-content/uploads/2019/11/docker-centos7.png)








	  AI 思考中...





			** [Docker 安装 Ubuntu](https://www.runoob.com/docker-install-ubuntu.html)
			[Docker 安装 Node.js](https://www.runoob.com/docker-install-node.html) **













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