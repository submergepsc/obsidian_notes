# Matplotlib imsave() 方法

- Source: https://www.runoob.com/matplotlib/matplotlib-imsave.html

imsave() 方法是 Matplotlib 库中用于将图像数据保存到磁盘上的函数。


通过 imsave() 方法我们可以轻松将生成的图像保存到我们指定的目录中。


imsave() 方法保存图片支持多种图像格式，例如 PNG、JPEG、BMP 等。


imsave() 方法的语法如下：


```
matplotlib.pyplot.imsave(fname, arr, **kwargs)
```


**参数说明：**


- `fname`：保存图像的文件名，可以是相对路径或绝对路径。
- `arr`：表示图像的NumPy数组。
- `kwargs`：可选参数，用于指定保存的图像格式以及图像质量等参数。


以下是一个使用 imsave() 方法保存图像的简单实例：


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

# 创建一个二维的图像数据
img_data = np.random.random((100, 100))

# 显示图像
plt.imshow(img_data)

# 保存图像到磁盘上
plt.imsave('runoob-test.png', img_data)
```


以上实例我们使用 imsave() 方法将这个图像保存到了当前目录下，文件名为 **runoob-test.png**。

由于没有指定图像格式，Matplotlib 库默认将其保存为 PNG 格式的文件。

打开当前目录，会发现一个 **runoob-test.png** 文件，如下所示：


![](https://www.runoob.com/wp-content/uploads/2023/04/runoob-test.png)


以下实例演示了如何使用 imsave() 方法将一个灰度图像和一幅彩色图像保存到当前目录上：


## 实例


```python
import matplotlib.pyplot as plt
import numpy as np

# 创建一幅灰度图像
img_gray = np.random.random((100, 100))

# 创建一幅彩色图像
img_color = np.zeros((100, 100, 3))
img_color[:, :, 0] = np.random.random((100, 100))
img_color[:, :, 1] = np.random.random((100, 100))
img_color[:, :, 2] = np.random.random((100, 100))

# 显示灰度图像
plt.imshow(img_gray, cmap='gray')

# 保存灰度图像到磁盘上
plt.imsave('test_gray.png', img_gray, cmap='gray')

# 显示彩色图像
plt.imshow(img_color)

# 保存彩色图像到磁盘上
plt.imsave('test_color.jpg', img_color)
```


以上实例中我们使用了 **numpy.random** 模块分别创建了一幅灰度图像和一幅彩色图像，然后分别使用 imshow() 方法显示这两幅图像。

接着，我们使用 imsave() 函数将这两幅图像分别保存到了当前目录上，文件名分别为 **test_gray.png** 和 **test_color.jpg**。

在保存灰度图像时，我们使用了 cmap 参数将其保存为灰度图像格式。

在保存彩色图像时，我们没有指定图像格式，Matplotlib 库默认将其保存为 JPEG 格式的文件。









	  AI 思考中...





			** [Matplotlib imshow() 方法](https://www.runoob.com/matplotlib-imshow.html)
			[Matplotlib imread() 方法](https://www.runoob.com/matplotlib-imread.html) **













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