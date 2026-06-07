# Docker 安装 Python

- Source: https://www.runoob.com/docker/docker-install-python.html

---


## ### 方法一、docker pull python:3.5 查找 Docker Hub 上的 Python 镜像: 可以通过 Sort by 查看其他版本的 python，默认是最新版本 python:latest。 此外，我们还可以用 docker search python 命令来查看可用版本：
```
runoob@runoob:~/python$ docker search python
NAME                           DESCRIPTION                        STARS     OFFICIAL   AUTOMATED
python                         Python is an interpreted,...       982       [OK]
kaggle/python                  Docker image for Python...         33                   [OK]
azukiapp/python                Docker image to run Python ...     3                    [OK]
vimagick/python                mini python                                  2          [OK]
tsuru/python                   Image for the Python ...           2                    [OK]
pandada8/alpine-python         An alpine based python image                 1          [OK]
1science/python                Python Docker images based on ...  1                    [OK]
lucidfrontier45/python-uwsgi   Python with uWSGI                  1                    [OK]
orbweb/python                  Python image                       1                    [OK]
pathwar/python                 Python template for Pathwar levels 1                    [OK]
rounds/10m-python              Python, setuptools and pip.        0                    [OK]
ruimashita/python              ubuntu 14.04 python                0                    [OK]
tnanba/python                  Python on CentOS-7 image.          0                    [OK]
```
 这里我们拉取官方的镜像,标签为3.5
```
runoob@runoob:~/python$ docker pull python:3.5
```
 等待下载完成后，我们就可以在本地镜像列表里查到 REPOSITORY 为python, 标签为 3.5 的镜像。
```
runoob@runoob:~/python$ docker images python:3.5
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
python              3.5              045767ddf24a        9 days ago          684.1 MB
```
 ### 方法二、通过 Dockerfile 构建 创建 Dockerfile/p> 首先，创建目录 python，用于存放后面的相关东西。
```
runoob@runoob:~$ mkdir -p ~/python ~/python/myapp
```
 myapp 目录将映射为 python 容器配置的应用目录。 进入创建的 python 目录，创建 Dockerfile。
```
FROM buildpack-deps:jessie

# remove several traces of debian python
RUN apt-get purge -y python.*

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# gpg: key F73C700D: public key "Larry Hastings <[email protected]>" imported
ENV GPG_KEY 97FC712E4C024BBEA48A61ED3A5CA953F73C700D

ENV PYTHON_VERSION 3.5.1

# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid truth value '<VERSION>'"
ENV PYTHON_PIP_VERSION 8.1.2

RUN set -ex \
        && curl -fSL "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" -o python.tar.xz \
        && curl -fSL "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc" -o python.tar.xz.asc \
        && export GNUPGHOME="$(mktemp -d)" \
        && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \
        && gpg --batch --verify python.tar.xz.asc python.tar.xz \
        && rm -r "$GNUPGHOME" python.tar.xz.asc \
        && mkdir -p /usr/src/python \
        && tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
        && rm python.tar.xz \
        \
        && cd /usr/src/python \
        && ./configure --enable-shared --enable-unicode=ucs4 \
        && make -j$(nproc) \
        && make install \
        && ldconfig \
        && pip3 install --no-cache-dir --upgrade --ignore-installed pip==$PYTHON_PIP_VERSION \
        && find /usr/local -depth \
                \( \
                    \( -type d -a -name test -o -name tests \) \
                    -o \
                    \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
                \) -exec rm -rf '{}' + \
        && rm -rf /usr/src/python ~/.cache

# make some useful symlinks that are expected to exist
RUN cd /usr/local/bin \
        && ln -s easy_install-3.5 easy_install \
        && ln -s idle3 idle \
        && ln -s pydoc3 pydoc \
        && ln -s python3 python \
        && ln -s python3-config python-config

CMD ["python3"]
```
 通过 Dockerfile 创建一个镜像，替换成你自己的名字：
```
runoob@runoob:~/python$ docker build -t python:3.5 .
```
 创建完成后，我们可以在本地的镜像列表里查找到刚刚创建的镜像：
```
runoob@runoob:~/python$ docker images python:3.5
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
python              3.5              045767ddf24a        9 days ago          684.1 MB
```
 使用 python 镜像


在 ~/python/myapp 目录下创建一个 helloworld.py 文件，代码如下：


```
#!/usr/bin/python

print("Hello, World!");
```


### 运行容器


```
runoob@runoob:~/python$ docker run  -v $PWD/myapp:/usr/src/myapp  -w /usr/src/myapp python:3.5 python helloworld.py
```


命令说明：


**-v $PWD/myapp:/usr/src/myapp:** 将主机中当前目录下的 myapp 挂载到容器的 /usr/src/myapp。


**-w /usr/src/myapp: ** 指定容器的 /usr/src/myapp 目录为工作目录。


**python helloworld.py:** 使用容器的 python 命令来执行工作目录中的 helloworld.py 文件。


输出结果：


```
Hello, World!
```









	  AI 思考中...





			** [Docker 安装 Tomcat](https://www.runoob.com/docker-install-tomcat.html)
			[Docker 安装 Redis](https://www.runoob.com/docker-install-redis.html) **













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