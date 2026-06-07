# Pandas 时间序列分析

- Source: https://www.runoob.com/pandas/pandas-timeseries.html

时间序列分析是数据分析的重要组成部分，Pandas 提供了丰富的功能来处理和分析时间序列数据，包括重采样、滚动计算、移动平均等。


---


## 时间序列基本操作


### 创建时间序列


## 实例


```python
import pandas as pd
import numpy as np

# 创建时间序列数据
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=100, freq="D")

ts = pd.Series(
    np.random.randn(100).cumsum() + 100,
    index=dates
)

print("时间序列数据（前10条）：")
print(ts.head(10))
print()

# 查看信息
print(f"索引类型: {type(ts.index)}")
print(f"开始时间: {ts.index.min()}")
print(f"结束时间: {ts.index.max()}")
print(f"时间跨度: {ts.index.max() - ts.index.min()}")
```


### 设置日期为索引


## 实例


```python
import pandas as pd
import numpy as np

# 创建 DataFrame 并设置日期索引
df = pd.DataFrame({
    "日期": pd.date_range("2024-01-01", periods=30, freq="D"),
    "销售额": np.random.randint(100, 500, 30),
    "访客数": np.random.randint(50, 200, 30)
})

print("设置前：")
print(df.head())
print()

# 设置日期为索引
df = df.set_index("日期")
print("设置后：")
print(df.head())
print()

# 使用 loc 按日期查询
print("查询2024-01-05到2024-01-10：")
print(df.loc["2024-01-05":"2024-01-10"])
```


---


## 重采样


重采样（Resampling）是将时间序列数据从一个频率转换到另一个频率的过程，包括升采样（增加数据点）和降采样（减少数据点）。


### 降采样


## 实例


```python
import pandas as pd
import numpy as np

# 创建日级别数据
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=90, freq="D")
ts = pd.Series(np.random.randint(100, 500, 90), index=dates)

print("日级别数据（前10条）：")
print(ts.head(10))
print()

# 按月重采样（求和）
monthly = ts.resample("M").sum()
print("按月求和：")
print(monthly)
print()

# 按月重采样（求平均）
monthly_mean = ts.resample("M").mean()
print("按月求平均：")
print(monthly_mean)
```


### 升采样


## 实例


```python
import pandas as pd

# 创建低频数据
dates = pd.date_range("2024-01-01", periods=3, freq="M")
ts = pd.Series([100, 200, 150], index=dates)

print("月级别数据：")
print(ts)
print()

# 升采样到日级别（需要填充方法）
ts_daily = ts.resample("D").ffill()
print("升采样到日级别（前10条）：")
print(ts_daily.head(10))
```


### 常用重采样方法


| 方法 | 说明 |
| --- | --- |
| sum() | 求和 |
| mean() | 求平均 |
| max() / min() | 最大/最小值 |
| first() / last() | 第一个/最后一个值 |
| count() | 非空值数量 |
| ohlc() | 开盘、最高、最低、收盘 |


---


## 滚动计算


滚动计算（Rolling）是对时间序列数据进行滑动窗口计算，常用于计算移动平均、移动标准差等。


### 移动平均


## 实例


```python
import pandas as pd
import numpy as np

# 创建数据
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=30, freq="D")
ts = pd.Series(np.random.randint(100, 200, 30), index=dates)

# 计算7天移动平均
rolling_mean = ts.rolling(window=7).mean()
print("7天移动平均（前10条）：")
print(rolling_mean.head(10))
print()

# 计算7天移动标准差
rolling_std = ts.rolling(window=7).std()
print("7天移动标准差：")
print(rolling_std.head(10))
```


### 滚动应用自定义函数


## 实例


```python
import pandas as pd
import numpy as np

ts = pd.Series(range(1, 11))

print("原始数据：")
print(ts)
print()

# 滚动求和
print("滚动3求和：")
print(ts.rolling(3).sum())
print()

# 滚动最大值
print("滚动3最大值：")
print(ts.rolling(3).max())
print()

# 使用 apply
print("滚动3自定义函数（极差）：")
print(ts.rolling(3).apply(lambda x: x.max() - x.min()))
```


---


## 时序数据可视化


## 实例


```python
import pandas as pd
import numpy as np

# 创建示例数据
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=100, freq="D")
ts = pd.Series(
    np.random.randn(100).cumsum() + 100,
    index=dates
)

# 计算移动平均
ma_7 = ts.rolling(7).mean()
ma_30 = ts.rolling(30).mean()

# 显示数据
print("时间序列 + 移动平均：")
print(f"原始数据（前5条）: {ts.head().tolist()}")
print(f"7日均线（前10条）: {ma_7.dropna().head().tolist()}")
print(f"30日均线（最后5条）: {ma_30.dropna().tail().tolist()}")
```


---


## 时序特征提取


## 实例


```python
import pandas as pd

# 创建时间序列
ts = pd.Series(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    index=pd.date_range("2024-01-01", periods=10, freq="D")
)

# 差分
diff = ts.diff()
print("一阶差分：")
print(diff)
print()

# 百分比变化
pct = ts.pct_change()
print("百分比变化：")
print(pct)
print()

# 移位
shifted = ts.shift(1)
print("向后移位1：")
print(shifted)
```


---


## 实战：股票数据分析


## 实例


```python
import pandas as pd
import numpy as np

# 模拟股票数据
np.random.seed(42)
n_days = 60

df = pd.DataFrame({
    "日期": pd.date_range("2024-01-01", periods=n_days, freq="D"),
    "开盘价": 100 + np.random.randn(n_days).cumsum(),
    "收盘价": 100 + np.random.randn(n_days).cumsum(),
    "成交量": np.random.randint(1000000, 10000000, n_days)
})
df = df.set_index("日期")

# 计算每日收益率
df["收益率"] = df["收盘价"].pct_change()

# 计算波动率（7日滚动标准差）
df["波动率"] = df["收益率"].rolling(7).std() * np.sqrt(252)  # 年化

# 计算移动平均线
df["MA5"] = df["收盘价"].rolling(5).mean()
df["MA20"] = df["收盘价"].rolling(20).mean()

# 生成交易信号（金叉/死叉）
df["信号"] = 0
df.loc[df["MA5"] > df["MA20"], "信号"] = 1
df.loc[df["MA5"] < df["MA20"], "信号"] = -1

print("股票数据分析结果：")
print(df.tail(10))
```


---


## 常见问题


**1、日期不连续**


有些时间序列不是每天都有数据（节假日等），需要使用 `asfreq` 或 `reindex` 处理。


**2、时区问题**


处理跨时区数据时，使用 `tz_localize` 和 `tz_convert` 进行时区设置和转换。


**3、缺失值影响**


滚动计算默认会跳过缺失值，但可能影响结果的连续性。


**
时间序列分析是金融、气象、IoT等领域的基础技能，Pandas 提供了完整的工具链来处理这类数据。









	  AI 思考中...





			** [Pandas 日期与时间](https://www.runoob.com/pandas-datetime.html)
			[Pandas apply / map / applymap](https://www.runoob.com/pandas-apply.html) **













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