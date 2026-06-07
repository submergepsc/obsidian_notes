# Matplotlib imread() 方法

- Source: https://www.runoob.com/matplotlib/matplotlib-imread.html

imread() 方法是 Matplotlib 库中的一个函数，用于从图像文件中读取图像数据。


imread() 方法返回一个 numpy.ndarray 对象，其形状是 **(nrows, ncols, nchannels)**，表示读取的图像的行数、列数和通道数：


- 如果图像是灰度图像，则 nchannels 为 1。
- 如果是彩色图像，则 nchannels 为 3 或 4，分别表示红、绿、蓝三个颜色通道和一个 alpha 通道。


imread() 方法的语法如下：


```
matplotlib.pyplot.imread(fname, format=None)
```


**参数说明：**


- `fname`：指定了要读取的图像文件的文件名或文件路径，可以是相对路径或绝对路径。
- `format `：参数指定了图像文件的格式，如果不指定，则默认根据文件后缀名来自动识别格式。


以下实例演示了如何使用 imread 函数从一张图像文件中读取图像数据，并将其显示出来：


## 实例


```python
import matplotlib.pyplot as plt

# 读取图像文件，下载地址：https://static.jyshare.com/images/demo/map.jpeg
img = plt.imread('map.jpeg')

# 显示图像
plt.imshow(img)
plt.show()
```


以上实例中我们首先使用 imread() 方法从名为 map.jpeg 的图像文件中读取了图像数据，并将其存储在 img 变量中。

然后我们使用imshow() 方法显示了这张图像。

注意：我们在显示图像时没有指定颜色映射，这是因为 imread() 方法已经将图像数据按照正确的颜色映射转换成了 RGB 格式，因此我们可以直接使用默认的颜色映射来显示图像。

显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2023/04/runoob-imread-1.png)


我们可以通过更改 numpy 数组来修改图像。

例如，如果我们将数组乘以一个数 **0≤≤1**，我们将图像变暗：


## 实例


```python
import matplotlib.pyplot as plt

# 读取图像文件，下载地址：https://static.jyshare.com/images/mix/tiger.jpeg
img_array = plt.imread('tiger.jpeg')
tiger = img_array/255
#print(tiger)

# 显示图像
plt.figure(figsize=(10,6))

for i in range(1,5):
    plt.subplot(2,2,i)
    x = 1 - 0.2*(i-1)
    plt.axis('off') #hide coordinate axes
    plt.title('x={:.1f}'.format(x))
    plt.imshow(tiger*x)

plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2023/04/ccfa3b47cfa040d43b899cad1acbd6bf-1.png)


以下实例用于裁剪图像：


## 实例


```python
import matplotlib.pyplot as plt

# 读取图像文件，下载地址：https://static.jyshare.com/images/mix/tiger.jpeg
img_array = plt.imread('tiger.jpeg')
tiger = img_array/255
#print(tiger)

# 显示图像
plt.figure(figsize=(6,6))
plt.imshow(tiger[:300,100:400,:])
plt.axis('off')
plt.show()
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2023/04/readimg-crop.png)


如果我们将 RGB 颜色的绿色和蓝色坐标的数组元素设置为 0，我们将得到红色的图像：


## 实例


```python
import matplotlib.pyplot as plt

# 读取图像文件，下载地址：https://static.jyshare.com/images/mix/tiger.jpeg
img_array = plt.imread('tiger.jpeg')
tiger = img_array/255
#print(tiger)

# 显示图像
red_tiger = tiger.copy()

red_tiger[:, :,[1,2]] = 0

plt.figure(figsize=(10,10))
plt.imshow(red_tiger)
plt.axis('off')
plt.show()
```


显示结果如下：

![](https://www.runoob.com/wp-content/uploads/2023/04/readimg-red.png)








	  AI 思考中...





			** [Matplotlib imsave() 方法](https://www.runoob.com/matplotlib-imsave.html)
			[Matplotlib 中文显示](https://www.runoob.com/matplotlib-zh.html) **













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