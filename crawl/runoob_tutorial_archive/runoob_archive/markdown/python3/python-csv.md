# Python csv 模块

- Source: https://www.runoob.com/python3/python-csv.html

CSV（Comma-Separated Values）文件是一种常见的文件格式，用于存储表格数据。

CSV 文件由纯文本组成，每一行代表表格中的一行数据，而每一列则通过逗号（或其他分隔符）分隔。

CSV 文件通常用于数据交换，因为它简单且易于处理。


Python 提供了一个内置的 `csv` 模块，用于读取和写入 CSV 文件。这个模块简化了处理 CSV 文件的过程，使得开发者可以轻松地操作表格数据。


---


### 1. 读取 CSV 文件


要读取 CSV 文件，可以使用 `csv.reader` 对象。以下是一个简单的示例：


## 实例


```python
import csv

# 打开 CSV 文件
with open('data.csv', mode='r', encoding='utf-8') as file:
    # 创建 csv.reader 对象
    csv_reader = csv.reader(file)

    # 逐行读取数据
    for row in csv_reader:
        print(row)
```


#### 代码解释：


- `open('data.csv', mode='r', encoding='utf-8')`：以只读模式打开名为 `data.csv` 的文件，并指定编码为 UTF-8。
- `csv.reader(file)`：创建一个 `csv.reader` 对象，用于读取文件内容。
- `for row in csv_reader`：逐行读取文件内容，每一行数据会被解析为一个列表。


---


### 2. 写入 CSV 文件


要写入 CSV 文件，可以使用 `csv.writer` 对象。以下是一个示例：


## 实例


```python
import csv

# 要写入的数据
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles']
]

# 打开 CSV 文件
with open('output.csv', mode='w', encoding='utf-8', newline='') as file:
    # 创建 csv.writer 对象
    csv_writer = csv.writer(file)

    # 写入数据
    for row in data:
        csv_writer.writerow(row)
```


#### 代码解释：


- `open('output.csv', mode='w', encoding='utf-8', newline='')`：以写入模式打开名为 `output.csv` 的文件，并指定编码为 UTF-8。`newline=''` 用于避免在 Windows 系统中出现空行。
- `csv.writer(file)`：创建一个 `csv.writer` 对象，用于写入文件内容。
- `csv_writer.writerow(row)`：将每一行数据写入文件。


---


### 3. 使用字典读取和写入 CSV 文件


`csv` 模块还提供了 `DictReader` 和 `DictWriter` 类，它们可以将 CSV 文件的每一行解析为字典，或者将字典写入 CSV 文件。


#### 使用 DictReader 读取 CSV 文件：


## 实例


```python
import csv

with open('data.csv', mode='r', encoding='utf-8') as file:
    csv_dict_reader = csv.DictReader(file)

    for row in csv_dict_reader:
        print(row)
```


#### 使用 DictWriter 写入 CSV 文件：


## 实例


```python
import csv

data = [
    {'Name': 'Alice', 'Age': '30', 'City': 'New York'},
    {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'}
]

with open('output.csv', mode='w', encoding='utf-8', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)

    # 写入表头
    csv_dict_writer.writeheader()

    # 写入数据
    for row in data:
        csv_dict_writer.writerow(row)
```


---


## 常用的属性和方法

### csv 模块核心方法

| 方法 | 说明 | 示例 |
| --- | --- | --- |
| csv.reader() | 从文件对象读取 CSV 数据 | reader = csv.reader(file) |
| csv.writer() | 将数据写入 CSV 文件 | writer = csv.writer(file) |
| csv.DictReader() | 将 CSV 行读取为字典（带表头） | dict_reader = csv.DictReader(file) |
| csv.DictWriter() | 将字典写入 CSV 文件（需指定字段名） | dict_writer = csv.DictWriter(file, fieldnames) |
| csv.register_dialect() | 注册自定义 CSV 格式（如分隔符） | csv.register_dialect('mydialect', delimiter='\|') |
| csv.unregister_dialect() | 删除已注册的方言 | csv.unregister_dialect('mydialect') |
| csv.list_dialects() | 列出所有已注册的方言 | print(csv.list_dialects()) |

### csv.reader 和 csv.writer 对象常用方法

| 方法 | 说明 | 适用对象 |
| --- | --- | --- |
| __next__() | 迭代读取下一行（或使用 for 循环） | reader |
| writerow(row) | 写入单行数据 | writer |
| writerows(rows) | 写入多行数据（列表的列表） | writer |


### csv.DictReader 和 csv.DictWriter 对象特性

| 特性/方法 | 说明 | 示例 |
| --- | --- | --- |
| fieldnames | 字段名列表（DictReader 自动从首行获取） | dict_reader.fieldnames |
| writeheader() | 写入表头行（DictWriter 专用） | dict_writer.writeheader() |


### 常用参数说明


| 参数 | 说明 | 示例值 | 适用方法 |
| --- | --- | --- | --- |
| delimiter | 字段分隔符 | ','（默认）, '\t' | reader/writer |
| quotechar | 引用字符（包围特殊字段） | '"'（默认） | reader/writer |
| quoting | 引用规则 | csv.QUOTE_ALL（全部引用） | reader/writer |
| skipinitialspace | 忽略分隔符后的空格 | True/False | reader |
| lineterminator | 行结束符 | '\r\n'（默认） | writer |
| dialect | 预定义的方言名称 | 'excel'（默认） | 所有方法 |


### 实例

1. 读取 CSV 文件


## 实例


```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)  # 每行是一个列表
```


2. 写入 CSV 文件


## 实例


```python
data = [['Name', 'Age'], ['Alice', 25], ['Bob', 30]]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # 写入多行
```


3. 使用 DictReader 和 DictWriter（带表头）


## 实例


```python
# 读取
with open('data.csv', 'r') as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        print(row['Name'], row['Age'])  # 通过字段名访问

# 写入
fieldnames = ['Name', 'Age']
with open('output.csv', 'w', newline='') as file:
    dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    dict_writer.writeheader()  # 写入表头
    dict_writer.writerow({'Name': 'Alice', 'Age': 25})
```


4. 自定义方言（如处理 TSV 文件）


## 实例


```python
csv.register_dialect('tsv', delimiter='\t', quoting=csv.QUOTE_NONE)

with open('data.tsv', 'r') as file:
    reader = csv.reader(file, dialect='tsv')
    for row in reader:
        print(row)
```










	  AI 思考中...





			** [Python queue 模块](https://www.runoob.com/python-queue.html)
			[Python logging 模块](https://www.runoob.com/python-logging.html) **













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