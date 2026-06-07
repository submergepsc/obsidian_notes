# Pandas Input/Output (输入输出) API 手册

- Source: https://www.runoob.com/pandas/pandas-io-api-reference.html

Pandas 是一个强大的 Python 数据分析库，它提供了大量的数据操作工具，包括数据的输入和输出（I/O）。

以下是 Pandas Input/Output (输入输出) 常用的 API：


### 读取数据


| 方法 | 描述 |
| --- | --- |
| pd.read_csv(filepath, sep, header, index_col) | 从 CSV 文件读取数据。 |
| pd.read_excel(io, sheet_name) | 从 Excel 文件读取数据。 |
| pd.read_json(path_or_buf) | 从 JSON 文件读取数据。 |
| pd.read_html(io) | 从 HTML 文件中读取表格数据。 |
| pd.read_sql(sql, con) | 从 SQL 数据库读取数据。 |
| pd.read_clipboard() | 从剪贴板读取数据。 |
| pd.read_parquet(path) | 从 Parquet 文件读取数据。 |
| pd.read_feather(path) | 从 Feather 文件读取数据。 |
| pd.read_hdf(path, key) | 从 HDF5 文件读取数据。 |
| pd.read_pickle(path) | 从 Pickle 文件读取数据。 |
| pd.read_sas(filepath) | 从 SAS 文件读取数据。 |
| pd.read_spss(filepath) | 从 SPSS 文件读取数据。 |
| pd.read_sql_table(table_name, con) | 从 SQL 数据库的表中读取数据。 |
| pd.read_sql_query(sql, con) | 执行 SQL 查询并读取结果。 |
| pd.read_gbq(query) | 从 Google BigQuery 读取数据。 |


---


### 写入数据


| 方法 | 描述 |
| --- | --- |
| DataFrame.to_csv(path, sep, index) | 将 DataFrame 写入 CSV 文件。 |
| DataFrame.to_excel(path, sheet_name) | 将 DataFrame 写入 Excel 文件。 |
| DataFrame.to_json(path) | 将 DataFrame 写入 JSON 文件。 |
| DataFrame.to_html(path) | 将 DataFrame 写入 HTML 文件。 |
| DataFrame.to_sql(name, con) | 将 DataFrame 写入 SQL 数据库。 |
| DataFrame.to_clipboard() | 将 DataFrame 复制到剪贴板。 |
| DataFrame.to_parquet(path) | 将 DataFrame 写入 Parquet 文件。 |
| DataFrame.to_feather(path) | 将 DataFrame 写入 Feather 文件。 |
| DataFrame.to_hdf(path, key) | 将 DataFrame 写入 HDF5 文件。 |
| DataFrame.to_pickle(path) | 将 DataFrame 写入 Pickle 文件。 |
| DataFrame.to_markdown(path) | 将 DataFrame 写入 Markdown 文件。 |
| DataFrame.to_string() | 将 DataFrame 转换为字符串。 |
| DataFrame.to_latex(path) | 将 DataFrame 写入 LaTeX 文件。 |
| DataFrame.to_records() | 将 DataFrame 转换为 numpy 记录数组。 |
| DataFrame.to_dict() | 将 DataFrame 转换为字典。 |
| DataFrame.to_numpy() | 将 DataFrame 转换为 numpy 数组。 |


---


### 实例


## 实例


```python
import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('data.csv')

# 读取 Excel 文件
df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# 读取 JSON 文件
df_json = pd.read_json('data.json')

# 写入 CSV 文件
df.to_csv('output.csv', index=False)

# 写入 Excel 文件
df.to_excel('output.xlsx', sheet_name='Sheet1')

# 写入 JSON 文件
df.to_json('output.json')
```


---


### 详细参数说明


#### pd.read_csv()


| 参数 | 描述 |
| --- | --- |
| filepath | 文件路径。 |
| sep | 分隔符，默认为 ,。 |
| header | 指定作为列名的行号，默认为 0（第一行）。 |
| index_col | 指定作为索引的列号或列名。 |
| dtype | 指定列的数据类型。 |
| na_values | 指定哪些值应被视为缺失值。 |


#### DataFrame.to_csv()


| 参数 | 描述 |
| --- | --- |
| path | 文件路径。 |
| sep | 分隔符，默认为 ,。 |
| index | 是否写入索引，默认为 True。 |
| header | 是否写入列名，默认为 True。 |
| encoding | 文件编码，默认为 utf-8。 |


#### pd.read_excel()


| 参数 | 描述 |
| --- | --- |
| io | 文件路径或文件对象。 |
| sheet_name | 工作表名称或索引，默认为 0。 |
| header | 指定作为列名的行号，默认为 0。 |
| index_col | 指定作为索引的列号或列名。 |


#### DataFrame.to_excel()


| 参数 | 描述 |
| --- | --- |
| path | 文件路径。 |
| sheet_name | 工作表名称，默认为 Sheet1。 |
| index | 是否写入索引，默认为 True。 |
| header | 是否写入列名，默认为 True。 |


---


如果需要更详细的信息，可以参考 [Pandas 官方文档](https://pandas.pydata.org/docs/reference/io.html)。








	  AI 思考中...





			** [Pandas DataFrame API 手册](https://www.runoob.com/pandas-dataframe-api-reference.html)
			[Pandas 常用函数](https://www.runoob.com/pandas-general-functions.html) **













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