# PHP MySQL 插入多条数据

- Source: https://www.runoob.com/php/php-mysql-insert-multiple.html

---


## 使用 MySQLi 和 PDO 向 MySQL 插入多条数据


mysqli_multi_query() 函数可用来执行多条SQL语句。


以下实例向 "MyGuests" 表添加了三条新的记录:


## 实例 (MySQLi - 面向对象)


```php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// 创建链接
$conn = new mysqli($servername, $username, $password, $dbname);
// 检查链接
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}

$sql = "INSERT INTO MyGuests (firstname, lastname, email)
VALUES ('John', 'Doe', '[email protected]');";
$sql .= "INSERT INTO MyGuests (firstname, lastname, email)
VALUES ('Mary', 'Moe', '[email protected]');";
$sql .= "INSERT INTO MyGuests (firstname, lastname, email)
VALUES ('Julie', 'Dooley', '[email protected]')";

if ($conn->multi_query($sql) === TRUE) {
    echo "新记录插入成功";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
```


**


|  | 请注意，每个SQL语句必须用分号隔开。 |
| --- | --- |


## 实例 (MySQLi - 面向过程)


```php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// 创建链接
$conn = mysqli_connect($servername, $username, $password, $dbname);
// 检查链接
if (!$conn) {
    die("连接失败: " . mysqli_connect_error());
}

$sql = "INSERT INTO MyGuests (firstname, lastname, email)
VALUES ('John', 'Doe', '[email protected]');";
$sql .= "INSERT INTO MyGuests (firstname, lastname, email)
VALUES ('Mary', 'Moe', '[email protected]');";
$sql .= "INSERT INTO MyGuests (firstname, lastname, email)
VALUES ('Julie', 'Dooley', '[email protected]')";

if (mysqli_multi_query($conn, $sql)) {
    echo "新记录插入成功";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

mysqli_close($conn);
?>
```


## 实例 (PDO)


```php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDBPDO";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // 开始事务
    $conn->beginTransaction();
    // SQL 语句
    $conn->exec("INSERT INTO MyGuests (firstname, lastname, email)
    VALUES ('John', 'Doe', '[email protected]')");
    $conn->exec("INSERT INTO MyGuests (firstname, lastname, email)
    VALUES ('Mary', 'Moe', '[email protected]')");
    $conn->exec("INSERT INTO MyGuests (firstname, lastname, email)
    VALUES ('Julie', 'Dooley', '[email protected]')");

    // 提交事务
    $conn->commit();
    echo "新记录插入成功";
}
catch(PDOException $e)
{
    // 如果执行失败回滚
    $conn->rollback();
    echo $sql . "<br>" . $e->getMessage();
}

$conn = null;
?>
```


---


## 使用预处理语句


mysqli 扩展提供了第二种方式用于插入语句。


我们可以预处理语句及绑定参数。


mysql 扩展可以不带数据发送语句或查询到mysql数据库。 你可以向列关联或 "绑定" 变量。


## 实例 (MySQLi 使用预处理语句)


```php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);
// 检测连接
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
} else {
    $sql = "INSERT INTO MyGuests(firstname, lastname, email)  VALUES(?, ?, ?)";

    // 为 mysqli_stmt_prepare() 初始化 statement 对象
    $stmt = mysqli_stmt_init($conn);

    //预处理语句
    if (mysqli_stmt_prepare($stmt, $sql)) {
        // 绑定参数
        mysqli_stmt_bind_param($stmt, 'sss', $firstname, $lastname, $email);

        // 设置参数并执行
        $firstname = 'John';
        $lastname = 'Doe';
        $email = '[email protected]';
        mysqli_stmt_execute($stmt);

        $firstname = 'Mary';
        $lastname = 'Moe';
        $email = '[email protected]';
        mysqli_stmt_execute($stmt);

        $firstname = 'Julie';
        $lastname = 'Dooley';
        $email = '[email protected]';
        mysqli_stmt_execute($stmt);
    }
}
?>
```


我们可以看到以上实例中使用模块化来处理问题。我们可以通过创建代码块实现更简单的读取和管理。


注意参数的绑定。让我们看下 mysqli_stmt_bind_param() 中的代码：


```
mysqli_stmt_bind_param($stmt, 'sss', $firstname, $lastname, $email);
```


该函数绑定参数查询并将参数传递给数据库。第二个参数是 "sss" 。以下列表展示了参数的类型。 s 字符告诉 mysql 参数是字符串。


可以是以下四种参数:


- i - 整数
- d - 双精度浮点数
- s - 字符串
- b - 二进制 blob 存储对象


每个参数必须指定类型，来保证数据的安全性。通过类型的判断可以减少SQL注入漏洞带来的风险。









	  AI 思考中...





			** [PHP JSON](https://www.runoob.com/php-json.html)
			[PHP MySQL 创建表](https://www.runoob.com/php-mysql-create-table.html) **













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