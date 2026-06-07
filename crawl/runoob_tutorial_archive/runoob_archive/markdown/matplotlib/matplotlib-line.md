# Matplotlib 绘图线

- Source: https://www.runoob.com/matplotlib/matplotlib-line.html

绘图过程如果我们自定义线的样式，包括线的类型、颜色和大小等。


### 线的类型

线的类型可以使用 **linestyle** 参数来定义，简写为 **ls**。


| 类型 | 简写 | 说明 |
| --- | --- | --- |
| 'solid' (默认) | '-' | 实线 |
| 'dotted' | ':' | 点虚线 |
| 'dashed' | '--' | 破折线 |
| 'dashdot' | '-.' | 点划线 |
| 'None' | '' 或 ' ' | 不画线 |


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/07/pl_line-1.png)


使用简写：


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, ls = '-.')
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/07/pl_line-2.png)


### 线的颜色

线的颜色可以使用 **color** 参数来定义，简写为 **c**。


颜色类型：


| 颜色标记 | 描述 |
| --- | --- |
| 'r' | 红色 |
| 'g' | 绿色 |
| 'b' | 蓝色 |
| 'c' | 青色 |
| 'm' | 品红 |
| 'y' | 黄色 |
| 'k' | 黑色 |
| 'w' | 白色 |

当然也可以自定义颜色类型，例如：**SeaGreen、#8FBC8F** 等，完整样式可以参考 [HTML 颜色值](https://www.runoob.com/../html/html-colorvalues.html)。


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, color = 'r')
plt.show()
```


显示结果如下：

![](https://www.runoob.com/wp-content/uploads/2021/07/pl_line-3.png)


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, c = '#8FBC8F')
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/07/pl_line-4.png)


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, c = 'SeaGreen')
plt.show()
```


显示结果如下：

![](https://www.runoob.com/wp-content/uploads/2021/07/pl_line-5.png)


### 线的宽度


线的宽度可以使用 ** linewidth ** 参数来定义，简写为 **lw**，值可以是浮点数，如：**1**、**2.0**、**5.67** 等。


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, linewidth = '12.5')
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/07/pl_line-6.png)


### 多条线

plot() 方法中可以包含多对 x,y 值来绘制多条线。


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 7, 5, 9])
y2 = np.array([6, 2, 13, 10])

plt.plot(y1)
plt.plot(y2)

plt.show()
```


从上图可以看出 **x** 的值默认设置为 **[0, 1, 2, 3]**。


显示结果如下：


我们也可以自己设置 x 坐标等值：


![](https://www.runoob.com/wp-content/uploads/2021/07/pl_line-7.png)


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 7, 5, 9])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 13, 10])

plt.plot(x1, y1, x2, y2)
plt.show()
```


显示结果如下：

![](https://www.runoob.com/wp-content/uploads/2021/07/pl_line-8.png)








	  AI 思考中...





			** [Matplotlib 绘图标记](https://www.runoob.com/matplotlib-marker.html)
			[Matplotlib 轴标签和标题](https://www.runoob.com/matplotlib-label.html) **













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