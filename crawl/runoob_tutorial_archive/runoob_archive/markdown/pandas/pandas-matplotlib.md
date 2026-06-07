# Pandas 数据可视化

- Source: https://www.runoob.com/pandas/pandas-matplotlib.html

数据可视化是数据分析中的重要环节，它帮助我们更好地理解和解释数据的模式、趋势和关系。

通过图形、图表等形式，数据可视化将复杂的数字和统计信息转化为易于理解的图像，从而便于做出决策。

Pandas 提供了与 [Matplotlib](https://www.runoob.com/../matplotlib/matplotlib-tutorial.html) 和 [Seaborn](https://www.runoob.com/../matplotlib/seaborn-tutorial.html) 等可视化库的集成，使得数据的可视化变得简单而高效。


在 Pandas 中，数据可视化功能主要通过 `DataFrame.plot()` 和 `Series.plot()` 方法实现，这些方法实际上是对 Matplotlib 库的封装，简化了图表的绘制过程。


| 图表类型 | 描述 | 方法 |
| --- | --- | --- |
| 折线图 | 展示数据随时间或其他连续变量的变化趋势 | df.plot(kind='line') |
| 柱状图 | 比较不同类别的数据 | df.plot(kind='bar') |
| 水平柱状图 | 比较不同类别的数据，但柱子水平排列 | df.plot(kind='barh') |
| 直方图 | 显示数据的分布 | df.plot(kind='hist') |
| 散点图 | 展示两个数值型变量之间的关系 | df.plot(kind='scatter', x='col1', y='col2') |
| 箱线图 | 显示数据分布，包括中位数、四分位数等 | df.plot(kind='box') |
| 密度图 | 展示数据的密度分布 | df.plot(kind='kde') |
| 饼图 | 显示不同部分在整体中的占比 | df.plot(kind='pie') |
| 区域图 | 展示数据的累计数值 | df.plot(kind='area') |


Pandas 数据可视化的基本功能和方法可以满足大多数日常数据可视化的需求，但若要实现更复杂的可视化，可以结合 Matplotlib 和 Seaborn 使用，进行更精细的图表定制。


---

## 一、Pandas 数据可视化概述


Pandas 提供的 `plot()` 方法可以轻松地绘制不同类型的图表，包括折线图、柱状图、直方图、散点图等。`plot()` 方法有很多参数，可以定制图表的样式、颜色、标签等。


### 1. 基本的 plot() 方法


| 参数 | 说明 |
| --- | --- |
| kind | 图表类型，支持 'line', 'bar', 'barh', 'hist', 'box', 'kde', 'density', 'area', 'pie' 等类型 |
| x | 设置 x 轴的数据列 |
| y | 设置 y 轴的数据列 |
| title | 图表的标题 |
| xlabel | x 轴的标签 |
| ylabel | y 轴的标签 |
| color | 设置图表的颜色 |
| figsize | 设置图表的大小（宽, 高） |
| legend | 是否显示图例 |


### 2. 常用图表类型


| 图表类型 | 描述 | 常用用法 |
| --- | --- | --- |
| 折线图 | 用于显示随时间变化的数据趋势 | df.plot(kind='line') |
| 柱状图 | 用于显示类别之间的比较数据 | df.plot(kind='bar') |
| 水平柱状图 | 与柱状图类似，但柱子是水平的 | df.plot(kind='barh') |
| 直方图 | 用于显示数据的分布（频率分布） | df.plot(kind='hist') |
| 散点图 | 用于显示两个数值变量之间的关系 | df.plot(kind='scatter', x='col1', y='col2') |
| 箱线图 | 用于显示数据的分布、异常值及四分位数 | df.plot(kind='box') |
| 密度图 | 用于显示数据的密度分布 | df.plot(kind='kde') |
| 饼图 | 用于显示各部分占总体的比例 | df.plot(kind='pie') |
| 区域图 | 用于显示累计数值的图表（类似于折线图，但填充了颜色） | df.plot(kind='area') |


---

## 二、数据可视化示例


### 1. 折线图 (Line Plot)


折线图通常用于展示数据随时间的变化趋势。


## 实例


```python
import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {'Year': [2015, 2016, 2017, 2018, 2019, 2020],
        'Sales': [100, 150, 200, 250, 300, 350]}
df = pd.DataFrame(data)

# 绘制折线图
df.plot(kind='line', x='Year', y='Sales', title='Sales Over Years', xlabel='Year', ylabel='Sales', figsize=(10, 6))
plt.show()
```


**输出：**


![](https://www.runoob.com/wp-content/uploads/2024/12/pd-views-1.png)


### 2. 柱状图 (Bar Chart)


柱状图用于展示不同类别之间的比较，尤其适用于离散数据。


## 实例


```python
import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 15, 7, 12]}
df = pd.DataFrame(data)

# 绘制柱状图
df.plot(kind='bar', x='Category', y='Value', title='Category Values', xlabel='Category', ylabel='Value', figsize=(8, 5))
plt.show()
```


**输出：**


![](https://www.runoob.com/wp-content/uploads/2024/12/pd-views-2.png)


### 3. 散点图 (Scatter Plot)


散点图用于展示两个数值变量之间的关系。


## 实例


```python
import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {'Height': [150, 160, 170, 180, 190],
        'Weight': [50, 60, 70, 80, 90]}
df = pd.DataFrame(data)

# 绘制散点图
df.plot(kind='scatter', x='Height', y='Weight', title='Height vs Weight', xlabel='Height (cm)', ylabel='Weight (kg)', figsize=(8, 5))
plt.show()
```


**输出：**


![](https://www.runoob.com/wp-content/uploads/2024/12/pd-views-3.png)


### 4. 直方图 (Histogram)


直方图用于显示数据的分布，特别是用于描述数据的频率分布。


## 实例


```python
import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {'Scores': [55, 70, 85, 90, 60, 75, 80, 95, 100, 65]}
df = pd.DataFrame(data)

# 绘制直方图
df.plot(kind='hist', y='Scores', bins=5, title='Scores Distribution', xlabel='Scores', figsize=(8, 5))
plt.show()
```


**输出：**


![](https://www.runoob.com/wp-content/uploads/2024/12/pd-views-4.png)


### 5. 箱线图 (Box Plot)


箱线图用于展示数据的分布情况，包括中位数、四分位数以及异常值。


## 实例


```python
import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {'Scores': [55, 70, 85, 90, 60, 75, 80, 95, 100, 65]}
df = pd.DataFrame(data)

# 绘制箱线图
df.plot(kind='box', title='Scores Boxplot', ylabel='Scores', figsize=(8, 5))
plt.show()
```


**输出：**


![](https://www.runoob.com/wp-content/uploads/2024/12/pd-views-5.png)


### 6. 饼图 (Pie Chart)


饼图用于展示各部分占总体的比例。


## 实例


```python
import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 15, 7, 12]}
df = pd.DataFrame(data)

# 绘制饼图
df.plot(kind='pie', y='Value', labels=df['Category'], autopct='%1.1f%%', title='Category Proportions', figsize=(8, 5))
plt.show()
```


**输出：**


![](https://www.runoob.com/wp-content/uploads/2024/12/pd-views-6.png)


---

## 三、Seaborn 可视化


Seaborn 是基于 Matplotlib 的高级数据可视化库，提供了更漂亮、更易用的图表和更丰富的统计图表类型。

在 Pandas 中，可以直接与 Seaborn 配合使用。

**热力图（Heatmap）:**


## 实例


```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 示例数据
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# 绘制热力图
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
```


**输出：**


![](https://www.runoob.com/wp-content/uploads/2024/12/pd-views-7.png)


**数据集中所有数值特征之间的散点图矩阵**:


## 实例


```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 示例数据
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

sns.pairplot(df)
plt.show()
```


**输出：**


![](https://www.runoob.com/wp-content/uploads/2024/12/pd-views-8.png)


---

## 四、Matplotlib 高级自定义


除了使用 Pandas 提供的 `plot()` 方法外，Matplotlib 还可以提供更灵活的自定义功能，例如添加标题、标签、设置图表风格、调整坐标轴等。


## 实例


```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 示例数据
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Sales': [100, 150, 200, 250, 300]}
df = pd.DataFrame(data)

# 绘制折线图
plt.plot(df['Year'], df['Sales'], color='blue', marker='o')

# 自定义
plt.title('Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)

# 显示
plt.show()
```


**输出：**


![](https://www.runoob.com/wp-content/uploads/2024/12/pd-views-9.png)








	  AI 思考中...





			** [Pandas 数据排序与聚合](https://www.runoob.com/pandas-sorting.html)
			[Pandas 高级功能](https://www.runoob.com/pandas-advanced.html) **













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