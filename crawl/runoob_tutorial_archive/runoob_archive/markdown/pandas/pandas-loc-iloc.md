# Pandas 数据选取（loc / iloc / at）

- Source: https://www.runoob.com/pandas/pandas-loc-iloc.html

数据选取是 Pandas 最常用的操作之一。理解 `loc`、`iloc`、`at` 的区别和应用场景，可以让你更高效地处理数据。


---


## loc 与 iloc 的区别


| 特性 | loc | iloc |
| --- | --- | --- |
| 索引方式 | 标签索引（label-based） | 位置索引（integer-based） |
| 切片 | 包含结束位置 | 不包含结束位置 |
| 单个值 | 返回标量 | 返回标量 |
| 推荐场景 | 有明确索引标签时 | 按位置选择时 |


## 实例


```python
import pandas as pd

# 创建示例 DataFrame
df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "钱七"],
    "年龄": [25, 30, 28, 35, 22],
    "城市": ["北京", "上海", "广州", "深圳", "杭州"]
}, index=[1, 3, 5, 7, 9])  # 注意：索引不是连续的

print("DataFrame：")
print(df)
print()

# loc: 使用标签索引（包含结束位置）
print("df.loc[1:5]（标签切片，包含5）：")
print(df.loc[1:5])
print()

# iloc: 使用位置索引（不包含结束位置）
print("df.iloc[0:2]（位置切片，不包含2）：")
print(df.iloc[0:2])
```


---


## loc 的用法


### 选择行


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六"],
    "年龄": [25, 30, 28, 35],
    "城市": ["北京", "上海", "广州", "深圳"]
}, index=["a", "b", "c", "d"])

# 选择单行（返回 Series）
print("选择一行：")
print(df.loc["a"])
print()

# 选择多行
print("选择多行：")
print(df.loc[["a", "c"]])
print()

# 切片选择（包含开始和结束）
print("切片选择：")
print(df.loc["a":"c"])
```


### 选择列


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 28],
    "城市": ["北京", "上海", "广州"]
}, index=["a", "b", "c"])

# 选择单列
print("选择单列：")
print(df.loc[:, "姓名"])
print()

# 选择多列
print("选择多列：")
print(df.loc[:, ["姓名", "城市"]])
print()

# 切片选择列
print("切片选择列：")
print(df.loc[:, "姓名":"城市"])
```


### 选择特定行列（推荐方式）


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六"],
    "年龄": [25, 30, 28, 35],
    "城市": ["北京", "上海", "广州", "深圳"]
}, index=["a", "b", "c", "d"])

# 选择特定行列
print("选择单个值：")
print(df.loc["a", "姓名"])  # 返回 "张三"
print(type(df.loc["a", "姓名"]))  # 类型是 str
print()

# 选择多行多列
print("选择子集：")
print(df.loc[["a", "c"], ["姓名", "城市"]])
print()

# 条件选择
print("年龄大于28的行：")
print(df.loc[df["年龄"] > 28])
```


---


## iloc 的用法


### 按位置选择


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六"],
    "年龄": [25, 30, 28, 35],
    "城市": ["北京", "上海", "广州", "深圳"]
})

# 选择第0行
print("选择第0行：")
print(df.iloc[0])
print()

# 选择前3行
print("选择前3行：")
print(df.iloc[:3])
print()

# 选择特定行
print("选择特定行：")
print(df.iloc[[0, 2, 3]])
print()

# 负数索引（从末尾开始）
print("选择最后一行：")
print(df.iloc[-1])
print()

print("选择最后3行：")
print(df.iloc[-3:])
```


### 选择列


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 28],
    "城市": ["北京", "上海", "广州"]
})

# 选择第0列
print("第0列：")
print(df.iloc[:, 0])
print()

# 选择第1和第2列
print("选择多列：")
print(df.iloc[:, [1, 2]])
print()

# 切片选择
print("切片选择列：")
print(df.iloc[:, 0:2])
```


---


## at 与 iat（获取单个值）


`at` 和 `iat` 是专门用于获取/设置单个值的访问器，比 `loc` 和 `iloc>更快。`


## 实例


```python
import pandas as pd
import time
import numpy as np

# 创建大 DataFrame 用于性能测试
df = pd.DataFrame(np.random.randn(1000, 10), columns=[f"col_{i}" for i in range(10)])

# at 获取单个值（标签索引）
print(f"at: {df.at[0, 'col_0']}")

# iat 获取单个值（位置索引）
print(f"iat: {df.iat[0, 0]}")

# 性能对比
n = 10000

start = time.time()
for _ in range(n):
    _ = df.iloc[0, 0]
print(f"iloc 耗时: {time.time() - start:.4f}s")

start = time.time()
for _ in range(n):
    _ = df.iat[0, 0]
print(f"iat 耗时: {time.time() - start:.4f}s")
```


---


## 条件选择


使用布尔条件筛选数据是最常见的操作之一。


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六"],
    "年龄": [25, 30, 28, 35],
    "城市": ["北京", "上海", "广州", "北京"],
    "薪资": [12000, 15000, 11000, 18000]
})

# 单一条件
print("年龄大于28的员工：")
print(df[df["年龄"] > 28])
print()

# 多条件（使用 & | ~）
print("北京且薪资大于12000：")
print(df[(df["城市"] == "北京") & (df["薪资"] > 12000)])
print()

# isin 筛选
print("城市是北京或上海：")
print(df[df["城市"].isin(["北京", "上海"])])
print()

# 字符串包含
print("姓名包含'三'：")
print(df[df["姓名"].str.contains("三")])
```


---


## 注意事项


**1、切片包含结束位置**


`loc` 的切片包含结束位置，`iloc` 不包含。


**2、索引不存在会报错**


使用 `loc` 时如果索引不存在会抛出 KeyError，可以使用 `loc[index_list]` 配合 `reindex`。


**3、推荐优先使用 `loc`


因为 `loc` 更易读且不容易出错，除非需要按位置选择。


> `at`/`iat` 是访问单个值最快的方式，`loc`/`iloc` 用于选择多个值。选择合适的方法可以提升代码性能和可读性。









	  AI 思考中...





			** [Pandas 类别类型（Categorical）](https://www.runoob.com/pandas-categorical.html)
			[Pandas 过滤与条件查询](https://www.runoob.com/pandas-filter.html) **













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