# MySQL Node.js 连接与使用

- Source: https://www.runoob.com/mysql/mysql-nodejs-intro.html

MySQL 是最流行的开源关系型数据库之一，而 Node.js 是一个基于 Chrome V8 引擎的 JavaScript 运行时环境，将两者结合可以构建强大的后端服务。


**为什么选择 MySQL + Node.js？**


- MySQL 提供可靠的数据存储和管理
- Node.js 的非阻塞 I/O 模型适合数据库操作
- JavaScript 全栈开发（前后端使用同种语言）
- 丰富的 npm 生态中有许多 MySQL 相关包


### 安装必要的依赖


在开始之前，我们需要安装 `mysql2` 包，这是 Node.js 中连接 MySQL 的流行选择。


```
npm install mysql2
```


**为什么选择 mysql2 而不是 mysql？**


- 更好的性能
- 支持 Promise API
- 支持预处理语句
- 活跃的维护


---


## 建立数据库连接


### 基本连接配置


## 实例


```sql
const mysql = require('mysql2');

// 创建连接池（推荐生产环境使用）
const pool = mysql.createPool({
  host: 'localhost',     // 数据库服务器地址
  user: 'root',          // 数据库用户名
  password: 'password',  // 数据库密码
  database: 'test_db',   // 要连接的数据库名称
  waitForConnections: true,
  connectionLimit: 10,   // 连接池最大连接数
  queueLimit: 0
});

// 获取一个 Promise 版本的连接
const promisePool = pool.promise();
```


### 连接池 vs 单一连接


**连接池优点：**


- 复用连接，减少开销
- 自动管理连接生命周期
- 防止连接泄漏
- 更好的性能表现


**单一连接适用场景：**


- 简单脚本
- 测试环境
- 低并发应用


---


## 执行基本 CRUD 操作


### 查询数据（SELECT）


## 实例


```sql
async function getUsers() {
  try {
    const [rows, fields] = await promisePool.query('SELECT * FROM users');
    console.log(rows);
    return rows;
  } catch (err) {
    console.error('查询出错:', err);
    throw err;
  }
}
```


### 插入数据（INSERT）


## 实例


```sql
async function addUser(user) {
  try {
    const [result] = await promisePool.query(
      'INSERT INTO users (name, email) VALUES (?, ?)',
      [user.name, user.email]
    );
    console.log('插入ID:', result.insertId);
    return result;
  } catch (err) {
    console.error('插入出错:', err);
    throw err;
  }
}
```


### 更新数据（UPDATE）


## 实例


```sql
async function updateUser(id, updates) {
  try {
    const [result] = await promisePool.query(
      'UPDATE users SET name = ?, email = ? WHERE id = ?',
      [updates.name, updates.email, id]
    );
    console.log('影响行数:', result.affectedRows);
    return result;
  } catch (err) {
    console.error('更新出错:', err);
    throw err;
  }
}
```


### 删除数据（DELETE）


## 实例


```sql
async function deleteUser(id) {
  try {
    const [result] = await promisePool.query(
      'DELETE FROM users WHERE id = ?',
      [id]
    );
    console.log('删除行数:', result.affectedRows);
    return result;
  } catch (err) {
    console.error('删除出错:', err);
    throw err;
  }
}
```


---


## 高级功能与最佳实践


### 事务处理


## 实例


```sql
async function transferFunds(fromId, toId, amount) {
  let connection;
  try {
    // 从连接池获取连接
    connection = await promisePool.getConnection();

    // 开始事务
    await connection.beginTransaction();

    // 执行转账操作
    await connection.query(
      'UPDATE accounts SET balance = balance - ? WHERE id = ?',
      [amount, fromId]
    );

    await connection.query(
      'UPDATE accounts SET balance = balance + ? WHERE id = ?',
      [amount, toId]
    );

    // 提交事务
    await connection.commit();
    console.log('转账成功');
  } catch (err) {
    // 出错时回滚
    if (connection) await connection.rollback();
    console.error('转账失败:', err);
    throw err;
  } finally {
    // 释放连接回连接池
    if (connection) connection.release();
  }
}
```


### 预处理语句


预处理语句可以提高性能并防止 SQL 注入：


## 实例


```sql
async function getUserById(id) {
  try {
    // 准备预处理语句
    const [rows] = await promisePool.execute(
      'SELECT * FROM users WHERE id = ?',
      [id]
    );
    return rows[0];
  } catch (err) {
    console.error('查询出错:', err);
    throw err;
  }
}
```


### 连接池事件监听


## 实例


```sql
pool.on('connection', (connection) => {
  console.log('新连接建立');
});

pool.on('acquire', (connection) => {
  console.log('连接被获取');
});

pool.on('release', (connection) => {
  console.log('连接被释放');
});

pool.on('enqueue', () => {
  console.log('等待可用连接');
});
```


---


## 错误处理与调试


### 常见错误类型


- **连接错误**：数据库服务器不可达、认证失败等
- **查询语法错误**：SQL 语句有误
- **约束违反**：如重复主键、外键约束等
- **超时错误**：查询执行时间过长


### 错误处理策略


## 实例


```sql
async function safeQuery(sql, params) {
  try {
    const [rows] = await promisePool.query(sql, params);
    return rows;
  } catch (err) {
    // 根据错误类型采取不同措施
    switch (err.code) {
      case 'ER_DUP_ENTRY':
        console.warn('重复条目:', err.sqlMessage);
        throw new Error('数据已存在');
      case 'ECONNREFUSED':
        console.error('无法连接数据库');
        throw new Error('服务不可用，请稍后再试');
      default:
        console.error('数据库错误:', err);
        throw err;
    }
  }
}
```


---


## 性能优化建议


- **合理设置连接池大小**：通常为 CPU 核心数的 2-3 倍
- **使用连接池而非单个连接**：特别是在 Web 应用中
- **合理使用索引**：加速查询性能
- **批量操作**：减少往返次数
- **使用预处理语句**：提高重复查询性能
- **定期释放资源**：避免连接泄漏


**批量插入示例：**


## 实例


```sql
async function batchInsertUsers(users) {
  const values = users.map(user => [user.name, user.email]);

  try {
    const [result] = await promisePool.query(
      'INSERT INTO users (name, email) VALUES ?',
      [values]
    );
    console.log('插入行数:', result.affectedRows);
    return result;
  } catch (err) {
    console.error('批量插入出错:', err);
    throw err;
  }
}
```


---


## 安全注意事项


- **永远不要拼接 SQL 字符串**：使用参数化查询防止 SQL 注入
- **限制数据库用户权限**：应用账号只需必要权限
- **加密敏感数据**：如密码应加盐哈希存储
- **使用 SSL 连接**：生产环境建议加密连接
- **定期更新依赖**：保持 mysql2 包为最新版本


---


## 完整示例项目结构


```
project/
├── config/
│   └── db.js          # 数据库配置
├── models/
│   └── userModel.js   # 数据模型
├── services/
│   └── userService.js # 业务逻辑
├── app.js             # 主应用文件
└── package.json
```


**db.js 示例:**


## 实例


```sql
const mysql = require('mysql2');

const pool = mysql.createPool({
  host: process.env.DB_HOST || 'localhost',
  user: process.env.DB_USER || 'root',
  password: process.env.DB_PASSWORD || '',
  database: process.env.DB_NAME || 'test_db',
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
});

module.exports = pool.promise();
```










	  AI 思考中...





			** [MySQL 测验](https://www.runoob.com/mysql-quiz.html)
			[MySQL Python 连接与使用](https://www.runoob.com/mysql-python-intro.html) **













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