# MongoDB 自动增长

- Source: https://www.runoob.com/mongodb/mongodb-autoincrement-sequence.html

MongoDB 没有像 SQL 一样有自动增长的功能， MongoDB 的 _id 是系统自动生成的12字节唯一标识。


但在某些情况下，我们可能需要实现 ObjectId 自动增长功能。


由于 MongoDB 没有实现这个功能，我们可以通过编程的方式来实现，以下我们将在 counters 集合中实现_id字段自动增长。


---


## 使用 counters 集合


考虑以下 products 文档。我们希望 _id 字段实现 从 1,2,3,4 到 n 的自动增长功能。


```
{
  "_id":1,
  "product_name": "Apple iPhone",
  "category": "mobiles"
}
```


为此，创建 counters 集合，序列字段值可以实现自动长：


```
>db.createCollection("counters")
```


现在我们向 counters 集合中插入以下文档，使用 productid 作为 key:


```
{
  "_id":"productid",
  "sequence_value": 0
}
```


sequence_value 字段是序列通过自动增长后的一个值。


使用以下命令插入 counters 集合的序列文档中：


```
>db.counters.insert({_id:"productid",sequence_value:0})
```


---


## 创建 Javascript 函数


现在，我们创建函数 getNextSequenceValue 来作为序列名的输入， 指定的序列会自动增长 1 并返回最新序列值。在本文的实例中序列名为 productid 。


```
>function getNextSequenceValue(sequenceName){
   var sequenceDocument = db.counters.findAndModify(
      {
         query:{_id: sequenceName },
         update: {$inc:{sequence_value:1}},
         "new":true
      });
   return sequenceDocument.sequence_value;
}
```


---


## 使用 Javascript 函数


接下来我们将使用 getNextSequenceValue 函数创建一个新的文档， 并设置文档 _id 自动为返回的序列值：


```
>db.products.insert({
   "_id":getNextSequenceValue("productid"),
   "product_name":"Apple iPhone",
   "category":"mobiles"})

>db.products.insert({
   "_id":getNextSequenceValue("productid"),
   "product_name":"Samsung S3",
   "category":"mobiles"})
```


就如你所看到的，我们使用 getNextSequenceValue 函数来设置 _id 字段。


为了验证函数是否有效，我们可以使用以下命令读取文档：


```
>db.products.find()
```


以上命令将返回以下结果，我们发现 _id 字段是自增长的：


```
{ "_id" : 1, "product_name" : "Apple iPhone", "category" : "mobiles"}

{ "_id" : 2, "product_name" : "Samsung S3", "category" : "mobiles" }
```









	  AI 思考中...





			** [MongoDB 固定集合（Capped Collections）](https://www.runoob.com/mongodb-capped-collections.html)
			[MongoDB 创建数据库](https://www.runoob.com/mongodb-create-database.html) **













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