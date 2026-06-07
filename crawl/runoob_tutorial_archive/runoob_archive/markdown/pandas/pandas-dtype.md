# Pandas 数据类型（dtype 与类型转换）

- Source: https://www.runoob.com/pandas/pandas-dtype.html

Pandas 提供了丰富的数据类型系统，正确理解和使用数据类型是高效数据分析的基础。本节详细介绍 Pandas 的数据类型体系、类型推断和类型转换方法。


---


## Pandas 数据类型概览


| dtype | 说明 | Python 类型 | 示例 |
| --- | --- | --- | --- |
| int64 | 64位整数 | int | 1, 2, 100 |
| float64 | 64位浮点数 | float | 1.5, 3.14 |
| object | 字符串或混合类型 | str | "hello" |
| bool | 布尔值 | bool | True, False |
| datetime64[ns] | 日期时间 | datetime | 2024-01-01 |
| timedelta64[ns] | 时间差 | timedelta | 1 days |
| category | 类别类型 | - | 有限集合 |


## 实例


```python
import pandas as pd
import numpy as np

# 创建各种数据类型的 DataFrame
df = pd.DataFrame({
    "整数": [1, 2, 3],
    "浮点数": [1.5, 2.5, 3.5],
    "字符串": ["a", "b", "c"],
    "布尔值": [True, False, True],
    "日期": pd.date_range("2024-01-01", periods=3)
})

print("各列数据类型：")
print(df.dtypes)
```


---


## 类型推断与指定


### 自动类型推断


## 实例


```python
import pandas as pd

# CSV 读取时的类型推断
# pandas 会尝试推断每列的最合适类型
df = pd.read_csv("data.csv")

# 或者使用 dtype 参数显式指定类型
df = pd.read_csv("data.csv", dtype={
    "年龄": "int32",     # 指定为32位整数，节省内存
    "薪资": "float32",   # 指定为32位浮点数
    "姓名": "string"     # 使用 PyArrow 字符串
})
```


### 创建时指定类型


## 实例


```python
import pandas as pd
import numpy as np

# 指定数据类型创建 Series
s = pd.Series([1, 2, 3], dtype="int8")  # 使用更小的整数类型
print(f"int8 类型：{s.dtype}")

s = pd.Series([1.5, 2.5, 3.5], dtype="float32")  # 使用 float32
print(f"float32 类型：{s.dtype}")

# 使用 numpy 类型
s = pd.Series([1, 2, 3], dtype=np.int8)
print(f"np.int8 类型：{s.dtype}")
```


---


## 类型转换


### 使用 astype 转换


## 实例


```python
import pandas as pd
import numpy as np

# 创建示例数据
df = pd.DataFrame({
    "整数": [1, 2, 3],
    "浮点数": [1.5, 2.5, 3.5],
    "字符串": ["1", "2", "3"],
    "布尔值": [1, 0, 1]
})

print("原始类型：")
print(df.dtypes)
print()

# 转换为字符串
df["整数_str"] = df["整数"].astype(str)
print("转为字符串后：")
print(df.dtypes)

# 字符串转数值
df["字符串_int"] = df["字符串"].astype(int)
print("\n字符串转整数：")
print(df.dtypes)

# 数值转布尔值（非0为True）
df["布尔_int"] = df["布尔值"].astype(bool)
print("\n整数转布尔：")
print(df.dtypes)

# 浮点数转整数（截断）
df["浮点_int"] = df["浮点数"].astype(int)
print("\n浮点转整数：")
print(df)
```


### 使用 pd.to_numeric 转换


## 实例


```python
import pandas as pd
import numpy as np

# 处理带特殊字符的数值字符串
s = pd.Series(["$1,000", "$2,500", "$3,200"])

# 清理并转换
s_cleaned = s.str.replace("$", "", regex=False).str.replace(",", "", regex=False)
s_numeric = pd.to_numeric(s_cleaned)
print("字符串转数值：")
print(s_numeric)
print(f"类型: {s_numeric.dtype}")
print()

# 处理缺失值
s_with_na = pd.Series(["1", "2", "NA", "4"])
s_numeric = pd.to_numeric(s_with_na, errors="coerce")  # 无效值转为 NaN
print("处理缺失值：")
print(s_numeric)
```


### 使用 pd.to_datetime 转换日期


## 实例


```python
import pandas as pd

# 各种日期格式转换
dates = ["2024-01-01", "2024/01/02", "01/03/2024", "20240104"]

# 转换日期
dt = pd.to_datetime(dates, errors="coerce")
print("日期转换结果：")
print(dt)
print(f"类型: {dt.dtype}")
print()

# 指定日期格式
dates2 = ["20240101", "20240102", "20240103"]
dt2 = pd.to_datetime(dates2, format="%Y%m%d")
print("指定格式转换：")
print(dt2)
```


---


## 内存优化


选择合适的数据类型可以显著减少内存占用。


### 整数类型选择


## 实例


```python
import pandas as pd
import numpy as np

# 创建大数据量的 Series
s = pd.Series(np.random.randint(0, 100, 1000000))

# 默认 int64
print(f"int64 内存: {s.dtype} -> {s.memory_usage(deep=True) / 1024 / 1024:.2f} MB")

# 转换为更小的类型
s_int8 = s.astype("int8")
print(f"int8 内存: {s_int8.dtype} -> {s_int8.memory_usage(deep=True) / 1024 / 1024:.2f} MB")

# 根据数据范围选择合适类型
# np.iinfo 查看整数范围
print(f"\nint8 范围: {np.iinfo('int8').min} 到 {np.iinfo('int8').max}")
print(f"int16 范围: {np.iinfo('int16').min} 到 {np.iinfo('int16').max}")
print(f"int32 范围: {np.iinfo('int32').min} 到 {np.iinfo('int32').max}")
```


### 使用 category 类型


## 实例


```python
import pandas as pd
import numpy as np

# 创建有大量重复值的 Series
s = pd.Series(np.random.choice(["北京", "上海", "广州", "深圳"], 1000000))

# 字符串类型
print(f"object 类型内存: {s.dtype} -> {s.memory_usage(deep=True) / 1024 / 1024:.2f} MB")

# 转换为 category 类型
s_cat = s.astype("category")
print(f"category 类型内存: {s_cat.dtype} -> {s_cat.memory_usage(deep=True) / 1024 / 1024:.2f} MB")

# 缺点：某些操作会变慢
print("\ncategory 信息：")
print(s_cat.cat.categories)
```


---


## 类型检查与判断


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "整数": [1, 2, 3],
    "浮点": [1.5, 2.5, 3.5],
    "字符串": ["a", "b", "c"]
})

# 检查数据类型
print("检查是否为数值类型：")
print(df.dtypes)

# 使用 is_integer_dtype
print(f"\n整数列: {pd.api.types.is_integer_dtype(df['整数'])}")
print(f"浮点列: {pd.api.types.is_float_dtype(df['浮点'])}")
print(f"字符串列: {pd.api.types.is_object_dtype(df['字符串'])}")

# 检查是否可以转换为数值
print(f"\n是否可转为数值: {pd.api.types.is_numeric_dtype(df['整数'])}")
print(f"是否为日期时间: {pd.api.types.is_datetime64_any_dtype(pd.Series(pd.date_range('2024', periods=3)))}")
```


---


## 常见问题


**1、整数列出现浮点数**


DataFrame 中混入会自动转为 float64，使用 `Nullable Integer` 类型可以保留整数空值。


**2、日期格式不统一**


使用 `pd.to_datetime` 并指定 `format` 参数处理非标准格式。


**3、读取 CSV 时类型错误**


使用 `dtype` 参数显式指定类型，或使用 `converters` 进行转换。


**
大数据集优先考虑使用更小的数据类型（如 int8、int16、float32）和 category 类型来减少内存占用。









	  AI 思考中...





			** [Pandas 多层索引（MultiIndex）](https://www.runoob.com/pandas-multiindex.html)
			[Pandas 类别类型（Categorical）](https://www.runoob.com/pandas-categorical.html) **













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