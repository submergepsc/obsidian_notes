# Pandas apply / map / applymap

- Source: https://www.runoob.com/pandas/pandas-apply.html

apply、map 和 applymap 是 Pandas 中用于数据转换的三大函数，它们可以对 DataFrame 或 Series 进行灵活的逐元素或批量操作。


---


## Series.map


`map` 是 Series 的方法，用于对 Series 中的每个元素进行转换。


### 基本用法


## 实例


```python
import pandas as pd

# 创建 Series
s = pd.Series([1, 2, 3, 4, 5])

print("原始数据：")
print(s)
print()

# 使用函数
print("每个元素 * 2：")
print(s.map(lambda x: x * 2))
print()

# 使用字典映射
mapping = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
print("使用字典映射：")
print(s.map(mapping))
print()

# 使用 Series 映射
mapping_series = pd.Series(["A", "B", "C", "D", "E"], index=[1, 2, 3, 4, 5])
print("使用 Series 映射：")
print(s.map(mapping_series))
```


### 处理缺失值


## 实例


```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, np.nan, 4, 5])

print("包含 NaN：")
print(s)
print()

# map 默认跳过 NaN
print("map 处理（跳过 NaN）：")
print(s.map(lambda x: x * 2 if pd.notna(x) else -1))
```


---


## DataFrame.applymap


`applymap` 是 DataFrame 的方法，对每个元素逐个应用函数（注意：Pandas 2.0+ 推荐使用 `DataFrame.map` 代替）。


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
})

print("原始数据：")
print(df)
print()

# 对每个元素乘以2
print("每个元素 * 2：")
print(df.applymap(lambda x: x * 2))
print()

# 保留2位小数
print("保留2位小数：")
print(df.applymap(lambda x: round(x, 2)))
```


**
applymap 逐元素操作，对于大数据可能会比较慢。如果只需要对数值列操作，考虑使用向量化操作或 apply 配合 axis 参数。


---


## DataFrame.apply


`apply` 是最灵活的方法，可以沿着坐标轴应用函数。


### 按列应用


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [10, 20, 30, 40, 50],
    "C": [100, 200, 300, 400, 500]
})

print("原始数据：")
print(df)
print()

# 默认 axis=0，按列应用
print("每列求和：")
print(df.apply(sum))
print()

print("每列最大值：")
print(df.apply(max))
```


### 按行应用


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [10, 20, 30],
    "C": [100, 200, 300]
})

print("原始数据：")
print(df)
print()

# axis=1，按行应用
print("每行求和：")
print(df.apply(sum, axis=1))
print()

# 每行最大值-最小值
print("每行极差：")
print(df.apply(lambda x: x.max() - x.min(), axis=1))
```


### 使用 aggfunc 聚合


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [10, 20, 30]
})

# 同时应用多个函数
print("同时求和与均值：")
print(df.apply([sum, np.mean]))
print()

# 返回多个值
result = df.apply(lambda x: pd.Series({
    "sum": x.sum(),
    "mean": x.mean(),
    "max": x.max()
}, index=["sum", "mean", "max"]))

print("返回多个值：")
print(result)
```


---


## Series.apply


Series 同样可以使用 apply，功能与 map 类似但更灵活。


## 实例


```python
import pandas as pd
import numpy as np

s = pd.Series([1, 4, 9, 16, 25])

print("原始数据：")
print(s)
print()

# 开平方
print("开平方：")
print(s.apply(np.sqrt))
print()

# 条件返回
print("条件判断：")
print(s.apply(lambda x: "大" if x > 10 else "小"))
```


---


## 性能对比


## 实例


```python
import pandas as pd
import numpy as np
import time

# 创建大数据
n = 100000
s = pd.Series(np.random.randn(n))

# 测试 map vs apply
func = lambda x: x * 2 + 1

start = time.time()
result1 = s.map(func)
map_time = time.time() - start

start = time.time()
result2 = s.apply(func)
apply_time = time.time() - start

# 向量化（最快）
start = time.time()
result3 = s * 2 + 1
vec_time = time.time() - start

print(f"map 耗时: {map_time:.4f}s")
print(f"apply 耗时: {apply_time:.4f}s")
print(f"向量化耗时: {vec_time:.4f}s")

print("\n结论：优先使用向量化操作，性能最好")
```


---


## 实战：数据转换


## 实例


```python
import pandas as pd
import numpy as np

# 创建示例 DataFrame
df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六"],
    "年龄": [25, 30, 28, 35],
    "薪资": [12000, 15000, 11000, 18000],
    "部门": ["技术", "销售", "技术", "运营"]
})

print("原始数据：")
print(df)
print()

# 使用 apply 进行行级别计算
def calculate(row):
    """计算年收入和税后薪资"""
    annual = row["薪资"] * 12
    tax = annual * 0.1 if annual > 120000 else annual * 0.05
    after_tax = annual - tax
    return pd.Series({
        "年薪": annual,
        "税": tax,
        "税后": after_tax
    })

result = df.apply(calculate, axis=1)
df_result = pd.concat([df, result], axis=1)

print("计算结果：")
print(df_result)
```


---


## 三者的选择


| 方法 | 适用对象 | 场景 | 性能 |
| --- | --- | --- | --- |
| map | Series | 元素级转换、字典映射 | 快 |
| applymap | DataFrame | 元素级转换（非数值列） | 慢 |
| apply | Series/DataFrame | 行列聚合、自定义函数 | 中 |


> 能用向量化操作（直接用运算符）的情况下不要用 apply/map，能用 map 的情况下不要用 apply。









	  AI 思考中...





			** [Pandas 时间序列分析](https://www.runoob.com/pandas-timeseries.html)
			[Pandas 数据合并（merge / join）](https://www.runoob.com/pandas-merge.html) **













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