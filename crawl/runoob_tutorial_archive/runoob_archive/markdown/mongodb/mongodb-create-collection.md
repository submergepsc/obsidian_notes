# MongoDB 创建集合

- Source: https://www.runoob.com/mongodb/mongodb-create-collection.html

本章节我们为大家介绍如何使用 MongoDB 来创建集合。


MongoDB 中使用 **createCollection()** 方法来创建集合。


语法格式：


```
db.createCollection(name, options)
```


参数说明：


- name: 要创建的集合名称。
- options: 可选参数, 指定有关内存大小及索引的选项。


options 可以是如下参数：


| 参数名 | 类型 | 描述 | 示例值 |
| --- | --- | --- | --- |
| capped | 布尔值 | 是否创建一个固定大小的集合。 | true |
| size | 数值 | 集合的最大大小（以字节为单位）。仅在 capped 为 true 时有效。 | 10485760 (10MB) |
| max | 数值 | 集合中允许的最大文档数。仅在 capped 为 true 时有效。 | 5000 |
| validator | 对象 | 用于文档验证的表达式。 | { $jsonSchema: { ... }} |
| validationLevel | 字符串 | 指定文档验证的严格程度。"off"：不进行验证。"strict"：插入和更新操作都必须通过验证（默认）。"moderate"：仅现有文档更新时必须通过验证，插入新文档时不需要。 | "strict" |
| validationAction | 字符串 | 指定文档验证失败时的操作。"error"：阻止插入或更新（默认）。"warn"：允许插入或更新，但会发出警告。 | "error" |
| storageEngine | 对象 | 为集合指定存储引擎配置。 | { wiredTiger: { ... }} |
| collation | 对象 | 指定集合的默认排序规则。 | { locale: "en", strength: 2 } |


在插入文档时，MongoDB 首先检查固定集合的 size 字段，然后检查 max 字段。

使用这些选项创建一个集合的实例：


## 实例


```mongodb
db.createCollection("myComplexCollection", {
  capped: true,
  size: 10485760,
  max: 5000,
  validator: { $jsonSchema: {
    bsonType: "object",
    required: ["name", "email"],
    properties: {
      name: {
        bsonType: "string",
        description: "必须为字符串且为必填项"
      },
      email: {
        bsonType: "string",
        pattern: "^.+@.+$",
        description: "必须为有效的电子邮件地址"
      }
    }
  }},
  validationLevel: "strict",
  validationAction: "error",
  storageEngine: {
    wiredTiger: { configString: "block_compressor=zstd" }
  },
  collation: { locale: "en", strength: 2 }
});
```


这个例子创建了一个集合，具有以下特性：


- 固定大小，最大 10MB，最多存储 5000 个文档。
- 文档必须包含 `name` 和 `email` 字段，其中 `name` 必须是字符串，`email` 必须是有效的电子邮件格式。
- 验证级别为严格，验证失败将阻止插入或更新。
- 使用 WiredTiger 存储引擎，指定块压缩器为 zstd。
- 默认使用英语排序规则。


### 实例


在 test 数据库中创建 runoob 集合：


```
> use test
switched to db test
> db.createCollection("runoob")
{ "ok" : 1 }
>
```


如果要查看已有集合，可以使用 **show collections** 或 **show tables** 命令：


```
> show collections
runoob
system.indexes
```


下面是带有几个关键参数的 createCollection() 的用法：


创建了一个固定大小的集合，最大大小为 5MB（5242880 字节），最多存储 5000 个文档。


```
db.createCollection("myCappedCollection", { capped: true, size: 5242880, max: 5000 });
```


在 MongoDB 中，你不需要创建集合，当你插入一些文档时，MongoDB 会自动创建集合。


```
> db.mycol2.insert({"name" : "菜鸟教程"})
> show collections
mycol2
...
```


创建了一个最大大小为 1MB（1048576 字节）的固定大小集合：


```
db.createCollection("myCappedCollection", { capped: true, size: 1048576 });
```


以下例子为 myCollection 集合创建了一个验证器，要求文档中必须有 name 和 age 字段，且 name 必须是字符串，age 必须是非负整数。


## 实例


```mongodb
db.createCollection("myCollection", {
  validator: { $jsonSchema: {
    bsonType: "object",
    required: ["name", "age"],
    properties: {
      name: {
        bsonType: "string",
        description: "必须为字符串且为必填项"
      },
      age: {
        bsonType: "int",
        minimum: 0,
        description: "必须为整数且为必填项"
      }
    }
  }}
});
```










	  AI 思考中...





			** [Mac OSX 平台安装 MongoDB](https://www.runoob.com/mongodb-osx-install.html)
			[MongoDB 删除集合](https://www.runoob.com/mongodb-delete-collection.html) **













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