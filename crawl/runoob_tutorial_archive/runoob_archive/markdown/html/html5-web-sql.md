# HTML5 Web SQL 数据库

- Source: https://www.runoob.com/html/html5-web-sql.html

**
Web SQL 的状态：**Web SQL API 已经被废弃，不再推荐使用。新的浏览器标准更倾向于使用 IndexedDB 来处理客户端存储。Web SQL 只在某些老旧的浏览器中仍有支持。


替代方案：
由于 Web SQL 的未来不确定性和不再有广泛支持，建议转向使用 IndexedDB，它是一种支持事务、键值对存储的现代浏览器 API。


Web SQL 数据库 API 并不是 HTML5 规范的一部分，但是它是一个独立的规范，引入了一组使用 SQL 操作客户端数据库的 APIs。


如果你是一个 Web 后端程序员，应该很容易理解 SQL 的操作。


你也可以参考我们的 [SQL 教程](https://www.runoob.com/../sql/sql-tutorial.html)，了解更多数据库操作知识。


Web SQL 数据库可以在最新版的 Safari, Chrome 和 Opera 浏览器中工作。


---


## 核心方法


以下是规范中定义的三个核心方法：


- **openDatabase**：这个方法使用现有的数据库或者新建的数据库创建一个数据库对象。
- **transaction**：这个方法让我们能够控制一个事务，以及基于这种情况执行提交或者回滚。
- **executeSql**：这个方法用于执行实际的 SQL 查询。


---


## 打开数据库


我们可以使用 openDatabase() 方法来打开已存在的数据库，如果数据库不存在，则会创建一个新的数据库，使用代码如下：


```
var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);
```


openDatabase() 方法对应的五个参数说明：


- 数据库名称
- 版本号
- 描述文本
- 数据库大小
- 创建回调


第五个参数，创建回调会在创建数据库后被调用。


---


## 执行查询操作


执行操作使用 database.transaction() 函数：


```html
var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);
db.transaction(function (tx) {
   tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id unique, log)');
});
```


上面的语句执行后会在 'mydb' 数据库中创建一个名为 LOGS 的表。


---


## 插入数据


在执行上面的创建表语句后，我们可以插入一些数据：


```html
var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);
db.transaction(function (tx) {
   tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id unique, log)');
   tx.executeSql('INSERT INTO LOGS (id, log) VALUES (1, "菜鸟教程")');
   tx.executeSql('INSERT INTO LOGS (id, log) VALUES (2, "www.runoob.com")');
});
```


我们也可以使用动态值来插入数据：


```html
var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);
db.transaction(function (tx) {
  tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id unique, log)');
  tx.executeSql('INSERT INTO LOGS (id,log) VALUES (?, ?)', [e_id, e_log]);
});
```


实例中的 e_id 和 e_log 是外部变量，executeSql 会映射数组参数中的每个条目给 "?"。


---


## 读取数据


以下实例演示了如何读取数据库中已经存在的数据：


```html
var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);

db.transaction(function (tx) {
   tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id unique, log)');
   tx.executeSql('INSERT INTO LOGS (id, log) VALUES (1, "菜鸟教程")');
   tx.executeSql('INSERT INTO LOGS (id, log) VALUES (2, "www.runoob.com")');
});

db.transaction(function (tx) {
   tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) {
      var len = results.rows.length, i;
      msg = "<p>查询记录条数: " + len + "</p>";
      document.querySelector('#status').innerHTML +=  msg;

      for (i = 0; i < len; i++){
         alert(results.rows.item(i).log );
      }

   }, null);
});
```


---


## 完整实例


## 实例


```html
var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);
var msg;

db.transaction(function (tx) {
    tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id unique, log)');
    tx.executeSql('INSERT INTO LOGS (id, log) VALUES (1, "菜鸟教程")');
    tx.executeSql('INSERT INTO LOGS (id, log) VALUES (2, "www.runoob.com")');
    msg = '<p>数据表已创建，且插入了两条数据。</p>';
    document.querySelector('#status').innerHTML =  msg;
});

db.transaction(function (tx) {
tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) {
    var len = results.rows.length, i;
    msg = "<p>查询记录条数: " + len + "</p>";
    document.querySelector('#status').innerHTML +=  msg;

    for (i = 0; i < len; i++){
        msg = "<p><b>" + results.rows.item(i).log + "</b></p>";
        document.querySelector('#status').innerHTML +=  msg;
    }
}, null);
});
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_websql)


以上实例运行结果如下图所示：


![](https://www.runoob.com/wp-content/uploads/2015/12/websql.jpg)


---


## 删除记录


删除记录使用的格式如下：


```
db.transaction(function (tx) {
    tx.executeSql('DELETE FROM LOGS  WHERE id=1');
});
```


删除指定的数据id也可以是动态的：


```
db.transaction(function(tx) {
    tx.executeSql('DELETE FROM LOGS WHERE id=?', [id]);
});
```


---


## 更新记录


更新记录使用的格式如下：


```
db.transaction(function (tx) {
    tx.executeSql('UPDATE LOGS SET log=\'www.w3cschool.cc\' WHERE id=2');
});
```


更新指定的数据id也可以是动态的：


```
db.transaction(function(tx) {
    tx.executeSql('UPDATE LOGS SET log=\'www.w3cschool.cc\' WHERE id=?', [id]);
});
```


---


## 完整实例


## 实例


```html
var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);
var msg;

 db.transaction(function (tx) {
    tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id unique, log)');
    tx.executeSql('INSERT INTO LOGS (id, log) VALUES (1, "菜鸟教程")');
    tx.executeSql('INSERT INTO LOGS (id, log) VALUES (2, "www.runoob.com")');
    msg = '<p>数据表已创建，且插入了两条数据。</p>';
    document.querySelector('#status').innerHTML =  msg;
 });

 db.transaction(function (tx) {
      tx.executeSql('DELETE FROM LOGS  WHERE id=1');
      msg = '<p>删除 id 为 1 的记录。</p>';
      document.querySelector('#status').innerHTML =  msg;
 });

 db.transaction(function (tx) {
     tx.executeSql('UPDATE LOGS SET log=\'www.w3cschool.cc\' WHERE id=2');
      msg = '<p>更新 id 为 2 的记录。</p>';
      document.querySelector('#status').innerHTML =  msg;
 });

 db.transaction(function (tx) {
    tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) {
       var len = results.rows.length, i;
       msg = "<p>查询记录条数: " + len + "</p>";
       document.querySelector('#status').innerHTML +=  msg;

       for (i = 0; i < len; i++){
          msg = "<p><b>" + results.rows.item(i).log + "</b></p>";
          document.querySelector('#status').innerHTML +=  msg;
       }
    }, null);
 });
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_websql2)


以上实例运行结果如下图所示：


![](https://www.runoob.com/wp-content/uploads/2015/12/8E8CF48D-A590-4577-B338-715C0034D029.png)








	  AI 思考中...





			** [HTML5 MathML](https://www.runoob.com/html5-mathml.html)
			[HTML(5) 代码规范](https://www.runoob.com/html5-syntax.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/html-examples.html)

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