# 点/边连通度 - OI Wiki

- Source: https://oi-wiki.org/graph/connectivity/

# 点/边连通度

## 定义

以下内容的定义，请参见 [图论相关概念](../concept/)：

  * 边连通度、边割集；
  * 点连通度、点割集；
  * 团．

## 性质

### Whitney 不等式

**Whitney 不等式** （1932）给出了点连通度 𝜅κ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、边连通度 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和最小度 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的关系：

𝜅≤𝜆≤𝛿κ≤λ≤δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

直觉上，如果有一个大小为 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边割集，其中每一条边任选一个端点，就可以得到一个大小为 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点割集，所以第一个不等式成立．

与度最小的结点（如有多个，任选一个）相邻的所有边构成大小为 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边割集，所以第二个不等式也成立．

这个不等式不能改进；换言之，对每个满足它的三元组，均可以找出满足这个三元组的图．

构造

把两个大小为 𝛿 +1δ+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的团用 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边连起来，使两个团分别有 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝜅κ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同的结点被连在这些边上．

### Menger 定理

由 [最大流最小割定理](../flow/min-cut/)（又名 Ford–Fulkerson 定理）可推出，两点间的不相交（指两两没有公共边）路径的最大数量等于割集的最小大小（这个推论又叫 **Menger 定理** ——译者注）．

## 计算

以下图的边权均为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 用最大流计算边连通度

枚举点对 (𝑠,𝑡)(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为源点，𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为汇点跑边权为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大流．需要 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次最大流，如果使用 Edmonds–Karp 算法，复杂度为 𝑂(|𝑉|3|𝐸|2)O(|V|3|E|2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．使用 Dinic 算法可以更优，复杂度为 𝑂(|𝑉|2|𝐸|min(|𝑉|2/3,|𝐸|1/2))O(|V|2|E|min(|V|2/3,|E|1/2))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 全局最小割

使用 [Stoer–Wagner 算法](../stoer-wagner/) 只需跑一次无源汇最小割即可．复杂度为 𝑂(|𝑉||𝐸| +|𝑉|2log⁡|𝑉|)O(|V||E|+|V|2log⁡|V|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，一般可近似看作 𝑂(|𝑉|3)O(|V|3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 点连通度

仍然枚举点对，这次把每个非源汇的点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 拆成两个点 𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并连边 (𝑥1,𝑥2)(x1,x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．把原图中所有边 (𝑢,𝑣)(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 换成两条边 (𝑢2,𝑣1)(u2,v1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑣2,𝑢1)(v2,u1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时最大流等于 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的最小点割集大小（又称局部点连通度）．复杂度与用最大流计算边连通度相同．

**本页面译自博文[Рёберная связность. Свойства и нахождение](http://e-maxx.ru/algo/rib_connectivity)、[Вершинная связность. Свойства и нахождение](http://e-maxx.ru/algo/vertex_connectivity) 与其英文翻译版 [Edge connectivity/Vertex connectivity](https://cp-algorithms.com/graph/edge_vertex_connectivity.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

## 延伸阅读

  * 论文 [_Connectivity Algorithms_](https://www.cse.msu.edu/~cse835/Papers/Graph_connectivity_revised.pdf) 介绍了近年来连通度计算算法的进展．感兴趣的读者可以自行浏览．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/connectivity.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/connectivity.md "edit.link.title")  
>  __本页面贡献者：[jifbt](https://github.com/jifbt), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [Mayuri0v0](https://github.com/Mayuri0v0), [mayuri0v0](https://github.com/mayuri0v0)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
