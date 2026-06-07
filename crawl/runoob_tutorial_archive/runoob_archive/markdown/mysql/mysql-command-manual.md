# MySQL 命令大全

- Source: https://www.runoob.com/mysql/mysql-command-manual.html

## 基础命令


| 操作 | 命令 |
| --- | --- |
| 连接到 MySQL 数据库 | mysql -u 用户名 -p |
| 查看所有数据库 | SHOW DATABASES; |
| 选择一个数据库 | USE 数据库名; |
| 查看所有表 | SHOW TABLES; |
| 查看表结构 | DESCRIBE 表名; 或 SHOW COLUMNS FROM 表名; |
| 创建一个新数据库 | CREATE DATABASE 数据库名; |
| 删除一个数据库 | DROP DATABASE 数据库名; |
| 创建一个新表 | CREATE TABLE 表名 (列名1 数据类型 [约束], 列名2 数据类型 [约束], ...); |
| 删除一个表 | DROP TABLE 表名; |
| 插入数据 | INSERT INTO 表名 (列1, 列2, ...) VALUES (值1, 值2, ...); |
| 查询数据 | SELECT 列1, 列2, ... FROM 表名 WHERE 条件; |
| 更新数据 | UPDATE 表名 SET 列1 = 值1, 列2 = 值2, ... WHERE 条件; |
| 删除数据 | DELETE FROM 表名 WHERE 条件; |
| 创建用户 | CREATE USER '用户名'@'主机' IDENTIFIED BY '密码'; |
| 授权用户 | GRANT 权限 ON 数据库名.* TO '用户名'@'主机'; |
| 刷新权限 | FLUSH PRIVILEGES; |
| 查看当前用户 | SELECT USER(); |
| 退出 MySQL | EXIT; |


## 数据库相关命令

下面是与 MySQL 数据库操作相关的命令，包括创建、删除和修改数据库等操作：


| 操作 | 命令 |
| --- | --- |
| 创建数据库 | CREATE DATABASE 数据库名; |
| 删除数据库 | DROP DATABASE 数据库名; |
| 修改数据库编码格式和排序规则 | ALTER DATABASE 数据库名 DEFAULT CHARACTER SET 编码格式 DEFAULT COLLATE 排序规则; |
| 查看所有数据库 | SHOW DATABASES; |
| 查看数据库详细信息 | SHOW CREATE DATABASE 数据库名; |
| 选择数据库 | USE 数据库名; |
| 查看数据库的状态信息 | SHOW STATUS; |
| 查看数据库的错误信息 | SHOW ERRORS; |
| 查看数据库的警告信息 | SHOW WARNINGS; |
| 查看数据库的表 | SHOW TABLES; |
| 查看表的结构 | DESC 表名;DESCRIBE 表名;SHOW COLUMNS FROM 表名;EXPLAIN 表名; |
| 创建表 | CREATE TABLE 表名 (列名1 数据类型 [约束], 列名2 数据类型 [约束], ...); |
| 删除表 | DROP TABLE 表名; |
| 修改表结构 | ALTER TABLE 表名 ADD 列名 数据类型 [约束];ALTER TABLE 表名 DROP 列名;ALTER TABLE 表名 MODIFY 列名 数据类型 [约束]; |
| 查看表的创建 SQL | SHOW CREATE TABLE 表名; |


## 数据表相关命令

以下是与 MySQL 数据表相关的常用命令，包括创建、修改、删除表以及查看表的结构和数据等操作：


| 操作 | 命令 |
| --- | --- |
| 创建表 | CREATE TABLE 表名 (列名1 数据类型 [约束], 列名2 数据类型 [约束], ...); |
| 删除表 | DROP TABLE 表名; |
| 修改表结构 | 添加列: ALTER TABLE 表名 ADD 列名 数据类型 [约束];删除列: ALTER TABLE 表名 DROP 列名;修改列: ALTER TABLE 表名 MODIFY 列名 数据类型 [约束];重命名列: ALTER TABLE 表名 CHANGE 旧列名 新列名 数据类型 [约束]; |
| 查看表结构 | DESC 表名;DESCRIBE 表名;SHOW COLUMNS FROM 表名;EXPLAIN 表名; |
| 查看表的创建 SQL | SHOW CREATE TABLE 表名; |
| 查看表中的所有数据 | SELECT * FROM 表名; |
| 插入数据 | INSERT INTO 表名 (列1, 列2, ...) VALUES (值1, 值2, ...); |
| 更新数据 | UPDATE 表名 SET 列1 = 值1, 列2 = 值2, ... WHERE 条件; |
| 删除数据 | DELETE FROM 表名 WHERE 条件; |
| 查看表的索引 | SHOW INDEX FROM 表名; |
| 创建索引 | CREATE INDEX 索引名 ON 表名 (列名); |
| 删除索引 | DROP INDEX 索引名 ON 表名; |
| 查看表的约束 | SHOW CREATE TABLE 表名; (约束信息会包含在创建表的 SQL 中) |
| 查看表的统计信息 | SHOW TABLE STATUS LIKE '表名'; |


## MySQL 事务相关命令

以下是与 MySQL 事务相关的常用命令：


| 操作 | 命令 |
| --- | --- |
| 开始事务 | START TRANSACTION; 或 BEGIN; |
| 提交事务 | COMMIT; |
| 回滚事务 | ROLLBACK; |
| 查看当前事务的状态 | SHOW ENGINE INNODB STATUS; (可查看 InnoDB 存储引擎的事务状态) |
| 锁定表以进行事务操作 | LOCK TABLES 表名 WRITE; 或 LOCK TABLES 表名 READ; |
| 释放锁定的表 | UNLOCK TABLES; |
| 设置事务的隔离级别 | SET TRANSACTION ISOLATION LEVEL READ COMMITTED;SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED; |








	  AI 思考中...





			** [MySQL 运算符](https://www.runoob.com/mysql-operator.html)
			[MySQL 测验](https://www.runoob.com/mysql-quiz.html) **













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