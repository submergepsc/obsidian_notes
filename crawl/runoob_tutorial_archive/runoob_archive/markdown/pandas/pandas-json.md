# Pandas JSON

- Source: https://www.runoob.com/pandas/pandas-json.html

JSON（**J**ava**S**cript **O**bject **N**otation，JavaScript 对象表示法），是存储和交换文本信息的语法，类似 XML。

JSON 比 XML 更小、更快，更易解析，更多 JSON 内容可以参考 [JSON 教程](https://www.runoob.com/../json/json-tutorial.html)。


Pandas 提供了强大的方法来处理 JSON 格式的数据，支持从 JSON 文件或字符串中读取数据并将其转换为 DataFrame，以及将 DataFrame 转换回 JSON 格式。


| 操作 | 方法 | 说明 |
| --- | --- | --- |
| 从 JSON 文件/字符串读取数据 | pd.read_json() | 从 JSON 数据中读取并加载为 DataFrame |
| 将 DataFrame 转换为 JSON | DataFrame.to_json() | 将 DataFrame 转换为 JSON 格式的数据，可以指定结构化方式 |
| 支持 JSON 结构化方式 | orient 参数 | 支持多种结构化方式，如 split、records、columns |


Pandas 可以很方便的处理 JSON 数据，本文以 [sites.json](https://static.jyshare.com/download/sites.json) 为例，内容如下：


## 实例


```python
[
   {
   "id": "A001",
   "name": "菜鸟教程",
   "url": "www.runoob.com",
   "likes": 61
   },
   {
   "id": "A002",
   "name": "Google",
   "url": "www.google.com",
   "likes": 124
   },
   {
   "id": "A003",
   "name": "淘宝",
   "url": "www.taobao.com",
   "likes": 45
   }
]
```


---


## 从 JSON 文件/字符串加载数据

### pd.read_json() - 读取 JSON 数据

read_json() 用于从 JSON 格式的数据中读取并加载为一个 DataFrame。它支持从 JSON 文件、JSON 字符串或 JSON 网址中加载数据。


**语法格式：**


```
import pandas as pd

df = pd.read_json(
    path_or_buffer,      # JSON 文件路径、JSON 字符串或 URL
    orient=None,         # JSON 数据的结构方式，默认是 'columns'
    dtype=None,          # 强制指定列的数据类型
    convert_axes=True,   # 是否转换行列索引
    convert_dates=True,  # 是否将日期解析为日期类型
    keep_default_na=True # 是否保留默认的缺失值标记
)
```


** 参数说明：**

| 参数 | 说明 | 默认值 |
| --- | --- | --- |
| path_or_buffer | JSON 文件的路径、JSON 字符串或 URL | 必需参数 |
| orient | 定义 JSON 数据的格式方式。常见值有 split、records、index、columns、values。 | None（根据文件自动推断） |
| dtype | 强制指定列的数据类型 | None |
| convert_axes | 是否将轴转换为合适的数据类型 | True |
| convert_dates | 是否将日期解析为日期类型 | True |
| keep_default_na | 是否保留默认的缺失值标记（如 NaN） | True |

**常见的 orient 参数选项:**


| orient 值 | JSON 格式示例 | 描述 |
| --- | --- | --- |
| split | {"index":["a","b"],"columns":["A","B"],"data":[[1,2],[3,4]]} | 使用键 index、columns 和 data 结构 |
| records | [{"A":1,"B":2},{"A":3,"B":4}] | 每个记录是一个字典，表示一行数据 |
| index | {"a":{"A":1,"B":2},"b":{"A":3,"B":4}} | 使用索引为键，值为字典的方式 |
| columns | {"A":{"a":1,"b":3},"B":{"a":2,"b":4}} | 使用列名为键，值为字典的方式 |
| values | [[1,2],[3,4]] | 只返回数据，不包括索引和列名 |


从 JSON 文件加载数据：

## 实例


```python
import pandas as pd

df = pd.read_json('sites.json')

print(df.to_string())
```


**to_string()** 用于返回 DataFrame 类型的数据，我们也可以直接处理 JSON 字符串。


## 实例


```python
import pandas as pd

data =[
    {
      "id": "A001",
      "name": "菜鸟教程",
      "url": "www.runoob.com",
      "likes": 61
    },
    {
      "id": "A002",
      "name": "Google",
      "url": "www.google.com",
      "likes": 124
    },
    {
      "id": "A003",
      "name": "淘宝",
      "url": "www.taobao.com",
      "likes": 45
    }
]
df = pd.DataFrame(data)

print(df)
```


以上实例输出结果为：


```
id    name             url  likes
0  A001    菜鸟教程  www.runoob.com     61
1  A002  Google  www.google.com    124
2  A003      淘宝  www.taobao.com     45
```


JSON 对象与 Python 字典具有相同的格式，所以我们可以直接将 Python 字典转化为 DataFrame 数据：



## 实例


```python
import pandas as pd

# 字典格式的 JSON
s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}

# 读取 JSON 转为 DataFrame
df = pd.DataFrame(s)
print(df)
```


以上实例输出结果为：


```
col1 col2
row1     1    x
row2     2    y
row3     3    z
```


从 URL 中读取 JSON 数据：


## 实例


```python
import pandas as pd

URL = 'https://static.jyshare.com/download/sites.json'
df = pd.read_json(URL)
print(df)
```


以上实例输出结果为：


```
id    name             url  likes
0  A001    菜鸟教程  www.runoob.com     61
1  A002  Google  www.google.com    124
2  A003      淘宝  www.taobao.com     45
```


从 JSON 字符串加载数据：


## 实例


```python
import pandas as pd

# JSON 字符串
json_data = '''
[
  {"Name": "Alice", "Age": 25, "City": "New York"},
  {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
  {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]
'''

# 从 JSON 字符串读取数据
df = pd.read_json(json_data)

print(df)
```


输出：


```
Name  Age           City
0    Alice   25       New York
1      Bob   30    Los Angeles
2  Charlie   35        Chicago
```


从 JSON 数据读取（指定 orient 为 records）：


## 实例


```python
import pandas as pd

# JSON 数据
json_data = '''
[
  {"Name": "Alice", "Age": 25, "City": "New York"},
  {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
  {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]
'''

# 从 JSON 字符串读取数据，指定 orient='records'
df = pd.read_json(json_data, orient='records')

print(df)
```


输出：


```
Name  Age           City
0    Alice   25       New York
1      Bob   30    Los Angeles
2  Charlie   35        Chicago
```


### 内嵌的 JSON 数据

假设有一组内嵌的 JSON 数据文件 **nested_list.json** ：

## nested_list.json 文件内容


```python
{
    "school_name": "ABC primary school",
    "class": "Year 1",
    "students": [
    {
        "id": "A001",
        "name": "Tom",
        "math": 60,
        "physics": 66,
        "chemistry": 61
    },
    {
        "id": "A002",
        "name": "James",
        "math": 89,
        "physics": 76,
        "chemistry": 51
    },
    {
        "id": "A003",
        "name": "Jenny",
        "math": 79,
        "physics": 90,
        "chemistry": 78
    }]
}
```


使用以下代码格式化完整内容：


## 实例


```python
import pandas as pd

df = pd.read_json('nested_list.json')

print(df)
```


以上实例输出结果为：


```
school_name   class                                           students
0  ABC primary school  Year 1  {'id': 'A001', 'name': 'Tom', 'math': 60, 'phy...
1  ABC primary school  Year 1  {'id': 'A002', 'name': 'James', 'math': 89, 'p...
2  ABC primary school  Year 1  {'id': 'A003', 'name': 'Jenny', 'math': 79, 'p...
```


这时我们就需要使用到 **json_normalize()** 方法将内嵌的数据完整的解析出来：


## 实例


```python
import pandas as pd
import json

# 使用 Python JSON 模块载入数据
with open('nested_list.json','r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(data, record_path =['students'])
print(df_nested_list)
```


以上实例输出结果为：


```
id   name  math  physics  chemistry
0  A001    Tom    60       66         61
1  A002  James    89       76         51
2  A003  Jenny    79       90         78
```


**data = json.loads(f.read())** 使用 Python JSON 模块载入数据。


**json_normalize()** 使用了参数 **record_path** 并设置为 **['students']** 用于展开内嵌的 JSON 数据 **students**。


显示结果还没有包含 school_name 和 class 元素，如果需要展示出来可以使用 meta 参数来显示这些元数据：


## 实例


```python
import pandas as pd
import json

# 使用 Python JSON 模块载入数据
with open('nested_list.json','r') as f:
    data = json.loads(f.read())

# 展平数据
df_nested_list = pd.json_normalize(
    data,
    record_path =['students'],
    meta=['school_name', 'class']
)
print(df_nested_list)
```


以上实例输出结果为：


```
id   name  math  physics  chemistry         school_name   class
0  A001    Tom    60       66         61  ABC primary school  Year 1
1  A002  James    89       76         51  ABC primary school  Year 1
2  A003  Jenny    79       90         78  ABC primary school  Year 1
```


接下来，让我们尝试读取更复杂的 JSON 数据，该数据嵌套了列表和字典，数据文件 **nested_mix.json** 如下：


## nested_mix.json 文件内容


```python
{
    "school_name": "local primary school",
    "class": "Year 1",
    "info": {
      "president": "John Kasich",
      "address": "ABC road, London, UK",
      "contacts": {
        "email": "[email protected]",
        "tel": "123456789"
      }
    },
    "students": [
    {
        "id": "A001",
        "name": "Tom",
        "math": 60,
        "physics": 66,
        "chemistry": 61
    },
    {
        "id": "A002",
        "name": "James",
        "math": 89,
        "physics": 76,
        "chemistry": 51
    },
    {
        "id": "A003",
        "name": "Jenny",
        "math": 79,
        "physics": 90,
        "chemistry": 78
    }]
}
```


nested_mix.json 文件转换为 DataFrame：


## 实例


```python
import pandas as pd
import json

# 使用 Python JSON 模块载入数据
with open('nested_mix.json','r') as f:
    data = json.loads(f.read())

df = pd.json_normalize(
    data,
    record_path =['students'],
    meta=[
        'class',
        ['info', 'president'],
        ['info', 'contacts', 'tel']
    ]
)

print(df)
```


以上实例输出结果为：


```
id   name  math  physics  chemistry   class info.president info.contacts.tel
0  A001    Tom    60       66         61  Year 1    John Kasich         123456789
1  A002  James    89       76         51  Year 1    John Kasich         123456789
2  A003  Jenny    79       90         78  Year 1    John Kasich         123456789
```


### 读取内嵌数据中的一组数据


以下是实例文件 **nested_deep.json**，我们只读取内嵌中的 **math** 字段：


## nested_deep.json 文件内容


```python
{
    "school_name": "local primary school",
    "class": "Year 1",
    "students": [
    {
        "id": "A001",
        "name": "Tom",
        "grade": {
            "math": 60,
            "physics": 66,
            "chemistry": 61
        }

    },
    {
        "id": "A002",
        "name": "James",
        "grade": {
            "math": 89,
            "physics": 76,
            "chemistry": 51
        }

    },
    {
        "id": "A003",
        "name": "Jenny",
        "grade": {
            "math": 79,
            "physics": 90,
            "chemistry": 78
        }
    }]
}
```


这里我们需要使用到 **glom** 模块来处理数据套嵌，**glom** 模块允许我们使用 **.** 来访问内嵌对象的属性。


第一次使用我们需要安装 glom：


```
pip3 install glom
```


## 实例


```python
import pandas as pd
from glom import glom

df = pd.read_json('nested_deep.json')

data = df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)
```


以上实例输出结果为：


```
0    60
1    89
2    79
Name: students, dtype: int64
```


---


## 将 DataFrame 转换为 JSON

### DataFrame.to_json() - 将 DataFrame 转换为 JSON 数据

to_json() 方法用于将 DataFrame 转换为 JSON 格式的数据，可以指定 JSON 的结构化方式。


语法格式：


```
df.to_json(
    path_or_buffer=None,    # 输出的文件路径或文件对象，如果是 None 则返回 JSON 字符串
    orient=None,            # JSON 格式方式，支持 'split', 'records', 'index', 'columns', 'values'
    date_format=None,       # 日期格式，支持 'epoch', 'iso'
    default_handler=None,   # 自定义非标准类型的处理函数
    lines=False,            # 是否将每行数据作为一行（适用于 'records' 或 'split'）
    encoding='utf-8'        # 编码格式
)
```


** 参数说明：**

| 参数 | 说明 | 默认值 |
| --- | --- | --- |
| path_or_buffer | 输出的文件路径或文件对象，若为 None，则返回 JSON 字符串 | None |
| orient | 指定 JSON 格式结构，支持 split、records、index、columns、values | None（默认是 columns） |
| date_format | 日期格式，支持 'epoch' 或 'iso' 格式 | None |
| default_handler | 自定义处理非标准类型（如 datetime 等）的处理函数 | None |
| lines | 是否将每行数据作为一行输出（适用于 records 或 split） | False |
| encoding | 输出文件的编码格式 | 'utf-8' |


## 实例


```python
import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# 将 DataFrame 转换为 JSON 字符串
json_str = df.to_json()

print(json_str)
```


将 DataFrame 转换为 JSON 文件（指定 orient='records'）：


## 实例


```python
import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# 将 DataFrame 转换为 JSON 文件，指定 orient='records'
df.to_json('data.json', orient='records', lines=True)

# 输出生成的文件内容：
# [
#   {"Name":"Alice","Age":25,"City":"New York"},
#   {"Name":"Bob","Age":30,"City":"Los Angeles"},
#   {"Name":"Charlie","Age":35,"City":"Chicago"}
# ]
```


将 DataFrame 转换为 JSON 并指定日期格式：


## 实例


```python
import pandas as pd

# 创建 DataFrame，包含日期数据
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Date': pd.to_datetime(['2021-01-01', '2022-02-01', '2023-03-01']),
    'Age': [25, 30, 35]
})

# 将 DataFrame 转换为 JSON，并指定日期格式为 'iso'
json_str = df.to_json(date_format='iso')

print(json_str)
<p>
```


输出：


```
{"Name":{"0":"Alice","1":"Bob","2":"Charlie"},"Date":{"0":"2021-01-01T00:00:00.000Z","1":"2022-02-01T00:00:00.000Z","2":"2023-03-01T00:00:00.000Z"},"Age":{"0":25,"1":30,"2":35}}
```









	  AI 思考中...





			** [Pandas CSV 文件](https://www.runoob.com/pandas-csv-file.html)
			[Pandas 数据清洗](https://www.runoob.com/pandas-cleaning.html) **













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