# Pandas 读取 SQL 数据库

- Source: https://www.runoob.com/pandas/pandas-sql.html

Pandas 提供了一组直接与 SQL 数据库交互的函数，可以将查询结果直接读取为 DataFrame，也可以将 DataFrame 写回数据库。这使得数据分析师无需手动处理数据库连接和结果解析，大幅简化了数据库与 Python 的交互流程。


---


## 核心函数概览


| 函数 | 用途 | 返回类型 |
| --- | --- | --- |
| pd.read_sql() | 执行 SQL 查询或读取整张表（兼容两种场景的通用函数） | DataFrame |
| pd.read_sql_query() | 执行 SQL 查询语句，适合复杂查询 | DataFrame |
| pd.read_sql_table() | 直接读取整张表，仅支持 SQLAlchemy 连接 | DataFrame |
| DataFrame.to_sql() | 将 DataFrame 写入数据库表 | None / int |


**
实际工作中推荐使用 `pd.read_sql()`，它会根据传入参数自动判断是执行查询还是读取整表，兼容性最好。`pd.read_sql_table()` 仅支持 SQLAlchemy 引擎连接，不支持原生 `sqlite3` 等 DB-API 连接。


---


## 建立数据库连接


Pandas 本身不直接连接数据库，需要借助第三方库建立连接后传入。主流方式有两种：SQLAlchemy 引擎**（推荐）和 **DB-API 原生连接**（轻量简单）。


### 方式一：SQLAlchemy（推荐）


SQLAlchemy 是 Python 最主流的数据库工具包，支持所有主流数据库，且与 Pandas 兼容性最好：


```
pip install sqlalchemy
```


## 实例


```python
from sqlalchemy import create_engine

# SQLAlchemy 连接字符串格式：数据库类型+驱动://用户名:密码@主机:端口/数据库名
# SQLite（文件数据库，无需用户名密码）
engine = create_engine("sqlite:///mydata.db")

# MySQL
engine = create_engine("mysql+pymysql://root:password@localhost:3306/mydb")

# PostgreSQL
engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/mydb")

# SQL Server
engine = create_engine("mssql+pyodbc://user:password@server/mydb?driver=ODBC+Driver+17+for+SQL+Server")

# 验证连接是否成功
with engine.connect() as conn:
    print("连接成功")
```


### 方式二：sqlite3 原生连接（仅 SQLite）


Python 内置 `sqlite3` 模块，无需额外安装，适合轻量级本地 SQLite 数据库：


## 实例


```python
import sqlite3

# 连接到 SQLite 文件数据库（文件不存在时自动创建）
conn = sqlite3.connect("mydata.db")

# 连接到内存数据库（程序退出后数据消失，适合测试）
conn_memory = sqlite3.connect(":memory:")

# 使用完毕后需手动关闭连接
# conn.close()
```


---


## pd.read_sql() 读取数据


### 基本语法


```
pd.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)
```


主要参数说明：


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| sql | str | SQL 查询语句，或表名（与 con 类型有关） |
| con | 连接对象 | SQLAlchemy 引擎或 DB-API 连接对象 |
| index_col | str 或 list | 将指定列设为 DataFrame 的行索引 |
| params | list 或 dict | SQL 参数化查询的参数值，防止 SQL 注入 |
| parse_dates | list 或 dict | 将指定列解析为 datetime 类型 |
| chunksize | int | 分块读取，每块返回指定行数的 DataFrame 迭代器 |


### 1、读取整张表


## 实例


```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydata.db")

# 读取整张 employees 表
df = pd.read_sql("employees", con=engine)
print(df.head())
print(f"共 {len(df)} 行，{len(df.columns)} 列")
```


### 2、执行 SQL 查询


## 实例


```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydata.db")

# 带条件的查询
df = pd.read_sql("SELECT * FROM employees WHERE department = 'IT'", con=engine)

# 多表关联查询
sql = """
    SELECT e.name, e.salary, d.department_name
    FROM employees e
    JOIN departments d ON e.dept_id = d.id
    WHERE e.salary > 10000
    ORDER BY e.salary DESC
"""
df = pd.read_sql(sql, con=engine)
print(df.head(10))
```


### 3、参数化查询（防止 SQL 注入）


查询条件来自用户输入时，**务必使用参数化查询**，不要用字符串拼接 SQL：


## 实例


```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydata.db")

# &#x274c; 危险写法：字符串拼接 SQL，存在 SQL 注入风险
dept = "IT"
# df = pd.read_sql(f"SELECT * FROM employees WHERE department = '{dept}'", engine)

# &#x2705; 安全写法：使用 ? 占位符（sqlite3）或 :name 命名参数（SQLAlchemy）
# SQLite / DB-API 风格（使用 ?）
df = pd.read_sql(
    "SELECT * FROM employees WHERE department = ? AND salary > ?",
    con=engine,
    params=["IT", 8000]   # params 是列表，按位置替换 ?
)

# SQLAlchemy 命名参数风格（使用 :param_name）
from sqlalchemy import text
with engine.connect() as conn:
    df = pd.read_sql(
        text("SELECT * FROM employees WHERE department = :dept AND salary > :min_salary"),
        con=conn,
        params={"dept": "IT", "min_salary": 8000}
    )

print(df)
```


### 4、设置索引列


## 实例


```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydata.db")

# 将数据库中的 id 列设为 DataFrame 的行索引
df = pd.read_sql("SELECT * FROM employees", con=engine, index_col="id")
print(df.head())

# 使用多列作为复合索引
df = pd.read_sql(
    "SELECT * FROM orders",
    con=engine,
    index_col=["year", "month"]  # 复合索引
)
```


### 5、解析日期列


数据库中存储的日期字段读取后默认是字符串类型，使用 `parse_dates` 参数可以直接解析为 `datetime`：


## 实例


```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydata.db")

# 将 created_at 和 updated_at 列解析为 datetime 类型
df = pd.read_sql(
    "SELECT * FROM orders",
    con=engine,
    parse_dates=["created_at", "updated_at"]
)

print(df.dtypes)
# created_at    datetime64[ns]
# updated_at    datetime64[ns]

# 也可以指定解析格式（针对非标准日期格式）
df = pd.read_sql(
    "SELECT * FROM orders",
    con=engine,
    parse_dates={"created_at": "%Y%m%d"}  # 将 "20240115" 这样的格式解析为日期
)
```


---


## 分块读取大数据（chunksize）


当数据库表数据量很大时，一次性全部读入内存会导致 OOM（内存溢出）。使用 `chunksize` 参数可以将数据分批读取，每次只处理一部分：


## 实例


```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:password@localhost/bigdata")

# chunksize=10000 表示每次读取 10000 行，返回一个迭代器
chunks = pd.read_sql("SELECT * FROM large_table", con=engine, chunksize=10000)

# 逐块处理（每次只有 10000 行在内存中）
result_list = []
for i, chunk in enumerate(chunks):
    # 对每块数据执行处理逻辑（如过滤、聚合等）
    processed = chunk[chunk["status"] == "active"]
    result_list.append(processed)
    print(f"已处理第 {i+1} 块，当前块有效行数：{len(processed)}")

# 将所有处理后的块合并为一个 DataFrame
final_df = pd.concat(result_list, ignore_index=True)
print(f"最终共 {len(final_df)} 行有效数据")
```


---


## pd.read_sql_query() 和 pd.read_sql_table()


### pd.read_sql_query()：只执行查询


与 `pd.read_sql()` 功能基本相同，但只接受 SQL 查询语句，不接受表名。参数完全一致，适合需要明确区分"查询"和"读表"操作的场景：


## 实例


```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydata.db")

df = pd.read_sql_query(
    "SELECT name, salary FROM employees WHERE salary > 5000",
    con=engine
)
print(df)
```


### pd.read_sql_table()：读取整张表（仅 SQLAlchemy）


`pd.read_sql_table()` 专门用于读取整张表，支持通过参数过滤列和行，但**仅支持 SQLAlchemy 引擎连接**，不支持 sqlite3 等原生连接：


## 实例


```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydata.db")

# 读取 employees 表的指定列
df = pd.read_sql_table(
    "employees",
    con=engine,
    columns=["id", "name", "salary", "department"]  # 只读取这几列
)

# 还支持指定 schema（数据库中的模式）
df = pd.read_sql_table(
    "employees",
    con=engine,
    schema="hr"    # 读取 hr 模式下的 employees 表
)

print(df.head())
```


---


## 将 DataFrame 写入数据库（to_sql）


使用 `DataFrame.to_sql()` 可以将 DataFrame 写入数据库，支持新建表、追加数据或覆盖原表：


### 基本语法


```
DataFrame.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None, method=None)
```


`if_exists` 参数决定目标表已存在时的行为：


| if_exists 值 | 行为 | 适用场景 |
| --- | --- | --- |
| 'fail'（默认） | 表已存在时报错 | 防止意外覆盖已有数据 |
| 'replace' | 先删除原表，再重新建表写入 | 全量刷新数据 |
| 'append' | 向已有表追加数据，不改变表结构 | 增量写入新数据 |


## 实例


```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydata.db")

# 准备示例数据
df = pd.DataFrame({
    "name": ["张三", "李四", "王五"],
    "department": ["IT", "HR", "IT"],
    "salary": [12000, 8000, 15000]
})

# 将 DataFrame 写入 employees 表，如果已存在则替换
df.to_sql(
    "employees",
    con=engine,
    if_exists="replace",  # 覆盖原有数据
    index=False           # 不将 DataFrame 的行索引写入数据库（通常不需要）
)

# 向已有表追加新数据（注意：列名和数据类型必须匹配）
new_employees = pd.DataFrame({
    "name": ["赵六"],
    "department": ["Finance"],
    "salary": [11000]
})
new_employees.to_sql("employees", con=engine, if_exists="append", index=False)

# 验证写入结果
result = pd.read_sql("SELECT * FROM employees", con=engine)
print(result)
```


### 指定列的数据类型


写入时可以通过 `dtype` 参数显式指定每列在数据库中的类型：


## 实例


```python
import pandas as pd
from sqlalchemy import create_engine, Integer, String, Float, DateTime

engine = create_engine("sqlite:///mydata.db")

df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "score": [92.5, 88.0, 95.3],
})

df.to_sql(
    "students",
    con=engine,
    if_exists="replace",
    index=False,
    dtype={
        "id":    Integer(),   # 整数类型
        "name":  String(50),  # 变长字符串，最大 50 字符
        "score": Float()      # 浮点数
    }
)
```


---


## 完整使用示例


下面是一个从 SQLite 数据库中读取销售数据并进行分析的完整示例：


## 实例


```python
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# 第一步：准备测试数据库
engine = create_engine("sqlite:///sales.db")
conn = sqlite3.connect("sales.db")

# 创建示例数据并写入数据库
sales_data = pd.DataFrame({
    "order_id":   [1001, 1002, 1003, 1004, 1005, 1006],
    "product":    ["笔记本", "手机", "平板", "笔记本", "手机", "平板"],
    "amount":     [6999, 3999, 2999, 7299, 4299, 3199],
    "quantity":   [2, 5, 3, 1, 4, 2],
    "order_date": ["2024-01-10", "2024-01-15", "2024-01-20",
                   "2024-02-05", "2024-02-10", "2024-02-18"]
})
sales_data.to_sql("sales", con=engine, if_exists="replace", index=False)

# 第二步：读取数据并解析日期
df = pd.read_sql(
    "SELECT * FROM sales",
    con=engine,
    parse_dates=["order_date"]
)
print("原始数据：")
print(df)
print()

# 第三步：按产品统计销售额
sql_agg = """
    SELECT product,
           COUNT(*) AS 订单数,
           SUM(amount * quantity) AS 总销售额,
           AVG(amount) AS 平均单价
    FROM sales
    GROUP BY product
    ORDER BY 总销售额 DESC
"""
summary = pd.read_sql(sql_agg, con=engine)
print("各产品销售汇总：")
print(summary)
print()

# 第四步：将统计结果写回数据库
summary.to_sql("sales_summary", con=engine, if_exists="replace", index=False)
print("汇总数据已写入 sales_summary 表")

conn.close()
```


以上代码执行结果为：


```
原始数据：
   order_id product  amount  quantity order_date
0      1001     笔记本    6999         2 2024-01-10
1      1002      手机    3999         5 2024-01-15
2      1003      平板    2999         3 2024-01-20
3      1004     笔记本    7299         1 2024-02-05
4      1005      手机    4299         4 2024-02-10
5      1006      平板    3199         2 2024-02-18

各产品销售汇总：
  product  订单数  总销售额   平均单价
0     手机    2   36991   4149.0
1    笔记本    2   21297   7149.0
2     平板    2   15395   3099.0

汇总数据已写入 sales_summary 表
```


---


## 常见问题与注意事项


**1、连接用完后需要关闭**


使用 DB-API 原生连接时（如 sqlite3），操作完成后需手动关闭连接。推荐用 `with` 语句自动管理：


## 实例


```python
import sqlite3
import pandas as pd

# 使用 with 语句，退出时自动关闭连接，即使发生异常也不会泄漏连接
with sqlite3.connect("mydata.db") as conn:
    df = pd.read_sql("SELECT * FROM employees", con=conn)

print(df)  # 连接已自动关闭，但 df 数据仍然可用
```


**2、大表不要直接读取全部数据**


对于几百万行以上的大表，直接 `SELECT *` 读取全量数据会耗尽内存。应优先在 SQL 层面过滤数据（WHERE、LIMIT），或使用 `chunksize` 分块读取。


**3、read_sql_table 仅支持 SQLAlchemy**


若使用 sqlite3 等 DB-API 原生连接调用 `pd.read_sql_table()`，会报 `NotImplementedError`。请改用 `pd.read_sql()` 或换用 SQLAlchemy 引擎。


**4、to_sql 的 index 参数默认为 True**


默认情况下 `to_sql` 会把 DataFrame 的行索引（0, 1, 2...）也写入数据库，形成一个名为 `index` 的列，通常这是多余的。建议明确传入 `index=False`。


**5、数据库驱动需单独安装**


SQLAlchemy 连接不同数据库时，还需安装对应的驱动包：


| 数据库 | 驱动包 | 安装命令 |
| --- | --- | --- |
| MySQL | PyMySQL | pip install pymysql |
| PostgreSQL | psycopg2 | pip install psycopg2-binary |
| SQL Server | pyodbc | pip install pyodbc |
| Oracle | cx_Oracle | pip install cx_Oracle |
| SQLite | 内置 | 无需安装 |








	  AI 思考中...





			** [Pandas pd.Series() 函数](https://www.runoob.com/pandas-pd-series.html)
			[Pandas 读取 HTML 表格](https://www.runoob.com/pandas-html-tables.html) **













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