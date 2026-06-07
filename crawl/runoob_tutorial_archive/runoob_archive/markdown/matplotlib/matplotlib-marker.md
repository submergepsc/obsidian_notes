# Matplotlib 绘图标记

- Source: https://www.runoob.com/matplotlib/matplotlib-marker.html

绘图过程如果我们想要给坐标自定义一些不一样的标记，就可以使用 **plot()** 方法的 **marker** 参数来定义。


以下实例定义了实心圆标记：


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1,3,4,5,8,9,6,1,3,4,5,2,4])

plt.plot(ypoints, marker = 'o')
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/07/pl_marker01.png)


**marker** 可以定义的符号如下：


| 标记 | 符号 | 描述 |
| --- | --- | --- |
| "." |  | 点 |
| "," |  | 像素点 |
| "o" |  | 实心圆 |
| "v" |  | 下三角 |
| "^" |  | 上三角 |
| "" |  | 右三角 |
| "1" |  | 下三叉 |
| "2" |  | 上三叉 |
| "3" |  | 左三叉 |
| "4" |  | 右三叉 |
| "8" |  | 八角形 |
| "s" |  | 正方形 |
| "p" |  | 五边形 |
| "P" |  | 加号（填充） |
| "*" |  | 星号 |
| "h" |  | 六边形 1 |
| "H" |  | 六边形 2 |
| "+" |  | 加号 |
| "x" |  | 乘号 x |
| "X" |  | 乘号 x (填充) |
| "D" |  | 菱形 |
| "d" |  | 瘦菱形 |
| "\|" |  | 竖线 |
| "_" |  | 横线 |
| 0 (TICKLEFT) |  | 左横线 |
| 1 (TICKRIGHT) |  | 右横线 |
| 2 (TICKUP) |  | 上竖线 |
| 3 (TICKDOWN) |  | 下竖线 |
| 4 (CARETLEFT) |  | 左箭头 |
| 5 (CARETRIGHT) |  | 右箭头 |
| 6 (CARETUP) |  | 上箭头 |
| 7 (CARETDOWN) |  | 下箭头 |
| 8 (CARETLEFTBASE) |  | 左箭头 (中间点为基准) |
| 9 (CARETRIGHTBASE) |  | 右箭头 (中间点为基准) |
| 10 (CARETUPBASE) |  | 上箭头 (中间点为基准) |
| 11 (CARETDOWNBASE) |  | 下箭头 (中间点为基准) |
| "None", " " or "" |  | 没有任何标记 |
| '$...$' |  | 渲染指定的字符。例如 "$f$" 以字母 f 为标记。 |


以下实例定义了 ***** 标记：


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1,3,4,5,8,9,6,1,3,4,5,2,4])

plt.plot(ypoints, marker = '*')
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/07/pl_marker-1.png)


以下实例定义了下箭头：


## 实例


```python
import matplotlib.pyplot as plt
import matplotlib.markers

plt.plot([1, 2, 3], marker=matplotlib.markers.CARETDOWNBASE)
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/07/pl_marker_2.png)


### fmt 参数

fmt 参数定义了基本格式，如标记、线条样式和颜色。


```
fmt = '[marker][line][color]'
```


例如 **o:r**，**o** 表示实心圆标记，**:** 表示虚线，**r** 表示颜色为红色。


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, 'o:r')
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/07/pl_marker-3.png)


线类型：


| 线类型标记 | 描述 |
| --- | --- |
| '-' | 实线 |
| ':' | 虚线 |
| '--' | 破折线 |
| '-.' | 点划线 |


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


### 标记大小与颜色

我们可以自定义标记的大小与颜色，使用的参数分别是：

- markersize，简写为 **ms**：定义标记的大小。
- markerfacecolor，简写为 **mfc**：定义标记内部的颜色。
- markeredgecolor，简写为 **mec**：定义标记边框的颜色。


设置标记大小：


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/07/pl_marker-5.png)


设置标记外边框颜色：


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/07/pl_marker-6.png)


设置标记内部颜色：


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/07/pl_marker-7.png)


自定义标记内部与边框的颜色：


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/07/pl_marker-8.png)








	  AI 思考中...





			** [Matplotlib Pyplot](https://www.runoob.com/matplotlib-pyplot.html)
			[Matplotlib 绘图线](https://www.runoob.com/matplotlib-line.html) **













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