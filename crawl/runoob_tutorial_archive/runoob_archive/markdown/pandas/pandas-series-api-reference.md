# Pandas Series API 手册

- Source: https://www.runoob.com/pandas/pandas-series-api-reference.html

Series 是一种一维数组，能够存储任何数据类型（整数、字符串、浮点数、Python 对象等），并且每个元素都有一个标签，称为索引。


以下是 Pandas Series 的常用 API 手册：


### Series 构造函数


| 方法 | 描述 |
| --- | --- |
| pd.Series(data, index, dtype, name, copy) | 创建一个 Series 对象，支持自定义数据、索引、数据类型和名称。 |


---


### Series 属性


| 属性 | 描述 |
| --- | --- |
| Series.values | 返回 Series 的数据部分（numpy 数组）。 |
| Series.index | 返回 Series 的索引。 |
| Series.dtype | 返回 Series 的数据类型。 |
| Series.shape | 返回 Series 的形状（元组形式）。 |
| Series.size | 返回 Series 中元素的数量。 |
| Series.name | 返回或设置 Series 的名称。 |
| Series.empty | 检查 Series 是否为空。 |
| Series.nbytes | 返回 Series 占用的字节数。 |
| Series.ndim | 返回 Series 的维度数（始终为 1）。 |
| Series.hasnans | 检查 Series 是否包含缺失值（NaN）。 |
| Series.array | 返回 Series 的底层数据（Pandas 数组）。 |


---


### Series 方法


#### 数据查看


| 方法 | 描述 |
| --- | --- |
| Series.head(n=5) | 返回前 n 行数据。 |
| Series.tail(n=5) | 返回后 n 行数据。 |
| Series.describe() | 返回 Series 的统计摘要（如计数、均值、标准差等）。 |


#### 缺失值处理


| 方法 | 描述 |
| --- | --- |
| Series.isnull() | 检查每个元素是否为缺失值（NaN）。 |
| Series.notnull() | 检查每个元素是否不为缺失值。 |
| Series.dropna() | 删除所有缺失值。 |
| Series.fillna(value) | 用指定值填充缺失值。 |


#### 唯一值处理


| 方法 | 描述 |
| --- | --- |
| Series.unique() | 返回 Series 中的唯一值。 |
| Series.nunique() | 返回 Series 中唯一值的数量。 |
| Series.value_counts() | 返回 Series 中每个值的频率。 |


#### 排序


| 方法 | 描述 |
| --- | --- |
| Series.sort_values(ascending=True) | 按值排序。 |
| Series.sort_index(ascending=True) | 按索引排序。 |


#### 索引操作


| 方法 | 描述 |
| --- | --- |
| Series.reset_index(drop=False) | 重置索引。 |
| Series.drop(labels) | 删除指定索引的元素。 |
| Series.get(key, default=None) | 获取指定索引的值，如果不存在则返回默认值。 |
| Series.set_axis(labels) | 设置新的索引。 |


#### 数据转换


| 方法 | 描述 |
| --- | --- |
| Series.map(arg) | 根据传入的函数或字典映射 Series 中的值。 |
| Series.apply(func) | 对 Series 中的每个元素应用函数。 |
| Series.astype(dtype) | 将 Series 转换为指定数据类型。 |
| Series.to_dict() | 将 Series 转换为字典。 |
| Series.to_frame() | 将 Series 转换为 DataFrame。 |
| Series.to_numpy() | 将 Series 转换为 numpy 数组。 |


#### 数据操作


| 方法 | 描述 |
| --- | --- |
| Series.copy() | 复制 Series。 |
| Series.append(to_append, ignore_index) | 追加另一个 Series。 |
| Series.replace(to_replace, value) | 替换 Series 中的值。 |
| Series.update(other) | 用另一个 Series 的值更新当前 Series。 |
| Series.clip(lower, upper) | 将 Series 中的值限制在指定范围内。 |
| Series.isin(values) | 检查 Series 中的值是否在指定列表中。 |
| Series.between(left, right) | 检查 Series 中的值是否在指定范围内。 |


#### 统计计算


| 方法 | 描述 |
| --- | --- |
| Series.sum() | 返回 Series 中所有值的和。 |
| Series.mean() | 返回 Series 中所有值的平均值。 |
| Series.median() | 返回 Series 中所有值的中位数。 |
| Series.min() | 返回 Series 中的最小值。 |
| Series.max() | 返回 Series 中的最大值。 |
| Series.std() | 返回 Series 中所有值的标准差。 |
| Series.var() | 返回 Series 中所有值的方差。 |
| Series.count() | 返回 Series 中非缺失值的数量。 |
| Series.mode() | 返回 Series 中的众数。 |
| Series.quantile(q) | 返回 Series 中指定分位数的值。 |


#### 时间序列操作


| 方法 | 描述 |
| --- | --- |
| Series.dt | 访问日期时间属性（仅适用于 datetime 类型的 Series）。 |
| Series.dt.year | 返回年份。 |
| Series.dt.month | 返回月份。 |
| Series.dt.day | 返回日期。 |


#### 字符串操作


| 方法 | 描述 |
| --- | --- |
| Series.str | 访问字符串方法（仅适用于字符串类型的 Series）。 |
| Series.str.lower() | 将字符串转换为小写。 |
| Series.str.upper() | 将字符串转换为大写。 |
| Series.str.contains(pattern) | 检查字符串是否包含指定模式。 |


---


### 实例


## 实例


```python
import pandas as pd

# 创建 Series
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'], name='MySeries')

# 查看数据
print(s.head(2))  # 输出前 2 行

# 缺失值处理
s_with_nan = pd.Series([10, None, 30])
print(s_with_nan.fillna(0))  # 用 0 填充缺失值

# 唯一值处理
print(s.nunique())  # 输出唯一值的数量

# 排序
print(s.sort_values(ascending=False))  # 按值降序排序

# 统计计算
print(s.mean())  # 输出平均值
```


---


如果需要更详细的信息，可以参考 [Pandas 官方文档](https://pandas.pydata.org/docs/reference/series.html#)。









	  AI 思考中...





			** [Pandas 股票数据分析](https://www.runoob.com/pandas-stock.html)
			[Pandas DataFrame API 手册](https://www.runoob.com/pandas-dataframe-api-reference.html) **













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