# 

- Source: https://www.runoob.com/pandas/pandas-dateoffset-object.html

Pandas 的 DateOffset 对象是用于处理日期和时间数据时进行时间偏移的一种工具。

以下是 DateOffset 的一些关键特性和用法：


### 基本概念

DateOffset 对象类似于 Timedelta，但它遵循日历中的日期时间规则，而不是直接进行时间性质的算术计算，这意味着 DateOffset 会考虑到实际的日历天数，例如在处理跨月或跨年的日期时，它会正确地计算天数差异，而 Timedelta 则是简单地加上指定的天数，不考虑月份和年份的变化。


### 使用方法

DateOffset 可以通过算数运算符（如 +）或 apply 方法来执行日期偏移操作。

例如，你可以这样使用 DateOffset 来增加月份或小时：


## 实例


```python
ts = pd.Timestamp('2017-01-01 09:10:11')
ts + DateOffset(months=3)  # 增加三个月
ts + DateOffset(hours=2)   # 增加两小时
```


如果不指定任何参数，DateOffset() 默认增加一个日历日：


```
ts + DateOffset()  # 默认增加一天
```


### 支持的参数

DateOffset 支持多种参数，可以指定增加或替换的时间单位，如年、月、周、日、小时、分钟、秒等。这些参数可以是增加到偏移值的（如 years、months、weeks、days、hours、minutes、seconds 等），也可以是替换偏移值的（如 year、month、day、weekday、hour、minute、second 等）。


### 特殊方法


DateOffset 还提供了 rollforward() 和 rollback() 方法，用于将日期向前或向后滚动到最近的一个有效日期。例如，如果你使用工作日偏移（BDay），它会跳过周末，直接滚动到下一个工作日。


## 实例


```python
friday = pd.Timestamp('2022-01-05')
two_business_days = 2 * pd.offsets.BDay()
friday + two_business_days  # 增加两个工作日，会跳过周末
```


### 频率字符串

DateOffset 支持频率字符串或偏移别名，可以作为 freq 参数传入。这些频率字符串表示的是 DateOffset 对象及其子类，它们定义了日期时间索引的频率。

DateOffset 是 Pandas 中处理时间序列数据时非常有用的工具，它使得日期和时间的偏移操作更加符合实际日历规则。


---

## 常用函数


### DateOffset 构造函数


| 类/方法 | 描述 |
| --- | --- |
| pd.DateOffset(**kwargs) | 创建一个 DateOffset 对象，支持自定义时间偏移量。 |


---


### 常用 DateOffset 子类


| 类 | 描述 |
| --- | --- |
| pd.offsets.Day() | 表示天数的偏移量。 |
| pd.offsets.BDay() | 表示工作日的偏移量（不包括周末）。 |
| pd.offsets.Hour() | 表示小时的偏移量。 |
| pd.offsets.Minute() | 表示分钟的偏移量。 |
| pd.offsets.Second() | 表示秒数的偏移量。 |
| pd.offsets.Milli() | 表示毫秒的偏移量。 |
| pd.offsets.Micro() | 表示微秒的偏移量。 |
| pd.offsets.MonthEnd() | 表示月末的偏移量。 |
| pd.offsets.MonthBegin() | 表示月初的偏移量。 |
| pd.offsets.YearEnd() | 表示年末的偏移量。 |
| pd.offsets.YearBegin() | 表示年初的偏移量。 |
| pd.offsets.QuarterEnd() | 表示季末的偏移量。 |
| pd.offsets.QuarterBegin() | 表示季初的偏移量。 |
| pd.offsets.Week() | 表示周的偏移量。 |
| pd.offsets.WeekOfMonth() | 表示月中第几周的偏移量。 |


---


### DateOffset 属性


| 属性 | 描述 |
| --- | --- |
| DateOffset.name | 返回 DateOffset 的名称。 |
| DateOffset.n | 返回或设置偏移量的数量。 |
| DateOffset.normalize | 返回或设置是否将时间标准化为午夜。 |


---


### DateOffset 方法


| 方法 | 描述 |
| --- | --- |
| DateOffset.apply(other) | 将偏移量应用于另一个日期时间对象。 |
| DateOffset.rollforward(other) | 将日期向前滚动到下一个偏移量。 |
| DateOffset.rollback(other) | 将日期向后滚动到上一个偏移量。 |
| DateOffset.is_anchored() | 检查偏移量是否锚定（即是否固定频率）。 |
| DateOffset.onOffset(date) | 检查日期是否与偏移量对齐。 |


---


### 实例


## 实例


```python
import pandas as pd
from pandas.tseries.offsets import Day, BDay, MonthEnd

# 创建 DateOffset
offset = Day(3)
print(offset)  # 输出 <3 * Days>

# 应用 DateOffset
date = pd.Timestamp('2023-01-01')
new_date = date + offset
print(new_date)  # 输出 2023-01-04

# 使用常用子类
bday_offset = BDay(2)
new_bdate = date + bday_offset
print(new_bdate)  # 输出 2023-01-05（跳过周末）

# 月末偏移量
month_end_offset = MonthEnd()
new_month_end = date + month_end_offset
print(new_month_end)  # 输出 2023-01-31
```


---


### 详细参数说明


#### pd.DateOffset()


| 参数 | 描述 |
| --- | --- |
| years | 年数偏移量。 |
| months | 月数偏移量。 |
| weeks | 周数偏移量。 |
| days | 天数偏移量。 |
| hours | 小时数偏移量。 |
| minutes | 分钟数偏移量。 |
| seconds | 秒数偏移量。 |
| milliseconds | 毫秒数偏移量。 |
| microseconds | 微秒数偏移量。 |
| nanoseconds | 纳秒数偏移量。 |


#### pd.offsets.BDay()


| 参数 | 描述 |
| --- | --- |
| n | 偏移量的数量，默认为 1。 |
| normalize | 是否将时间标准化为午夜，默认为 False。 |


#### pd.offsets.MonthEnd()


| 参数 | 描述 |
| --- | --- |
| n | 偏移量的数量，默认为 1。 |
| normalize | 是否将时间标准化为午夜，默认为 False。 |


---


如果需要更详细的信息，可以参考 [Pandas 官方文档](https://pandas.pydata.org/docs/reference/offset_frequency.html)。









	  AI 思考中...





			** [Pandas Index 对象](https://www.runoob.com/pandas-index-object.html)
			[Pandas 测验](https://www.runoob.com/../quiz/pandas-quiz.html) **













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