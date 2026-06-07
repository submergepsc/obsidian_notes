# Pandas 分组操作（groupby）

- Source: https://www.runoob.com/pandas/pandas-groupby.html

`groupby` 是 Pandas 最强大的功能之一，允许按照一个或多个列对数据进行分组，然后对每个分组进行聚合、转换或过滤操作。


---


## groupby 基本用法


### 单列分组


## 实例


```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    "部门": ["技术", "销售", "技术", "运营", "销售", "技术"],
    "姓名": ["张三", "李四", "王五", "赵六", "钱七", "孙八"],
    "薪资": [12000, 15000, 11000, 18000, 14000, 13000]
})

print("原始数据：")
print(df)
print()

# 按部门分组
grouped = df.groupby("部门")
print(f"分组对象: {type(grouped)}")
print(f"分组数量: {len(grouped)}")
print()

# 查看分组
print("各分组数据：")
for name, group in grouped:
    print(f"\n部门: {name}")
    print(group)
```


### 分组并聚合


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "部门": ["技术", "销售", "技术", "运营", "销售"],
    "薪资": [12000, 15000, 11000, 18000, 14000]
})

print("按部门分组求平均薪资：")
print(df.groupby("部门")["薪资"].mean())
print()

print("按部门分组求和：")
print(df.groupby("部门")["薪资"].sum())
print()

print("按部门分组计数：")
print(df.groupby("部门").size())
```


---


## 多列分组


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "年份": ["2023", "2023", "2024", "2024"],
    "部门": ["技术", "销售", "技术", "销售"],
    "薪资": [12000, 15000, 13000, 16000]
})

print("按年份和部门分组：")
print(df.groupby(["年份", "部门"])["薪资"].sum())
print()

# 作为 DataFrame 输出
result = df.groupby(["年份", "部门"]).agg({
    "薪资": "sum"
}).reset_index()
print("结果 DataFrame：")
print(result)
```


---


## 常用聚合函数


### 单一聚合


| 函数 | 说明 |
| --- | --- |
| sum() | 求和 |
| mean() | 求平均 |
| median() | 求中位数 |
| std() | 标准差 |
| min() / max() | 最小/最大值 |
| count() | 计数 |
| first() / last() | 首/末值 |


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "部门": ["技术", "销售", "技术", "运营"],
    "薪资": [12000, 15000, 11000, 18000]
})

# 链式调用多个聚合
print("链式聚合：")
print(df.groupby("部门")["薪资"].agg(["sum", "mean", "max", "min"]))
```


### 自定义聚合


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "部门": ["技术", "销售", "技术", "运营"],
    "薪资": [12000, 15000, 11000, 18000]
})

# 自定义聚合函数
def range_func(x):
    return x.max() - x.min()

print("使用自定义函数：")
print(df.groupby("部门")["薪资"].agg(range_func))
print()

# 命名聚合（推荐）
print("命名聚合：")
print(df.groupby("部门").agg(
    最低薪资=("薪资", "min"),
    最高薪资=("薪资", "max"),
    平均薪资=("薪资", "mean")
))
```


---


## transform


transform 可以在保持原数据形状的同时，对每个分组进行计算并返回与原数据相同形状的结果。


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "部门": ["技术", "销售", "技术", "运营", "销售"],
    "薪资": [12000, 15000, 11000, 18000, 14000]
})

print("原始数据：")
print(df)
print()

# 计算每个部门的平均薪资，并广播到每行
df["部门平均薪资"] = df.groupby("部门")["薪资"].transform("mean")
print("添加部门平均薪资：")
print(df)
print()

# 计算每人的薪资占部门比例
df["薪资占比"] = df["薪资"] / df["部门平均薪资"]
print("薪资占比：")
print(df)
```


---


## filter 过滤


filter 可以根据分组条件过滤数据。


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "部门": ["技术", "销售", "技术", "运营", "销售", "技术"],
    "薪资": [12000, 15000, 11000, 18000, 14000, 13000]
})

print("原始数据：")
print(df)
print()

# 过滤部门平均薪资大于13000的部门
print("部门平均薪资 > 13000：")
filtered = df.groupby("部门").filter(lambda x: x["薪资"].mean() > 13000)
print(filtered)
print()

# 过滤数量大于2的组
print("成员数 > 2：")
filtered2 = df.groupby("部门").filter(lambda x: len(x) > 2)
print(filtered2)
```


---


## apply 自定义函数


apply 允许对每个分组应用自定义函数。


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "部门": ["技术", "销售", "技术", "运营"],
    "薪资": [12000, 15000, 11000, 18000]
})

# 对每个分组应用自定义函数
result = df.groupby("部门").apply(
    lambda x: pd.Series({
        "总和": x["薪资"].sum(),
        "均值": x["薪资"].mean()
    })
)
print("自定义聚合结果：")
print(result)
```


---


## 实战：销售数据分析


## 实例


```python
import pandas as pd

# 模拟销售数据
sales = pd.DataFrame({
    "日期": pd.date_range("2024-01-01", periods=30, freq="D"),
    "产品": ["手机", "电脑", "平板"] * 10,
    "渠道": ["线上"] * 15 + ["线下"] * 15,
    "销售额": [1000, 2000, 1500] * 10
})

print("=== 销售数据分析 ===\n")

# 1. 按产品统计
print("1. 按产品统计：")
product_summary = sales.groupby("产品")["销售额"].agg(["sum", "mean", "count"])
print(product_summary)
print()

# 2. 按渠道统计
print("2. 按渠道统计：")
channel_summary = sales.groupby("渠道")["销售额"].sum()
print(channel_summary)
print()

# 3. 按产品和渠道交叉统计
print("3. 产品×渠道交叉统计：")
cross_summary = sales.groupby(["产品", "渠道"])["销售额"].sum().unstack()
print(cross_summary)
print()

# 4. 计算各产品销售额占比
print("4. 销售额占比：")
total = sales["销售额"].sum()
product_pct = sales.groupby("产品")["销售额"].sum() / total * 100
print(product_pct.round(2))
```


**
groupby 是数据分析的核心操作，熟练掌握可以高效完成各种统计分析任务。









	  AI 思考中...





			** [Pandas 数据重塑（pivot / melt / stack / unstack）](https://www.runoob.com/pandas-pivot.html)
			[Pandas 窗口函数（rolling / expanding / ewm）](https://www.runoob.com/pandas-rolling.html) **













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