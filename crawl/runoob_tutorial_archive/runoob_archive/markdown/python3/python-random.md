# Python random 模块

- Source: https://www.runoob.com/python3/python-random.html

Python **random** 模块主要用于生成随机数。


**random** 模块实现了各种分布的伪随机数生成器。


要使用 **random** 函数必须先导入：


```
import random
```


查看 random 模块中的内容:


## 实例


```python
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_inst', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
```


接下来我们使用 [random()](https://www.runoob.com/python3-func-number-random.html) 方法返回一个随机数，它在[半开放区间](https://www.runoob.com/w3cnote/programming-range.html) **[0,1)** 范围内，包含 0 但不包含 1。


## 实例


```python
# 导入 random 包
import random

# 生成随机数
print(random.random())
```


以上实例输出结果为：


```
0.4784904215869241
```


**[seed()](https://www.runoob.com/python3-func-number-seed.html)** 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。


## 实例


```python
#!/usr/bin/python3
import random

random.seed()
print ("使用默认种子生成随机数：", random.random())
print ("使用默认种子生成随机数：", random.random())

random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())

random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())
```


以上实例运行后输出结果为：


```
使用默认种子生成随机数： 0.7908102856355441
使用默认种子生成随机数： 0.81038961519195
使用整数 10 种子生成随机数： 0.5714025946899135
使用整数 10 种子生成随机数： 0.5714025946899135
使用字符串种子生成随机数： 0.3537754404730722
```


### random 模块方法


random 模块方法如下：


| 方法 | 描述 |
| --- | --- |
| seed() | 初始化随机数生成器 |
| getstate() | 返回捕获生成器当前内部状态的对象。 |
| setstate() | state 应该是从之前调用 getstate() 获得的，并且 setstate() 将生成器的内部状态恢复到 getstate() 被调用时的状态。 |
| getrandbits(k) | 返回具有 k 个随机比特位的非负 Python 整数。 此方法随 MersenneTwister 生成器一起提供，其他一些生成器也可能将其作为 API 的可选部分提供。 在可能的情况下，getrandbits() 会启用 randrange() 来处理任意大的区间。 |
| randrange() | 从 range(start, stop, step) 返回一个随机选择的元素。 |
| randint(a, b) | 返回随机整数 N 满足 a  0 和 beta > 0。 返回值的范围介于 0 和 1 之间。 |
| expovariate(lambd) | 指数分布。 lambd 是 1.0 除以所需的平均值，它应该是非零的。 |
| gammavariate() | Gamma 分布（ 不是伽马函数） 参数的条件是 alpha > 0 和 beta > 0。 |
| gauss(mu, sigma) | 正态分布，也称高斯分布。 mu 为平均值，而 sigma 为标准差。 此函数要稍快于下面所定义的 normalvariate() 函数。 |
| lognormvariate(mu, sigma) | 对数正态分布。 如果你采用这个分布的自然对数，你将得到一个正态分布，平均值为 mu 和标准差为 sigma 。 mu 可以是任何值，sigma 必须大于零。 |
| normalvariate(mu, sigma) | 正态分布。 mu 是平均值，sigma 是标准差。 |
| vonmisesvariate(mu, kappa) | 冯·米塞斯分布。 mu 是平均角度，以弧度表示，介于0和 2*pi 之间，kappa 是浓度参数，必须大于或等于零。 如果 kappa 等于零，则该分布在 0 到 2*pi 的范围内减小到均匀的随机角度。 |
| paretovariate(alpha) | 帕累托分布。 alpha 是形状参数。 |
| weibullvariate(alpha, beta) | 威布尔分布。 alpha 是比例参数，beta 是形状参数。 |








	  AI 思考中...





			** [Python requests 模块](https://www.runoob.com/python-requests.html)
			[Python random randint() 方法](https://www.runoob.com/ref-random-randint.html) **













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