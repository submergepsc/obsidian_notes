# MongoDB PHP

- Source: https://www.runoob.com/mongodb/mongodb-php.html

在php中使用mongodb你必须使用 mongodb 的 php驱动。


MongoDB PHP在各平台上的安装及驱动包下载请查看:[PHP安装MongoDB扩展驱动](https://www.runoob.com/mongodb-install-php-driver.html)


如果你使用的是 PHP7，请参阅：[PHP7 MongoDB 安装与使用](https://www.runoob.com/php7-mongdb-tutorial.html)。


## 确保连接及选择一个数据库


为了确保正确连接，你需要指定数据库名，如果数据库在mongoDB中不存在，mongoDB会自动创建


代码片段如下：


```
<?php
$m = new MongoClient(); // 连接默认主机和端口为：mongodb://localhost:27017
$db = $m->test; // 获取名称为 "test" 的数据库
?>
```


---


## 创建集合


创建集合的代码片段如下：


```
<?php
$m = new MongoClient(); // 连接
$db = $m->test; // 获取名称为 "test" 的数据库
$collection = $db->createCollection("runoob");
echo "集合创建成功";
?>
```


执行以上程序，输出结果如下：


```
集合创建成功
```


---


## 插入文档


在mongoDB中使用 insert() 方法插入文档：


插入文档代码片段如下：


```
<?php
$m = new MongoClient();    // 连接到mongodb
$db = $m->test;            // 选择一个数据库
$collection = $db->runoob; // 选择集合
$document = array(
    "title" => "MongoDB",
    "description" => "database",
    "likes" => 100,
    "url" => "http://www.runoob.com/mongodb/",
    "by", "菜鸟教程"
);
$collection->insert($document);
echo "数据插入成功";
?>
```


执行以上程序，输出结果如下：


```
数据插入成功
```


然后我们在 mongo 客户端使用 **db.runoob.find().pretty();** 命令查看数据：


![](https://www.runoob.com/wp-content/uploads/2015/09/D1BA0B68-F33C-4597-AAEC-DF3F09BD0C0E.jpg)


---


## 查找文档


使用find() 方法来读取集合中的文档。


读取使用文档的代码片段如下：


```
<?php
$m = new MongoClient();    // 连接到mongodb
$db = $m->test;            // 选择一个数据库
$collection = $db->runoob; // 选择集合

$cursor = $collection->find();
// 迭代显示文档标题
foreach ($cursor as $document) {
    echo $document["title"] . "\n";
}
?>
```


执行以上程序，输出结果如下：


```
MongoDB
```


---


## 更新文档


使用 update() 方法来更新文档。


以下实例将更新文档中的标题为' MongoDB 教程'， 代码片段如下：


```
<pre>
<?php
$m = new MongoClient();    // 连接到mongodb
$db = $m->test;            // 选择一个数据库
$collection = $db->runoob; // 选择集合
// 更新文档
$collection->update(array("title"=>"MongoDB"), array('$set'=>array("title"=>"MongoDB 教程")));
// 显示更新后的文档
$cursor = $collection->find();
// 循环显示文档标题
foreach ($cursor as $document) {
    echo $document["title"] . "\n";
}
?>
```


执行以上程序，输出结果如下：


```
MongoDB 教程
```


然后我们在 mongo 客户端使用 **db.runoob.find().pretty();** 命令查看数据：


![](https://www.runoob.com/wp-content/uploads/2015/09/D1BA0B68-F33C-4597-AAEC-DF3F09BD0C0E.jpg)


---


## 删除文档


使用 remove() 方法来删除文档。


以下实例中我们将移除 'title' 为 'MongoDB 教程' 的一条数据记录。， 代码片段如下：


```
<?php
$m = new MongoClient();    // 连接到mongodb
$db = $m->test;            // 选择一个数据库
$collection = $db->runoob; // 选择集合

// 移除文档
$collection->remove(array("title"=>"MongoDB 教程"), array("justOne" => true));

// 显示可用文档数据
$cursor = $collection->find();
foreach ($cursor as $document) {
    echo $document["title"] . "\n";
}
?>
```


除了以上实例外，在php中你还可以使用findOne(), save(), limit(), skip(), sort()等方法来操作Mongodb数据库。


更多的操作方法可以参考 Mongodb 核心类：[http://php.net/manual/zh/mongo.core.php](http://php.net/manual/zh/mongo.core.php)。








	  AI 思考中...





			** [MongoDB Java](https://www.runoob.com/mongodb-java.html)
			[MongoDB 关系](https://www.runoob.com/mongodb-relationships.html) **













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