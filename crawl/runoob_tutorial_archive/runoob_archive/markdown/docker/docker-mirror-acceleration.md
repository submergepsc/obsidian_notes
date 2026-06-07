# Docker 镜像加速

- Source: https://www.runoob.com/docker/docker-mirror-acceleration.html

国内从 DockerHub 拉取镜像有时会遇到困难，此时可以配置镜像加速器。


目前国内 Docker 镜像源出现了一些问题，基本不能用了，后期能用我再更新下。


Docker 官方和国内很多云服务商都提供了国内加速器服务，例如：


- 科大镜像：**https://docker.mirrors.ustc.edu.cn/**
- 网易：**https://hub-mirror.c.163.com/**
- 阿里云：**https://.mirror.aliyuncs.com**
- 七牛云加速器：**https://reg-mirror.qiniu.com**


当配置某一个加速器地址之后，若发现拉取不到镜像，请切换到另一个加速器地址。国内各大云服务商均提供了 Docker 镜像加速服务，建议根据运行 Docker 的云平台选择对应的镜像加速服务。


阿里云镜像获取地址：[https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors)，登陆后，左侧菜单选中镜像加速器就可以看到你的专属地址了：


![](https://www.runoob.com/wp-content/uploads/2019/10/02F3AF04-8203-4E3B-A5AF-96973DBE515F.jpg)


之前还有 Docker 官方加速器 **https://registry.docker-cn.com** ，现在好像已经不能使用了，我们可以多添加几个国内的镜像，如果有不能使用的，会切换到可以使用的镜像来拉取。


### Ubuntu14.04、Debian7Wheezy


对于使用 upstart 的系统而言，编辑 /etc/default/docker 文件，在其中的 DOCKER_OPTS 中配置加速器地址：


```
DOCKER_OPTS="--registry-mirror=https://registry.docker-cn.com"
```


重新启动服务:


```
$ sudo service docker restart
```


### Ubuntu16.04+、Debian8+、CentOS7


对于使用 systemd 的系统，请在 /etc/docker/daemon.json 中写入如下内容（如果文件不存在请新建该文件）：


```
{"registry-mirrors":["https://reg-mirror.qiniu.com/"]}
```


之后重新启动服务：


```docker
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```


### Windows 10


对于使用 Windows 10 的系统，在系统右下角托盘 Docker 图标内右键菜单选择 Settings，打开配置窗口后左侧导航菜单选择 Daemon。在 Registrymirrors 一栏中填写加速器地址 **https://docker.mirrors.ustc.edu.cn/** ，之后点击 Apply 保存后 Docker 就会重启并应用配置的镜像地址了。


![](https://www.runoob.com/wp-content/uploads/2019/10/38507F68-E30F-4CCA-AE9D-9E9EEF60EC83.jpg)


### Mac OS X


对于使用 Mac OS X 的用户，在任务栏点击 Docker for mac 应用图标-> Perferences...-> Daemon-> Registrymirrors。在列表中填写加速器地址 **https://reg-mirror.qiniu.com** 。修改完成之后，点击 Apply&Restart; 按钮，Docker 就会重启并应用配置的镜像地址了。


![](https://www.runoob.com/wp-content/uploads/2019/10/D26C96AF-8EFF-46E5-8618-4C67E72ACBAF.jpg)


### 检查加速器是否生效


检查加速器是否生效配置加速器之后，如果拉取镜像仍然十分缓慢，请手动检查加速器配置是否生效，在命令行执行 **docker info**，如果从结果中看到了如下内容，说明配置成功。


```
$ docker info
Registry Mirrors:
    https://reg-mirror.qiniu.com
```










	  AI 思考中...





			** [Debian Docker 安装](https://www.runoob.com/debian-docker-install.html)
			[Docker 仓库管理](https://www.runoob.com/docker-repository.html) **













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