# MongoDB 监控

- Source: https://www.runoob.com/mongodb/mongodb-mongostat-mongotop.html

在你已经安装部署并允许MongoDB服务后，你必须要了解MongoDB的运行情况，并查看MongoDB的性能。这样在大流量得情况下可以很好的应对并保证MongoDB正常运作。


MongoDB中提供了mongostat 和 mongotop 两个命令来监控MongoDB的运行情况。


---


## mongostat 命令


mongostat是mongodb自带的状态检测工具，在命令行下使用。它会间隔固定时间获取mongodb的当前运行状态，并输出。如果你发现数据库突然变慢或者有其他问题的话，你第一手的操作就考虑采用mongostat来查看mongo的状态。


启动你的Mongod服务，进入到你安装的MongoDB目录下的bin目录， 然后输入mongostat命令，如下所示：


```
D:\set up\mongodb\bin>mongostat
```


以上命令输出结果如下：

![](https://www.runoob.com/wp-content/uploads/2013/12/mongostat.png)

## mongotop 命令


mongotop也是mongodb下的一个内置工具，mongotop提供了一个方法，用来跟踪一个MongoDB的实例，查看哪些大量的时间花费在读取和写入数据。 mongotop提供每个集合的水平的统计数据。默认情况下，mongotop返回值的每一秒。


启动你的Mongod服务，进入到你安装的MongoDB目录下的bin目录， 然后输入mongotop命令，如下所示：


```
D:\set up\mongodb\bin>mongotop
```


以上命令执行输出结果如下：


![](https://www.runoob.com/wp-content/uploads/2013/12/mongotop.png) 带参数实例


```
E:\mongodb-win32-x86_64-2.2.1\bin>mongotop 10
```



![](https://www.runoob.com/wp-content/uploads/2013/12/29122412-e32a9f09e46e496a8833433fdb421311.gif) 后面的10是**参数 ，可以不使用，等待的时间长度，以秒为单位，mongotop等待调用之间。通过的默认mongotop返回数据的每一秒。



```
E:\mongodb-win32-x86_64-2.2.1\bin>mongotop --locks
```



报告每个数据库的锁的使用中，使用mongotop - 锁，这将产生以下输出：


![](https://www.runoob.com/wp-content/uploads/2013/12/29122706-bfdd58e62c404b948f8039c489f8be81.gif)


输出结果字段说明：


- ** ns：**包含数据库命名空间，后者结合了数据库名称和集合。
- ** db：**包含数据库的名称。名为 . 的数据库针对全局锁定，而非特定数据库。
- ** total：**mongod花费的时间工作在这个命名空间提供总额。
- ** read：**提供了大量的时间，这mongod花费在执行读操作，在此命名空间。
- ** write：**提供这个命名空间进行写操作，这mongod花了大量的时间。








	  AI 思考中...





			** [MongoDB 备份(mongodump)与恢复(mongorestore)](https://www.runoob.com/mongodb-mongodump-mongorestore.html)
			[MongoDB Java](https://www.runoob.com/mongodb-java.html) **













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