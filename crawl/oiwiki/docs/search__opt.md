# 优化 - OI Wiki

- Source: https://oi-wiki.org/search/opt/

# 优化

## 前言

DFS（深度优先搜索）是一种常见的算法，大部分的题目都可以用 DFS 解决，但是大部分情况下，这都是骗分算法，很少会有爆搜为正解的题目．因为 DFS 的时间复杂度特别高．（没学过 DFS 的请自行补上这一课）

既然不能成为正解，那就多骗一点分吧．那么这一篇文章将介绍一些实用的优化算法（俗称「剪枝」）．

先来一段深搜模板，之后的模板将在此基础上进行修改．

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text int ans = 最坏情况 , now ; // now 为当前答案 void dfs ( 传入数值 ) { if ( 到达目的地 ) ans = 从当前解与已有解中选最优 ; for ( 遍历所有可能性 ) if ( 可行 ) { 进行操作 ; dfs ( 缩小规模 ); 撤回操作 ; } } ```   
---|---  
  
其中的 ans 可以是解的记录，那么从当前解与已有解中选最优就变成了输出解．

## 剪枝方法

最常用的剪枝有三种，记忆化搜索、最优性剪枝、可行性剪枝．

### 记忆化搜索

因为在搜索中，相同的传入值往往会带来相同的解，那我们就可以用数组来记忆，详见 [记忆化搜索](../../dp/memo/)．

**模板：**

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` |  ```text int g [ MAXN ]; // 定义记忆化数组 int ans = 最坏情况 , now ; void dfs f ( 传入数值 ) { if ( g [ 规模 ] != 无效数值 ) return ; // 或记录解，视情况而定 if ( 到达目的地 ) ans = 从当前解与已有解中选最优 ; // 输出解，视情况而定 for ( 遍历所有可能性 ) if ( 可行 ) { 进行操作 ; dfs ( 缩小规模 ); 撤回操作 ; } } int main () { // ... memset ( g , 无效数值 , sizeof ( g )); // 初始化记忆化数组 // ... } ```   
---|---  
  
### 最优性剪枝

在搜索中导致运行慢的原因还有一种，就是在当前解已经比已有解差时仍然在搜索，那么我们只需要判断一下当前解是否已经差于已有解．

**模板：**

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text int ans = 最坏情况 , now ; void dfs ( 传入数值 ) { if ( now比ans的答案还要差 ) return ; if ( 到达目的地 ) ans = 从当前解与已有解中选最优 ; for ( 遍历所有可能性 ) if ( 可行 ) { 进行操作 ; dfs ( 缩小规模 ); 撤回操作 ; } } ```   
---|---  
  
### 可行性剪枝

在搜索过程中当前解已经不可用了还继续搜索下去也是运行慢的原因．

**模板：**

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text int ans = 最坏情况 , now ; void dfs ( 传入数值 ) { if ( 当前解已不可用 ) return ; if ( 到达目的地 ) ans = 从当前解与已有解中选最优 ; for ( 遍历所有可能性 ) if ( 可行 ) { 进行操作 ; dfs ( 缩小规模 ); 撤回操作 ; } } ```   
---|---  
  
## 剪枝思路

剪枝思路有很多种，大多需要对于具体问题来分析，在此简要介绍几种常见的剪枝思路．

  * 极端法：考虑极端情况，如果最极端（最理想）的情况都无法满足，那么肯定实际情况搜出来的结果不会更优了．

  * 调整法：通过对子树的比较剪掉重复子树和明显不是最有「前途」的子树．

  * 数学方法：比如在图论中借助连通分量，数论中借助模方程的分析，借助不等式的放缩来估计下界等等．

## 例题

工作分配问题

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（1 ≤𝑛 ≤151≤n≤15![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）份工作要分配给 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人来完成，每个人完成一份．第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人完成第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 份工作所用的时间为一个正整数 𝑡𝑖,𝑘ti,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（1 ≤𝑡𝑖,𝑘 ≤1041≤ti,k≤104![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），其中 1 ≤𝑖,𝑘 ≤𝑛1≤i,k≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．试确定一个分配方案，使得完成这 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 份工作的时间总和最小．

由于每个人都必须分配到工作，在这里可以建一个二维数组 `time[i][j]`，用以表示 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人完成 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号工作所花费的时间．给定一个循环，从第 1 个人开始循环分配工作，直到所有人都分配到．为第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人分配工作时，再循环检查每个工作是否已被分配，没有则分配给 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人，否则检查下一个工作．可以用一个一维数组 `is_working[j]` 来表示第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号工作是否已被分配，未分配则 `is_working[j]=0`，否则 `is_working[j]=1`．利用回溯思想，在工人循环结束后回到上一工人，取消此次分配的工作，而去分配下一工作直到可以分配为止．这样，一直回溯到第 1 个工人后，就能得到所有的可行解．

检查工作分配，其实就是判断取得可行解时的二维数组的第一维下标各不相同并且第二维下标各不相同．而我们是要得到完成这 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 份工作的最小时间总和，即可行解中时间总和最小的一个，故需要再定义一个全局变量 `cost_time_total_min` 表示目前找到的解中最小的时间总和，初始 `cost_time_total_min` 为 `time[i][i]` 之和，即对角线工作时间相加之和．在所有人分配完工作时，比较 `count` 与 `cost_time_total_min` 的大小，如果 `count` 小于 `cost_time_total_min`，说明找到了一个最优解，此时就把 `count` 赋给 `cost_time_total_min`．

但考虑到算法的效率，这里还有一个剪枝优化的工作可以做．就是在每次计算局部费用变量 `count` 的值时，如果判断 `count` 已经大于 `cost_time_total_min`，就没必要再往下分配了，因为这时得到的解必然不是最优解．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 ``` |  ```text #include <iostream> constexpr int N = 16 ; int is_working [ N ] = { 0 }; // 某项工作是否被分配 int tm [ N ][ N ]; // 完成某项工作所需的时间 int cost_time_total_min ; // 完成 n 份工作的最小时间总和 // i 表示第几个人，count 表示工作费用总和 void work ( int i , int count , int n ) { // 如果 i 超出了所能分配的最大工作件数，表示分配完成，并且 count 比原来 // cost_time_total_min 花费少，则更新 cost_time_total_min 的值 if ( i > n && count < cost_time_total_min ) { cost_time_total_min = count ; return ; } // 回溯思想 if ( count < cost_time_total_min ) { // j 表示第几件工作 for ( int j = 1 ; j <= n ; j ++ ) { // 如果工作未被分配 is_working = 0 if ( is_working [ j ] == 0 ) { // 分配工作 is_working = 1 is_working [ j ] = 1 ; // 工作交给第 i + 1 个人 work ( i \+ 1 , count \+ tm [ i ][ j ], n ); // 在一轮迭代完成之后，返回到上一个人，要对此次的工作进行重新分配 // 将 is_working[j] 重设为 0 is_working [ j ] = 0 ; } } } } using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int n ; cin >> n ; for ( int i = 1 ; i <= n ; i ++ ) { for ( int j = 1 ; j <= n ; j ++ ) { cin >> tm [ i ][ j ]; } cost_time_total_min += tm [ i ][ i ]; } work ( 1 , 0 , n ); cout << cost_time_total_min << '\n' ; return 0 ; } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/search/opt.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/search/opt.md "edit.link.title")  
>  __本页面贡献者：[AngelKitty](https://github.com/AngelKitty), [Ir1d](https://github.com/Ir1d), [ouuan](mailto:1609483441@qq.com), [StudyingFather](https://github.com/StudyingFather), [H-J-Granger](https://github.com/H-J-Granger), [sshwy](https://github.com/sshwy), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [cbw2007](https://github.com/cbw2007), [CCXXXI](https://github.com/CCXXXI), [ChungZH](https://github.com/ChungZH), [Enter-tainer](https://github.com/Enter-tainer), [ksyx](https://github.com/ksyx), [mgt](mailto:i@margatroid.xyz), [abc1763613206](https://github.com/abc1763613206), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [minghu6](https://github.com/minghu6), [ouuan](https://github.com/ouuan), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [c-forrest](https://github.com/c-forrest), [CBW2007](https://github.com/CBW2007), [Chrogeek](https://github.com/Chrogeek), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [HeRaNO](https://github.com/HeRaNO), [kenlig](https://github.com/kenlig), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Marcythm](https://github.com/Marcythm), [Peanut-Tang](https://github.com/Peanut-Tang), [SukkaW](https://github.com/SukkaW), [Tiphereth-A](https://github.com/Tiphereth-A), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
