# MongoDB 原子操作

- Source: https://www.runoob.com/mongodb/mongodb-atomic-operations.html

mongodb不支持事务，所以，在你的项目中应用时，要注意这点。无论什么设计，都不要要求mongodb保证数据的完整性。


但是mongodb提供了许多原子操作，比如文档的保存，修改，删除等，都是原子操作。


所谓原子操作就是要么这个文档保存到Mongodb，要么没有保存到Mongodb，不会出现查询到的文档没有保存完整的情况。


---


## 原子操作数据模型


考虑下面的例子，图书馆的书籍及结账信息。


实例说明了在一个相同的文档中如何确保嵌入字段关联原子操作（update：更新）的字段是同步的。


```
book = {
          _id: 123456789,
          title: "MongoDB: The Definitive Guide",
          author: [ "Kristina Chodorow", "Mike Dirolf" ],
          published_date: ISODate("2010-09-24"),
          pages: 216,
          language: "English",
          publisher_id: "oreilly",
          available: 3,
          checkout: [ { by: "joe", date: ISODate("2012-10-15") } ]
        }
```


你可以使用 db.collection.findAndModify() 方法来判断书籍是否可结算并更新新的结算信息。


在同一个文档中嵌入的 available 和 checkout 字段来确保这些字段是同步更新的:


```
db.books.findAndModify ( {
   query: {
            _id: 123456789,
            available: { $gt: 0 }
          },
   update: {
             $inc: { available: -1 },
             $push: { checkout: { by: "abc", date: new Date() } }
           }
} )
```


---


## 原子操作常用命令


#### $set


用来指定一个键并更新键值，若键不存在并创建。


```
{ $set : { field : value } }
```


#### $unset


用来删除一个键。


```
{ $unset : { field : 1} }
```


#### $inc


$inc可以对文档的某个值为数字型（只能为满足要求的数字）的键进行增减的操作。


```
{ $inc : { field : value } }
```


#### $push


用法：


```
{ $push : { field : value } }
```


把value追加到field里面去，field一定要是数组类型才行，如果field不存在，会新增一个数组类型加进去。


#### $pushAll


同$push,只是一次可以追加多个值到一个数组字段内。


```
{ $pushAll : { field : value_array } }
```


#### $pull


从数组field内删除一个等于value值。


```
{ $pull : { field : _value } }
```


#### $addToSet


增加一个值到数组内，而且只有当这个值不在数组内才增加。


#### $pop

删除数组的第一个或最后一个元素
```
{ $pop : { field : 1 } }
```
 #### $rename 修改字段名称


```
{ $rename : { old_field_name : new_field_name } }
```


#### $bit

位操作，integer类型
```
{$bit : { field : {and : 5}}}
```
 #### 偏移操作符
```
> t.find() { "_id" : ObjectId("4b97e62bf1d8c7152c9ccb74"), "title" : "ABC", "comments" : [ { "by" : "joe", "votes" : 3 }, { "by" : "jane", "votes" : 7 } ] }

> t.update( {'comments.by':'joe'}, {$inc:{'comments.$.votes':1}}, false, true )

> t.find() { "_id" : ObjectId("4b97e62bf1d8c7152c9ccb74"), "title" : "ABC", "comments" : [ { "by" : "joe", "votes" : 4 }, { "by" : "jane", "votes" : 7 } ] }
```
 AI 思考中... ** [MongoDB 查询分析](https://www.runoob.com/mongodb-analyzing-queries.html) [MongoDB 高级索引](https://www.runoob.com/mongodb-advanced-indexing.html) ** ### 点我分享笔记 笔记需要是本篇文章的内容扩展！
**

[文章投稿，可点击这里](https://www.runoob.com/tougao)


[注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)


### 分享笔记前必须登录！


[注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)
-->





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