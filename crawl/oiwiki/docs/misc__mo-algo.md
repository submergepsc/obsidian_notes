# 普通莫队算法 - OI Wiki

- Source: https://oi-wiki.org/misc/mo-algo/

# 普通莫队算法

## 形式

假设 𝑛 =𝑚n=m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么对于序列上的区间询问问题，如果从 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的答案能够 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 扩展到 [𝑙 −1,𝑟],[𝑙 +1,𝑟],[𝑙,𝑟 +1],[𝑙,𝑟 −1][l−1,r],[l+1,r],[l,r+1],[l,r−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即与 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相邻的区间）的答案，那么可以在 𝑂(𝑛√𝑛)O(nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度内求出所有询问的答案．

## 解释

离线后排序，顺序处理每个询问，暴力从上一个区间的答案转移到下一个区间答案（一步一步移动即可）．

## 排序方法

对于区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 以 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在块的编号为第一关键字，𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为第二关键字从小到大排序．

## 实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text void move ( int pos , int sign ) { // update nowAns } void solve () { BLOCK_SIZE = int ( ceil ( pow ( n , 0.5 ))); sort ( querys , querys \+ m ); for ( int i = 0 ; i < m ; ++ i ) { const query & q = querys [ i ]; while ( l > q . l ) move ( \-- l , 1 ); while ( r < q . r ) move ( ++ r , 1 ); while ( l < q . l ) move ( l ++ , -1 ); while ( r > q . r ) move ( r \-- , -1 ); ans [ q . id ] = nowAns ; } } ```   
---|---  
  
## 复杂度分析

以下的情况在 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同阶的前提下讨论．

首先是分块这一步，这一步的时间复杂度是 𝑂(√𝑛 ⋅√𝑛log⁡√𝑛 +𝑛log⁡𝑛) =𝑂(𝑛log⁡𝑛)O(n⋅nlog⁡n+nlog⁡n)=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

接着就到了莫队算法的精髓了，下面我们用通俗易懂的初中方法来证明它的时间复杂度是 𝑂(𝑛√𝑛)O(nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

证：令每一块中 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大值为 max1,max2,max3,⋯,max⌈√𝑛⌉max1,max2,max3,⋯,max⌈n⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由第一次排序可知，max1 ≤max2 ≤⋯ ≤max⌈√𝑛⌉max1≤max2≤⋯≤max⌈n⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

显然，对于每一块暴力求出第一个询问的时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑最坏的情况，在每一块中，𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大值均为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每次修改操作均要将 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 由 max𝑖−1maxi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 修改至 max𝑖maxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或由 max𝑖maxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 修改至 max𝑖−1maxi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：因为 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在块中已经排好序，所以在同一块修改完它的时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于所有块就是 𝑂(𝑛√𝑛)O(nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

重点分析 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：因为每一次改变的时间复杂度都是 𝑂(max𝑖 −max𝑖−1)O(maxi−maxi−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，所以在同一块中时间复杂度为 𝑂(√𝑛 ⋅(max𝑖 −max𝑖−1))O(n⋅(maxi−maxi−1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

将每一块 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度合在一起，可以得到：

对于 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的总时间复杂度为

𝑂(√𝑛(max1−1)+√𝑛(max2−max1)+√𝑛(max3−max2)+⋯+√𝑛(max⌈√𝑛⌉−max⌈√𝑛⌉−1))=𝑂(√𝑛⋅(max1−1+max2−max1+max3−max2+⋯+max⌈√𝑛⌉−1−max⌈√𝑛⌉−2+max⌈√𝑛⌉−max⌈√𝑛⌉−1))=𝑂(√𝑛⋅(max⌈√𝑛⌉−1))O(n(max1−1)+n(max2−max1)+n(max3−max2)+⋯+n(max⌈n⌉−max⌈n⌉−1))=O(n⋅(max1−1+max2−max1+max3−max2+⋯+max⌈n⌉−1−max⌈n⌉−2+max⌈n⌉−max⌈n⌉−1))=O(n⋅(max⌈n⌉−1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

（裂项求和）

由题可知 max⌈√𝑛⌉max⌈n⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最大为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的总时间复杂度最坏情况下为 𝑂(𝑛√𝑛)O(nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

综上所述，莫队算法的时间复杂度为 𝑂(𝑛√𝑛)O(nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

但是对于 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的其他取值，如 𝑚 <𝑛m<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，分块方式需要改变才能变的更优．

怎么分块呢？

我们设块长度为 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么对于任意多个在同一块内的询问，挪动的距离就是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，一共 𝑛𝑆nS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个块，移动的总次数就是 𝑛2𝑆n2S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，移动可能跨越块，所以还要加上一个 𝑚𝑆mS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度，总复杂度为 𝑂(𝑛2𝑆+𝑚𝑆)O(n2S+mS)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们要让这个值尽量小，那么就要将这两个项尽量相等，发现 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取 𝑛√𝑚nm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是最优的，此时复杂度为 𝑂⎛⎜ ⎜ ⎜ ⎜ ⎜⎝𝑛2𝑛√𝑚+𝑚(𝑛√𝑚)⎞⎟ ⎟ ⎟ ⎟ ⎟⎠ =𝑂(𝑛√𝑚)O(n2nm+m(nm))=O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

事实上，如果块长度的设定不准确，则莫队的时间复杂度会受到很大影响．例如，如果 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同阶，并且块长误设为 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则可以很容易构造出一组数据使其时间复杂度为 𝑂(𝑛√𝑛)O(nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而不是正确的 𝑂(𝑛5/4)O(n5/4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

莫队算法看起来十分暴力，很大程度上是因为莫队算法的分块排序方法看起来很粗糙．我们会想到通过看上去更精细的排序方法对所有区间排序．一种方法是把所有区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 看成平面上的点 (𝑙,𝑟)(l,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并对所有点建立曼哈顿最小生成树，每次沿着曼哈顿最小生成树的边在询问之间转移答案．这样看起来可以改善莫队算法的时间复杂度，但是实际上对询问分块排序的方法的时间复杂度上界已经是最优的了．

假设 𝑛,𝑚n,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同阶且 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全平方数．我们考虑形如 [𝑎√𝑛,𝑏√𝑛](1 ≤𝑎,𝑏 ≤√𝑛)[an,bn](1≤a,b≤n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的区间，这样的区间一共有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．如果把所有的区间看成平面上的点，则两点之间的曼哈顿距离恰好为两区间的转移代价，并且任意两个区间之间的最小曼哈顿距离为 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以处理所有询问的时间复杂度最小为 𝑂(𝑛√𝑛)O(nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．其它情况的数据构造方法与之类似．

莫队算法还有一个特点：当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不变时，𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 越大，处理每次询问的平均转移代价就越小．一些其他的离线算法也具有同样的特点（如求 LCA 的 Tarjan 算法），但是莫队算法的平均转移代价随 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的变化最明显．

## 例题 & 代码

例题 [「国家集训队」小 Z 的袜子](https://www.luogu.com.cn/problem/P1494)

题目大意：

有一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列 {𝑐𝑖}{ci}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．现在给出 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个询问，每次给出两个数 𝑙,𝑟l,r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从编号在 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的数中随机选出两个不同的数，求两个数相等的概率．

### 过程

思路：莫队算法模板题．

对于区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在块的编号为第一关键字，𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为第二关键字从小到大排序．

然后从序列的第一个询问开始计算答案，第一个询问通过直接暴力算出，复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，后面的询问在前一个询问的基础上得到答案．

具体做法：

对于区间 [𝑖,𝑖][i,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由于区间只有一个元素，我们很容易就能知道答案．然后一步一步从当前区间（已知答案）向下一个区间靠近．

我们设 𝑐𝑜𝑙[𝑖]col[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示当前颜色 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出现了多少次，𝑎𝑛𝑠ans![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示当前共有多少种可行的配对方案（有多少种可以选到一双颜色相同的袜子）．然后每次移动的时候更新答案：设当前颜色为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果是增长区间就是 𝑎𝑛𝑠ans![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加上 (𝑐𝑜𝑙[𝑘]+12) −(𝑐𝑜𝑙[𝑘]2)(col[k]+12)−(col[k]2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；如果是缩短就是 𝑎𝑛𝑠ans![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 减去 (𝑐𝑜𝑙[𝑘]2) −(𝑐𝑜𝑙[𝑘]−12)(col[k]2)−(col[k]−12)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这个询问的答案就是 𝑎𝑛𝑠(𝑟−𝑙+12)ans(r−l+12)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这里有个优化：(𝑎2) =𝑎(𝑎−1)2(a2)=a(a−1)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

所以 (𝑎+12) −(𝑎2) =(𝑎+1)𝑎2 −𝑎(𝑎−1)2 =𝑎2 ⋅(𝑎 +1 −𝑎 +1) =𝑎2 ⋅2 =𝑎(a+12)−(a2)=(a+1)a2−a(a−1)2=a2⋅(a+1−a+1)=a2⋅2=a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

所以 (𝑐𝑜𝑙[𝑘]+12) −(𝑐𝑜𝑙[𝑘]2) =𝑐𝑜𝑙[𝑘](col[k]+12)−(col[k]2)=col[k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

算法总复杂度：𝑂(𝑛√𝑛)O(nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

下面的代码中 `deno` 表示答案的分母 (denominator)，`nume` 表示分子 (numerator)，`sqn` 表示块的大小：√𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，`arr` 是输入的数组，`node` 是存储询问的结构体，`tab` 是询问序列（排序后的），`col` 同上所述．

**注意：由于`++l` 和 `--r` 的存在，下面代码中的移动区间的 4 个 while 循环的位置很关键，不能随意改变它们之间的位置关系．**

关于四个循环位置的讨论

莫队区间的移动过程，就相当于加入了 [1,𝑟][1,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素，并删除了 [1,𝑙 −1][1,l−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素．因此，

  * 对于 𝑙 ≤𝑟l≤r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况，[1,𝑙 −1][1,l−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素相当于被加入了一次又被删除了一次，[𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素被加入一次，[𝑟 +1, +∞)[r+1,+∞)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素没有被加入．这个区间是合法区间．
  * 对于 𝑙 =𝑟 +1l=r+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况，[1,𝑟][1,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素相当于被加入了一次又被删除了一次，[𝑟 +1, +∞)[r+1,+∞)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素没有被加入．这时这个区间表示空区间．
  * 对于 𝑙 >𝑟 +1l>r+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况，那么 [𝑟 +1,𝑙 −1][r+1,l−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（这个区间非空）的元素被删除了一次但没有被加入，因此这个元素被加入的次数是负数．

因此，如果某时刻出现 𝑙 >𝑟 +1l>r+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况，那么会存在一个元素，它的加入次数是负数．这在某些题目会出现问题，例如我们如果用一个 `set` 维护区间中的所有数，就会出现「需要删除 `set` 中不存在的元素」的问题．

代码中的四个 while 循环一共有 4! =244!=24![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种排列顺序．不妨设第一个循环用于操作左端点，就有以下 1212![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种排列（另外 1212![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种是对称的）．下表列出了这 12 种写法的正确性，还给出了错误写法的反例．

循环顺序| 正确性| 反例或注释  
---|---|---  
`l--,l++,r--,r++`| 错误| 𝑙 <𝑟 <𝑙′ <𝑟′l<r<l′<r′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`l--,l++,r++,r--`| 错误| 𝑙 <𝑟 <𝑙′ <𝑟′l<r<l′<r′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`l--,r--,l++,r++`| 错误| 𝑙 <𝑟 <𝑙′ <𝑟′l<r<l′<r′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`l--,r--,r++,l++`| 正确| 证明较繁琐  
`l--,r++,l++,r--`| 正确|   
`l--,r++,r--,l++`| 正确|   
`l++,l--,r--,r++`| 错误| 𝑙 <𝑟 <𝑙′ <𝑟′l<r<l′<r′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`l++,l--,r++,r--`| 错误| 𝑙 <𝑟 <𝑙′ <𝑟′l<r<l′<r′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`l++,r++,l--,r--`| 错误| 𝑙 <𝑟 <𝑙′ <𝑟′l<r<l′<r′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`l++,r++,r--,l--`| 错误| 𝑙 <𝑟 <𝑙′ <𝑟′l<r<l′<r′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`l++,r--,l--,r++`| 错误| 𝑙 <𝑟 <𝑙′ <𝑟′l<r<l′<r′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`l++,r--,r++,l--`| 错误| 𝑙 <𝑟 <𝑙′ <𝑟′l<r<l′<r′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
  
全部 24 种排列中只有 6 种是正确的，其中有 2 种的证明较繁琐，这里只给出其中 4 种的证明．

这 4 种正确写法的共同特点是，前两步先扩大区间（`l--` 或 `r++`），后两步再缩小区间（`l++` 或 `r--`）．这样写，前两步是扩大区间，可以保持 𝑙 ≤𝑟 +1l≤r+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；执行完前两步后，𝑙 ≤𝑙′ ≤𝑟′ ≤𝑟l≤l′≤r′≤r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定成立，再执行后两步只会把区间缩小到 [𝑙′,𝑟′][l′,r′]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，依然有 𝑙 ≤𝑟 +1l≤r+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此这样写是正确的．

### 实现

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 ``` |  ```text #include <algorithm> #include <cmath> #include <iostream> using namespace std ; constexpr int N = 50005 ; int n , m , maxn ; int c [ N ]; long long sum ; int cnt [ N ]; long long ans1 [ N ], ans2 [ N ]; struct query { int l , r , id ; bool operator < ( const query & x ) const { // 重载<运算符 if ( l / maxn != x . l / maxn ) return l < x . l ; return ( l / maxn ) & 1 ? r < x . r : r > x . r ; } } a [ N ]; void add ( int i ) { sum += cnt [ i ]; cnt [ i ] ++ ; } void del ( int i ) { cnt [ i ] \-- ; sum -= cnt [ i ]; } long long gcd ( long long a , long long b ) { return b ? gcd ( b , a % b ) : a ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> m ; maxn = sqrt ( n ); for ( int i = 1 ; i <= n ; i ++ ) cin >> c [ i ]; for ( int i = 0 ; i < m ; i ++ ) cin >> a [ i ]. l >> a [ i ]. r , a [ i ]. id = i ; sort ( a , a \+ m ); for ( int i = 0 , l = 1 , r = 0 ; i < m ; i ++ ) { // 具体实现 if ( a [ i ]. l == a [ i ]. r ) { ans1 [ a [ i ]. id ] = 0 , ans2 [ a [ i ]. id ] = 1 ; continue ; } while ( l > a [ i ]. l ) add ( c [ \-- l ]); while ( r < a [ i ]. r ) add ( c [ ++ r ]); while ( l < a [ i ]. l ) del ( c [ l ++ ]); while ( r > a [ i ]. r ) del ( c [ r \-- ]); ans1 [ a [ i ]. id ] = sum ; ans2 [ a [ i ]. id ] = ( long long )( r \- l \+ 1 ) * ( r \- l ) / 2 ; } for ( int i = 0 ; i < m ; i ++ ) { if ( ans1 [ i ] != 0 ) { long long g = gcd ( ans1 [ i ], ans2 [ i ]); ans1 [ i ] /= g , ans2 [ i ] /= g ; } else ans2 [ i ] = 1 ; cout << ans1 [ i ] << '/' << ans2 [ i ] << '\n' ; } return 0 ; } ```   
---|---  
  
## 普通莫队的优化

### 过程

我们看一下下面这组数据

```text 1 2 3 4 5 ``` |  ```text // 设块的大小为 2 (假设) 1 1 2 100 3 1 4 100 ```   
---|---  
  
手动模拟一下可以发现，r 指针的移动次数大概为 300 次，我们处理完第一个块之后，𝑙 =2,𝑟 =100l=2,r=100![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时只需要移动两次 l 指针就可以得到第四个询问的答案，但是我们却将 r 指针移动到 1 来获取第三个询问的答案，再移动到 100 获取第四个询问的答案，这样多了九十几次的指针移动．我们怎么优化这个地方呢？这里我们就要用到奇偶化排序．

什么是奇偶化排序？奇偶化排序即对于属于奇数块的询问，r 按从小到大排序，对于属于偶数块的排序，r 从大到小排序，这样我们的 r 指针在处理完这个奇数块的问题后，将在返回的途中处理偶数块的问题，再向 n 移动处理下一个奇数块的问题，优化了 r 指针的移动次数，一般情况下，这种优化能让程序快 30% 左右．

### 实现

排序代码：

压行不压行

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text // clang-format off // 这里有个小细节等下会讲 int unit ; // 块的大小 struct node { int l , r , id ; bool operator < ( const node & x ) const { return l / unit == x . l / unit ? ( r == x . r ? 0 : (( l / unit ) & 1 ) ^ ( r < x . r )) : l < x . l ; } }; ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text struct node { int l , r , id ; bool operator < ( const node & x ) const { if ( l / unit != x . l / unit ) return l < x . l ; // 注意下面两行不能写小于（大于）等于，否则会出错（详见下面的小细节） if (( l / unit ) & 1 ) return r < x . r ; return r > x . r ; } }; ```   
---|---  
  
小细节

如果使用 `sort` 比较两个结构体，不能出现 𝑎 <𝑏a<b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏 <𝑎b<a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同时为真的情况，否则会运行错误，详见 [常见错误](../../contest/common-mistakes/#会导致-re)．

对于压行版，如果没有 `r == x.r` 的特判，当 l 属于同一奇数块且 r 相等时，会出现上面小细节中的问题（自己手动模拟一下），对于不压行版，如果写成小于（大于）等于，则也会出现同样的问题．

## 参考资料

  * [莫队算法学习笔记 | Sengxian's Blog](https://blog.sengxian.com/algorithms/mo-s-algorithm)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/mo-algo.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/mo-algo.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [countercurrent-time](https://github.com/countercurrent-time), [Backl1ght](https://github.com/Backl1ght), [H-J-Granger](https://github.com/H-J-Granger), [mgt](mailto:i@margatroid.xyz), [NachtgeistW](https://github.com/NachtgeistW), [Tiphereth-A](https://github.com/Tiphereth-A), [akakw1](https://github.com/akakw1), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [Enter-tainer](https://github.com/Enter-tainer), [AngelKitty](https://github.com/AngelKitty), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [greyqz](https://github.com/greyqz), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [MicDZ](https://github.com/MicDZ), [minghu6](https://github.com/minghu6), [ouuan](https://github.com/ouuan), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [Xeonacid](https://github.com/Xeonacid), [AtomAlpaca](https://github.com/AtomAlpaca), [cesonic](https://github.com/cesonic), [Chrogeek](https://github.com/Chrogeek), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [GuanghaoYe](https://github.com/GuanghaoYe), [Henry-ZHR](https://github.com/Henry-ZHR), [HeRaNO](https://github.com/HeRaNO), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [konnyakuxzy](https://github.com/konnyakuxzy), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [leoleoasd](https://github.com/leoleoasd), [lychees](https://github.com/lychees), [Menci](https://github.com/Menci), [MingqiHuang](mailto:hmq011212@163.com), [Peanut-Tang](https://github.com/Peanut-Tang), [renyancheng](https://github.com/renyancheng), [SukkaW](https://github.com/SukkaW), [Sweetlemon68](https://github.com/Sweetlemon68), [thallium](https://github.com/thallium), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
