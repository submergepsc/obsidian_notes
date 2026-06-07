# Matplotlib Pyplot

- Source: https://www.runoob.com/matplotlib/matplotlib-pyplot.html

Pyplot 是 Matplotlib 的子库，提供了和 MATLAB 类似的绘图 API。


Pyplot 是常用的绘图模块，能很方便让用户绘制 2D 图表。

Pyplot 包含一系列绘图函数的相关函数，每个函数会对当前的图像进行一些修改，例如：给图像加上标记，生新的图像，在图像中产生新的绘图区域等等。


使用的时候，我们可以使用 import 导入 pyplot 库，并设置一个别名 **plt**：


```python
import matplotlib.pyplot as plt
```


这样我们就可以使用 **plt** 来引用 Pyplot 包的方法。


以下是一些常用的 pyplot 函数：


- `plot()`：用于绘制线图和散点图
- `scatter()`：用于绘制散点图
- `bar()`：用于绘制垂直条形图和水平条形图
- `hist()`：用于绘制直方图
- `pie()`：用于绘制饼图
- `imshow()`：用于绘制图像
- `subplots()`：用于创建子图


除了这些基本的函数，pyplot 还提供了很多其他的函数，例如用于设置图表属性的函数、用于添加文本和注释的函数、用于保存图表到文件的函数等等。


以下实例，我们通过两个坐标 **(0,0)** 到 **(6,100)** 来绘制一条线:


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 100])

plt.plot(xpoints, ypoints)
plt.show()
```


输出结果如下所示：


![](https://www.runoob.com/wp-content/uploads/2021/06/A8A7DE3A-DFF7-41DC-95BC-FD987E3E8CE2.jpg)


以上实例中我们使用了 Pyplot 的 **plot()** 函数， **plot()** 函数是绘制二维图形的最基本函数。

**plot()** 用于画图它可以绘制点和线，语法格式如下：


```
# 画单条线
plot([x], y, [fmt], *, data=None, **kwargs)
# 画多条线
plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
```


参数说明：

- **x, y：**点或线的节点，x 为 x 轴数据，y 为 y 轴数据，数据可以列表或数组。
- **fmt：**可选，定义基本格式（如颜色、标记和线条样式）。
- ****kwargs：**可选，用在二维平面图上，设置指定属性，如标签，线的宽度等。


```python
>>> plot(x, y)        # 创建 y 中数据与 x 中对应值的二维线图，使用默认样式
>>> plot(x, y, 'bo')  # 创建 y 中数据与 x 中对应值的二维线图，使用蓝色实心圈绘制
>>> plot(y)           # x 的值为 0..N-1
>>> plot(y, 'r+')     # 使用红色 + 号
```


**颜色字符：**'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，'c' 青绿色，'#008000' RGB 颜色符串。多条曲线不指定颜色时，会自动选择不同颜色。


**线型参数：**'‐' 实线，'‐‐' 破折线，'‐.' 点划线，':' 虚线。


**标记字符：**'.' 点标记，',' 像素标记(极小点)，'o' 实心圈标记，'v' 倒三角标记，'^' 上三角标记，'>' 右三角标记，'







	  AI 思考中...





			** [Matplotlib 安装](https://www.runoob.com/matplotlib-install.html)
			[Matplotlib 绘图标记](https://www.runoob.com/matplotlib-marker.html) **













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