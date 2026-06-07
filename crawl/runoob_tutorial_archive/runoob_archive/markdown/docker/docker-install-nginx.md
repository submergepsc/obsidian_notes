# Docker 安装 Nginx

- Source: https://www.runoob.com/docker/docker-install-nginx.html

Nginx 是一个高性能的 HTTP 和反向代理 web 服务器，同时也提供了 IMAP/POP3/SMTP 服务 。


### 1、查看可用的 Nginx 版本


访问 Nginx 镜像库地址： [https://hub.docker.com/_/nginx?tab=tags](https://hub.docker.com/_/nginx?tab=tags)。


可以通过 Sort by 查看其他版本的 Nginx，默认是最新版本 **nginx:latest**。


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-nginx1.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-nginx1.png)


你也可以在下拉列表中找到其他你想要的版本：


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-nginx2.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-nginx2.png)


此外，我们还可以用 **docker search nginx** 命令来查看可用版本：


```
$ docker search nginx
NAME                      DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
nginx                     Official build of Nginx.                        3260      [OK]
jwilder/nginx-proxy       Automated Nginx reverse proxy for docker c...   674                  [OK]
richarvey/nginx-php-fpm   Container running Nginx + PHP-FPM capable ...   207                  [OK]
million12/nginx-php       Nginx + PHP-FPM 5.5, 5.6, 7.0 (NG), CentOS...   67                   [OK]
maxexcloo/nginx-php       Docker framework container with Nginx and ...   57                   [OK]
...
```


### 2、取最新版的 Nginx 镜像


这里我们拉取官方的最新版本的镜像：


```
$ docker pull nginx:latest
```


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-nginx3.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-nginx3.png)


### 3、查看本地镜像


使用以下命令来查看是否已安装了 nginx：


```
$ docker images
```


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-nginx4.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-nginx4.png)


在上图中可以看到我们已经安装了最新版本（latest）的 nginx 镜像。


### 4、运行容器


安装完成后，我们可以使用以下命令来运行 nginx 容器：


```
$ docker run --name nginx-test -p 8080:80 -d nginx
```


参数说明：


- **--name nginx-test**：容器名称。
- **-p 8080:80**： 端口进行映射，将本地 8080 端口映射到容器内部的 80 端口。
- **-d nginx**： 设置容器在在后台一直运行。


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-nginx5.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-nginx5.png)


### 5、安装成功


最后我们可以通过浏览器可以直接访问 8080 端口的 nginx 服务：


[![](https://www.runoob.com/wp-content/uploads/2016/06/docker-nginx6.png)](https://www.runoob.com/wp-content/uploads/2016/06/docker-nginx6.png)








	  AI 思考中...





			** [Docker 容器连接](https://www.runoob.com/docker-container-connection.html)
			[Docker 安装 MySQL](https://www.runoob.com/docker-install-mysql.html) **













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