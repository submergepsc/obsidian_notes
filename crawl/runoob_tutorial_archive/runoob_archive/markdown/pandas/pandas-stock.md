# Pandas 股票数据分析

- Source: https://www.runoob.com/pandas/pandas-stock.html

在股票数据分析中，pandas 是一个非常强大的工具，可以帮助我们处理和分析股票市场的数据。

在本章节我们使用 yfinance（雅虎财经库）下载历史股票数据，并进行各种分析，包括数据清洗、可视化、技术指标计算等。


yfinance 是一个 Python 库，可以轻松地从雅虎财经（Yahoo Finance）获取股票、基金、加密货币等资产的历史和实时数据。

通过 pandas，我们可以将这些数据存储为 DataFrame 并进行后续的分析。


- **数据清洗**：处理缺失值、删除不必要的列等。
- **数据可视化**：绘制股票的时间序列图、移动平均线、RSI 等。
- **技术指标计算**：如移动平均线（SMA）、相对强弱指数（RSI）等。
- **日收益率与累计收益率分析**：帮助评估股票的短期和长期表现。
- **波动率分析**：衡量股票的价格波动性。


更多财经库及量化分析可以参考：[Python 量化交易](https://www.runoob.com/../python-qt/qt-tutorial.html)


### 安装 yfinance

首先，我们需要安装 yfinance 库，方法如下：


```
pip install yfinance --upgrade --no-cache-dir
```


安装 yfinance 时，pandas 通常会作为依赖项被自动安装。这意味着在使用 yfinance 时，你可以直接利用 pandas 提供的数据结构和功能来处理和分析数据。


导入所需的库：


```
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```


### 获取股票数据


使用 yfinance 库，我们可以轻松下载股票数据。


我们通常使用 yf.download() 函数从雅虎财经获取某个股票的历史数据。

茅台的股票代码为 600519.SS，其中 **.SS** 是上海证券交易所的后缀。


使用 yfinance 获取股票数据：


## 实例


```python
import yfinance as yf

# 获取茅台（600519.SS）的股票数据，日期范围从 2020-01-01 到 2021-01-01
stock_data = yf.download('600519.SS', start='2020-01-01', end='2021-01-01')

# 查看数据的前几行
print(stock_data.head())
```


输出数据如下所示：


![](https://www.runoob.com/wp-content/uploads/2024/12/da9d70773fcaf98395d38975aa92d215.png)


返回的数据包含以下列：


- `Open`：开盘价
- `High`：最高价
- `Low`：最低价
- `Close`：收盘价
- `Adj Close`：调整后的收盘价（考虑了股息、拆股等因素）
- `Volume`：成交量


yf.download() 函数会返回一个 pandas.DataFrame，其中包含了指定股票的历史数据：


## 实例


```python
import yfinance as yf

# 获取茅台股票（600519.SS）的数据
stock_data = yf.download('600519.SS', start='2020-01-01', end='2021-01-01')

# 检查数据类型
print(type(stock_data))  # 应该输出 <class 'pandas.core.frame.DataFrame'>
```


输出为：


```
[*********************100%%**********************]  1 of 1 completed
<class 'pandas.core.frame.DataFrame'>
```


---


## 数据清洗与处理

在分析股票数据时，我们通常需要做一些数据清洗和处理。

常见的步骤包括填充缺失值、删除无关列、数据类型转换等。


在一些版本的 yfinance 中，可以自动引入了 pandas，不需要再引入，所以在使用 yfinance 时，你可以直接利用 pandas 提供的数据结构和功能来处理和分析数据。


检查缺失值并填充:


## 实例


```python
import yfinance as yf

# 获取茅台（600519.SS）的股票数据，日期范围从 2020-01-01 到 2021-01-01
stock_data = yf.download('600519.SS', start='2020-01-01', end='2021-01-01')

# 检查缺失值
print(stock_data.isnull().sum())

# 使用前向填充替换缺失值
stock_data.ffill(inplace=True)

# 或者使用后向填充
# stock_data.bfill(inplace=True)

# 检查缺失值是否已经处理
print(stock_data.isnull().sum())
```


输出结果如下所示：


```
[*********************100%%**********************]  1 of 1 completed
Open         0
High         0
Low          0
Close        0
Adj Close    0
Volume       0
dtype: int64
Open         0
High         0
Low          0
Close        0
Adj Close    0
Volume       0
```


删除无关列：


## 实例


```python
import yfinance as yf

# 获取茅台（600519.SS）的股票数据，日期范围从 2020-01-01 到 2021-01-01
stock_data = yf.download('600519.SS', start='2020-01-01', end='2021-01-01')

# 删除"Volume"和"Adj Close"列
stock_data_cleaned = stock_data.drop(columns=['Adj Close', 'Volume'])
print(stock_data_cleaned.head())
```


输出结果如下所示：


![](https://www.runoob.com/wp-content/uploads/2024/12/d3a6e25a1d384daf2dcd28904954f6cb.png)


---


## 数据可视化：绘制股票价格曲线

使用 matplotlib 或 seaborn，我们可以对股票数据进行可视化，帮助我们识别趋势和波动。


绘制收盘价的时间序列图:


## 实例


```python
import yfinance as yf
import matplotlib.pyplot as plt
# 获取茅台（600519.SS）的股票数据，日期范围从 2020-01-01 到 2021-01-01
stock_data = yf.download('600519.SS', start='2020-01-01', end='2021-01-01')

# 删除"Volume"和"Adj Close"列
stock_data_cleaned = stock_data.drop(columns=['Adj Close', 'Volume'])

# 绘制茅台收盘价曲线
plt.figure(figsize=(10, 6))
plt.plot(stock_data_cleaned['Close'], label='Close Price')
plt.title('Maotai Stock Price (2020)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Close Price (CNY)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
```


输出如下所示:


![](https://www.runoob.com/wp-content/uploads/2024/12/pandas-mt-2020.png)

---


## 计算股票的技术指标

在股票分析中，技术指标（如移动平均线、相对强弱指数 RSI 等）经常被使用来辅助决策，pandas 可以帮助我们计算这些指标。


### 1、移动平均线（SMA）


简单移动平均线（SMA）是最常用的技术指标之一，表示过去 N 天的平均收盘价。


## 实例


```python
import yfinance as yf
import matplotlib.pyplot as plt
# 获取茅台（600519.SS）的股票数据，日期范围从 2020-01-01 到 2021-01-01
stock_data = yf.download('600519.SS', start='2020-01-01', end='2021-01-01')

# 删除"Volume"和"Adj Close"列
stock_data_cleaned = stock_data.drop(columns=['Adj Close', 'Volume'])

# 计算 50 日和 200 日的移动平均线
stock_data_cleaned['SMA_50'] = stock_data_cleaned['Close'].rolling(window=50).mean()
stock_data_cleaned['SMA_200'] = stock_data_cleaned['Close'].rolling(window=200).mean()

# 绘制收盘价和移动平均线
plt.figure(figsize=(12, 6))
plt.plot(stock_data_cleaned['Close'], label='Close Price')
plt.plot(stock_data_cleaned['SMA_50'], label='50-Day SMA')
plt.plot(stock_data_cleaned['SMA_200'], label='200-Day SMA')
plt.title('Maotai Stock Price with Moving Averages', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (CNY)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
```


输出如下所示:


![](https://www.runoob.com/wp-content/uploads/2024/12/pandas-mt-2020-2.png)


### 2、相对强弱指数（RSI）

RSI 是用来评估股票是否被过度买入或卖出的技术指标，一般来说，RSI 大于 70 表示过度买入，小于 30 表示过度卖出。


## 实例


```python
import yfinance as yf
import matplotlib.pyplot as plt
# 获取茅台（600519.SS）的股票数据，日期范围从 2020-01-01 到 2021-01-01
stock_data = yf.download('600519.SS', start='2020-01-01', end='2021-01-01')

# 删除"Volume"和"Adj Close"列
stock_data_cleaned = stock_data.drop(columns=['Adj Close', 'Volume'])

# 计算 RSI 指标
delta = stock_data_cleaned['Close'].diff(1)
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)

# 计算平均收益和损失
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()

# 计算相对强弱指数 RSI
rs = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))

# 添加 RSI 到数据中
stock_data_cleaned['RSI'] = rsi

# 绘制 RSI 曲线
plt.figure(figsize=(12, 6))
plt.plot(stock_data_cleaned['RSI'], label='RSI')
plt.axhline(y=70, color='r', linestyle='--', label='Overbought (70)')
plt.axhline(y=30, color='g', linestyle='--', label='Oversold (30)')
plt.title('RSI Indicator for Maotai Stock', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('RSI', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
```


输出如下所示:


![](https://www.runoob.com/wp-content/uploads/2024/12/pandas-mt-2020-3.png)

---


## 股票数据分析的应用

在实际股票数据分析中，可以使用 Pandas 进行以下常见操作：


### 1、日收益率与累计收益率

计算股票的日收益率和累计收益率有助于评估其长期表现。


## 实例


```python
import yfinance as yf
import matplotlib.pyplot as plt
# 获取茅台（600519.SS）的股票数据，日期范围从 2020-01-01 到 2021-01-01
stock_data = yf.download('600519.SS', start='2020-01-01', end='2021-01-01')

# 删除"Volume"和"Adj Close"列
stock_data_cleaned = stock_data.drop(columns=['Adj Close', 'Volume'])

# 计算日收益率
stock_data_cleaned['Daily_Return'] = stock_data_cleaned['Close'].pct_change()

# 计算累计收益率
stock_data_cleaned['Cumulative_Return'] = (1 + stock_data_cleaned['Daily_Return']).cumprod()

# 绘制累计收益率
plt.figure(figsize=(10, 6))
plt.plot(stock_data_cleaned['Cumulative_Return'], label='Cumulative Return')
plt.title('Cumulative Return of Maotai Stock (2020)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Cumulative Return', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
```


输出如下所示:


![](https://www.runoob.com/wp-content/uploads/2024/12/pandas-mt-2020-4.png)


### 2、股票的波动率

波动率是衡量股票价格波动的一个指标。

通常，我们可以使用收益率的标准差来衡量股票的波动率。


## 实例


```python
import yfinance as yf
import matplotlib.pyplot as plt
# 获取茅台（600519.SS）的股票数据，日期范围从 2020-01-01 到 2021-01-01
stock_data = yf.download('600519.SS', start='2020-01-01', end='2021-01-01')

# 删除"Volume"和"Adj Close"列
stock_data_cleaned = stock_data.drop(columns=['Adj Close', 'Volume'])

# 计算日收益率
stock_data_cleaned['Daily_Return'] = stock_data_cleaned['Close'].pct_change()

# 计算累计收益率
stock_data_cleaned['Cumulative_Return'] = (1 + stock_data_cleaned['Daily_Return']).cumprod()

# 计算日收益率的标准差（波动率）
volatility = stock_data_cleaned['Daily_Return'].std()

# 显示波动率
print(f"Daily Volatility: {volatility:.4f}")
```


输出如下所示:


```
[*********************100%%**********************]  1 of 1 completed
Daily Volatility: 0.0181
```









	  AI 思考中...





			** [Pandas 性能优化](https://www.runoob.com/pandas-optimization.html)
			[Pandas Series API 手册](https://www.runoob.com/pandas-series-api-reference.html) **













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