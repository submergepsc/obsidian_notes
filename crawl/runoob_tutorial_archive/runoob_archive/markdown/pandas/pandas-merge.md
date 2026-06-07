# Pandas 数据合并（merge / join）

- Source: https://www.runoob.com/pandas/pandas-merge.html

Pandas 提供了强大的数据合并功能，可以像 SQL 一样根据键将两个或多个 DataFrame 连接在一起。`merge` 和 `join` 是最常用的两种方法。


---


## merge 基本用法


`pd.merge()` 函数用于将两个 DataFrame 按列进行合并，类似于 SQL 的 JOIN 操作。


### 简单合并


## 实例


```python
import pandas as pd

# 创建两个 DataFrame
df1 = pd.DataFrame({
    "学号": ["S001", "S002", "S003"],
    "姓名": ["张三", "李四", "王五"]
})

df2 = pd.DataFrame({
    "学号": ["S001", "S002", "S003"],
    "数学": [85, 92, 78]
})

print("DataFrame 1：")
print(df1)
print()

print("DataFrame 2：")
print(df2)
print()

# 合并
result = pd.merge(df1, df2, on="学号")
print("合并结果：")
print(result)
```


### 不同列名合并


## 实例


```python
import pandas as pd

df1 = pd.DataFrame({
    "学号": ["S001", "S002", "S003"],
    "姓名": ["张三", "李四", "王五"]
})

df2 = pd.DataFrame({
    "student_id": ["S001", "S002", "S003"],
    "数学": [85, 92, 78]
})

# 使用 left_on 和 right_on
result = pd.merge(df1, df2, left_on="学号", right_on="student_id")
print("不同列名合并：")
print(result)
print()

# 删除多余列
result = result.drop("student_id", axis=1)
print("删除多余列后：")
print(result)
```


---


## 合并类型


### inner / left / right / outer


## 实例


```python
import pandas as pd

df1 = pd.DataFrame({
    "学号": ["S001", "S002", "S003", "S004"],
    "姓名": ["张三", "李四", "王五", "赵六"]
})

df2 = pd.DataFrame({
    "学号": ["S001", "S002", "S003", "S005"],
    "数学": [85, 92, 78, 88]
})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
print()

# inner join（默认）：只保留两者都有的
print("inner join（交集）：")
print(pd.merge(df1, df2, on="学号", how="inner"))
print()

# left join：保留左表所有行
print("left join（保留左表）：")
print(pd.merge(df1, df2, on="学号", how="left"))
print()

# right join：保留右表所有行
print("right join（保留右表）：")
print(pd.merge(df1, df2, on="学号", how="right"))
print()

# outer join：保留所有行
print("outer join（并集）：")
print(pd.merge(df1, df2, on="学号", how="outer"))
```


**
理解四种 JOIN 的区别很重要：inner 保留交集，left 保留左表全部，right 保留右表全部，outer 保留两表全部。


---


## 多键合并 实例


```python
import pandas as pd

df1 = pd.DataFrame({
    "城市": ["北京", "北京", "上海", "上海"],
    "年份": [2023, 2024, 2023, 2024],
    "销售额": [100, 120, 90, 110]
})

df2 = pd.DataFrame({
    "城市": ["北京", "北京", "上海", "上海"],
    "年份": [2023, 2024, 2023, 2024],
    "利润": [20, 25, 18, 22]
})

# 多键合并
result = pd.merge(df1, df2, on=["城市", "年份"])
print("多键合并：")
print(result)
```


---


## join 方法


`DataFrame.join()` 是另一种合并方式，默认为左连接，按索引进行合并。


### 按索引合并


## 实例


```python
import pandas as pd

# 创建数据，设置索引
df1 = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 28]
}, index=["S001", "S002", "S003"])

df2 = pd.DataFrame({
    "数学": [85, 92, 78],
    "英语": [90, 88, 95]
}, index=["S001", "S002", "S003"])

print("DataFrame 1：")
print(df1)
print()

print("DataFrame 2：")
print(df2)
print()

# 使用 join 合并
result = df1.join(df2)
print("join 合并：")
print(result)
```


### 多表合并


## 实例


```python
import pandas as pd

df1 = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"]
}, index=["S001", "S002", "S003"])

df2 = pd.DataFrame({
    "数学": [85, 92, 78]
}, index=["S001", "S002", "S004"])

df3 = pd.DataFrame({
    "英语": [90, 88, 95]
}, index=["S001", "S003", "S004"])

# 链式 join
result = df1.join(df2, how="left").join(df3, how="left")
print("多表 join（左连接）：")
print(result)
print()

# 使用 outer
result2 = df1.join(df2, how="outer").join(df3, how="outer")
print("多表 join（全外连接）：")
print(result2)
```


---


## 实战：多表关联


## 实例


```python
import pandas as pd

# 模拟业务数据
# 1. 员工表
employees = pd.DataFrame({
    "员工ID": ["E001", "E002", "E003", "E004"],
    "姓名": ["张三", "李四", "王五", "赵六"],
    "部门ID": ["D001", "D001", "D002", "D003"]
})

# 2. 部门表
departments = pd.DataFrame({
    "部门ID": ["D001", "D002", "D003"],
    "部门名称": ["技术部", "销售部", "运营部"]
})

# 3. 薪资表
salaries = pd.DataFrame({
    "员工ID": ["E001", "E002", "E003", "E004"],
    "薪资": [12000, 15000, 11000, 18000]
})

print("步骤1：合并员工和部门")
result = pd.merge(employees, departments, on="部门ID")
print(result)
print()

print("步骤2：再合并薪资")
result = pd.merge(result, salaries, on="员工ID")
print(result)
```


---


## merge vs join 选择


| 对比 | merge | join |
| --- | --- | --- |
| 合并依据 | 列 | 索引 |
| 默认连接 | inner | left |
| 适用场景 | 按业务键合并 | 按主键/索引合并 |


> 大多数情况下 merge 更灵活，join 在按索引合并时更简洁。根据实际数据结构选择合适的方法。









	  AI 思考中...





			** [Pandas apply / map / applymap](https://www.runoob.com/pandas-apply.html)
			[Pandas 数据拼接（concat / append）](https://www.runoob.com/pandas-concat.html) **













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