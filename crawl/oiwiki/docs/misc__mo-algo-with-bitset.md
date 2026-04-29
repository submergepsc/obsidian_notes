# 莫队配合 bitset - OI Wiki

- Source: https://oi-wiki.org/misc/mo-algo-with-bitset/

# 莫队配合 bitset

bitset 常用于常规数据结构难以维护的判定、统计问题，而莫队可以维护常规数据结构难以维护的区间信息．把两者结合起来使用可以同时利用两者的优势．

## 例题 [「Ynoi2016」掉进兔子洞](https://www.luogu.com.cn/problem/P4688)

本题刚好符合上面提到的莫队配合 bitset 的特征．不难想到我们可以分别用 bitset 存储每一个区间内的出现过的所有权值，一组询问的答案即所有区间的长度和减去三者的并集元素个数 ×3×3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

但是在莫队中使用 bitset 也需要针对 bitset 的特性调整算法：

  1. bitset 不能很好地处理同时出现多个权值的情况．我们可以把当前元素离散化后的权值与当前区间的出现次数之和作为往 bitset 中插入的对象．
  2. 我们平常使用莫队时，可能会不注意 4 种移动指针的方法顺序，所以指针移动的过程中可能会出现区间的左端点在右端点右边，区间长度为负值的情况，导致元素的个数为负数．这在其他情况下并没有什么影响，但是本题中在 bitset 中插入的元素与元素个数有关，所以我们需要注意 4 种移动指针的方法顺序，将左右指针分别往左边和右边移动的语句写在前面，避免往 bitset 中插入负数．
  3. 虽然 bitset 用空间小，但是仍然难以承受 105 ×105105×105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数据规模．所以我们需要将询问划分成常数块分别处理，保证空间刚好足够的情况下时间复杂度不变．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 ``` |  ```text #include <algorithm> #include <bitset> #include <cmath> #include <cstring> #include <iostream> using namespace std ; constexpr int N = 100005 , M = N / 3 \+ 10 ; int n , m , maxn ; int a [ N ], ans [ M ], cnt [ N ]; bitset < N > sum [ M ], now ; struct query { int l , r , id ; bool operator < ( const query & x ) const { if ( l / maxn != x . l / maxn ) return l < x . l ; return ( l / maxn ) & 1 ? r < x . r : r > x . r ; } } q [ M * 3 ]; void static_set () { static int tmp [ N ]; memcpy ( tmp , a , sizeof ( a )); sort ( tmp \+ 1 , tmp \+ n \+ 1 ); for ( int i = 1 ; i <= n ; i ++ ) a [ i ] = lower_bound ( tmp \+ 1 , tmp \+ n \+ 1 , a [ i ]) \- tmp ; } void add ( int x ) { now . set ( x \+ cnt [ x ]); cnt [ x ] ++ ; } void del ( int x ) { cnt [ x ] \-- ; now . reset ( x \+ cnt [ x ]); } void solve () { int cnt = 0 , tot = 0 ; now . reset (); for ( tot = 0 ; tot < M \- 5 && m ; tot ++ ) { m \-- ; ans [ tot ] = 0 ; sum [ tot ]. set (); for ( int j = 0 ; j < 3 ; j ++ ) { cin >> q [ cnt ]. l >> q [ cnt ]. r ; q [ cnt ]. id = tot ; ans [ tot ] += q [ cnt ]. r \- q [ cnt ]. l \+ 1 ; cnt ++ ; } } sort ( q , q \+ cnt ); for ( int i = 0 , l = 1 , r = 0 ; i < cnt ; i ++ ) { while ( l > q [ i ]. l ) add ( a [ \-- l ]); while ( r < q [ i ]. r ) add ( a [ ++ r ]); while ( l < q [ i ]. l ) del ( a [ l ++ ]); while ( r > q [ i ]. r ) del ( a [ r \-- ]); sum [ q [ i ]. id ] &= now ; } for ( int i = 0 ; i < tot ; i ++ ) cout << ans [ i ] \- ( int ) sum [ i ]. count () * 3 << '\n' ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> m ; for ( int i = 1 ; i <= n ; i ++ ) cin >> a [ i ]; static_set (); maxn = sqrt ( n ); solve (); memset ( cnt , 0 , sizeof ( cnt )); solve (); memset ( cnt , 0 , sizeof ( cnt )); solve (); return 0 ; } ```   
---|---  
  
## 习题

  * [小清新人渣的本愿](https://www.luogu.com.cn/problem/P3674)
  * [「Ynoi2017」由乃的玉米田](https://www.luogu.com.cn/problem/P5355)
  * [「Ynoi2011」WBLT](https://www.luogu.com.cn/problem/P5313)

* * *

>  __本页面最近更新： 2026/4/23 03:45:48，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/mo-algo-with-bitset.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/mo-algo-with-bitset.md "edit.link.title")  
>  __本页面贡献者：[countercurrent-time](https://github.com/countercurrent-time), [Ir1d](https://github.com/Ir1d), [Backl1ght](https://github.com/Backl1ght), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [greyqz](https://github.com/greyqz), [kenlig](https://github.com/kenlig), [lailai0916](https://github.com/lailai0916), [MicDZ](https://github.com/MicDZ), [ouuan](https://github.com/ouuan), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
