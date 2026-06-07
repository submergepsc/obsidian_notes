# Pandas 窗口函数（rolling / expanding / ewm）

- Source: https://www.runoob.com/pandas/pandas-rolling.html

窗口函数用于对时间序列或有序数据进行滑动窗口计算，是金融分析、信号处理等领域的重要工具。


---


## rolling 滚动窗口


### 基本用法


## 实例


```python
import pandas as pd
import numpy as np

# 创建时间序列数据
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=20, freq="D")
ts = pd.Series(np.random.randint(100, 200, 20), index=dates)

print("原始数据（前10条）：")
print(ts.head(10))
print()

# 7天滚动平均
ma7 = ts.rolling(window=7).mean()
print("7天滚动平均（前10条）：")
print(ma7.head(10))
print()

# 滚动求和
rolling_sum = ts.rolling(window=5).sum()
print("5天滚动求和：")
print(rolling_sum.head(10))
```


### 滚动窗口类型


## 实例


```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 固定窗口大小
print("固定窗口 (3)：")
print(s.rolling(3).mean())
print()

# 移动窗口（时间窗口）
# 1分钟后窗口
s2 = pd.Series([1, 2, 3, 4, 5], index=pd.date_range("2024-01-01", periods=5, freq="T"))
print("时间窗口（1分钟）：")
print(s2.rolling("1min").sum())
```


---


## expanding 扩展窗口


扩展窗口从开始累积到当前位置，窗口大小逐渐增大。


## 实例


```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 4, 5])

# 扩展窗口计算累积均值
exp_mean = s.expanding().mean()
print("累积均值：")
print(exp_mean)
print()

# 扩展窗口计算累积最大值
exp_max = s.expanding().max()
print("累积最大值：")
print(exp_max)
print()

# 扩展窗口计算标准差
exp_std = s.expanding().std()
print("累积标准差：")
print(exp_std)
```


---


## ewm 指数加权移动


指数加权移动平均（EWMA）对近期数据赋予更大权重。


## 实例


```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# alpha 越小，近期数据权重越大
ewm_05 = s.ewm(alpha=0.5).mean()
ewm_2 = s.ewm(alpha=0.2).mean()

print("原始数据：")
print(s.values)
print("\nalpha=0.5:")
print(ewm_05.values)
print("\nalpha=0.2:")
print(ewm_2.values)
print()

# 使用 span（与 alpha 关系：alpha = 2/(span+1)）
ewm_span = s.ewm(span=5).mean()
print("span=5:")
print(ewm_span.values)
```


**
EWM 对趋势变化更敏感，适合需要快速响应的场景。


---


## 实战：股票技术指标


## 实例


```python
import pandas as pd
import numpy as np

# 模拟股价数据
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=30, freq="D")
df = pd.DataFrame({
    "日期": dates,
    "收盘价": 100 + np.random.randn(30).cumsum()
})

# 计算技术指标
# 5日均线
df["MA5"] = df["收盘价"].rolling(5).mean()

# 10日均线
df["MA10"] = df["收盘价"].rolling(10).mean()

# 5日指数加权均线
df["EMA5"] = df["收盘价"].ewm(span=5).mean()

# 波动率（5日滚动标准差）
df["Volatility"] = df["收盘价"].rolling(5).std()

# 累积最高价
df["Highest"] = df["收盘价"].expanding().max()

print("股票技术指标：")
print(df.round(2))
```


---


## 窗口函数对比


| 类型 | 说明 | 适用场景 |
| --- | --- | --- |
| rolling | 固定大小窗口 | 移动平均、波动率 |
| expanding | 累积窗口 | 累计统计、止损/止盈 |
| ewm | 指数加权 | 趋势跟踪、快速响应 |









	  AI 思考中...





			** [Pandas 分组操作（groupby）](https://www.runoob.com/pandas-groupby.html)
			[Pandas 描述性统计](https://www.runoob.com/pandas-describe.html) **













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