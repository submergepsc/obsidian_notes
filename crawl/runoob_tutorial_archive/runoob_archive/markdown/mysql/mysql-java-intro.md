# MySQL Java 连接与使用

- Source: https://www.runoob.com/mysql/mysql-java-intro.html

MySQL 是最流行的开源关系型数据库之一，而 Java 是企业级应用开发中最常用的编程语言。将 Java 与 MySQL 结合使用，可以构建强大的数据驱动型应用程序。

本文将详细介绍如何在 Java 程序中连接和使用 MySQL 数据库，包括：


本文介绍了 Java 连接和使用 MySQL 数据库的基本步骤，包括：


- 加载 JDBC 驱动
- 建立数据库连接
- 执行 SQL 查询和更新
- 使用 PreparedStatement 防止 SQL 注入
- 事务管理
- 资源关闭
- 最佳实践


---


## 准备工作


### 下载 MySQL JDBC 驱动

Java 通过 JDBC (Java Database Connectivity) 技术与数据库交互。要连接 MySQL，你需要下载 MySQL Connector/J 驱动：


- 访问 [MySQL Connector/J 下载页面](https://dev.mysql.com/downloads/connector/j/)
- 选择与你的 Java 版本兼容的驱动版本
- 下载 JAR 文件（如 mysql-connector-java-8.0.xx.jar）


### 将驱动添加到项目

根据你使用的开发工具或构建工具（如 Eclipse、IntelliJ IDEA、Maven 或 Gradle），将下载的 JAR 文件添加到项目的类路径中。


---


## 建立数据库连接


### 加载驱动程序


在 Java 代码中，首先需要加载 MySQL JDBC 驱动：


## 实例


```sql
try {
    Class.forName("com.mysql.cj.jdbc.Driver");
} catch (ClassNotFoundException e) {
    System.out.println("MySQL JDBC 驱动未找到");
    e.printStackTrace();
}
```


### 创建连接

使用 `DriverManager.getConnection()`方法建立与数据库的连接：


## 实例


```sql
String url = "jdbc:mysql://localhost:3306/你的数据库名?useSSL=false&serverTimezone=UTC";
String username = "你的用户名";
String password = "你的密码";

try {
    Connection connection = DriverManager.getConnection(url, username, password);
    System.out.println("数据库连接成功！");
} catch (SQLException e) {
    System.out.println("数据库连接失败");
    e.printStackTrace();
}
```


#### 3.2.1 连接参数说明


- `jdbc:mysql://localhost:3306/`：MySQL 服务器的默认地址和端口
- `useSSL=false`：禁用 SSL 连接（开发环境）
- `serverTimezone=UTC`：设置服务器时区，避免时区问题


---


## 执行 SQL 操作


### 创建 Statement 对象

Statement 对象用于执行静态 SQL 语句：


## 实例


```sql
Statement statement = connection.createStatement();
```


### 执行查询

使用 `executeQuery()` 方法执行 SELECT 语句：


## 实例


```sql
String sql = "SELECT * FROM 表名";
ResultSet resultSet = statement.executeQuery(sql);

while (resultSet.next()) {
    int id = resultSet.getInt("id");
    String name = resultSet.getString("name");
    System.out.println("ID: " + id + ", Name: " + name);
}
```


### 执行更新


使用 `executeUpdate()` 方法执行 INSERT、UPDATE 或 DELETE 语句：


## 实例


```sql
String insertSQL = "INSERT INTO 表名 (列1, 列2) VALUES ('值1', '值2')";
int rowsAffected = statement.executeUpdate(insertSQL);
System.out.println("影响的行数: " + rowsAffected);
```


### 使用 PreparedStatement

PreparedStatement 可以防止 SQL 注入，提高性能：


## 实例


```sql
String sql = "INSERT INTO users (name, email) VALUES (?, ?)";
PreparedStatement preparedStatement = connection.prepareStatement(sql);

preparedStatement.setString(1, "张三");
preparedStatement.setString(2, "[email protected]");

int rowsInserted = preparedStatement.executeUpdate();
System.out.println("插入的行数: " + rowsInserted);
```


---


## 事务管理


### 基本概念

事务是一组要么全部成功要么全部失败的 SQL 操作。


### 事务操作示例


## 实例


```sql
try {
    // 关闭自动提交
    connection.setAutoCommit(false);

    // 执行多个 SQL 操作
    statement.executeUpdate("UPDATE accounts SET balance = balance - 100 WHERE id = 1");
    statement.executeUpdate("UPDATE accounts SET balance = balance + 100 WHERE id = 2");

    // 提交事务
    connection.commit();
    System.out.println("事务执行成功");
} catch (SQLException e) {
    // 发生错误时回滚
    connection.rollback();
    System.out.println("事务执行失败，已回滚");
    e.printStackTrace();
} finally {
    // 恢复自动提交
    connection.setAutoCommit(true);
}
```


---


## 关闭资源


### 为什么需要关闭资源

数据库连接是有限的资源，使用后必须关闭以避免资源泄漏。


### 如何正确关闭资源


## 实例


```sql
try {
    if (resultSet != null) resultSet.close();
    if (statement != null) statement.close();
    if (connection != null) connection.close();
} catch (SQLException e) {
    e.printStackTrace();
}
```


### 6.3 使用 try-with-resources


Java 7+ 可以使用 try-with-resources 自动关闭资源：


## 实例


```sql
try (Connection conn = DriverManager.getConnection(url, username, password);
     Statement stmt = conn.createStatement();
     ResultSet rs = stmt.executeQuery("SELECT * FROM users")) {

    while (rs.next()) {
        // 处理结果
    }
} catch (SQLException e) {
    e.printStackTrace();
}
```


---


## 最佳实践


### 使用连接池

生产环境中应使用连接池（如 HikariCP、c3p0）管理数据库连接：


## 实例


```sql
// HikariCP 示例
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:mysql://localhost:3306/你的数据库");
config.setUsername("用户名");
config.setPassword("密码");

HikariDataSource dataSource = new HikariDataSource(config);
Connection connection = dataSource.getConnection();
```


### 处理异常

正确处理 SQL 异常，提供有意义的错误信息：


## 实例


```sql
try {
    // 数据库操作
} catch (SQLException e) {
    System.err.println("SQL 错误: " + e.getMessage());
    System.err.println("SQL 状态: " + e.getSQLState());
    System.err.println("错误代码: " + e.getErrorCode());
}
```


### 7.3 使用 DAO 模式

将数据访问逻辑封装在 Data Access Object (DAO) 中，提高代码的可维护性：


## 实例


```sql
public class UserDao {
    private Connection connection;

    public UserDao(Connection connection) {
        this.connection = connection;
    }

    public User getUserById(int id) throws SQLException {
        String sql = "SELECT * FROM users WHERE id = ?";
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setInt(1, id);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                return new User(rs.getInt("id"), rs.getString("name"));
            }
        }
        return null;
    }
}
```


通过掌握这些基础知识，你已经可以开始在 Java 应用程序中使用 MySQL 数据库了。随着经验的积累，你可以进一步学习更高级的主题，如连接池、ORM 框架（如 Hibernate、MyBatis）等。








	  AI 思考中...





			** [MySQL Python 连接与使用](https://www.runoob.com/mysql-python-intro.html)














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