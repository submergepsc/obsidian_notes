# 可持久化字典树 - OI Wiki

- Source: https://oi-wiki.org/ds/persistent-trie/

# 可持久化字典树

## 引入

可持久化 Trie 的方式和可持久化线段树的方式是相似的，即每次只修改被添加或值被修改的节点，而保留没有被改动的节点，在上一个版本的基础上连边，使最后每个版本的 Trie 树的根遍历所能分离出的 Trie 树都是完整且包含全部信息的．

大部分的可持久化 Trie 题中，Trie 都是以 [01-Trie](../../string/trie/#维护异或极值) 的形式出现的．

例题 [最大异或和](https://www.luogu.com.cn/problem/P4735)

对一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数组 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维护以下操作：

  1. 在数组的末尾添加一个数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，数组的长度 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 自增 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 给出查询区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和一个值 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求当 𝑙 ≤𝑝 ≤𝑟l≤p≤r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝑘 ⊕⨁𝑛𝑖=𝑝𝑎𝑖k⊕⨁i=pnai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大值．

## 过程

这个求的值可能有些麻烦，利用常用的处理连续异或的方法，记 𝑠𝑥 =⨁𝑥𝑖=1𝑎𝑖sx=⨁i=1xai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则原式等价于 𝑠𝑝−1 ⊕𝑠𝑛 ⊕𝑘sp−1⊕sn⊕k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，观察到 𝑠𝑛 ⊕𝑘sn⊕k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在查询的过程中是固定的，题目的查询变化为查询在区间 [𝑙 −1,𝑟 −1][l−1,r−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中异或定值（𝑠𝑛 ⊕𝑘sn⊕k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）的最大值．

继续按类似于可持久化线段树的思路，考虑每次的查询都查询整个区间．我们只需把这个区间建一棵 Trie 树，将这个区间中的每个树都加入这棵 Trie 中，查询的时候，尽量往与当前位不相同的地方跳．

查询区间，只需要利用前缀和和差分的思想，用两棵前缀 Trie 树（也就是按顺序添加数的两个历史版本）相减即得到该区间的 Trie 树．再利用动态开点的思想，不添加没有计算过的点，以减少空间占用．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 ``` |  ```text #include <algorithm> #include <cstring> #include <iostream> using namespace std ; constexpr int MAXN = 600010 ; int n , q , a [ MAXN ], s [ MAXN ], l , r , x ; char op ; struct Trie { int cnt , rt [ MAXN ], ch [ MAXN * 33 ][ 2 ], val [ MAXN * 33 ]; void insert ( int o , int lst , int v ) { for ( int i = 28 ; i >= 0 ; i \-- ) { val [ o ] = val [ lst ] \+ 1 ; // 在原版本的基础上更新 if (( v & ( 1 << i )) == 0 ) { if ( ! ch [ o ][ 0 ]) ch [ o ][ 0 ] = ++ cnt ; ch [ o ][ 1 ] = ch [ lst ][ 1 ]; o = ch [ o ][ 0 ]; lst = ch [ lst ][ 0 ]; } else { if ( ! ch [ o ][ 1 ]) ch [ o ][ 1 ] = ++ cnt ; ch [ o ][ 0 ] = ch [ lst ][ 0 ]; o = ch [ o ][ 1 ]; lst = ch [ lst ][ 1 ]; } } val [ o ] = val [ lst ] \+ 1 ; } int query ( int o1 , int o2 , int v ) { int ret = 0 ; for ( int i = 28 ; i >= 0 ; i \-- ) { int t = (( v & ( 1 << i )) ? 1 : 0 ); if ( val [ ch [ o1 ][ ! t ]] \- val [ ch [ o2 ][ ! t ]]) ret += ( 1 << i ), o1 = ch [ o1 ][ ! t ], o2 = ch [ o2 ][ ! t ]; // 尽量向不同的地方跳 else o1 = ch [ o1 ][ t ], o2 = ch [ o2 ][ t ]; } return ret ; } } st ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> q ; for ( int i = 1 ; i <= n ; i ++ ) cin >> a [ i ], s [ i ] = s [ i \- 1 ] ^ a [ i ]; for ( int i = 1 ; i <= n ; i ++ ) st . rt [ i ] = ++ st . cnt , st . insert ( st . rt [ i ], st . rt [ i \- 1 ], s [ i ]); while ( q \-- ) { cin >> op ; if ( op == 'A' ) { n ++ ; cin >> a [ n ]; s [ n ] = s [ n \- 1 ] ^ a [ n ]; st . rt [ n ] = ++ st . cnt ; st . insert ( st . rt [ n ], st . rt [ n \- 1 ], s [ n ]); } if ( op == 'Q' ) { cin >> l >> r >> x ; l \-- ; r \-- ; if ( l == 0 ) cout << max ( s [ n ] ^ x , st . query ( st . rt [ r ], st . rt [ 0 ], s [ n ] ^ x )) << '\n' ; else cout << st . query ( st . rt [ r ], st . rt [ l \- 1 ], s [ n ] ^ x ) << '\n' ; } } return 0 ; } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/persistent-trie.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/persistent-trie.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [H-J-Granger](https://github.com/H-J-Granger), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [CCXXXI](https://github.com/CCXXXI), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [AngelKitty](https://github.com/AngelKitty), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [c-forrest](https://github.com/c-forrest), [Chrogeek](https://github.com/Chrogeek), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Henry-ZHR](https://github.com/Henry-ZHR), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [ouuan](https://github.com/ouuan), [Peanut-Tang](https://github.com/Peanut-Tang), [REYwmp](https://github.com/REYwmp), [shuzhouliu](https://github.com/shuzhouliu), [SukkaW](https://github.com/SukkaW), [Tiphereth-A](https://github.com/Tiphereth-A), [代建杉](mailto:wood3s@foxmail.com)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
