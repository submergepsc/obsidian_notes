# SciPy 图结构

- Source: https://www.runoob.com/scipy/scipy-graph.html

图结构是算法学中最强大的框架之一。


图是各种关系的节点和边的集合，节点是与对象对应的顶点，边是对象之间的连接。


SciPy 提供了 scipy.sparse.csgraph 模块来处理图结构。


### 邻接矩阵


邻接矩阵（Adjacency Matrix）是表示顶点之间相邻关系的矩阵。

邻接矩阵逻辑结构分为两部分：V 和 E 集合，其中，V 是顶点，E 是边，边有时会有权重，表示节点之间的连接强度。


![](https://www.runoob.com/wp-content/uploads/2021/08/undirected-graph.png)


用一个一维数组存放图中所有顶点数据，用一个二维数组存放顶点间关系（边或弧）的数据，这个二维数组称为邻接矩阵。


看下下图实例：


![](https://www.runoob.com/wp-content/uploads/2021/08/scipy_graph.png)


顶点有 A、B、C，边权重有 1 和 2。


A 与 B 是连接的，权重为 1。


A 与 C 是连接的，权重为 2。


C 与 B 是没有连接的。


这个邻接矩阵可以表示为以下二维数组：


```
A B C
   A:[0 1 2]
   B:[1 0 0]
   C:[2 0 0]
```


邻接矩阵又分为有向图邻接矩阵和无向图邻接矩阵。


无向图是双向关系，边没有方向：


![](https://www.runoob.com/wp-content/uploads/2021/08/GraphAdjacencyMatrix1.jpeg)

有向图的边带有方向，是单向关系：

![](https://www.runoob.com/wp-content/uploads/2021/08/GraphAdjacencyMatrix2.jpeg)


**注：**上面两个图中的 D 节点是自环，自环是指一条边的两端为同一个节点。


### 连接组件

查看所有连接组件使用 connected_components() 方法。


## 实例


```python
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(connected_components(newarr))
```


以上代码输出结果为：


```
(1, array([0, 0, 0], dtype=int32))
```


### Dijkstra -- 最短路径算法


Dijkstra(迪杰斯特拉)最短路径算法，用于计算一个节点到其他所有节点的最短路径。


Scipy 使用 dijkstra() 方法来计算一个元素到其他元素的最短路径。

dijkstra() 方法可以设置以下几个参数：

- **return_predecessors:** 布尔值，设置 True，遍历所有路径，如果不想遍历所有路径可以设置为 False。
- **indices:** 元素的索引，返回该元素的所有路径。
- **limit:** 路径的最大权重。


## 实例


查找元素 1 到 2 的最短路径：


```python
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(dijkstra(newarr, return_predecessors=True, indices=0))
```


以上代码输出结果为：


```
(array([ 0.,  1.,  2.]), array([-9999,     0,     0], dtype=int32))
```


### Floyd Warshall -- 弗洛伊德算法


弗洛伊德算法算法是解决任意两点间的最短路径的一种算法。

Scipy 使用 floyd_warshall() 方法来查找所有元素对之间的最短路径。


## 实例


查找所有元素对之间的最短路径径：


```python
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(floyd_warshall(newarr, return_predecessors=True))
```


以上代码输出结果为：


```
(array([[ 0.,  1.,  2.],
       [ 1.,  0.,  3.],
       [ 2.,  3.,  0.]]), array([[-9999,     0,     0],
       [    1, -9999,     0],
       [    2,     0, -9999]], dtype=int32))
```


### Bellman Ford -- 贝尔曼-福特算法

贝尔曼-福特算法是解决任意两点间的最短路径的一种算法。


Scipy 使用 bellman_ford() 方法来查找所有元素对之间的最短路径，通常可以在任何图中使用，包括有向图、带负权边的图。


## 实例


使用负权边的图查找从元素 1 到元素 2 的最短路径：


```python
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(bellman_ford(newarr, return_predecessors=True, indices=0))
```


以上代码输出结果为：


```
(array([ 0., -1.,  2.]), array([-9999,     0,     0], dtype=int32))
```


### 深度优先顺序

depth_first_order() 方法从一个节点返回深度优先遍历的顺序。


可以接收以下参数：


- 图
- 图开始遍历的元素


## 实例


给定一个邻接矩阵，返回深度优先遍历的顺序：


```python
import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(depth_first_order(newarr, 1))
```


以上代码输出结果为：


```
(array([1, 0, 3, 2], dtype=int32), array([    1, -9999,     1,     0], dtype=int32))
```


### 广度优先顺序

breadth_first_order() 方法从一个节点返回广度优先遍历的顺序。


可以接收以下参数：


- 图
- 图开始遍历的元素


## 实例


给定一个邻接矩阵，返回广度优先遍历的顺序：


```python
import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(breadth_first_order(newarr, 1))
```


以上代码输出结果为：


```
(array([1, 0, 2, 3], dtype=int32), array([    1, -9999,     1,     1], dtype=int32))
```









	  AI 思考中...





			** [SciPy 稀疏矩阵](https://www.runoob.com/scipy-sparse-matrix.html)
			[SciPy 空间数据](https://www.runoob.com/scipy-spatial-data.html) **













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