# 排序

- Source: https://www.runoob.com/python3/python-mongodb-sort.html

[![Python Mongodb](https://www.runoob.com/images/up.gif) Python Mongodb](https://www.runoob.com/python-mongodb.html)


**sort()** 方法可以指定升序或降序排序。


**sort() **方法第一个参数为要排序的字段，第二个字段指定排序规则，**1** 为升序，**-1** 为降序，默认为升序。


**本文使用的测试数据如下(点击图片查看大图)：**


[![](https://www.runoob.com/wp-content/uploads/2018/06/64CCAEE8-05CB-4F14-8DB1-D9EB9B77FB17.png)](https://www.runoob.com/wp-content/uploads/2018/06/64CCAEE8-05CB-4F14-8DB1-D9EB9B77FB17.png)


对字段 alexa 按升序排序：


## 实例



```python
#!/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

mydoc = mycol.find().sort("alexa")
for x in mydoc:
  print(x)
```


输出结果为：


![](https://www.runoob.com/wp-content/uploads/2018/06/5CD821D4-A48D-4C18-837F-07DBC18D18B6.png)


对字段 alexa 按降序排序：


## 实例



```python
#!/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

mydoc = mycol.find().sort("alexa", -1)

for x in mydoc:
  print(x)
```


输出结果为：


![](https://www.runoob.com/wp-content/uploads/2018/06/811CAC2F-E851-4269-9F4D-498B853CE23E.png)


[![Python Mongodb](https://www.runoob.com/images/up.gif) Python Mongodb](https://www.runoob.com/python-mongodb.html)









	  AI 思考中...





			** [Python Mongodb 删除数据](https://www.runoob.com/python-mongodb-delete-document.html)
			[Python3 集合](https://www.runoob.com/python3-set.html) **













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