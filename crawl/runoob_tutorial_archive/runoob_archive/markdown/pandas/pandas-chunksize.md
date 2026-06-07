# Pandas 处理大文件（chunksize）

- Source: https://www.runoob.com/pandas/pandas-chunksize.html

处理大型数据文件时，内存可能不足以一次性加载所有数据。Pandas 提供了分块读取功能，可以分批处理数据。


---


## 分块读取 CSV


### chunksize 参数


## 实例


```python
import pandas as pd
import io

# 模拟大文件内容（实际使用时替换为文件路径）
data = """id,value
1,100
2,200
3,300
4,400
5,500
6,600
7,700
8,800
9,900
10,1000
"""

# 使用 chunksize 分块读取
chunks = pd.read_csv(io.StringIO(data), chunksize=3)

print("分块处理：")
for i, chunk in enumerate(chunks):
    print(f"\n块 {i+1}:")
    print(chunk)
```


### 聚合处理


## 实例


```python
import pandas as pd
import io
import numpy as np

# 模拟大文件
data = "value\n" + "\n".join([str(i) for i in range(1, 1001)])

# 分块计算总和
total = 0
count = 0

for chunk in pd.read_csv(io.StringIO(data), chunksize=100):
    total += chunk["value"].sum()
    count += len(chunk)

print(f"总行数: {count}")
print(f"总和: {total}")
print(f"平均值: {total / count}")
```


---


## 增量处理


### 筛选过滤


## 实例


```python
import pandas as pd
import io

# 模拟数据
data = """id,value,category
1,100,A
2,200,B
3,150,A
4,300,C
5,250,B
6,180,A
"""

# 筛选特定条件的数据
filtered_chunks = []

for chunk in pd.read_csv(io.StringIO(data), chunksize=2):
    filtered = chunk[chunk["category"] == "A"]
    if len(filtered) > 0:
        filtered_chunks.append(filtered)

result = pd.concat(filtered_chunks)
print("筛选 category='A' 的数据：")
print(result)
```


### 多进程并行处理


## 实例


```python
import pandas as pd
import io
from concurrent.futures import ProcessPoolExecutor

# 并行处理（适用于CPU密集型任务）
def process_chunk(chunk):
    """处理单个数据块"""
    return chunk["value"].sum()

# 模拟数据
data = "value\n" + "\n".join([str(i) for i in range(1, 101)])

# 准备数据块
chunks = list(pd.read_csv(io.StringIO(data), chunksize=10))

# 串行处理
total = sum(process_chunk(chunk) for chunk in chunks)
print(f"串行处理总和: {total}")
```


---


## 处理 JSON 大文件


## 实例


```python
import pandas as pd
import json
import io

# 模拟 JSON Lines 格式数据
jsonl_data = '\n'.join([
    json.dumps({"id": i, "value": i * 10})
    for i in range(1, 101)
])

# 分块读取 JSON Lines
chunks = []
chunk_size = 20

for chunk in pd.read_json(io.StringIO(jsonl_data), lines=True, chunksize=chunk_size):
    chunks.append(chunk)
    if len(chunks) >= 3:  # 只处理前3块作为示例
        break

result = pd.concat(chunks)
print(f"读取了 {len(result)} 行数据")
print(result.head())
```


**
分块处理可以显著降低内存占用，但会增加处理时间。合理选择 chunk 大小以平衡内存和时间。









	  AI 思考中...





			** [Pandas 数据分箱（cut / qcut）](https://www.runoob.com/pandas-cut.html)
			[Pandas 与 NumPy 结合使用](https://www.runoob.com/pandas-numpy.html) **













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