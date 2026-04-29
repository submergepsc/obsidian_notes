# IDA* - OI Wiki

- Source: https://oi-wiki.org/search/idastar/

# IDA*

前置知识：[A* 算法](../astar/)、[迭代加深搜索](../iterative/)

本页面将简要介绍 IDA* 算法．IDA* 就是采用了迭代加深算法的 A* 算法．

## 过程

IDA* 算法是迭代加深搜索的一种变形．迭代加深搜索在每次 DFS 中限制搜索深度，而 IDA* 则限制单次 DFS 的路径成本．

在一次迭代中，算法从起点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始进行 DFS，记录到达当前结点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的实际成本 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并利用它到终点的最小成本估计 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行剪枝．如果沿着当前路径到达终点的总成本估计

𝑓(𝑥)=𝑔(𝑥)+ℎ(𝑥)f(x)=g(x)+h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

超过阈值 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则停止对该分支的搜索．

阈值 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在迭代间动态更新．初始阈值取为起点的总成本估计值 ℎ(𝑠)h(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．在一次迭代中，每当因超过阈值而停止时，就记录所有尚未访问的后继结点的总成本估计的最小值．迭代结束后，将阈值更新为这一最小值，继续下一轮搜索．

## 性质

由于使用了和 A* 算法一样的剪枝策略，所以对 A* 算法性质的讨论对 IDA* 算法也适用．

和 A* 算法相比，IDA* 算法有如下优点：

  * 不需要判重，不需要排序，利于深度剪枝．
  * 空间需求减少．每次迭代都是一个深度优先搜索，但是对搜索中的路径成本有限制，使用 DFS 可以减小空间消耗．

同时，它也有缺点：

  * 重复搜索．即使前后两次搜索相差微小，每次放宽限制都要再次从头搜索．

## 实现

设 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个合适的估价函数，𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为搜索起点．完整的算法流程大致如下所示：

𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦. IdaStar():𝐎𝐮𝐭𝐩𝐮𝐭. The shortest path, 𝑝𝑎𝑡ℎ, and its cost, 𝐶, if a path exists,and NOT_FOUND, otherwise.𝐌𝐞𝐭𝐡𝐨𝐝.1𝐶←ℎ(𝑠)2𝑝𝑎𝑡ℎ←[𝑠]3𝐰𝐡𝐢𝐥𝐞 true4𝑡←Search(𝑝𝑎𝑡ℎ,0,𝐶)5𝐢𝐟 𝑡=FOUND 𝐭𝐡𝐞𝐧 𝐫𝐞𝐭𝐮𝐫𝐧 (𝑝𝑎𝑡ℎ,𝐶)6𝐢𝐟 𝑡=∞ 𝐭𝐡𝐞𝐧 𝐫𝐞𝐭𝐮𝐫𝐧 NOT_FOUND7𝐶←𝑡𝐒𝐮𝐛-𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦. Search(𝑝𝑎𝑡ℎ,𝑔,𝐶):𝐈𝐧𝐩𝐮𝐭. The current path, 𝑝𝑎𝑡ℎ, its cost, 𝑔, and search limit 𝐶.𝐎𝐮𝐭𝐩𝐮𝐭. FOUND, if the target node has been reached; ∞, if allreachable nodes have been explored; otherwise, the minimumtotal cost, 𝑡, among nodes not yet explored.𝐌𝐞𝐭𝐡𝐨𝐝.1𝑛𝑜𝑑𝑒←the last element in 𝑝𝑎𝑡ℎ2𝑓←𝑔+ℎ(𝑛𝑜𝑑𝑒)3𝐢𝐟 𝑓>𝐶 𝐭𝐡𝐞𝐧 𝐫𝐞𝐭𝐮𝐫𝐧 𝑓4𝐢𝐟 𝑛𝑜𝑑𝑒 is the target 𝐭𝐡𝐞𝐧 𝐫𝐞𝐭𝐮𝐫𝐧 FOUND5𝑚𝑖𝑛←∞6𝐟𝐨𝐫 each 𝑐ℎ𝑖𝑙𝑑 of 𝑛𝑜𝑑𝑒 𝐝𝐨7𝐢𝐟 𝑐ℎ𝑖𝑙𝑑 not in 𝑝𝑎𝑡ℎ 𝐭𝐡𝐞𝐧8append 𝑐ℎ𝑖𝑙𝑑 to 𝑝𝑎𝑡ℎ9𝑡←Search(𝑝𝑎𝑡ℎ,𝑔+Cost(𝑛𝑜𝑑𝑒,𝑐ℎ𝑖𝑙𝑑),𝐶)10𝐢𝐟 𝑡=FOUND 𝐭𝐡𝐞𝐧 𝐫𝐞𝐭𝐮𝐫𝐧 FOUND11𝐢𝐟 𝑡<𝑚𝑖𝑛 𝐭𝐡𝐞𝐧 𝑚𝑖𝑛←𝑡12remove the last element of 𝑝𝑎𝑡ℎ13𝐫𝐞𝐭𝐮𝐫𝐧 𝑚𝑖𝑛Algorithm. IdaStar():Output. The shortest path, path, and its cost, C, if a path exists,and NOT_FOUND, otherwise.Method.1C←h(s)2path←[s]3while true4t←Search(path,0,C)5if t=FOUND then return (path,C)6if t=∞ then return NOT_FOUND7C←tSub-Algorithm. Search(path,g,C):Input. The current path, path, its cost, g, and search limit C.Output. FOUND, if the target node has been reached; ∞, if allreachable nodes have been explored; otherwise, the minimumtotal cost, t, among nodes not yet explored.Method.1node←the last element in path2f←g+h(node)3if f>C then return f4if node is the target then return FOUND5min←∞6for each child of node do7if child not in path then8append child to path9t←Search(path,g+Cost(node,child),C)10if t=FOUND then return FOUND11if t<min then min←t12remove the last element of path13return min![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 例题

[埃及分数](https://www.luogu.com.cn/problem/P1763)

在古埃及，人们使用互不相同的单位分数（即 1/𝑎1/a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑎 ∈𝐍+a∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）的和表示一切有理数．例如，23 =12 +1623=12+16![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但不允许 23 =13 +1323=13+13![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为在加数中不允许有相同的单位分数．

对于一个分数 𝑎𝑏ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示方法有很多种．规定：同一个分数的不同表示方法中，加数少的比加数多的好；如果加数个数相同，则最小的分数越大越好．例如，1945 =15 +16 +1181945=15+16+118![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是最佳方案．

输入整数 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（0 <𝑎 <𝑏 <10000<a<b<1000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），试编程计算最佳表达式．

解题思路

这道题目理论上可以用回溯法求解，但是解答树会非常「恐怖」——不仅深度没有明显的上界，而且加数的选择理论上也是无限的．换句话说，如果用宽度优先遍历，连一层都扩展不完，因为每一层都是无限大的．

解决方案是采用迭代加深搜索：从小到大枚举深度上限 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每次搜索只考虑深度不超过 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的结点．这样，只要解的深度有限，则一定可以在有限时间内枚举到．

深度上限 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还可以用来剪枝．按照分母递增的顺序来进行扩展，如果扩展到 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层时，前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个分数之和为 𝑐𝑑cd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个分数为 1𝑒1e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则接下来至少还需要

ℎ=(𝑎𝑏−𝑐𝑑)/(1𝑒+1)h=(ab−cd)/(1e+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

个分数，总和才能达到 𝑎𝑏ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．例如，当前搜索到 1945 =15 +1100 +⋯1945=15+1100+⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则后面的分数每个最大为 11011101![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，至少需要 (1945−15)/(1101) =23(1945−15)/(1101)=23![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项总和才能达到 19451945![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此前 2222![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次迭代是根本不会考虑这棵子树的．这里的关键在于：可以估计至少还要多少步才能出解．

注意，这里使用「至少」一词表示估计是「乐观的」．和 A* 算法一样，好的估计函数都需要是「乐观的」，也就是说，它不能高估实际成本．将迭代加深搜索中的深度限制 𝑔 ≤𝐶g≤C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 替换为更严格的限制 𝑔 +ℎ ≤𝐶g+h≤C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就得到了本页面所讨论的 IDA* 算法．因为本文中的路径成本就是它的长度，所以，IDA* 算法同样是对路径长度进行限制，只是加上了对于还需要多少步的估计．更一般的问题中，根据具体要最小化的成本不同，还可以设计出其他的估计函数．

在实现中，对 IDA* 算法进一步剪枝优化：

  1. 扩展结点时，下一个要考虑的分母至少是 (𝑎𝑏−𝑐𝑑)−1(ab−cd)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以以此改进枚举 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的起点．
  2. IDA* 的路径成本限制可以变形为

𝑒≤(𝑎𝑏−𝑐𝑑)−1(𝐶−𝑔)−1.e≤(ab−cd)−1(C−g)−1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，不必枚举所有的后续分母再逐个判断，只需要枚举到这个上界即可．

  3. 在搜索到最后两个分数时，直接利用二次方程计算是否可行，而非继续搜索．具体地，要找到 𝑒 <𝑥 <𝑦 ≤𝐸maxe<x<y≤Emax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

1𝑥+1𝑦=𝑝𝑞:=𝑎𝑏−𝑐𝑑,1x+1y=pq:=ab−cd,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

只需要求解二元二次方程组

{𝑥+𝑦=𝑘𝑝,𝑥𝑦=𝑘𝑞{x+y=kp,xy=kq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即可，其中，𝑘 ∈𝐍+k∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由二次方程的知识可知，方程组在

Δ=𝑘2𝑝2−4𝑘𝑞>0⟺𝑘>4𝑞𝑝2Δ=k2p2−4kq>0⟺k>4qp2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

时，才有两个不同的实根

𝑥=𝑘𝑝−√Δ2, 𝑦=𝑘𝑝+√Δ2.x=kp−Δ2, y=kp+Δ2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，可以直接枚举所有可行的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，判断是否存在这样一组整数解．枚举 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，上界通过 𝑦 <𝐸maxy<Emax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 判断．

  4. 每次得到一组答案时，都将分母的上界 𝑀𝑒Me![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 调整到当前答案中的最大分母减一．

另外，实现中，直接记录了 𝑎𝑏 −𝑐𝑑ab−cd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐶 −𝑔C−g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值，前者的分子和分母分别存储在变量 `a` 和 `b` 中，后者则存储为变量 `d`．

示例代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 ``` |  ```text #include <cmath> #include <iostream> #include <numeric> #include <vector> int max_e = 1e7 ; std :: vector < int > ans ; std :: vector < int > current ; long long gcd ( long long x , long long y ) { return y ? gcd ( y , x % y ) : x ; } bool dfs ( int d , long long a , long long b , int e ) { long long _gcd = gcd ( a , b ); a /= _gcd ; b /= _gcd ; bool solved = false ; if ( d == 2 ) { for ( int k = 4 * b / ( a * a ) \+ 1 ;; ++ k ) { long long delta = a * a * k * k \- 4 * b * k ; long long t = std :: sqrt ( delta \+ 0.5l ); long long x = ( a * k \- t ) / 2 ; long long y = ( a * k \+ t ) / 2 ; if ( y > max_e ) break ; if ( ! t || t * t != delta || ( a * k \- t ) % 2 != 0 ) continue ; ans = current ; ans . push_back ( x ); ans . push_back ( y ); max_e = y \- 1 ; solved = true ; } } else { int e1 = std :: max ( e \+ 1 , int (( b \+ a \- 1 ) / a )); for (; e1 <= d * b / a && e1 <= max_e ; e1 ++ ) { current . push_back ( e1 ); // a/b - 1/e solved |= dfs ( d \- 1 , a * e1 \- b , b * e1 , e1 ); current . pop_back (); } } return solved ; } int solve ( int a , int b ) { if ( b % a == 0 ) { ans . push_back ( b / a ); return 1 ; } for ( int lim = 2 ; lim <= 100 ; lim ++ ) if ( dfs ( lim , a , b , 1 )) return lim ; return -1 ; } int main () { int a , b ; std :: cin >> a >> b ; solve ( a , b ); for ( auto x : ans ) std :: cout << x << ' ' ; std :: cout << std :: endl ; return 0 ; } ```   
---|---  
  
## 习题

  * [UVa1343 旋转游戏](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=4089)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/search/idastar.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/search/idastar.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [ksyx](https://github.com/ksyx), [Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [hsfzLZH1](https://github.com/hsfzLZH1), [CCXXXI](https://github.com/CCXXXI), [Chrogeek](https://github.com/Chrogeek), [ChungZH](https://github.com/ChungZH), [Enter-tainer](https://github.com/Enter-tainer), [frank-xjh](https://github.com/frank-xjh), [greyqz](https://github.com/greyqz), [GreyTigerOIer](https://github.com/GreyTigerOIer), [Henry-ZHR](https://github.com/Henry-ZHR), [HHH2309](https://github.com/HHH2309), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [Kuludu](https://github.com/Kuludu), [lct8712](https://github.com/lct8712), [NachtgeistW](https://github.com/NachtgeistW), [ouuan](https://github.com/ouuan), [Phemon](mailto:i@phemon.me), [yusancky](https://github.com/yusancky), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
