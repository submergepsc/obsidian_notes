# MongoDB 备份(mongodump)与恢复(mongorestore)

- Source: https://www.runoob.com/mongodb/mongodb-mongodump-mongorestore.html

---


## MongoDB数据备份


在Mongodb中我们使用mongodump命令来备份MongoDB数据。该命令可以导出所有数据到指定目录中。


mongodump命令可以通过参数指定导出的数据量级转存的服务器。


### 语法


mongodump命令脚本语法如下：


```
>mongodump -h dbhost -d dbname -o dbdirectory
```


- ** -h：**MongoDB 所在服务器地址，例如：127.0.0.1，当然也可以指定端口号：127.0.0.1:27017
- ** -d：**需要备份的数据库实例，例如：test
- ** -o：**备份的数据存放位置，例如：c:\data\dump，当然该目录需要提前建立，在备份完成后，系统自动在dump目录下建立一个test目录，这个目录里面存放该数据库实例的备份数据。


### 实例


在本地使用 27017 启动你的mongod服务。打开命令提示符窗口，进入MongoDB安装目录的bin目录输入命令mongodump:


```
>mongodump
```


执行以上命令后，客户端会连接到ip为 127.0.0.1 端口号为 27017 的MongoDB服务上，并备份所有数据到 bin/dump/ 目录中。命令输出结果如下：


![MongoDB数据备份](https://www.runoob.com/wp-content/uploads/2013/12/mongodump.png)


mongodump 命令可选参数列表如下所示：


| 语法 | 描述 | 实例 |
| --- | --- | --- |
| mongodump --host HOST_NAME --port PORT_NUMBER | 该命令将备份所有MongoDB数据 | mongodump --host runoob.com --port 27017 |
| mongodump --dbpath DB_PATH --out BACKUP_DIRECTORY |  | mongodump --dbpath /data/db/ --out /data/backup/ |
| mongodump --collection COLLECTION --db DB_NAME | 该命令将备份指定数据库的集合。 | mongodump --collection mycol --db test |


---

## MongoDB数据恢复


mongodb使用 mongorestore 命令来恢复备份的数据。


### 语法


mongorestore命令脚本语法如下：



```
>mongorestore -h <hostname><:port> -d dbname <path>
```


- ** --host , -h ：**MongoDB所在服务器地址，默认为： localhost:27017
- ** --db , -d ：**需要恢复的数据库实例，例如：test，当然这个名称也可以和备份时候的不一样，比如test2
- ** --drop：**恢复的时候，先删除当前数据，然后恢复备份的数据。就是说，恢复后，备份后添加修改的数据都会被删除，慎用哦！
- **
：** mongorestore 最后的一个参数，设置备份数据所在位置，例如：c:\data\dump\test。 你不能同时指定 和 --dir 选项，--dir也可以设置备份目录。 - ** --dir：**指定备份的目录 你不能同时指定 和 --dir 选项。 接下来我们执行以下命令:


```
>mongorestore
```


执行以上命令输出结果如下：


![MongoDB数据恢复](https://www.runoob.com/wp-content/uploads/2013/12/mongorestore.png)








	  AI 思考中...





			** [MongoDB 分片](https://www.runoob.com/mongodb-sharding.html)
			[MongoDB 监控](https://www.runoob.com/mongodb-mongostat-mongotop.html) **













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