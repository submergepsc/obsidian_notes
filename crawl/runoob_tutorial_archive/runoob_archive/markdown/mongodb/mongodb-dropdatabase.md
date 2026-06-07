# MongoDB 删除数据库

- Source: https://www.runoob.com/mongodb/mongodb-dropdatabase.html

### 语法


MongoDB 删除数据库的语法格式如下：


```
db.dropDatabase()
```


删除当前数据库，默认为 test，你可以使用 db 命令查看当前数据库名。


### 实例


以下实例我们删除了数据库 runoob。


首先，查看所有数据库：


```
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
runoob  0.000GB
```


接下来我们切换到数据库 runoob：


```
> use runoob
switched to db runoob
>
```


执行删除命令：


```
> db.dropDatabase()
{ "dropped" : "runoob", "ok" : 1 }
```


最后，我们再通过 show dbs 命令数据库是否删除成功：


```
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
```


### 删除集合


集合删除语法格式如下：


```
db.collection.drop()
```


以下实例删除了 runoob 数据库中的集合 site：


```
> use runoob
switched to db runoob
> db.createCollection("runoob")     # 先创建集合，类似数据库中的表
> show tables             # show collections 命令会更加准确点
runoob
> db.runoob.drop()
true
> show tables
>
```









	  AI 思考中...





			** [MongoDB 创建数据库](https://www.runoob.com/mongodb-create-database.html)
			[PHP7 MongDB 安装与使用](https://www.runoob.com/php7-mongdb-tutorial.html) **













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