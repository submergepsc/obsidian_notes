# MySQL WHERE 子句

- Source: https://www.runoob.com/mysql/mysql-where-clause.html

我们知道从 MySQL 表中使用 **SELECT** 语句来读取数据。

如需有条件地从表中选取数据，可将 WHERE 子句添加到 SELECT 语句中。

WHERE 子句用于在 MySQL 中过滤查询结果，只返回满足特定条件的行。


### 语法


以下是 SQL SELECT 语句使用 WHERE 子句从数据表中读取数据的通用语法：


```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```


**参数说明：**


- `column1`, `column2`, ... 是你要选择的列的名称，如果使用 `*` 表示选择所有列。
- `table_name` 是你要从中查询数据的表的名称。
- `WHERE condition` 是用于指定过滤条件的子句。


**更多说明：**


- 查询语句中你可以使用一个或者多个表，表之间使用逗号**,** 分割，并使用WHERE语句来设定查询条件。
- 你可以在 WHERE 子句中指定任何条件。
- 你可以使用 AND 或者 OR 指定一个或多个条件。
- WHERE 子句也可以运用于 SQL 的 DELETE 或者 UPDATE 命令。
- WHERE 子句类似于程序语言中的 if 条件，根据 MySQL 表中的字段值来读取指定的数据。


以下为操作符列表，可用于 WHERE 子句中。


下表中实例假定 A 为 10, B 为 20


| 操作符 | 描述 | 实例 |
| --- | --- | --- |
| = | 等号，检测两个值是否相等，如果相等返回true | (A = B) 返回false。 |
| , != | 不等于，检测两个值是否相等，如果不相等返回true | (A != B) 返回 true。 |
| > | 大于号，检测左边的值是否大于右边的值, 如果左边的值大于右边的值返回true | (A > B) 返回false。 |
| = | 大于等于号，检测左边的值是否大于或等于右边的值, 如果左边的值大于或等于右边的值返回true | (A >= B) 返回false。 |
|







	  AI 思考中...





			** [MySQL 查询数据](https://www.runoob.com/mysql-select-query.html)
			[MySQL UPDATE 更新](https://www.runoob.com/mysql-update-query.html) **