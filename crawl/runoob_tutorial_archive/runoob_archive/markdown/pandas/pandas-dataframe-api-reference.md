# Pandas DataFrame API 手册

- Source: https://www.runoob.com/pandas/pandas-dataframe-api-reference.html

DataFrame 是一个二维标签化数据结构，你可以将其想象为一个 Excel 电子表格或者 SQL 表，或者是一个字典类型的集合。


以下是 Pandas DataFrame 的常用 API 手册：


### DataFrame 构造函数


| 方法 | 描述 |
| --- | --- |
| pd.DataFrame(data, index, columns, dtype, copy) | 创建一个 DataFrame 对象，支持自定义数据、索引、列名和数据类型。 |


---


### DataFrame 属性


| 属性 | 描述 |
| --- | --- |
| DataFrame.values | 返回 DataFrame 的数据部分（numpy 数组）。 |
| DataFrame.index | 返回 DataFrame 的行索引。 |
| DataFrame.columns | 返回 DataFrame 的列名。 |
| DataFrame.dtypes | 返回每列的数据类型。 |
| DataFrame.shape | 返回 DataFrame 的形状（元组形式）。 |
| DataFrame.size | 返回 DataFrame 中元素的总数。 |
| DataFrame.empty | 检查 DataFrame 是否为空。 |
| DataFrame.ndim | 返回 DataFrame 的维度数（始终为 2）。 |
| DataFrame.T | 返回 DataFrame 的转置。 |
| DataFrame.axes | 返回行索引和列名的列表。 |
| DataFrame.memory_usage() | 返回每列的内存使用情况。 |


---


### DataFrame 方法


#### 数据查看


| 方法 | 描述 |
| --- | --- |
| DataFrame.head(n=5) | 返回前 n 行数据。 |
| DataFrame.tail(n=5) | 返回后 n 行数据。 |
| DataFrame.describe() | 返回 DataFrame 的统计摘要（如计数、均值、标准差等）。 |
| DataFrame.info() | 打印 DataFrame 的简要信息（如列名、数据类型、非空值数量等）。 |


#### 缺失值处理


| 方法 | 描述 |
| --- | --- |
| DataFrame.isnull() | 检查每个元素是否为缺失值（NaN）。 |
| DataFrame.notnull() | 检查每个元素是否不为缺失值。 |
| DataFrame.dropna() | 删除包含缺失值的行或列。 |
| DataFrame.fillna(value) | 用指定值填充缺失值。 |


#### 数据操作


| 方法 | 描述 |
| --- | --- |
| DataFrame.drop() | 删除指定的行或列。 |
| DataFrame.rename() | 重命名行索引或列名。 |
| DataFrame.set_index() | 将指定列设置为索引。 |
| DataFrame.reset_index() | 重置索引。 |
| DataFrame.sort_values() | 按值排序。 |
| DataFrame.sort_index() | 按索引排序。 |
| DataFrame.replace() | 替换 DataFrame 中的值。 |
| DataFrame.append() | 追加另一个 DataFrame。 |
| DataFrame.join() | 根据索引或列连接另一个 DataFrame。 |
| DataFrame.merge() | 根据指定列合并另一个 DataFrame。 |
| DataFrame.concat() | 沿指定轴连接多个 DataFrame。 |
| DataFrame.update() | 用另一个 DataFrame 的值更新当前 DataFrame。 |
| DataFrame.pivot() | 创建透视表。 |
| DataFrame.melt() | 将宽格式数据转换为长格式数据。 |


#### 数据选择


| 方法 | 描述 |
| --- | --- |
| DataFrame.loc[] | 通过标签选择数据。 |
| DataFrame.iloc[] | 通过位置选择数据。 |
| DataFrame.at[] | 通过标签选择单个值。 |
| DataFrame.iat[] | 通过位置选择单个值。 |
| DataFrame.filter() | 根据列名选择数据。 |
| DataFrame.get() | 获取指定列的值。 |
| DataFrame.query() | 根据条件查询数据。 |


#### 数据转换


| 方法 | 描述 |
| --- | --- |
| DataFrame.astype() | 将 DataFrame 转换为指定数据类型。 |
| DataFrame.apply() | 对 DataFrame 的行或列应用函数。 |
| DataFrame.applymap() | 对 DataFrame 的每个元素应用函数。 |
| DataFrame.map() | 对 Series 中的每个元素应用函数。 |
| DataFrame.to_dict() | 将 DataFrame 转换为字典。 |
| DataFrame.to_numpy() | 将 DataFrame 转换为 numpy 数组。 |
| DataFrame.to_csv() | 将 DataFrame 保存为 CSV 文件。 |
| DataFrame.to_excel() | 将 DataFrame 保存为 Excel 文件。 |


#### 统计计算


| 方法 | 描述 |
| --- | --- |
| DataFrame.sum() | 返回每列的和。 |
| DataFrame.mean() | 返回每列的平均值。 |
| DataFrame.median() | 返回每列的中位数。 |
| DataFrame.min() | 返回每列的最小值。 |
| DataFrame.max() | 返回每列的最大值。 |
| DataFrame.std() | 返回每列的标准差。 |
| DataFrame.var() | 返回每列的方差。 |
| DataFrame.count() | 返回每列的非缺失值数量。 |
| DataFrame.corr() | 返回列之间的相关系数矩阵。 |
| DataFrame.cov() | 返回列之间的协方差矩阵。 |
| DataFrame.mode() | 返回每列的众数。 |
| DataFrame.quantile() | 返回每列的分位数。 |


#### 时间序列操作


| 方法 | 描述 |
| --- | --- |
| DataFrame.dt | 访问日期时间属性（仅适用于 datetime 类型的列）。 |
| DataFrame.resample() | 对时间序列数据进行重采样。 |
| DataFrame.shift() | 将数据按时间轴移动。 |


#### 字符串操作


| 方法 | 描述 |
| --- | --- |
| DataFrame.str | 访问字符串方法（仅适用于字符串类型的列）。 |
| DataFrame.str.lower() | 将字符串转换为小写。 |
| DataFrame.str.upper() | 将字符串转换为大写。 |
| DataFrame.str.contains() | 检查字符串是否包含指定模式。 |


---


### 实例


## 实例


```python
import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['a', 'b', 'c'])

# 查看数据
print(df.head(2))  # 输出前 2 行

# 缺失值处理
df_with_nan = pd.DataFrame({
    'A': [1, None, 3],
    'B': [4, 5, None]
})
print(df_with_nan.fillna(0))  # 用 0 填充缺失值

# 统计计算
print(df.mean())  # 输出每列的平均值
```


---


如果需要更详细的信息，可以参考 [Pandas 官方文档](https://pandas.pydata.org/docs/reference/frame.html)。









	  AI 思考中...





			** [Pandas Series API 手册](https://www.runoob.com/pandas-series-api-reference.html)
			[Pandas Input/Output (输入输出) API 手册](https://www.runoob.com/pandas-io-api-reference.html) **













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