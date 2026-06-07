# Pandas 数据重塑（pivot / melt / stack / unstack）

- Source: https://www.runoob.com/pandas/pandas-pivot.html

数据重塑是数据分析中的常见操作，用于改变数据的布局结构。Pandas 提供了 pivot、melt、stack、unstack 等函数来实现长格式和宽格式之间的转换。


---


## pivot 透视表


`pivot` 将长格式数据转换为宽格式，类似于 Excel 的透视表功能。


### 基本用法


## 实例


```python
import pandas as pd

# 创建长格式数据
df = pd.DataFrame({
    "日期": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02"],
    "产品": ["A", "B", "A", "B"],
    "销量": [100, 150, 120, 90]
})

print("长格式数据：")
print(df)
print()

# 转换为宽格式
pivot_df = df.pivot(index="日期", columns="产品", values="销量")
print("宽格式数据：")
print(pivot_df)
```


### 多重索引


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "年份": ["2024", "2024", "2024", "2024"],
    "季度": ["Q1", "Q1", "Q2", "Q2"],
    "产品": ["A", "B", "A", "B"],
    "销量": [100, 150, 120, 90]
})

print("数据：")
print(df)
print()

# 多重索引透视
pivot_df = df.pivot(index=["年份", "季度"], columns="产品", values="销量")
print("多重索引透视：")
print(pivot_df)
```


### 聚合函数


## 实例


```python
import pandas as pd

# 有重复值的情况
df = pd.DataFrame({
    "日期": ["2024-01-01", "2024-01-01", "2024-01-01", "2024-01-02"],
    "产品": ["A", "A", "B", "B"],
    "销量": [100, 110, 80, 90]
})

print("有重复值的数据：")
print(df)
print()

# pivot 默认不支持重复值，需要用 pivot_table 并指定聚合函数
pivot_df = df.pivot_table(index="日期", columns="产品", values="销量", aggfunc="sum")
print("使用 sum 聚合：")
print(pivot_df)
print()

# 使用 mean
print("使用 mean 聚合：")
print(df.pivot_table(index="日期", columns="产品", values="销量", aggfunc="mean"))
```


**
`pivot` 不允许有重复值，有重复值时使用 `pivot_table` 并指定聚合函数。


---


## melt 逆透视


`melt` 将宽格式数据转换为长格式，是 pivot 的逆操作。


## 实例


```python
import pandas as pd

# 创建宽格式数据
df = pd.DataFrame({
    "日期": ["2024-01-01", "2024-01-02"],
    "A": [100, 120],
    "B": [150, 90]
})

print("宽格式数据：")
print(df)
print()

# 转换为长格式
melted = df.melt(id_vars="日期", var_name="产品", value_name="销量")
print("长格式数据：")
print(melted)
```


### 保持多列不变


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "城市": ["北京", "上海"],
    "2023营收": [1000, 800],
    "2023利润": [200, 150],
    "2024营收": [1200, 950],
    "2024利润": [250, 180]
})

print("宽格式：")
print(df)
print()

# 保持"城市"不变，其他列转换为长格式
melted = df.melt(
    id_vars="城市",
    var_name="指标",
    value_name="数值"
)
print("长格式：")
print(melted)
```


---


## stack 与 unstack


stack 和 unstack 是 MultiIndex 专用的重塑函数。


### unstack


## 实例


```python
import pandas as pd

# 创建带多层索引的数据
df = pd.DataFrame({
    "A": [1, 2, 3, 4],
    "B": [5, 6, 7, 8]
}, index=pd.MultiIndex.from_tuples(
    [("X", 1), ("X", 2), ("Y", 1), ("Y", 2)],
    names=["类别", "编号"]
))

print("多层索引数据：")
print(df)
print()

# unstack 将内层索引转为列
print("unstack 后：")
print(df.unstack())
```


### stack


## 实例


```python
import pandas as pd

# 创建宽格式（带列索引）
df = pd.DataFrame({
    ("A", "X"): [1, 2],
    ("A", "Y"): [3, 4],
    ("B", "X"): [5, 6],
    ("B", "Y"): [7, 8]
})

print("带多层列索引：")
print(df)
print()

# stack 将列索引转为内层索引
print("stack 后：")
print(df.stack())
```


---


## 实战：业务报表转换


## 实例


```python
import pandas as pd

# 模拟业务数据 - 销售记录
sales = pd.DataFrame({
    "日期": ["2024-01"] * 4,
    "产品": ["手机", "电脑", "平板", "耳机"],
    "渠道": ["线上", "线上", "线下", "线上"],
    "销售额": [10000, 20000, 8000, 5000]
})

print("原始销售数据：")
print(sales)
print()

# 使用 pivot 转换
pivot = sales.pivot_table(
    index="产品",
    columns="渠道",
    values="销售额",
    aggfunc="sum",
    fill_value=0
)
print("渠道销售透视：")
print(pivot)
print()

# 还原为长格式
print("还原为长格式：")
print(pivot.reset_index().melt(id_vars="产品", var_name="渠道", value_name="销售额"))
```


---


## 重塑函数选择


| 函数 | 作用 | 典型场景 |
| --- | --- | --- |
| pivot | 长→宽 | 行列转换 |
| pivot_table | 长→宽（带聚合） | 有重复值时 |
| melt | 宽→长 | 数据整理 |
| unstack | 索引→列 | 多层索引 |
| stack | 列→索引 | 多层索引 |


> 数据重塑的目的是为了让数据更适合分析或展示。根据下游需求选择合适的转换方式。









	  AI 思考中...





			** [Pandas 数据拼接（concat / append）](https://www.runoob.com/pandas-concat.html)
			[Pandas 分组操作（groupby）](https://www.runoob.com/pandas-groupby.html) **













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