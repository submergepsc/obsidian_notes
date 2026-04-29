# 背包 DP - OI Wiki

- Source: https://oi-wiki.org/dp/knapsack/

# 背包 DP

前置知识：[动态规划部分简介](../)．

## 引入

在具体讲何为「背包 dp」前，先来看如下的例题：

[「USACO07 DEC」Charm Bracelet](https://www.luogu.com.cn/problem/P2871)

题意概要：有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品和一个容量为 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的背包，每个物品有重量 𝑤𝑖wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和价值 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两种属性，要求选若干物品放入背包使背包中物品的总价值最大且背包中物品的总重量不超过背包的容量．

在上述例题中，由于每个物体只有两种可能的状态（取与不取），对应二进制中的 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这类问题便被称为「0-1 背包问题」．

## 0-1 背包

### 解释

例题中已知条件有第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品的重量 𝑤𝑖wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，价值 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以及背包的总容量 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

设 DP 状态 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为在只能放前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品的情况下，容量为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的背包所能达到的最大总价值．

考虑转移．假设当前已经处理好了前 𝑖 −1i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品的所有状态，那么对于第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品，当其不放入背包时，背包的剩余容量不变，背包中物品的总价值也不变，故这种情况的最大价值为 𝑓𝑖−1,𝑗fi−1,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；当其放入背包时，背包的剩余容量会减小 𝑤𝑖wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，背包中物品的总价值会增大 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故这种情况的最大价值为 𝑓𝑖−1,𝑗−𝑤𝑖 +𝑣𝑖fi−1,j−wi+vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由此可以得出状态转移方程：

𝑓𝑖,𝑗=max(𝑓𝑖−1,𝑗,𝑓𝑖−1,𝑗−𝑤𝑖+𝑣𝑖)fi,j=max(fi−1,j,fi−1,j−wi+vi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里如果直接采用二维数组对状态进行记录，会出现 MLE．可以考虑改用滚动数组的形式来优化．

由于对 𝑓𝑖fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有影响的只有 𝑓𝑖−1fi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以去掉第一维，直接用 𝑓𝑖fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来表示处理到当前物品时背包容量为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大价值，得出以下方程：

𝑓𝑗=max(𝑓𝑗,𝑓𝑗−𝑤𝑖+𝑣𝑖)fj=max(fj,fj−wi+vi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**务必牢记并理解这个转移方程，因为大部分背包问题的转移方程都是在此基础上推导出来的．**

### 实现

还有一点需要注意的是，很容易写出这样的 **错误核心代码** ：

C++Python

```text 1 2 3 4 5 ``` |  ```text for ( int i = 1 ; i <= n ; i ++ ) for ( int l = 0 ; l <= W \- w [ i ]; l ++ ) f [ l \+ w [ i ]] = max ( f [ l ] \+ v [ i ], f [ l \+ w [ i ]]); // 由 f[i][l + w[i]] = max(max(f[i - 1][l + w[i]], f[i - 1][l] + w[i]), // f[i][l + w[i]]); 简化而来 ```   
---|---  
  
```text 1 2 3 4 5 ``` |  ```text for i in range ( 1 , n \+ 1 ): for l in range ( 0 , W \- w [ i ] \+ 1 ): f [ l \+ w [ i ]] = max ( f [ l ] \+ v [ i ], f [ l \+ w [ i ]]) # 由 f[i][l + w[i]] = max(max(f[i - 1][l + w[i]], f[i - 1][l] + w[i]), # f[i][l + w[i]]) 简化而来 ```   
---|---  
  
这段代码哪里错了呢？枚举顺序错了．

仔细观察代码可以发现：对于当前处理的物品 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和当前状态 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在 𝑗 ⩾𝑤𝑖j⩾wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是会被 𝑓𝑖,𝑗−𝑤𝑖fi,j−wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所影响的．这就相当于物品 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以多次被放入背包，与题意不符．（事实上，这正是完全背包问题的解法）

为了避免这种情况发生，我们可以改变枚举的顺序，从 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚举到 𝑤𝑖wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样就不会出现上述的错误，因为 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是在 𝑓𝑖,𝑗−𝑤𝑖fi,j−wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 前被更新．

因此实际核心代码为

C++Python

```text 1 2 ``` |  ```text for ( int i = 1 ; i <= n ; i ++ ) for ( int l = W ; l >= w [ i ]; l \-- ) f [ l ] = max ( f [ l ], f [ l \- w [ i ]] \+ v [ i ]); ```   
---|---  
  
```text 1 2 3 ``` |  ```text for i in range ( 1 , n \+ 1 ): for l in range ( W , w [ i ] \- 1 , \- 1 ): f [ l ] = max ( f [ l ], f [ l \- w [ i ]] \+ v [ i ]) ```   
---|---  
  
例题代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text #include <iostream> using namespace std ; constexpr int MAXN = 13010 ; int n , W , w [ MAXN ], v [ MAXN ], f [ MAXN ]; int main () { cin >> n >> W ; for ( int i = 1 ; i <= n ; i ++ ) cin >> w [ i ] >> v [ i ]; // 读入数据 for ( int i = 1 ; i <= n ; i ++ ) for ( int l = W ; l >= w [ i ]; l \-- ) if ( f [ l \- w [ i ]] \+ v [ i ] > f [ l ]) f [ l ] = f [ l \- w [ i ]] \+ v [ i ]; // 状态方程 cout << f [ W ]; return 0 ; } ```   
---|---  
  
## 完全背包

### 解释

完全背包模型与 0-1 背包类似，与 0-1 背包的区别仅在于一个物品可以选取无限次，而非仅能选取一次．

我们可以借鉴 0-1 背包的思路，进行状态定义：设 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为只能选前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品时，容量为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的背包可以达到的最大价值．

需要注意的是，虽然定义与 0-1 背包类似，但是其状态转移方程与 0-1 背包并不相同．

### 过程

可以考虑一个朴素的做法：对于第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 件物品，枚举其选了多少个来转移．这样做的时间复杂度是 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

状态转移方程如下：

𝑓𝑖,𝑗=+∞max𝑘=0(𝑓𝑖−1,𝑗−𝑘×𝑤𝑖+𝑣𝑖×𝑘)fi,j=maxk=0+∞(fi−1,j−k×wi+vi×k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

考虑做一个简单的优化．可以发现，对于 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只要通过 𝑓𝑖,𝑗−𝑤𝑖fi,j−wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转移就可以了．因此状态转移方程为：

𝑓𝑖,𝑗=max(𝑓𝑖−1,𝑗,𝑓𝑖,𝑗−𝑤𝑖+𝑣𝑖)fi,j=max(fi−1,j,fi,j−wi+vi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

理由是当我们这样转移时，𝑓𝑖,𝑗−𝑤𝑖fi,j−wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 已经由 𝑓𝑖,𝑗−2×𝑤𝑖fi,j−2×wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更新过，那么 𝑓𝑖,𝑗−𝑤𝑖fi,j−wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是充分考虑了第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 件物品所选次数后得到的最优结果．换言之，我们通过局部最优子结构的性质重复使用了之前的枚举过程，优化了枚举的复杂度．

与 0-1 背包相同，我们可以将第一维去掉来优化空间复杂度．如果理解了 0-1 背包的优化方式，就不难明白压缩后的循环是正向的（也就是上文中提到的错误优化）．

[「Luogu P1616」疯狂的采药](https://www.luogu.com.cn/problem/P1616)

题意概要：有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种物品和一个容量为 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的背包，每种物品有重量 𝑤𝑖wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和价值 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两种属性，要求选若干个物品放入背包使背包中物品的总价值最大且背包中物品的总重量不超过背包的容量．

例题代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text #include <iostream> using namespace std ; constexpr int MAXN = 1e4 \+ 5 ; constexpr int MAXW = 1e7 \+ 5 ; int n , W , w [ MAXN ], v [ MAXN ]; long long f [ MAXW ]; int main () { cin >> W >> n ; for ( int i = 1 ; i <= n ; i ++ ) cin >> w [ i ] >> v [ i ]; for ( int i = 1 ; i <= n ; i ++ ) for ( int l = w [ i ]; l <= W ; l ++ ) if ( f [ l \- w [ i ]] \+ v [ i ] > f [ l ]) f [ l ] = f [ l \- w [ i ]] \+ v [ i ]; // 核心状态方程 cout << f [ W ]; return 0 ; } ```   
---|---  
  
## 多重背包

多重背包也是 0-1 背包的一个变式．与 0-1 背包的区别在于每种物品有 𝑘𝑖ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，而非一个．

一个很朴素的想法就是：把「每种物品选 𝑘𝑖ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次」等价转换为「有 𝑘𝑖ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个相同的物品，每个物品选一次」．这样就转换成了一个 0-1 背包模型，套用上文所述的方法就可已解决．状态转移方程如下：

𝑓𝑖,𝑗=𝑘𝑖max𝑘=0(𝑓𝑖−1,𝑗−𝑘×𝑤𝑖+𝑣𝑖×𝑘)fi,j=maxk=0ki(fi−1,j−k×wi+vi×k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

时间复杂度 𝑂(𝑊∑𝑛𝑖=1𝑘𝑖)O(W∑i=1nki)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

核心代码

```text 1 2 3 4 5 6 7 8 ``` |  ```text for ( int i = 1 ; i <= n ; i ++ ) { for ( int weight = W ; weight >= w [ i ]; weight \-- ) { // 多遍历一层物品数量 for ( int k = 1 ; k * w [ i ] <= weight && k <= cnt [ i ]; k ++ ) { dp [ weight ] = max ( dp [ weight ], dp [ weight \- k * w [ i ]] \+ k * v [ i ]); } } } ```   
---|---  
  
### 二进制分组优化

考虑优化．我们仍考虑把多重背包转化成 0-1 背包模型来求解．

### 解释

显然，复杂度中的 𝑂(𝑛𝑊)O(nW)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 部分无法再优化了，我们只能从 𝑂(∑𝑘𝑖)O(∑ki)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处入手．为了表述方便，我们用 𝐴𝑖,𝑗Ai,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代表第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种物品拆分出的第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品．

在朴素的做法中，∀𝑗 ≤𝑘𝑖∀j≤ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐴𝑖,𝑗Ai,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均表示相同物品．那么我们效率低的原因主要在于我们进行了大量重复性的工作．举例来说，我们考虑了「同时选 𝐴𝑖,1,𝐴𝑖,2Ai,1,Ai,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」与「同时选 𝐴𝑖,2,𝐴𝑖,3Ai,2,Ai,3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」这两个完全等效的情况．这样的重复性工作我们进行了许多次．那么优化拆分方式就成为了解决问题的突破口．

### 过程

我们可以通过「二进制分组」的方式使拆分方式更加优美．

具体地说就是令 𝐴𝑖,𝑗(𝑗∈[0,⌊log2⁡(𝑘𝑖+1)⌋−1])Ai,j(j∈[0,⌊log2⁡(ki+1)⌋−1])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别表示由 2𝑗2j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个单个物品「捆绑」而成的大物品．特殊地，若 𝑘𝑖 +1ki+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数次幂，则需要在最后添加一个由 𝑘𝑖 −2⌊log2⁡(𝑘𝑖+1)⌋−1ki−2⌊log2⁡(ki+1)⌋−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个单个物品「捆绑」而成的大物品用于补足．

举几个例子：

  * 6 =1 +2 +36=1+2+3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 8 =1 +2 +4 +18=1+2+4+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 18 =1 +2 +4 +8 +318=1+2+4+8+3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 31 =1 +2 +4 +8 +1631=1+2+4+8+16![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

显然，通过上述拆分方式，可以表示任意 ≤𝑘𝑖≤ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品的等效选择方式．将每种物品按照上述方式拆分后，使用 0-1 背包的方法解决即可．

时间复杂度 𝑂(𝑊∑𝑛𝑖=1log2⁡𝑘𝑖)O(W∑i=1nlog2⁡ki)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 实现

二进制分组代码

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text index = 0 ; for ( int i = 1 ; i <= m ; i ++ ) { int c = 1 , p , h , k ; cin >> p >> h >> k ; while ( k > c ) { k -= c ; list [ ++ index ]. w = c * p ; list [ index ]. v = c * h ; c *= 2 ; } list [ ++ index ]. w = p * k ; list [ index ]. v = h * k ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text index = 0 for i in range ( 1 , m \+ 1 ): c = 1 p , h , k = map ( int , input () . split ()) while k > c : k -= c index += 1 list [ index ] . w = c * p list [ index ] . v = c * h c *= 2 index += 1 list [ index ] . w = p * k list [ index ] . v = h * k ```   
---|---  
  
### 单调队列优化

见 [单调队列/单调栈优化](../opt/monotonous-queue-stack/)．

习题：[「Luogu P1776」宝物筛选_NOI 导刊 2010 提高（02）](https://www.luogu.com.cn/problem/P1776)

## 混合背包

混合背包就是将前面三种的背包问题混合起来，有的只能取一次，有的能取无限次，有的只能取 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．

这种题目看起来很吓人，可是只要领悟了前面几种背包的中心思想，并将其合并在一起就可以了．下面给出伪代码：

```text 1 2 3 4 5 6 7 8 ``` |  ```text for (循环物品种类) { if (是 0 - 1 背包) 套用 0 - 1 背包代码; else if (是完全背包) 套用完全背包代码; else if (是多重背包) 套用多重背包代码; } ```   
---|---  
  
### 例题

[「Luogu P1833」樱花](https://www.luogu.com.cn/problem/P1833)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种樱花树和长度为 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间，有的樱花树只能看一遍，有的樱花树最多看 𝐴𝑖Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍，有的樱花树可以看无数遍．每棵樱花树都有一个美学值 𝐶𝑖Ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求在 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内看哪些樱花树能使美学值最高．

核心代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text for ( int i = 1 ; i <= n ; i ++ ) { if ( cnt [ i ] == 0 ) { // 如果数量没有限制使用完全背包的核心代码 for ( int weight = w [ i ]; weight <= W ; weight ++ ) { dp [ weight ] = max ( dp [ weight ], dp [ weight \- w [ i ]] \+ v [ i ]); } } else { // 物品有限使用多重背包的核心代码，它也可以处理0-1背包问题 for ( int weight = W ; weight >= w [ i ]; weight \-- ) { for ( int k = 1 ; k * w [ i ] <= weight && k <= cnt [ i ]; k ++ ) { dp [ weight ] = max ( dp [ weight ], dp [ weight \- k * w [ i ]] \+ k * v [ i ]); } } } } ```   
---|---  
  
习题：[HDU 5410 CRB and His Birthday](https://acm.hdu.edu.cn/showproblem.php?pid=5410)

## 二维费用背包

[「Luogu P1855」榨取 kkksc03](https://www.luogu.com.cn/problem/P1855)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个任务需要完成，完成第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个任务需要花费 𝑡𝑖ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分钟，产生 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元的开支．

现在有 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分钟时间，𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元钱来处理这些任务，求最多能完成多少任务．

这道题是很明显的 0-1 背包问题，可是不同的是选一个物品会消耗两种价值（经费、时间），只需在状态中增加一维存放第二种价值即可．

这时候就要注意，再开一维存放物品编号就不合适了，因为容易 MLE．

### 实现

C++Python

```text 1 2 3 4 ``` |  ```text for ( int k = 1 ; k <= n ; k ++ ) for ( int i = m ; i >= mi ; i \-- ) // 对经费进行一层枚举 for ( int j = t ; j >= ti ; j \-- ) // 对时间进行一层枚举 dp [ i ][ j ] = max ( dp [ i ][ j ], dp [ i \- mi ][ j \- ti ] \+ 1 ); ```   
---|---  
  
```text 1 2 3 4 ``` |  ```text for k in range ( 1 , n \+ 1 ): for i in range ( m , mi \- 1 , \- 1 ): # 对经费进行一层枚举 for j in range ( t , ti \- 1 , \- 1 ): # 对时间进行一层枚举 dp [ i ][ j ] = max ( dp [ i ][ j ], dp [ i \- mi ][ j \- ti ] \+ 1 ) ```   
---|---  
  
## 分组背包

[「Luogu P1757」通天之分组背包](https://www.luogu.com.cn/problem/P1757)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 件物品和一个大小为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的背包，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品的价值为 𝑤𝑖wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，体积为 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．同时，每个物品属于一个组，同组内最多只能选择一个物品．求背包能装载物品的最大总价值．

这种题怎么想呢？其实是从「在所有物品中选择一件」变成了「从当前组中选择一件」，于是就对每一组进行一次 0-1 背包就可以了．

再说一说如何进行存储．我们可以将 𝑡𝑘,𝑖tk,i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 件物品的编号是多少，再用 cnt𝑘cntk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组物品有多少个．

### 实现

C++Python

```text 1 2 3 4 5 6 ``` |  ```text for ( int k = 1 ; k <= ts ; k ++ ) // 循环每一组 for ( int i = m ; i >= 0 ; i \-- ) // 循环背包容量 for ( int j = 1 ; j <= cnt [ k ]; j ++ ) // 循环该组的每一个物品 if ( i >= w [ t [ k ][ j ]]) // 背包容量充足 dp [ i ] = max ( dp [ i ], dp [ i \- w [ t [ k ][ j ]]] \+ c [ t [ k ][ j ]]); // 像0-1背包一样状态转移 ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text for k in range ( 1 , ts \+ 1 ): # 循环每一组 for i in range ( m , \- 1 , \- 1 ): # 循环背包容量 for j in range ( 1 , cnt [ k ] \+ 1 ): # 循环该组的每一个物品 if i >= w [ t [ k ][ j ]]: # 背包容量充足 dp [ i ] = max ( dp [ i ], dp [ i \- w [ t [ k ][ j ]]] \+ c [ t [ k ][ j ]] ) # 像0-1背包一样状态转移 ```   
---|---  
  
这里要注意：**一定不能搞错循环顺序** ，这样才能保证正确性．

## 有依赖的背包

[「Luogu P1064」金明的预算方案](https://www.luogu.com.cn/problem/P1064)

金明有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元钱，想要买 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 件物品的价格为 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，重要度为 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．有些物品是从属于某个主件物品的附件，要买这个物品，必须购买它的主件．

目标是让所有购买的物品的 𝑣𝑖 ×𝑝𝑖vi×pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之和最大．

考虑分类讨论．对于一个主件和它的若干附件，有以下几种可能：只买主件，买主件 + 某些附件．因为这几种可能性只能选一种，所以可以将这看成分组背包．

如果是多叉树的集合，则要先算子节点的集合，最后算父节点的集合．

## 泛化物品的背包

这种背包，没有固定的费用和价值，它的价值是随着分配给它的费用而定．在背包容量为 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的背包问题中，当分配给它的费用为 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，能得到的价值就是 ℎ(𝑣𝑖)h(vi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这时，将固定的价值换成函数的引用即可．

## 杂项

### 小优化

根据贪心原理，当费用相同时，只需保留价值最高的；当价值一定时，只需保留费用最低的；当有两件物品 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的价值大于 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的价值并且 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的费用小于 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的费用时，只需保留 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 背包问题变种

#### 输出方案

输出方案其实就是记录下来背包中的某一个状态是怎么推出来的．我们可以用 𝑔𝑖,𝑣gi,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 件物品占用空间为 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时候是否选择了此物品．然后在转移时记录是选用了哪一种策略（选或不选）．输出时的伪代码：

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text int v = V ; // 记录当前的存储空间 // 因为最后一件物品存储的是最终状态，所以从最后一件物品进行循环 for ( 从最后一件循环至第一件 ) { if ( g [ i ][ v ]) { 选了第 i 项物品 ; v -= 第 i 项物品的重量 ; } else { 未选第 i 项物品 ; } } ```   
---|---  
  
#### 求方案数

对于给定的一个背包容量、物品费用、其他关系等的问题，求装到一定容量的方案总数．

这种问题就是把求最大值换成求和即可．

例如 0-1 背包问题的转移方程就变成了：

dp𝑗←dp𝑗+dp𝑗−𝑐𝑖(𝑗≥𝑐𝑖)dpj←dpj+dpj−ci(j≥ci)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

初始条件：dp0 =1dp0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为当容量为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时也有一个方案，即什么都不装．

#### 求最优方案总数

要求最优方案总数，我们要对 0-1 背包里的 dpdp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组的定义稍作修改，DP 状态 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为在只能放前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品的情况下，容量为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的背包「正好装满」所能达到的最大总价值．

这样修改之后，每一种 DP 状态都可以用一个 𝑔𝑖,𝑗gi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来表示方案数．

𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示只考虑前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品时背包体积「正好」是 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时的最大价值．

𝑔𝑖,𝑗gi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示只考虑前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品时背包体积「正好」是 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时的方案数．

转移方程：

如果 𝑓𝑖,𝑗 =𝑓𝑖−1,𝑗fi,j=fi−1,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓𝑖,𝑗 ≠𝑓𝑖−1,𝑗−𝑣 +𝑤fi,j≠fi−1,j−v+w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 说明我们此时不选择把物品放入背包更优，方案数由 𝑔𝑖−1,𝑗gi−1,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转移过来，

如果 𝑓𝑖,𝑗 ≠𝑓𝑖−1,𝑗fi,j≠fi−1,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓𝑖,𝑗 =𝑓𝑖−1,𝑗−𝑣 +𝑤fi,j=fi−1,j−v+w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 说明我们此时选择把物品放入背包更优，方案数由 𝑔𝑖−1,𝑗−𝑣gi−1,j−v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转移过来，

如果 𝑓𝑖,𝑗 =𝑓𝑖−1,𝑗fi,j=fi−1,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓𝑖,𝑗 =𝑓𝑖−1,𝑗−𝑣 +𝑤fi,j=fi−1,j−v+w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 说明放入或不放入都能取得最优解，方案数由 𝑔𝑖−1,𝑗gi−1,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔𝑖−1,𝑗−𝑣gi−1,j−v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转移过来．

初始条件：

```text 1 2 3 4 5 ``` |  ```text memset ( f , 0xcf , sizeof ( f )); // 因为是求最大值，初始化为负无穷，避免没有装满而进行了转移 // 若求最小值，则初始化为正无穷0x3f f [ 0 ] = 0 ; g [ 0 ] = 1 ; // 什么都不装是一种方案 ```   
---|---  
  
因为背包体积最大值有可能装不满，所以最优解不一定是 𝑓𝑚fm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最后我们通过找到最优解的价值，把 𝑔𝑗gj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组里取到最优解的所有方案数相加即可．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` |  ```text for ( int i = 0 ; i < N ; i ++ ) { for ( int j = V ; j >= v [ i ]; j \-- ) { int tmp = std :: max ( dp [ j ], dp [ j \- v [ i ]] \+ w [ i ]); int c = 0 ; if ( tmp == dp [ j ]) c += cnt [ j ]; // 如果从dp[j]转移 if ( tmp == dp [ j \- v [ i ]] \+ w [ i ]) c += cnt [ j \- v [ i ]]; // 如果从dp[j-v[i]]转移 dp [ j ] = tmp ; cnt [ j ] = c ; } } int max = 0 ; // 寻找最优解 for ( int i = 0 ; i <= V ; i ++ ) { max = std :: max ( max , dp [ i ]); } int res = 0 ; for ( int i = 0 ; i <= V ; i ++ ) { if ( dp [ i ] == max ) { res += cnt [ i ]; // 求和最优解方案数 } } ```   
---|---  
  
#### 背包的第 k 优解

普通的 0-1 背包是要求最优解，在普通的背包 DP 方法上稍作改动，增加一维用于记录当前状态下的前 k 优解，即可得到求 0-1 背包第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 优解的算法． 具体来讲：dpi,j,kdpi,j,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记录了前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品中，选择的物品总体积为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，能够得到的第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大的价值和．这个状态可以理解为将普通 0-1 背包只用记录一个数据的 dpi,jdpi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 扩展为记录一个有序的优解序列．转移时，普通背包最优解的求法是 dpi,j =max(dpi−1,j,dpi−1,j−vi +𝑤𝑖)dpi,j=max(dpi−1,j,dpi−1,j−vi+wi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，现在我们则是要合并 dpi−1,jdpi−1,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，dpi−1,j−vi +𝑤𝑖dpi−1,j−vi+wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这两个大小为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的递减序列，并保留合并后前 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大的价值记在 dpi,jdpi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 里，这一步利用双指针法，复杂度是 𝑂(𝑘)O(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，整体时间复杂度为 𝑂(𝑛𝑚𝑘)O(nmk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．空间上，此方法与普通背包一样可以压缩掉第一维，复杂度是 𝑂(𝑚𝑘)O(mk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

例题 [HDU 2639 Bone Collector II](https://acm.hdu.edu.cn/showproblem.php?pid=2639)

求 0-1 背包的严格第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 优解．𝑛 ≤100,𝑣 ≤1000,𝑘 ≤30n≤100,v≤1000,k≤30![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text memset ( dp , 0 , sizeof ( dp )); int i , j , p , x , y , z ; scanf ( "%d%d%d" , & n , & m , & K ); for ( i = 0 ; i < n ; i ++ ) scanf ( "%d" , & w [ i ]); for ( i = 0 ; i < n ; i ++ ) scanf ( "%d" , & c [ i ]); for ( i = 0 ; i < n ; i ++ ) { for ( j = m ; j >= c [ i ]; j \-- ) { for ( p = 1 ; p <= K ; p ++ ) { a [ p ] = dp [ j \- c [ i ]][ p ] \+ w [ i ]; b [ p ] = dp [ j ][ p ]; } a [ p ] = b [ p ] = -1 ; x = y = z = 1 ; while ( z <= K && ( a [ x ] != -1 || b [ y ] != -1 )) { if ( a [ x ] > b [ y ]) dp [ j ][ z ] = a [ x ++ ]; else dp [ j ][ z ] = b [ y ++ ]; if ( dp [ j ][ z ] != dp [ j ][ z \- 1 ]) z ++ ; } } } printf ( "%d \n " , dp [ m ][ K ]); ```   
---|---  
  
## 参考资料与注释

  * [背包问题九讲 - 崔添翼](https://github.com/tianyicui/pack)．

* * *

>  __本页面最近更新： 2026/1/21 10:53:40，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/dp/knapsack.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/dp/knapsack.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [Marcythm](https://github.com/Marcythm), [partychicken](https://github.com/partychicken), [H-J-Granger](https://github.com/H-J-Granger), [NachtgeistW](https://github.com/NachtgeistW), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [Tiphereth-A](https://github.com/Tiphereth-A), [weiranfu](https://github.com/weiranfu), [greyqz](https://github.com/greyqz), [iamtwz](https://github.com/iamtwz), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [ouuan](https://github.com/ouuan), [paigeman](https://github.com/paigeman), [wolfdan666](https://github.com/wolfdan666), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [GoodCoder666](https://github.com/GoodCoder666), [Henry-ZHR](https://github.com/Henry-ZHR), [HeRaNO](https://github.com/HeRaNO), [Link-cute](https://github.com/Link-cute), [LovelyBuggies](https://github.com/LovelyBuggies), [LuoshuiTianyi](https://github.com/LuoshuiTianyi), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [odeinjul](https://github.com/odeinjul), [oldoldtea](https://github.com/oldoldtea), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [shenshuaijie](https://github.com/shenshuaijie), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [Xeonacid](https://github.com/Xeonacid), [xyf007](https://github.com/xyf007), [Alisahhh](https://github.com/Alisahhh), [Alphnia](https://github.com/Alphnia), [c-forrest](https://github.com/c-forrest), [cbw2007](https://github.com/cbw2007), [dhbloo](https://github.com/dhbloo), [fps5283](https://github.com/fps5283), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [hsfzLZH1](https://github.com/hsfzLZH1), [hydingsy](https://github.com/hydingsy), [kenlig](https://github.com/kenlig), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Menci](https://github.com/Menci), [n-WN](https://github.com/n-WN), [Peanut-Tang](https://github.com/Peanut-Tang), [PlanariaIce](https://github.com/PlanariaIce), [sbofgayschool](https://github.com/sbofgayschool), [shawlleyw](https://github.com/shawlleyw), [Siyuan](mailto:294873684@qq.com), [SukkaW](https://github.com/SukkaW), [TianKong-y](https://github.com/TianKong-y), [tLLWtG](https://github.com/tLLWtG), [WAAutoMaton](https://github.com/WAAutoMaton), [x4Cx58x54](https://github.com/x4Cx58x54), [xk2013](https://github.com/xk2013), [zhb2000](https://github.com/zhb2000), [zhufengning](https://github.com/zhufengning)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
