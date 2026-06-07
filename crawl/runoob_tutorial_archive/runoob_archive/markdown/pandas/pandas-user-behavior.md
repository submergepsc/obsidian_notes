# Pandas 用户行为分析实战

- Source: https://www.runoob.com/pandas/pandas-user-behavior.html

用户行为分析是产品优化的重要依据。本案例展示如何分析用户的访问、留存、转化等行为数据。


---


## 数据准备


### 模拟用户行为数据


## 实例


```python
import pandas as pd
import numpy as np

np.random.seed(42)
n_users = 500
n_events = 5000

# 用户基础信息
users = pd.DataFrame({
    "用户ID": range(1, n_users + 1),
    "注册日期": pd.date_range("2024-01-01", periods=n_users, freq="D")[:n_users],
    "渠道": np.random.choice(["自然搜索", "广告", "推荐", "社交"], n_users),
    "设备": np.random.choice(["PC", "Mobile", "Tablet"], n_users, p=[0.3, 0.6, 0.1])
})

# 用户行为事件
events = pd.DataFrame({
    "事件ID": range(1, n_events + 1),
    "用户ID": np.random.randint(1, n_users + 1, n_events),
    "事件类型": np.random.choice(
        ["浏览", "点击", "收藏", "加购", "下单", "评论"],
        n_events,
        p=[0.4, 0.25, 0.1, 0.1, 0.1, 0.05]
    ),
    "事件时间": pd.date_range("2024-01-15", periods=n_events, freq="10min")
})

# 合并数据
events = events.merge(users[["用户ID", "渠道", "设备"]], on="用户ID")

print("用户数据：")
print(users.head())
print(f"\n用户数: {len(users)}")
print("\n事件数据：")
print(events.head())
print(f"\n事件数: {len(events)}")
```


---


## 用户活跃分析


### 事件类型分布


## 实例


```python
# 事件类型统计
event_dist = events["事件类型"].value_counts()
event_pct = events["事件类型"].value_counts(normalize=True) * 100

print("=== 事件类型分布 ===\n")
event_analysis = pd.DataFrame({
    "次数": event_dist,
    "占比": event_pct.round(2)
})
print(event_analysis)
print()

# 各事件类型用户数
event_users = events.groupby("事件类型")["用户ID"].nunique()
print("各事件类型参与用户数：")
print(event_users)
```


### 用户参与度


## 实例


```python
# 用户事件统计
user_events = events.groupby("用户ID").agg({
    "事件ID": "count",
    "事件类型": lambda x: x.nunique()
}).rename(columns={
    "事件ID": "事件总数",
    "事件类型": "事件类型数"
})

print("=== 用户参与度 ===\n")
print(f"平均每用户事件数: {user_events['事件总数'].mean():.1f}")
print(f"中位数: {user_events['事件总数'].median():.0f}")
print(f"最高: {user_events['事件总数'].max()}")
print()

# 用户分层
user_events["活跃度"] = pd.cut(
    user_events["事件总数"],
    bins=[0, 3, 10, 20, float("inf")],
    labels=["低活跃", "一般", "活跃", "高活跃"]
)

print("用户活跃度分布：")
print(user_events["活跃度"].value_counts())
```


---


## 转化漏斗分析


### 转化路径


## 实例


```python
# 按事件类型计算用户数
funnel = events.groupby("事件类型")["用户ID"].nunique()
funnel = funnel.reindex(["浏览", "点击", "收藏", "加购", "下单", "评论"])

# 计算转化率
funnel_df = pd.DataFrame({
    "用户数": funnel,
    "绝对转化率": (funnel / funnel["浏览"] * 100).round(2),
    "步骤转化率": (funnel / funnel.shift(1) * 100).round(2)
}).fillna(100)

print("=== 转化漏斗 ===\n")
print(funnel_df)
print()

# 可视化漏斗数据
print("漏斗数据：")
for step, row in funnel_df.iterrows():
    print(f"{step}: {row['用户数']} 人 ({row['绝对转化率']:.1f}%)")
```


---


## 渠道分析


### 各渠道表现


## 实例


```python
# 渠道用户分析
channel_analysis = events.groupby("渠道").agg({
    "用户ID": "nunique",
    "事件ID": "count"
}).rename(columns={
    "用户ID": "用户数",
    "事件ID": "事件数"
})

channel_analysis["人均事件数"] = (
    channel_analysis["事件数"] / channel_analysis["用户数"]
).round(2)

print("=== 渠道分析 ===\n")
print(channel_analysis)
print()

# 渠道转化对比
channel_funnel = events[events["事件类型"].isin(["浏览", "下单"])].groupby(
    ["渠道", "事件类型"]
)["用户ID"].nunique().unstack()

channel_funnel["转化率"] = (
    channel_funnel["下单"] / channel_funnel["浏览"] * 100
).round(2)

print("各渠道转化率：")
print(channel_funnel)
```


---


## 设备分析


## 实例


```python
# 设备分析
device_analysis = events.groupby("设备").agg({
    "用户ID": "nunique",
    "事件ID": "count"
}).rename(columns={
    "用户ID": "用户数",
    "事件ID": "事件数"
})

device_analysis["人均事件"] = (
    device_analysis["事件数"] / device_analysis["用户数"]
).round(2)

print("=== 设备分布 ===\n")
print(device_analysis)
print()

# 设备转化率
device_funnel = events[events["事件类型"].isin(["浏览", "下单"])].groupby(
    ["设备", "事件类型"]
)["用户ID"].nunique().unstack()

device_funnel["转化率"] = (
    device_funnel["下单"] / device_funnel["浏览"] * 100
).round(2)

print("各设备转化率：")
print(device_funnel)
```


### 留存分析


## 实例


```python
# 简化留存分析
# 假设注册后7天内活跃视为留存
users_with_events = events.groupby("用户ID")["事件时间"].agg(["min", "max"])
users_with_events.columns = ["首次活跃", "最后活跃"]

# 合并注册信息
users_analysis = users.merge(users_with_events, left_on="用户ID", right_index=True, how="left")

# 计算活跃天数
users_analysis["活跃天数"] = (
    users_analysis["最后活跃"] - users_analysis["首次活跃"]
).dt.days + 1

print("=== 用户留存分析 ===\n")
print(f"有行为用户: {len(users_with_events)}")
print(f"平均活跃天数: {users_analysis['活跃天数'].mean():.1f} 天")
print()

# 次日留存（简化）
retention_1d = len(users_analysis[users_analysis["活跃天数"] >= 2]) / len(users_analysis) * 100
retention_3d = len(users_analysis[users_analysis["活跃天数"] >= 3]) / len(users_analysis) * 100

print(f"次日留存率: {retention_1d:.1f}%")
print(f"3日留存率: {retention_3d:.1f}%")
```


## 分析总结


## 实例


```python
print("""
=== 用户行为分析总结 ===

1. 用户参与度
   - 事件类型以浏览为主，点击次之
   - 用户平均参与事件数较少，需要提升用户粘性

2. 转化漏斗
   - 存在较大流失，需要优化用户体验
   - 从浏览到下单转化率较低

3. 渠道效果
   - 建议重点优化高用户量渠道的转化路径
   - 各渠道表现存在差异，需精细化运营

4. 设备表现
   - Mobile 是主要设备，需重点优化移动端体验

5. 优化建议
   - 1) 优化商品展示，提升浏览-点击转化
   - 2) 简化购物流程，降低下单流失
   - 3) 针对Mobile端优化页面加载速度
   - 4) 建立用户分层运营体系
""")
```










	  AI 思考中...





			** [Pandas 电商数据分析实战](https://www.runoob.com/pandas-ecommerce.html)
			[Pandas pd.isna() 函数](https://www.runoob.com/pandas-pd-isna.html) **













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