# Pandas 教程

- Source: https://www.runoob.com/pandas/pandas-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2021/04/pandas.png)


**Pandas 是 Python 语言的一个扩展程序库，用于数据分析。**


Pandas 名字衍生自术语 "panel data"（面板数据）和 "**Python data analysis**"（Python 数据分析）。


Pandas 是一个开放源码、BSD 许可的库，提供高性能、易于使用的数据结构和数据分析工具。


Pandas 一个强大的分析结构化数据的工具集，基础是 [Numpy](https://www.runoob.com/../numpy/numpy-tutorial.html)（提供高性能的矩阵运算）。


---

## 学习本教程前你需要了解


在开始学习 Pandas 教程之前，我们需要具备基本的 Python 基础，如果你对 Python还不了解，可以阅读我们的教程：


- [Python 2.x 版本](https://www.runoob.com/../python/python-tutorial.html)
- [Python 3.x 版本](https://www.runoob.com/../python3/python3-tutorial.html)
- [Matplotlib 教程](https://www.runoob.com/../matplotlib/matplotlib-tutorial.html)

---

## Pandas 应用


Pandas 可以从各种文件格式比如 CSV、JSON、SQL、Microsoft Excel 导入数据。

Pandas 可以对各种数据进行运算操作，比如归并、再成形、选择，还有数据清洗和数据加工特征。


Pandas 广泛应用在学术、金融、统计学等各个数据分析领域。


---


## Pandas 功能

Pandas 是数据分析的利器，它不仅提供了高效、灵活的数据结构，还能帮助你以极低的成本完成复杂的数据操作和分析任务。


Pandas 提供了丰富的功能，包括：



- 数据清洗：处理缺失数据、重复数据等。
- 数据转换：改变数据的形状、结构或格式。
- 数据分析：进行统计分析、聚合、分组等。
- 数据可视化：通过整合 Matplotlib 和 Seaborn 等库，可以进行数据可视化。


---

## 数据结构


Pandas 的主要数据结构是 Series （一维数据）与 DataFrame（二维数据）。


- **[Series](https://www.runoob.com/pandas-series.html)** 是一种类似于一维数组的对象，它由一组数据（各种 Numpy 数据类型）以及一组与之相关的数据标签（即索引）组成。
- **[DataFrame](https://www.runoob.com/pandas-dataframe.html)** 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。


Pandas 是 Python 数据科学领域中不可或缺的工具之一，它的灵活性和强大的功能使得数据处理和分析变得更加简单和高效。


---

## 第一个 pandas 实例

以下实例创建一个简单的 DataFrame：


## 实例


```python
import pandas as pd

# 创建一个简单的 DataFrame
data = {'Name': ['Google', 'Runoob', 'Taobao'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# 查看 DataFrame
print(df)
```


以上代码输出结果为：


```
Name  Age
0  Google   25
1  Runoob   30
2  Taobao   35
```


---

## 相关链接

- Pandas 官网 [https://pandas.pydata.org/](https://pandas.pydata.org/)
- Pandas 源代码：[https://github.com/pandas-dev/pandas](https://github.com/pandas-dev/pandas)








	  AI 思考中...






			[Pandas 安装](https://www.runoob.com/pandas-install.html) **













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