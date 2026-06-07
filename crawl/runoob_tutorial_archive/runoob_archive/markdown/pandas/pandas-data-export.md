# Pandas 数据导出

- Source: https://www.runoob.com/pandas/pandas-data-export.html

Pandas 提供了丰富的导出功能，可以将 DataFrame 导出为各种常见格式，包括 CSV、Excel、SQL 数据库、JSON 等。本节详细介绍各种导出方式的使用方法和注意事项。


---


## 导出为 CSV


CSV 是最通用的数据交换格式，导出会受环境默认编码影响，需要注意中文编码问题。


### 基本导出


## 实例


```python
import pandas as pd

# 准备测试数据
df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六"],
    "年龄": [25, 30, 28, 35],
    "城市": ["北京", "上海", "广州", "深圳"],
    "薪资": [12000, 15000, 11000, 18000]
})

# 最基本的导出（包含索引）
df.to_csv("output.csv")

# 不包含索引
df.to_csv("output.csv", index=False)
```


### 中文编码处理


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "城市": ["北京", "上海", "广州"]
})

# UTF-8 编码（推荐）
df.to_csv("output_utf8.csv", encoding="utf-8")

# UTF-8 with BOM（Excel 打开不乱码）
df.to_csv("output_utf8_bom.csv", encoding="utf-8-sig")

# GBK 编码（适合老旧系统）
df.to_csv("output_gbk.csv", encoding="gbk")

# 验证编码
import os
print("文件大小对比：")
for f in ["output_utf8.csv", "output_utf8_bom.csv", "output_gbk.csv"]:
    print(f"{f}: {os.path.getsize(f)} bytes")
```


### 导出选项详解


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四"],
    "年龄": [25, 30]
})

# 指定分隔符（默认是逗号）
df.to_csv("output.tsv", sep="\t")  # TSV 格式

# 不写入表头
df.to_csv("output.csv", header=False)

# 自定义列名（当 header=False 时）
df.to_csv("output.csv", header=False, columns=["姓名", "年龄"])

# 只导出特定列
df.to_csv("output.csv", columns=["姓名"])  # 只导出"姓名"列

# 缺失值处理
import numpy as np
df_with_na = pd.DataFrame({
    "A": [1, 2, np.nan, 4],
    "B": ["a", None, "c", "d"]
})
df_with_na.to_csv("output.csv", na_rep="NULL")  # 指定缺失值表示形式

# 浮点数精度
df = pd.DataFrame({"value": [1.23456789, 2.3456789]})
df.to_csv("output.csv", float_format="%.2f")  # 保留2位小数
```


---


## 导出为 Excel


Excel 格式适合人工查看和编辑，但大文件导出较慢。


### 安装依赖


```
pip install openpyxl xlwt
```


### 基本导出


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 28],
    "城市": ["北京", "上海", "广州"],
    "薪资": [12000, 15000, 11000]
})

# 导出为 Excel（.xlsx 格式，需要 openpyxl）
df.to_excel("output.xlsx", index=False)

# 导出为老版本 .xls 格式（需要 xlwt）
df.to_excel("output.xls", index=False)
```


### 多 Sheet 导出


## 实例


```python
import pandas as pd

# 创建多个 DataFrame
df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
df2 = pd.DataFrame({"C": [7, 8, 9], "D": [10, 11, 12]})

# 导出到同一个 Excel 的不同 Sheet
with pd.ExcelWriter("output.xlsx", engine="openpyxl") as writer:
    df1.to_excel(writer, sheet_name="Sheet1", index=False)
    df2.to_excel(writer, sheet_name="Sheet2", index=False)

print("多 Sheet 导出成功")
```


### 格式化导出


## 实例


```python
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

# 创建 DataFrame
df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 28],
    "薪资": [12000, 15000, 11000]
})

# 使用 ExcelWriter 进行更精细的控制
with pd.ExcelWriter("output_formatted.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="员工信息", index=False)

    # 获取工作表
    worksheet = writer.sheets["员工信息"]

    # 设置列宽
    worksheet.column_dimensions["A"].width = 15
    worksheet.column_dimensions["B"].width = 10
    worksheet.column_dimensions["C"].width = 12

    # 冻结首行
    worksheet.freeze_panes = "A2"

print("格式化导出完成")
```


---


## 导出为数据库


可以直接将 DataFrame 导出到 SQL 数据库，详见《Pandas 读取 SQL 数据库》一章。


## 实例


```python
import pandas as pd
from sqlalchemy import create_engine

# 创建内存数据库
engine = create_engine("sqlite:///output.db")

# 准备数据
df = pd.DataFrame({
    "name": ["张三", "李四", "王五"],
    "age": [25, 30, 28],
    "city": ["北京", "上海", "广州"]
})

# 导出到数据库
# if_exists: 'fail'(默认) / 'replace' / 'append'
df.to_sql("users", con=engine, if_exists="replace", index=False)

print("导出到数据库成功")
```


---


## 导出为 JSON


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 28]
})

# 不同 orient 格式
df.to_json("records.json", orient="records", force_ascii=False, indent=2)
df.to_json("index.json", orient="index", force_ascii=False)
df.to_json("columns.json", orient="columns", force_ascii=False)

# JSON Lines 格式（每行一个 JSON 对象，适合日志）
df.to_json("lines.json", orient="records", lines=True, force_ascii=False)
```


---


## 导出为其他格式


### 导出为 HTML


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四"],
    "年龄": [25, 30]
})

# 导出为 HTML 表格
df.to_html("output.html", index=False)

# 添加样式
df.to_html(
    "output_styled.html",
    index=False,
    border=2,
    classes=["table", "table-striped"]  # 添加 CSS 类
)
```


### 导出为 Markdown


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 28]
})

# 导出为 Markdown 表格
print(df.to_markdown(index=False))
# 输出:
# | 姓名 | 年龄 |
# | ---- | ---- |
# | 张三 | 25   |
# | 李四 | 30   |
# | 王五 | 28   |

# 保存到文件
with open("output.md", "w") as f:
    f.write(df.to_markdown(index=False))
```


### 导出为 LaTeX


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四"],
    "年龄": [25, 30]
})

# 导出为 LaTeX 表格
print(df.to_latex(index=False))
# 输出 LaTeX 表格代码
```


### 导出为 Pickle


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": ["a", "b", "c"]
})

# 导出为 Pickle（保持数据类型）
df.to_pickle("data.pkl")

# 压缩格式
df.to_pickle("data.pkl.gz", compression="gzip")

print("Pickle 导出完成")
```


---


## 大数据量导出


导出大数据量时需要注意内存和性能问题。


## 实例


```python
import pandas as pd

# 大数据量导出建议：
# 1. 使用 chunksize 分批写入
df = pd.DataFrame({"a": range(1000000), "b": range(1000000)})

# CSV 分块写入
csv_path = "large_output.csv"
df.to_csv(csv_path, index=False, chunksize=100000)

# 2. 使用更高效的格式（Parquet）
df.to_parquet("large_output.parquet", index=False)

# 3. 使用压缩格式减少 IO
df.to_csv("large_output.csv.gz", index=False, compression="gzip")

print("大数据量导出完成")
```


---


## 常见问题与注意事项


**1、Excel 打开 CSV 文件乱码**


使用 `utf-8-sig` 编码导出，Excel 可以正确识别中文。


**2、导出大数据时内存不足**


使用 `chunksize` 参数分批写入，或使用 Parquet 格式替代 CSV。


**3、日期时间格式丢失**


CSV 导出时会转换为字符串，可以指定 `date_format` 参数控制格式。


**4、导出到数据库类型不匹配**


可以使用 `dtype` 参数显式指定列类型。


**
日常数据分析推荐使用 Parquet 格式，它具有高压缩比、快速读写、保持数据类型等优点。只有在需要人工查看或分享时才使用 Excel 或 CSV 格式。









	  AI 思考中...





			** [Pandas 读取 Parquet / Feather 文件](https://www.runoob.com/pandas-parquet-feather.html)
			[Pandas 数据读写](https://www.runoob.com/pandas-data-io.html) **













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