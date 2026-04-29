# 动态规划基础 - OI Wiki

- Source: https://oi-wiki.org/dp/basic/

# 动态规划基础

本页面主要介绍了动态规划的基本思想，以及动态规划中状态及状态转移方程的设计思路，帮助各位初学者对动态规划有一个初步的了解．

本部分的其他页面，将介绍各种类型问题中动态规划模型的建立方法，以及一些动态规划的优化技巧．

## 引入

[[IOI1994] 数字三角形](https://www.luogu.com.cn/problem/P1216)

给定一个 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行的数字三角形（𝑟 ≤1000r≤1000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），需要找到一条从最高点到底部任意处结束的路径，使路径经过数字的和最大．每一步可以走到当前点左下方的点或右下方的点．

```text 1 2 3 4 5 ``` |  ```text 7 3 8 8 1 0 2 7 4 4 4 5 2 6 5 ```   
---|---  
  
在上面这个例子中，最优路径是 7 →3 →8 →7 →57→3→8→7→5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最简单粗暴的思路是尝试所有的路径．因为路径条数是 𝑂(2𝑟)O(2r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别的，这样的做法无法接受．

注意到这样一个事实，一条最优的路径，它的每一步决策都是最优的．

以例题里提到的最优路径为例，只考虑前四步 7 →3 →8 →77→3→8→7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不存在一条从最顶端到 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行第 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数的权值更大的路径．

而对于每一个点，它的下一步决策只有两种：往左下角或者往右下角（如果存在）．因此只需要记录当前点的最大权值，用这个最大权值执行下一步决策，来更新后续点的最大权值．

这样做还有一个好处：我们成功缩小了问题的规模，将一个问题分成了多个规模更小的问题．要想得到从顶端到第 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行的最优方案，只需要知道从顶端到第 𝑟 −1r−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行的最优方案的信息就可以了．

这时候还存在一个问题：子问题间重叠的部分会有很多，同一个子问题可能会被重复访问多次，效率还是不高．解决这个问题的方法是把每个子问题的解存储下来，通过记忆化的方式限制访问顺序，确保每个子问题只被访问一次．

上面就是动态规划的一些基本思路．下面将会更系统地介绍动态规划的思想．

## 动态规划原理

能用动态规划解决的问题，需要满足三个条件：最优子结构，无后效性和子问题重叠．

### 最优子结构

具有最优子结构也可能是适合用贪心的方法求解．

注意要确保我们考察了最优解中用到的所有子问题．

  1. 证明问题最优解的第一个组成部分是做出一个选择；
  2. 对于一个给定问题，在其可能的第一步选择中，假定你已经知道哪种选择才会得到最优解．你现在并不关心这种选择具体是如何得到的，只是假定已经知道了这种选择；
  3. 给定可获得的最优解的选择后，确定这次选择会产生哪些子问题，以及如何最好地刻画子问题空间；
  4. 证明作为构成原问题最优解的组成部分，每个子问题的解就是它本身的最优解．方法是反证法，考虑加入某个子问题的解不是其自身的最优解，那么就可以从原问题的解中用该子问题的最优解替换掉当前的非最优解，从而得到原问题的一个更优的解，从而与原问题最优解的假设矛盾．

要保持子问题空间尽量简单，只在必要时扩展．

最优子结构的不同体现在两个方面：

  1. 原问题的最优解中涉及多少个子问题；
  2. 确定最优解使用哪些子问题时，需要考察多少种选择．

子问题图中每个定点对应一个子问题，而需要考察的选择对应关联至子问题顶点的边．

### 无后效性

已经求解的子问题，不会再受到后续决策的影响．

### 子问题重叠

如果有大量的重叠子问题，我们可以用空间将这些子问题的解存储下来，避免重复求解相同的子问题，从而提升效率．

### 基本思路

对于一个能用动态规划解决的问题，一般采用如下思路解决：

  1. 将原问题划分为若干 **阶段** ，每个阶段对应若干个子问题，提取这些子问题的特征（称之为 **状态** ）；
  2. 寻找每一个状态的可能 **决策** ，或者说是各状态间的相互转移方式（用数学的语言描述就是 **状态转移方程** ）．
  3. 按顺序求解每一个阶段的问题．

如果用图论的思想理解，我们建立一个 [有向无环图](../../graph/dag/)，每个状态对应图上一个节点，决策对应节点间的连边．这样问题就转变为了一个在 DAG 上寻找最长（短）路的问题（参见：[DAG 上的 DP](../dag/)）．

## 最长公共子序列

最长公共子序列问题

给定一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和一个 长度为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑛,𝑚 ≤5000n,m≤5000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），求出一个最长的序列，使得该序列既是 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子序列，也是 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子序列．

子序列的定义可以参考 [子序列](../../string/basic/)．一个简要的例子：字符串 `abcde` 与字符串 `acde` 的公共子序列有 `a`、`c`、`d`、`e`、`ac`、`ad`、`ae`、`cd`、`ce`、`de`、`acd`、`ade`、`ace`、`cde`、`acde`，最长公共子序列的长度是 4．

设 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示只考虑 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素，𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素时的最长公共子序列的长度，求这时的最长公共子序列的长度就是 **子问题** ．𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是我们所说的 **状态** ，则 𝑓(𝑛,𝑚)f(n,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是最终要达到的状态，即为所求结果．

对于每个 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，存在三种决策：如果 𝐴𝑖 =𝐵𝑗Ai=Bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则可以将它接到公共子序列的末尾；另外两种决策分别是跳过 𝐴𝑖Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或者 𝐵𝑗Bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．状态转移方程如下：

𝑓(𝑖,𝑗)={𝑓(𝑖−1,𝑗−1)+1𝐴𝑖=𝐵𝑗max(𝑓(𝑖−1,𝑗),𝑓(𝑖,𝑗−1))𝐴𝑖≠𝐵𝑗f(i,j)={f(i−1,j−1)+1Ai=Bjmax(f(i−1,j),f(i,j−1))Ai≠Bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可参考 [SourceForge 的 LCS 交互网页](http://lcs-demo.sourceforge.net/) 来更好地理解 LCS 的实现过程．

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text int n , m , a [ MAXN ], b [ MAXM ], f [ MAXN ][ MAXM ]; int dp () { for ( int i = 1 ; i <= n ; i ++ ) for ( int j = 1 ; j <= m ; j ++ ) if ( a [ i ] == b [ j ]) f [ i ][ j ] = f [ i \- 1 ][ j \- 1 ] \+ 1 ; else f [ i ][ j ] = std :: max ( f [ i \- 1 ][ j ], f [ i ][ j \- 1 ]); return f [ n ][ m ]; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 ``` |  ```text def dp ( n , m , a , b ) : f = [[ 0 ] * ( m \+ 1 ) for _ in range ( n \+ 1 )] for i in range ( 1 , n \+ 1 ) : for j in range ( 1 , m \+ 1 ) : if a [ i ] == b [ j ] : f [ i ][ j ] = f [ i \- 1 ][ j \- 1 ] \+ 1 else : f [ i ][ j ] = max ( f [ i \- 1 ][ j ], f [ i ][ j \- 1 ]) return f [ n ][ m ] ```   
---|---  
  
该做法的时间复杂度为 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

另外，本题存在 𝑂(𝑛𝑚𝑤)O(nmw)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的算法1．有兴趣的同学可以自行探索．

## 最长不下降子序列

最长不下降子序列问题

给定一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑛 ≤5000n≤5000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），求出一个最长的 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子序列，满足该子序列的后一个元素不小于前一个元素．

### 算法一

设 𝑓(𝑖)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示以 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为结尾的最长不下降子序列的长度，则所求为 max1≤𝑖≤𝑛𝑓(𝑖)max1≤i≤nf(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

计算 𝑓(𝑖)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，尝试将 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 接到其他的最长不下降子序列后面，以更新答案．于是可以写出这样的状态转移方程：𝑓(𝑖) =max1≤𝑗<𝑖, 𝑎𝑗≤𝑎𝑖(𝑓(𝑗) +1)f(i)=max1≤j<i, aj≤ai(f(j)+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text int n , a [ MAXN ], d [ MAXN ]; int dp () { d [ 1 ] = 1 ; int ans = 1 ; for ( int i = 2 ; i <= n ; i ++ ) { d [ i ] = 1 ; for ( int j = 1 ; j < i ; j ++ ) if ( a [ j ] <= a [ i ]) { d [ i ] = std :: max ( d [ i ], d [ j ] \+ 1 ); ans = std :: max ( ans , d [ i ]); } } return ans ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text def dp ( n , a ): d = [ 0 ] * ( n \+ 1 ) d [ 1 ] = 1 ans = 1 for i in range ( 2 , n \+ 1 ): d [ i ] = 1 for j in range ( 1 , i ): if a [ j ] <= a [ i ]: d [ i ] = max ( d [ i ], d [ j ] \+ 1 ) ans = max ( ans , d [ i ]) return ans ```   
---|---  
  
容易发现该算法的时间复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 算法二

当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的范围扩大到 𝑛 ≤105n≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，第一种做法就不够快了，下面给出了一个 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的做法．

考虑之前定义的状态 (𝑖,𝑙)(i,l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示序列以第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素结尾的不下降子序列最长为 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．不同于以往按固定 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处理状态的方法，这里直接判断 (𝑖,𝑙)(i,l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否合法：

  * 初始状态 (1,1)(1,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然合法．
  * 对于任意 (𝑖,𝑙)(i,l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果存在 𝑗 <𝑖j<i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 (𝑗,𝑙 −1)(j,l−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 合法，同时 𝑎𝑗 ≤𝑎𝑖aj≤ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 (𝑖,𝑙)(i,l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 合法．

最终，只需要找到合法状态中 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最大的 (𝑖,𝑙)(i,l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即可得到最长不下降子序列的长度．

设原序列为 𝑎1,⋯,𝑎𝑛a1,⋯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义数组 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中第 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位表示长度为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的不下降子序列末尾元素的最小值．初始时序列为空．令 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 从 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍历，依次求出前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的最长不下降子序列的长度．对于当前元素 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

  * 如果 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大于等于序列 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中最后一个元素，直接将元素 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 插入到序列 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的末尾．
    * 解释：若 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大于等于当前最长子序列的末尾元素，说明存在一个不下降子序列可以接上 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．不插入将破坏最优性．
  * 如果 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 严格小于 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中最后一个元素，找到 **第一个** 大于它的元素，并用 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 替换它．
    * 解释：若直接插在末尾，会破坏 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的单调性；替换操作可以保证每个长度的末尾元素尽可能小，从而为后续元素保留更多可能性．
    * 优化：因为 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单调不减，可用二分查找直接找到元素的插入位置，将整体复杂度降低到 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而非暴力查找的 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

如果还要输出具体的最长不下降子序列，可以额外维护数组 𝑑′𝑥dx′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示长度为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的不下降子序列中末尾最小元素的位置（有多个可任选一个）．具体维护时，只需要在插入元素 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑑𝑥dx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，同时更新 𝑑′𝑥dx′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．同时，需要记录 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最优前驱 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑑′𝑥−1dx−1′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．最终，从任意最大长度状态出发，沿前驱 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 回溯，即可得到完整子序列．

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text int n , a [ MAXN ], d [ MAXN ], di [ MAXN ], pre [ MAXN ], res [ MAXN ]; int dp () { int ans = 0 ; for ( int i = 1 ; i <= n ; ++ i ) { int tmp = std :: upper_bound ( d , d \+ ans , a [ i ]) \- d ; pre [ i ] = tmp ? di [ tmp \- 1 ] : -1 ; d [ tmp ] = a [ i ]; di [ tmp ] = i ; if ( tmp == ans ) ++ ans ; } // Construct the subsequence. for ( int k = ans , i = di [ ans \- 1 ]; k ; \-- k ) { res [ k ] = a [ i ]; i = pre [ i ]; } return ans ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` |  ```text n = 0 a = [ 0 ] * MAXN d = [ 0 ] * MAXN di = [ 0 ] * MAXN pre = [ 0 ] * MAXN res = [ 0 ] * MAXN def dp (): ans = 0 for i in range ( 1 , n \+ 1 ): tmp = bisect . bisect_right ( d , a [ i ], 0 , ans ) pre [ i ] = di [ tmp \- 1 ] if tmp else \- 1 d [ tmp ] = a [ i ] di [ tmp ] = i if tmp == ans : ans += 1 # Construct the subsequence k = ans i = di [ ans \- 1 ] while k : res [ k ] = a [ i ] i = pre [ i ] k -= 1 return ans ```   
---|---  
  
该算法的时间复杂度为 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．输出答案的时间复杂度为 𝑂(𝑎𝑛𝑠)O(ans)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注意

对于最长 **上升** 子序列问题，类似地，可以令 𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示所有长度为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最长上升子序列的末尾元素的最小值．

需要注意的是，在步骤 2 中，若 𝑎𝑖 ≤𝑑𝑙𝑒𝑛ai≤dlen![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由于最长上升子序列中相邻元素不能相等，需要在 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 序列中找到 **第一个** **不小于** 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素，用 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 替换之．

在实现上（以 C++ 为例），需要将 `upper_bound` 函数改为 `lower_bound`．

## 参考资料与注释

  * [最长不下降子序列 nlogn 算法详解 - lvmememe - 博客园](https://www.cnblogs.com/itlqs/p/5743114.html)

* * *

  1. [位运算求最长公共子序列 - -Wallace- - 博客园](https://www.cnblogs.com/-Wallace-/p/bit-lcs.html) ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/dp/basic.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/dp/basic.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Chrogeek](https://github.com/Chrogeek), [ChungZH](https://github.com/ChungZH), [ouuan](https://github.com/ouuan), [Xeonacid](https://github.com/Xeonacid), [hhc0001](https://github.com/hhc0001), [ksyx](https://github.com/ksyx), [Marcythm](https://github.com/Marcythm), [StudyingFather](https://github.com/StudyingFather), [tptpp](https://github.com/tptpp), [c-forrest](https://github.com/c-forrest), [cbw2007](https://github.com/cbw2007), [Enter-tainer](https://github.com/Enter-tainer), [greyqz](https://github.com/greyqz), [HeRaNO](https://github.com/HeRaNO), [hsfzLZH1](https://github.com/hsfzLZH1), [partychicken](https://github.com/partychicken), [Persdre](https://github.com/Persdre), [Tiphereth-A](https://github.com/Tiphereth-A), [xhn16729](mailto:xiong_haonan@163.com), [XiaoSuan250](https://github.com/XiaoSuan250), [xyf007](https://github.com/xyf007), [zhb2000](https://github.com/zhb2000), [caoji2001](https://github.com/caoji2001), [CBW2007](https://github.com/CBW2007), [dong628](https://github.com/dong628), [iamtwz](https://github.com/iamtwz), [LincolnYe](https://github.com/LincolnYe), [Menci](https://github.com/Menci), [NachtgeistW](https://github.com/NachtgeistW), [ree-chee](https://github.com/ree-chee), [shawlleyw](https://github.com/shawlleyw), [shuzhouliu](https://github.com/shuzhouliu), [Taoran-01](https://github.com/Taoran-01), [Taoran\\_01](https://github.com/Taoran\\_01), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [WAAutoMaton](https://github.com/WAAutoMaton), [xhn16729](https://github.com/xhn16729), [xiaoyezi2007](https://github.com/xiaoyezi2007), [yusancky](https://github.com/yusancky), [ZhangZhanhaoxiang](https://github.com/ZhangZhanhaoxiang), [zychen20](https://github.com/zychen20), [zzhx2006](https://github.com/zzhx2006)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
