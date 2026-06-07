# SciPy 插值

- Source: https://www.runoob.com/scipy/scipy-interpolation.html

### 什么是插值？


在数学的数值分析领域中，插值（英语：interpolation）是一种通过已知的、离散的数据点，在范围内推求新数据点的过程或方法。


简单来说插值是一种在给定的点之间生成点的方法。


**例如：**对于两个点 1 和 2，我们可以插值并找到点 1.33 和 1.66。


插值有很多用途，在机器学习中我们经常处理数据缺失的数据，插值通常可用于替换这些值。


这种填充值的方法称为插补。


除了插补，插值经常用于我们需要平滑数据集中离散点的地方。


### 如何在 SciPy 中实现插值？


SciPy 提供了 scipy.interpolate 模块来处理插值。


### 一维插值


一维数据的插值运算可以通过方法 **interp1d()** 完成。

该方法接收两个参数 x 点和 y 点。


返回值是可调用函数，该函数可以用新的 x 调用并返回相应的 y，**y = f(x)**。


对给定的 xs 和 ys 插值，从 2.1、2.2... 到 2.9：


## 实例


```python
from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)
```


输出结果为：


```
[5.2  5.4  5.6  5.8  6.   6.2  6.4  6.6  6.8]
```


**注意：**新的 xs 应该与旧的 xs 处于相同的范围内，这意味着我们不能使用大于 10 或小于 0 的值调用 interp_func()。



### 单变量插值


在一维插值中，点是针对单个曲线拟合的，而在样条插值中，点是针对使用多项式分段定义的函数拟合的。


单变量插值使用 UnivariateSpline() 函数，该函数接受 xs 和 ys 并生成一个可调用函数，该函数可以用新的 xs 调用。


分段函数，就是对于自变量 x 的不同的取值范围，有着不同的解析式的函数。


为非线性点找到 2.1、2.2...2.9 的单变量样条插值：


## 实例


```python
from scipy.interpolate import UnivariateSpline
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = UnivariateSpline(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)
```


输出结果为：


```
[5.62826474 6.03987348 6.47131994 6.92265019 7.3939103  7.88514634
   8.39640439 8.92773053 9.47917082]
```


### 径向基函数插值

径向基函数是对应于固定参考点定义的函数。


曲面插值里我们一般使用径向基函数插值。


Rbf() 函数接受 xs 和 ys 作为参数，并生成一个可调用函数，该函数可以用新的 xs 调用。


## 实例


```python
from scipy.interpolate import Rbf
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = Rbf(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)
```


输出结果为：


```
[6.25748981  6.62190817  7.00310702  7.40121814  7.8161443   8.24773402
   8.69590519  9.16070828  9.64233874]
```










	  AI 思考中...





			** [SciPy Matlab 数组](https://www.runoob.com/scipy-matlab-arrays.html)
			[Scipy 显著性检验](https://www.runoob.com/scipy-significance-tests.html) **













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