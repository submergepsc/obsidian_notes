# Node.js JXcore 打包

- Source: https://www.runoob.com/nodejs/nodejs-jxcore-packaging.html

Node.js 是一个开放源代码、跨平台的、用于服务器端和网络应用的运行环境。


JXcore 是一个支持多线程的 Node.js 发行版本，基本不需要对你现有的代码做任何改动就可以直接线程安全地以多线程运行。


这篇文章主要是要向大家介绍 JXcore 的打包功能。


---


## JXcore 安装


下载 JXcore 安装包，并解压，在解压的的目录下提供了 jx 二进制文件命令，接下来我们主要使用这个命令。


### 步骤1、下载


下载 JXcore 安装包 [https://github.com/jxcore/jxcore-release](https://github.com/jxcore/jxcore-release)，你需要根据你自己的系统环境来下载安装包。


1、Window 平台下载：[Download(Windows x64 (V8))](https://raw.githubusercontent.com/jxcore/jxcore-release/master/0311/jx_win64v8.zip)。


2、Linux/OSX 安装命令：


```
$ curl https://raw.githubusercontent.com/jxcore/jxcore/master/tools/jx_install.sh | bash
```


如果权限不足，可以使用以下命令：


```
$ curl https://raw.githubusercontent.com/jxcore/jxcore/master/tools/jx_install.sh | sudo bash
```


以上步骤如果操作正确，使用以下命令，会输出版本号信息：


```
$ jx --version
v0.10.32
```


---


## 包代码


例如，我们的 Node.js 项目包含以下几个文件，其中 index.js 是主文件：


```
drwxr-xr-x  2 root root  4096 Nov 13 12:42 images
-rwxr-xr-x  1 root root 30457 Mar  6 12:19 index.htm
-rwxr-xr-x  1 root root 30452 Mar  1 12:54 index.js
drwxr-xr-x 23 root root  4096 Jan 15 03:48 node_modules
drwxr-xr-x  2 root root  4096 Mar 21 06:10 scripts
drwxr-xr-x  2 root root  4096 Feb 15 11:56 style
```


接下来我们使用 **jx** 命令打包以上项目，并指定 index.js 为 Node.js 项目的主文件：


```
$ jx package index.js index
```


以上命令执行成功，会生成以下两个文件：


- **index.jxp** 这是一个中间件文件，包含了需要编译的完整项目信息。
- **index.jx** 这是一个完整包信息的二进制文件，可运行在客户端上。


---


## 载入 JX 文件


Node.js 的项目运行：


```
$ node index.js command_line_arguments
```


使用 JXcore 编译后，我们可以使用以下命令来执行生成的 jx 二进制文件：


```
$ jx index.jx command_line_arguments
```


---


更多 JXcore 安装参考：[https://github.com/jxcore/jxcore/blob/master/doc/INSTALLATION.md](https://github.com/jxcore/jxcore/blob/master/doc/INSTALLATION.md)。


更多 JXcore 功能特性你可以参考官网：[https://github.com/jxcore/jxcore](https://github.com/jxcore/jxcore)。








	  AI 思考中...





			** [Node.js 多进程](https://www.runoob.com/nodejs-process.html)
			[Node.js 连接 MySQL](https://www.runoob.com/nodejs-mysql.html) **













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