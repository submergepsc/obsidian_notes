# SQL COUNT() 函数

- Source: https://www.runoob.com/sql/sql-func-count.html

---


COUNT() 函数返回匹配指定条件的行数。


---


### SQL COUNT(column_name) 语法


COUNT(column_name) 函数返回指定列的值的数目（NULL 不计入）：


SELECT COUNT(column_name) FROM table_name;


### SQL COUNT(*) 语法


COUNT(*) 函数返回表中的记录数：


SELECT COUNT(*) FROM table_name;


### SQL COUNT(DISTINCT column_name) 语法


COUNT(DISTINCT column_name) 函数返回指定列的不同值的数目：


SELECT COUNT(DISTINCT column_name) FROM table_name;


**注释：**COUNT(DISTINCT) 适用于 ORACLE 和 Microsoft SQL Server，但是无法用于 Microsoft Access。


---


## 演示数据库


在本教程中，我们将使用 RUNOOB 样本数据库。


下面是选自 "access_log" 表的数据：


```
+-----+---------+-------+------------+
| aid | site_id | count | date       |
+-----+---------+-------+------------+
|   1 |       1 |    45 | 2016-05-10 |
|   2 |       3 |   100 | 2016-05-13 |
|   3 |       1 |   230 | 2016-05-14 |
|   4 |       2 |    10 | 2016-05-14 |
|   5 |       5 |   205 | 2016-05-14 |
|   6 |       4 |    13 | 2016-05-15 |
|   7 |       3 |   220 | 2016-05-15 |
|   8 |       5 |   545 | 2016-05-16 |
|   9 |       3 |   201 | 2016-05-17 |
+-----+---------+-------+------------+
```


---


## SQL COUNT(column_name) 实例


下面的 SQL 语句计算 "access_log" 表中 "site_id"=3 的总访问量：


## 实例


```sql
SELECT COUNT(count) AS nums FROM access_logWHERE
	site_id=3;
```


---


## SQL COUNT(*) 实例


下面的 SQL 语句计算 "access_log" 表中总记录数：


## 实例


```sql
SELECT COUNT(*) AS nums FROM access_log;
```


执行以上 SQL 输出结果如下：


```sql

```


---


## SQL COUNT(DISTINCT column_name) 实例


下面的 SQL 语句计算 "access_log" 表中不同 site_id 的记录数：


## 实例


```sql
SELECT COUNT(DISTINCT site_id) AS nums FROM access_log;
```


执行以上 SQL 输出结果如下：


```sql

```










	  AI 思考中...





			** [SQL AVG() 函数](https://www.runoob.com/sql-func-avg.html)
			[SQL FIRST() 函数](https://www.runoob.com/sql-func-first.html) **