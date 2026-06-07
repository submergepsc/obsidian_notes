# PHP MySQL 插入数据

- Source: https://www.runoob.com/php/php-mysql-insert.html

---


## 使用 MySQLi 和 PDO 向 MySQL 插入数据


在创建完数据库和表后，我们可以向表中添加数据。


以下为一些语法规则：


- PHP 中 SQL 查询语句必须使用引号
- 在 SQL 查询语句中的字符串值必须加引号
- 数值的值不需要引号
- NULL 值不需要引号


INSERT INTO 语句通常用于向 MySQL 表添加新的记录：


```
INSERT INTO table_name (column1, column2, column3,...)
VALUES (value1, value2, value3,...)
```


学习更多关于 SQL 知识，请查看我们的 [SQL 教程](https://www.runoob.com/../sql/sql-tutorial.html)。


在前面的几个章节中我们已经创建了表 "MyGuests"，表字段有: "id", "firstname", "lastname", "email" 和 "reg_date"。 现在，让我们开始向表填充数据。


|  | 注意： 如果列设置 AUTO_INCREMENT (如 "id" 列) 或 TIMESTAMP (如 "reg_date" 列),，我们就不需要在 SQL 查询语句中指定值； MySQL 会自动为该列添加值。 |
| --- | --- |


以下实例向 "MyGuests" 表添加了新的记录:


## 实例 (MySQLi - 面向对象)


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
}

$sql = "INSERT INTO MyGuests (firstname, lastname, email)
VALUES ('John', 'Doe', '[email protected]')";

if ($conn->query($sql) === TRUE) {
    echo "新记录插入成功";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
```


## 实例 (MySQLi - 面向过程)


```php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// 创建连接
$conn = mysqli_connect($servername, $username, $password, $dbname);
// 检测连接
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$sql = "INSERT INTO MyGuests (firstname, lastname, email)
VALUES ('John', 'Doe', '[email protected]')";

if (mysqli_query($conn, $sql)) {
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
    // 设置 PDO 错误模式，用于抛出异常
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $sql = "INSERT INTO MyGuests (firstname, lastname, email)
    VALUES ('John', 'Doe', '[email protected]')";
    // 使用 exec() ，没有结果返回
    $conn->exec($sql);
    echo "新记录插入成功";
}
catch(PDOException $e)
{
    echo $sql . "<br>" . $e->getMessage();
}

$conn = null;
?>
```










	  AI 思考中...





			** [PHP MySQL 创建数据库](https://www.runoob.com/php-mysql-create.html)
			[PHP MySQL 读取数据](https://www.runoob.com/php-mysql-select.html) **