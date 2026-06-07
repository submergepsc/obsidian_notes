# MongoDB 高级索引

- Source: https://www.runoob.com/mongodb/mongodb-advanced-indexing.html

考虑以下文档集合（users ）:


```
{
   "address": {
      "city": "Los Angeles",
      "state": "California",
      "pincode": "123"
   },
   "tags": [
      "music",
      "cricket",
      "blogs"
   ],
   "name": "Tom Benzamin"
}
```


以上文档包含了 address 子文档和 tags 数组。


---


## 索引数组字段


假设我们基于标签来检索用户，为此我们需要对集合中的数组 tags 建立索引。


在数组中创建索引，需要对数组中的每个字段依次建立索引。所以在我们为数组 tags 创建索引时，会为 music、cricket、blogs三个值建立单独的索引。


使用以下命令创建数组索引：


```
>db.users.ensureIndex({"tags":1})
```


创建索引后，我们可以这样检索集合的 tags 字段：


```
>db.users.find({tags:"cricket"})
```


为了验证我们使用使用了索引，可以使用 explain 命令：


```
>db.users.find({tags:"cricket"}).explain()
```


以上命令执行结果中会显示 "cursor" : "BtreeCursor tags_1" ，则表示已经使用了索引。


---

## 索引子文档字段


假设我们需要通过city、state、pincode字段来检索文档，由于这些字段是子文档的字段，所以我们需要对子文档建立索引。


为子文档的三个字段创建索引，命令如下：


```
>db.users.ensureIndex({"address.city":1,"address.state":1,"address.pincode":1})
```


一旦创建索引，我们可以使用子文档的字段来检索数据：


```
>db.users.find({"address.city":"Los Angeles"})
```


查询表达不一定遵循指定的索引的顺序，mongodb 会自动优化。所以上面创建的索引将支持以下查询：


```
>db.users.find({"address.state":"California","address.city":"Los Angeles"})
```


同样支持以下查询：


```
>db.users.find({"address.city":"Los Angeles","address.state":"California","address.pincode":"123"})
```










	  AI 思考中...





			** [MongoDB 原子操作](https://www.runoob.com/mongodb-atomic-operations.html)
			[MongoDB 索引限制](https://www.runoob.com/mongodb-indexing-limitations.html) **













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