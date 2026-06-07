# Pandas 性能优化

- Source: https://www.runoob.com/pandas/pandas-optimization.html

Pandas 是一个非常强大的数据分析工具，但当数据集变得庞大时，常常会遇到性能瓶颈。

为了提高 Pandas 在处理大规模数据时的效率，了解并应用一些性能优化技巧是非常必要的。

Pandas 性能优化涉及多个方面，包括数据类型优化、避免不必要的循环、使用向量化操作、优化索引以及分块加载大数据集等方法。

下面我们将详细介绍 Pandas 性能优化的几种方法。


---

## 使用适当的数据类型


Pandas 中的数据类型（`dtype`）直接影响内存使用和计算速度。合理选择数据类型可以显著减少内存占用和加速计算。


### 1. 使用适当的数值类型


Pandas 默认的数值类型是 `int64` 和 `float64`，但对于大部分数据，这可能会浪费内存。可以使用更小的类型，如 `int8`, `int16`, `float32` 等。


| 方法 | 说明 |
| --- | --- |
| astype() | 用于转换列的数据类型 |
| downcast | 将数据类型降级，例如将 int64 降级为 int32 或 int16 |


## 实例


```python
import pandas as pd

# 示例数据
df = pd.DataFrame({'A': [100, 200, 300, 400], 'B': [1000, 2000, 3000, 4000]})

# 将列数据类型转换为较小的数据类型
df['A'] = df['A'].astype('int16')
df['B'] = df['B'].astype('int32')

print(df.dtypes)
```


**输出：**


```
A    int16
B    int32
dtype: object
```


### 2. 对字符数据使用 category 类型


对于具有重复值的字符串列，可以使用 `category` 类型来减少内存消耗。`category` 类型在内存中存储的是整数索引，而不是字符串本身。


## 实例


```python
# 示例数据
df = pd.DataFrame({'Category': ['A', 'B', 'A', 'C', 'B', 'A']})

# 使用 category 类型
df['Category'] = df['Category'].astype('category')

print(df.dtypes)
```


**输出：**


```
Category    category
dtype: object
```


---

## 使用向量化操作而非循环


Pandas 的最大优势之一就是其能够利用向量化操作进行快速的批量运算。在 Pandas 中，尽量避免使用 Python 的原生循环，应该使用 Pandas 内置的函数，这样可以利用底层的优化进行快速计算。


## 实例


```python
import pandas as pd

# 示例数据
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})

# 使用向量化操作，避免使用循环
df['C'] = df['A'] + df['B']
print(df)
```


**输出：**


```
A  B  C
0  1  5  6
1  2  6  8
2  3  7  10
3  4  8  12
```


相较于逐行处理数据，使用 Pandas 的向量化操作可以显著提高运算速度。


---

## 3. 使用 apply() 和 applymap() 优化


Pandas 提供了 `apply()` 和 `applymap()` 方法，它们可以让你在数据框架中按行或按列应用函数，能够比循环更高效。


## 实例


```python
# 使用 apply() 在列上应用自定义函数
df['D'] = df['A'].apply(lambda x: x ** 2)
print(df)
```


**输出：**


```
A  B   C   D
0  1  5   6   1
1  2  6   8   4
2  3  7  10   9
3  4  8  12  16
```


`apply()` 适用于处理一维数据，`applymap()` 则是对 DataFrame 中的每个元素应用函数，适用于二维数据。


## 实例


```python
# 使用 applymap() 对 DataFrame 的每个元素应用函数
df = df.applymap(lambda x: x * 10)
print(df)
```


**输出：**


```
A   B   C   D
0  10  50  60  10
1  20  60  80  40
2  30  70 100  90
3  40  80 120 160
```


---

## 使用合适的索引


Pandas 的索引可以提高数据的查找速度，尤其是在需要进行多次查找或数据合并时，索引可以显著提升效率。对于大数据集，确保使用适当的索引并减少不必要的索引操作可以提高性能。


## 实例


```python
# 创建索引并进行查找
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
df.set_index('A', inplace=True)

# 通过索引快速查找
print(df.loc[2])
```


**输出：**


```
B    6
Name: 2, dtype: int64
```


---

## 使用分块加载大数据集


当数据集过大时，加载整个数据集会占用大量内存，甚至导致内存溢出。此时，可以通过分块读取数据来减小内存压力。


Pandas 提供了 `chunksize` 参数，允许在读取 CSV 或 Excel 文件时分块加载数据。


## 实例


```python
# 分块读取 CSV 文件
chunksize = 10000
for chunk in pd.read_csv('large_file.csv', chunksize=chunksize):
    # 对每个数据块进行处理
    process(chunk)
```


---

## Dask 和 Vaex 是两个能够处理比内存更大的数据集的库。它们与 Pandas 兼容，支持多线程和分布式计算，可以有效地处理非常大的数据集。 实例


```python
import dask.dataframe as dd

# 使用 Dask 读取大数据集
df = dd.read_csv('large_file.csv')

# 进行计算操作
df.groupby('category').sum().compute()
```


---

## 通过 numba 加速计算


`numba` 是一个 JIT 编译器，可以将 Python 代码加速。通过将数据处理的代码加速，可以显著提高性能。特别是对于循环、数值计算等计算密集型操作，`numba` 可以极大地提高速度。


## 实例


```python
import numba
import pandas as pd

# 示例函数
@numba.jit
def calculate_square(x):
    return x ** 2

# 使用 numba 加速计算
df = pd.DataFrame({'A': [1, 2, 3, 4]})
df['B'] = df['A'].apply(calculate_square)
print(df)
```


---

## 避免链式赋值


链式赋值（chained assignment）是 Pandas 中常见的性能陷阱之一。它可能导致不必要的副作用，并且通常会减慢执行速度。最好使用明确的赋值方式，避免在同一行中进行多次赋值。


## 实例


```python
# 链式赋值：可能引发警告并影响性能
df['A'][df['A'] > 2] = 0

# 正确赋值方法：
df.loc[df['A'] > 2, 'A'] = 0
```


---

## 合并操作优化


当需要将多个 DataFrame 合并时，使用 `merge()` 或 `concat()` 时需要注意优化合并操作，特别是在处理大数据集时。可以使用 `on` 和 `how` 参数明确指定合并方式，避免不必要的计算。


## 实例


```python
import pandas as pd

# 使用合适的合并方式
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Value': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Value': ['X', 'Y', 'Z']})

# 使用 on 参数进行合并
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)
```


**输出：**


```
ID Value_x Value_y
0   1       A       X
1   2       B       Y
2   3       C       Z
```










	  AI 思考中...





			** [Pandas 高级功能](https://www.runoob.com/pandas-advanced.html)
			[Pandas 股票数据分析](https://www.runoob.com/pandas-stock.html) **













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