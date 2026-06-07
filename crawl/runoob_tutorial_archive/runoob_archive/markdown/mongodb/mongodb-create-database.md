# MongoDB 创建数据库

- Source: https://www.runoob.com/mongodb/mongodb-create-database.html

在MongoDB中，数据库的创建是一个简单的过程，当你首次向MongoDB中插入数据时，如果数据库不存在，MongoDB会自动创建它。


我们只需选择一个数据库名称，并开始向其中插入文档即可。


### 语法

当你使用 **use** 命令来指定一个数据库时，如果该数据库不存在，MongoDB将自动创建它。


MongoDB 创建数据库的语法格式如下：


```
use DATABASE_NAME
```


如果数据库不存在，则创建数据库，否则切换到指定数据库。


### 实例


以下实例我们创建了数据库 runoob:


```
> use runoob
switched to db runoob
> db
runoob
>
```


执行 **use runoob** 命令后，MongoDB 将创建名为 runoob 的新数据库。此时，你可以开始在这个数据库中创建集合和插入文档。


如果你想查看所有数据库，可以使用 **show dbs** 命令：


```
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
>
```


可以看到，我们刚创建的数据库 runoob 并不在数据库的列表中， 要显示它，我们需要向 runoob 数据库插入一些数据。


```
> db.runoob.insertOne({"name":"菜鸟教程"})
WriteResult({ "nInserted" : 1 })
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
runoob  0.000GB
```


### 创建集合

创建数据库后，通常需要在其中创建集合（collections），以存储文档（documents）。

集合类似于关系数据库中的表，以下是创建集合的步骤：


使用 use 命令指定数据库。

使用 db.createCollection() 方法创建集合。


## 实例


```mongodb
use myNewDatabase
db.createCollection("myNewCollection")
```


上述命令将在 myNewDatabase 数据库中创建一个名为 myNewCollection 的新集合。


### 查看数据库列表

要查看当前 MongoDB 实例中所有数据库的列表，可以使用 **show dbs** 命令：


```
show dbs
```


### 查看当前数据库

要查看当前正在使用的数据库，可以使用 **db** 命令：


```
db
```


### 删除数据库

如果你需要删除数据库，可以使用 **db.dropDatabase()** 方法：


```
use myDatabase
db.dropDatabase()
```


上述命令将删除当前正在使用的 myDatabase 数据库及其所有集合。


### 默认数据库


MongoDB 中默认的数据库为 test，如果你没有创建新的数据库，集合将存放在 test 数据库中。
当您通过 shell 连接到 MongoDB 实例时，如果未使用 use 命令切换到其他数据库，则会默认使用 test 数据库。


例如，在启动 MongoDB 实例并连接到 MongoDB shell 后，如果您开始插入文档而未显式指定数据库，MongoDB 将默认使用 test 数据库。


## 实例


```mongodb
use test
db.myCollection.insertOne({ name: "Alice", age: 30 })
```


在这个例子中，如果 test 数据库不存在，则 MongoDB 将自动创建它。


需要注意的是，默认数据库仅在特定情况下才会使用。在实际开发中，您通常会选择自己创建的数据库来存储数据。

**
注意:** 在 MongoDB 中，集合只有在内容插入后才会创建，就是说，创建集合(数据表)后要再插入一个文档(记录)，集合才会真正创建。


### 注意事项


- 数据库名不能包含空格、点（.）或美元符号（$）。
- 数据库的创建是自动的，不需要显式创建，除非你需要在创建时指定特定的配置选项。
- 在MongoDB中，只有在数据库中至少有一个集合时，数据库才会在 `show dbs` 命令的输出中显示。








	  AI 思考中...





			** [MongoDB 自动增长](https://www.runoob.com/mongodb-autoincrement-sequence.html)
			[MongoDB 删除数据库](https://www.runoob.com/mongodb-dropdatabase.html) **













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