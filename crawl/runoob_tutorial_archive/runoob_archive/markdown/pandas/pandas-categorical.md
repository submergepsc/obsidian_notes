# Pandas 类别类型（Categorical）

- Source: https://www.runoob.com/pandas/pandas-categorical.html

Categorical 是 Pandas 中用于处理有限类别值的数据类型，特别适合处理枚举类型的数据，如性别、学历、等级等。类别类型可以显著减少内存占用并提升计算性能。


---


## 创建 Categorical 数据


### 从 Series 创建


## 实例


```python
import pandas as pd

# 创建类别数据
s = pd.Series(["男", "女", "男", "女", "男"], dtype="category")
print("基本类别数据：")
print(s)
print(f"类型: {s.dtype}")
print()

# 指定类别顺序
s2 = pd.Series(
    ["低", "中", "高", "中", "低"],
    dtype=pd.CategoricalDtype(categories=["低", "中", "高"], ordered=True)
)
print("有序类别：")
print(s2)
print(f"类别顺序: {s2.dtype.categories.tolist()}")
```


### 从列表创建


## 实例


```python
import pandas as pd

# 使用 pd.Categorical
categories = pd.Categorical(
    ["甲", "乙", "甲", "丙", "乙"],
    categories=["甲", "乙", "丙"]
)

s = pd.Series(categories)
print("从 Categorical 创建：")
print(s)
```


---


## 类别属性与方法


### 访问类别信息


## 实例


```python
import pandas as pd

s = pd.Series(
    ["低", "中", "高", "中", "低"],
    dtype=pd.CategoricalDtype(categories=["低", "中", "高"], ordered=True)
)

# 类别属性
print(f"类别: {s.dtype.categories.tolist()}")
print(f"是否有序: {s.dtype.ordered}")
print()

# 统计各类别数量
print("类别统计：")
print(s.value_counts())
```


### 修改类别


## 实例


```python
import pandas as pd

s = pd.Series(["A", "B", "C", "A", "B"], dtype="category")

print("修改类别名称：")
s2 = s.cat.rename_categories({"A": "优秀", "B": "良好", "C": "及格"})
print(s2)
print()

# 添加新类别
print("添加类别：")
s3 = s.cat.add_categories(["D"])
print(s3.dtype.categories.tolist())
print()

# 删除类别
print("删除类别：")
s4 = s.cat.remove_categories(["C"])
print(s4.dtype.categories.tolist())
```


---


## 有序类别


有序类别支持比较操作，适用于有大小顺序的分类数据。


## 实例


```python
import pandas as pd

# 创建有序类别
s = pd.Series(
    ["低", "中", "高", "高", "低", "中"],
    dtype=pd.CategoricalDtype(categories=["低", "中", "高"], ordered=True)
)

# 比较操作
print("高 > 中:", s > "中")
print("中 > 低:", s > "低")
print()

# 排序
print("排序后：")
print(s.sort_values())
```


---


## 实战：数据分组


## 实例


```python
import pandas as pd

# 模拟用户等级数据
users = pd.DataFrame({
    "用户ID": range(1, 1001),
    "等级": pd.Categorical(
        ["VIP"] * 100 + ["金卡"] * 300 + ["银卡"] * 400 + ["普通"] * 200,
        categories=["普通", "银卡", "金卡", "VIP"],
        ordered=True
    ),
    "消费额": [1000, 500, 100, 50] * 250
})

print("用户等级分布：")
print(users["等级"].value_counts().sort_index())
print()

# 按等级分组统计
print("按等级统计：")
print(users.groupby("等级", observed=True)["消费额"].sum())
```


---


## 内存优化


类别类型可以大幅减少字符串数据的内存占用。


## 实例


```python
import pandas as pd
import numpy as np

# 创建大量重复的字符串数据
np.random.seed(42)
s_str = pd.Series(np.random.choice(["北京", "上海", "广州", "深圳"], 1000000))

# 转换为类别类型
s_cat = s_str.astype("category")

# 内存对比
print(f"字符串类型内存: {s_str.memory_usage(deep=True) / 1024 / 1024:.2f} MB")
print(f"类别类型内存: {s_cat.memory_usage(deep=True) / 1024 / 1024:.2f} MB")
print(f"节省: {(1 - s_cat.memory_usage(deep=True) / s_str.memory_usage(deep=True)) * 100:.1f}%")
```


**
当数据中有大量重复的字符串值时，使用类别类型可以显著减少内存占用，特别适合大数据集。









	  AI 思考中...





			** [Pandas 数据类型（dtype 与类型转换）](https://www.runoob.com/pandas-dtype.html)
			[Pandas 数据选取（loc / iloc / at）](https://www.runoob.com/pandas-loc-iloc.html) **













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