# 树上随机游走 - OI Wiki

- Source: https://oi-wiki.org/graph/tree-random-walk/

# 树上随机游走

给定一棵有根树，树的某个结点上有一个硬币，在某一时刻硬币会等概率地移动到邻接结点上，问硬币移动到邻接结点上的期望距离．

## 需要用到的定义

  * 𝑇 =(𝑉,𝐸)T=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7): 所讨论的树
  * 𝑑(𝑢)d(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7): 结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的度数
  * 𝑤(𝑢,𝑣)w(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7): 结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的边的边权
  * 𝑝𝑢pu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7): 结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的父结点
  * 𝑟𝑜𝑜𝑡root![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7): 树的根结点
  * 𝑠𝑜𝑛𝑢sonu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7): 结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子结点集合
  * 𝑠𝑖𝑏𝑙𝑖𝑛𝑔𝑢siblingu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7): 结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的兄弟结点集合

## 向父结点走的期望距离

设 𝑓(𝑢)f(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代表 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结点走到其父结点 𝑝𝑢pu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的期望距离，则有：

𝑓(𝑢)=𝑤(𝑢,𝑝𝑢)+∑𝑣∈𝑠𝑜𝑛𝑢(𝑤(𝑢,𝑣)+𝑓(𝑣)+𝑓(𝑢))𝑑(𝑢)f(u)=w(u,pu)+∑v∈sonu(w(u,v)+f(v)+f(u))d(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

分子中的前半部分代表直接走向了父结点，后半部分代表先走向了子结点再由子结点走回来然后再向父结点走；分母 𝑑(𝑢)d(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代表从 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结点走向其任何邻接点的概率相同．

化简如下：

𝑓(𝑢)=𝑤(𝑢,𝑝𝑢)+∑𝑣∈𝑠𝑜𝑛𝑢(𝑤(𝑢,𝑣)+𝑓(𝑣)+𝑓(𝑢))𝑑(𝑢)=𝑤(𝑢,𝑝𝑢)+∑𝑣∈𝑠𝑜𝑛𝑢(𝑤(𝑢,𝑣)+𝑓(𝑣))+(𝑑(𝑢)−1)𝑓(𝑢)𝑑(𝑢)=𝑤(𝑢,𝑝𝑢)+∑𝑣∈𝑠𝑜𝑛𝑢(𝑤(𝑢,𝑣)+𝑓(𝑣))=∑(𝑢,𝑡)∈𝐸𝑤(𝑢,𝑡)+∑𝑣∈𝑠𝑜𝑛𝑢𝑓(𝑣)f(u)=w(u,pu)+∑v∈sonu(w(u,v)+f(v)+f(u))d(u)=w(u,pu)+∑v∈sonu(w(u,v)+f(v))+(d(u)−1)f(u)d(u)=w(u,pu)+∑v∈sonu(w(u,v)+f(v))=∑(u,t)∈Ew(u,t)+∑v∈sonuf(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于叶子结点 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，初始状态为 𝑓(𝑙) =𝑤(𝑝𝑙,𝑙)f(l)=w(pl,l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

当树上所有边的边权都为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，上式可化为：

𝑓(𝑢)=𝑑(𝑢)+∑𝑣∈𝑠𝑜𝑛𝑢𝑓(𝑣)f(u)=d(u)+∑v∈sonuf(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 子树的所有结点的度数和，也即 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 子树大小的两倍 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（每个结点连向其父亲的边都有且只有一条，除 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑝𝑢pu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的边只有 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点度数的贡献外，每条边会产生 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点度数的贡献）．

## 向子结点走的期望距离

设 𝑔(𝑢)g(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代表 𝑝𝑢pu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结点走到其子结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的期望距离，则有：

𝑔(𝑢)=𝑤(𝑝𝑢,𝑢)+(𝑤(𝑝𝑢,𝑝𝑝𝑢)+𝑔(𝑝𝑢)+𝑔(𝑢))+∑𝑠∈𝑠𝑖𝑏𝑙𝑖𝑛𝑔𝑢(𝑤(𝑝𝑢,𝑠)+𝑓(𝑠)+𝑔(𝑢))𝑑(𝑝𝑢)g(u)=w(pu,u)+(w(pu,ppu)+g(pu)+g(u))+∑s∈siblingu(w(pu,s)+f(s)+g(u))d(pu)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

分子中的第一部分代表直接走向了子结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，第二部分代表先走向了父结点再由父结点走回来然后再向 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结点走，第三部分代表先走向 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结点的兄弟结点再由其走回来然后再向 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结点走；分母 𝑑(𝑝𝑢)d(pu)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代表从 𝑝𝑢pu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结点走向其任何邻接点的概率相同．

化简如下：

𝑔(𝑢)=𝑤(𝑝𝑢,𝑢)+(𝑤(𝑝𝑢,𝑝𝑝𝑢)+𝑔(𝑝𝑢)+𝑔(𝑢))+∑𝑠∈𝑠𝑖𝑏𝑙𝑖𝑛𝑔𝑢(𝑤(𝑝𝑢,𝑠)+𝑓(𝑠)+𝑔(𝑢))𝑑(𝑝𝑢)=𝑤(𝑝𝑢,𝑢)+𝑤(𝑝𝑢,𝑝𝑝𝑢)+𝑔(𝑝𝑢)+∑𝑠∈𝑠𝑖𝑏𝑙𝑖𝑛𝑔𝑢(𝑤(𝑝𝑢,𝑠)+𝑓(𝑠))+(𝑑(𝑝𝑢)−1)𝑔(𝑢)𝑑(𝑝𝑢)=𝑤(𝑝𝑢,𝑢)+𝑤(𝑝𝑢,𝑝𝑝𝑢)+𝑔(𝑝𝑢)+∑𝑠∈𝑠𝑖𝑏𝑙𝑖𝑛𝑔𝑢(𝑤(𝑝𝑢,𝑠)+𝑓(𝑠))=∑(𝑝𝑢,𝑡)∈𝐸𝑤(𝑝𝑢,𝑡)+𝑔(𝑝𝑢)+∑𝑠∈𝑠𝑖𝑏𝑙𝑖𝑛𝑔𝑢𝑓(𝑠)=∑(𝑝𝑢,𝑡)∈𝐸𝑤(𝑝𝑢,𝑡)+𝑔(𝑝𝑢)+⎛⎜ ⎜⎝𝑓(𝑝𝑢)−∑(𝑝𝑢,𝑡)∈𝐸𝑤(𝑝𝑢,𝑡)−𝑓(𝑢)⎞⎟ ⎟⎠=𝑔(𝑝𝑢)+𝑓(𝑝𝑢)−𝑓(𝑢)g(u)=w(pu,u)+(w(pu,ppu)+g(pu)+g(u))+∑s∈siblingu(w(pu,s)+f(s)+g(u))d(pu)=w(pu,u)+w(pu,ppu)+g(pu)+∑s∈siblingu(w(pu,s)+f(s))+(d(pu)−1)g(u)d(pu)=w(pu,u)+w(pu,ppu)+g(pu)+∑s∈siblingu(w(pu,s)+f(s))=∑(pu,t)∈Ew(pu,t)+g(pu)+∑s∈siblinguf(s)=∑(pu,t)∈Ew(pu,t)+g(pu)+(f(pu)−∑(pu,t)∈Ew(pu,t)−f(u))=g(pu)+f(pu)−f(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

初始状态为 𝑔(root) =0g(root)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 代码实现（以无权树为例）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text vector < int > G [ MAXN ]; void dfs1 ( int u , int p ) { f [ u ] = G [ u ]. size (); for ( auto v : G [ u ]) { if ( v == p ) continue ; dfs1 ( v , u ); f [ u ] += f [ v ]; } } void dfs2 ( int u , int p ) { if ( u != root ) g [ u ] = g [ p ] \+ f [ p ] \- f [ u ]; for ( auto v : G [ u ]) { if ( v == p ) continue ; dfs2 ( v , u ); } } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/tree-random-walk.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/tree-random-walk.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [StableAgOH](https://github.com/StableAgOH), [aofall](https://github.com/aofall), [CJTracer](https://github.com/CJTracer), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Marcythm](https://github.com/Marcythm), [Persdre](https://github.com/Persdre), [shuzhouliu](https://github.com/shuzhouliu)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
