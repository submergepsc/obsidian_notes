# 倍增 - OI Wiki

- Source: https://oi-wiki.org/basic/binary-lifting/

# 倍增

本页面将简要介绍倍增法．

## 定义

倍增法（英语：binary lifting），顾名思义就是「成倍增长」．我们在进行递推时，如果状态空间很大，通常的线性递推无法满足时间与空间复杂度的要求，那么我们可以通过成倍增长的方式，只递推状态空间中在 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数次幂位置上的值作为代表．当需要其他位置上的值时，我们通过「任意整数可以表示成若干个 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的次幂项的和」这一性质，使用之前求出的代表值拼成所需的值．所以使用倍增算法也要求我们递推的问题的状态空间关于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的次幂具有可划分性．通常情况下 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．1

这个方法在很多算法中均有应用，其中最常用的是 RMQ 问题和求 [LCA（最近公共祖先）](../../graph/lca/)．

## 应用

### RMQ 问题

参见：[RMQ 专题](../../topic/rmq/)

RMQ 是 Range Maximum/Minimum Query 的缩写，表示区间最大（最小）值．使用倍增思想解决 RMQ 问题的方法是 [ST 表](../../ds/sparse-table/)．

### 树上倍增求 LCA

参见：[最近公共祖先](../../graph/lca/)

## 例题

### 题 1

例题

如何用尽可能少的砝码称量出 [0,31][0,31]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的所有重量？（只能在天平的一端放砝码）

解题思路

答案是使用 1 2 4 8 16 这五个砝码，可以称量出 [0,31][0,31]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的所有重量．同样，如果要称量 [0,127][0,127]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的所有重量，可以使用 1 2 4 8 16 32 64 这七个砝码．每次我们都选择 2 的整次幂作砝码的重量，就可以使用极少的砝码个数量出任意我们所需要的重量．

为什么说是极少呢？因为如果我们要量出 [0,1023][0,1023]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的所有重量，只需要 10 个砝码，需要量出 [0,1048575][0,1048575]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的所有重量，只需要 20 个．如果我们的目标重量翻倍，砝码个数只需要增加 1．这叫「对数级」的增长速度，因为砝码的所需个数与目标重量的范围的对数成正比．

### 题 2

例题

给出一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的环和一个常数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每次会从第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点跳到第 (𝑖 +𝑘)mod𝑛 +1(i+k)modn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点，总共跳了 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．每个点都有一个权值，记为 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次跳跃的起点的权值之和对 109 +7109+7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模的结果．

数据范围：1 ≤𝑛 ≤1061≤n≤106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，1 ≤𝑚 ≤10181≤m≤1018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，1 ≤𝑘 ≤𝑛1≤k≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，0 ≤𝑎𝑖 ≤1090≤ai≤109![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解题思路

这里显然不能暴力模拟跳 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．因为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最大可到 10181018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别，如果暴力模拟的话，时间承受不住．

所以就需要进行一些预处理，提前整合一些信息，以便于在查询的时候更快得出结果．如果记录下来每一个可能的跳跃次数的结果的话，不论是时间还是空间都难以承受．

那么应该如何预处理呢？看看第一道例题．有思路了吗？

回到本题．我们要预处理一些信息，然后用预处理的信息尽量快的整合出答案．同时预处理的信息也不能太多．所以可以预处理出以 2 的整次幂为单位的信息，这样的话在预处理的时候只需要处理少量信息，在整合的时候也不需要大费周章．

在这题上，就是我们预处理出从每个点开始跳 1、2、4、8 等等步之后的结果（所处点和点权和），然后如果要跳 13 步，只需要跳 1+4+8 步就好了．也就是说先在起始点跳 1 步，然后再在跳了之后的终点跳 4 步，再接着跳 8 步，同时统计一下预先处理好的点权和，就可以知道跳 13 步的点权和了．

对于每一个点开始的 2𝑖2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步，记录一个 `go[i][x]` 表示第 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点跳 2𝑖2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步之后的终点，而 `sum[i][x]` 表示第 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点跳 2𝑖2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步之后能获得的点权和．预处理的时候，开两重循环，对于跳 2𝑖2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步的信息，我们可以看作是先跳了 2𝑖−12i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步，再跳 2𝑖−12i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步，因为显然有 2𝑖−1 +2𝑖−1 =2𝑖2i−1+2i−1=2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．即我们有 `sum[i][x] = sum[i-1][x]+sum[i-1][go[i-1][x]]`，且 `go[i][x] = go[i-1][go[i-1][x]]`．

当然还有一些实现细节需要注意．为了保证统计的时候不重不漏，我们一般预处理出「左闭右开」的点权和．亦即，对于跳 1 步的情况，我们只记录该点的点权和；对于跳 2 步的情况，我们只记录该点及其下一个点的点权和．相当于总是不将终点的点权和计入 sum．这样在预处理的时候，只需要将两部分的点权和直接相加就可以了，不需要担心第一段的终点和第二段的起点会被重复计算．

这题的 𝑚 ≤1018m≤1018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，虽然看似恐怖，但是实际上只需要预处理出 6565![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以内的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以轻松解决，比起暴力枚举快了很多．用行话讲，这个做法的 [时间复杂度](../complexity/) 是预处理 Θ(𝑛log⁡𝑚)Θ(nlog⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，查询每次 Θ(log⁡𝑚)Θ(log⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 ``` |  ```text #include <cstdio> using namespace std ; constexpr int mod = 1000000007 ; int modadd ( int a , int b ) { if ( a \+ b >= mod ) return a \+ b \- mod ; // 减法代替取模，加快运算 return a \+ b ; } int vi [ 1000005 ]; int go [ 75 ][ 1000005 ]; // 将数组稍微开大以避免越界，小的一维尽量定义在前面 int sum [ 75 ][ 1000005 ]; int main () { int n , k ; scanf ( "%d%d" , & n , & k ); for ( int i = 1 ; i <= n ; ++ i ) { scanf ( "%d" , vi \+ i ); } for ( int i = 1 ; i <= n ; ++ i ) { go [ 0 ][ i ] = ( i \+ k ) % n \+ 1 ; sum [ 0 ][ i ] = vi [ i ]; } int logn = 31 \- __builtin_clz ( n ); // 一个快捷的取对数的方法 for ( int i = 1 ; i <= logn ; ++ i ) { for ( int j = 1 ; j <= n ; ++ j ) { go [ i ][ j ] = go [ i \- 1 ][ go [ i \- 1 ][ j ]]; sum [ i ][ j ] = modadd ( sum [ i \- 1 ][ j ], sum [ i \- 1 ][ go [ i \- 1 ][ j ]]); } } long long m ; scanf ( "%lld" , & m ); int ans = 0 ; int curx = 1 ; for ( int i = 0 ; m ; ++ i ) { if ( m & ( 1l l << i )) { // 参见位运算的相关内容，意为 m 的第 i 位是否为 1 ans = modadd ( ans , sum [ i ][ curx ]); curx = go [ i ][ curx ]; m ^= 1l l << i ; // 将第 i 位置零 } } printf ( "%d \n " , ans ); } ```   
---|---  
  
* * *

  1. 引用自李煜东《算法竞赛进阶指南》0x06. 倍增一节 ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/basic/binary-lifting.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/basic/binary-lifting.md "edit.link.title")  
>  __本页面贡献者：[orzAtalod](https://github.com/orzAtalod), [ouuan](mailto:1609483441@qq.com), [Ir1d](https://github.com/Ir1d), [H-J-Granger](https://github.com/H-J-Granger), [NachtgeistW](https://github.com/NachtgeistW), [StudyingFather](https://github.com/StudyingFather), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [CCXXXI](https://github.com/CCXXXI), [sshwy](https://github.com/sshwy), [AngelKitty](https://github.com/AngelKitty), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [Marcythm](https://github.com/Marcythm), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [Tiphereth-A](https://github.com/Tiphereth-A), [weiyong1024](https://github.com/weiyong1024), [Backl1ght](https://github.com/Backl1ght), [Chrogeek](https://github.com/Chrogeek), [Fomalhauthmj](https://github.com/Fomalhauthmj), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Great-designer](https://github.com/Great-designer), [HeRaNO](https://github.com/HeRaNO), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [kxccc](https://github.com/kxccc), [leoleoasd](https://github.com/leoleoasd), [Lewy Zeng](mailto:zengxingchen@csu.edu.cn), [lychees](https://github.com/lychees), [MingqiHuang](https://github.com/MingqiHuang), [opsiff](https://github.com/opsiff), [Peanut-Tang](https://github.com/Peanut-Tang), [PeterlitsZo](https://github.com/PeterlitsZo), [ShadowsEpic](https://github.com/ShadowsEpic), [siger-young](https://github.com/siger-young), [SukkaW](https://github.com/SukkaW), [Xeonacid](https://github.com/Xeonacid), [yu-qe](https://github.com/yu-qe)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
