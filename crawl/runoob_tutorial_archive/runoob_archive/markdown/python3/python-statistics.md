# Python statistics 模块

- Source: https://www.runoob.com/python3/python-statistics.html

在数据分析和科学计算中，统计学是一个非常重要的工具。

Python 提供了一个内置的 `statistics` 模块，专门用于处理基本的统计计算。本文将详细介绍 `statistics` 模块的功能和使用方法，帮助初学者快速掌握如何使用这个模块进行基本的统计分析。


`statistics` 模块提供了许多常用的统计函数，如均值、中位数、方差、标准差等。


要使用 statistics 函数必须先导入：


```
import statistics
```


查看 statistics 模块中的内容:


```python
>>> import statistics
>>> dir(statistics)
['Counter', 'Decimal', 'Fraction', 'NormalDist', 'StatisticsError', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_coerce', '_convert', '_exact_ratio', '_fail_neg', '_find_lteq', '_find_rteq', '_isfinite', '_normal_dist_inv_cdf', '_ss', '_sum', 'bisect_left', 'bisect_right', 'erf', 'exp', 'fabs', 'fmean', 'fsum', 'geometric_mean', 'groupby', 'harmonic_mean', 'hypot', 'itemgetter', 'log', 'math', 'mean', 'median', 'median_grouped', 'median_high', 'median_low', 'mode', 'multimode', 'numbers', 'pstdev', 'pvariance', 'quantiles', 'random', 'sqrt', 'stdev', 'tau', 'variance']
```


---


## 常用的统计函数


### 均值（Mean）


均值是数据集中所有数值的平均值。`statistics` 模块提供了 `mean()` 函数来计算均值。


## 实例


```python
data = [1, 2, 3, 4, 5]
mean_value = statistics.mean(data)
print("均值:", mean_value)
```


输出：


```
均值: 3
```


### 中位数（Median）


中位数是将数据集按大小顺序排列后位于中间位置的数值。`statistics` 模块提供了 `median()` 函数来计算中位数。


## 实例


```python
data = [1, 2, 3, 4, 5]
median_value = statistics.median(data)
print("中位数:", median_value)
```


输出：


```
中位数: 3
```


如果数据集的长度为偶数，`median()` 函数会自动计算中间两个数的平均值。


## 实例


```python
data = [1, 2, 3, 4]
median_value = statistics.median(data)
print("中位数:", median_value)
```


输出：


```
中位数: 2.5
```


### 众数（Mode）


众数是数据集中出现频率最高的数值。`statistics` 模块提供了 `mode()` 函数来计算众数。


## 实例


```python
data = [1, 2, 2, 3, 4]
mode_value = statistics.mode(data)
print("众数:", mode_value)
```


输出：


```
众数: 2
```


如果数据集中没有重复的数值，`mode()` 函数会抛出 `StatisticsError` 异常。


### 方差（Variance）


方差是衡量数据集中数值离散程度的指标。`statistics` 模块提供了 `variance()` 函数来计算方差。


## 实例


```python
data = [1, 2, 3, 4, 5]
variance_value = statistics.variance(data)
print("方差:", variance_value)
```


输出：


```
方差: 2.5
```


### 标准差（Standard Deviation）


标准差是方差的平方根，用于衡量数据集的离散程度。`statistics` 模块提供了 `stdev()` 函数来计算标准差。


## 实例


```python
data = [1, 2, 3, 4, 5]
stdev_value = statistics.stdev(data)
print("标准差:", stdev_value)
```


输出：


```
标准差: 1.5811388300841898
```


### 调和平均数（Harmonic Mean）


调和平均数是一种特殊的平均数，适用于计算速率等场景。`statistics` 模块提供了 `harmonic_mean()` 函数来计算调和平均数。


## 实例


```python
data = [1, 2, 4]
harmonic_mean_value = statistics.harmonic_mean(data)
print("调和平均数:", harmonic_mean_value)
```


输出：


```
调和平均数: 1.7142857142857142
```


### 几何平均数（Geometric Mean）


几何平均数是一种用于计算增长率或比例的平均数。`statistics` 模块提供了 `geometric_mean()` 函数来计算几何平均数。


## 实例


```python
data = [1, 2, 4]
geometric_mean_value = statistics.geometric_mean(data)
print("几何平均数:", geometric_mean_value)
```


输出：


```
几何平均数: 2.0
```


---

## 其他常用函数


### 中位数低（Median Low）和中位数高（Median High）


`statistics` 模块还提供了 `median_low()` 和 `median_high()` 函数，分别用于计算数据集的中位数低和中位数高。


## 实例


```python
data = [1, 2, 3, 4]
median_low_value = statistics.median_low(data)
median_high_value = statistics.median_high(data)
print("中位数低:", median_low_value)
print("中位数高:", median_high_value)
```


输出：


```
中位数低: 2
中位数高: 3
```


### 分位数（Quantiles）


分位数是将数据集分成若干等份的数值。`statistics` 模块提供了 `quantiles()` 函数来计算分位数。


## 实例


```python
data = [1, 2, 3, 4, 5]
quantiles_value = statistics.quantiles(data, n=4)
print("四分位数:", quantiles_value)
```


输出：


```
四分位数: [1.5, 3.0, 4.5]
```


---


## math 模块方法


| 方法 | 描述 |
| --- | --- |
| statistics.harmonic_mean() | 计算给定数据集的调和平均值。 |
| statistics.mean() | 计算数据集的平均值 |
| statistics.median() | 计算数据集的中位数 |
| statistics.median_grouped() | 计算给定分组数据集的分组中位数 |
| statistics.median_high() | 计算给定数据集的高位中位数 |
| statistics.median_low() | 计算给定数据集的低位中位数。 |
| statistics.mode() | 算数据集的众数（出现频率最高的值） |
| statistics.pstdev() | 计算给定数据集的样本标准偏差 |
| statistics.stdev() | 计算数据集的标准差 |
| statistics.pvariance() | 计算给定数据集的样本方差 |
| statistics.variance() | 计算数据集的方差 |
| statistics.quantiles() | 计算数据集的分位数，可指定分位数的数量（默认为四分位数） |









	  AI 思考中...





			** [Python object() 函数](https://www.runoob.com/python-func-object.html)
			[Python statistics.harmonic_mean() 方法](https://www.runoob.com/ref-stat-harmonic_mean.html) **













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