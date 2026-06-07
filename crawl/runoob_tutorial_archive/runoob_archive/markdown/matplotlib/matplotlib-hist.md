# Matplotlib 直方图

- Source: https://www.runoob.com/matplotlib/matplotlib-hist.html

我们可以使用 pyplot 中的 hist() 方法来绘制直方图。


hist() 方法是 Matplotlib 库中的 pyplot 子库中的一种用于绘制直方图的函数。


hist() 方法可以用于可视化数据的分布情况，例如观察数据的中心趋势、偏态和异常值等。


hist() 方法语法格式如下：


```
matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, **kwargs)
```


**参数说明：**


- `x`：表示要绘制直方图的数据，可以是一个一维数组或列表。
- `bins`：可选参数，表示直方图的箱数。默认为10。
- `range`：可选参数，表示直方图的值域范围，可以是一个二元组或列表。默认为None，即使用数据中的最小值和最大值。
- `density`：可选参数，表示是否将直方图归一化。默认为False，即直方图的高度为每个箱子内的样本数，而不是频率或概率密度。
- `weights`：可选参数，表示每个数据点的权重。默认为None。
- `cumulative`：可选参数，表示是否绘制累积分布图。默认为False。
- `bottom`：可选参数，表示直方图的起始高度。默认为None。
- `histtype`：可选参数，表示直方图的类型，可以是'bar'、'barstacked'、'step'、'stepfilled'等。默认为'bar'。
- `align`：可选参数，表示直方图箱子的对齐方式，可以是'left'、'mid'、'right'。默认为'mid'。
- `orientation`：可选参数，表示直方图的方向，可以是'vertical'、'horizontal'。默认为'vertical'。
- `rwidth`：可选参数，表示每个箱子的宽度。默认为None。
- `log`：可选参数，表示是否在y轴上使用对数刻度。默认为False。
- `color`：可选参数，表示直方图的颜色。
- `label`：可选参数，表示直方图的标签。
- `stacked`：可选参数，表示是否堆叠不同的直方图。默认为False。
- `**kwargs`：可选参数，表示其他绘图参数。


以下实例我们简单实用 hist() 来创建一个直方图:


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

# 生成一组随机数据
data = np.random.randn(1000)

# 绘制直方图
plt.hist(data, bins=30, color='skyblue', alpha=0.8)

# 设置图表属性
plt.title('RUNOOB hist() Test')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示图表
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2023/04/runoob-test-hist.png)


以下实例演示了如何使用 hist() 函数绘制多个数据组的直方图，并进行比较：


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

# 生成三组随机数据
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1, 1000)
data3 = np.random.normal(-2, 1, 1000)

# 绘制直方图
plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
plt.hist(data3, bins=30, alpha=0.5, label='Data 3')

# 设置图表属性
plt.title('RUNOOB hist() TEST')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# 显示图表
plt.show()
```


以上实例中我们生成了三组不同的随机数据，并使用 hist() 函数绘制了它们的直方图。通过设置不同的均值和标准差，我们可以生成具有不同分布特征的随机数据。


我们设置了 bins 参数为 30，这意味着将数据范围分成 30 个等宽的区间，然后统计每个区间内数据的频数。

我们设置了 alpha 参数为 0.5，这意味着每个直方图的颜色透明度为 50%。

我们使用 label 参数设置了每个直方图的标签，以便在图例中显示。

然后使用 legend() 函数显示图例。最后，我们使用 title()、xlabel() 和 ylabel() 函数设置了图表的标题和坐标轴标签。


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2023/04/runoob-test-hist-2.png)


从上图中我们可以清晰地看出这三组数据的分布情况，其中 data1 和 data2 分布接近正态分布，而 data3 分布偏态。

这种比较直方图的方式可以帮助我们分析和比较不同数据组的分布情况。


### 结合 Pandas

以下实例我们结合 Pandas 来绘制直方图：


## 实例


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 使用 NumPy 生成随机数
random_data = np.random.normal(170, 10, 250)

# 将数据转换为 Pandas DataFrame
dataframe = pd.DataFrame(random_data)

# 使用 Pandas hist() 方法绘制直方图
dataframe.hist()

# 设置图表属性
plt.title('RUNOOB hist() Test')
plt.xlabel('X-Value')
plt.ylabel('Y-Value')

# 显示图表
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2023/04/hist-pandas.png)


除了数据框之外，您还可以使用 Pandas 中的 Series 对象绘制直方图。只需将数据框中的列替换为 Series 对象即可。


## 实例


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 生成随机数据
data = pd.Series(np.random.normal(size=100))

# 绘制直方图
# bins 参数指定了直方图中的柱子数量
plt.hist(data, bins=10)

# 设置图形标题和坐标轴标签
plt.title('RUNOOB hist() Tes')
plt.xlabel('X-Values')
plt.ylabel('Y-Values')

# 显示图形
plt.show()
```


![](https://www.runoob.com/wp-content/uploads/2023/04/af3ddff7580ee52a9ee24d7368ab1dbc.png)









	  AI 思考中...





			** [Matplotlib 饼图](https://www.runoob.com/matplotlib-pie.html)
			[Matplotlib imshow() 方法](https://www.runoob.com/matplotlib-imshow.html) **













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