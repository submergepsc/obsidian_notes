# MongoDB PHP 扩展

- Source: https://www.runoob.com/mongodb/mongodb-install-php-driver.html

本教程将向大家介绍如何在Linux、window、Mac平台上安装MongoDB扩展。


---

## Linux 上安装 MongoDB PHP 扩展


### 在终端上安装


你可以在 Linux 中执行以下命令来安装 MongoDB 的 PHP 扩展驱动


```
$ sudo pecl install mongodb
```


使用php的pecl安装命令必须保证网络连接可用以及root权限。


### 安装手册


如果你想通过源码来编译扩展驱动。你必须手动编译源码包，这样做的好是最新修正的 bug 包含在源码包中。


你可以在 PHP 官网上下载 MongoDB PHP 驱动包,下载地址：[http://pecl.php.net/package/mongodb](http://pecl.php.net/package/mongodb)。


![](https://www.runoob.com/wp-content/uploads/2013/10/1C8A3531-039B-4077-A2DA-5C950A071FD4.jpg)


完整安装命令如下：


```
$ wget http://pecl.php.net/get/mongodb-1.5.2.tgz
$ cd /mongodb-1.5.2
$ phpize
$ ./configure
$ make && make install
```


如果你的 php 是自己编译的，则安装方法如下(假设是编译在 /usr/local/php目录中)：


```
$ wget http://pecl.php.net/get/mongodb-1.5.2.tgz
$ cd /mongodb-1.5.2
$ /usr/local/php/bin/phpize
$ ./configure --with-php-config=/usr/local/php/bin/php-config
$ make && make install
```


安装成功后，会有类似以下安装目录信息输出：


```
...
Installing shared extensions:     /usr/lib/php/extensions/debug-non-zts-20151012/
```


执行以上命令后，你需要修改php.ini文件，在 php.ini 文件中添加mongo配置，配置如下：


```
extension_dir=/usr/lib/php/extensions/debug-non-zts-20151012/
extension=mongodb.so
```


**
注意：**你需要指明 extension_dir 配置项的路径。


可以通过以下命令查看目录地址：


```
$ php -i | grep extension_dir
  extension_dir => /usr/lib/php/extensions/debug-non-zts-20151012 =>
                   /usr/lib/php/extensions/debug-non-zts-20151012
```


---


## Window 上安装 MongoDB PHP扩展


PECL 上已经提供了用于 Window 平台的预编译 php mongodb 驱动二进制包(下载地址： [https://pecl.php.net/package/mongodb](https://pecl.php.net/package/mongodb))，你可以下载与你 php 对应的版本，但是你需要注意以下几点问题：


- VC6 是运行于 Apache 服务器
- Thread safe（线程安全）是以模块形式运行在 Apache 上，如果你以 CGI 的模式运行 PHP，请选择非线程安全模式（non-thread safe）。
- VC9 是运行于 IIS 服务器上。
- 下载完你需要的二进制包后，解压压缩包，将 php_mongodb.dll 文件添加到你的PHP扩展目录中（ext）。ext 目录通常在 PHP 安装目录下的 ext 目录。


打开 php 配置文件 php.ini 添加以下配置：


```
extension=php_mongodb.dll
```


重启服务器。


通过浏览器访问phpinfo，如果安装成功，就会看到类型以下的信息：

![](https://www.runoob.com/wp-content/uploads/2013/10/mongo-php-driver-installed-windows.png)


---

## MAC 中安装 MongoDB PHP扩展驱动


你可以使用 **autoconf** 安装 MongoDB PHP 扩展驱动。


你可以使用 **Xcode** 安装 MongoDB PHP 扩展驱动。


如果你使用 XAMPP，你可以使用以下命令安装 MongoDB PHP 扩展驱动：


```
sudo /Applications/XAMPP/xamppfiles/bin/pecl install mongo
```


如果以上命令在XMPP或者MAMP中不起作用，你需要在 Github上下载兼容的预编译包。


然后添加 extension=mongodb.so 配置到你的 php.ini 文件中。








	  AI 思考中...





			** [MongoDB 连接](https://www.runoob.com/mongodb-connections.html)
			[MongoDB 插入文档](https://www.runoob.com/mongodb-insert.html) **













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