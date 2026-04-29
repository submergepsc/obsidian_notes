# 空间优化简介 - OI Wiki

- Source: https://oi-wiki.org/misc/space-optimization/

# 空间优化简介

空间优化相关技巧在算法竞赛中不太常见，但仍有讨论价值．

## 信息熵

信息熵描述了存储数据所占用的空间下限，若实际可用的空间低于这个下限则必然损失信息．

定义

对随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义信息熵为

𝐻(𝑋)=−∑𝑥𝑃(𝑋=𝑥)log2⁡𝑃(𝑋=𝑥).H(X)=−∑xP(X=x)log2⁡P(X=x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

定义中对数底数为 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是因为计算机中存储的信息每位只有 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种取值：00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

例如设 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 服从 {1,2,…,𝑛}{1,2,…,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的均匀分布，则其信息熵为

𝐻(𝑋)=−𝑛∑𝑖=11𝑛log2⁡1𝑛=log2⁡𝑛,H(X)=−∑i=1n1nlog2⁡1n=log2⁡n,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以我们至少需要 log2⁡𝑛log2⁡n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位来存储 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数．

### 例题

[[WC2022] 猜词](https://www.luogu.com.cn/problem/P8079)

交互题，你需要在有限次数内猜一个 5 个字母的单词．每次猜测都需要猜一个词库中存在的单词．如果猜对了，游戏结束；在每次猜错后，交互库会返回哪些字母的位置是正确的，以及哪些字母在待猜单词中出现了但位置是错误的．

解法

参见 [用信息论解 Wordle 谜题 - 3Blue1Brown](https://www.bilibili.com/video/BV1zZ4y1k7Jw)．

考虑计算信息熵，显然每次猜词时选择信息熵高的词可使得期望猜词次数尽可能小．

由于本题在猜测之前给出了答案首字母，所以我们可以预处理出每种首字母的最优猜测．

另外若剩余的词很少的话，我们可以考虑优先输出可能是答案的词，从而减小次数．

## 常见技巧

### 避免存储不必要的数据

例如：

  * 在 [可持久化线段树](../../ds/persistent-seg/) 中，由于单次修改只会产生 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个新结点，所以我们不需要把每个版本的线段树都完整地存储下来，只需要记录新结点即可．
  * 考虑 [图的存储](../../graph/save/)，对稀疏图来说，若使用邻接矩阵则会存储大量无用的 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以一般使用邻接表存稀疏图．
  * `bool` 数组的每个元素均会占用一个字节的空间，必要时可用每个元素只占用一位的 `std::vector<bool>` 或 [bitset](../../lang/csl/bitset/) 代替．
  * 在 [背包 DP](../../dp/knapsack/) 中，对 01 背包而言，每次计算 DP 值只会用到上一次计算时的数据，所以我们可以用滚动数组优化空间，只需要记录当前 DP 值即可．

### 利用数据特性

考虑支持路径压缩和启发式合并的 [并查集](../../ds/dsu/)，传统做法需要两个数组，分别记录父结点编号和子树大小．

注意到：

  1. 在应用了路径压缩后，对于并查集中的一棵树，我们只需要记录根结点对应的子树大小．
  2. 根结点的父亲一定是自己．

我们可以利用有符号整数的特性，用负数表示根结点，正数表示非根结点，所以我们只需一个数组即可实现支持路径压缩和启发式合并的并查集．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` |  ```text #include <cstdint> #include <vector> using i32 = int32_t ; using u32 = uint32_t ; class dsu { // p[i] < 0 时表示 i 为根节点，其对应的子树大小为 -p[i] // p[i] >= 0 时表示 i 不为根节点，其父亲节点的编号为 p[i] std :: vector < i32 > p ; public : // 节点编号从 0 到 sz-1 explicit dsu ( u32 sz ) : p ( sz , -1 ) {} i32 find ( u32 x ) { return p [ x ] < 0 ? ( i32 ) x : p [ x ] = find (( u32 ) p [ x ]); } u32 size ( u32 x ) { return ( u32 ) \- p [( u32 ) find ( x )]; } bool same_root ( u32 x , u32 y ) { return find ( x ) == find ( y ); } bool merge ( u32 x , u32 y ) { if (( x = ( u32 ) find ( x )) == ( y = ( u32 ) find ( y ))) return false ; if ( p [ x ] > p [ y ]) std :: swap ( x , y ); // 启发式合并 p [ x ] += p [ y ], p [ y ] = ( i32 ) x ; return true ; } }; ```   
---|---  
  
## 习题

  * [QOJ 6669 Mapa](https://qoj.ac/problem/6669)
  * [[SDOI/SXOI2022] 无处存储](https://www.luogu.com.cn/problem/P8353)

## 参考资料与拓展阅读

  1. 陈知轩．《浅谈信息学竞赛中的空间优化问题》．2022 国家集训队论文
  2. [Information theory - Wikipedia](https://en.wikipedia.org/wiki/Information_theory)
  3. [浅谈信息论 - 洛谷专栏](https://www.luogu.com.cn/article/i65ca8i5)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/space-optimization.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/space-optimization.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [cn-Mouxy](https://github.com/cn-Mouxy)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
