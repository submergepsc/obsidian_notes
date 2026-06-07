# Python math 模块

- Source: https://www.runoob.com/python3/python-math.html

**Python math 模块**提供了大量常用数学函数，可用于完成：


- 三角函数计算（sin / cos / tan）
- 对数与指数运算（log / exp / pow）
- 取整与舍入（ceil / floor / trunc）
- 组合排列与阶乘（comb / perm / factorial）
- 距离与几何计算（dist / hypot / sqrt）


它是 Python 进行数学运算最常用的标准库之一。


就需要借助 `math` 模块完成。


**math** 模块下的函数，返回值均为浮点数，除非另有明确说明。


如果你需要计算复数，请使用 **cmath** 模块中的同名函数。


要使用 math 函数必须先导入：


```
import math
```


查看 math 模块中的内容:


```python
>>> import math
>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
```


### 为什么使用 math 模块？


虽然 Python 自带许多基本运算符（如 `+`、`-`、`*`、`/`），但对于更复杂的数学计算，例如：


- 开平方
- 三角函数
- 自然对数
- 浮点精度处理


### Python math 模块使用示例


```python
import math

print(math.sqrt(16))      # 4.0
print(math.pow(2, 3))     # 8.0
print(math.ceil(4.2))     # 5
print(math.floor(4.9))    # 4
print(math.sin(math.pi/2))# 1.0
```


输出结果为：


```
4.0
8.0
5
4
1.0
```


### math 模块常量


| 常量 | 描述 |
| --- | --- |
| math.e | 返回欧拉数 (2.7182...) |
| math.inf | 返回正无穷大浮点数 |
| math.nan | 返回一个浮点值 NaN (not a number) |
| math.pi | π 一般指圆周率。 圆周率 PI (3.1415...) |
| math.tau | 数学常数 τ = 6.283185...，精确到可用精度。Tau 是一个圆周常数，等于 2π，圆的周长与半径之比。 |


### math 模块函数


| 函数 | 描述 |
| --- | --- |
| math.acos(x) | 返回 x 的反余弦，结果范围在 0 到 pi 之间。 |
| math.acosh(x) | 返回 x 的反双曲余弦值。 |
| math.asin(x) | 返回 x 的反正弦值，结果范围在 -pi/2 到 pi/2 之间。 |
| math.asinh(x) | 返回 x 的反双曲正弦值。 |
| math.atan(x) | 返回 x 的反正切值，结果范围在 -pi/2 到 pi/2 之间。 |
| math.atan2(y, x) | 返回给定的 X 及 Y 坐标值的反正切值，结果是在 -pi 和 pi 之间。 |
| math.atanh(x) | 返回 x 的反双曲正切值。 |
| math.ceil(x) | 将 x 向上舍入到最接近的整数 |
| math.comb(n, k) | 返回不重复且无顺序地从 n 项中选择 k 项的方式总数。 |
| math.copysign(x, y) | 返回一个基于 x 的绝对值和 y 的符号的浮点数。 |
| math.cos() | 返回 x 弧度的余弦值。 |
| math.cosh(x) | 返回 x 的双曲余弦值。 |
| math.degrees(x) | 将角度 x 从弧度转换为度数。 |
| math.dist(p, q) | 返回 p 与 q 两点之间的欧几里得距离，以一个坐标序列（或可迭代对象）的形式给出。 两个点必须具有相同的维度。 |
| math.erf(x) | 返回一个数的误差函数 |
| math.erfc(x) | 返回 x 处的互补误差函数 |
| math.exp(x) | 返回 e 的 x 次幂，Ex， 其中 e = 2.718281... 是自然对数的基数。 |
| math.expm1() | 返回 Ex - 1， e 的 x 次幂，Ex，其中 e = 2.718281... 是自然对数的基数。这通常比 math.e ** x 或 pow(math.e, x) 更精确。 |
| math.fabs(x) | 返回 x 的绝对值。 |
| math.factorial(x) | 返回 x 的阶乘。 如果 x 不是整数或为负数时则将引发 ValueError。 |
| math.floor() | 将数字向下舍入到最接近的整数 |
| math.fmod(x, y) | 返回 x/y 的余数 |
| math.frexp(x) | 以 (m, e) 对的形式返回 x 的尾数和指数。 m 是一个浮点数， e 是一个整数，正好是 x == m * 2**e 。 如果 x 为零，则返回 (0.0, 0) ，否则返回 0.5







	  AI 思考中...





			** [Python3 operator 模块](https://www.runoob.com/python-operator.html)
			[Python math.e 常量](https://www.runoob.com/ref-math-e.html) **













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