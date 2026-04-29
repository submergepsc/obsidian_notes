# 二维莫队 - OI Wiki

- Source: https://oi-wiki.org/misc/mo-algo-2dimen/

# 二维莫队

二维莫队，顾名思义就是每个状态有四个方向可以扩展．

二维莫队每次移动指针要操作一行或者一列的数，具体实现方式与普通的一维莫队类似，这里不再赘述．这里重点讲块长选定部分．

## 块长选定

记询问次数为 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当前矩阵的左上角坐标为 (𝑥1, 𝑦1)(x1, y1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，右下角坐标为 (𝑥2, 𝑦2)(x2, y2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，取块长为 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

那么指针 𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 移动了 Θ(𝑞 ⋅𝐵)Θ(q⋅B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，而指针 𝑦2y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 移动了 Θ(𝑛4 ⋅𝐵−3)Θ(n4⋅B−3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．

所以只需令 𝑞 ⋅𝐵 =𝑛4 ⋅𝐵−3q⋅B=n4⋅B−3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝐵 =𝑛 ⋅𝑞−14B=n⋅q−14![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

注意这样计算 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的结果 **可能为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)**，**注意特判** ．

最终，计算部分时间复杂度是 Θ(𝑛2 ⋅𝑞34)Θ(n2⋅q34)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，加上对询问的排序过程，总时间复杂度为 Θ(𝑛2 ⋅𝑞34 +𝑞log⁡𝑞)Θ(n2⋅q34+qlog⁡q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 例题 1

[BZOJ 2639 矩形计算](https://hydro.ac/p/bzoj-P2639)

输入一个 𝑛 ×𝑚n×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵，矩阵的每一个元素都是一个整数，然后有 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个询问，每次询问一个子矩阵的权值．矩阵的权值是这样定义的，对于一个整数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果它在该矩阵中出现了 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，那么它给该矩阵的权值就贡献 𝑝2p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

数据范围：1 ≤𝑛, 𝑚 ≤2001≤n, m≤200![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，0 ≤𝑞 ≤1050≤q≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，||![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矩阵元素大小 | ≤2 ×109|≤2×109![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解题思路

先离散化，二维莫队时用一个数组记录每个数当前出现的次数即可．

示例代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 ``` |  ```text #include <algorithm> #include <cmath> #include <iostream> using namespace std ; int n , m , q , a [ 201 ][ 201 ]; long long ans [ 100001 ]; int disc [ 250001 ], cntdisc ; // 离散化用 int blocklen , counts [ 40001 ]; long long now ; struct Question { int x1 , y1 , x2 , y2 , qid ; bool operator < ( Question tmp ) const { if ( x1 / blocklen != tmp . x1 / blocklen ) return x1 < tmp . x1 ; if ( y1 / blocklen != tmp . y1 / blocklen ) return y1 < tmp . y1 ; if ( x2 / blocklen != tmp . x2 / blocklen ) return x2 < tmp . x2 ; return y2 < tmp . y2 ; } } Q [ 100001 ]; int Qcnt ; void mo_algo_row ( int id , int val , int Y1 , int Y2 ) { for ( int i = Y1 ; i <= Y2 ; i ++ ) now -= ( long long ) counts [ a [ id ][ i ]] * counts [ a [ id ][ i ]], counts [ a [ id ][ i ]] += val , now += ( long long ) counts [ a [ id ][ i ]] * counts [ a [ id ][ i ]]; } void mo_algo_column ( int id , int val , int X1 , int X2 ) { for ( int i = X1 ; i <= X2 ; i ++ ) now -= ( long long ) counts [ a [ i ][ id ]] * counts [ a [ i ][ id ]], counts [ a [ i ][ id ]] += val , now += ( long long ) counts [ a [ i ][ id ]] * counts [ a [ i ][ id ]]; } void mo_algo () { blocklen = pow ( n * m , 0.5 ) / pow ( q , 0.25 ); if ( blocklen < 1 ) blocklen = 1 ; sort ( Q \+ 1 , Q \+ 1 \+ Qcnt ); int X1 = 1 , Y1 = 1 , X2 = 0 , Y2 = 0 ; for ( int i = 1 ; i <= Qcnt ; i ++ ) { while ( X1 > Q [ i ]. x1 ) mo_algo_row ( \-- X1 , 1 , Y1 , Y2 ); while ( X2 < Q [ i ]. x2 ) mo_algo_row ( ++ X2 , 1 , Y1 , Y2 ); while ( Y1 > Q [ i ]. y1 ) mo_algo_column ( \-- Y1 , 1 , X1 , X2 ); while ( Y2 < Q [ i ]. y2 ) mo_algo_column ( ++ Y2 , 1 , X1 , X2 ); while ( X1 < Q [ i ]. x1 ) mo_algo_row ( X1 ++ , -1 , Y1 , Y2 ); while ( X2 > Q [ i ]. x2 ) mo_algo_row ( X2 \-- , -1 , Y1 , Y2 ); while ( Y1 < Q [ i ]. y1 ) mo_algo_column ( Y1 ++ , -1 , X1 , X2 ); while ( Y2 > Q [ i ]. y2 ) mo_algo_column ( Y2 \-- , -1 , X1 , X2 ); ans [ Q [ i ]. qid ] = now ; } } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> m ; for ( int i = 1 ; i <= n ; i ++ ) for ( int j = 1 ; j <= m ; j ++ ) cin >> a [ i ][ j ], disc [ ++ cntdisc ] = a [ i ][ j ]; sort ( disc \+ 1 , disc \+ 1 \+ cntdisc ); cntdisc = unique ( disc \+ 1 , disc \+ cntdisc \+ 1 ) \- disc \- 1 ; for ( int i = 1 ; i <= n ; i ++ ) for ( int j = 1 ; j <= m ; j ++ ) a [ i ][ j ] = lower_bound ( disc \+ 1 , disc \+ 1 \+ cntdisc , a [ i ][ j ]) \- disc ; cin >> q ; for ( int i = 1 ; i <= q ; i ++ ) { int x1 , y1 , x2 , y2 ; cin >> x1 >> y1 >> x2 >> y2 ; if ( x1 > x2 ) swap ( x1 , x2 ); if ( y1 > y2 ) swap ( y1 , y2 ); Q [ ++ Qcnt ] = { x1 , y1 , x2 , y2 , i }; } mo_algo (); for ( int i = 1 ; i <= q ; ++ i ) cout << ans [ i ] << '\n' ; return 0 ; } ```   
---|---  
  
## 例题 2

[洛谷 P1527 [国家集训队] 矩阵乘法](https://www.luogu.com.cn/problem/P1527)

给你一个 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵，𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次询问，每次询问一个子矩形的第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小数．

数据范围：1 ≤𝑛 ≤5001≤n≤500![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，1 ≤𝑞 ≤6 ×1041≤q≤6×104![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，0 ≤𝑎𝑖,𝑗 ≤1090≤ai,j≤109![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

首先和上一题一样，需要离散化整个矩阵．但是需要注意，本题除了需要对数值进行分块，还需要对数值的值域进行分块，才能求出答案．

这里还需要用到奇偶化排序进行优化，具体内容请见 [普通莫队算法](../mo-algo/#普通莫队的优化)．

对于本题而言，时间限制不那么宽，注意代码常数的处理．取的块长计算值普遍较小，𝑛, 𝑞n, q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都取最大值时块长大约在 1111![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 左右，可以直接设定为常数来节约代码耗时．

示例代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 ``` |  ```text #include <algorithm> #include <iostream> #include <vector> using namespace std ; int n , q , a [ 501 ][ 501 ], ans [ 60001 ]; int disc [ 250001 ], cntdisc ; // 离散化用 int nn ; int blockId [ 501 ], blocklen ; // 分块 int rangeblockId [ 250001 ], rangeblocklen ; // 值域分块 int counts [ 250001 ], countsum [ 501 ]; // 该值次数及值域块总和 struct Position { int x , y ; }; vector < Position > pos [ 250001 ]; struct Question { int x1 , y1 , x2 , y2 , k , qid ; bool operator < ( Question tmp ) const { if ( blockId [ x1 ] != blockId [ tmp . x1 ]) return blockId [ x1 ] < blockId [ tmp . x1 ]; if ( blockId [ y1 ] != blockId [ tmp . y1 ]) return blockId [ x1 ] & 1 ? y1 < tmp . y1 : y1 > tmp . y1 ; if ( blockId [ y2 ] != blockId [ tmp . y2 ]) return blockId [ y1 ] & 1 ? y2 < tmp . y2 : y2 > tmp . y2 ; else return blockId [ y2 ] & 1 ? x2 < tmp . x2 : x2 > tmp . x2 ; } } Q [ 60001 ]; int Qcnt ; void mo_algo () { blocklen = 11 ; for ( int i = 1 ; i <= n ; ++ i ) blockId [ i ] = ( i \- 1 ) / blocklen \+ 1 ; rangeblocklen = n \+ 1 ; for ( int i = 1 ; i <= nn ; ++ i ) rangeblockId [ i ] = ( i \- 1 ) / rangeblocklen \+ 1 ; counts [ a [ 1 ][ 1 ]] = countsum [ rangeblockId [ a [ 1 ][ 1 ]]] = 1 ; sort ( Q \+ 1 , Q \+ 1 \+ Qcnt ); int L = 1 , R = 1 , D = 1 , U = 1 ; for ( int i = 1 ; i <= q ; ++ i ) { while ( R < Q [ i ]. y2 ) { ++ R ; for ( int i = U ; i <= D ; ++ i ) ++ counts [ a [ i ][ R ]], ++ countsum [ rangeblockId [ a [ i ][ R ]]]; } while ( L > Q [ i ]. y1 ) { \-- L ; for ( int i = U ; i <= D ; ++ i ) ++ counts [ a [ i ][ L ]], ++ countsum [ rangeblockId [ a [ i ][ L ]]]; } while ( D < Q [ i ]. x2 ) { ++ D ; for ( int i = L ; i <= R ; ++ i ) ++ counts [ a [ D ][ i ]], ++ countsum [ rangeblockId [ a [ D ][ i ]]]; } while ( U > Q [ i ]. x1 ) { \-- U ; for ( int i = L ; i <= R ; ++ i ) ++ counts [ a [ U ][ i ]], ++ countsum [ rangeblockId [ a [ U ][ i ]]]; } while ( R > Q [ i ]. y2 ) { for ( int i = U ; i <= D ; ++ i ) \-- counts [ a [ i ][ R ]], \-- countsum [ rangeblockId [ a [ i ][ R ]]]; \-- R ; } while ( L < Q [ i ]. y1 ) { for ( int i = U ; i <= D ; ++ i ) \-- counts [ a [ i ][ L ]], \-- countsum [ rangeblockId [ a [ i ][ L ]]]; ++ L ; } while ( D > Q [ i ]. x2 ) { for ( int i = L ; i <= R ; ++ i ) \-- counts [ a [ D ][ i ]], \-- countsum [ rangeblockId [ a [ D ][ i ]]]; \-- D ; } while ( U < Q [ i ]. x1 ) { for ( int i = L ; i <= R ; ++ i ) \-- counts [ a [ U ][ i ]], \-- countsum [ rangeblockId [ a [ U ][ i ]]]; ++ U ; } int res = 1 , cnt = 0 ; while ( cnt \+ countsum [ res ] < Q [ i ]. k && res <= rangeblockId [ nn ]) cnt += countsum [ res ], ++ res ; res = ( res \- 1 ) * rangeblocklen \+ 1 ; while ( cnt \+ counts [ res ] < Q [ i ]. k && res <= nn ) cnt += counts [ res ], ++ res ; ans [ Q [ i ]. qid ] = disc [ res ]; } } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> q ; nn = n * n ; for ( int i = 1 ; i <= n ; ++ i ) for ( int j = 1 ; j <= n ; ++ j ) { int x ; cin >> x ; a [ i ][ j ] = disc [ ++ cntdisc ] = x ; } sort ( disc \+ 1 , disc \+ 1 \+ cntdisc ); cntdisc = unique ( disc \+ 1 , disc \+ cntdisc \+ 1 ) \- disc \- 1 ; for ( int i = 1 ; i <= n ; ++ i ) for ( int j = 1 ; j <= n ; ++ j ) a [ i ][ j ] = lower_bound ( disc \+ 1 , disc \+ 1 \+ cntdisc , a [ i ][ j ]) \- disc ; for ( int i = 1 ; i <= q ; ++ i ) { int x1 , y1 , x2 , y2 , k ; cin >> x1 >> y1 >> x2 >> y2 >> k ; Q [ ++ Qcnt ] = { x1 , y1 , x2 , y2 , k , i }; } mo_algo (); for ( int i = 1 ; i <= q ; ++ i ) cout << ans [ i ] << '\n' ; return 0 ; } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/mo-algo-2dimen.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/mo-algo-2dimen.md "edit.link.title")  
>  __本页面贡献者：[HeRaNO](https://github.com/HeRaNO), [megakite](https://github.com/megakite), [Molmin](https://github.com/Molmin), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
