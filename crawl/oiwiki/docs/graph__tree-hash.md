# 树哈希 - OI Wiki

- Source: https://oi-wiki.org/graph/tree-hash/

# 树哈希

判断一些树是否同构的时，我们常常把这些树转成哈希值储存起来，以降低复杂度．

树哈希是很灵活的，可以设计出各种各样的哈希方式；但是如果随意设计，很有可能是错误的，可能被卡．以下介绍一类容易实现且不易被卡的方法．

## 方法

这类方法需要一个多重集的哈希函数．以某个结点为根的子树的哈希值，就是以它的所有儿子为根的子树的哈希值构成的多重集的哈希值，即：

ℎ𝑥=𝑓({ℎ𝑖∣𝑖∈𝑠𝑜𝑛(𝑥)})hx=f({hi∣i∈son(x)})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 ℎ𝑥hx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示以 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树的哈希值，𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是多重集的哈希函数．

以代码中使用的哈希函数为例：

𝑓(𝑆)=(𝑐+∑𝑥∈𝑆𝑔(𝑥))mod𝑚f(S)=(c+∑x∈Sg(x))modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为常数，一般使用 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为模数，一般使用 232232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 264264![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行自然溢出，也可使用大素数．𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为整数到整数的映射，代码中使用 xor shift，也可以选用其他的函数，但是不建议使用多项式．为了预防出题人对着 xor hash 卡，还可以在映射前后异或一个随机常数．

这种哈希十分好写．如果需要换根，第二次 DP 时只需把子树哈希减掉即可．

## 例题

### [UOJ #763. 树哈希](https://uoj.ac/problem/763)

这是一道模板题．不用多说，以 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根跑一遍 DFS 就好了．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 ``` |  ```text #include <cctype> #include <iostream> #include <random> #include <set> #include <vector> using ull = unsigned long long ; const ull mask = std :: mt19937_64 ( time ( nullptr ))(); ull shift ( ull x ) { x ^= mask ; x ^= x << 13 ; x ^= x >> 7 ; x ^= x << 17 ; x ^= mask ; return x ; } constexpr int N = 1e6 \+ 10 ; int n ; ull hash [ N ]; std :: vector < int > edge [ N ]; std :: set < ull > trees ; void getHash ( int x , int p ) { hash [ x ] = 1 ; for ( int i : edge [ x ]) { if ( i == p ) { continue ; } getHash ( i , x ); hash [ x ] += shift ( hash [ i ]); } trees . insert ( hash [ x ]); } using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n ; for ( int i = 1 ; i < n ; i ++ ) { int u , v ; cin >> u >> v ; edge [ u ]. push_back ( v ); edge [ v ]. push_back ( u ); } getHash ( 1 , 0 ); cout << trees . size (); } ```   
---|---  
  
### [[BJOI2015] 树的同构](https://www.luogu.com.cn/problem/P5043)

这道题所说的同构是指无根树的，而上面所介绍的方法是针对有根树的．因此只有当根一样时，同构的两棵无根树哈希值才相同．由于数据范围较小，我们可以暴力求出以每个点为根时的哈希值，排序后比较．

如果数据范围较大，我们也可以使用换根 DP，遍历树两遍，求出以每个点为根时的哈希值．我们还可以利用上面的多重集哈希函数：把以每个结点为根时的哈希值都存进多重集，再把多重集的哈希值算出来，进行比较（做法一）．

还可以通过找重心的方式来优化复杂度．一棵树的重心最多只有两个，只需把以它（们）为根时的哈希值求出来即可．接下来，既可以分别比较这些哈希值（做法二），也可以在有一个重心时取它的哈希值作为整棵树的哈希值，有两个时则取其中较小（大）的．

做法一

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 ``` |  ```text #include <iostream> #include <map> #include <random> #include <vector> using ull = unsigned long long ; constexpr int N = 60 , M = 998244353 ; const ull mask = std :: mt19937_64 ( time ( nullptr ))(); ull shift ( ull x ) { x ^= mask ; x ^= x << 13 ; x ^= x >> 7 ; x ^= x << 17 ; x ^= mask ; return x ; } std :: vector < int > edge [ N ]; ull sub [ N ], root [ N ]; std :: map < ull , int > trees ; void getSub ( int x ) { sub [ x ] = 1 ; for ( int i : edge [ x ]) { getSub ( i ); sub [ x ] += shift ( sub [ i ]); } } void getRoot ( int x ) { for ( int i : edge [ x ]) { root [ i ] = sub [ i ] \+ shift ( root [ x ] \- shift ( sub [ i ])); getRoot ( i ); } } using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int m ; cin >> m ; for ( int t = 1 ; t <= m ; t ++ ) { int n , rt = 0 ; cin >> n ; for ( int i = 1 ; i <= n ; i ++ ) { int fa ; cin >> fa ; if ( fa ) { edge [ fa ]. push_back ( i ); } else { rt = i ; } } getSub ( rt ); root [ rt ] = sub [ rt ]; getRoot ( rt ); ull hash = 1 ; for ( int i = 1 ; i <= n ; i ++ ) { hash += shift ( root [ i ]); } if ( ! trees . count ( hash )) { trees [ hash ] = t ; } cout << trees [ hash ] << '\n' ; for ( int i = 1 ; i <= n ; i ++ ) { edge [ i ]. clear (); } } } ```   
---|---  
  
做法二

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 ``` |  ```text #include <iostream> #include <map> #include <random> #include <vector> using ull = unsigned long long ; using Hash2 = std :: pair < ull , ull > ; constexpr int N = 60 , M = 998244353 ; const ull mask = std :: mt19937_64 ( time ( nullptr ))(); ull shift ( ull x ) { x ^= mask ; x ^= x << 13 ; x ^= x >> 7 ; x ^= x << 17 ; x ^= mask ; return x ; } int n ; int size [ N ], weight [ N ], centroid [ 2 ]; std :: vector < int > edge [ N ]; std :: map < Hash2 , int > trees ; void getCentroid ( int x , int fa ) { size [ x ] = 1 ; weight [ x ] = 0 ; for ( int i : edge [ x ]) { if ( i == fa ) { continue ; } getCentroid ( i , x ); size [ x ] += size [ i ]; weight [ x ] = std :: max ( weight [ x ], size [ i ]); } weight [ x ] = std :: max ( weight [ x ], n \- size [ x ]); if ( weight [ x ] <= n / 2 ) { int index = centroid [ 0 ] != 0 ; centroid [ index ] = x ; } } ull getHash ( int x , int fa ) { ull hash = 1 ; for ( int i : edge [ x ]) { if ( i == fa ) { continue ; } hash += shift ( getHash ( i , x )); } return hash ; } using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int m ; cin >> m ; for ( int t = 1 ; t <= m ; t ++ ) { cin >> n ; for ( int i = 1 ; i <= n ; i ++ ) { int fa ; cin >> fa ; if ( fa ) { edge [ fa ]. push_back ( i ); edge [ i ]. push_back ( fa ); } } getCentroid ( 1 , 0 ); Hash2 hash ; hash . first = getHash ( centroid [ 0 ], 0 ); if ( centroid [ 1 ]) { hash . second = getHash ( centroid [ 1 ], 0 ); if ( hash . first > hash . second ) { std :: swap ( hash . first , hash . second ); } } else { hash . second = hash . first ; } if ( ! trees . count ( hash )) { trees [ hash ] = t ; } cout << trees [ hash ] << '\n' ; for ( int i = 1 ; i <= n ; i ++ ) { edge [ i ]. clear (); } centroid [ 0 ] = centroid [ 1 ] = 0 ; } } ```   
---|---  
  
### [HDU 6647 Bracket Sequences on Tree](https://acm.hdu.edu.cn/showproblem.php?pid=6647)

题目要求遍历一棵无根树产生的本质不同括号序列方案数．

首先可以注意到，两棵不同构的有根树一定不会生成相同的括号序列．我们先考虑遍历有根树能够产生的本质不同括号序列方案数，假设我们当前考虑的子树根节点为 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，记 𝑓(𝑢)f(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示这棵子树的方案数，从 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始往下遍历，顺序可以随意选择，产生 |𝑠𝑜𝑛(𝑢)|!|son(u)|!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种排列，遍历每个儿子节点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子树内有 𝑓(𝑣)f(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种方案，因此有 𝑓(𝑢) =|𝑠𝑜𝑛(𝑢)|! ⋅∏𝑣∈𝑠𝑜𝑛(𝑢)𝑓(𝑣)f(u)=|son(u)|!⋅∏v∈son(u)f(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，同构的子树之间会产生重复，𝑓(𝑢)f(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要除掉每种本质不同子树出现次数阶乘的乘积，类似于多重集合的排列．

通过上述 DP，可以求出根节点的方案数．再通过换根 DP，将父亲节点的哈希值和方案信息转移给儿子，可以求出以每个节点为根时的哈希值和方案数．每种不同的子树只需要计数一次即可．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 ``` |  ```text #include <iostream> #include <map> #include <random> #include <vector> using ull = unsigned long long ; constexpr int N = 1e5 \+ 10 , M = 998244353 ; const ull mask = std :: mt19937_64 ( time ( nullptr ))(); struct Tree { ull hash , deg , ans ; std :: map < ull , ull > son ; Tree () { clear (); } void add ( Tree & o ); void remove ( Tree & o ); void clear (); }; ull inv ( ull x ) { ull y = M \- 2 , z = 1 ; while ( y ) { if ( y & 1 ) { z = z * x % M ; } x = x * x % M ; y >>= 1 ; } return z ; } ull shift ( ull x ) { x ^= mask ; x ^= x << 13 ; x ^= x >> 7 ; x ^= x << 17 ; x ^= mask ; return x ; } void Tree::add ( Tree & o ) { ull temp = shift ( o . hash ); hash += temp ; ans = ans * ++ deg % M * inv ( ++ son [ temp ]) % M * o . ans % M ; } void Tree::remove ( Tree & o ) { ull temp = shift ( o . hash ); hash -= temp ; ans = ans * inv ( deg \-- ) % M * son [ temp ] \-- % M * inv ( o . ans ) % M ; } void Tree::clear () { hash = 1 ; deg = 0 ; ans = 1 ; son . clear (); } std :: vector < int > edge [ N ]; Tree sub [ N ], root [ N ]; std :: map < ull , ull > trees ; void getSub ( int x , int fa ) { for ( int i : edge [ x ]) { if ( i == fa ) { continue ; } getSub ( i , x ); sub [ x ]. add ( sub [ i ]); } } void getRoot ( int x , int fa ) { for ( int i : edge [ x ]) { if ( i == fa ) { continue ; } root [ x ]. remove ( sub [ i ]); root [ i ] = sub [ i ]; root [ i ]. add ( root [ x ]); root [ x ]. add ( sub [ i ]); getRoot ( i , x ); } trees [ root [ x ]. hash ] = root [ x ]. ans ; } using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int t , n ; cin >> t ; while ( t \-- ) { cin >> n ; for ( int i = 1 ; i < n ; i ++ ) { int u , v ; cin >> u >> v ; edge [ u ]. push_back ( v ); edge [ v ]. push_back ( u ); } getSub ( 1 , 0 ); root [ 1 ] = sub [ 1 ]; getRoot ( 1 , 0 ); ull tot = 0 ; for ( auto p : trees ) { tot = ( tot \+ p . second ) % M ; } cout << tot << '\n' ; for ( int i = 1 ; i <= n ; i ++ ) { edge [ i ]. clear (); sub [ i ]. clear (); root [ i ]. clear (); } trees . clear (); } } ```   
---|---  
  
## 参考资料

文中的哈希方法参考并拓展自博客 [一种好写且卡不掉的树哈希](https://peehs-moorhsum.blog.uoj.ac/blog/7891)．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/tree-hash.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/tree-hash.md "edit.link.title")  
>  __本页面贡献者：[yjl9903](https://github.com/yjl9903), [H-J-Granger](https://github.com/H-J-Granger), [jifbt](https://github.com/jifbt), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [Henry-ZHR](https://github.com/Henry-ZHR), [Marcythm](https://github.com/Marcythm), [c-forrest](https://github.com/c-forrest), [Chrogeek](https://github.com/Chrogeek), [kenlig](https://github.com/kenlig), [mcendu](https://github.com/mcendu), [Menci](https://github.com/Menci), [partychicken](https://github.com/partychicken), [platelett](https://github.com/platelett), [StudyingFather](https://github.com/StudyingFather)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
