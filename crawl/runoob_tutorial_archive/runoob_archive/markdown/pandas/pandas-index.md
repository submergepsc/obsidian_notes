# Pandas Index（索引）

- Source: https://www.runoob.com/pandas/pandas-index.html

Index（索引）是 Pandas 数据结构的核心组成部分，它决定了数据的组织和访问方式。Pandas 支持多种类型的索引，从简单的 RangeIndex 到复杂的多层索引（MultiIndex），本节将详细介绍各种索引类型的使用方法。


---


## Index 的基本概念


Index 类似于数据库的主键或 Excel 的行号，用于唯一标识每行数据。DataFrame 有行索引（index）和列索引（columns）两部分。


## 实例


```python
import pandas as pd

# 创建简单的 DataFrame（默认使用 RangeIndex）
df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 28],
    "城市": ["北京", "上海", "广州"]
})

print("DataFrame 信息：")
print(f"行索引: {df.index.tolist()}")
print(f"列索引: {df.columns.tolist()}")
print("\n数据：")
print(df)
```


---


## RangeIndex


RangeIndex 是默认的整数索引，类似 Python 的 `range(n)`，从 0 开始递增。


### 创建与使用


## 实例


```python
import pandas as pd

# 创建 RangeIndex
idx = pd.RangeIndex(start=0, stop=10, step=1)
print(f"RangeIndex: {idx}")
print(f"类型: {type(idx)}")

# DataFrame 默认使用 RangeIndex
df = pd.DataFrame({"A": [1, 2, 3]}, index=range(3))
print(f"\n默认索引类型: {type(df.index)}")

# 重置索引后也返回 RangeIndex
df_reset = df.reset_index()
print(f"重置后索引类型: {type(df_reset.index)}")
```


### RangeIndex 特点


- 内存占用最小
- 支持默认的整数位置访问
- 与其他索引类型转换简单


---


## Index 类型转换


Index 支持在多种类型之间转换。


### 转换为其他索引类型


## 实例


```python
import pandas as pd

# 创建示例 DataFrame
df = pd.DataFrame({"值": [1, 2, 3, 4]}, index=[10, 20, 30, 40])

# 转换为 Index 类型
print("原始索引:", df.index)
print("索引类型:", type(df.index))

# 转换为列表
idx_list = df.index.tolist()
print(f"转换为列表: {idx_list}")

# 转换为 NumPy 数组
idx_array = df.index.values
print(f"转换为数组: {idx_array}")

# 重新设置索引为 RangeIndex
df = df.reset_index(drop=True)
print(f"重置为 RangeIndex: {df.index}")
```


---


## 设置自定义索引


可以用 DataFrame 的列来设置行索引。


### 使用 set_index


## 实例


```python
import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    "学号": ["S001", "S002", "S003", "S004"],
    "姓名": ["张三", "李四", "王五", "赵六"],
    "分数": [85, 92, 78, 90]
})

print("原始数据：")
print(df)
print()

# 将"学号"列设置为索引
df1 = df.set_index("学号")
print("设置学号为索引：")
print(df1)
print()

# 设置多个索引（会创建 MultiIndex）
df2 = df.set_index(["学号", "姓名"])
print("设置多个索引：")
print(df2)
```


### 使用 index 参数创建


## 实例


```python
import pandas as pd

# 在创建 DataFrame 时直接指定索引
df = pd.DataFrame(
    {"姓名": ["张三", "李四", "王五"], "年龄": [25, 30, 28]},
    index=["A001", "A002", "A003"]
)

print(df)
print(f"\n索引: {df.index.tolist()}")

# 使用 DatetimeIndex
dates = pd.date_range("2024-01-01", periods=3, freq="D")
df_date = pd.DataFrame({"值": [100, 200, 300]}, index=dates)

print("\n使用日期索引：")
print(df_date)
print(f"索引类型: {type(df_date.index)}")
```


---


## 索引操作


### 重置索引


## 实例


```python
import pandas as pd

# 创建带自定义索引的 DataFrame
df = pd.DataFrame(
    {"姓名": ["张三", "李四"], "分数": [85, 92]},
    index=["A001", "A002"]
)

# 重置索引为默认的 RangeIndex
df_reset = df.reset_index()
print("重置索引：")
print(df_reset)

# drop 参数：是否丢弃原索引列
df_reset2 = df.reset_index(drop=True)
print("\n重置并丢弃原索引：")
print(df_reset2)
```


### 重新索引


## 实例


```python
import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}, index=[1, 2, 3])

# 重新索引（改变索引顺序）
df_reindex = df.reindex([1, 2, 3, 4, 5])
print("重新索引（填充缺失为 NaN）：")
print(df_reindex)

# 使用 fill_value 填充缺失值
df_reindex2 = df.reindex([1, 2, 3, 4, 5], fill_value=0)
print("\n重新索引（用0填充）：")
print(df_reindex2)
```


### 索引层级操作


## 实例


```python
import pandas as pd

# 创建多层索引 DataFrame
df = pd.DataFrame({
    "语文": [85, 92, 78],
    "数学": [90, 88, 95]
}, index=pd.MultiIndex.from_tuples(
    [("高一", "A班"), ("高一", "B班"), ("高二", "A班")],
    names=["年级", "班级"]
))

print("多层索引 DataFrame：")
print(df)
print()

# 获取外层索引
print(f"外层索引（年级）: {df.index.get_level_values(0).tolist()}")
print(f"内层索引（班级）: {df.index.get_level_values(1).tolist()}")
```


---


## 索引的属性与方法


| 属性/方法 | 说明 | 示例 |
| --- | --- | --- |
| index.tolist() | 转换为 Python 列表 | df.index.tolist() |
| index.values | 转换为 NumPy 数组 | df.index.values |
| index.unique() | 获取唯一值 | df.index.unique() |
| index.is_unique | 检查索引是否唯一 | df.index.is_unique |
| index.astype() | 转换索引类型 | df.index.astype(str) |


### 索引属性使用示例


## 实例


```python
import pandas as pd

# 创建示例 DataFrame
df = pd.DataFrame(
    {"值": [1, 2, 3, 4]},
    index=["a", "b", "c", "d"]
)

# 查看索引属性
print(f"索引是否唯一: {df.index.is_unique}")
print(f"索引长度: {len(df.index)}")
print(f"索引数据类型: {df.index.dtype}")

# 转换为字符串类型
str_index = df.index.astype(str)
print(f"转换后类型: {str_index.dtype}")
```


---


## 实战：使用索引提升查询效率


在实际数据分析中，合理设置索引可以显著提升查询效率。


## 实例


```python
import pandas as pd

# 模拟业务数据
df = pd.DataFrame({
    "订单ID": range(1000),
    "客户ID": [f"C{i%100:03d}" for i in range(1000)],
    "产品": [f"产品{i%20}" for i in range(1000)],
    "金额": [round(i * 1.5, 2) for i in range(1000)]
})

# 设置常用查询列为索引
df_indexed = df.set_index(["客户ID", "产品"])

# 使用索引快速查询（类似数据库主键查询）
result = df_indexed.loc[("C001", "产品1")]
print("使用索引查询单个客户的产品：")
print(result)

# 按客户ID分组统计
print("\n各客户消费总额：")
customer_total = df.groupby("客户ID")["金额"].sum()
print(customer_total.head(10))
```


---


## 注意事项


**1、索引值必须唯一**


如果索引值不唯一，某些操作（如 `loc` 查找）会返回多个匹配行。


**2、索引可以有名称**


给索引命名可以提高代码可读性：`df.index.name = "学号"`


**3、索引会跟随数据操作**


切片、筛选等操作会保留索引，需要注意索引与数据的对应关系。


**
索引是 Pandas 性能的关键。常用查询列设置为索引可以大幅提升查找速度，但过多的索引会增加写入开销，需要权衡使用。









	  AI 思考中...





			** [Pandas 数据读写](https://www.runoob.com/pandas-data-io.html)
			[Pandas 多层索引（MultiIndex）](https://www.runoob.com/pandas-multiindex.html) **













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