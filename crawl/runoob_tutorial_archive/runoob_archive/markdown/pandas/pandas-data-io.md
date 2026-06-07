# Pandas 数据读写

- Source: https://www.runoob.com/pandas/pandas-data-io.html

Pandas 提供了丰富的函数来读取和写入各种数据格式。除了常用的 CSV 和 Excel，还支持 SQL 数据库、HTML 表格、Parquet 等格式。本节将介绍这些补充的 I/O 功能，帮助你在不同场景下灵活处理数据导入导出。


---


## 核心 I/O 函数概览


Pandas 的 I/O 功能非常强大，支持多种数据格式的读写操作。以下是常用的读取和写入函数：


| 读取函数 | 写入函数 | 支持格式 | 典型场景 |
| --- | --- | --- | --- |
| pd.read_csv() | to_csv() | CSV、TSV | 日志文件、表格数据 |
| pd.read_excel() | to_excel() | Excel（.xlsx, .xls） | 业务报表、财务数据 |
| pd.read_sql() | to_sql() | SQL 数据库 | 企业数据库交互 |
| pd.read_html() | - | HTML 表格 | 网页数据抓取 |
| pd.read_parquet() | to_parquet() | Apache Parquet | 大数据分析、存储 |
| pd.read_feather() | to_feather() | Feather 格式 | 快速读写、内存数据 |
| pd.read_json() | to_json() | JSON | API 数据、Web 服务 |
| pd.read_pickle() | to_pickle() | Python pickle | 序列化 Python 对象 |


**
不同格式有不同的适用场景。CSV 是通用格式但文件较大；Parquet 是列式存储，适合大数据分析；Excel 适合人工查看但不适合大数据量。


---


## CSV 与文本文件


CSV（Comma-Separated Values）是最通用的数据交换格式，Pandas 对它的支持也最完善。


### 常见读取参数


## 实例


```python
import pandas as pd

# 最基本的读取
df = pd.read_csv("data.csv")

# 指定分隔符（CSV 默认是逗号，TSV 是制表符）
df_tsv = pd.read_csv("data.tsv", sep="\t")

# 指定编码（处理中文文件常用）
df_utf8 = pd.read_csv("data.csv", encoding="utf-8")
df_gbk = pd.read_csv("data.csv", encoding="gbk")

# 跳过行（跳过表头后的行或注释行）
df = pd.read_csv("data.csv", skiprows=3)  # 跳过前3行
df = pd.read_csv("data.csv", skiprows=[2, 4])  # 跳过第2、4行

# 使用表头行（默认第一行）
df = pd.read_csv("data.csv", header=0)  # 第0行作为表头
df = pd.read_csv("data.csv", header=None)  # 不使用表头，自动生成 0,1,2...

# 指定列名
df = pd.read_csv("data.csv", names=["ID", "姓名", "年龄", "城市"])

# 指定索引列
df = pd.read_csv("data.csv", index_col=0)  # 第0列作为索引
df = pd.read_csv("data.csv", index_col=["姓名"])  # 多列作为复合索引
```


### 处理缺失值


## 实例


```python
import pandas as pd
import numpy as np

# 指定哪些值被视为缺失值
df = pd.read_csv(
    "data.csv",
    na_values=["NA", "null", "NULL", "N/A", "", " "]  # 这些值都会被识别为 NaN
)

# 不同的列可以用不同的缺失值标记
df = pd.read_csv(
    "data.csv",
    na_values={
        "年龄": ["未知", "0"],  # "年龄"列的缺失值
        "城市": ["未知"]        # "城市"列的缺失值
    }
)

# 保留某些值作为正常值（不被识别为缺失值）
df = pd.read_csv("data.csv", keep_default_na=False)
```


### 写入 CSV 文件


## 实例


```python
import pandas as pd

# 准备测试数据
df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 28],
    "城市": ["北京", "上海", "广州"]
})

# 写入 CSV（默认有索引）
df.to_csv("output.csv")

# 不写入索引
df.to_csv("output.csv", index=False)

# 指定分隔符
df.to_csv("output.csv", sep="\t")

# 不写入表头
df.to_csv("output.csv", header=False)

# 指定编码
df.to_csv("output.csv", encoding="utf-8-sig")  # 带 BOM，适合 Excel 打开
```


---


## JSON 文件


JSON（JavaScript Object Notation）是 Web 应用中最常见的数据格式，Pandas 提供了灵活的读写功能。


### JSON 结构与读取方式


JSON 数据结构有多种形式，读取时需要根据实际结构选择合适的参数：


## 实例


```python
import pandas as pd
import json

# 准备测试 JSON 数据
data_records = '''
[
    {"name": "张三", "age": 25, "city": "北京"},
    {"name": "李四", "age": 30, "city": "上海"},
    {"name": "王五", "age": 28, "city": "广州"}
]
'''

# 方式1：JSON 数组（每行一个对象）-> DataFrame
df = pd.read_json(data_records, orient="records")
print("orient='records':")
print(df)
print()

# 方式2：JSON 对象（键值对）-> Series
data_dict = '{"name": "张三", "age": 25, "city": "北京"}'
s = pd.read_json(data_dict, typ="series")
print("读取为 Series:")
print(s)
```


### JSON Lines 格式


JSON Lines（.jsonl）是每行一个完整 JSON 对象的格式，常用于日志和大数据场景：


## 实例


```python
import pandas as pd

# JSON Lines 格式数据
jsonl_data = '''{"name": "张三", "age": 25}
{"name": "李四", "age": 30}
{"name": "王五", "age": 28}
{"name": "赵六", "age": 35}
'''

# 写入 JSON Lines 文件
with open("data.jsonl", "w", encoding="utf-8") as f:
    f.write(jsonl_data)

# 读取 JSON Lines（每行是一个 JSON 对象）
df = pd.read_json("data.jsonl", lines=True)
print(df)
```


### 写入 JSON


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 28],
    "城市": ["北京", "上海", "广州"]
})

# 写入不同 orient 的 JSON
df.to_json("output_records.json", orient="records", force_ascii=False, indent=2)
df.to_json("output_index.json", orient="index", force_ascii=False, indent=2)
df.to_json("output_columns.json", orient="columns", force_ascii=False, indent=2)

# JSON Lines 格式
df.to_json("output.jsonl", orient="records", lines=True, force_ascii=False)
```


---


## Pickle 序列化


Pickle 是 Python 原生的对象序列化格式，可以保存任何 Python 对象，包括 DataFrame 和复杂的嵌套结构。


## 实例


```python
import pandas as pd
import pickle

# 创建复杂结构的 DataFrame
df = pd.DataFrame({
    "A": range(10),
    "B": range(10, 20),
    "C": ["foo", "bar"] * 5
})

# 写入 Pickle 文件
df.to_pickle("data.pkl")

# 读取 Pickle 文件
df_loaded = pd.read_pickle("data.pkl")
print(df_loaded)

# 压缩写入（gzip 压缩，文件更小）
df.to_pickle("data.pkl.gz", compression="gzip")
df_loaded = pd.read_pickle("data.pkl.gz", compression="gzip")
```


> Pickle 格式只能被 Python 读取，不适合跨语言数据交换。另外，从不可信来源加载 Pickle 文件存在安全风险，不要加载来源不明的 .pkl 文件。


---


## 性能与场景选择


不同的数据格式有不同的性能特点，选择合适的格式可以大幅提升效率：


| 格式 | 读取速度 | 写入速度 | 文件大小 | 适用场景 |
| --- | --- | --- | --- | --- |
| CSV | 慢 | 中 | 大 | 通用交换格式，人工可读 |
| Parquet | 很快 | 快 | 很小 | 大数据分析、列式查询 |
| Feather | 极快 | 极快 | 大 | 内存数据快速传递 |
| Pickle | 快 | 快 | 中 | Python 对象持久化 |
| JSON | 慢 | 中 | 很大 | Web API、跨语言 |


---


## 常见问题与注意事项


1、读取大文件时内存不足**


对于超大的 CSV 或 JSON 文件，可以使用 `chunksize` 参数分块读取，避免一次性加载到内存中。


**2、中文编码问题**


处理中文文件时，确保指定正确的编码。常见编码有 utf-8、gbk、gb2312、utf-8-sig（BOM）等。


**3、写入后文件损坏**


写入重要数据前，建议先读取验证。写入大文件时使用压缩格式可以减少磁盘 IO 并降低数据损坏风险。


**4、Excel 格式限制**


Excel 2003 版（.xls）单 Sheet 最多 65536 行，2007 版（.xlsx）最多 1048576 行。超出限制请考虑其他格式。









	  AI 思考中...





			** [Pandas 数据导出](https://www.runoob.com/pandas-data-export.html)
			[Pandas Index（索引）](https://www.runoob.com/pandas-index.html) **













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