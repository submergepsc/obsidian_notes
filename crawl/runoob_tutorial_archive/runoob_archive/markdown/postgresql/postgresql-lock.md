# PostgreSQL LOCK（锁）

- Source: https://www.runoob.com/postgresql/postgresql-lock.html

锁主要是为了保持数据库数据的一致性，可以阻止用户修改一行或整个表，一般用在并发较高的数据库中。


在多个用户访问数据库的时候若对并发操作不加控制就可能会读取和存储不正确的数据，破坏数据库的一致性。

数据库中有两种基本的锁：排它锁（Exclusive Locks）和共享锁（Share Locks）。

如果数据对象加上排它锁，则其他的事务不能对它读取和修改。


如果加上共享锁，则该数据库对象可以被其他事务读取，但不能修改。


### LOCK 命令语法


LOCK 命令基础语法如下：


```
LOCK [ TABLE ]
name
 IN
lock_mode
```


- name：要锁定的现有表的名称（可选模式限定）。如果只在表名之前指定，则只锁定该表。如果未指定，则锁定该表及其所有子表（如果有）。
- lock_mode：锁定模式指定该锁与哪个锁冲突。如果没有指定锁定模式，则使用限制最大的访问独占模式。可能的值是：ACCESS SHARE，ROW SHARE， ROW EXCLUSIVE， SHARE UPDATE EXCLUSIVE， SHARE，SHARE ROW EXCLUSIVE，EXCLUSIVE，ACCESS EXCLUSIVE。


一旦获得了锁，锁将在当前事务的其余时间保持。没有解锁表命令；锁总是在事务结束时释放。


### 死锁


当两个事务彼此等待对方完成其操作时，可能会发生死锁。尽管 PostgreSQL 可以检测它们并以回滚结束它们，但死锁仍然很不方便。为了防止应用程序遇到这个问题，请确保将应用程序设计为以相同的顺序锁定对象。


### 咨询锁


PostgreSQL 提供了创建具有应用程序定义含义的锁的方法。这些被称为咨询锁。由于系统不强制使用它们，所以正确使用它们取决于应用程序。咨询锁对于不适合 MVCC 模型的锁定策略非常有用。


例如，咨询锁的一个常见用途是模拟所谓"平面文件"数据管理系统中典型的悲观锁定策略。虽然存储在表中的标志可以用于相同的目的，但是通知锁更快，避免了表膨胀，并且在会话结束时由服务器自动清理。


### 实例


创建 COMPANY 表（[下载 COMPANY SQL 文件](https://static.jyshare.com/download/company.sql) ），数据内容如下：


```
runoobdb# select * from COMPANY;
 id | name  | age | address   | salary
----+-------+-----+-----------+--------
  1 | Paul  |  32 | California|  20000
  2 | Allen |  25 | Texas     |  15000
  3 | Teddy |  23 | Norway    |  20000
  4 | Mark  |  25 | Rich-Mond |  65000
  5 | David |  27 | Texas     |  85000
  6 | Kim   |  22 | South-Hall|  45000
  7 | James |  24 | Houston   |  10000
(7 rows)
```


下面的示例将 runoobdb 数据库中的 COMPANY 表锁定为 ACCESS EXCLUSIVE 模式。


LOCK 语句只在事务模式下工作。


```
runoobdb=#BEGIN;
LOCK TABLE company1 IN ACCESS EXCLUSIVE MODE;
```


上面操作将得到下面结果：


```
LOCK TABLE
```


上面的消息指示表被锁定，直到事务结束，并且要完成事务，您必须回滚或提交事务。








	  AI 思考中...





			** [PostgreSQL TRANSACTION（事务）](https://www.runoob.com/postgresql-transaction.html)
			[PostgreSQL 子查询](https://www.runoob.com/postgresql-sub-queries.html) **













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