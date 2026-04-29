# 零和游戏 - OI Wiki

- Source: https://oi-wiki.org/math/game-theory/zero-sum-game/

# 零和游戏

前置知识：[博弈论简介](../intro/)

本文讨论（二人）[零和游戏](../intro/#零和非零和博弈)．

在零和游戏中，两名玩家的收益之和恒为零，一方的收益必然意味着另一方的损失．零和游戏可以视为常和游戏的特殊情形．不过，任何常和游戏都可以通过对某一方的收益整体加上或减去一个常数，等价地转化为零和游戏，所以仅需要讨论零和游戏．

在算法竞赛中常见的零和游戏大致可分为两类：序贯零和游戏与同时零和游戏．

## 序贯零和游戏

序贯零和游戏中，两名玩家轮流行动，直到游戏终止．

序贯零和游戏中，玩家的收益函数呈现递归结构．游戏局面 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以分为三类，即终止局面 𝑆0S0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行动的局面 𝑆1S1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和玩家 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行动的局面 𝑆2S2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．假设终止局面 𝑠 ∈𝑆0s∈S0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处，玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的收益为 𝑣(𝑠)v(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，相应地，玩家 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的收益为 −𝑣(𝑠)−v(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，轮到玩家 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行动时，最大化它的收益就相当于最小化玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的收益．由此，假设双方都采取最优策略，玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在局面 𝑠 ∈𝑆s∈S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处能够获得的最大收益 𝑉(𝑠)V(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足如下递推关系：

𝑉(𝑠)=⎧{ {⎨{ {⎩𝑣(𝑠),𝑠∈𝑆0,max𝑡∈𝑠𝑉(𝑡),𝑠∈𝑆1,min𝑡∈𝑠𝑉(𝑡),𝑠∈𝑆2.V(s)={v(s),s∈S0,maxt∈sV(t),s∈S1,mint∈sV(t),s∈S2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑡 ∈𝑠t∈s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的后继局面．这就是 [极小化极大思想](../../../search/alpha-beta/#minimax-算法)．

将这一算法应用于实际问题中，通常有如下具体方法：

  * 如果游戏中涉及的局面数量较少，直接暴力实现这一算法即可．

  * 如果游戏中涉及的局面数量较为庞大且没有特殊结构，可以考虑 [Alpha–Beta 剪枝](../../../search/alpha-beta/#alphabeta-剪枝) 并结合其他搜索剪枝算法使用．

  * 如果游戏中单个局面经常是多个局面的后继局面，为避免重复搜索，可以考虑记忆化搜索或其他动态规划算法．

  * 如果游戏中玩家的最终收益是终局前所有行动的收益和，可以适当优化建模方式．具体地，假设到达终局 𝑠 ∈𝑆0s∈S0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，玩家 𝑖 =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的行动序列分别为 {𝑎(𝑖)𝑗}𝑘𝑖𝑗=1{aj(i)}j=1ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，行动 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的收益为 𝑤(𝑎)w(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的收益函数为

𝑣(𝑠)=𝑘1∑𝑗=1𝑤(𝑎(1)𝑗)−𝑘2∑𝑗=1𝑤(𝑎(2)𝑗).v(s)=∑j=1k1w(aj(1))−∑j=1k2w(aj(2)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么，可以设 ˜𝑉(𝑠)V~(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为当前玩家在局面 𝑠 ∈𝑆s∈S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之后的游戏中能够取得的最大分数．对于初始状态 𝑠0s0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑉(𝑠0) =˜𝑉(𝑠0)V(s0)=V~(s0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此求出 ˜𝑉( ⋅)V~(⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 足以求解原问题．对于 ˜𝑉( ⋅)V~(⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有如下递推关系：

˜𝑉(𝑠)={0,𝑠∈𝑆0,max𝑡∈𝑠𝑤(𝑎𝑠→𝑡)−˜𝑉(𝑡),𝑠∈𝑆1∪𝑆2.V~(s)={0,s∈S0,maxt∈sw(as→t)−V~(t),s∈S1∪S2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑎𝑠→𝑡as→t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示可以使得状态从 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转移到 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的行动，如果有多个这样的行动，取收益 𝑤(𝑎)w(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最高的那个．

  * 公平组合游戏都是序贯零和游戏，只需要设游戏中胜利方和失败方的收益分别为 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时，收益函数 𝑉( ⋅)V(⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的递推关系其实就是判定必胜状态和必败状态的 [引理](../impartial-game/#博弈图和状态)．

这类问题还有一种常见的变形，即求胜利方最少需要的回合数和失败方最多可以坚持的回合数．为此，只需要注意到从终止状态开始做 BFS 并按照引理判定必胜状态和必败状态时，记录判定必胜状态和必败状态时 BFS 进行到的轮次数，就是所求的回合数．这是因为判定为必胜状态只需要一个后继状态是必败状态即可，它总是由后继状态中轮次数最小的必败状态转移而来；而判定为必败状态需要所有后继状态都是必胜状态，它总是由后继状态中轮次数最大的必胜状态转移而来．

这一方法同样可以推广到一般的 [有向图游戏](../impartial-game/#有向图游戏)．

### 例题

[Codeforces 794 E. Choosing Carrot](https://codeforces.com/problemset/problem/794/E)

设有一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数列 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．两名玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轮流从数列的两端取走一个数，直到数列中仅剩下最后一个数字为止．玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的目标是最大化这个最后剩下的数字，玩家 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的目标是最小化它．在游戏正式开始前，玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还可以先进行 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次行动．假设两名玩家在整个过程中都采取最优策略．对于每一个 𝑘 =0,1,2,⋯,𝑛 −1k=0,1,2,⋯,n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求出游戏结束时最后剩下的数字．其中，1 ≤𝑛 ≤3 ×1051≤n≤3×105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解答

因为无论双方怎样取走数字，数列剩余部分都是一段完整的区间．所以，游戏中的局面可以仅由区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和当前行动的玩家 𝑖 =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 描述，可以使用动态规划算法求解．设 𝑓(𝑙,𝑟,𝑖)f(l,r,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为局面由 (𝑙,𝑟,𝑖)(l,r,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 描述时，游戏最后剩下的数字．由前文分析可知，当 𝑙 <𝑟l<r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，这一函数满足状态转移方程：

𝑓(𝑙,𝑟,1)=max{𝑓(𝑙+1,𝑟,2),𝑓(𝑙,𝑟−1,2)},𝑓(𝑙,𝑟,2)=min{𝑓(𝑙+1,𝑟,1),𝑓(𝑙,𝑟−1,1)}.f(l,r,1)=max{f(l+1,r,2),f(l,r−1,2)},f(l,r,2)=min{f(l+1,r,1),f(l,r−1,1)}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

终值条件为 𝑓(𝑙,𝑙,1) =𝑓(𝑙,𝑙,2) =𝑎𝑙f(l,l,1)=f(l,l,2)=al![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．据此，可以在 Θ(𝑛2)Θ(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内求出所有可能局面的函数值．对于每个 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，答案就是

𝑔(𝑘)=max𝑓(𝑙,𝑟,1) subject to 𝑟−𝑙+1=𝑘.g(k)=maxf(l,r,1) subject to r−l+1=k.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这一算法无法通过原题所设的数据范围，因此需要考虑优化转移．此处有很多种处理方法，本文只提供其中一种．

将状态转移方程看作是对数列整体的操作．两个转移方程分别表示将相邻数字取最大值和最小值得到新数列，将它们分别称为「最大化操作」和「最小化操作」．每次操作都会使得数列长度减一．所有长度为 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的区间对应结果共计 (𝑛 −𝑑 +1)(n−d+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，这就相当于对序列进行 (𝑑 −1)(d−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次操作得到的序列．另外，要得到 𝑓(𝑙,𝑟,1)f(l,r,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的结果，就需要保证最后一次操作是最大化操作．因此，这些操作序列的结尾总是最大化操作．

考虑连续两次操作给数列带来的变化．不妨考虑首先做最小化操作，再做最大化操作．此时，数列 𝑎1,𝑎2,𝑎3a1,a2,a3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将变为

max{min{𝑎1,𝑎2},min{𝑎2,𝑎3}}.max{min{a1,a2},min{a2,a3}}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

枚举 𝑎1,𝑎2,𝑎3a1,a2,a3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 三个数字之间所有可能的大小关系可知，除了 𝑎1 <𝑎2a1<a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎2 >𝑎3a2>a3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是严格极大值）这种情形外，这一表达式总是等于 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．也就是说，如果一个数列不存在任何严格极大值点，那么，连续两次操作对它的唯一影响就是删去了数列首尾各一个数字．这显然大幅简化了转移．剩下唯一的问题就是：如何保证数列不存在任何严格极大值点？事实上，只要对序列做一次最大化操作，就能保证不存在严格极大值点．故而，所有偶数次操作的结果，可以通过对初始数列进行两次操作得到的序列，逐对删去首尾数字得到；所有奇数次操作的结果，可以通过对初始数列进行一次操作得到的序列，逐对删去首尾数字得到．

由于对序列的完整操作至多只需要进行 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，而后续统计答案只需要 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次遍历，所以该算法的总时间复杂度为 Θ(𝑛)Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``` |  ```text #include <algorithm> #include <iostream> #include <vector> int main () { int n ; std :: cin >> n ; std :: vector < int > a ( n ); for ( int & x : a ) std :: cin >> x ; std :: vector < int > ans ( n ), tmp ; tmp = a ; for ( int i = 0 ; i < n \- 1 ; ++ i ) { tmp [ i ] = std :: max ( tmp [ i ], tmp [ i \+ 1 ]); } for ( int l = n / 2 \- 1 , r = ( n \- 1 ) / 2 , ma = 0 ; l >= 0 ; \-- l , ++ r ) { ma = std :: max ({ ma , tmp [ l ], tmp [ r ]}); ans [ r \- l ] = ma ; } tmp = a ; for ( int i = 0 ; i < n \- 1 ; ++ i ) { tmp [ i ] = std :: min ( tmp [ i ], tmp [ i \+ 1 ]); } for ( int i = 0 ; i < n \- 2 ; ++ i ) { tmp [ i ] = std :: max ( tmp [ i ], tmp [ i \+ 1 ]); } for ( int l = ( n \- 3 ) / 2 , r = n / 2 \- 1 , ma = 0 ; l >= 0 ; \-- l , ++ r ) { ma = std :: max ({ ma , tmp [ l ], tmp [ r ]}); ans [ r \- l ] = ma ; } ans [ n \- 1 ] = * std :: max_element ( a . begin (), a . end ()); for ( auto x : ans ) std :: cout << x << ' ' ; std :: cout << std :: endl ; return 0 ; } ```   
---|---  
  
### 习题

  * [Luogu P2734 [USACO3.3] 游戏 A Game](https://www.luogu.com.cn/problem/P2734)
  * [Luogu P4576 [CQOI2013] 棋盘游戏](https://www.luogu.com.cn/problem/P4576)
  * [Luogu P7097 [yLOI2020] 牵丝戏](https://www.luogu.com.cn/problem/P7097)
  * [Codeforces 388 C. Fox and Card Game](https://codeforces.com/problemset/problem/388/C)
  * [Codeforces 794 E. Choosing Carrot](https://codeforces.com/problemset/problem/794/E)
  * [Codeforces 1628 D2. Game on Sum (Hard Version)](https://codeforces.com/problemset/problem/1628/D2)
  * [Luogu P3210 [HNOI2010] 取石头游戏](https://www.luogu.com.cn/problem/P3210)

## 同时零和游戏

同时零和博弈中，两名玩家同时行动．

同时零和游戏通常采用收益矩阵表示．假设玩家 𝑖 =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的行动集合为 𝐴𝑖Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且当玩家 𝑖 =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别采取行动 𝑎𝑖 ∈𝐴𝑖ai∈Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，两人的收益分别是 𝑣(𝑎1,𝑎2)v(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 −𝑣(𝑎1,𝑎2)−v(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

例子

考虑石头剪刀布游戏．假定胜利得 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分，失败得 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分，平局得 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分．那么，游戏中两人的收益可以表示为

⎛⎜ ⎜ ⎜⎝0,01,−1−1,1−1,10,01,−11,−1−1,10,0⎞⎟ ⎟ ⎟⎠.(0,01,−1−1,1−1,10,01,−11,−1−1,10,0).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

一般的二人同时游戏也可以表示为类似形式，故而也称为 [双矩阵游戏](https://en.wikipedia.org/wiki/Bimatrix_game)（bimatrix game）．对于零和博弈，由于玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的收益矩阵和玩家 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的收益矩阵互为相反数，所以可以只考虑玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的收益矩阵：

𝑉=(𝑣(𝑎1,𝑎2))(𝑎1,𝑎2)∈𝐴1×𝐴2=⎛⎜ ⎜ ⎜⎝01−1−1011−10⎞⎟ ⎟ ⎟⎠.V=(v(a1,a2))(a1,a2)∈A1×A2=(01−1−1011−10).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

需要解决的问题是：给定收益矩阵 𝑉 =(𝑣(𝑎1,𝑎2))(𝑎1,𝑎2)∈𝐴1×𝐴2V=(v(a1,a2))(a1,a2)∈A1×A2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如何求出两名玩家的最优策略和最大收益？

### 混合策略

相较于序贯零和游戏，同时游戏中两名玩家的角色是对称的．但是，既然已经解决了序贯零和游戏，那么不妨考虑同时游戏的序贯版本．例如，如果假定玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 首先做出行动，玩家 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 再做出行动，那么，根据前文讨论，游戏结束时玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的收益将由

𝑤−=max𝑎1∈𝐴1min𝑎2∈𝐴2𝑣(𝑎1,𝑎2)w−=maxa1∈A1mina2∈A2v(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

给出．由于玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的行动对于玩家 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单向透明，这应该是玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所能获得的最差结果．对称地，如果假定玩家 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 首先行动，那么，玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的收益将由

𝑤+=min𝑎2∈𝐴2max𝑎1∈𝐴1𝑣(𝑎1,𝑎2)w+=mina2∈A2maxa1∈A1v(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

给出．由于玩家 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的行动对于玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单向透明，这应该是玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所能获得的最好结果．玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 应该期待实际进行游戏时，所能获得的收益 𝑤 ∈[𝑤−,𝑤+]w∈[w−,w+]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．尽管不等式 𝑤− ≤𝑤+w−≤w+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是成立（证明参见 [弱对偶定理](../../linear-programming/#对偶原理)），但是由于等号未必成立，所以，仅采用序贯游戏的分析手段，一般情况下没有办法唯一确定游戏结果．

例子（续）

石头剪刀布游戏中，如果出手有先后，那么先手必输，后手必赢．转换为数学语言，这就是下列不等式：

𝑤−=−1≤+1=𝑤+.w−=−1≤+1=w+.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

此时，𝑤− ≠𝑤+w−≠w+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并不成立．

上述分析过程遗漏了同时游戏的一个关键因素，就是玩家无法准确预测对手的行动．形式上，这意味着双方可以采取某种随机策略．这一想法在序贯博弈的语境下并不成立，因为无论先手玩家如何随机选择行动，后手玩家总能准确地观测到这一行动，并有针对性地回应．但是，对于同时游戏，随机策略引入的战略模糊将使得对手无法有效地针对己方的行动．

例子（续）

石头剪刀布游戏中，如果玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均匀随机地选择剪刀、石头、布三个行动之一，那么，根据玩家 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的行动不同，玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能获得的收益是

13(0,1,−1)𝑇+13(−1,0,1)𝑇+13(1,−1,0)𝑇=(0,0,0)𝑇.13(0,1,−1)T+13(−1,0,1)T+13(1,−1,0)T=(0,0,0)T.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

此时，无论玩家 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 如何选择行动，玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的期望收益总是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这显然好于确定性地选择单个行动．

由此，就引入了混合策略的概念．

混合策略

同时游戏中，玩家 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **混合策略** （mixed strategy），简称 **策略** ，是指函数 𝑠𝑖 :𝐴𝑖 →[0,1]si:Ai→[0,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且它满足 ∑𝑎𝑖∈𝐴𝑖𝑠𝑖(𝑎𝑖) =1∑ai∈Aisi(ai)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．也就是说，策略 𝑠𝑖si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是玩家 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的行动集合 𝐴𝑖Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的一个概率分布．玩家 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 全体混合策略的集合记作 𝑆𝑖 =Δ(𝐴𝑖)Si=Δ(Ai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，Δ(𝐴𝑖)Δ(Ai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝐴𝑖Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的全体概率分布的集合．如果 𝑠𝑖si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是退化的概率分布，即存在 𝑎 ∈𝐴𝑖a∈Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑠𝑖(𝑎) =1si(a)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，也称策略 𝑠𝑖si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **纯策略** （pure strategy）．

混合策略的收益就是单个行动收益的期望：

𝑣(𝑠1,𝑠2)=∑𝑎1∈𝐴1∑𝑎2∈𝐴2𝑠1(𝑎1)𝑠2(𝑎2)𝑣(𝑎1,𝑎2).v(s1,s2)=∑a1∈A1∑a2∈A2s1(a1)s2(a2)v(a1,a2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将单个行动看作对应的纯策略，那么，就可以将行动集合 𝐴𝑖Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 嵌入（混合）策略集合 𝑆𝑖Si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，且上式定义的 𝑣(𝑠1,𝑠2)v(s1,s2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就可以看作是将 𝑣(𝑎1,𝑎2)v(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 从 𝐴1 ×𝐴2A1×A2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 延拓到 𝑆1 ×𝑆2S1×S2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上．

### von Neumann 定理

引入混合策略后，极大化极小思想和极小化极大思想得到的结果是一致的，由此，同时零和游戏的结果也是唯一确定的．

定理（von Neumann）

允许混合策略的同时零和游戏中，如果双方都采取最优策略，那么，玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大收益为

𝑤=max𝑠1∈𝑆1min𝑠2∈𝑆2𝑣(𝑠1,𝑠2)=min𝑠2∈𝑆2max𝑠1∈𝑆1𝑣(𝑠1,𝑠2),w=maxs1∈S1mins2∈S2v(s1,s2)=mins2∈S2maxs1∈S1v(s1,s2),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

玩家 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大收益为 −𝑤−w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

设 𝑤 =max𝑠1∈𝑆1min𝑠2∈𝑆2𝑣(𝑠1,𝑠2)w=maxs1∈S1mins2∈S2v(s1,s2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．考虑内层最小化问题，因为 𝑣(𝑠1,𝑠2) =∑𝑎2∈𝐴2𝑠2(𝑎2)𝑣(𝑠1,𝑎2)v(s1,s2)=∑a2∈A2s2(a2)v(s1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，max𝑠2∈𝑆2𝑣(𝑠1,𝑠2) =max𝑎2∈𝐴2𝑣(𝑠1,𝑎2)maxs2∈S2v(s1,s2)=maxa2∈A2v(s1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，前者的最优解就是后者的最优解对应的纯策略．因此，有 𝑤 =max𝑠1∈𝑆1min𝑎2∈𝐴2𝑣(𝑠1,𝑎2)w=maxs1∈S1mina2∈A2v(s1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．进而，引入辅助变量 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，问题就可以改写为

𝑤=max𝑠1∈𝑆1𝑢 subject to 𝑢≤min𝑎2∈𝐴2𝑣(𝑠1,𝑎2).w=maxs1∈S1u subject to u≤mina2∈A2v(s1,a2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为这个约束就等价于 𝑢 ≤𝑣(𝑠1,𝑎2)u≤v(s1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有 𝑎2 ∈𝐴2a2∈A2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．最后，引入混合策略 𝑠1s1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义和收益函数 𝑣(𝑠1,𝑎2)v(s1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表达式，原问题就等价于 [线性规划问题](../../linear-programming/)

(𝑃)𝑤=max𝑢,𝑠1𝑢subject to ∑𝑎1∈𝐴1𝑠1(𝑎1)𝑣(𝑎1,𝑎2)≥𝑢, ∀𝑎2∈𝐴2,∑𝑎1∈𝐴1𝑠1(𝑎1)=1,𝑠1(𝑎1)≥0, ∀𝑎1∈𝐴1.(P)w=maxu,s1usubject to ∑a1∈A1s1(a1)v(a1,a2)≥u, ∀a2∈A2,∑a1∈A1s1(a1)=1,s1(a1)≥0, ∀a1∈A1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这个问题显然是可行的，且最优解有解．根据 [对偶原理](../../linear-programming/#对偶原理) 可知，它的最优解就等于对偶问题的最优解：

(𝐷)𝑤=min𝑡,𝑠2𝑡subject to ∑𝑎2∈𝐴2𝑠2(𝑎2)𝑣(𝑎1,𝑎2)≤𝑡, ∀𝑎1∈𝐴1,∑𝑎2∈𝐴2𝑠2(𝑎2)=1,𝑠2(𝑎2)≥0, ∀𝑎2∈𝐴2.(D)w=mint,s2tsubject to ∑a2∈A2s2(a2)v(a1,a2)≤t, ∀a1∈A1,∑a2∈A2s2(a2)=1,s2(a2)≥0, ∀a2∈A2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

重复前文的步骤，这一问题就等价于 min𝑠2∈𝐴2min𝑠1∈𝑆1𝑣(𝑠1,𝑠2)mins2∈A2mins1∈S1v(s1,s2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．定理得证．

这一结果正是这一游戏的 [Nash 均衡](https://en.wikipedia.org/wiki/Nash_equilibrium)．也就是说，假定双方都选择均衡中的最优策略，那么，没有任何玩家能够从偏离均衡策略中严格获益．

### 转化为线性规划问题

von Neumann 定理的证明同时也指出了同时零和游戏的求解方法．设 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别是玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可采取的行动数目．给定玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的收益矩阵 𝑉 ∈𝐑𝑛×𝑚V∈Rn×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以求解如下线性规划问题：

𝑤=max(𝑢,𝑠)∈𝐑×𝐑𝑛𝑢subject to 𝑉𝑇𝑠≥𝑢𝟏,𝟏𝑇𝑠=1,𝑠≥0.w=max(u,s)∈R×Rnusubject to VTs≥u1,1Ts=1,s≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是一个规模为 Θ(𝑛 +𝑚)Θ(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性规划问题，可以用 [单纯形法](../../simplex/) 高效求解．算法得到的最优解 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是玩家 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最优（混合）策略．要求得玩家 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最优策略，只需要从单纯形表中获得该问题最优解的对偶变量（即影子价格）即可．

### 习题

  * [Luogu P4232 无意识之外的捉迷藏](https://www.luogu.com.cn/problem/P4232)

## 参考资料与注释

  * [Zero-sum game - Wikipedia](https://en.wikipedia.org/wiki/Zero-sum_game)
  * [Minimax theorem - Wikipedia](https://en.wikipedia.org/wiki/Minimax_theorem)

* * *

>  __本页面最近更新： 2025/10/17 09:50:13，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/game-theory/zero-sum-game.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/game-theory/zero-sum-game.md "edit.link.title")  
>  __本页面贡献者：[c-forrest](https://github.com/c-forrest)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
