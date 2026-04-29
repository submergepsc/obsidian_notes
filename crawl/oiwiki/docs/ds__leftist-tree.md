# 左偏树 - OI Wiki

- Source: https://oi-wiki.org/ds/leftist-tree/

# 左偏树

## 什么是左偏树？

**左偏树** 与 [**配对堆**](../pairing-heap/) 一样，是一种 **可并堆** ，具有堆的性质，并且可以快速合并．

## 左偏树的定义和性质

对于一棵二叉树，我们定义 **外节点** 为子节点数小于两个的节点，定义一个节点的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为其到子树中最近的外节点所经过的边的数量．空节点的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注意

有些资料中对 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义是本文中的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 减 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样定义是因为代码编写时可以省略一些判空流程，但需要注意应预先置空节点的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．本文中所有代码对 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义 **均为空节点 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义**，请注意与行文间 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 定义的差别．

左偏树是一棵二叉树，它不仅具有堆的性质，并且是「左偏」的：每个节点左儿子的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都大于等于右儿子的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因此，左偏树每个节点的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都等于其右儿子的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加一．

需要注意的是，distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是深度，**左偏树的深度没有保证** ，一条向左的链也符合左偏树的定义．

## 核心操作：合并（merge）

合并两个堆时，由于要满足堆性质，先取值较小（为了方便，本文讨论小根堆）的那个根作为合并后堆的根节点，然后将这个根的左儿子作为合并后堆的左儿子，递归地合并其右儿子与另一个堆，作为合并后的堆的右儿子．为了满足左偏性质，合并后若左儿子的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小于右儿子的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就交换两个儿子．

参考代码：

实现

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text int merge ( int x , int y ) { if ( ! x || ! y ) return x | y ; // 若一个堆为空则返回另一个堆 if ( t [ x ]. val > t [ y ]. val ) swap ( x , y ); // 取值较小的作为根 t [ x ]. rs = merge ( t [ x ]. rs , y ); // 递归合并右儿子与另一个堆 if ( t [ t [ x ]. rs ]. d > t [ t [ x ]. ls ]. d ) swap ( t [ x ]. ls , t [ x ]. rs ); // 若不满足左偏性质则交换左右儿子 t [ x ]. d = t [ t [ x ]. rs ]. d \+ 1 ; // 更新dist return x ; } ```   
---|---  
  
由于左偏性质，每递归一层，其中一个堆根节点的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就会减小 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而一棵有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点的二叉树，根的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不超过 ⌈log⁡(𝑛+1)⌉⌈log⁡(n+1)⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以合并两个大小分别为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的堆复杂度是 𝑂(log⁡𝑛 +log⁡𝑚)O(log⁡n+log⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

关于 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 性质的证明

一棵根的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二叉树至少有 𝑥 −1x−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层是满二叉树，那么就至少有 2𝑥 −12x−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点．注意这个性质是所有二叉树都具有的，并不是左偏树所特有的．

左偏树还有一种无需交换左右儿子的写法：将 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 较大的儿子视作左儿子，distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 较小的儿子视作右儿子：

实现

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text int & rs ( int x ) { return t [ x ]. ch [ t [ t [ x ]. ch [ 1 ]]. d < t [ t [ x ]. ch [ 0 ]]. d ]; } int merge ( int x , int y ) { if ( ! x || ! y ) return x | y ; if ( t [ x ]. val < t [ y ]. val ) swap ( x , y ); int & rs_ref = rs ( x ); rs_ref = merge ( rs_ref , y ); t [ x ]. d = t [ rs ( x )]. d \+ 1 ; return x ; } ```   
---|---  
  
## 左偏树的其它操作

### 插入节点

单个节点也可以视为一个堆，合并即可．

### 删除根

合并根的左右儿子即可．

### 删除任意节点

#### 做法

先将左右儿子合并，然后自底向上更新 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、不满足左偏性质时交换左右儿子，当 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 无需更新时结束递归：

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``` |  ```text int & rs ( int x ) { return t [ x ]. ch [ t [ t [ x ]. ch [ 1 ]]. d < t [ t [ x ]. ch [ 0 ]]. d ]; } // 有了 pushup，直接 merge 左右儿子就实现了删除节点并保持左偏性质 int merge ( int x , int y ) { if ( ! x || ! y ) return x | y ; if ( t [ x ]. val < t [ y ]. val ) swap ( x , y ); int & rs_ref = rs ( x ); rs_ref = merge ( rs_ref , y ); t [ rs_ref ]. fa = x ; t [ x ]. d = t [ rs ( x )]. d \+ 1 ; return x ; } void pushup ( int x ) { if ( ! x ) return ; if ( t [ x ]. d != t [ rs ( x )]. d \+ 1 ) { t [ x ]. d = t [ rs ( x )]. d \+ 1 ; pushup ( t [ x ]. fa ); } } void erase ( int x ) { int y = merge ( t [ x ]. ch [ 0 ], t [ x ]. ch [ 1 ]); t [ y ]. fa = t [ x ]. fa ; if ( t [ t [ x ]. fa ]. ch [ 0 ] == x ) t [ t [ x ]. fa ]. ch [ 0 ] = y ; else if ( t [ t [ x ]. fa ]. ch [ 1 ] == x ) t [ t [ x ]. fa ]. ch [ 1 ] = y ; pushup ( t [ y ]. fa ); } ```   
---|---  
  
#### 复杂度证明

先考虑 `merge` 的过程，每次都会使 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向下一层，也就是说最极端的情况，就是一直选择左偏树的右节点（distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小的节点）向下一层，此时 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 减少了 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

再考虑 `pushup` 的过程，我们令当前 `pushup` 的这个节点为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其父亲为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，一个节点的「初始 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」为它在 `pushup` 前的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．从被删除节点的父亲开始递归，有两种情况：

  1. 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的右儿子，此时 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的初始 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的初始 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加一．
  2. 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左儿子，由于节点的 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最多减一，因此只有 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左右儿子初始 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相等时（此时左儿子 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 减一会导致左右儿子互换）才会继续递归下去，因此 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的初始 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仍然是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的初始 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加一．

所以，我们得到，每递归一层 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的初始 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就会加一，因此最多递归 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层．

### 整个堆加上/减去一个值、乘上一个正数

其实可以打标记且不改变相对大小的操作都可以．

在根打上标记，删除根/合并堆（访问儿子）时下传标记即可：

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text int merge ( int x , int y ) { if ( ! x || ! y ) return x | y ; if ( t [ x ]. val > t [ y ]. val ) swap ( x , y ); pushdown ( x ); t [ x ]. rs = merge ( t [ x ]. rs , y ); if ( t [ t [ x ]. rs ]. d > t [ t [ x ]. ls ]. d ) swap ( t [ x ]. ls , t [ x ]. rs ); t [ x ]. d = t [ t [ x ]. rs ]. d \+ 1 ; return x ; } int pop ( int x ) { pushdown ( x ); return merge ( t [ x ]. ls , t [ x ]. rs ); } ```   
---|---  
  
## 其他可并堆

### 随机堆

实现

```text 1 2 3 4 5 6 7 8 ``` |  ```text int merge ( int x , int y ) { if ( ! x || ! y ) return x | y ; if ( t [ y ]. val < t [ x ]. val ) swap ( x , y ); if ( rand () & 1 ) // 随机选择是否交换左右子节点 swap ( t [ x ]. ls , t [ x ]. rs ); t [ x ]. ls = merge ( t [ x ]. ls , y ); return x ; } ```   
---|---  
  
可以看到该实现方法唯一不同之处便是采用了随机数来实现合并，这样一来便可以省去 distdist![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的相关计算．且平均时间复杂度亦为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，详细证明可参考 [Randomized Heap](https://cp-algorithms.com/data_structures/randomized_heap.html)．

### 斜堆

斜堆是左偏树的自适应形式．当合并两个堆时，它无条件交换合并路径上的所有节点，以此试图维护平衡．根据均摊分析，自顶向下斜堆（top-down skew heap）插入，合并，删除最小值的复杂度为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)1．

## 例题

### 模板题

[luogu P3377【模板】左偏树（可并堆）](https://www.luogu.com.cn/problem/P3377)

[Monkey King](https://www.luogu.com.cn/problem/P1456)

[罗马游戏](https://www.luogu.com.cn/problem/P2713)

需要注意的是：

  1. 合并前要检查是否已经在同一堆中．

  2. 左偏树的深度可能达到 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此找一个点所在的堆顶要用并查集维护，不能直接暴力跳父亲．（虽然很多题数据水，暴力跳父亲可以过……）（用并查集维护根时要保证原根指向新根，新根指向自己．）

罗马游戏参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 ``` |  ```text #include <iostream> using namespace std ; constexpr int N = 1000010 ; struct Node { int val , ls , rs , d ; Node () { val = ls = rs = 0 ; d = -1 ; } Node ( int v ) { val = v ; ls = rs = d = 0 ; } } t [ N ]; int merge ( int x , int y ) { if ( ! x || ! y ) return x | y ; if ( t [ x ]. val > t [ y ]. val ) swap ( x , y ); t [ x ]. rs = merge ( t [ x ]. rs , y ); if ( t [ t [ x ]. rs ]. d > t [ t [ x ]. ls ]. d ) swap ( t [ x ]. ls , t [ x ]. rs ); t [ x ]. d = t [ t [ x ]. rs ]. d \+ 1 ; return x ; } int f [ N ]; // 查找 int find ( int x ) { return x == f [ x ] ? x : f [ x ] = find ( f [ x ]); } bool kill [ N ]; int main () { ios :: sync_with_stdio ( false ); cin . tie ( nullptr ); int n ; cin >> n ; for ( int i = 1 ; i <= n ; ++ i ) { int v ; cin >> v ; t [ i ] = Node ( v ); f [ i ] = i ; } int m ; cin >> m ; int x , y ; char op ; while ( m \-- ) { cin >> op ; if ( op == 'M' ) { cin >> x >> y ; if ( kill [ x ] || kill [ y ]) continue ; x = find ( x ); y = find ( y ); if ( x != y ) f [ x ] = f [ y ] = merge ( x , y ); } else { cin >> x ; if ( ! kill [ x ]) { x = find ( x ); kill [ x ] = true ; f [ x ] = f [ t [ x ]. ls ] = f [ t [ x ]. rs ] = merge ( t [ x ]. ls , t [ x ]. rs ); // 由于堆中的点会 find 到 x，所以 f[x] 也要修改 cout << t [ x ]. val << '\n' ; } else cout << "0 \n " ; } } return 0 ; } ```   
---|---  
  
### 树上问题

[「APIO2012」派遣](https://www.luogu.com.cn/problem/P1552)

[「JLOI2015」城池攻占](https://loj.ac/problem/2107)

这类题目往往是每个节点维护一个堆，与儿子合并，依题意弹出、修改、计算答案，有点像线段树合并的类似题目．

城池攻占参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 ``` |  ```text #include <iostream> using namespace std ; using ll = long long ; constexpr int N = 300010 ; struct Node { int ls , rs , d ; ll val , add , mul ; Node () { ls = rs = 0 ; d = -1 ; val = add = 0 ; mul = 1 ; } Node ( int v ) { ls = rs = d = 0 ; val = v ; add = 0 ; mul = 1 ; } } t [ N ]; int head [ N ], nxt [ N ], to [ N ], cnt ; int n , m , p [ N ], f [ N ], a [ N ], dep [ N ], c [ N ], ans1 [ N ], ans2 [ N ]; // p 是树上每个点对应的堆顶 ll h [ N ], b [ N ]; void add ( int u , int v ) { nxt [ ++ cnt ] = head [ u ]; head [ u ] = cnt ; to [ cnt ] = v ; } void madd ( int u , ll x ) { t [ u ]. val += x ; t [ u ]. add += x ; } void mmul ( int u , ll x ) { t [ u ]. val *= x ; t [ u ]. add *= x ; t [ u ]. mul *= x ; } void pushdown ( int x ) { // 类似线段树下传标记 mmul ( t [ x ]. ls , t [ x ]. mul ); madd ( t [ x ]. ls , t [ x ]. add ); mmul ( t [ x ]. rs , t [ x ]. mul ); madd ( t [ x ]. rs , t [ x ]. add ); t [ x ]. add = 0 ; t [ x ]. mul = 1 ; } int merge ( int x , int y ) { if ( ! x || ! y ) return x | y ; if ( t [ x ]. val > t [ y ]. val ) swap ( x , y ); pushdown ( x ); t [ x ]. rs = merge ( t [ x ]. rs , y ); if ( t [ t [ x ]. rs ]. d > t [ t [ x ]. ls ]. d ) swap ( t [ x ]. ls , t [ x ]. rs ); t [ x ]. d = t [ t [ x ]. rs ]. d \+ 1 ; return x ; } int pop ( int x ) { pushdown ( x ); return merge ( t [ x ]. ls , t [ x ]. rs ); } void dfs ( int u ) { for ( int i = head [ u ]; i ; i = nxt [ i ]) { int v = to [ i ]; dep [ v ] = dep [ u ] \+ 1 ; dfs ( v ); } while ( p [ u ] && t [ p [ u ]]. val < h [ u ]) { ++ ans1 [ u ]; ans2 [ p [ u ]] = dep [ c [ p [ u ]]] \- dep [ u ]; p [ u ] = pop ( p [ u ]); } if ( a [ u ]) mmul ( p [ u ], b [ u ]); else madd ( p [ u ], b [ u ]); if ( u > 1 ) p [ f [ u ]] = merge ( p [ u ], p [ f [ u ]]); else while ( p [ u ]) { ans2 [ p [ u ]] = dep [ c [ p [ u ]]] \+ 1 ; p [ u ] = pop ( p [ u ]); } } int main () { ios :: sync_with_stdio ( false ); cin . tie ( nullptr ); cin >> n >> m ; for ( int i = 1 ; i <= n ; ++ i ) cin >> h [ i ]; for ( int i = 2 ; i <= n ; ++ i ) { cin >> f [ i ] >> a [ i ] >> b [ i ]; add ( f [ i ], i ); } for ( int i = 1 ; i <= m ; ++ i ) { int v ; cin >> v >> c [ i ]; t [ i ] = Node ( v ); p [ c [ i ]] = merge ( i , p [ c [ i ]]); } dfs ( 1 ); for ( int i = 1 ; i <= n ; ++ i ) cout << ans1 [ i ] << '\n' ; for ( int i = 1 ; i <= m ; ++ i ) cout << ans2 [ i ] << '\n' ; return 0 ; } ```   
---|---  
  
### [「SCOI2011」棘手的操作](https://loj.ac/problem/2441)

首先，找一个节点所在堆的堆顶要用并查集，而不能暴力向上跳．

再考虑单点查询，若用普通的方法打标记，就得查询点到根路径上的标记之和，最坏情况下可以达到 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度．如果只有堆顶有标记，就可以快速地查询了，但如何做到呢？

可以用类似启发式合并的方式，每次合并的时候把较小的那个堆标记暴力下传到每个节点，然后把较大的堆的标记作为合并后的堆的标记．由于合并后有另一个堆的标记，所以较小的堆下传标记时要下传其标记减去另一个堆的标记．由于每个节点每被合并一次所在堆的大小至少乘二，所以每个节点最多被下放 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次标记，暴力下放标记的总复杂度就是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

再考虑单点加，先删除，再更新，最后插入即可．

然后是全局最大值，可以用一个平衡树/支持删除任意节点的堆（如左偏树）/multiset 来维护每个堆的堆顶．

所以，每个操作分别如下：

  1. 暴力下传点数较小的堆的标记，合并两个堆，更新 size、tag，在 multiset 中删去合并后不在堆顶的那个原堆顶．
  2. 删除节点，更新值，插入回来，更新 multiset．需要分删除节点是否为根来讨论一下．
  3. 堆顶打标记，更新 multiset．
  4. 打全局标记．
  5. 查询值 + 堆顶标记 + 全局标记．
  6. 查询根的值 + 堆顶标记 + 全局标记．
  7. 查询 multiset 最大值 + 全局标记．

棘手的操作参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 ``` |  ```text #include <iostream> #include <set> using namespace std ; constexpr int N = 300010 ; struct Node { int val , ch [ 2 ], d , fa ; Node () { val = ch [ 0 ] = ch [ 1 ] = 0 ; d = -1 ; fa = 0 ; } Node ( int v ) { val = v ; ch [ 0 ] = ch [ 1 ] = d = fa = 0 ; } } t [ N ]; int n , m , f [ N ], tag [ N ], siz [ N ], delta ; char op [ 10 ]; multiset < int > s ; int & rs ( int x ) { return t [ x ]. ch [ t [ t [ x ]. ch [ 1 ]]. d < t [ t [ x ]. ch [ 0 ]]. d ]; } int merge ( int x , int y ) { if ( ! x || ! y ) return x | y ; if ( t [ x ]. val < t [ y ]. val ) swap ( x , y ); int & rs_ref = rs ( x ); rs_ref = merge ( rs_ref , y ); t [ rs_ref ]. fa = x ; t [ x ]. d = t [ rs ( x )]. d \+ 1 ; return x ; } void pushdown ( int x , int y ) { if ( ! x ) return ; t [ x ]. val += y ; pushdown ( t [ x ]. ch [ 0 ], y ); pushdown ( t [ x ]. ch [ 1 ], y ); } int find ( int x ) { return x == f [ x ] ? x : f [ x ] = find ( f [ x ]); } int main () { ios :: sync_with_stdio ( false ); cin . tie ( nullptr ); cin >> n ; for ( int i = 1 ; i <= n ; ++ i ) { int v ; cin >> v ; t [ i ] = Node ( v ); f [ i ] = i ; siz [ i ] = 1 ; s . insert ( v ); } cin >> m ; while ( m \-- ) { cin >> op ; if ( op [ 0 ] == 'U' ) { int x , y ; cin >> x >> y ; x = find ( x ); y = find ( y ); if ( x != y ) { if ( siz [ x ] > siz [ y ]) swap ( x , y ); pushdown ( x , tag [ x ] \- tag [ y ]); f [ x ] = f [ y ] = merge ( x , y ); if ( f [ x ] == x ) { s . erase ( s . find ( t [ y ]. val \+ tag [ y ])); tag [ x ] = tag [ y ]; siz [ x ] += siz [ y ]; tag [ y ] = siz [ y ] = 0 ; } else { s . erase ( s . find ( t [ x ]. val \+ tag [ y ])); siz [ y ] += siz [ x ]; tag [ x ] = siz [ x ] = 0 ; } } } else if ( op [ 0 ] == 'A' ) { if ( op [ 1 ] == '1' ) { int x , v ; cin >> x >> v ; if ( x == find ( x )) { t [ t [ x ]. ch [ 0 ]]. fa = t [ t [ x ]. ch [ 1 ]]. fa = 0 ; int y = merge ( t [ x ]. ch [ 0 ], t [ x ]. ch [ 1 ]); s . erase ( s . find ( t [ x ]. val \+ tag [ x ])); t [ x ]. val += v ; t [ x ]. fa = t [ x ]. ch [ 0 ] = t [ x ]. ch [ 1 ] = 0 ; t [ x ]. d = 1 ; f [ x ] = f [ y ] = merge ( x , y ); s . insert ( t [ f [ x ]]. val \+ tag [ x ]); if ( f [ x ] == y ) { tag [ y ] = tag [ x ]; siz [ y ] = siz [ x ]; tag [ x ] = siz [ x ] = 0 ; } } else { t [ t [ x ]. ch [ 0 ]]. fa = t [ t [ x ]. ch [ 1 ]]. fa = t [ x ]. fa ; t [ t [ x ]. fa ]. ch [ x == t [ t [ x ]. fa ]. ch [ 1 ]] = merge ( t [ x ]. ch [ 0 ], t [ x ]. ch [ 1 ]); t [ x ]. val += v ; t [ x ]. fa = t [ x ]. ch [ 0 ] = t [ x ]. ch [ 1 ] = 0 ; t [ x ]. d = 1 ; int y = find ( x ); f [ x ] = f [ y ] = merge ( x , y ); if ( f [ x ] == x ) { s . erase ( s . find ( t [ y ]. val \+ tag [ y ])); s . insert ( t [ x ]. val \+ tag [ y ]); tag [ x ] = tag [ y ]; siz [ x ] = siz [ y ]; tag [ y ] = siz [ y ] = 0 ; } } } else if ( op [ 1 ] == '2' ) { int x , v ; cin >> x >> v ; x = find ( x ); s . erase ( s . find ( t [ x ]. val \+ tag [ x ])); tag [ x ] += v ; s . insert ( t [ x ]. val \+ tag [ x ]); } else { int v ; cin >> v ; delta += v ; } } else { if ( op [ 1 ] == '1' ) { int x ; cin >> x ; cout << t [ x ]. val \+ tag [ find ( x )] \+ delta << '\n' ; } else if ( op [ 1 ] == '2' ) { int x ; cin >> x ; x = find ( x ); cout << t [ x ]. val \+ tag [ x ] \+ delta << '\n' ; } else { cout << * s . rbegin () \+ delta << '\n' ; } } } return 0 ; } ```   
---|---  
  
### [「BOI2004」Sequence 数字序列](https://www.luogu.com.cn/problem/P4331)

这是一道论文题，详见 [《黄源河 -- 左偏树的特点及其应用》](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2005%E8%AE%BA%E6%96%87%E9%9B%86/%E9%BB%84%E6%BA%90%E6%B2%B3--%E5%B7%A6%E5%81%8F%E6%A0%91%E7%9A%84%E7%89%B9%E7%82%B9%E5%8F%8A%E5%85%B6%E5%BA%94%E7%94%A8/%E9%BB%84%E6%BA%90%E6%B2%B3.pdf)．

## 参考资料

* * *

  1. [Self-Adjusting Heaps](https://epubs.siam.org/doi/10.1137/0215004) ↩

* * *

>  __本页面最近更新： 2026/1/10 01:47:56，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/leftist-tree.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/leftist-tree.md "edit.link.title")  
>  __本页面贡献者：[ouuan](https://github.com/ouuan), [HeRaNO](https://github.com/HeRaNO), [Tiphereth-A](https://github.com/Tiphereth-A), [Yanjun-Zhao](https://github.com/Yanjun-Zhao), [firefly-zjyjoe](https://github.com/firefly-zjyjoe), [Henry-ZHR](https://github.com/Henry-ZHR), [Ir1d](https://github.com/Ir1d), [JiZiQian](https://github.com/JiZiQian), [ksyx](https://github.com/ksyx), [Xeonacid](https://github.com/Xeonacid), [aofall](https://github.com/aofall), [c-forrest](https://github.com/c-forrest), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [FFjet](https://github.com/FFjet), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [llleixx](https://github.com/llleixx), [Marcythm](https://github.com/Marcythm), [Persdre](https://github.com/Persdre), [shuzhouliu](https://github.com/shuzhouliu), [StudyingFather](https://github.com/StudyingFather)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
