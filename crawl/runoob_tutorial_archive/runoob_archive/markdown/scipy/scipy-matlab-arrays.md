# SciPy Matlab 数组

- Source: https://www.runoob.com/scipy/scipy-matlab-arrays.html

NumPy 提供了 Python 可读格式的数据保存方法。


SciPy 提供了与 Matlab 的交互的方法。


SciPy 的 scipy.io 模块提供了很多函数来处理 Matlab 的数组。


### 以 Matlab 格式导出数据


**savemat()** 方法可以导出 Matlab 格式的数据。


该方法参数有：


- **filename** - 保存数据的文件名。
- **mdict** - 包含数据的字典。
- **do_compression** - 布尔值，指定结果数据是否压缩。默认为 False。


将数组作为变量 "vec" 导出到 mat 文件：


## 实例


```python
from scipy import io
import numpy as np

arr = np.arange(10)

io.savemat('arr.mat', {"vec": arr})
```


**注意：**上面的代码会在您的计算机上保存了一个名为 "arr.mat" 的文件。


### 导入 Matlab 格式数据


loadmat() 方法可以导入 Matlab 格式数据。


该方法参数：


- **filename** - 保存数据的文件名。


返回一个结构化数组，其键是变量名，对应的值是变量值。


以下实例从 mat 文件中导入数组：


## 实例


```python
from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

# 导出
io.savemat('arr.mat', {"vec": arr})

# 导入
mydata = io.loadmat('arr.mat')

print(mydata)
```


返回结果如下：


```
{
   '__header__': b'MATLAB 5.0 MAT-file Platform: nt, Created on: Tue Sep 22 13:12:32 2020',
   '__version__': '1.0',
   '__globals__': [],
   'vec': array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
 }
```


使用变量名 "vec" 只显示 matlab 数据的数组：


## 实例


```python
from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

# 导出
io.savemat('arr.mat', {"vec": arr})

# 导入
mydata = io.loadmat('arr.mat')

print(mydata['vec'])
```


返回结果如下：


```
[[0 1 2 3 4 5 6 7 8 9]]
```


从结果可以看出数组最初是一维的，但在提取时它增加了一个维度，变成了二维数组。

解决这个问题可以传递一个额外的参数 **squeeze_me=True**：


## 实例


```python
from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

# 导出
io.savemat('arr.mat', {"vec": arr})

# 导入
mydata = io.loadmat('arr.mat', squeeze_me=True)

print(mydata['vec'])
```


返回结果如下：


```
[0 1 2 3 4 5 6 7 8 9]
```









	  AI 思考中...





			** [SciPy 空间数据](https://www.runoob.com/scipy-spatial-data.html)
			[SciPy 插值](https://www.runoob.com/scipy-interpolation.html) **













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