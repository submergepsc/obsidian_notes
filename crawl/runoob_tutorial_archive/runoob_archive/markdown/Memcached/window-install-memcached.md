# Windows 下安装 Memcached

- Source: https://www.runoob.com/Memcached/window-install-memcached.html

官网上并未提供 Memcached 的 Windows 平台安装包，我们可以使用以下链接来下载，你需要根据自己的系统平台及需要的版本号点击对应的链接下载即可：


- 32位系统 1.2.5版本：[http://static.jyshare.com/download/memcached-1.2.5-win32-bin.zip](http://static.jyshare.com/download/memcached-1.2.5-win32-bin.zip)
- 32位系统 1.2.6版本：[http://static.jyshare.com/download/memcached-1.2.6-win32-bin.zip](http://static.jyshare.com/download/memcached-1.2.6-win32-bin.zip)
- 32位系统 1.4.4版本：[http://static.jyshare.com/download/memcached-win32-1.4.4-14.zip](http://static.jyshare.com/download/memcached-win32-1.4.4-14.zip)
- 64位系统 1.4.4版本：[http://static.jyshare.com/download/memcached-win64-1.4.4-14.zip](http://static.jyshare.com/download/memcached-win64-1.4.4-14.zip)
- 32位系统 1.4.5版本：[http://static.jyshare.com/download/memcached-1.4.5-x86.zip](http://static.jyshare.com/download/memcached-1.4.5-x86.zip)
- 64位系统 1.4.5版本：[http://static.jyshare.com/download/memcached-1.4.5-amd64.zip](http://static.jyshare.com/download/memcached-1.4.5-amd64.zip)


在 1.4.5 版本以前 memcached 可以作为一个服务安装，而在 1.4.5 及之后的版本删除了该功能。因此我们以下介绍两个不同版本 1.4.4 及 1.4.5的不同安装方法：


---


## memcached = 1.4.5 版本安装


1、解压下载的安装包到指定目录。


2、在 memcached1.4.5 版本之后，memcached 不能作为服务来运行，需要使用任务计划中来开启一个普通的进程，在 window 启动时设置 memcached自动执行。

我们使用管理员身份执行以下命令将 memcached 添加来任务计划表中：


```
schtasks /create /sc onstart /tn memcached /tr "'c:\memcached\memcached.exe' -m 512"
```


**注意：**你需要使用真实的路径替代 c:\memcached\memcached.exe。


**注意：****-m 512** 意思是设置 memcached 最大的缓存配置为512M。


**注意：**我们可以通过使用 "*c:\memcached\memcached.exe -h*" 命令查看更多的参数配置。


3、如果需要删除 memcached 的任务计划可以执行以下命令：


```
schtasks /delete /tn memcached
```









	  AI 思考中...





			** [Java 连接 Memcached 服务](https://www.runoob.com/../memcached/java-memcached.html)














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