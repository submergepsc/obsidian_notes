# SQL DEFAULT 约束

- Source: https://www.runoob.com/sql/sql-default.html

DEFAULT 约束用于向列中插入默认值。


如果没有规定其他的值，那么会将默认值添加到所有的新记录。


### 语法


** 1、在创建表时定义 DEFAULT 约束：**


```
CREATE TABLE 表名 (
    列名 数据类型 DEFAULT 默认值
);
```


**2、在现有表中添加 DEFAULT 约束：**


```
ALTER TABLE 表名
ALTER COLUMN 列名 SET DEFAULT 默认值;
```


---


### 实例


**1、创建表时定义 DEFAULT 约束**


## 实例


```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    HireDate DATE DEFAULT GETDATE(), -- 默认值为当前日期
    Salary DECIMAL(10, 2) DEFAULT 0.00 -- 默认值为 0.00
);
```


**2、在现有表中添加 DEFAULT 约束**


```
ALTER TABLE Employees
ALTER COLUMN Salary SET DEFAULT 0.00;
```


**3、插入数据时使用默认值**


```
INSERT INTO Employees (EmployeeID, FirstName, LastName)
VALUES (1, 'John', 'Doe');
```


如果未提供 HireDate 和 Salary 的值，数据库会自动使用默认值。


---


### 删除 DEFAULT 约束


不同数据库的删除方式有所不同：


**1、SQL Server**


```
ALTER TABLE 表名
DROP CONSTRAINT 约束名;
```


**2、MySQL**


```
ALTER TABLE 表名
ALTER COLUMN 列名 DROP DEFAULT;
```


**3、Oracle**


```
ALTER TABLE 表名
MODIFY 列名 DEFAULT NULL;
```


**4、MS Access**


```
ALTER TABLE 表名
ALTER COLUMN 列名 DROP DEFAULT;
```


### 注意事项


- `DEFAULT` 约束的值必须与列的数据类型兼容。
- 如果列定义为 `NOT NULL` 且未提供默认值，插入数据时必须显式提供值，否则会报错。
- 默认值可以是常量值、表达式或函数（如 `GETDATE()`）。


### 适用场景

- 为日期列设置当前日期为默认值。
- 为数值列设置初始值（如 `0`）。
- 为状态列设置默认状态（如 `'Active'`）。








	  AI 思考中...





			** [SQL CHECK 约束](https://www.runoob.com/sql-check.html)
			[SQL CREATE INDEX 语句](https://www.runoob.com/sql-create-index.html) **













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