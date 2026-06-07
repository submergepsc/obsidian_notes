# Pandas 重复数据处理

- Source: https://www.runoob.com/pandas/pandas-duplicate.html

重复数据是数据分析中常见的问题，会影响统计结果的准确性。Pandas 提供了检测和处理重复数据的完整功能。


---


## 检测重复数据


### duplicated 方法


## 实例


```python
import pandas as pd

# 创建包含重复行的 DataFrame
df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "张三", "李四", "赵六"],
    "年龄": [25, 30, 28, 25, 30, 35],
    "城市": ["北京", "上海", "广州", "北京", "深圳", "北京"]
})

print("原始数据：")
print(df)
print()

# 检测重复行（默认从第一条开始标记，keep='first'）
print("检测重复行：")
print(df.duplicated())
print()

# 统计重复行数量
print(f"重复行数量: {df.duplicated().sum()}")
print()

# 检测特定列的重复
print("按'姓名'列检测重复：")
print(df.duplicated(subset=["姓名"]))
```


### keep 参数


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "张三", "王五", "李四"],
    "年龄": [25, 30, 25, 28, 30]
})

print("原始数据：")
print(df)
print()

# keep='first'：保留第一次出现的（默认）
print("keep='first'（默认）：")
print(df.duplicated(keep="first"))
print()

# keep='last'：保留最后一次出现的
print("keep='last'：")
print(df.duplicated(keep="last"))
print()

# keep=False：标记所有重复项（不保留任何）
print("keep=False（标记所有重复）：")
print(df.duplicated(keep=False))
```


---


## 删除重复数据


### drop_duplicates 基本用法


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "张三", "王五", "李四"],
    "年龄": [25, 30, 25, 28, 30],
    "城市": ["北京", "上海", "北京", "广州", "深圳"]
})

print("原始数据：")
print(df)
print()

# 删除重复行（默认保留第一个）
print("删除重复行（保留第一个）：")
print(df.drop_duplicates())
print()

# 保留最后一个
print("删除重复行（保留最后一个）：")
print(df.drop_duplicates(keep="last"))
print()

# 不保留任何重复行
print("删除所有重复行：")
print(df.drop_duplicates(keep=False))
```


### 按列删除重复


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "张三", "王五"],
    "年龄": [25, 30, 35, 28],
    "城市": ["北京", "上海", "北京", "广州"]
})

print("原始数据：")
print(df)
print()

# 按单列去重
print("按'姓名'列去重：")
print(df.drop_duplicates(subset=["姓名"]))
print()

# 按多列组合去重
print("按'姓名'+'城市'组合去重：")
print(df.drop_duplicates(subset=["姓名", "城市"]))
print()

# 保留特定列值最大的行
print("按'姓名'分组，保留年龄最大的：")
print(df.sort_values("年龄", ascending=False).drop_duplicates(subset=["姓名"], keep="first"))
```


---


## 实战：数据清洗


### 综合案例


## 实例


```python
import pandas as pd
import numpy as np

# 创建模拟的订单数据（包含重复）
orders = pd.DataFrame({
    "订单号": ["O001", "O002", "O001", "O003", "O002", "O004"],
    "客户ID": ["C001", "C002", "C001", "C003", "C002", "C004"],
    "商品": ["iPhone", "MacBook", "iPhone", "iPad", "AirPods", "Apple Watch"],
    "金额": [8000, 12000, 8000, 5000, 1500, 3000],
    "日期": ["2024-01-01", "2024-01-02", "2024-01-01", "2024-01-03", "2024-01-02", "2024-01-04"]
})

print("原始订单数据：")
print(orders)
print()

# 1. 检测重复订单
print("重复订单检测：")
duplicates = orders[orders.duplicated(subset=["订单号"], keep=False)]
print(duplicates)
print()

# 2. 删除完全重复的订单
orders_clean = orders.drop_duplicates()
print("删除完全重复后：")
print(f"原始 {len(orders)} 行 -> {len(orders_clean)} 行")
print()

# 3. 按订单号去重，保留最新的
# 假设最后一条是最新的
orders_clean = orders.sort_values("日期").drop_duplicates(
    subset=["订单号"],
    keep="last"
).sort_index()

print("按订单号去重（保留最新）：")
print(orders_clean)
```


---


## 高级用法


### 按分组保留特定行


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "客户": ["A", "A", "A", "B", "B", "B"],
    "月份": ["01", "02", "03", "01", "02", "03"],
    "消费": [100, 200, 150, 300, 250, 280]
})

print("原始数据：")
print(df)
print()

# 保留每个客户消费最高的月份
print("每个客户消费最高的月份：")
result = df.sort_values("消费", ascending=False).drop_duplicates(
    subset=["客户"],
    keep="first"
).sort_values("客户")
print(result)
print()

# 保留每个客户的第一条记录（按月份）
print("每个客户的第一条记录：")
result = df.sort_values("月份").drop_duplicates(
    subset=["客户"],
    keep="first"
)
print(result)
```


### 标记重复而非删除


## 实例


```python
import pandas as pd

df = pd.DataFrame({
    "姓名": ["张三", "李四", "张三", "王五", "李四"],
    "城市": ["北京", "上海", "北京", "广州", "深圳"]
})

# 添加重复标记列
df["是否重复"] = df.duplicated(subset=["姓名"], keep=False)

print("标记重复行：")
print(df)
print()

# 或者使用 groupby 标记
df["重复次数"] = df.groupby("姓名")["姓名"].transform("count")
df["是否首次"] = ~df.duplicated(subset=["姓名"], keep="first")

print("分组统计重复次数：")
print(df)
```


---


## 注意事项


**1、区分"完全重复"和"部分重复"**


完全重复指所有列值相同，部分重复指特定列相同。使用 `subset` 参数指定判断重复的列。


**2、保留策略选择**


根据业务需求选择保留第一条、最后一条或不保留。保留哪一条可能影响后续分析结果。


**3、数据类型影响**


判断重复时会考虑数据类型，例如整数的 1 和浮点数的 1.0 会被视为不同。


**
删除重复数据前，建议先分析重复的原因和分布，确保删除操作不会丢失重要信息。









	  AI 思考中...





			** [Pandas 缺失值处理](https://www.runoob.com/pandas-missing-data.html)
			[Pandas 字符串操作](https://www.runoob.com/pandas-string.html) **













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