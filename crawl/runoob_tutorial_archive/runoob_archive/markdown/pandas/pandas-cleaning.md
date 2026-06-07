# Pandas 数据清洗

- Source: https://www.runoob.com/pandas/pandas-cleaning.html

数据清洗是对一些没有用的数据进行处理的过程。

很多数据集存在数据缺失、数据格式错误、错误数据或重复数据的情况，如果要使数据分析更加准确，就需要对这些没有用的数据进行处理。


数据清洗与预处理的常见步骤：


- **缺失值处理**：识别并填补缺失值，或删除含缺失值的行/列。
- **重复数据处理**：检查并删除重复数据，确保每条数据唯一。
- **异常值处理**：识别并处理异常值，如极端值、错误值。
- **数据格式转换**：转换数据类型或进行单位转换，如日期格式转换。
- **标准化与归一化**：对数值型数据进行标准化（如 Z-score）或归一化（如 Min-Max）。
- **类别数据编码**：将类别变量转换为数值形式，常见方法包括 One-Hot 编码和标签编码。
- **文本处理**：对文本数据进行清洗，如去除停用词、词干化、分词等。
- **数据抽样**：从数据集中抽取样本，或通过过采样/欠采样处理类别不平衡。
- **特征工程**：创建新特征、删除不相关特征、选择重要特征等。


在这个教程中，我们将利用 Pandas包来进行数据清洗。


本文使用到的测试数据 [property-data.csv](https://static.jyshare.com/download/property-data.csv) 如下：


![](https://www.runoob.com/wp-content/uploads/2021/06/6A6DE9DA-E0EE-4001-8C21-1D6A8EBF70FF.jpeg)


上表包含了四种空数据：


- n/a
- NA
- —
- na


---


## Pandas 清洗空值


如果我们要删除包含空字段的行，可以使用 **dropna()** 方法，语法格式如下：


```
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
```


**参数说明：**

- axis：默认为 **0**，表示逢空值剔除整行，如果设置参数 **axis＝1** 表示逢空值去掉整列。
- how：默认为 **'any'** 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 **how='all'** 一行（或列）都是 NA 才去掉这整行。
- thresh：设置需要多少非空值的数据才可以保留下来的。
- subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
- inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。

我们可以通过 **isnull()** 判断各个单元格是否为空。


## 实例


```python
import pandas as pd

df = pd.read_csv('property-data.csv')

print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())
```


以上实例输出结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/06/2A5B93BC-E0A3-4864-98B7-7DAE0E92C5F2.jpg)


以上例子中我们看到 Pandas 把 n/a 和 NA 当作空数据，na 不是空数据，不符合我们要求，我们可以指定空数据类型：


## 实例


```python
import pandas as pd

missing_values = ["n/a", "na", "--"]
df = pd.read_csv('property-data.csv', na_values = missing_values)

print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())
```


以上实例输出结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/06/FCE8C077-C981-4764-ACBC-CB129304F831.jpg)


接下来的实例演示了删除包含空数据的行。


## 实例


```python
import pandas as pd

df = pd.read_csv('property-data.csv')

new_df = df.dropna()

print(new_df.to_string())
```


以上实例输出结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/06/4744B204-1527-49DE-B749-E39D6C7DFE01.jpg)


**注意：**默认情况下，dropna() 方法返回一个新的 DataFrame，不会修改源数据。


如果你要修改源数据 DataFrame, 可以使用 **inplace = True** 参数:


## 实例


```python
import pandas as pd

df = pd.read_csv('property-data.csv')

df.dropna(inplace = True)

print(df.to_string())
```


以上实例输出结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/06/4744B204-1527-49DE-B749-E39D6C7DFE01.jpg)


我们也可以移除指定列有空值的行：


## 实例

移除 ST_NUM 列中字段值为空的行：


```python
import pandas as pd

df = pd.read_csv('property-data.csv')

df.dropna(subset=['ST_NUM'], inplace = True)

print(df.to_string())
```


以上实例输出结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/06/C83C70BC-5E47-4397-938D-7445104BE551.jpg)


我们也可以 **fillna()** 方法来替换一些空字段：


## 实例

使用 12345 替换空字段：


```python
import pandas as pd

df = pd.read_csv('property-data.csv')

df.fillna(12345, inplace = True)

print(df.to_string())
```


以上实例输出结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/06/5033AA75-BC7D-4192-9428-221765EA3C58.jpg)


我们也可以指定某一个列来替换数据：


## 实例

使用 12345 替换 PID 为空数据：


```python
import pandas as pd

df = pd.read_csv('property-data.csv')

df['PID'].fillna(12345, inplace = True)

print(df.to_string())
```


以上实例输出结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/06/2F955E95-8C4C-4E7C-B788-5714B2C898C2.jpg)


替换空单元格的常用方法是计算列的均值、中位数值或众数。

Pandas使用 **mean()**、**median()** 和 **mode()** 方法计算列的均值（所有值加起来的平均值）、中位数值（排序后排在中间的数）和众数（出现频率最高的数）。


## 实例

使用 mean() 方法计算列的均值并替换空单元格：


```python
import pandas as pd

df = pd.read_csv('property-data.csv')

x = df["ST_NUM"].mean()

df["ST_NUM"].fillna(x, inplace = True)

print(df.to_string())
```


以上实例输出结果如下，红框为计算的均值替换来空单元格：


![](https://www.runoob.com/wp-content/uploads/2021/06/6A758363-02FA-4F6E-9F30-7A3E4489639A.jpg)


## 实例

使用 median() 方法计算列的中位数并替换空单元格：


```python
import pandas as pd

df = pd.read_csv('property-data.csv')

x = df["ST_NUM"].median()

df["ST_NUM"].fillna(x, inplace = True)

print(df.to_string())
```


以上实例输出结果如下，红框为计算的中位数替换来空单元格：


![](https://www.runoob.com/wp-content/uploads/2021/06/551B8875-D393-4003-BB68-695EBEDBB0FE.jpg)


## 实例

使用 mode() 方法计算列的众数并替换空单元格：


```python
import pandas as pd

df = pd.read_csv('property-data.csv')

x = df["ST_NUM"].mode()

df["ST_NUM"].fillna(x, inplace = True)

print(df.to_string())
```


以上实例输出结果如下，红框为计算的众数替换来空单元格：


![](https://www.runoob.com/wp-content/uploads/2021/06/40F6D1C2-CFD7-4C53-B887-86695F486E6D.jpg)


---


## Pandas 清洗格式错误数据

数据格式错误的单元格会使数据分析变得困难，甚至不可能。


我们可以通过包含空单元格的行，或者将列中的所有单元格转换为相同格式的数据。


以下实例会格式化日期：


## 实例


```python
import pandas as pd

# 第三个日期格式错误
data = {
  "Date": ['2020/12/01', '2020/12/02' , '20201226'],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())
```


以上实例输出结果如下：


```
Date  duration
day1 2020-12-01        50
day2 2020-12-02        40
day3 2020-12-26        45
```


---


## Pandas 清洗错误数据

数据错误也是很常见的情况，我们可以对错误的数据进行替换或移除。


以下实例会替换错误年龄的数据：


## 实例


```python
import pandas as pd

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)

df.loc[2, 'age'] = 30 # 修改数据

print(df.to_string())
```


以上实例输出结果如下：


```
name  age
0  Google   50
1  Runoob   40
2  Taobao   30
```


也可以设置条件语句：


## 实例

将 age 大于 120 的设置为 120:


```python
import pandas as pd

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 200, 12345]
}

df = pd.DataFrame(person)

for x in df.index:
  if df.loc[x, "age"] > 120:
    df.loc[x, "age"] = 120

print(df.to_string())
```


以上实例输出结果如下：


```
name  age
0  Google   50
1  Runoob  120
2  Taobao  120
```


也可以将错误数据的行删除：


## 实例

将 age 大于 120 的删除:


```python
import pandas as pd

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)

for x in df.index:
  if df.loc[x, "age"] > 120:
    df.drop(x, inplace = True)

print(df.to_string())
```


以上实例输出结果如下：


```
name  age
0  Google   50
1  Runoob   40
```


---


## Pandas 清洗重复数据

如果我们要清洗重复数据，可以使用 **duplicated()** 和 **drop_duplicates()** 方法。


如果对应的数据是重复的，**duplicated()** 会返回 True，否则返回 False。


## 实例


```python
import pandas as pd

person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]
}
df = pd.DataFrame(person)

print(df.duplicated())
```


以上实例输出结果如下：


```
0    False
1    False
2     True
3    False
dtype: bool
```


删除重复数据，可以直接使用**drop_duplicates()** 方法。


## 实例


```python
import pandas as pd

persons = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]
}

df = pd.DataFrame(persons)

df.drop_duplicates(inplace = True)
print(df)
```


以上实例输出结果如下：


```
name  age
0  Google   50
1  Runoob   40
3  Taobao   23
```


## 常用方法及说明

数据清洗与预处理的常见方法：


| 操作 | 方法/步骤 | 说明 | 常用函数/方法 |
| --- | --- | --- | --- |
| 缺失值处理 | 填充缺失值 | 使用指定的值（如均值、中位数、众数等）填充缺失值。 | df.fillna(value) |
|  | 删除缺失值 | 删除包含缺失值的行或列。 | df.dropna() |
| 重复数据处理 | 删除重复数据 | 删除 DataFrame 中的重复行。 | df.drop_duplicates() |
| 异常值处理 | 异常值检测（基于统计方法） | 通过 Z-score 或 IQR 方法识别并处理异常值。 | 自定义函数（如基于 Z-score 或 IQR） |
|  | 替换异常值 | 使用合适的值（如均值或中位数）替换异常值。 | 自定义函数（如替换异常值） |
| 数据格式转换 | 转换数据类型 | 将数据类型从一个类型转换为另一个类型，如将字符串转换为日期。 | df.astype() |
|  | 日期时间格式转换 | 转换字符串或数字为日期时间类型。 | pd.to_datetime() |
| 标准化与归一化 | 标准化 | 将数据转换为均值为0，标准差为1的分布。 | StandardScaler() |
|  | 归一化 | 将数据缩放到指定的范围（如 [0, 1]）。 | MinMaxScaler() |
| 类别数据编码 | 标签编码 | 将类别变量转换为整数形式。 | LabelEncoder() |
|  | 独热编码（One-Hot Encoding） | 将每个类别转换为一个新的二进制特征。 | pd.get_dummies() |
| 文本数据处理 | 去除停用词 | 从文本中去除无关紧要的词，如 "the" 、 "is" 等。 | 自定义函数（基于 nltk 或 spaCy） |
|  | 词干化与词形还原 | 提取词干或恢复单词的基本形式。 | nltk.stem.PorterStemmer() |
|  | 分词 | 将文本分割成单词或子词。 | nltk.word_tokenize() |
| 数据抽样 | 随机抽样 | 从数据中随机抽取一定比例的样本。 | df.sample() |
|  | 上采样与下采样 | 通过过采样（复制少数类样本）或欠采样（减少多数类样本）来平衡数据集中的类别分布。 | SMOTE()（上采样）； RandomUnderSampler()（下采样） |
| 特征工程 | 特征选择 | 选择对目标变量有影响的特征，去除冗余或无关特征。 | SelectKBest() |
|  | 特征提取 | 从原始数据中创建新的特征，提升模型的预测能力。 | PolynomialFeatures() |
|  | 特征缩放 | 对数值特征进行缩放，使其具有相同的量级。 | MinMaxScaler() 、 StandardScaler() |
| 类别特征映射 | 特征映射 | 将类别变量映射为对应的数字编码。 | 自定义映射函数 |
| 数据合并与连接 | 合并数据 | 将多个 DataFrame 按照某些列合并在一起，支持内连接、外连接、左连接、右连接等。 | pd.merge() |
|  | 连接数据 | 将多个 DataFrame 进行行或列拼接。 | pd.concat() |
| 数据重塑 | 数据透视表 | 将数据根据某些维度进行分组并计算聚合结果。 | pd.pivot_table() |
|  | 数据变形 | 改变数据的形状，如从长格式转为宽格式或从宽格式转为长格式。 | df.melt() 、 df.pivot() |
| 数据类型转换与处理 | 字符串处理 | 对字符串数据进行处理，如去除空格、转换大小写等。 | str.replace() 、 str.upper() 等 |
|  | 分组计算 | 按照某个特征分组后进行聚合计算。 | df.groupby() |
| 缺失值预测填充 | 使用模型预测填充缺失值 | 使用机器学习模型（如回归模型）预测缺失值，并填充缺失数据。 | 自定义模型（如 sklearn.linear_model.LinearRegression） |
| 时间序列处理 | 时间序列缺失值填充 | 使用时间序列的方法（如前向填充、后向填充）填充缺失值。 | df.fillna(method='ffill') |
|  | 滚动窗口计算 | 使用滑动窗口进行时间序列数据的统计计算（如均值、标准差等）。 | df.rolling(window=5).mean() |
| 数据转换与映射 | 数据映射与替换 | 将数据中的某些值替换为其他值。 | df.replace() |


** 填充缺失值：**


## 实例


```python
import pandas as pd

# 示例数据
data = {'Name': ['Alice', 'Bob', 'Charlie', None],
        'Age': [25, 30, None, 35],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# 填充缺失的 "Age" 为均值
df['Age'].fillna(df['Age'].mean(), inplace=True)

print(df)
```


输出：


```
Name  Age           City
0    Alice   25.0       New York
1      Bob   30.0    Los Angeles
2  Charlie   30.0        Chicago
3     None   35.0        Houston
```


独热编码：


## 实例


```python
import pandas as pd

# 示例数据
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# 对 "City" 列进行 One-Hot 编码
df_encoded = pd.get_dummies(df, columns=['City'])

print(df_encoded)
```


输出：


```
City_Chicago  City_Houston  City_Los Angeles  City_New York
0             0             0                 0              1
1             0             0                 1              0
2             1             0                 0              0
3             0             1                 0              0
```


标准化：


## 实例


```python
from sklearn.preprocessing import StandardScaler
import pandas as pd

# 示例数据
data = {'Age': [25, 30, 35, 40, 45],
        'Salary': [50000, 60000, 70000, 80000, 90000]}

df = pd.DataFrame(data)

# 标准化数据
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

print(df_scaled)
```


输出：


```
[[-1.41421356 -1.41421356]
 [-0.70710678 -0.70710678]
 [ 0.          0.        ]
 [ 0.70710678  0.70710678]
 [ 1.41421356  1.41421356]]
```









	  AI 思考中...





			** [Pandas JSON](https://www.runoob.com/pandas-json.html)
			[Pandas 常用函数](https://www.runoob.com/pandas-functions.html) **













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