# MongoDB 全文检索

- Source: https://www.runoob.com/mongodb/mongodb-text-search.html

全文检索对每一个词建立一个索引，指明该词在文章中出现的次数和位置，当用户查询时，检索程序就根据事先建立的索引进行查找，并将查找的结果反馈给用户的检索方式。


这个过程类似于通过字典中的检索字表查字的过程。


MongoDB 从 2.4 版本开始支持全文检索，目前支持15种语言的全文索引。


- danish
- dutch
- english
- finnish
- french
- german
- hungarian
- italian
- norwegian
- portuguese
- romanian
- russian
- spanish
- swedish
- turkish


---


## 启用全文检索


MongoDB 在 2.6 版本以后是默认开启全文检索的，如果你使用之前的版本，你需要使用以下代码来启用全文检索:


```
>db.adminCommand({setParameter:true,textSearchEnabled:true})
```


或者使用命令：


```
mongod --setParameter textSearchEnabled=true
```


---


## 创建全文索引


考虑以下 posts 集合的文档数据，包含了文章内容（post_text）及标签(tags)：


```
{
   "post_text": "enjoy the mongodb articles on Runoob",
   "tags": [
      "mongodb",
      "runoob"
   ]
}
```


我们可以对 post_text 字段建立全文索引，这样我们可以搜索文章内的内容：


```
>db.posts.ensureIndex({post_text:"text"})
```


---


## 使用全文索引


现在我们已经对 post_text 建立了全文索引，我们可以搜索文章中的关键词 runoob：


```
>db.posts.find({$text:{$search:"runoob"}})
```


以下命令返回了如下包含 runoob 关键词的文档数据：


```
{
   "_id" : ObjectId("53493d14d852429c10000002"),
   "post_text" : "enjoy the mongodb articles on Runoob",
   "tags" : [ "mongodb", "runoob" ]
}
```


如果你使用的是旧版本的 MongoDB，你可以使用以下命令：


```
>db.posts.runCommand("text",{search:"runoob"})
```


使用全文索引可以提高搜索效率。


---


## 删除全文索引


删除已存在的全文索引，可以使用 find 命令查找索引名：


```
>db.posts.getIndexes()
```


通过以上命令获取索引名，本例的索引名为post_text_text，执行以下命令来删除索引：


```
>db.posts.dropIndex("post_text_text")
```










	  AI 思考中...





			** [MongoDB Map Reduce](https://www.runoob.com/mongodb-map-reduce.html)
			[MongoDB 正则表达式](https://www.runoob.com/mongodb-regular-expression.html) **













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