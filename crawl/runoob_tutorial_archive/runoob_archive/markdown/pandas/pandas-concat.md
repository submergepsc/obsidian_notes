# Pandas 数据拼接（concat / append）

- Source: https://www.runoob.com/pandas/pandas-concat.html

数据拼接是将多个 DataFrame 或 Series 按行或按列拼接在一起。`pd.concat` 是主要的拼接函数，`append` 是简化版本（已废弃，更推荐使用 concat）。


---


## concat 基本用法


`pd.concat()` 可以沿着轴方向拼接多个 DataFrame 或 Series。


### 行方向拼接（上下拼接）


## 实例


```python
import pandas as pd

# 创建两个 DataFrame
df1 = pd.DataFrame({
    "姓名": ["张三", "李四"],
    "年龄": [25, 30]
})

df2 = pd.DataFrame({
    "姓名": ["王五", "赵六"],
    "年龄": [28, 35]
})

print("DataFrame 1：")
print(df1)
print()

print("DataFrame 2：")
print(df2)
print()

# 上下拼接
result = pd.concat([df1, df2], ignore_index=True)
print("拼接结果：")
print(result)
```


### 列方向拼接（左右拼接）


## 实例


```python
import pandas as pd

df1 = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"]
})

df2 = pd.DataFrame({
    "年龄": [25, 30, 28],
    "城市": ["北京", "上海", "广州"]
})

# 左右拼接
result = pd.concat([df1, df2], axis=1)
print("左右拼接：")
print(result)
```


**
`axis=0` 表示行方向拼接（增加行），`axis=1` 表示列方向拼接（增加列）。


---


## 处理重复索引


### ignore_index


## 实例


```python
import pandas as pd

df1 = pd.DataFrame({
    "姓名": ["张三", "李四"],
    "年龄": [25, 30]
}, index=[0, 1])

df2 = pd.DataFrame({
    "姓名": ["王五", "赵六"],
    "年龄": [28, 35]
}, index=[0, 1])

# 默认保留原始索引
print("保留原始索引：")
print(pd.concat([df1, df2]))
print()

# 忽略旧索引，重新生成
print("忽略原始索引：")
print(pd.concat([df1, df2], ignore_index=True))
```


### 验证重复键


## 实例


```python
import pandas as pd

df1 = pd.DataFrame({
    "A": [1, 2]
})

df2 = pd.DataFrame({
    "A": [3, 4]
})

# 检查是否有重复键
print("验证对象：")
print(pd.concat([df1, df2], verify_integrity=True))
```


---


## 处理列不匹配


### join 参数


## 实例


```python
import pandas as pd

df1 = pd.DataFrame({
    "A": [1, 2, 3],
    "B": ["a", "b", "c"]
})

df2 = pd.DataFrame({
    "B": ["x", "y", "z"],
    "C": [10, 20, 30]
})

print("df1：")
print(df1)
print()

print("df2：")
print(df2)
print()

# outer join（默认）：保留所有列
print("outer 拼接（保留所有列）：")
print(pd.concat([df1, df2], join="outer"))
print()

# inner join：只保留共同的列
print("inner 拼接（保留共同列）：")
print(pd.concat([df1, df2], join="inner"))
```


### 只添加新列


## 实例


```python
import pandas as pd

df1 = pd.DataFrame({
    "姓名": ["张三", "李四"],
    "年龄": [25, 30]
})

df2 = pd.DataFrame({
    "城市": ["北京", "上海"]
})

# 将 df2 的列添加到 df1
result = pd.concat([df1, df2], axis=1)
print("只添加新列：")
print(result)
```


---


## keys 参数创建层次索引


## 实例


```python
import pandas as pd

df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
df3 = pd.DataFrame({"A": [9, 10], "B": [11, 12]})

# 使用 keys 参数创建层次索引
result = pd.concat([df1, df2, df3], keys=["第一年", "第二年", "第三年"])
print("带层次索引的拼接：")
print(result)
print()

# 从层次索引获取数据
print("获取第二年数据：")
print(result.loc["第二年"])
```


---


## 实战：合并多个月份数据


## 实例


```python
import pandas as pd

# 模拟多个月份的销售数据
jan_sales = pd.DataFrame({
    "月份": ["2024-01"] * 3,
    "产品": ["A", "B", "C"],
    "销量": [100, 150, 80]
})

feb_sales = pd.DataFrame({
    "月份": ["2024-02"] * 3,
    "产品": ["A", "B", "C"],
    "销量": [120, 140, 90]
})

mar_sales = pd.DataFrame({
    "月份": ["2024-03"] * 3,
    "产品": ["A", "B", "C"],
    "销量": [110, 160, 85]
})

# 合并第一季度数据
quarterly = pd.concat([jan_sales, feb_sales, mar_sales], ignore_index=True)
print("第一季度汇总：")
print(quarterly)
print()

# 按月统计
monthly_summary = quarterly.groupby("月份")["销量"].sum()
print("月度销量汇总：")
print(monthly_summary)
```


---


## append 方法（已废弃）


`DataFrame.append()` 在 Pandas 2.0 中已废弃，不推荐使用。请使用 `pd.concat()` 代替。


```
# 不推荐（已废弃）
result = df1.append(df2)

# 推荐
result = pd.concat([df1, df2])
```


> `concat` 是 Pandas 中拼接数据的标准方法，性能更好，功能更完整。









	  AI 思考中...





			** [Pandas 数据合并（merge / join）](https://www.runoob.com/pandas-merge.html)
			[Pandas 数据重塑（pivot / melt / stack / unstack）](https://www.runoob.com/pandas-pivot.html) **













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