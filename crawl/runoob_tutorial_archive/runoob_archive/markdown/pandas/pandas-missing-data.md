# Pandas 缺失值处理

- Source: https://www.runoob.com/pandas/pandas-missing-data.html

真实数据中往往存在缺失值（NaN），Pandas 提供了丰富的函数来处理缺失数据。本节详细介绍 fillna、dropna、interpolate 等方法的使用。


---


## 缺失值的表示


Pandas 中使用 `NaN`（Not a Number）表示缺失值，它来源于 NumPy 库。


## 实例


```python
import pandas as pd
import numpy as np

# 创建包含缺失值的数据
s = pd.Series([1, 2, np.nan, 4, 5])
print("包含 NaN 的 Series：")
print(s)
print(f"是否有缺失值: {s.isna().any()}")
print()

# DataFrame 中的缺失值
df = pd.DataFrame({
    "A": [1, 2, np.nan, 4],
    "B": [np.nan, 2, 3, 4],
    "C": [1, 2, 3, np.nan]
})

print("包含缺失值的 DataFrame：")
print(df)
print()

# 检测缺失值
print("缺失值位置：")
print(df.isna())
print()

# 统计每列缺失值数量
print("每列缺失值数量：")
print(df.isna().sum())
```


**
在 Pandas 中，`NaN`、`None`、`pandas.NA` 都会被识别为缺失值。使用 `isna()` 或 `isnull()` 可以统一检测这些缺失值。


---


## dropna 删除缺失值


### 删除行


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 2, np.nan, 4],
    "B": [1, np.nan, 3, 4],
    "C": [1, 2, 3, np.nan]
})

print("原始数据：")
print(df)
print()

# 删除包含缺失值的行（默认）
print("删除有缺失值的行：")
print(df.dropna())
print()

# how='all'：只有全部为缺失值才删除
print("只有全部为缺失值的行才删除：")
print(df.dropna(how="all"))
print()

# thresh：至少有 N 个非缺失值才保留
print("至少2个非缺失值才保留：")
print(df.dropna(thresh=2))
```


### 删除列


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 2, np.nan, 4],
    "B": [np.nan, np.nan, np.nan, np.nan],  # 全部缺失
    "C": [1, 2, 3, 4]
})

print("原始数据：")
print(df)
print()

# 删除包含缺失值的列
print("删除有缺失值的列：")
print(df.dropna(axis=1))
print()

# how='all'：删除全部为缺失值的列
print("删除全部为缺失值的列：")
print(df.dropna(axis=1, how="all"))
```


---


## fillna 填充缺失值


### 固定值填充


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 2, np.nan, 4, 5],
    "B": [np.nan, 2, 3, np.nan, 5],
    "C": [1, 2, 3, 4, np.nan]
})

print("原始数据：")
print(df)
print()

# 用 0 填充
print("用0填充：")
print(df.fillna(0))
print()

# 用指定值填充不同列
print("不同列用不同值填充：")
print(df.fillna({"A": 0, "B": 99, "C": -1}))
print()

# 用前一个值填充（前向填充）
print("前向填充：")
print(df.fillna(method="ffill"))
print()

# 用后一个值填充（后向填充）
print("后向填充：")
print(df.fillna(method="bfill"))
```


### 统计值填充


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 2, np.nan, 4, 5, 6],
    "B": [10, np.nan, 30, np.nan, 50, 60]
})

print("原始数据：")
print(df)
print()

# 用均值填充
print("用均值填充：")
print(df.fillna(df.mean()))
print()

# 用中位数填充
print("用中位数填充：")
print(df.fillna(df.median()))
print()

# 按列分别填充
print("A列用均值，B列用0：")
print(df.fillna({"A": df["A"].mean(), "B": 0}))
```


> 前向填充和后向填充在时间序列数据中特别有用，可以保持数据的连续性。选择哪种方式取决于数据的业务含义。


---


## interpolate 插值填充


插值是一种更智能的填充方式，可以根据相邻数据推算缺失值。


### 线性插值


## 实例


```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, np.nan, 4, 5, np.nan, 7])

print("原始 Series：")
print(s)
print()

# 线性插值（默认）
print("线性插值：")
print(s.interpolate())
print()

# 指定插值方法
print("time 加权插值（时间序列）：")
s2 = pd.Series([1, np.nan, np.nan, 4], index=pd.date_range("2024-01-01", periods=4, freq="D"))
print(s2.interpolate(method="time"))
print()

# 邻近值填充
print("用邻近值填充：")
print(s.interpolate(method="nearest"))
```


### DataFrame 插值


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 2, np.nan, 4, 5],
    "B": [10, np.nan, 30, 40, np.nan]
})

print("原始数据：")
print(df)
print()

# 在原 DataFrame 上插值
df_interpolated = df.interpolate(method="linear")
print("线性插值后：")
print(df_interpolated)
print()

# 限制插值范围
print("只填充连续缺失值的首尾（最多1个）：")
print(df.interpolate(limit=1))
```


---


## 实战：处理真实数据


## 实例


```python
import pandas as pd
import numpy as np

# 模拟真实的业务数据
np.random.seed(42)
n = 20

df = pd.DataFrame({
    "日期": pd.date_range("2024-01-01", periods=n),
    "销售额": np.random.choice([100, 200, np.nan, 300, np.nan], n),
    "客户数": np.random.choice([10, np.nan, 20, 30], n),
    "转化率": np.random.choice([0.05, 0.1, np.nan, 0.15], n)
})

print("原始数据缺失情况：")
print(df.isna().sum())
print()

# 处理策略：
# 1. 销售额用前后均值填充（业务允许波动）
df["销售额"] = df["销售额"].interpolate()

# 2. 客户数用均值填充
df["客户数"] = df["客户数"].fillna(df["客户数"].mean())

# 3. 转化率用0填充（表示未转化）
df["转化率"] = df["转化率"].fillna(0)

print("处理后数据：")
print(df)
print()

print("处理后缺失情况：")
print(df.isna().sum())
```


---


## 常见问题


1、fillna 会创建新对象还是原地修改**


`fillna` 默认返回新对象，使用 `inplace=True` 可以原地修改。


**2、插值后仍有缺失值


如果缺失值在序列开头或结尾，插值无法填充，需要额外处理。


3、区分 NaN 和空字符串**


空字符串 `""` 不是缺失值，需要用 `replace("", np.nan)` 转换。


**
选择填充方式时要考虑业务含义：前向填充适合时间序列，后向填充适合静态数据，均值适合数值型数据，插值适合连续数据。









	  AI 思考中...





			** [Pandas 过滤与条件查询](https://www.runoob.com/pandas-filter.html)
			[Pandas 重复数据处理](https://www.runoob.com/pandas-duplicate.html) **













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