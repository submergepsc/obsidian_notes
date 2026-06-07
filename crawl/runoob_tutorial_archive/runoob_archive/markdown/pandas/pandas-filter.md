# Pandas 过滤与条件查询

- Source: https://www.runoob.com/pandas/pandas-filter.html

数据过滤是数据分析中最常用的操作之一。Pandas 提供了丰富的条件查询功能，可以根据各种条件筛选数据。本节详细介绍各种数据过滤方法。


---


## 基础条件过滤


### 单一条件过滤


## 实例


```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "钱七"],
    "年龄": [25, 30, 28, 35, 22],
    "城市": ["北京", "上海", "广州", "北京", "深圳"],
    "薪资": [12000, 15000, 11000, 18000, 9000],
    "部门": ["技术", "销售", "技术", "运营", "技术"]
})

print("原始数据：")
print(df)
print()

# 等于过滤
print("城市等于北京：")
print(df[df["城市"] == "北京"])
print()

# 不等于过滤
print("城市不等于北京：")
print(df[df["城市"] != "北京"])
print()

# 大于小于
print("薪资大于12000：")
print(df[df["薪资"] > 12000])
print()

# 字符串条件
print("姓名包含'三'：")
print(df[df["姓名"].str.contains("三")])
```


### 多条件组合


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "钱七"],
    "年龄": [25, 30, 28, 35, 22],
    "城市": ["北京", "上海", "广州", "北京", "深圳"],
    "薪资": [12000, 15000, 11000, 18000, 9000],
    "部门": ["技术", "销售", "技术", "运营", "技术"]
})

# AND 条件：使用 & 符号
print("北京 且 薪资>10000：")
print(df[(df["城市"] == "北京") & (df["薪资"] > 10000)])
print()

# OR 条件：使用 | 符号
print("技术部门 或 薪资>15000：")
print(df[(df["部门"] == "技术") | (df["薪资"] > 15000)])
print()

# NOT 条件：使用 ~ 符号
print("不是技术部门：")
print(df[~(df["部门"] == "技术")])
print()

# 复杂组合
print("（北京且年龄>25）或（上海）：")
print(df[((df["城市"] == "北京") & (df["年龄"] > 25)) | (df["城市"] == "上海")])
```


**
多条件组合时，每个条件需要用括号括起来，并且条件之间使用 `&`（与）、`|`（或）连接，不能使用 Python 的 `and`、`or` 关键字。


---


## isin 与 where


### isin 筛选


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "钱七"],
    "城市": ["北京", "上海", "广州", "北京", "深圳"],
    "部门": ["技术", "销售", "技术", "运营", "技术"]
})

# 在列表中筛选
print("城市是北京或上海：")
print(df[df["城市"].isin(["北京", "上海"])])
print()

# 不在列表中
print("城市不是北京和上海：")
print(df[~df["城市"].isin(["北京", "上海"])])
print()

# 多列 isin
df2 = pd.DataFrame({
    "城市": ["北京", "上海"],
    "部门": ["技术", "销售"]
})
print("同时满足城市和部门：")
print(df[df[["城市", "部门"]].isin(df2).all(axis=1)])
```


### where 条件


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 5, 3, 7],
    "B": [4, 2, 8, 3]
})

# where：保留满足条件的值，不满足的设为 NaN 或 指定值
print("值大于3的保留，其他设为0：")
result = df.where(df > 3, 0)
print(result)
print()

# 使用其他 DataFrame 作为条件
other = pd.DataFrame({
    "A": [True, False, True, False],
    "B": [False, True, False, True]
})
print("根据条件 DataFrame 筛选：")
print(df.where(other, -1))
```


---


## 字符串过滤


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "孙七"],
    "城市": ["北京市", "上海市", "广州市", "深圳市", "杭州市"],
    "邮箱": ["[email protected]", "[email protected]", "[email protected]",
             "[email protected]", "[email protected]"]
})

# 包含
print("城市包含'北京'：")
print(df[df["城市"].str.contains("北京")])
print()

# 开头/结尾
print("邮箱以 zhang 开头：")
print(df[df["邮箱"].str.startswith("zhang")])
print()

# 正则匹配
print("邮箱用户名长度大于4：")
print(df[df["邮箱"].str.extract(r"(\w+)@")[0].str.len() > 4])
print()

# 多个模式匹配
print("城市以 北、上、广、深 开头：")
print(df[df["城市"].str.contains("^北|^上|^广|^深")])
```


---


## 数值范围过滤


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "钱七"],
    "年龄": [25, 30, 28, 35, 22],
    "薪资": [12000, 15000, 11000, 18000, 9000]
})

# 范围筛选
print("年龄在25-30之间（含）：")
print(df[df["年龄"].between(25, 30)])
print()

# 分位数筛选
q1 = df["薪资"].quantile(0.25)
q3 = df["薪资"].quantile(0.75)
print(f"薪资在25%-75%之间（{q1}-{q3}）：")
print(df[df["薪资"].between(q1, q3)])
print()

# 最小/最大N条
print("薪资最高的3条：")
print(df.nlargest(3, "薪资"))
print()

print("薪资最低的2条：")
print(df.nsmallest(2, "薪资"))
```


---


## 时间数据过滤


## 实例


```python
import pandas as pd

# 创建时间序列数据
df = pd.DataFrame({
    "日期": pd.date_range("2024-01-01", periods=10, freq="D"),
    "销量": [100, 120, 90, 150, 200, 180, 110, 130, 170, 190]
})
df = df.set_index("日期")

print("时间序列数据：")
print(df)
print()

# 按日期筛选
print("2024-01-05 的数据：")
print(df.loc["2024-01-05"])
print()

# 日期范围筛选
print("2024-01-03 到 2024-01-07：")
print(df.loc["2024-01-03":"2024-01-07"])
print()

# 使用 truncate（更高效的切片）
print("truncate 筛选：")
print(df.truncate(before="2024-01-03", after="2024-01-07"))
```


---


## query 方法


`query` 方法提供了一种更简洁的 SQL 风格的过滤方式。


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六"],
    "年龄": [25, 30, 28, 35],
    "城市": ["北京", "上海", "广州", "北京"],
    "薪资": [12000, 15000, 11000, 18000]
})

# 使用 query 方法
print("年龄>26 且 城市='北京'：")
print(df.query("年龄 > 26 and 城市 == '北京'"))
print()

# 使用变量
min_age = 26
city = "北京"
print(f"年龄>{min_age} 且 城市={city}：")
print(df.query("年龄 > @min_age and 城市 == @city"))
print()

# 列名有空格时需要用反引号
df2 = df.rename(columns={"姓名": "姓 名"})
print("列名有空格时：")
print(df2.query("`姓 名` == '张三'"))
```


---


## 常见问题


1、条件组合报错**


多条件过滤时要使用括号明确优先级，并且使用 `&`、`|` 而不是 `and`、`or`。


**2、字符串包含空值**


使用 `str.contains` 前需要处理空值：`df[df["列"].str.contains("x", na=False)]`


**3、索引过滤**


如果 DataFrame 有自定义索引，需要注意 `loc` 和 `iloc` 的区别。


**
对于复杂的多条件查询，`query` 方法的语法更接近自然语言，代码更易读。当数据量很大时，`loc` 配合布尔数组通常比 `query` 更快。









	  AI 思考中...





			** [Pandas 数据选取（loc / iloc / at）](https://www.runoob.com/pandas-loc-iloc.html)
			[Pandas 缺失值处理](https://www.runoob.com/pandas-missing-data.html) **













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