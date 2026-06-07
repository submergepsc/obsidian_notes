# Pandas 电商数据分析实战

- Source: https://www.runoob.com/pandas/pandas-ecommerce.html

本节通过一个完整的电商数据分析案例，综合运用 Pandas 的各种功能进行数据分析。


---


## 案例概述


分析电商平台的订单数据，包括销售趋势、产品表现、客户分析等维度。


### 数据准备


## 实例


```python
import pandas as pd
import numpy as np

# 模拟电商订单数据
np.random.seed(42)
n_orders = 1000

orders = pd.DataFrame({
    "订单ID": range(1, n_orders + 1),
    "客户ID": np.random.randint(100, 200, n_orders),
    "商品ID": np.random.randint(1, 20, n_orders),
    "下单日期": pd.date_range("2024-01-01", periods=n_orders, freq="30min"),
    "数量": np.random.randint(1, 5, n_orders),
    "单价": np.random.uniform(10, 500, n_orders).round(2)
})

# 计算订单金额
orders["订单金额"] = (orders["数量"] * orders["单价"]).round(2)

print("订单数据概览：")
print(orders.head(10))
print(f"\n数据量: {len(orders)} 条")
```


### 数据预处理


## 实例


```python
# 提取日期特征
orders["日期"] = orders["下单日期"].dt.date
orders["小时"] = orders["下单日期"].dt.hour
orders["星期"] = orders["下单日期"].dt.day_name()
orders["月份"] = orders["下单日期"].dt.month

print("添加时间特征后：")
print(orders.head())
print()

# 缺失值检查
print("缺失值检查：")
print(orders.isnull().sum())
```


---


## 销售分析


### 整体销售情况


## 实例


```python
# 整体销售指标
print("=== 整体销售情况 ===\n")
print(f"总订单数: {len(orders):,}")
print(f"总销售额: ¥{orders['订单金额'].sum():,.2f}")
print(f"平均订单金额: ¥{orders['订单金额'].mean():,.2f}")
print(f"中位数订单金额: ¥{orders['订单金额'].median():,.2f}")
print()

# 按月统计
monthly = orders.groupby("月份").agg({
    "订单ID": "count",
    "订单金额": "sum",
    "客户ID": "nunique"
}).rename(columns={
    "订单ID": "订单数",
    "订单金额": "销售额",
    "客户ID": "客户数"
})

print("月度销售趋势：")
print(monthly)
```


### 产品分析


## 实例


```python
# 产品销售排名
product_sales = orders.groupby("商品ID").agg({
    "订单ID": "count",
    "数量": "sum",
    "订单金额": "sum"
}).rename(columns={
    "订单ID": "订单数",
    "数量": "销量",
    "订单金额": "销售额"
}).sort_values("销售额", ascending=False)

print("=== 产品销售排名 Top 10 ===\n")
print(product_sales.head(10))
print()

# 热销产品
print(f"热销产品: 商品 {product_sales.index[0]}")
print(f"销售额: ¥{product_sales.iloc[0]['销售额']:,.2f}")
```


### 客户分析


## 实例


```python
# 客户消费分析
customer_sales = orders.groupby("客户ID").agg({
    "订单ID": "count",
    "订单金额": "sum"
}).rename(columns={
    "订单ID": "订单数",
    "订单金额": "总消费"
})

print("=== 客户分析 ===\n")
print(f"活跃客户数: {len(customer_sales)}")
print(f"客户平均订单数: {customer_sales['订单数'].mean():.1f}")
print(f"客户平均消费: ¥{customer_sales['总消费'].mean():,.2f}")
print()

# 客户分层
customer_sales["分层"] = pd.cut(
    customer_sales["总消费"],
    bins=[0, 1000, 5000, 10000, float("inf")],
    labels=["普通", "银卡", "金卡", "VIP"]
)

print("客户分层统计：")
print(customer_sales["分层"].value_counts())
```


### 时间分析


## 实例


```python
# 按时段分析
hourly = orders.groupby("小时")["订单金额"].sum()

print("=== 时段销售分析 ===\n")
print(f"销售高峰时段: {hourly.idxmax()} 点")
print(f"该时段销售额: ¥{hourly.max():,.2f}")
print()

# 按星期分析
weekday = orders.groupby("星期")["订单金额"].sum().reindex([
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
])

print("星期销售：")
for day, amount in weekday.items():
    print(f"{day}: ¥{amount:,.2f}")
```


---


## 分析总结


## 实例


```python
print("""
=== 电商数据分析总结 ===

1. 销售概况
   - 总订单数: {0}
   - 总销售额: ¥{1:,.2f}
   - 平均客单价: ¥{2:.2f}

2. 产品表现
   - 热销产品: 商品 {3}
   - 产品销售额分布不均，头部产品贡献大量收入

3. 客户洞察
   - 活跃客户: {4} 人
   - 建议重点维护高价值客户

4. 时间规律
   - 销售高峰在 {5} 点左右
   - 可根据高峰时段调整营销策略

5. 优化建议
   - 1) 针对热销产品加大库存和推广
   - 2) 对高价值客户提供个性化服务
   - 3) 在销售高峰时段增加客服配置
""".format(
    len(orders),
    orders["订单金额"].sum(),
    orders["订单金额"].mean(),
    product_sales.index[0],
    len(customer_sales),
    hourly.idxmax()
))
```










	  AI 思考中...





			** [Pandas 与 Matplotlib / Seaborn 进阶可视化](https://www.runoob.com/panda-matplotlib-seaborn.html)
			[Pandas 用户行为分析实战](https://www.runoob.com/pandas-user-behavior.html) **













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