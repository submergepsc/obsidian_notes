# Seaborn 教程

- Source: https://www.runoob.com/matplotlib/seaborn-tutorial.html

Seaborn 是一个建立在 Matplotlib 基础之上的 Python 数据可视化库，专注于绘制各种统计图形，以便更轻松地呈现和理解数据。

Seaborn 的设计目标是简化统计数据可视化的过程，提供高级接口和美观的默认主题，使得用户能够通过少量的代码实现复杂的图形。


Seaborn 提供了一些简单的高级接口，可以轻松地绘制各种统计图形，包括散点图、折线图、柱状图、热图等，而且具有良好的美学效果。


Seaborn 在设计时注重美观性，其默认主题和颜色调色板经过精心选择，使得绘图更加吸引人。


安装 Seaborn:


```
pip install seaborn
```


Seaborn 提供了多种内置主题和颜色调色板，可以通过设置来改变图形的外观。


## 实例


```python
import seaborn as sns

# 设置主题和颜色调色板
sns.set_theme(style="whitegrid", palette="pastel")
```


通过设置 sns.set_theme() 函数，可以选择不同的主题和模板，以下是 Seaborn 内置的一些主题和模板：


### 主题（Theme）


**darkgrid**（默认）：深色网格主题。


```
import seaborn as sns

# 设置为 darkgrid 主题
sns.set_theme(style="darkgrid")
```


**whitegrid**：浅色网格主题。


```
import seaborn as sns

# 设置为 whitegrid 主题
sns.set_theme(style="whitegrid")
```


**dark**：深色主题，没有网格。


```
import seaborn as sns

# 设置为 dark 主题
sns.set_theme(style="dark")
```


**white**：浅色主题，没有网格。


```
import seaborn as sns

# 设置为 white 主题
sns.set_theme(style="white")
```


**ticks**：深色主题，带有刻度标记。


```
import seaborn as sns

# 设置为 ticks 主题
sns.set_theme(style="ticks")
```


### 模板（Context）


**paper**：适用于小图，具有较小的标签和线条。


```
import seaborn as sns

# 设置为 paper 模板
sns.set_theme(context="paper")
```


**notebook**（默认）：适用于笔记本电脑和类似环境，具有中等大小的标签和线条。


```
import seaborn as sns

# 设置为 notebook 模板
sns.set_theme(context="notebook")
```


**talk**：适用于演讲幻灯片，具有大尺寸的标签和线条。


```
import seaborn as sns

# 设置为 talk 模板
sns.set_theme(context="talk")
```


**poster**：适用于海报，具有非常大的标签和线条。


```
import seaborn as sns

# 设置为 poster 模板
sns.set_theme(context="poster")
```


通过设置不同的主题和模板，可以调整 Seaborn 图形的大小、线条的粗细、颜色等属性，以适应不同的绘图场景。这些内置的主题和模板使得用户能够更轻松地创建美观且具有一致性的图形。


以下实例使用 Seaborn 和 Matplotlib 绘制了一个简单的柱状图，用于展示不同产品的销售情况：


## 实例


```python
import seaborn as sns
import matplotlib.pyplot as plt

# 设置主题和颜色调色板
sns.set_theme(style="darkgrid", palette="pastel")
# 示例数据
products = ["Product A", "Product B", "Product C", "Product D"]
sales = [120, 210, 150, 180]

# 创建柱状图
sns.barplot(x=products, y=sales)

# 添加标签和标题
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales by Category")

# 显示图表
plt.show()
```


结果如下图所示：


![](https://www.runoob.com/wp-content/uploads/2024/02/40073d5c93c16effe1e472047c8c0326.png)


---


## 绘图函数


Seaborn 提供了多个绘图函数，用于创建各种统计图形，以下是 Seaborn 主要的几个绘图函数及相应的实例：


### 1. 散点图 - sns.scatterplot()


用于绘制两个变量之间的散点图，可选择添加趋势线。


## 实例


```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# 绘制散点图
sns.scatterplot(x='A', y='B', data=df)
plt.show()
```


结果如下图所示：


![](https://www.runoob.com/wp-content/uploads/2024/02/Seaborn-1.png)


### 2. 折线图 - sns.lineplot()


用于绘制变量随着另一个变量变化的趋势线图。


## 实例


```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# 绘制折线图
sns.lineplot(x='X', y='Y', data=df)
plt.show()
```


结果如下图所示：


![](https://www.runoob.com/wp-content/uploads/2024/02/Seaborn-2.png)


### 3. 柱状图 - sns.barplot()

用于绘制变量的均值或其他聚合函数的柱状图。


## 实例


```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'Category': ['A', 'B', 'C'], 'Value': [3, 7, 5]}
df = pd.DataFrame(data)

# 绘制柱状图
sns.barplot(x='Category', y='Value', data=df)
plt.show()
```


结果如下图所示：


![](https://www.runoob.com/wp-content/uploads/2024/02/Seaborn-3.png)


### 4. 箱线图 - sns.boxplot()

用于绘制变量的分布情况，包括中位数、四分位数等。


## 实例


```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'], 'Value': [3, 7, 5, 9, 2, 6]}
df = pd.DataFrame(data)

# 绘制箱线图
sns.boxplot(x='Category', y='Value', data=df)
plt.show()
```


结果如下图所示：


![](https://www.runoob.com/wp-content/uploads/2024/02/Seaborn-4.png)


### 5. 热图 - sns.heatmap()

用于绘制矩阵数据的热图，通常用于展示相关性矩阵。


## 实例


```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)
# 创建一个相关性矩阵
correlation_matrix = df.corr()

# 使用热图可视化相关性矩阵
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()
```


结果如下图所示：


![](https://www.runoob.com/wp-content/uploads/2024/02/38fa14c44f0cc4f315a3dd4d5597d2b1_w.png)


### 6. 小提琴图 - sns.violinplot()


用于显示分布的形状和密度估计，结合了箱线图和核密度估计。


## 实例


```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'], 'Value': [3, 7, 5, 9, 2, 6]}
df = pd.DataFrame(data)

# 绘制小提琴图
sns.violinplot(x='Category', y='Value', data=df)
plt.show()
```


结果如下图所示：


![](https://www.runoob.com/wp-content/uploads/2024/02/Seaborn-6.png)

**

更多内容可以参考官网教程：[https://seaborn.pydata.org/tutorial.html](https://seaborn.pydata.org/tutorial.html)










	  AI 思考中...





			** [Matplotlib 中文显示](https://www.runoob.com/matplotlib-zh.html)














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