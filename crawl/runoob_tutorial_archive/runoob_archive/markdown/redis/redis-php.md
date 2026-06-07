# PHP 使用 Redis

- Source: https://www.runoob.com/redis/redis-php.html

## 安装


开始在 PHP 中使用 Redis 前， 我们需要确保已经安装了 redis 服务及 PHP redis 驱动，且你的机器上能正常使用 PHP。 接下来让我们安装 PHP redis 驱动：下载地址为:[**https://github.com/phpredis/phpredis/releases**](https://github.com/phpredis/phpredis/releases)。


### PHP安装redis扩展


以下操作需要在下载的 phpredis 目录中完成：


```
$ wget https://github.com/phpredis/phpredis/archive/3.1.4.tar.gz
$ tar zxvf 3.1.4.tar.gz                  # 解压
$ cd phpredis-3.1.4                      # 进入 phpredis 目录
$ /usr/local/php/bin/phpize              # php安装后的路径
$ ./configure --with-php-config=/usr/local/php/bin/php-config
$ make && make install
```


### 修改php.ini文件


```
vi /usr/local/php/lib/php.ini
```


增加如下内容:


```
extension_dir = "/usr/local/php/lib/php/extensions/no-debug-zts-20090626"

extension=redis.so
```


安装完成后重启php-fpm 或 apache。查看phpinfo信息，就能看到redis扩展。

![](https://www.runoob.com/wp-content/uploads/2014/11/14022020088882.jpg)


---


## 连接到 redis 服务


## 实例


```redis
<?php
    //连接本地的 Redis 服务
   $redis = new Redis();
   $redis->connect('127.0.0.1', 6379);
   echo "Connection to server successfully";
         //查看服务是否运行
   echo "Server is running: " . $redis->ping();
?>
```


执行脚本，输出结果为：


```
Connection to server successfully
Server is running: PONG
```


---


## Redis PHP String(字符串) 实例


## 实例


```redis
<?php
//连接本地的 Redis 服务
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
echo "Connection to server successfully";
//设置 redis 字符串数据
$redis->set("tutorial-name", "Redis tutorial");
// 获取存储的数据并输出
echo "Stored string in redis:: " . $redis->get("tutorial-name");
?>
```


执行脚本，输出结果为：


```
Connection to server successfully
Stored string in redis:: Redis tutorial
```


---


## Redis PHP List(列表) 实例


## 实例


```redis
<?php
//连接本地的 Redis 服务
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
echo "Connection to server successfully";
//存储数据到列表中
$redis->lpush("tutorial-list", "Redis");
$redis->lpush("tutorial-list", "Mongodb");
$redis->lpush("tutorial-list", "Mysql");
// 获取存储的数据并输出
$arList = $redis->lrange("tutorial-list", 0 ,5);
echo "Stored string in redis";
print_r($arList);
?>
```


执行脚本，输出结果为：


```
Connection to server successfully
Stored string in redis
Mysql
Mongodb
Redis
```


---


## Redis PHP Keys 实例


## 实例


```redis
<?php
//连接本地的 Redis 服务
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
echo "Connection to server successfully";
// 获取数据并输出
$arList = $redis->keys("*");
echo "Stored keys in redis:: ";
print_r($arList);
?>
```


执行脚本，输出结果为：


```
Connection to server successfully
Stored string in redis::
tutorial-name
tutorial-list
```









	  AI 思考中...





			** [Java 使用 Redis](https://www.runoob.com/redis-java.html)
			[Redis PEXPIRE 命令](https://www.runoob.com/keys-pexpire.html) **













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