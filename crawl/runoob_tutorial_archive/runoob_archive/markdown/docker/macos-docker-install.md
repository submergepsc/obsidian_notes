# MacOS Docker 安装

- Source: https://www.runoob.com/docker/macos-docker-install.html

## 使用 Homebrew 安装


macOS 我们可以使用 Homebrew 来安装 Docker。


Homebrew 的 Cask 已经支持 Docker for Mac，因此可以很方便的使用 Homebrew Cask 来进行安装：


```
$ brew install --cask --appdir=/Applications docker

==> Creating Caskroom at /usr/local/Caskroom
==> We'll set permissions properly so we won't need sudo in the future
Password:          # 输入 macOS 密码
==> Satisfying dependencies
==> Downloading https://download.docker.com/mac/stable/21090/Docker.dmg
######################################################################## 100.0%
==> Verifying checksum for Cask docker
==> Installing Cask docker
==> Moving App 'Docker.app' to '/Applications/Docker.app'.
&#x1f37a;  docker was successfully installed!
```


在载入 Docker app 后，点击 Next，可能会询问你的 macOS 登陆密码，你输入即可。之后会弹出一个 Docker 运行的提示窗口，状态栏上也有有个小鲸鱼的图标（![](https://www.runoob.com/wp-content/uploads/2018/01/1515480613-2248-whale-x.png)）。

---


## 手动下载安装


如果需要手动下载，请点击以下链接下载 [Install Docker Desktop on Mac](https://docs.docker.com/docker-for-mac/install/) 。


![](https://www.runoob.com/wp-content/uploads/2018/01/1E045CE6-D504-4E7D-8C57-EEFB8AC83BF1.jpg)


如同 macOS 其它软件一样，安装也非常简单，双击下载的 .dmg 文件，然后将鲸鱼图标拖拽到 Application 文件夹即可。


![](https://www.runoob.com/wp-content/uploads/2018/01/1515480386-7270-1293367-9516b2edf79deee7.png)


从应用中找到 Docker 图标并点击运行。可能会询问 macOS 的登陆密码，输入即可。

![](https://www.runoob.com/wp-content/uploads/2018/01/1515480613-7638-docker-app-in-apps.png)


点击顶部状态栏中的鲸鱼图标会弹出操作菜单。


![](https://www.runoob.com/wp-content/uploads/2018/01/1515480612-6026-whale-in-menu-bar.png)


![](https://www.runoob.com/wp-content/uploads/2018/01/1515480613-8590-menu.png)


第一次点击图标，可能会看到这个安装成功的界面，点击 "Got it!" 可以关闭这个窗口。


![](https://www.runoob.com/wp-content/uploads/2018/01/1515480614-7648-install-success-docker-cloud.png)


启动终端后，通过命令可以检查安装后的 Docker 版本。


```
$ docker --version
Docker version 17.09.1-ce, build 19e2cf6
```


## 镜像加速


鉴于国内网络问题，后续拉取 Docker 镜像十分缓慢，我们可以需要配置加速器来解决，我使用的是网易的镜像地址：**http://hub-mirror.c.163.com**。

在任务栏点击 Docker for mac 应用图标 -> Perferences... -> Daemon -> Registry mirrors。在列表中填写加速器地址即可。修改完成之后，点击 Apply & Restart 按钮，Docker 就会重启并应用配置的镜像地址了。


![](https://www.runoob.com/wp-content/uploads/2018/01/6B76CF7C-DC88-4DB4-8305-31EEF4323372.png)


之后我们可以通过 docker info 来查看是否配置成功。


```
$ docker info
...
Registry Mirrors:
 http://hub-mirror.c.163.com
Live Restore Enabled: false
```










	  AI 思考中...





			** [Docker 资源汇总](https://www.runoob.com/docker-resources.html)
			[Docker load 命令](https://www.runoob.com/docker-load-command.html) **













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