# MongoDB $type 操作符

- Source: https://www.runoob.com/mongodb/mongodb-operators-type.html

在 MongoDB 中，**$type** 操作符用于查询具有指定类型的字段的文档。


MongoDB 的 $type 操作符用于查询字段的 BSON 数据类型。

它允许您指定一个或多个类型，并返回匹配这些类型的文档。
以下是 $type 操作符的详细介绍和示例。

语法：


```
db.collection.find({ field: { $type: <type> } })
```


- **field**：要检查类型的字段。
- **type**：指定的 BSON 类型，可以是类型的数字代码或类型名称的字符串。


### BSON 类型

以下是常见的 BSON 类型及其对应的数字代码和字符串名称：


| 类型代码 | 类型名称 |
| --- | --- |
| 1 | double |
| 2 | string |
| 3 | object |
| 4 | array |
| 5 | binData |
| 6 | undefined |
| 7 | objectId |
| 8 | bool |
| 9 | date |
| 10 | null |
| 11 | regex |
| 12 | dbPointer |
| 13 | javascript |
| 14 | symbol |
| 15 | javascriptWithScope |
| 16 | int |
| 17 | timestamp |
| 18 | long |
| 19 | decimal |
| 255 | minKey |
| 127 | maxKey |


### 实例


查找字段类型为字符串的文档:


```
db.myCollection.find({ fieldName: { $type: "string" } })
```


或使用类型代码：


```
db.myCollection.find({ fieldName: { $type: 2 } })
```


查找字段类型为数字的文档，例如，查找 age 字段类型为整数的文档：


```
db.myCollection.find({ age: { $type: "int" } })
```


或使用类型代码：


```
db.myCollection.find({ age: { $type: 16 } })
```


查找字段类型为布尔值的文档：


```
db.myCollection.find({ isActive: { $type: "bool" } })
```


或使用类型代码：


```
db.myCollection.find({ isActive: { $type: 8 } })
```


查找字段类型为日期的文档：


```
db.myCollection.find({ createdAt: { $type: "date" } })
```


或使用类型代码：


```
db.myCollection.find({ createdAt: { $type: 9 } })
```


查找字段类型为多种类型的文档，例如，查找 value 字段类型为字符串或整数的文档：


```
db.myCollection.find({ value: { $type: ["string", "int"] } })
```


或使用类型代码：


```
db.myCollection.find({ value: { $type: [2, 16] } })
```


查找 details 字段类型为对象，并且 score 字段类型为双精度浮点数的文档：


## 实例


```mongodb
db.myCollection.find({
    $and: [
        { details: { $type: "object" } },
        { score: { $type: "double" } }
    ]
})
```


或使用类型代码：


## 实例


```mongodb
db.myCollection.find({
    $and: [
        { details: { $type: 3 } },
        { score: { $type: 1 } }
    ]
})
```


通过使用 $type 操作符，您可以精确地查询文档中特定字段的数据类型，从而进行更细粒度的数据过滤和管理。


---

## 更多实例


**我们使用的数据库名称为"runoob" 我们的集合名称为"col"，以下为我们插入的数据。**


简单的集合"col"：


```
>db.col.insert({
    title: 'PHP 教程',
    description: 'PHP 是一种创建动态交互性站点的强有力的服务器端脚本语言。',
    by: '菜鸟教程',
    url: 'http://www.runoob.com',
    tags: ['php'],
    likes: 200
})
```


**


```
>db.col.insert({title: 'Java 教程',
    description: 'Java 是由Sun Microsystems公司于1995年5月推出的高级程序设计语言。',
    by: '菜鸟教程',
    url: 'http://www.runoob.com',
    tags: ['java'],
    likes: 150
})
```





```
>db.col.insert({title: 'MongoDB 教程',
    description: 'MongoDB 是一个 Nosql 数据库',
    by: '菜鸟教程',
    url: 'http://www.runoob.com',
    tags: ['mongodb'],
    likes: 100
})
```


使用find()命令查看数据：


```
> db.col.find()
{ "_id" : ObjectId("56066542ade2f21f36b0313a"), "title" : "PHP 教程", "description" : "PHP 是一种创建动态交互性站点的强有力的服务器端脚本语言。", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "php" ], "likes" : 200 }
{ "_id" : ObjectId("56066549ade2f21f36b0313b"), "title" : "Java 教程", "description" : "Java 是由Sun Microsystems公司于1995年5月推出的高级程序设计语言。", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "java" ], "likes" : 150 }
{ "_id" : ObjectId("5606654fade2f21f36b0313c"), "title" : "MongoDB 教程", "description" : "MongoDB 是一个 Nosql 数据库", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "mongodb" ], "likes" : 100 }
```


## MongoDB 操作符 - $type 实例


如果想获取 "col" 集合中 title 为 String 的数据，你可以使用以下命令：


```
db.col.find({"title" : {$type : 2}})
或
db.col.find({"title" : {$type : 'string'}})
```


输出结果为：


```
{ "_id" : ObjectId("56066542ade2f21f36b0313a"), "title" : "PHP 教程", "description" : "PHP 是一种创建动态交互性站点的强有力的服务器端脚本语言。", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "php" ], "likes" : 200 }
{ "_id" : ObjectId("56066549ade2f21f36b0313b"), "title" : "Java 教程", "description" : "Java 是由Sun Microsystems公司于1995年5月推出的高级程序设计语言。", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "java" ], "likes" : 150 }
{ "_id" : ObjectId("5606654fade2f21f36b0313c"), "title" : "MongoDB 教程", "description" : "MongoDB 是一个 Nosql 数据库", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "mongodb" ], "likes" : 100 }
```









	  AI 思考中...





			** [MongoDB 条件操作符](https://www.runoob.com/mongodb-operators.html)
			[MongoDB Limit 与 Skip 方法](https://www.runoob.com/mongodb-limit-skip.html) **













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