# DFS（搜索） - OI Wiki

- Source: https://oi-wiki.org/search/dfs/

# DFS（搜索）

## 引入

DFS 为图论中的概念，详见 [DFS（图论）](../../graph/dfs/) 页面．在 **搜索算法** 中，该词常常指利用递归函数方便地实现暴力枚举的算法，与图论中的 DFS 算法有一定相似之处，但并不完全相同．

## 解释

考虑这个例子：

例题

把正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解为 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个正整数，如 6 =1 +2 +36=1+2+3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，排在后面的数必须大于等于前面的数，输出所有方案．

对于这个问题，如果不知道搜索，应该怎么办呢？当然是三重循环，参考代码如下：

实现

C++PythonJava

```text 1 2 3 4 ``` |  ```text for ( int i = 1 ; i <= n ; ++ i ) for ( int j = i ; j <= n ; ++ j ) for ( int k = j ; k <= n ; ++ k ) if ( i \+ j \+ k == n ) printf ( "%d = %d + %d + %d \n " , n , i , j , k ); ```   
---|---  
  
```text 1 2 3 4 5 ``` |  ```text for i in range ( 1 , n \+ 1 ): for j in range ( i , n \+ 1 ): for k in range ( j , n \+ 1 ): if i \+ j \+ k == n : print ( " %d = %d \+ %d \+ %d " % ( n , i , j , k )) ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text for ( int i = 1 ; i < n \+ 1 ; i ++ ) { for ( int j = i ; j < n \+ 1 ; j ++ ) { for ( int k = j ; k < n \+ 1 ; k ++ ) { if ( i \+ j \+ k == n ) System . out . printf ( "%d = %d + %d + %d%n" , n , i , j , k ); } } } ```   
---|---  
  
那如果是分解成四个整数呢？再加一重循环？那分解成小于等于 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数呢？

这时候就需要用到递归搜索了．该类搜索算法的特点在于，将要搜索的目标分成若干「层」，每层基于前几层的状态进行决策，直到达到目标状态．

考虑上述问题，即将正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解成不超过 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个正整数之和，且排在后面的数必须大于等于前面的数，并输出所有方案．

设一组方案将正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解成 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个正整数 𝑎1,𝑎2,…,𝑎𝑘a1,a2,…,ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的和．将问题分层，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层决定 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．则为了进行第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层决策，我们需要记录三个状态变量：𝑛 −∑𝑖𝑗=1𝑎𝑗n−∑j=1iaj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示后面所有正整数的和；𝑎𝑖−1ai−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示前一层的正整数，以确保正整数递增；以及 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，确保我们最多输出 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个正整数．为了记录方案，我们用 `arr` 数组，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项表示 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 注意到 `arr` 实际上是一个长度为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的栈．

代码如下：

实现

C++PythonJava

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text int m , arr [ 103 ]; // arr 用于记录方案 void dfs ( int n , int i , int a ) { if ( n == 0 ) { for ( int j = 1 ; j <= i \- 1 ; ++ j ) printf ( "%d " , arr [ j ]); printf ( " \n " ); } if ( i <= m ) { for ( int j = a ; j <= n ; ++ j ) { arr [ i ] = j ; dfs ( n \- j , i \+ 1 , j ); // 请仔细思考该行含义． } } } // 主函数 scanf ( "%d%d" , & n , & m ); dfs ( n , 1 , 1 ); ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text arr = [ 0 ] * 103 # arr 用于记录方案 def dfs ( n , i , a ): if n == 0 : print ( arr [ 1 : i ]) if i <= m : for j in range ( a , n \+ 1 ): arr [ i ] = j dfs ( n \- j , i \+ 1 , j ) # 请仔细思考该行含义． # 主函数 n , m = map ( int , input () . split ()) dfs ( n , 1 , 1 ) ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text static int m ; // arr 用于记录方案 static int [] arr = new int [ 103 ] ; public static void dfs ( int n , int i , int a ) { if ( n == 0 ) { for ( int j = 1 ; j <= i \- 1 ; j ++ ) System . out . printf ( "%d " , arr [ j ] ); System . out . println (); } if ( i <= m ) { for ( int j = a ; j <= n ; ++ j ) { arr [ i ] = j ; dfs ( n \- j , i \+ 1 , j ); // 请仔细思考该行含义． } } } // 主函数 final int N = new Scanner ( System . in ). nextInt (); m = new Scanner ( System . in ). nextInt (); dfs ( N , 1 , 1 ); ```   
---|---  
  
## 例题

[Luogu P1706 全排列问题](https://www.luogu.com.cn/problem/P1706)

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` |  ```text #include <iomanip> #include <iostream> using namespace std ; int n ; bool vis [ 50 ]; // 访问标记数组 int a [ 50 ]; // 排列数组，按顺序储存当前搜索结果 void dfs ( int step ) { if ( step == n \+ 1 ) { // 边界 for ( int i = 1 ; i <= n ; i ++ ) { cout << setw ( 5 ) << a [ i ]; // 保留5个场宽 } cout << endl ; return ; } for ( int i = 1 ; i <= n ; i ++ ) { if ( ! vis [ i ]) { // 判断数字i是否在正在进行的全排列中 vis [ i ] = true ; a [ step ] = i ; dfs ( step \+ 1 ); vis [ i ] = false ; // 这一步不使用该数 置0后允许下一步使用 } } return ; } int main () { cin >> n ; dfs ( 1 ); return 0 ; } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/search/dfs.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/search/dfs.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [H-J-Granger](https://github.com/H-J-Granger), [partychicken](https://github.com/partychicken), [StudyingFather](https://github.com/StudyingFather), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [ksyx](https://github.com/ksyx), [NachtgeistW](https://github.com/NachtgeistW), [iamtwz](https://github.com/iamtwz), [AngelKitty](https://github.com/AngelKitty), [Anyexyz](https://github.com/Anyexyz), [CCXXXI](https://github.com/CCXXXI), [ChungZH](https://github.com/ChungZH), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [greyqz](https://github.com/greyqz), [Henry-ZHR](https://github.com/Henry-ZHR), [Konano](https://github.com/Konano), [loader3229](https://github.com/loader3229), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [ouuan](mailto:1609483441@qq.com), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [Tiphereth-A](https://github.com/Tiphereth-A), [weiyong1024](https://github.com/weiyong1024), [Acfboy](https://github.com/Acfboy), [c-forrest](https://github.com/c-forrest), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [kenlig](https://github.com/kenlig), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Menci](https://github.com/Menci), [ouuan](https://github.com/ouuan), [Peanut-Tang](https://github.com/Peanut-Tang), [shawlleyw](https://github.com/shawlleyw), [SukkaW](https://github.com/SukkaW), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [vincent-163](https://github.com/vincent-163), [wysunrise2](https://github.com/wysunrise2), [Xeonacid](https://github.com/Xeonacid), [Yue-plus](https://github.com/Yue-plus), [zyouxam](https://github.com/zyouxam)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
