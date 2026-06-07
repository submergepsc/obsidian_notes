# Pandas CSV 文件

- Source: https://www.runoob.com/pandas/pandas-csv-file.html

CSV（Comma-Separated Values，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。

CSV 是一种通用的、相对简单的文件格式，被用户、商业和科学广泛应用。


Pandas 可以很方便的处理 CSV 文件，常用方法有：


| 方法名称 | 功能描述 | 常用参数 |
| --- | --- | --- |
| pd.read_csv() | 从 CSV 文件读取数据并加载为 DataFrame | filepath_or_buffer (路径或文件对象)，sep (分隔符)，header (行标题)，names (自定义列名)，dtype (数据类型)，index_col (索引列) |
| DataFrame.to_csv() | 将 DataFrame 写入到 CSV 文件 | path_or_buffer (目标路径或文件对象)，sep (分隔符)，index (是否写入索引)，columns (指定列)，header (是否写入列名)，mode (写入模式) |


本文以 [nba.csv](https://static.jyshare.com/download/nba.csv) 为例，你可以[下载 nba.csv](https://static.jyshare.com/download/nba.csv) 或[打开 nba.csv](https://static.jyshare.com/download/nba.csv.txt) 查看。


### pd.read_csv() - 读取 CSV 文件

read_csv() 是从 CSV 文件中读取数据的主要方法，将数据加载为一个 DataFrame。


```
import pandas as pd

# 读取 CSV 文件，并自定义列名和分隔符
df = pd.read_csv('data.csv', sep=';', header=0, names=['A', 'B', 'C'], dtype={'A': int, 'B': float})
print(df)
```


read_csv 常用参数:


| 参数 | 说明 | 默认值 |
| --- | --- | --- |
| filepath_or_buffer | CSV 文件的路径或文件对象（支持 URL、文件路径、文件对象等） | 必需参数 |
| sep | 定义字段分隔符，默认是逗号（,），可以改为其他字符，如制表符（\t） | ',' |
| header | 指定行号作为列标题，默认为 0（表示第一行），或者设置为 None 没有标题 | 0 |
| names | 自定义列名，传入列名列表 | None |
| index_col | 用作行索引的列的列号或列名 | None |
| usecols | 读取指定的列，可以是列的名称或列的索引 | None |
| dtype | 强制将列转换为指定的数据类型 | None |
| skiprows | 跳过文件开头的指定行数，或者传入一个行号的列表 | None |
| nrows | 读取前 N 行数据 | None |
| na_values | 指定哪些值应视为缺失值（NaN） | None |
| skipfooter | 跳过文件结尾的指定行数 | 0 |
| encoding | 文件的编码格式（如 utf-8，latin1 等） | None |


读取 nba.csv 文件数据：


## 实例


```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.to_string())
```


**to_string()** 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 **...** 代替。


## 实例


```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df)
```


输出结果为：


```
Name            Team  Number Position   Age Height  Weight            College     Salary
0    Avery Bradley  Boston Celtics     0.0       PG  25.0    6-2   180.0              Texas  7730337.0
1      Jae Crowder  Boston Celtics    99.0       SF  25.0    6-6   235.0          Marquette  6796117.0
2     John Holland  Boston Celtics    30.0       SG  27.0    6-5   205.0  Boston University        NaN
3      R.J. Hunter  Boston Celtics    28.0       SG  22.0    6-5   185.0      Georgia State  1148640.0
4    Jonas Jerebko  Boston Celtics     8.0       PF  29.0   6-10   231.0                NaN  5000000.0
..             ...             ...     ...      ...   ...    ...     ...                ...        ...
453   Shelvin Mack       Utah Jazz     8.0       PG  26.0    6-3   203.0             Butler  2433333.0
454      Raul Neto       Utah Jazz    25.0       PG  24.0    6-1   179.0                NaN   900000.0
455   Tibor Pleiss       Utah Jazz    21.0        C  26.0    7-3   256.0                NaN  2900000.0
456    Jeff Withey       Utah Jazz    24.0        C  26.0    7-0   231.0             Kansas   947276.0
457            NaN             NaN     NaN      NaN   NaN    NaN     NaN                NaN        NaN
```


### df.to_csv() - 将 DataFrame 写入 CSV 文件

to_csv() 是将 DataFrame 写入 CSV 文件的方法，支持自定义分隔符、列名、是否包含索引等设置。


```
import pandas as pd

# 假设 df 是一个已有的 DataFrame
df.to_csv('output.csv', index=False, header=True, columns=['A', 'B'])
```


to_csv 常用参数:


| 参数 | 说明 | 默认值 |
| --- | --- | --- |
| path_or_buffer | CSV 文件的路径或文件对象（支持文件路径、文件对象） | 必需参数 |
| sep | 定义字段分隔符，默认是逗号（,），可以改为其他字符，如制表符（\t） | ',' |
| index | 是否写入行索引，默认 True 表示写入索引 | True |
| columns | 指定写入的列，可以是列的名称列表 | None |
| header | 是否写入列名，默认 True 表示写入列名，设置为 False 表示不写列名 | True |
| mode | 写入文件的模式，默认是 w（写模式），可以设置为 a（追加模式） | 'w' |
| encoding | 文件的编码格式，如 utf-8，latin1 等 | None |
| line_terminator | 定义行结束符，默认为 \n | None |
| quoting | 设置如何对文件中的数据进行引号处理（0-3，具体引用方式可查文档） | None |
| quotechar | 设置用于引用的字符，默认为双引号 " | '"' |
| date_format | 自定义日期格式，如果列包含日期数据，则可以使用此参数指定日期格式 | None |
| doublequote | 如果为 True，则在写入时会将包含引号的文本使用双引号括起来 | True |


我们也可以使用 **to_csv()** 方法将 DataFrame 存储为 csv 文件：


## 实例


```python
import pandas as pd

# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]

# 字典
dict = {'name': nme, 'site': st, 'age': ag}

df = pd.DataFrame(dict)

# 保存 dataframe
df.to_csv('site.csv')
```


执行成功后，我们打开 site.csv 文件，显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/05/9758194A-0D8E-4C53-95A0-157C690614E6.jpg)


---

## 数据处理


### head()


**head( *n* )** 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行。


## 实例 - 读取前面 5 行


```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.head())
```


输出结果为：


```
Name            Team  Number Position   Age Height  Weight            College     Salary
0  Avery Bradley  Boston Celtics     0.0       PG  25.0    6-2   180.0              Texas  7730337.0
1    Jae Crowder  Boston Celtics    99.0       SF  25.0    6-6   235.0          Marquette  6796117.0
2   John Holland  Boston Celtics    30.0       SG  27.0    6-5   205.0  Boston University        NaN
3    R.J. Hunter  Boston Celtics    28.0       SG  22.0    6-5   185.0      Georgia State  1148640.0
4  Jonas Jerebko  Boston Celtics     8.0       PF  29.0   6-10   231.0                NaN  5000000.0
```


## 实例 - 读取前面 10 行


```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.head(10))
```


输出结果为：


```
Name            Team  Number Position   Age Height  Weight            College      Salary
0  Avery Bradley  Boston Celtics     0.0       PG  25.0    6-2   180.0              Texas   7730337.0
1    Jae Crowder  Boston Celtics    99.0       SF  25.0    6-6   235.0          Marquette   6796117.0
2   John Holland  Boston Celtics    30.0       SG  27.0    6-5   205.0  Boston University         NaN
3    R.J. Hunter  Boston Celtics    28.0       SG  22.0    6-5   185.0      Georgia State   1148640.0
4  Jonas Jerebko  Boston Celtics     8.0       PF  29.0   6-10   231.0                NaN   5000000.0
5   Amir Johnson  Boston Celtics    90.0       PF  29.0    6-9   240.0                NaN  12000000.0
6  Jordan Mickey  Boston Celtics    55.0       PF  21.0    6-8   235.0                LSU   1170960.0
7   Kelly Olynyk  Boston Celtics    41.0        C  25.0    7-0   238.0            Gonzaga   2165160.0
8   Terry Rozier  Boston Celtics    12.0       PG  22.0    6-2   190.0         Louisville   1824360.0
9   Marcus Smart  Boston Celtics    36.0       PG  22.0    6-4   220.0     Oklahoma State   3431040.0
```


### tail()


** tail( *n* )** 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 **NaN**。


## 实例 - 读取末尾 5 行


```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.tail())
```


输出结果为：


```
Name       Team  Number Position   Age Height  Weight College     Salary
453  Shelvin Mack  Utah Jazz     8.0       PG  26.0    6-3   203.0  Butler  2433333.0
454     Raul Neto  Utah Jazz    25.0       PG  24.0    6-1   179.0     NaN   900000.0
455  Tibor Pleiss  Utah Jazz    21.0        C  26.0    7-3   256.0     NaN  2900000.0
456   Jeff Withey  Utah Jazz    24.0        C  26.0    7-0   231.0  Kansas   947276.0
457           NaN        NaN     NaN      NaN   NaN    NaN     NaN     NaN        NaN
```


## 实例 - 读取末尾 10 行


```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.tail(10))
```


输出结果为：


```
Name       Team  Number Position   Age Height  Weight   College      Salary
448  Gordon Hayward  Utah Jazz    20.0       SF  26.0    6-8   226.0    Butler  15409570.0
449     Rodney Hood  Utah Jazz     5.0       SG  23.0    6-8   206.0      Duke   1348440.0
450      Joe Ingles  Utah Jazz     2.0       SF  28.0    6-8   226.0       NaN   2050000.0
451   Chris Johnson  Utah Jazz    23.0       SF  26.0    6-6   206.0    Dayton    981348.0
452      Trey Lyles  Utah Jazz    41.0       PF  20.0   6-10   234.0  Kentucky   2239800.0
453    Shelvin Mack  Utah Jazz     8.0       PG  26.0    6-3   203.0    Butler   2433333.0
454       Raul Neto  Utah Jazz    25.0       PG  24.0    6-1   179.0       NaN    900000.0
455    Tibor Pleiss  Utah Jazz    21.0        C  26.0    7-3   256.0       NaN   2900000.0
456     Jeff Withey  Utah Jazz    24.0        C  26.0    7-0   231.0    Kansas    947276.0
457             NaN        NaN     NaN      NaN   NaN    NaN     NaN       NaN         NaN
```


### info()


info() 方法返回表格的一些基本信息：


## 实例


```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.info())
```


输出结果为：


```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 458 entries, 0 to 457          # 行数，458 行，第一行编号为 0
Data columns (total 9 columns):            # 列数，9列
 #   Column    Non-Null Count  Dtype       # 各列的数据类型
---  ------    --------------  -----
 0   Name      457 non-null    object
 1   Team      457 non-null    object
 2   Number    457 non-null    float64
 3   Position  457 non-null    object
 4   Age       457 non-null    float64
 5   Height    457 non-null    object
 6   Weight    457 non-null    float64
 7   College   373 non-null    object         # non-null，意思为非空的数据
 8   Salary    446 non-null    float64
dtypes: float64(4), object(5)                 # 类型
```


non-null 为非空数据，我们可以看到上面的信息中，总共 458 行，College 字段的空值最多。








	  AI 思考中...





			** [Pandas 数据结构 – DataFrame](https://www.runoob.com/pandas-dataframe.html)
			[Pandas JSON](https://www.runoob.com/pandas-json.html) **













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