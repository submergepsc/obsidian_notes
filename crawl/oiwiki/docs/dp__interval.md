# 区间 DP - OI Wiki

- Source: https://oi-wiki.org/dp/interval/

# 区间 DP

## 定义

区间类动态规划是线性动态规划的扩展，它在分阶段地划分问题时，与阶段中元素出现的顺序和由前一阶段的哪些元素合并而来有很大的关系．

令状态 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示将下标位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有元素合并能获得的价值的最大值，那么 𝑓(𝑖,𝑗) =max{𝑓(𝑖,𝑘) +𝑓(𝑘 +1,𝑗) +𝑐𝑜𝑠𝑡}f(i,j)=max{f(i,k)+f(k+1,j)+cost}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑐𝑜𝑠𝑡cost![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为将这两组元素合并起来的价值．

## 性质

区间 DP 有以下特点：

**合并** ：即将两个或多个部分进行整合，当然也可以反过来；

**特征** ：能将问题分解为能两两合并的形式；

**求解** ：对整个问题设最优值，枚举合并点，将问题分解为左右两个部分，最后合并两个部分的最优值得到原问题的最优值．

## 解释

### 例题

[「NOI1995」石子合并](https://loj.ac/problem/10147)

题目大意：在一个环上有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进行 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次合并操作，每次操作将相邻的两堆合并成一堆，能获得新的一堆中的石子数量的和的得分．你需要最大化你的得分．

需要考虑不在环上，而在一条链上的情况．

令 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示将区间 [𝑖,𝑗][i,j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的所有石子合并到一起的最大得分．

写出 **状态转移方程** ：𝑓(𝑖,𝑗) =max{𝑓(𝑖,𝑘) +𝑓(𝑘 +1,𝑗) +∑𝑗𝑡=𝑖𝑎𝑡} (𝑖 ≤𝑘 <𝑗)f(i,j)=max{f(i,k)+f(k+1,j)+∑t=ijat} (i≤k<j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令 𝑠𝑢𝑚𝑖sumi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组的前缀和，状态转移方程变形为 𝑓(𝑖,𝑗) =max{𝑓(𝑖,𝑘) +𝑓(𝑘 +1,𝑗) +𝑠𝑢𝑚𝑗 −𝑠𝑢𝑚𝑖−1}f(i,j)=max{f(i,k)+f(k+1,j)+sumj−sumi−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 怎样进行状态转移

由于计算 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值时需要知道所有 𝑓(𝑖,𝑘)f(i,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓(𝑘 +1,𝑗)f(k+1,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，而这两个中包含的元素的数量都小于 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以我们以 𝑙𝑒𝑛 =𝑗 −𝑖 +1len=j−i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为 DP 的阶段．首先从小到大枚举 𝑙𝑒𝑛len![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后枚举 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，根据 𝑙𝑒𝑛len![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 用公式计算出 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，然后枚举 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，时间复杂度为 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 怎样处理环

题目中石子围成一个环，而不是一条链，怎么办呢？

**方法一** ：由于石子围成一个环，我们可以枚举分开的位置，将这个环转化成一个链，由于要枚举 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，最终的时间复杂度为 𝑂(𝑛4)O(n4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**方法二** ：我们将这条链延长两倍，变成 2 ×𝑛2×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆，其中第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆与第 𝑛 +𝑖n+i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆相同，用动态规划求解后，取 𝑓(1,𝑛),𝑓(2,𝑛 +1),…,𝑓(𝑛,2𝑛 −1)f(1,n),f(2,n+1),…,f(n,2n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的最优值，即为最后的答案．时间复杂度 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 实现

C++Python

```text 1 2 3 4 5 6 ``` |  ```text for ( len = 2 ; len <= n ; len ++ ) for ( i = 1 ; i <= 2 * n \- len ; i ++ ) { int j = len \+ i \- 1 ; for ( k = i ; k < j ; k ++ ) f [ i ][ j ] = max ( f [ i ][ j ], f [ i ][ k ] \+ f [ k \+ 1 ][ j ] \+ sum [ j ] \- sum [ i \- 1 ]); } ```   
---|---  
  
```text 1 2 3 4 5 ``` |  ```text for len in range ( 2 , n \+ 1 ): for i in range ( 1 , 2 * n \- len \+ 1 ): j = len \+ i \- 1 for k in range ( i , j ): f [ i ][ j ] = max ( f [ i ][ j ], f [ i ][ k ] \+ f [ k \+ 1 ][ j ] \+ sum [ j ] \- sum [ i \- 1 ]) ```   
---|---  
  
## 几道练习题

[NOIP 2006 能量项链](https://www.luogu.com.cn/problem/P1063)

[NOIP 2007 矩阵取数游戏](https://www.luogu.com.cn/problem/P1005)

[「IOI2000」邮局](https://www.luogu.com.cn/problem/P4767)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/dp/interval.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/dp/interval.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Henry-ZHR](https://github.com/Henry-ZHR), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [ouuan](https://github.com/ouuan), [Xeonacid](https://github.com/Xeonacid), [AFObject](https://github.com/AFObject), [billchenchina](https://github.com/billchenchina), [Chlero](https://github.com/Chlero), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [fyulingi](https://github.com/fyulingi), [greyqz](https://github.com/greyqz), [HeRaNO](https://github.com/HeRaNO), [ImpleLee](https://github.com/ImpleLee), [isdanni](https://github.com/isdanni), [ksyx](https://github.com/ksyx), [Menci](https://github.com/Menci), [OYoooooo](https://github.com/OYoooooo), [partychicken](https://github.com/partychicken), [shawlleyw](https://github.com/shawlleyw), [shenshuaijie](https://github.com/shenshuaijie), [StudyingFather](https://github.com/StudyingFather), [thredreams](https://github.com/thredreams), [Tiphereth-A](https://github.com/Tiphereth-A), [Wang Hongtian](mailto:redefinition0726@163.com)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
