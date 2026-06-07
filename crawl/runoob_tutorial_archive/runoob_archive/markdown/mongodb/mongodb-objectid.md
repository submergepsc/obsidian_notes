# MongoDB ObjectId

- Source: https://www.runoob.com/mongodb/mongodb-objectid.html

---


在前面几个章节中我们已经使用了MongoDB 的对象 Id(ObjectId)。


在本章节中，我们将了解的ObjectId的结构。


ObjectId 是一个12字节 BSON 类型数据，有以下格式：


- 前4个字节表示时间戳
- 接下来的3个字节是机器标识码
- 紧接的两个字节由进程id组成（PID）
- 最后三个字节是随机数。


MongoDB中存储的文档必须有一个"_id"键。这个键的值可以是任何类型的，默认是个ObjectId对象。


在一个集合里面，每个文档都有唯一的"_id"值，来确保集合里面每个文档都能被唯一标识。


MongoDB采用ObjectId，而不是其他比较常规的做法（比如自动增加的主键）的主要原因，因为在多个 服务器上同步自动增加主键值既费力还费时。


---


## 创建新的ObjectId


使用以下代码生成新的ObjectId：


```
>newObjectId = ObjectId()
```


上面的语句返回以下唯一生成的id：


```
ObjectId("5349b4ddd2781d08c09890f3")
```


你也可以使用生成的id来取代MongoDB自动生成的ObjectId：


```
>myObjectId = ObjectId("5349b4ddd2781d08c09890f4")
```


---


## 创建文档的时间戳


由于 ObjectId 中存储了 4 个字节的时间戳，所以你不需要为你的文档保存时间戳字段，你可以通过 getTimestamp 函数来获取文档的创建时间:


```
>ObjectId("5349b4ddd2781d08c09890f4").getTimestamp()
```


以上代码将返回 ISO 格式的文档创建时间：


```
ISODate("2014-04-12T21:49:17Z")
```


---


## ObjectId 转换为字符串


在某些情况下，您可能需要将ObjectId转换为字符串格式。你可以使用下面的代码：


```
>new ObjectId().str
```


以上代码将返回Guid格式的字符串：：


```
5349b4ddd2781d08c09890f3
```









	  AI 思考中...





			** [MongoDB 索引限制](https://www.runoob.com/mongodb-indexing-limitations.html)
			[MongoDB Map Reduce](https://www.runoob.com/mongodb-map-reduce.html) **













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