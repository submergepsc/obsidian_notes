# Python 量化股票 K 线图

- Source: https://www.runoob.com/python-qt/python-stock-line-chart.html

我们可以通过 [Python pyecharts 模块](https://www.runoob.com/../python3/python-pyecharts.html)来绘制股票 K 线图。


pyecharts 是一个基于 ECharts 的 Python 数据可视化库，它允许用户使用 Python 语言生成各种类型的交互式图表和数据可视化。


Python pyecharts 模块内容查看：[Python pyecharts 模块](https://www.runoob.com/../python3/python-pyecharts.html)。


在 pyecharts 中，可以使用 K 线图（Kline）来展示股票走势，K 线图主要用于展示金融数据，如股票的开盘价、收盘价、最高价、最低价等信息。


首先，确保你已经安装了 pyecharts：


```
pip install pyecharts
```


我们使用雅虎财经（Yahoo Finance）的数据获取近一年的股票数据，我们可以使用 yfinance 库：


```
pip install yfinance
```


### K 线图使用

导入相关模块：


```
from pyecharts import options as opts
from pyecharts.charts import Kline
```


准备数据：


Kline 图的数据通常是一个包含开盘价、收盘价、最高价、最低价的二维数组，例如：


```
data = [
    [2320.26, 2320.26, 2287.3, 2362.94],
    [2300, 2291.3, 2288.26, 2308.38],
    # ...
]
```


配置 Kline 图：


```
kline = (
    Kline()
    .add_xaxis(xaxis_data=["2017-10-24", "2017-10-25", "2017-10-26", "2017-10-27"])
    .add_yaxis(series_name="Kline", y_axis=data)
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(is_scale=True),
        yaxis_opts=opts.AxisOpts(is_scale=True),
        title_opts=opts.TitleOpts(title="Kline 示例"),
    )
)
```


在这里，使用了 add_xaxis 设置 x 轴的数据，使用 add_yaxis 添加 Kline 数据系列，set_global_opts 则用于设置全局配置，包括标题等。


渲染图表：


```
kline.render("kline_chart.html")
```


将 Kline 图渲染到 HTML 文件中。


## 实例


```python
from pyecharts import options as opts
from pyecharts.charts import Kline

# 准备数据
data = [
    [2320.26, 2320.26, 2287.3, 2362.94],
    [2300, 2291.3, 2288.26, 2308.38],
    [2295.35, 2346.5, 2295.35, 2345.92],
    [2347.22, 2358.98, 2337.35, 2363.8],
    # ... more data
]

# 配置 Kline 图
kline = (
    Kline()
    .add_xaxis(xaxis_data=["2017-10-24", "2017-10-25", "2017-10-26", "2017-10-27"])
    .add_yaxis(series_name="Kline", y_axis=data)
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(is_scale=True),
        yaxis_opts=opts.AxisOpts(is_scale=True),
        title_opts=opts.TitleOpts(title="Kline 示例"),
    )
)

# 渲染图表
kline.render("kline_chart.html")
```


**说明：**


- 我们有一个名为 `data` 的数据集，其中包含每天的金融数据，包括开盘价、收盘价、最高价和最低价。
- 我们创建了一个 `Kline` 实例，使用 `add_xaxis` 设置 x 轴数据（在这种情况下是日期），使用 `add_yaxis` 添加 Kline 数据系列。
- 使用 `set_global_opts` 设置全局选项，例如 x 轴和 y 轴的缩放，以及图表标题。
- 最后，我们使用 `render` 将图表渲染到一个 HTML 文件中。

当前目录会生成一个 kline_chart.html 文件，打开该文件图表显示如下：


![](https://www.runoob.com/wp-content/uploads/2023/12/b22dbf03f097c87aebfa8b4aaeb2ef99.png)


下面是一个实例代码，演示如何获取贵州茅台的股票数据并生成 K 线图：


## 实例


```python
import yfinance as yf
from pyecharts import options as opts
from pyecharts.charts import Kline

# 获取贵州茅台近三年的股票数据
symbol = '600519.SS'  # 600519.SS 为贵州茅台的股票代码
start_date = '2020-01-01'
end_date = '2022-12-31'

stock_data = yf.download(symbol, start=start_date, end=end_date)

# 提取 K 线图所需的数据格式
kline_data = []
for index, row in stock_data.iterrows():
    kline_data.append([row['Open'], row['Close'], row['Low'], row['High']])

# 配置 Kline 图
kline = (
    Kline()
    .add_xaxis(xaxis_data=stock_data.index.strftime('%Y-%m-%d').tolist())
    .add_yaxis(series_name="Kline", y_axis=kline_data)
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(is_scale=True),
        yaxis_opts=opts.AxisOpts(is_scale=True),
        title_opts=opts.TitleOpts(title="贵州茅台 Kline 图示例"),
        datazoom_opts=[opts.DataZoomOpts()],
        toolbox_opts=opts.ToolboxOpts(
            feature={
                "dataZoom": {"yAxisIndex": "none"},
                "restore": {},
                "saveAsImage": {},
            }
        ),
    )
)

# 渲染图表
kline.render("maotai_kline_chart.html")
```


当前目录会生成一个 maotai_kline_chart.html 文件，打开该文件图表显示如下：


![](https://www.runoob.com/wp-content/uploads/2023/12/dc4e151b29cfecb873367a5e4aa4797d.png")


### 绘制曲线图


我们也可以使用 pyecharts 绘制股票的简单曲线图，以茅台（600519.SH）为例：


## 实例


```python
import yfinance as yf
from pyecharts import options as opts
from pyecharts.charts import Line
from datetime import datetime, timedelta

# 设置茅台股票代码
stock_code = "600519.SS"

# 获取当前日期
end_date = datetime.now().strftime('%Y-%m-%d')

# 计算三年前的日期
start_date = (datetime.now() - timedelta(days=3 * 365)).strftime('%Y-%m-%d')

# 使用yfinance获取股票数据
df = yf.download(stock_code, start=start_date, end=end_date)

# 提取数据中的日期和收盘价
dates = df.index.strftime('%Y-%m-%d').tolist()
closing_prices = df['Close'].tolist()

# 创建 Line 图表
line_chart = Line()
line_chart.add_xaxis(xaxis_data=dates)
line_chart.add_yaxis(series_name="茅台股价走势",
                     y_axis=closing_prices,
                     markline_opts=opts.MarkLineOpts(
                         data=[opts.MarkLineItem(type_="average", name="平均值")]
                     )
                     )
line_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="茅台股价走势图（近三年）"),
    xaxis_opts=opts.AxisOpts(type_="category"),
    yaxis_opts=opts.AxisOpts(is_scale=True),
    datazoom_opts=[opts.DataZoomOpts(pos_bottom="-2%")],
)

# 渲染图表
line_chart.render("maotai_stock_trend_chart.html")
```


当前目录会生成一个 maotai_stock_trend_chart.html 文件，打开该文件图表显示如下：


![](https://www.runoob.com/wp-content/uploads/2023/12/cc2729f42bb8513ed9a515df068726222.png)


可以考虑添加一些图表的工具，例如数据缩放、数据视图等，以提升用户的交互体验。

以下是优化后的代码，添加了数据缩放和数据视图的功能：


## 实例


```python
import yfinance as yf
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode
from datetime import datetime, timedelta

# 设置茅台股票代码
stock_code = "600519.SS"

# 获取当前日期
end_date = datetime.now().strftime('%Y-%m-%d')

# 计算三年前的日期
start_date = (datetime.now() - timedelta(days=3 * 365)).strftime('%Y-%m-%d')

# 使用yfinance获取股票数据
df = yf.download(stock_code, start=start_date, end=end_date)

# 提取数据中的日期和收盘价
dates = df.index.strftime('%Y-%m-%d').tolist()
closing_prices = df['Close'].tolist()

# 创建 Line 图表
line_chart = Line()
line_chart.add_xaxis(xaxis_data=dates)
line_chart.add_yaxis(series_name="茅台股价走势",
                     y_axis=closing_prices,
                     markline_opts=opts.MarkLineOpts(
                         data=[opts.MarkLineItem(type_="average", name="平均值")]
                     )
                     )
line_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="茅台股价走势图（近三年）"),
    xaxis_opts=opts.AxisOpts(type_="category"),
    yaxis_opts=opts.AxisOpts(is_scale=True),
    datazoom_opts=[
        opts.DataZoomOpts(
            pos_bottom="-2%",
            range_start=0,
            range_end=100,
            type_="inside"
        ),
        opts.DataZoomOpts(
            pos_bottom="-2%",
            range_start=0,
            range_end=100,
            type_="slider",
        ),
    ],
    toolbox_opts=opts.ToolboxOpts(
        feature={
            "dataZoom": {"yAxisIndex": "none"},
            "restore": {},
            "saveAsImage": {},
        }
    ),
)

# 渲染图表
line_chart.render("maotai_stock_trend_chart2.html")
```


当前目录会生成一个 maotai_stock_trend_chart2.html 文件，打开该文件图表显示如下：


![](https://www.runoob.com/wp-content/uploads/2023/12/a459367d52a739c4667fb0c1c21cc958.png)









	  AI 思考中...





			** [Python 量化回测](https://www.runoob.com/qt-cumulative.html)














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