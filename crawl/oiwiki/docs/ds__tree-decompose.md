# 树分块 - OI Wiki

- Source: https://oi-wiki.org/ds/tree-decompose/

# 树分块

## 树分块的方式

可以参考 [真 - 树上莫队](../../misc/mo-algo-on-tree/)．

也可以参考 [ouuan 的博客/莫队、带修莫队、树上莫队详解/树上莫队](https://ouuan.github.io/莫队、带修莫队、树上莫队详解/#树上莫队)．

树上莫队同样可以参考以上两篇文章．

## 树分块的应用

树分块除了应用于莫队，还可以灵活地运用到某些树上问题中．但可以用树分块解决的题目往往都有更优秀的做法，所以相关的题目较少．

顺带提一句，「gty 的妹子树」的树分块做法可以被菊花图卡掉．

### [BZOJ4763 雪辉](https://hydro.ac/p/bzoj-P4763)

先进行树分块，然后对每个块的关键点，预处理出它到祖先中每个关键点的路径上颜色的 bitset，以及每个关键点的最近关键点祖先，复杂度是 𝑂(𝑛√𝑛 +𝑛𝑐32)O(nn+nc32)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑛√𝑛nn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是暴力从每个关键点向上跳的复杂度，𝑛𝑐32nc32![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是把 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 `bitset` 存下来的复杂度．

回答询问的时候，先从路径的端点暴力跳到所在块的关键点，再从所在块的关键点一块一块地向上跳，直到 𝑙𝑐𝑎lca![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在块，然后再暴力跳到 𝑙𝑐𝑎lca![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．关键点之间的 `bitset` 已经预处理了，剩下的在暴力跳的过程中计算．单次询问复杂度是 𝑂(√𝑛 +𝑐32)O(n+c32)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是块内暴力跳以及块直接向上跳的复杂度，𝑂(𝑐32)O(c32)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是将预处理的结果与暴力跳的结果合并的复杂度．数颜色个数可以用 `bitset` 的 `count()`，求 mexmex![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以用 `bitset` 的 `_Find_first()`．

所以，总复杂度为 𝑂((𝑛 +𝑚)(√𝑛 +𝑐32))O((n+m)(n+c32))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 ``` |  ```text #include <bitset> #include <cctype> #include <iostream> #if defined(_MSC_VER) && !defined(__clang__) #include <immintrin.h> #endif using namespace std ; constexpr int N = 100010 ; constexpr int B = 666 ; constexpr int C = 30000 ; void add ( int u , int v ); void dfs ( int u ); int head [ N ], nxt [ N << 1 ], to [ N << 1 ], cnt ; int n , m , type , c [ N ], fa [ N ], dep [ N ], sta [ N ], top , tot , bl [ N ], key [ N / B \+ 5 ], p [ N ], keyid [ N ]; bool vis [ N ]; bitset < C > bs [ N / B \+ 5 ][ N / B \+ 5 ], temp ; template < size_t N > size_t find_first ( std :: bitset < N > b ) { #if defined(__GNUC__) && !defined(__clang__) return b . _Find_first (); #elif defined(_MSC_VER) && !defined(__clang__) using word_t = decltype ( b . _Getword ( 0 )); constexpr ptrdiff_t word_len = CHAR_BIT * sizeof ( word_t ); constexpr ptrdiff_t words = N == 0 ? 0 : ( N \- 1 ) / word_len ; size_t ans = 0 ; for ( size_t i = 0 ; i <= words ; ++ i ) if ( b . _Getword ( i ) != 0 ) { if ( sizeof ( word_t ) == sizeof ( unsigned int )) return i * word_len \+ _tzcnt_u32 ( b . _Getword ( i )); else return i * word_len \+ _tzcnt_u64 ( b . _Getword ( i )); } return N ; #else auto s = b . to_string (); for ( size_t i = s . size () \- 1 ; ~ i ; \-- i ) if ( s [ i ] & 1 ) return s . size () \- 1 \- i ; return N ; #endif } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int i , u , v , x , y , k , lastans = 0 ; cin >> n >> m >> type ; for ( i = 1 ; i <= n ; ++ i ) cin >> c [ i ]; for ( i = 1 ; i < n ; ++ i ) { cin >> u >> v ; add ( u , v ); add ( v , u ); } dfs ( 1 ); if ( ! tot ) ++ tot ; if ( keyid [ key [ tot ]] == tot ) keyid [ key [ tot ]] = 0 ; key [ tot ] = 1 ; keyid [ 1 ] = tot ; while ( top ) bl [ sta [ top \-- ]] = tot ; for ( i = 1 ; i <= tot ; ++ i ) { // 预处理 if ( vis [ key [ i ]]) continue ; vis [ key [ i ]] = true ; temp . reset (); for ( u = key [ i ]; u ; u = fa [ u ]) { temp [ c [ u ]] = 1 ; if ( keyid [ u ]) { if ( ! p [ key [ i ]] && u != key [ i ]) p [ key [ i ]] = u ; bs [ keyid [ key [ i ]]][ keyid [ u ]] = temp ; } } } while ( m \-- ) { cin >> k ; temp . reset (); while ( k \-- ) { cin >> x >> y ; u = x ^= lastans ; v = y ^= lastans ; while ( key [ bl [ x ]] != key [ bl [ y ]]) { if ( dep [ key [ bl [ x ]]] > dep [ key [ bl [ y ]]]) { if ( x == u ) { // 若是第一次跳先暴力跳到关键点 while ( x != key [ bl [ u ]]) { temp [ c [ x ]] = 1 ; x = fa [ x ]; } } else x = p [ x ]; // 否则跳一整块 } else { if ( y == v ) { while ( y != key [ bl [ v ]]) { temp [ c [ y ]] = 1 ; y = fa [ y ]; } } else y = p [ y ]; } } if ( keyid [ x ]) temp |= bs [ keyid [ key [ bl [ u ]]]][ keyid [ x ]]; if ( keyid [ y ]) temp |= bs [ keyid [ key [ bl [ v ]]]][ keyid [ y ]]; while ( x != y ) { if ( dep [ x ] > dep [ y ]) { temp [ c [ x ]] = 1 ; x = fa [ x ]; } else { temp [ c [ y ]] = 1 ; y = fa [ y ]; } } temp [ c [ x ]] = true ; } int ans1 = temp . count (), ans2 = find_first ( ~ temp ); cout << ans1 << ' ' << ans2 << '\n' ; lastans = ( ans1 \+ ans2 ) * type ; } return 0 ; } void dfs ( int u ) { // 根据题意找点 int i , v , t = top ; for ( i = head [ u ]; i ; i = nxt [ i ]) { v = to [ i ]; if ( v == fa [ u ]) continue ; fa [ v ] = u ; dep [ v ] = dep [ u ] \+ 1 ; dfs ( v ); if ( top \- t >= B ) { key [ ++ tot ] = u ; if ( ! keyid [ u ]) keyid [ u ] = tot ; while ( top > t ) bl [ sta [ top \-- ]] = tot ; } } sta [ ++ top ] = u ; } void add ( int u , int v ) { nxt [ ++ cnt ] = head [ u ]; head [ u ] = cnt ; to [ cnt ] = v ; } ```   
---|---  
  
### [BZOJ4812 由乃打扑克](https://hydro.ac/p/bzoj-P4812)

这题和上一题基本一样，唯一的区别是得到 `bitset` 后如何计算答案．

~~由于 BZOJ 是计算所有测试点总时限，不好卡，所以可以用`_Find_next()` 水过去．~~

正解是每 1616![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位一起算，先预处理出 216216![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种可能的情况高位连续 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数、低位连续 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数以及中间的贡献．只不过这样要手写 `bitset`，因为标准库的 `bitset` 不能取某 1616![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位……

代码可以参考 [这篇博客](https://www.cnblogs.com/FallDream/p/bzoj4763.html)．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/tree-decompose.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/tree-decompose.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [ouuan](https://github.com/ouuan), [StudyingFather](https://github.com/StudyingFather), [H-J-Granger](https://github.com/H-J-Granger), [CCXXXI](https://github.com/CCXXXI), [countercurrent-time](https://github.com/countercurrent-time), [Marcythm](https://github.com/Marcythm), [NachtgeistW](https://github.com/NachtgeistW), [Enter-tainer](https://github.com/Enter-tainer), [sshwy](https://github.com/sshwy), [Xeonacid](https://github.com/Xeonacid), [AngelKitty](https://github.com/AngelKitty), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [c-forrest](https://github.com/c-forrest), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Henry-ZHR](https://github.com/Henry-ZHR), [HeRaNO](https://github.com/HeRaNO), [isdanni](https://github.com/isdanni), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Peanut-Tang](https://github.com/Peanut-Tang), [shuzhouliu](https://github.com/shuzhouliu), [SukkaW](https://github.com/SukkaW), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
