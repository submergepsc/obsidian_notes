# Pandas 日期与时间

- Source: https://www.runoob.com/pandas/pandas-datetime.html

Pandas 提供了强大的日期时间处理能力，可以方便地将字符串转换为日期类型，并进行各种日期相关的计算和分析。


---


## 创建日期时间


### date_range 函数


## 实例


```python
import pandas as pd

# 创建日期范围
dates = pd.date_range("2024-01-01", periods=10, freq="D")
print("按天：")
print(dates)
print()

# 按月
dates_month = pd.date_range("2024-01-01", periods=12, freq="M")
print("按月：")
print(dates_month)
print()

# 按小时
dates_hour = pd.date_range("2024-01-01 00:00", periods=24, freq="H")
print("按小时（前5条）：")
print(dates_hour[:5])
```


### DatetimeIndex 与 DatetimeArray


## 实例


```python
import pandas as pd
import numpy as np

# 使用 datetime 对象创建
dt = pd.DatetimeIndex([
    pd.Timestamp("2024-01-01"),
    pd.Timestamp("2024-01-02"),
    pd.Timestamp("2024-01-03")
])
print("DatetimeIndex：")
print(dt)
print()

# 创建带时间的 Series
s = pd.Series(
    [100, 200, 300],
    index=pd.date_range("2024-01-01", periods=3, freq="D")
)
print("带日期索引的 Series：")
print(s)
```


---


## 字符串转日期


### pd.to_datetime


## 实例


```python
import pandas as pd

# 各种格式的字符串转日期
dates_str = ["2024-01-01", "2024/01/02", "01-03-2024", "20240104"]

# 自动推断格式
dt = pd.to_datetime(dates_str)
print("自动推断格式：")
print(dt)
print()

# 指定格式
dt2 = pd.to_datetime(dates_str, format="%Y-%m-%d")
print("指定格式：")
print(dt2)
print()

# 处理无效值
dt3 = pd.to_datetime(["2024-01-01", "invalid", "2024-01-03"], errors="coerce")
print("处理无效值（转为 NaT）：")
print(dt3)
```


### read_csv 自动解析日期


## 实例


```python
import pandas as pd
from io import StringIO

# 模拟 CSV 数据
csv_data = """日期,销售额
2024-01-01,100
2024-01-02,200
2024-01-03,150
"""

# 方法1：读取后转换
df = pd.read_csv(StringIO(csv_data))
df["日期"] = pd.to_datetime(df["日期"])
print("读取后转换：")
print(df.dtypes)
print()

# 方法2：读取时直接解析
df2 = pd.read_csv(StringIO(csv_data), parse_dates=["日期"])
print("读取时解析：")
print(df2.dtypes)
```


---


## 日期属性访问


日期时间转换为 datetime 类型后，可以方便地提取各种属性。


## 实例


```python
import pandas as pd

# 创建日期 Series
s = pd.Series(pd.date_range("2024-01-15", periods=5, freq="D"))

print("日期 Series：")
print(s)
print()

# 提取年/月/日
print("提取年：")
print(s.dt.year)
print()

print("提取月：")
print(s.dt.month)
print()

print("提取日：")
print(s.dt.day)
print()

# 提取星期几（0=周一，6=周日）
print("星期几（数字）：")
print(s.dt.dayofweek)
print()

# 提取星期几名称
print("星期几名称：")
print(s.dt.day_name())
```


### 更多日期属性


| 属性 | 说明 | 示例 |
| --- | --- | --- |
| year | 年 | 2024 |
| month | 月（1-12） | 1 |
| day | 日（1-31） | 15 |
| hour | 小时（0-23） | 10 |
| minute | 分钟（0-59） | 30 |
| dayofweek | 星期（0-6） | 0 |
| quarter | 季度（1-4） | 1 |
| is_month_start | 是否月初 | True/False |
| is_month_end | 是否月末 | True/False |


---


## 日期运算


### 日期加减


## 实例


```python
import pandas as pd

# 创建日期
date = pd.Timestamp("2024-01-15")
print(f"基准日期: {date}")
print()

# 加减天数
print(f"+3天: {date + pd.Timedelta(days=3)}")
print(f"-5天: {date - pd.Timedelta(days=5)}")
print()

# 日期差
date1 = pd.Timestamp("2024-01-01")
date2 = pd.Timestamp("2024-01-15")
print(f"日期差: {date2 - date1}")
print(f"天数差: {(date2 - date1).days}")
print()

# 日期 Series 运算
dates = pd.date_range("2024-01-01", periods=5, freq="D")
print("日期 + 3天：")
print(dates + pd.Timedelta(days=3))
```


### 日期偏移


## 实例


```python
import pandas as pd

date = pd.Timestamp("2024-01-15")
print(f"基准日期: {date}")
print()

# 月初/月末
print(f"月初: {date + pd.offsets.MonthBegin(1)}")
print(f"月末: {date + pd.offsets.MonthEnd(1)}")
print()

# 年份偏移
print(f"加1年: {date + pd.DateOffset(years=1)}")
print(f"减1月: {date + pd.DateOffset(months=-1)}")
print()

# 工作日
print(f"下周一: {date + pd.offsets.Week(weekday=0)}")
```


---


## 时区处理


## 实例


```python
import pandas as pd

# 创建不带时区的时间
dates = pd.date_range("2024-01-01 10:00", periods=3, freq="H")
print("不带时区：")
print(dates)
print()

# 设置时区
dates_utc = dates.tz_localize("UTC")
print("设置 UTC 时区：")
print(dates_utc)
print()

# 转换时区
dates_shanghai = dates_utc.tz_convert("Asia/Shanghai")
print("转换到上海时区：")
print(dates_shanghai)
```


---


## 实战：销售数据分析


## 实例


```python
import pandas as pd

# 模拟销售数据
df = pd.DataFrame({
    "日期": pd.date_range("2024-01-01", periods=30, freq="D"),
    "销售额": [100, 150, 120, 180, 200, 90, 80] * 4 + [100, 100]
})
df["日期"] = pd.to_datetime(df["日期"])

print("销售数据：")
print(df.head(10))
print()

# 按星期统计
print("按星期几统计平均销售额：")
weekday_sales = df.groupby(df["日期"].dt.day_name())["销售额"].mean()
print(weekday_sales)
print()

# 按月统计
print("按月统计：")
df["月份"] = df["日期"].dt.to_period("M")
monthly_sales = df.groupby("月份")["销售额"].sum()
print(monthly_sales)
print()

# 计算7天滚动平均
df["7天滚动平均"] = df["销售额"].rolling(window=7).mean()
print("添加7天滚动平均：")
print(df.head(10))
```


---


## 常见问题


**1、日期格式不统一**


使用 `pd.to_datetime` 时可以指定 `format` 参数明确格式，避免解析错误。


**2、时区混淆**


跨时区数据处理时，确保所有时间使用统一的时区或 UTC 时间。


**3、日期运算使用 Timedelta**


日期加减使用 `pd.Timedelta`，而不是简单的整数加减。


**
处理时间序列数据时，建议尽早将日期字符串转换为 datetime 类型，以便利用 Pandas 强大的日期功能。









	  AI 思考中...





			** [Pandas 字符串操作](https://www.runoob.com/pandas-string.html)
			[Pandas 时间序列分析](https://www.runoob.com/pandas-timeseries.html) **













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