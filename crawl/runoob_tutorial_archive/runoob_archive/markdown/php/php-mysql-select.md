# PHP MySQL 读取数据

- Source: https://www.runoob.com/php/php-mysql-select.html

## 从 MySQL 数据库读取数据


SELECT 语句用于从数据表中读取数据:


```
SELECT column_name(s) FROM table_name
```


我们可以使用 * 号来读取所有数据表中的字段：


```
SELECT * FROM table_name
```


如需学习更多关于 SQL 的知识，请访问我们的 [SQL 教程](https://www.runoob.com/../sql/sql-tutorial.html)。


---


## 使用 MySQLi


以下实例中我们从 myDB 数据库的 MyGuests 表读取了 id, firstname 和 lastname 列的数据并显示在页面上：


## 实例 (MySQLi - 面向对象)


```php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}

$sql = "SELECT id, firstname, lastname FROM MyGuests";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // 输出数据
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
    }
} else {
    echo "0 结果";
}
$conn->close();
?>
```


以上代码解析如下:


首先，我们设置了 SQL 语句从 MyGuests数据表中读取 id, firstname 和 lastname 三个字段。之后我们使用该 SQL 语句从数据库中取出结果集并赋给复制给变量 $result。


函数 num_rows() 判断返回的数据。


如果返回的是多条数据，函数 fetch_assoc() 将结合集放入到关联数组并循环输出。 while() 循环出结果集，并输出 id, firstname 和 lastname 三个字段值。


以下实例使用 MySQLi 面向过程的方式，效果类似以上代码:


## 实例 (MySQLi - 面向过程)


```php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// 创建连接
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("连接失败: " . mysqli_connect_error());
}

$sql = "SELECT id, firstname, lastname FROM MyGuests";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // 输出数据
    while($row = mysqli_fetch_assoc($result)) {
        echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
    }
} else {
    echo "0 结果";
}

mysqli_close($conn);
?>
```


---


## 使用 PDO (+ 预处理)


以下实例使用了预处理语句。


选取了 MyGuests 表中的 id, firstname 和 lastname 字段，并放到 HTML 表格中：


## 实例 (PDO)


```php
<?php
echo "<table style='border: solid 1px black;'>";
echo "<tr><th>Id</th><th>Firstname</th><th>Lastname</th></tr>";

class TableRows extends RecursiveIteratorIterator {
    function __construct($it) {
        parent::__construct($it, self::LEAVES_ONLY);
    }

    function current() {
        return "<td style='width:150px;border:1px solid black;'>" . parent::current(). "</td>";
    }

    function beginChildren() {
        echo "<tr>";
    }

    function endChildren() {
        echo "</tr>" . "\n";
    }
}

$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDBPDO";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $stmt = $conn->prepare("SELECT id, firstname, lastname FROM MyGuests");
    $stmt->execute();

    // 设置结果集为关联数组
    $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
    foreach(new TableRows(new RecursiveArrayIterator($stmt->fetchAll())) as $k=>$v) {
        echo $v;
    }
}
catch(PDOException $e) {
    echo "Error: " . $e->getMessage();
}
$conn = null;
echo "</table>";
?>
```










	  AI 思考中...





			** [PHP MySQL 插入数据](https://www.runoob.com/php-mysql-insert.html)
			[PHP MySQL Where 子句](https://www.runoob.com/php-mysql-where.html) **