# Pandas 相关性分析

- Source: https://www.runoob.com/pandas/pandas-correlations.html

相关性分析是数据分析中常见且重要的一步，它帮助我们理解数据中不同变量之间的关系。


在 Pandas 中，数据相关性分析是通过计算不同变量之间的相关系数来了解它们之间的关系。


在 Pandas 中，数据相关性是一项重要的分析任务，它帮助我们理解数据中各个变量之间的关系。


Pandas 提供了多种方法来计算和分析数据的相关性，常见的相关性方法包括皮尔逊相关系数（Pearson）、斯皮尔曼等级相关系数（Spearman）以及肯德尔秩相关系数（Kendall）。

以下相关性方法可以帮助我们揭示变量之间的线性关系、非线性关系或单调关系：


- **皮尔逊相关系数**：衡量变量之间的线性关系，适用于数值型变量。
- **斯皮尔曼等级相关系数**：衡量变量之间的单调关系，适用于数值型和顺序型变量。
- **肯德尔秩相关系数**：衡量变量之间的秩次关系，适用于小样本数据。
- **相关性矩阵**：用来查看各个变量之间的相关性。
- **热图**：一种有效的可视化方式，可以帮助我们直观地查看变量之间的相关性。


### 什么是相关性？

相关性表示两个或多个变量之间的关系强度和方向。根据相关性的数值，可以判断变量之间的关系。

- **正相关**：当一个变量增加时，另一个变量也增加。例如，身高和体重之间可能存在正相关关系。
- **负相关**：当一个变量增加时，另一个变量减少。例如，气温和取暖的使用量之间可能存在负相关关系。
- **无相关性**：两个变量之间没有明确的关系。


相关性的数值范围通常在 -1 到 1 之间：

- **1**：完全正相关
- **-1**：完全负相关
- **0**：没有线性相关性
- **接近 1 或 -1**：表示强相关
- **接近 0**：表示弱相关

---


## Pandas 中计算相关性的方法

Pandas 提供了 `DataFrame.corr()` 和 `DataFrame.cov()` 方法来计算相关性和协方差。


Pandas 使用 **corr()** 方法计算数据集中每列之间的关系。


```
df.corr(method='pearson', min_periods=1)
```


参数说明：


- **method** (可选): 字符串类型，用于指定计算相关系数的方法。默认是 'pearson'，还可以选择 'kendall'（Kendall Tau 相关系数）或 'spearman'（Spearman 秩相关系数）。
- **min_periods** (可选): 表示计算相关系数时所需的最小观测值数量。默认值是 1，即只要有至少一个非空值，就会进行计算。如果指定了 `min_periods`，并且在某些列中的非空值数量小于该值，则相应列的相关系数将被设为 NaN。


**df.corr()** 方法返回一个相关系数矩阵，矩阵的行和列对应数据框的列名，矩阵的元素是对应列之间的相关系数。


常见的相关性系数包括 Pearson 相关系数和 Spearman 秩相关系数：


### Pearson 相关系数

Pearson 即皮尔逊相关系数，用于衡量了两个变量之间的线性关系强度和方向，它的取值范围在 -1 到 1 之间，其中 -1 表示完全负相关，1 表示完全正相关，0 表示无线性相关。

皮尔逊相关系数用于衡量两个变量之间的线性关系，计算公式为：


![](https://www.runoob.com/wp-content/uploads/2024/02/5e816f5040916fb1e447746893ebe74c.png)


Pandas 可以使用 **corr()** 方法计算数据框中各列之间的 Pearson 相关系数。


**Pearson 相关系数**


## 实例


```python
import pandas as pd

# 示例数据
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [45, 55, 65, 75, 85],
    'Age': [20, 25, 30, 35, 40]
}

df = pd.DataFrame(data)

# 计算皮尔逊相关系数
correlation = df.corr(method='pearson')
print(correlation)
```


输出结果：


```
Height  Weight  Age
Height     1.0     1.0  1.0
Weight     1.0     1.0  1.0
Age        1.0     1.0  1.0
```


**说明**:


- `corr()` 方法计算了每对变量之间的皮尔逊相关系数。`method='pearson'` 是默认方法，表示计算皮尔逊相关系数。
- 可以看到，`Height` 与 `Weight` 和 `Age` 都有很强的正相关性。


### 斯皮尔曼等级相关系数（Spearman Correlation）


斯皮尔曼相关系数用于衡量两个变量的单调关系（无论是线性还是非线性），它是基于变量的排名计算的。斯皮尔曼相关系数的取值范围与皮尔逊相关系数相同：-1 到 1。


## 实例


```python
import pandas as pd

# 示例数据
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [45, 55, 65, 75, 85],
    'Age': [20, 25, 30, 35, 40]
}

df = pd.DataFrame(data)

# 计算斯皮尔曼等级相关系数
spearman_correlation = df.corr(method='spearman')
print(spearman_correlation)
```


输出结果：


```
Height  Weight  Age
Height     1.0     1.0  1.0
Weight     1.0     1.0  1.0
Age        1.0     1.0  1.0
```


**说明：**method='spearman' 会计算斯皮尔曼等级相关系数。在这个示例中，由于数据是线性增长的，斯皮尔曼相关系数与皮尔逊相关系数相同。


### 肯德尔秩相关系数（Kendall Correlation）

肯德尔秩相关系数也用于衡量变量之间的单调关系，它是通过计算两个变量排名之间的一致性来得出的。

肯德尔相关系数的计算较为复杂，适用于较小的数据集。


## 实例


```python
import pandas as pd

# 示例数据
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [45, 55, 65, 75, 85],
    'Age': [20, 25, 30, 35, 40]
}

df = pd.DataFrame(data)

# 计算肯德尔秩相关系数
kendall_correlation = df.corr(method='kendall')
print(kendall_correlation)
```


输出结果：


```
Height  Weight  Age
Height     1.0     1.0  1.0
Weight     1.0     1.0  1.0
Age        1.0     1.0  1.0
```


**说明：**method='kendall' 会计算肯德尔秩相关系数。在这种情况下，数据的变化是单调的，因此计算结果与皮尔逊和斯皮尔曼相同。


---

## 相关性矩阵

相关性矩阵是一个对称矩阵，矩阵中的每个值表示两个变量之间的相关系数。

可以通过 corr() 方法直接计算 DataFrame 中所有变量的相关性矩阵。


## 实例


```python
import pandas as pd

# 示例数据
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [45, 55, 65, 75, 85],
    'Age': [20, 25, 30, 35, 40]
}
df = pd.DataFrame(data)

# 计算相关性矩阵
correlation_matrix = df.corr()
print(correlation_matrix)
```


输出结果：


```
Height  Weight  Age
Height     1.0     1.0  1.0
Weight     1.0     1.0  1.0
Age        1.0     1.0  1.0
```


**说明：**相关性矩阵可以帮助我们快速识别出哪些变量之间有较强的线性或单调关系。在实际分析中，相关性矩阵对于特征选择和降维非常有帮助。

---


## 相关性热图（Correlation Heatmap）

为了更直观地呈现相关性矩阵，可以使用热图（Heatmap）来可视化各个变量之间的相关性。

使用 seaborn 库绘制相关性热图是一个常见的做法。


## 实例


```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 示例数据
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [45, 55, 65, 75, 85],
    'Age': [20, 25, 30, 35, 40]
}
df = pd.DataFrame(data)
# 绘制相关性热图
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.show()
```


显示如下：

![](https://www.runoob.com/wp-content/uploads/2024/02/pandas-232132.png)


**说明：**sns.heatmap() 绘制相关性热图，annot=True 表示在热图上显示数值，cmap='coolwarm' 设置颜色范围，vmin=-1, vmax=1 限制颜色范围为 -1 到 1。


---

## 可视化相关性

这里我们要使用 Python 的 Seaborn 库， Seaborn 是一个基于 Matplotlib 的数据可视化库，专注于统计图形的绘制，旨在简化数据可视化的过程。

Seaborn 提供了一些简单的高级接口，可以轻松地绘制各种统计图形，包括散点图、折线图、柱状图、热图等，而且具有良好的美学效果。


安装 Seaborn：


```
pip install seaborn
```


## 实例


```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 创建一个示例数据框
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# 计算 Pearson 相关系数
correlation_matrix = df.corr()
# 使用热图可视化 Pearson 相关系数
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()
```


**说明：**这段代码将生成一个热图，用颜色表示相关系数的强度，其中正相关用温暖色调表示，负相关用冷色调表示。**annot=True** 参数在热图上显示具体的数值。


![](https://www.runoob.com/wp-content/uploads/2024/02/38fa14c44f0cc4f315a3dd4d5597d2b1_w.png)


---

## 相关性分析中的应用


### 1、特征选择

在机器学习建模中，相关性分析常常用于特征选择。通过分析不同特征之间的相关性，可以帮助我们选择与目标变量最相关的特征，并去除与其他特征高度相关的冗余特征，从而提高模型的表现和效率。


## 2、处理多重共线性

如果两个或多个特征之间的相关性非常高（接近 1 或 -1），那么这些特征之间存在多重共线性问题。在回归分析中，多重共线性会导致模型的不稳定性和预测不准确。可以通过删除或合并相关性较高的特征来解决多重共线性问题。








	  AI 思考中...





			** [Pandas 简介](https://www.runoob.com/pandas-intro.html)
			[Pandas Excel 文件操作](https://www.runoob.com/pandas-excel.html) **













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