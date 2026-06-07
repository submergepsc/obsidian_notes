# Python 量化数据可视化

- Source: https://www.runoob.com/python-qt/qt-views.html

Python 量化数据可视化可以使用 **Matplotlib** 和 **Seaborn** 库。


安装 Matplotlib 和 Seaborn 可以在终端或命令提示符中运行：


```
pip install matplotlib seaborn
```


Matplotlib 详细内容可以参考： [Matplotlib 教程](https://www.runoob.com/../matplotlib/matplotlib-tutorial.html)


本章节主要为大家介绍 Seaborn 库的使用。

---


## Seaborn 库

Seaborn 是一个基于 Matplotlib 的数据可视化库，专注于统计图形的绘制。


Seaborn 提供了一些高层次的界面和颜色主题，使得在 Python 中创建漂亮的统计图表变得更加容易。


Seaborn 的目标是使数据可视化变得更简单，同时也让图表更具有吸引力。


### 1. 统计图形的简单创建


Seaborn 提供了一系列内置的绘图函数，可以轻松地创建各种统计图形，如散点图、直方图、箱线图等。


## 实例


```python
import seaborn as sns
import matplotlib.pyplot as plt

# 创建散点图
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris)
plt.show()
```


### 2. 内置颜色主题


Seaborn 提供了内置的颜色主题，可以让你轻松地改变图表的外观，使其更具有吸引力。


```
# 使用 Seaborn 颜色主题
sns.set(style="whitegrid")
```


### 3. 数据集可视化

Seaborn 包含一些内置的数据集，可以直接用于绘图，例如，tips 和 flights 数据集。


```
# 使用内置数据集
tips = sns.load_dataset("tips")
```


### 4. 分类数据的可视化

Seaborn 对于分类数据的处理非常方便，可以轻松地创建分组柱状图、箱线图等。


```
# 创建分组柱状图
sns.barplot(x="day", y="total_bill", hue="sex", data=tips)
```


### 5. 矩阵数据的可视化

Seaborn 提供了一些专门用于可视化矩阵数据的函数，例如热力图（heatmap）。


```
# 创建热力图
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
```


### 6. 分面绘图

Seaborn 支持分面绘图，可以根据数据的子集创建多个小图，以更全面地展示数据。


```
# 分面绘图
sns.relplot(x="total_bill", y="tip", hue="day", col="time", data=tips)
```


Seaborn 提供了大量的图形选项和参数，以满足不同类型的数据可视化需求。

总体而言，Seaborn 是一个功能强大而易用的库，适用于初学者和专业数据科学家，能够帮助用户更轻松地创建具有吸引力的统计图表。如果你已经熟悉 Matplotlib，Seaborn 是一个很好的补充，可以让你更高效地进行数据可视化。


---


## 实例

接下来吗我们使用 Python 进行一个简单的量化实例，你可以结合 yfinance 获取贵州茅台（600519.SS）的股票数据，然后使用 seaborn 进行数据可视化。


以下是一个简单的例子，演示如何下载茅台股票数据，并使用 seaborn 绘制股票的收盘价走势图：


## 实例


```python
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# 获取贵州茅台的股票数据
maotai_data = yf.download("600519.SS", start="2020-01-01", end="2023-01-01")

# 选取收盘价数据
closing_prices = maotai_data['Close']

# 使用 seaborn 绘制走势图
plt.figure(figsize=(12, 6))
sns.lineplot(x=closing_prices.index, y=closing_prices.values, label='Maotai Closing Prices')
plt.title('Maotai Stock Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price (CNY)')
plt.legend()
plt.show()
```


执行以上代码，输出结果为：


![](https://www.runoob.com/wp-content/uploads/2023/12/mt-qt-4.png)









	  AI 思考中...





			** [Python 获取金融数据](https://www.runoob.com/qt-get-data.html)
			[Python 量化金融基础](https://www.runoob.com/qt-ffk.html) **













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