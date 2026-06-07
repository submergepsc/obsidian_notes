# Pandas 数组/标量/数据类型参考手册

- Source: https://www.runoob.com/pandas/pandas-arrays-scalars-data-types-ref.html

对于大多数数据类型，Pandas 使用 NumPy 数组作为具体的存储对象，这些对象被包含在 Index（索引）、Series（序列）或 DataFrame（数据框）中。


对于某些数据类型，Pandas 扩展了 NumPy 的类型系统。这些类型的字符串别名可以在 dtypes 中找到。


### Pandas 数组


| 类/方法 | 描述 |
| --- | --- |
| pd.array(data, dtype) | 创建一个 Pandas 数组（ExtensionArray）。 |
| pd.Series.array | 返回 Series 的底层数组（ExtensionArray）。 |
| pd.arrays.IntegerArray | 用于存储整数数据的数组（支持缺失值）。 |
| pd.arrays.BooleanArray | 用于存储布尔数据的数组（支持缺失值）。 |
| pd.arrays.StringArray | 用于存储字符串数据的数组（支持缺失值）。 |
| pd.arrays.IntervalArray | 用于存储区间数据的数组。 |
| pd.arrays.DatetimeArray | 用于存储日期时间数据的数组。 |
| pd.arrays.TimedeltaArray | 用于存储时间差数据的数组。 |
| pd.arrays.PeriodArray | 用于存储周期数据的数组。 |
| pd.arrays.SparseArray | 用于存储稀疏数据的数组。 |


---


### Pandas 标量


| 类/方法 | 描述 |
| --- | --- |
| pd.NA | 表示缺失值的标量（类似于 NaN）。 |
| pd.Timestamp | 表示时间戳的标量。 |
| pd.Timedelta | 表示时间差的标量。 |
| pd.Period | 表示周期的标量。 |
| pd.Interval | 表示区间的标量。 |
| pd.Categorical | 表示分类数据的标量。 |


---


### Pandas 数据类型


| 类/方法 | 描述 |
| --- | --- |
| pd.StringDtype() | 字符串数据类型（支持缺失值）。 |
| pd.BooleanDtype() | 布尔数据类型（支持缺失值）。 |
| pd.Int8Dtype() | 8 位整数数据类型（支持缺失值）。 |
| pd.Int16Dtype() | 16 位整数数据类型（支持缺失值）。 |
| pd.Int32Dtype() | 32 位整数数据类型（支持缺失值）。 |
| pd.Int64Dtype() | 64 位整数数据类型（支持缺失值）。 |
| pd.Float32Dtype() | 32 位浮点数数据类型（支持缺失值）。 |
| pd.Float64Dtype() | 64 位浮点数数据类型（支持缺失值）。 |
| pd.CategoricalDtype() | 分类数据类型。 |
| pd.DatetimeTZDtype() | 带时区的日期时间数据类型。 |
| pd.PeriodDtype() | 周期数据类型。 |
| pd.IntervalDtype() | 区间数据类型。 |
| pd.SparseDtype() | 稀疏数据类型。 |


---


### 常用方法


#### 数组方法


| 方法 | 描述 |
| --- | --- |
| array.take(indices) | 根据索引从数组中提取元素。 |
| array.copy() | 复制数组。 |
| array.isna() | 检查数组中的缺失值。 |
| array.fillna(value) | 用指定值填充缺失值。 |
| array.unique() | 返回数组中的唯一值。 |
| array.value_counts() | 返回数组中每个值的频率。 |


#### 标量方法


| 方法 | 描述 |
| --- | --- |
| timestamp.to_pydatetime() | 将 Timestamp 转换为 Python 的 datetime 对象。 |
| timedelta.total_seconds() | 将 Timedelta 转换为总秒数。 |
| period.start_time | 返回 Period 的起始时间。 |
| period.end_time | 返回 Period 的结束时间。 |
| interval.left | 返回 Interval 的左边界。 |
| interval.right | 返回 Interval 的右边界。 |


#### 数据类型方法


| 方法 | 描述 |
| --- | --- |
| dtype.name | 返回数据类型的名称。 |
| dtype.kind | 返回数据类型的种类（如 i 表示整数，f 表示浮点数）。 |
| dtype.construct_array_type() | 返回与数据类型关联的数组类。 |


---


## 实例


```python
import pandas as pd

# 创建 Pandas 数组
arr = pd.array([1, 2, None], dtype=pd.Int64Dtype())
print(arr)

# 使用 Pandas 标量
ts = pd.Timestamp('2023-01-01')
print(ts.year)  # 输出年份

# 使用 Pandas 数据类型
dtype = pd.StringDtype()
print(dtype.name)  # 输出数据类型名称
```


---


如果需要更详细的信息，可以参考 [Pandas 官方文档](https://pandas.pydata.org/docs/reference/arrays.html)。









	  AI 思考中...





			** [Pandas 常用函数](https://www.runoob.com/pandas-general-functions.html)
			[Pandas Index 对象](https://www.runoob.com/pandas-index-object.html) **













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