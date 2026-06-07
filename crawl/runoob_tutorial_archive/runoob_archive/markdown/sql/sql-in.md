# SQL IN 操作符

- Source: https://www.runoob.com/sql/sql-in.html

---


## IN 操作符


IN 操作符允许您在 WHERE 子句中规定多个值。


### SQL IN 语法


```
SELECT column1, column2, ...
FROM table_name
WHERE column IN (value1, value2, ...);
```


参数说明：


- **column1, column2, ...**：要选择的字段名称，可以为多个字段。如果不指定字段名称，则会选择所有字段。
- **table_name**：要查询的表名称。
- **column**：要查询的字段名称。
- **value1, value2, ...**：要查询的值，可以为多个值。


## 演示数据库


在本教程中，我们将使用 RUNOOB 样本数据库。


下面是选自 "Websites" 表的数据：


```
mysql> SELECT * FROM Websites;
+----+---------------+---------------------------+-------+---------+
| id | name          | url                       | alexa | country |
+----+---------------+---------------------------+-------+---------+
|  1 | Google        | https://www.google.cm/    |     1 | USA     |
|  2 | 淘宝          | https://www.taobao.com/   |    13 | CN      |
|  3 | 菜鸟教程       | http://www.runoob.com/    |  5000 | USA     |
|  4 | 微博           | http://weibo.com/         |    20 | CN      |
|  5 | Facebook      | https://www.facebook.com/ |     3 | USA     |
|  7 | stackoverflow | http://stackoverflow.com/ |     0 | IND     |
+----+---------------+---------------------------+-------+---------+
```


---


## IN 操作符实例


下面的 SQL 语句选取 name 为 "Google" 或 "菜鸟教程" 的所有网站：


## 实例


```sql
SELECT * FROM Websites

WHERE name IN ('Google','菜鸟教程');
```


执行输出结果：


```sql

```










	  AI 思考中...





			** [SQL 通配符](https://www.runoob.com/sql-wildcards.html)
			[SQL BETWEEN 操作符](https://www.runoob.com/sql-between.html) **