# 随机增量法 - OI Wiki

- Source: https://oi-wiki.org/geometry/random-incremental/

# 随机增量法

## 引入

随机增量算法是计算几何的一个重要算法，它对理论知识要求不高，算法时间复杂度低，应用范围广大．

增量法 (Incremental Algorithm) 的思想与第一数学归纳法类似，它的本质是将一个问题化为规模刚好小一层的子问题．解决子问题后加入当前的对象．写成递归式是：

𝑇(𝑛)=𝑇(𝑛−1)+𝑔(𝑛)T(n)=T(n−1)+g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

增量法形式简洁，可以应用于许多的几何题目中．

增量法往往结合随机化，可以避免最坏情况的出现．

## 最小圆覆盖问题

### 题意描述

在一个平面上有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点，求一个半径最小的圆，能覆盖所有的点．

### 过程

假设圆 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是前 𝑖 −1i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点的最小覆盖圆，加入第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点，如果在圆内或边上则什么也不做．否则，新得到的最小覆盖圆肯定经过第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点．

然后以第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点为基础（半径为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），重复以上过程依次加入第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点，若第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点在圆外，则最小覆盖圆必经过第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点．

重复以上步骤．（因为最多需要三个点来确定这个最小覆盖圆，所以重复三次）

遍历完所有点之后，所得到的圆就是覆盖所有点得最小圆．

### 性质

**时间复杂度** 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，证明详见参考资料．

**空间复杂度** 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 实现

代码实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 ``` |  ```text #include <cmath> #include <cstdio> #include <cstdlib> #include <cstring> #include <iostream> using namespace std ; int n ; double r ; struct point { double x , y ; } p [ 100005 ], o ; double sqr ( double x ) { return x * x ; } double dis ( point a , point b ) { return sqrt ( sqr ( a . x \- b . x ) \+ sqr ( a . y \- b . y )); } bool cmp ( double a , double b ) { return fabs ( a \- b ) < 1e-8 ; } point geto ( point a , point b , point c ) { double a1 , a2 , b1 , b2 , c1 , c2 ; point ans ; a1 = 2 * ( b . x \- a . x ), b1 = 2 * ( b . y \- a . y ), c1 = sqr ( b . x ) \- sqr ( a . x ) \+ sqr ( b . y ) \- sqr ( a . y ); a2 = 2 * ( c . x \- a . x ), b2 = 2 * ( c . y \- a . y ), c2 = sqr ( c . x ) \- sqr ( a . x ) \+ sqr ( c . y ) \- sqr ( a . y ); if ( cmp ( a1 , 0 )) { ans . y = c1 / b1 ; ans . x = ( c2 \- ans . y * b2 ) / a2 ; } else if ( cmp ( b1 , 0 )) { ans . x = c1 / a1 ; ans . y = ( c2 \- ans . x * a2 ) / b2 ; } else { ans . x = ( c2 * b1 \- c1 * b2 ) / ( a2 * b1 \- a1 * b2 ); ans . y = ( c2 * a1 \- c1 * a2 ) / ( b2 * a1 \- b1 * a2 ); } return ans ; } int main () { scanf ( "%d" , & n ); for ( int i = 1 ; i <= n ; i ++ ) scanf ( "%lf%lf" , & p [ i ]. x , & p [ i ]. y ); for ( int i = 1 ; i <= n ; i ++ ) swap ( p [ rand () % n \+ 1 ], p [ rand () % n \+ 1 ]); o = p [ 1 ]; for ( int i = 1 ; i <= n ; i ++ ) { if ( dis ( o , p [ i ]) < r || cmp ( dis ( o , p [ i ]), r )) continue ; o . x = ( p [ i ]. x \+ p [ 1 ]. x ) / 2 ; o . y = ( p [ i ]. y \+ p [ 1 ]. y ) / 2 ; r = dis ( p [ i ], p [ 1 ]) / 2 ; for ( int j = 2 ; j < i ; j ++ ) { if ( dis ( o , p [ j ]) < r || cmp ( dis ( o , p [ j ]), r )) continue ; o . x = ( p [ i ]. x \+ p [ j ]. x ) / 2 ; o . y = ( p [ i ]. y \+ p [ j ]. y ) / 2 ; r = dis ( p [ i ], p [ j ]) / 2 ; for ( int k = 1 ; k < j ; k ++ ) { if ( dis ( o , p [ k ]) < r || cmp ( dis ( o , p [ k ]), r )) continue ; o = geto ( p [ i ], p [ j ], p [ k ]); r = dis ( o , p [ i ]); } } } printf ( "%.10lf \n %.10lf %.10lf" , r , o . x , o . y ); return 0 ; } ```   
---|---  
  
## 练习

[最小圆覆盖](https://www.luogu.com.cn/problem/P1742)

[「HNOI2012」射箭](https://www.luogu.com.cn/problem/P3222)

[CodeForces 442E](https://codeforces.com/problemset/problem/442/E)

## 参考资料与扩展阅读

[随机增量算法 - 解轶伦](https://github.com/hzwer/shareOI/blob/master/%E8%AE%A1%E7%AE%97%E5%87%A0%E4%BD%95/%E9%9A%8F%E6%9C%BA%E5%A2%9E%E9%87%8F%E7%AE%97%E6%B3%95_%E8%A7%A3%E8%BD%B6%E4%BC%A6.pdf)

<https://www.cnblogs.com/aininot260/p/9635757.html>

<https://www.cise.ufl.edu/~sitharam/COURSES/CG/kreveldnbhd.pdf>

<https://blog.csdn.net/u014609452/article/details/62039612>

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/geometry/random-incremental.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/geometry/random-incremental.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Catreap](https://github.com/Catreap), [TianyiQ](https://github.com/TianyiQ), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [Henry-ZHR](https://github.com/Henry-ZHR), [HeRaNO](https://github.com/HeRaNO), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [ouuan](https://github.com/ouuan), [sshwy](https://github.com/sshwy), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
