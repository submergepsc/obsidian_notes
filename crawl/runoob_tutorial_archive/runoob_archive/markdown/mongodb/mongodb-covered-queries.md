# MongoDB 覆盖索引查询

- Source: https://www.runoob.com/mongodb/mongodb-covered-queries.html

官方的MongoDB的文档中说明，覆盖查询是以下的查询：


- 所有的查询字段是索引的一部分
- 所有的查询返回字段在同一个索引中


由于所有出现在查询中的字段是索引的一部分， MongoDB 无需在整个数据文档中检索匹配查询条件和返回使用相同索引的查询结果。


因为索引存在于RAM中，从索引中获取数据比通过扫描文档读取数据要快得多。


---


## 使用覆盖索引查询


为了测试覆盖索引查询，使用以下 users 集合:


```
{
   "_id": ObjectId("53402597d852426020000002"),
   "contact": "987654321",
   "dob": "01-01-1991",
   "gender": "M",
   "name": "Tom Benzamin",
   "user_name": "tombenzamin"
}
```


我们在 users 集合中创建联合索引，字段为 gender 和 user_name :


```
>db.users.createIndex({gender:1,user_name:1})
```


**注：**5.0 之前版本可以使用 db.collection.ensureIndex() ，但 ensureIndex() 在 5.0 版本后已被移除，使用 createIndex() 代替。


现在，该索引会覆盖以下查询：


```
>db.users.find({gender:"M"},{user_name:1,_id:0})
```


也就是说，对于上述查询，MongoDB的不会去数据库文件中查找。相反，它会从索引中提取数据，这是非常快速的数据查询。


由于我们的索引中不包括 _id 字段，_id在查询中会默认返回，我们可以在MongoDB的查询结果集中排除它。


下面的实例没有排除_id，查询就不会被覆盖：


```
>db.users.find({gender:"M"},{user_name:1})
```


最后，如果是以下的查询，不能使用覆盖索引查询：


- 所有索引字段是一个数组
- 所有索引字段是一个子文档








	  AI 思考中...





			** [MongoDB 数据库引用](https://www.runoob.com/mongodb-database-references.html)
			[MongoDB 查询分析](https://www.runoob.com/mongodb-analyzing-queries.html) **













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