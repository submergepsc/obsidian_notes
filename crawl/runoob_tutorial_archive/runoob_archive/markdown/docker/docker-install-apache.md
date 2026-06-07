# Docker 安装 Apache

- Source: https://www.runoob.com/docker/docker-install-apache.html

---


### 方法一、docker pull httpd


查找 [Docker Hub](https://hub.docker.com/_/httpd?tab=tags) 上的 httpd 镜像:


[![](https://www.runoob.com/wp-content/uploads/2016/06/DD4D706F-7D45-41F6-9506-069E12A87F9D.jpg)](https://www.runoob.com/wp-content/uploads/2016/06/DD4D706F-7D45-41F6-9506-069E12A87F9D.jpg)


可以通过 Sort by 查看其他版本的 httpd，默认是最新版本 **httpd:latest**。


此外，我们还可以用 docker search httpd 命令来查看可用版本：


```
runoob@runoob:~/apache$ docker search httpd
NAME                           DESCRIPTION                  STARS  OFFICIAL AUTOMATED
httpd                          The Apache HTTP Server ..    524     [OK]
centos/httpd                                                7                [OK]
rgielen/httpd-image-php5       Docker image for Apache...   1                [OK]
microwebapps/httpd-frontend    Httpd frontend allowing...   1                [OK]
lolhens/httpd                  Apache httpd 2 Server        1                [OK]
publici/httpd                  httpd:latest                 0                [OK]
publicisworldwide/httpd        The Apache httpd webser...   0                [OK]
rgielen/httpd-image-simple     Docker image for simple...   0                [OK]
solsson/httpd                  Derivatives of the offi...   0                [OK]
rgielen/httpd-image-drush      Apache HTTPD + Drupal S...   0                [OK]
learninglayers/httpd                                        0                [OK]
sohrabkhan/httpd               Docker httpd + php5.6 (...   0                [OK]
aintohvri/docker-httpd         Apache HTTPD Docker ext...   0                [OK]
alizarion/httpd                httpd on centos with mo...   0                [OK]
...
```


这里我们拉取官方的镜像


```
runoob@runoob:~/apache$ docker pull httpd
```


等待下载完成后，我们就可以在本地镜像列表里查到REPOSITORY为httpd的镜像。


```
runoob@runoob:~/apache$ docker images httpd
REPOSITORY     TAG        IMAGE ID        CREATED           SIZE
httpd          latest     da1536b4ef14    23 seconds ago    195.1 MB
```


### 方法二、通过 Dockerfile 构建


**创建 Dockerfile**


首先，创建目录apache,用于存放后面的相关东西。


```
runoob@runoob:~$ mkdir -p  ~/apache/www ~/apache/logs ~/apache/conf
```


www 目录将映射为 apache 容器配置的应用程序目录。


logs 目录将映射为 apache 容器的日志目录。


conf 目录里的配置文件将映射为 apache 容器的配置文件。


进入创建的 apache 目录，创建 Dockerfile。


```
FROM debian:jessie

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
#RUN groupadd -r www-data && useradd -r --create-home -g www-data www-data

ENV HTTPD_PREFIX /usr/local/apache2
ENV PATH $PATH:$HTTPD_PREFIX/bin
RUN mkdir -p "$HTTPD_PREFIX" \
    && chown www-data:www-data "$HTTPD_PREFIX"
WORKDIR $HTTPD_PREFIX

# install httpd runtime dependencies
# https://httpd.apache.org/docs/2.4/install.html#requirements
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libapr1 \
        libaprutil1 \
        libaprutil1-ldap \
        libapr1-dev \
        libaprutil1-dev \
        libpcre++0 \
        libssl1.0.0 \
    && rm -r /var/lib/apt/lists/*

ENV HTTPD_VERSION 2.4.20
ENV HTTPD_BZ2_URL https://www.apache.org/dist/httpd/httpd-$HTTPD_VERSION.tar.bz2

RUN buildDeps=' \
        ca-certificates \
        curl \
        bzip2 \
        gcc \
        libpcre++-dev \
        libssl-dev \
        make \
    ' \
    set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends $buildDeps \
    && rm -r /var/lib/apt/lists/* \
    \
    && curl -fSL "$HTTPD_BZ2_URL" -o httpd.tar.bz2 \
    && curl -fSL "$HTTPD_BZ2_URL.asc" -o httpd.tar.bz2.asc \
# see https://httpd.apache.org/download.cgi#verify
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys A93D62ECC3C8EA12DB220EC934EA76E6791485A8 \
    && gpg --batch --verify httpd.tar.bz2.asc httpd.tar.bz2 \
    && rm -r "$GNUPGHOME" httpd.tar.bz2.asc \
    \
    && mkdir -p src \
    && tar -xvf httpd.tar.bz2 -C src --strip-components=1 \
    && rm httpd.tar.bz2 \
    && cd src \
    \
    && ./configure \
        --prefix="$HTTPD_PREFIX" \
        --enable-mods-shared=reallyall \
    && make -j"$(nproc)" \
    && make install \
    \
    && cd .. \
    && rm -r src \
    \
    && sed -ri \
        -e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \
        -e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \
        "$HTTPD_PREFIX/conf/httpd.conf" \
    \
    && apt-get purge -y --auto-remove $buildDeps

COPY httpd-foreground /usr/local/bin/

EXPOSE 80
CMD ["httpd-foreground"]
```


Dockerfile文件中 COPY httpd-foreground /usr/local/bin/ 是将当前目录下的httpd-foreground拷贝到镜像里，作为httpd服务的启动脚本，所以我们要在本地创建一个脚本文件httpd-foreground


```
#!/bin/bash
set -e

# Apache gets grumpy about PID files pre-existing
rm -f /usr/local/apache2/logs/httpd.pid

exec httpd -DFOREGROUND
```


赋予 httpd-foreground 文件可执行权限。


```
runoob@runoob:~/apache$ chmod +x httpd-foreground
```


通过 Dockerfile 创建一个镜像，替换成你自己的名字。


```
runoob@runoob:~/apache$ docker build -t httpd .
```


创建完成后，我们可以在本地的镜像列表里查找到刚刚创建的镜像。


```
runoob@runoob:~/apache$ docker images httpd
REPOSITORY     TAG        IMAGE ID        CREATED           SIZE
httpd          latest     da1536b4ef14    23 seconds ago    195.1 MB
```


---


## 使用 apache 镜像


### 运行容器


```
docker run -p 80:80 -v $PWD/www/:/usr/local/apache2/htdocs/ -v $PWD/conf/httpd.conf:/usr/local/apache2/conf/httpd.conf -v $PWD/logs/:/usr/local/apache2/logs/ -d httpd
```


命令说明：


**-p 80:80:**第一个 80 端口为主机端口，后面一个是容器端口，效果为将容器的 80 端口映射到主机的 80 端口。


**-v $PWD/www/:/usr/local/apache2/htdocs/:** 将主机中当前目录下的 www 目录挂载到容器的 /usr/local/apache2/htdocs/。


**-v $PWD/conf/httpd.conf:/usr/local/apache2/conf/httpd.conf:** 将主机中当前目录下的 conf/httpd.conf 文件挂载到容器的 /usr/local/apache2/conf/httpd.conf。


**-v $PWD/logs/:/usr/local/apache2/logs/:** 将主机中当前目录下的 logs 目录挂载到容器的 /usr/local/apache2/logs/。


更详细的命令参考：[Docker run 命令](https://www.runoob.com/docker-run-command.html)


查看容器启动情况：


```
runoob@runoob:~/apache$ docker ps
CONTAINER ID  IMAGE   COMMAND             ... PORTS               NAMES
79a97f2aac37  httpd   "httpd-foreground"  ... 0.0.0.0:80->80/tcp  sharp_swanson
```


通过浏览器访问


![](https://www.runoob.com/wp-content/uploads/2016/06/apache.png)









	  AI 思考中...





			** [Docker 安装 MongoDB](https://www.runoob.com/docker-install-mongodb.html)
			[Docker 命令大全](https://www.runoob.com/docker-command-manual.html) **













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