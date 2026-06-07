# MySQL Python 连接与使用

- Source: https://www.runoob.com/mysql/mysql-python-intro.html

MySQL 是最流行的开源关系型数据库之一，而 Python 是当今最受欢迎的编程语言之一。将 Python 与 MySQL 结合使用，可以让我们轻松地开发数据库驱动的应用程序。

本文将详细介绍如何使用 Python 连接和操作 MySQL 数据库，内容包含如下：


- 如何安装 MySQL Python 驱动
- 建立和关闭数据库连接
- 执行各种 SQL 查询
- 事务管理和错误处理
- 数据库操作的最佳实践


---


## 准备工作


### 安装必要的软件


在开始之前，请确保你已经安装了以下软件：


- **Python** (推荐 3.6 或更高版本)
- **MySQL Server** (社区版即可)
- **MySQL Connector/Python** (Python 的 MySQL 驱动)


### 安装 MySQL Connector/Python


可以通过 pip 安装 MySQL 官方提供的 Python 驱动：


```
pip install mysql-connector-python
```


或者安装 PyMySQL (另一个流行的 MySQL Python 驱动):


```
pip install pymysql
```


---


## 连接 MySQL 数据库


### 建立基本连接


以下是使用 `mysql-connector-python` 建立数据库连接的基本代码：


## 实例


```sql
import mysql.connector

# 创建数据库连接
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

print("数据库连接成功!")
```


### 连接参数说明


- `host`: MySQL 服务器地址 (本地为 "localhost")
- `user`: 数据库用户名
- `password`: 用户密码
- `database`: 要连接的数据库名称 (可选)


### 使用 PyMySQL 连接


如果你选择使用 PyMySQL，连接方式略有不同：


## 实例


```sql
import pymysql

# 创建数据库连接
db = pymysql.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

print("数据库连接成功!")
```


---


## 执行 SQL 查询


### 创建游标对象


在执行 SQL 语句前，我们需要创建一个游标(cursor)对象：


## 实例


```sql
cursor = db.cursor()
```


### 执行 SELECT 查询


## 实例


```sql
cursor.execute("SELECT * FROM your_table")

# 获取所有结果
results = cursor.fetchall()

for row in results:
    print(row)
```


### 执行 INSERT, UPDATE, DELETE 操作


## 实例


```sql
# 插入数据
sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
values = ("张三", 25)
cursor.execute(sql, values)

# 提交事务
db.commit()

print(cursor.rowcount, "条记录插入成功")
```


### 使用参数化查询


为了防止 SQL 注入，应该始终使用参数化查询：


## 实例


```sql
sql = "SELECT * FROM users WHERE name = %s"
name = ("张三",)
cursor.execute(sql, name)
```


---


## 事务管理


### 事务的基本概念


MySQL 事务是一组原子性的 SQL 查询，要么全部执行成功，要么全部不执行。


### 使用事务


## 实例


```sql
try:
    # 开始事务
    cursor.execute("START TRANSACTION")

    # 执行多个SQL语句
    cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")

    # 提交事务
    db.commit()
    print("事务执行成功")
except Exception as e:
    # 发生错误，回滚事务
    db.rollback()
    print("事务执行失败:", e)
```


---


## 错误处理


### 捕获数据库错误


## 实例


```sql
try:
    cursor.execute("SELECT * FROM non_existent_table")
except mysql.connector.Error as err:
    print("数据库错误:", err)
```


### 常见错误代码


- `1045`: 访问被拒绝 (错误的用户名或密码)
- `1049`: 未知数据库
- `1146`: 表不存在
- `1062`: 重复键值


---


## 关闭连接


### 正确关闭连接


完成数据库操作后，应该关闭游标和连接：


## 实例


```sql
cursor.close()
db.close()
print("数据库连接已关闭")
```


### 使用 with 语句


Python 的 `with` 语句可以自动管理资源：


## 实例


```sql
with mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
) as db:
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for row in results:
            print(row)
# 离开with块后连接会自动关闭
```


---


## 最佳实践


### 连接池


对于频繁连接数据库的应用，建议使用连接池：


## 实例


```sql
from mysql.connector import pooling

# 创建连接池
db_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

# 从连接池获取连接
db = db_pool.get_connection()
```


### ORM 框架


对于复杂应用，可以考虑使用 ORM (对象关系映射) 框架，如 SQLAlchemy 或 Django ORM。


---









	  AI 思考中...





			** [MySQL Node.js 连接与使用](https://www.runoob.com/mysql-nodejs-intro.html)
			[MySQL Java 连接与使用](https://www.runoob.com/mysql-java-intro.html) **













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