# Pandas 多层索引（MultiIndex）

- Source: https://www.runoob.com/pandas/pandas-multiindex.html

多层索引（MultiIndex）是 Pandas 中强大的索引功能，允许在行或列上创建多级层次结构。这在处理高维数据、分组统计和面板数据时特别有用。


---


## 创建 MultiIndex


### 从列表创建


## 实例


```python
import pandas as pd

# 方法1：使用数组创建
arrays = [
    ["A", "A", "B", "B", "C", "C"],
    [1, 2, 1, 2, 1, 2]
]

# 使用 pd.MultiIndex.from_arrays
index = pd.MultiIndex.from_arrays(arrays, names=["类别", "编号"])
print("从数组创建：")
print(index)
print()

# 方法2：使用元组列表
tuples = [
    ("A", 1), ("A", 2), ("B", 1), ("B", 2), ("C", 1), ("C", 2)
]
index = pd.MultiIndex.from_tuples(tuples, names=["类别", "编号"])
print("从元组创建：")
print(index)
print()

# 方法3：使用 product
index = pd.MultiIndex.from_product(
    [["A", "B", "C"], [1, 2, 3]],
    names=["类别", "编号"]
)
print("从 product 创建：")
print(index)
```


### 创建带 MultiIndex 的 DataFrame


## 实例


```python
import pandas as pd
import numpy as np

# 创建带多层索引的 DataFrame
df = pd.DataFrame(
    np.random.randn(6, 4),
    index=pd.MultiIndex.from_tuples(
        [("2024", "Q1"), ("2024", "Q2"), ("2024", "Q3"),
         ("2025", "Q1"), ("2025", "Q2"), ("2025", "Q3")]
    ),
    columns=["北京", "上海", "广州", "深圳"]
)
df.index.names = ["年份", "季度"]

print("带多层索引的 DataFrame：")
print(df)
```


---


## 多层索引的访问


### 使用 loc/iloc 访问


## 实例


```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    "语文": [85, 92, 78, 88],
    "数学": [90, 88, 95, 82]
}, index=pd.MultiIndex.from_tuples(
    [("高一", "A班"), ("高一", "B班"), ("高二", "A班"), ("高二", "B班")],
    names=["年级", "班级"]
))

print("原始数据：")
print(df)
print()

# 外层索引访问
print("访问所有高一年级：")
print(df.loc["高一"])
print()

# 内层索引访问
print("访问 A 班：")
print(df.loc[:, "A班"])
print()

# 多层索引访问
print("访问高一的 A 班：")
print(df.loc[("高一", "A班")])
```


### 使用 xs 访问


## 实例


```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    "语文": [85, 92, 78, 88],
    "数学": [90, 88, 95, 82]
}, index=pd.MultiIndex.from_tuples(
    [("高一", "A班"), ("高一", "B班"), ("高二", "A班"), ("高二", "B班")],
    names=["年级", "班级"]
))

# 使用 xs 访问特定层级的值
print("使用 xs 访问高一年级：")
print(df.xs("高一", level="年级"))
print()

print("使用 xs 访问 A 班：")
print(df.xs("A班", level="班级"))
```


---


## 多层索引的转换


### 堆叠与展开


## 实例


```python
import pandas as pd
import numpy as np

# 创建宽格式 DataFrame
df = pd.DataFrame(
    np.arange(12).reshape(3, 4),
    index=pd.MultiIndex.from_tuples(
        [("北京", "2024"), ("上海", "2024"), ("广州", "2024")]
    ),
    columns=pd.MultiIndex.from_tuples(
        [("Q1", "营收"), ("Q1", "利润"), ("Q2", "营收"), ("Q2", "利润")]
    )
)

print("原始数据（嵌套列）：")
print(df)
print()

# unstack：将内层索引转为列
df_unstacked = df.unstack()
print("unstack 后：")
print(df_unstacked)
print()

# stack：将列转为内层索引
df_stacked = df_unstacked.stack()
print("stack 后：")
print(df_stacked)
```


---


## 多层索引的排序


## 实例


```python
import pandas as pd

# 创建带乱序索引的 DataFrame
df = pd.DataFrame({
    "值": [1, 2, 3, 4, 5, 6]
}, index=pd.MultiIndex.from_tuples(
    [("C", 2), ("A", 1), ("B", 2), ("A", 2), ("C", 1), ("B", 1)],
    names=["字母", "数字"]
))

print("乱序数据：")
print(df)
print()

# 按外层排序
df_sorted1 = df.sort_index()
print("按外层排序后：")
print(df_sorted1)
print()

# 按内层排序
df_sorted2 = df.sort_index(level=1)
print("按内层排序后：")
print(df_sorted2)
print()

# 多层排序
df_sorted3 = df.sort_index(level=[0, 1])
print("按多层排序后：")
print(df_sorted3)
```


---


## 实战：分组统计


多层索引非常适合进行分组统计和透视分析。


## 实例


```python
import pandas as pd
import numpy as np

# 创建销售数据
np.random.seed(42)
df = pd.DataFrame({
    "年份": ["2023"] * 6 + ["2024"] * 6,
    "季度": ["Q1", "Q2", "Q3", "Q4"] * 3,
    "产品": ["手机", "手机", "电脑", "电脑"] * 3,
    "区域": ["华东", "华南", "华北"] * 4,
    "销售额": np.random.randint(100, 500, 12)
})

print("原始销售数据：")
print(df)
print()

# 设置多层索引后进行分组统计
df_grouped = df.set_index(["年份", "季度", "产品", "区域"])
print("按年份、季度、产品、区域分组：")
print(df_grouped)

# 按年份汇总
yearly = df_grouped.groupby(level="年份").sum()
print("\n年度销售额：")
print(yearly)

# 按年份和季度汇总
quarterly = df_grouped.groupby(level=["年份", "季度"]).sum()
print("\n季度销售额：")
print(quarterly)
```


---


## 常见问题与注意事项


**1、索引层次混乱**


操作数据时要小心，避免层次错乱。建议在操作前后检查 `df.index.names`。


**2、索引访问错误**


`loc` 使用标签访问，`iloc` 使用位置访问，两者不要混用。


**3、concat 时索引重复**


使用 `concat` 合并数据时，若有重复索引可能导致意外结果，可使用 `ignore_index=True` 重置。


**
多层索引是 Pandas 处理高维数据的核心功能。合理使用多层索引可以让数据组织更清晰，统计更便捷。









	  AI 思考中...





			** [Pandas Index（索引）](https://www.runoob.com/pandas-index.html)
			[Pandas 数据类型（dtype 与类型转换）](https://www.runoob.com/pandas-dtype.html) **













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