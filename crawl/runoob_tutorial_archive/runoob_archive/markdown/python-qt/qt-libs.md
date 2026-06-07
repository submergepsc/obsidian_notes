# Python 量化金融库

- Source: https://www.runoob.com/python-qt/qt-libs.html

学习一些量化金融领域常用的 Python 库，比如：


- **zipline**: 用于回测和实施交易算法的库，安装命令：**pip install zipline**。
- **Quantlib**: 用于定价金融工具和执行金融计算的库，安装命令：**pip install Quantlib**。
- **TA-Lib**: 用于技术分析的库，安装命令：**pip install TA-Lib**。
- **pyfolio**: 是一个用于评估投资组合性能的库，它可以与zipline等回测工具集成，提供分析投资组合收益、风险等方面的工具，安装命令：**pip install pyfolio**。
- **statsmodels**: 是一个用于估计统计模型的库，包括线性回归、时间序列分析等。在量化金融中，它可用于建立和测试交易策略，安装命令：**pip install statsmodels**。

---


## zipline


zipline 是一个用于量化金融研究和算法交易的开源框架。

它是由 Quantopian 公司开发的，旨在为研究员和开发者提供一个方便的工具，用于构建、测试和执行量化交易策略。


在 zipline 的使用之前，请确保你已经安装了该库，你可以使用以下命令进行安装：


```
conda install -c conda-forge zipline
```


这里我们使用 [Anaconda](https://www.runoob.com/anaconda-tutorial.html) 来安装 zipline，免得后面出现奇奇怪怪的问题。


接下来我们登录 [quandl](https://data.nasdaq.com/account/api) 官网，进行注册，获得 api key：[https://data.nasdaq.com/account/profile](https://data.nasdaq.com/account/profile)。


然后设置 api key，并下载数据包，具体命令如下：


```
set QUANDL_API_KEY=your_key
```


macOS 系统使用以下命令：


```
export QUANDL_API_KEY=your_key-zZQN
```


下载数据包：


```
zipline ingest -b quandl
```


查询数据包：


```
# zipline bundles
csvdir <no ingestions>
quandl 2023-12-09 06:02:03.178299
quandl 2023-12-09 05:59:04.273082
quandl 2023-12-09 05:54:57.277732
quandl 2023-12-09 05:52:15.532504
quandl 2023-12-09 03:32:03.853032
quantopian-quandl <no ingestions>
```


现在，让我们使用 zipline 进行一个简单的测试。


以下是是一个简单的 Zipline 策略脚本，用于进行股票交易的回测：


## 实例


```python
from zipline.api import order, record, symbol

def initialize(context):
    pass

def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), 'price'))
```


以上是一个简单的策略在每个交易日都以当前价格买入 10 股苹果公司的股票，并记录每个交易日的 AAPL 当前价格。


- `order(symbol('AAPL'), 10)`：这一行表示在每个交易日，以当前价格购买 10 股苹果公司（AAPL）的股票。`symbol('AAPL')` 用于获取 AAPL 的股票符号。
- `record(AAPL=data.current(symbol('AAPL'), 'price'))`：这一行表示记录每个交易日 AAPL 的当前价格。`data.current(symbol('AAPL'), 'price')` 用于获取当前 AAPL 的股价。


然后执行以下命令：


```
# zipline run -f my_strategy.py --start 2016-1-1 --end 2018-1-1 -o buyapple_out.pickle --no-benchmark
Simulated 503 trading days
 first open: 2016-01-04 14:30:00+00:00
 last close: 2017-12-29 21:00:00+00:00
```


执行成功后，会生成 **buyapple_out.pickle** 文件，我们可以使用 **pickle** 模块读取它。


** 命令说明：**


- **`zipline run`：** 启动 Zipline 运行回测。
- **`-f my_strategy.py`：** 指定策略文件。在这个例子中，`my_strategy.py` 是包含您编写的策略的 Python 文件。
- **`--start 2016-1-1` 和 `--end 2018-1-1`：** 指定回测的起始和结束日期。这个例子中回测的时间范围是从 2016 年 1 月 1 日到 2018 年 1 月 1 日。
- **`-o buyapple_out.pickle`：** 指定输出文件的名称。在这个例子中，回测的结果将被保存为 `buyapple_out.pickle` 文件。这个文件包含了回测的各种输出信息，例如交易记录、性能指标等。
- **`--no-benchmark`：** 禁用基准（benchmark）。在回测中，有时会使用某个基准来比较策略的表现。使用 `--no-benchmark` 选项表示不使用任何基准。


pickle 模块用于序列化和反序列化对象，可以方便地将对象保存到文件或从文件中加载对象。


以下演示如何读取 buyapple_out.pickle 文件中的内容：


## 实例


```python
import pickle

# 指定pickle文件路径
pickle_file_path = 'buyapple_out.pickle'

# 读取pickle文件
with open(pickle_file_path, 'rb') as file:
    buyapple_out_data = pickle.load(file)

# 打印读取的数据
print(buyapple_out_data)
```


输出内容如下所示：


```
period_open              period_close  short_value          pnl  long_exposure  ...  max_leverage  excess_return treasury_period_return trading_days  period_label
2016-01-04 21:00:00+00:00 2016-01-04 14:31:00+00:00 2016-01-04 21:00:00+00:00          0.0      0.00000            0.0  ...      0.000000            0.0                    0.0            1       2016-01
2016-01-05 21:00:00+00:00 2016-01-05 14:31:00+00:00 2016-01-05 21:00:00+00:00
```









	  AI 思考中...





			** [Python 量化金融基础](https://www.runoob.com/qt-ffk.html)
			[Anaconda 教程](https://www.runoob.com/anaconda-tutorial.html) **













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