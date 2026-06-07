# PHP7 MongDB 安装与使用

- Source: https://www.runoob.com/mongodb/php7-mongdb-tutorial.html

本文教程只适合在 PHP7 的环境，如果你是 PHP5 环境，你可以参阅 [PHP MongDB 安装与使用](https://www.runoob.com/mongodb-php.html)。


## PHP7 Mongdb 扩展安装


我们使用 pecl 命令来安装：


```
$ /usr/local/php7/bin/pecl install mongodb
```


执行成功后，会输出以下结果：


```
……
Build process completed successfully
Installing '/usr/local/php7/lib/php/extensions/no-debug-non-zts-20151012/mongodb.so'
install ok: channel://pecl.php.net/mongodb-1.1.7
configuration option "php_ini" is not set to php.ini location
You should add "extension=mongodb.so" to php.ini
```


接下来我们打开 php.ini 文件，添加 **extension=mongodb.so** 配置。


可以直接执行以下命令来添加。


```
$ echo "extension=mongodb.so" >> `/usr/local/php7/bin/php --ini | grep "Loaded Configuration" | sed -e "s|.*:\s*||"`
```


**

注意：**以上执行的命令中 php7 的安装目录为 /usr/local/php7/，如果你安装在其他目录，需要相应修改 pecl 与 php 命令的路径。


---


## Mongodb 使用


PHP7 连接 MongoDB 语法如下：


```
$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");
```


### 插入数据


将 name 为"菜鸟教程" 的数据插入到 test 数据库的 runoob 集合中。


```
<?php
$bulk = new MongoDB\Driver\BulkWrite;
$document = ['_id' => new MongoDB\BSON\ObjectID, 'name' => '菜鸟教程'];

$_id= $bulk->insert($document);

var_dump($_id);

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");
$writeConcern = new MongoDB\Driver\WriteConcern(MongoDB\Driver\WriteConcern::MAJORITY, 1000);
$result = $manager->executeBulkWrite('test.runoob', $bulk, $writeConcern);
?>
```


### 读取数据


这里我们将三个网址数据插入到 test 数据库的 sites 集合，并读取迭代出来：


```
<?php
$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");

// 插入数据
$bulk = new MongoDB\Driver\BulkWrite;
$bulk->insert(['x' => 1, 'name'=>'菜鸟教程', 'url' => 'http://www.runoob.com']);
$bulk->insert(['x' => 2, 'name'=>'Google', 'url' => 'http://www.google.com']);
$bulk->insert(['x' => 3, 'name'=>'taobao', 'url' => 'http://www.taobao.com']);
$manager->executeBulkWrite('test.sites', $bulk);

$filter = ['x' => ['$gt' => 1]];
$options = [
    'projection' => ['_id' => 0],
    'sort' => ['x' => -1],
];

// 查询数据
$query = new MongoDB\Driver\Query($filter, $options);
$cursor = $manager->executeQuery('test.sites', $query);

foreach ($cursor as $document) {
    print_r($document);
}
?>
```


输出结果为：


```
stdClass Object
(
    [x] => 3
    [name] => taobao
    [url] => http://www.taobao.com
)
stdClass Object
(
    [x] => 2
    [name] => Google
    [url] => http://www.google.com
)
```


### 更新数据


接下来我们将更新 test 数据库 sites 集合中 x 为 2 的数据：


```
<?php
$bulk = new MongoDB\Driver\BulkWrite;
$bulk->update(
    ['x' => 2],
    ['$set' => ['name' => '菜鸟工具', 'url' => 'tool.runoob.com']],
    ['multi' => false, 'upsert' => false]
);

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");
$writeConcern = new MongoDB\Driver\WriteConcern(MongoDB\Driver\WriteConcern::MAJORITY, 1000);
$result = $manager->executeBulkWrite('test.sites', $bulk, $writeConcern);
?>
```


接下来我们使用 "db.sites.find()" 命令查看数据的变化，x 为 2 的数据已经变成了菜鸟工具：


![](https://www.runoob.com/wp-content/uploads/2016/06/EFFDBCDE-1E7E-40AD-BE88-37CD57070E25.jpg)


### 删除数据


以下实例删除了 x 为 1 和 x 为 2的数据，注意 limit 参数的区别：


```
<?php
$bulk = new MongoDB\Driver\BulkWrite;
$bulk->delete(['x' => 1], ['limit' => 1]);   // limit 为 1 时，删除第一条匹配数据
$bulk->delete(['x' => 2], ['limit' => 0]);   // limit 为 0 时，删除所有匹配数据

$manager = new MongoDB\Driver\Manager("mongodb://localhost:27017");
$writeConcern = new MongoDB\Driver\WriteConcern(MongoDB\Driver\WriteConcern::MAJORITY, 1000);
$result = $manager->executeBulkWrite('test.sites', $bulk, $writeConcern);
?>
```


更多使用方法请参考：[http://php.net/manual/en/book.mongodb.php](http://php.net/manual/en/book.mongodb.php)。








	  AI 思考中...





			** [MongoDB 删除数据库](https://www.runoob.com/mongodb-dropdatabase.html)
			[Mac OSX 平台安装 MongoDB](https://www.runoob.com/mongodb-osx-install.html) **













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