# Pandas 描述性统计

- Source: https://www.runoob.com/pandas/pandas-describe.html

描述性统计用于总结和描述数据的基本特征。Pandas 提供了丰富的统计函数，可以快速获取数据的整体分布情况。


---


## 基本统计函数


## 实例


```python
import pandas as pd
import numpy as np

# 创建示例数据
df = pd.DataFrame({
    "年龄": [25, 30, 28, 35, 22, 40, 38, 45, 29, 31],
    "薪资": [12000, 15000, 11000, 18000, 9000, 20000, 17000, 22000, 12500, 14000],
    "绩效": [85, 92, 78, 88, 65, 95, 82, 90, 75, 89]
})

print("=== 数据概览 ===")
print(f"数据形状: {df.shape}")
print(f"\n基础统计：")
print(df.describe())
```


### 常用统计量


| 函数 | 说明 | 示例 |
| --- | --- | --- |
| count() | 非空值数量 | df["年龄"].count() |
| sum() | 求和 | df["薪资"].sum() |
| mean() | 平均值 | df["年龄"].mean() |
| median() | 中位数 | df["年龄"].median() |
| std() | 标准差 | df["绩效"].std() |
| var() | 方差 | df["绩效"].var() |
| min() / max() | 最小/最大值 | df["年龄"].min() |
| quantile() | 分位数 | df["薪资"].quantile(0.25) |


### 计算分位数


## 实例


```python
import pandas as pd
import numpy as np

s = pd.Series(range(1, 101))  # 1到100

print("各种分位数：")
print(f"0% (最小): {s.quantile(0)}")
print(f"25%: {s.quantile(0.25)}")
print(f"50% (中位数): {s.quantile(0.50)}")
print(f"75%: {s.quantile(0.75)}")
print(f"100% (最大): {s.quantile(1)}")
print()

# 同时计算多个分位数
print("批量分位数：")
print(s.quantile([0.1, 0.2, 0.5, 0.8, 0.9]))
```


---


## describe 汇总


`describe()` 提供数据集中数值列的综合统计摘要。


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "年龄": [25, 30, 28, 35],
    "薪资": [12000, 15000, 11000, 18000],
    "城市": ["北京", "上海", "广州", "深圳"]
})

print("数值列统计：")
print(df.describe())
print()

print("包含所有列：")
print(df.describe(include="all"))
```


---


## 相关系数与协方差


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "年龄": [25, 30, 28, 35, 22],
    "薪资": [12000, 15000, 11000, 18000, 9000],
    "绩效": [85, 92, 78, 88, 65]
})

print("相关系数矩阵：")
print(df.corr())
print()

# 与特定列的相关
print("与薪资的相关：")
print(df.corr()["薪资"])
```


**
相关系数范围 -1 到 1，越接近 1 表示正相关，越接近 -1 表示负相关，接近 0 表示无相关。


---


## 高级统计


## 实例


```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 偏度（衡量分布偏斜程度）
print(f"偏度: {s.skew()}")

# 峰度（衡量分布尖峭程度）
print(f"峰度: {s.kurtosis()}")
print()

# 累计统计
s = pd.Series([1, 2, 3, 4, 5])
print("累计和：")
print(s.cumsum())
print()

print("累计最大值：")
print(s.cummax())
```










	  AI 思考中...





			** [Pandas 窗口函数（rolling / expanding / ewm）](https://www.runoob.com/pandas-rolling.html)
			[Pandas 抽样与随机数据](https://www.runoob.com/pandas-sample.html) **













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