# SciPy 稀疏矩阵

- Source: https://www.runoob.com/scipy/scipy-sparse-matrix.html

稀疏矩阵（英语：sparse matrix）指的是在数值分析中绝大多数数值为零的矩阵。反之，如果大部分元素都非零，则这个矩阵是稠密的(Dense)。


在科学与工程领域中求解线性模型时经常出现大型的稀疏矩阵。


![](https://www.runoob.com/wp-content/uploads/2021/08/v2-d4b2cc03d5461fac7c9912aa4fe321b7_b.gif)


上图中左边就是一个稀疏矩阵，可以看到包含了很多 0 元素，右边是稠密的矩阵，大部分元素不是 0。


看一个简单例子：


![](https://static.jyshare.com/images/mix/1b9870651e865fa547146703a5db81c0546051b0.svg)


上述稀疏矩阵仅包含 9 个非零元素，另外包含 26 个零元。其稀疏度为 74%，密度为 26%。


SciPy 的 **scipy.sparse** 模块提供了处理稀疏矩阵的函数。


我们主要使用以下两种类型的稀疏矩阵：


- CSC - 压缩稀疏列（Compressed Sparse Column），按列压缩。
- CSR - 压缩稀疏行（Compressed Sparse Row），按行压缩。


本章节我们主要使用 CSR 矩阵。


### CSR 矩阵


我们可以通过向 **scipy.sparse.csr_matrix()** 函数传递数组来创建一个 CSR 矩阵。


## 实例

创建 CSR 矩阵。
```python
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))
```
 以上代码输出结果为：


```
(0, 5)        1
  (0, 6)        1
  (0, 8)        2
```


**结果解析：**


- 第一行：在矩阵第一行（索引值 0 ）第六（索引值 5 ）个位置有一个数值 1。
- 第二行：在矩阵第一行（索引值 0 ）第七（索引值 6 ）个位置有一个数值 1。
- 第三行：在矩阵第一行（索引值 0 ）第九（索引值 8 ）个位置有一个数值 2。


### CSR 矩阵方法


我们可以使用 **data** 属性查看存储的数据（不含 0 元素）：


## 实例


```python
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).data)
```


以上代码输出结果为：


```
[1 1 2]
```


使用 **count_nonzero()** 方法计算非 0 元素的总数：


## 实例


```python
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).count_nonzero())
```


以上代码输出结果为：


```
3
```


使用 **eliminate_zeros()** 方法删除矩阵中 0 元素：


## 实例


```python
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat = csr_matrix(arr)
mat.eliminate_zeros()

print(mat)
```


以上代码输出结果为：


```
(1, 2)    1
  (2, 0)    1
  (2, 2)    2
```


使用 sum_duplicates() 方法来删除重复项:


## 实例


```python
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat = csr_matrix(arr)
mat.sum_duplicates()

print(mat)
```


以上代码输出结果为：


```
(1, 2)    1
  (2, 0)    1
  (2, 2)    2
```


csr 转换为 csc 使用 tocsc() 方法：


## 实例


```python
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

newarr = csr_matrix(arr).tocsc()

print(newarr)
```


```
(2, 0)    1
  (1, 2)    1
  (2, 2)    2
```









	  AI 思考中...





			** [SciPy 优化器](https://www.runoob.com/scipy-optimize.html)
			[SciPy 图结构](https://www.runoob.com/scipy-graph.html) **













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