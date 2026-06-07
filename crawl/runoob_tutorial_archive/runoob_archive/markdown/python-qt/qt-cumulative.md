# Python 量化回测

- Source: https://www.runoob.com/python-qt/qt-cumulative.html

回测是在历史市场数据上模拟和评估一个交易策略的过程。


在量化金融和算法交易中，回测是一个关键的步骤，用于评估交易策略在过去市场行为上的表现。


通过回测，交易者可以了解其策略在不同市场条件下的表现，并进行优化和改进。


回测通常包括以下步骤：


- **定义交易策略：** 确定何时买入、卖出或持仓的规则。这可能涉及到技术指标、移动平均线策略、趋势跟踪、套利等各种策略。
- **获取历史数据：** 获取过去的市场数据，包括股票、期货、外汇等金融工具的价格、成交量等信息。
- **模拟交易：** 根据定义的策略，模拟在历史数据上执行交易。这包括确定何时买入或卖出，并计算每次交易的收益和损失。
- **计算绩效指标：** 根据回测结果，计算各种绩效指标，如年化收益率、最大回撤、夏普比率等，以评估策略的表现。
- **优化策略：** 如果回测结果不理想，交易者可以进行策略的优化，调整参数或修改规则，然后重新进行回测。
- **未来性检验：** 回测的一个关键问题是防止未来数据的泄漏。未来性检验是确保在设计和评估策略时只使用历史数据的一部分，以模拟实际交易中只能使用已知信息的情况。


接下来，这是一个简单的移动平均交叉策略的回测实例代码：


## 实例


```python
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 获取股票数据
symbol = "600519.SS"  # 茅台股票代码
start_date = "2019-01-01"
end_date = "2021-01-01"

data = yf.download(symbol, start=start_date, end=end_date)

# 计算移动平均
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

# 初始化交叉信号列
data['Signal'] = 0

# 计算交叉信号
data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1
data.loc[data['SMA_50'] < data['SMA_200'], 'Signal'] = -1

# 计算每日收益率
data['Daily_Return'] = data['Close'].pct_change()

# 计算策略信号的收益率（shift(1) 是为了避免未来数据的偏差）
data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']

# 计算累计收益
data['Cumulative_Return'] = (1 + data['Strategy_Return']).cumprod()

# 绘制累计收益曲线
plt.figure(figsize=(10, 6))
plt.plot(data['Cumulative_Return'], label='Strategy Cumulative Return', color='b')
plt.plot(data['Close'] / data['Close'].iloc[0], label='Stock Cumulative Return', color='g')
plt.title("Cumulative Return of Strategy vs. Stock")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()
plt.show()
```


执行以上代码，输出结果如下：


![](https://www.runoob.com/wp-content/uploads/2023/12/2671386a0770e90bf3a1ab20f4fc6d1a.png)









	  AI 思考中...





			** [Anaconda 教程](https://www.runoob.com/anaconda-tutorial.html)
			[Python 量化股票 K 线图](https://www.runoob.com/python-stock-line-chart.html) **













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