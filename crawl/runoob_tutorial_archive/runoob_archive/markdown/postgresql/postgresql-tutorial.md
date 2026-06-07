# PostgreSQL 教程

- Source: https://www.runoob.com/postgresql/postgresql-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2014/03/postgresql-11-1175122.png)

PostgreSQL 是一个免费的对象-关系数据库服务器(ORDBMS)，在灵活的BSD许可证下发行。


PostgreSQL 开发者把它念作 **post-gress-Q-L**。


PostgreSQL 的 Slogan 是 "世界上最先进的开源关系型数据库"。


参考内容：[PostgreSQL 10.1 手册](https://www.runoob.com/../manual/PostgreSQL/index.html)


---


## 什么是数据库？

数据库（Database）是按照数据结构来组织、存储和管理数据的仓库。

每个数据库都有一个或多个不同的 API 用于创建，访问，管理，搜索和复制所保存的数据。

我们也可以将数据存储在文件中，但是在文件中读写数据速度相对较慢。

所以，现在我们使用关系型数据库管理系统（RDBMS）来存储和管理的大数据量。所谓的关系型数据库，是建立在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据。

ORDBMS（对象关系数据库系统）是面向对象技术与传统的关系数据库相结合的产物，查询处理是 ORDBMS 的重要组成部分，它的性能优劣将直接影响到 DBMS 的性能。


ORDBMS 在原来关系数据库的基础上，增加了一些新的特性。


RDBMS 是关系数据库管理系统，是建立实体之间的联系，最后得到的是关系表。


OODBMS（object-oriented database management system） 面向对象数据库管理系统，将所有实体都看成对象，并将这些对象类进行封装，对象之间的通信通过消息 OODBMS 对象关系数据库在实质上还是关系数据库 。


---


## ORDBMS 术语

在我们开始学习 PostgreSQL 数据库前，让我们先了解下 ORDBMS 的一些术语：


- **数据库:** 数据库是一些关联表的集合。
- **数据表:** 表是数据的矩阵。在一个数据库中的表看起来像一个简单的电子表格。
- **列:** 一列(数据元素) 包含了相同的数据, 例如邮政编码的数据。
- **行：**一行（=元组，或记录）是一组相关的数据，例如一条用户订阅的数据。
- **冗余**：存储两倍数据，冗余降低了性能，但提高了数据的安全性。
- **主键**：主键是唯一的。一个数据表中只能包含一个主键。你可以使用主键来查询数据。
- **外键：**外键用于关联两个表。
- **复合键**：复合键（组合键）将多个列作为一个索引键，一般用于复合索引。
- **索引：**使用索引可快速访问数据库表中的特定信息。索引是对数据库表中一列或多列的值进行排序的一种结构。类似于书籍的目录。
- **参照完整性:** 参照的完整性要求关系中不允许引用不存在的实体。与实体完整性是关系模型必须满足的完整性约束条件，目的是保证数据的一致性。


---


## PostgreSQL 特征


- **函数**：通过函数，可以在数据库服务器端执行指令程序。
- **索引**：用户可以自定义索引方法，或使用内置的 B 树，哈希表与 GiST 索引。
- **触发器**：触发器是由SQL语句查询所触发的事件。如：一个INSERT语句可能触发一个检查数据完整性的触发器。触发器通常由INSERT或UPDATE语句触发。
- **多版本并发控制：**PostgreSQL使用多版本并发控制（MVCC，Multiversion concurrency control）系统进行并发控制，该系统向每个用户提供了一个数据库的"快照"，用户在事务内所作的每个修改，对于其他的用户都不可见，直到该事务成功提交。
- **规则**：规则（RULE）允许一个查询能被重写，通常用来实现对视图（VIEW）的操作，如插入（INSERT）、更新（UPDATE）、删除（DELETE）。
- **数据类型**：包括文本、任意精度的数值数组、JSON 数据、枚举类型、XML 数据等。
- **全文检索**：通过 Tsearch2 或 OpenFTS，8.3版本中内嵌 Tsearch2。
- **NoSQL**：JSON，JSONB，XML，HStore 原生支持，至 NoSQL 数据库的外部数据包装器。
- **数据仓库**：能平滑迁移至同属 PostgreSQL 生态的 GreenPlum，DeepGreen，HAWK 等，使用 FDW 进行 ETL。


---


## 相关资源


PostgreSQL 10.1 手册 在线手册：[http://www.runoob.com/manual/PostgreSQL/](https://www.runoob.com/../manual/PostgreSQL/index.html)


离线手册 - PDF 版本： [https://pan.baidu.com/s/1h1J14i8tzJUY3p9yyeW0mA](https://pan.baidu.com/s/1h1J14i8tzJUY3p9yyeW0mA)， 提取码: **xs7r**。


离线手册 - CHM 版本： [https://pan.baidu.com/s/1h1J14i8tzJUY3p9yyeW0mA](https://pan.baidu.com/s/1zzBu-Z9unrPew9wl7L_y9w)， 提取码: **tq4z**。



查看最新版：[https://github.com/postgres-cn/pgdoc-cn/releases](https://github.com/postgres-cn/pgdoc-cn/releases)








	  AI 思考中...






			[Linux 上安装 PostgreSQL](https://www.runoob.com/linux-install-postgresql.html) **













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