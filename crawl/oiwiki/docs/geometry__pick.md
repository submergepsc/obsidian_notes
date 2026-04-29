# Pick 定理 - OI Wiki

- Source: https://oi-wiki.org/geometry/pick/

# Pick 定理

## Pick 定理

Pick 定理：给定顶点均为整点的简单多边形，皮克定理说明了其面积 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和内部格点数目 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、边上格点数目 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的关系：𝐴=𝑖+𝑏2−1A=i+b2−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

具体证明：[Pick's theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem)

它有以下推广：

  * 取格点的组成图形的面积为一单位．在平行四边形格点，皮克定理依然成立．套用于任意三角形格点，皮克定理则是 𝐴=2×𝑖+𝑏−2A=2×i+b−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 对于非简单的多边形 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，皮克定理 𝐴=𝑖+𝑏2−𝜒(𝑃)A=i+b2−χ(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝜒(𝑃)χ(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **欧拉特征数** ．
  * 高维推广：Ehrhart 多项式
  * 皮克定理和 **欧拉公式** （𝑉−𝐸+𝐹=2V−E+F=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）等价．

## 一道例题 ([POJ 1265](http://poj.org/problem?id=1265))

### 题目大意

在直角坐标系中，一个机器人从任意点出发进行 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次移动，每次向右移动 𝑑𝑥dx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，向上移动 𝑑𝑦dy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最后会形成一个平面上的封闭简单多边形，求边上的点的数量，多边形内的点的数量，多边形面积．

### 题解

这道题目其实用了以下三个知识：

  * 以整点为顶点的线段，如果边 𝑑𝑥dx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑑𝑦dy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都不为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，经过的格点数是 gcd(𝑑𝑥,𝑑𝑦) +1gcd(dx,dy)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当然，如果要算一整个图形的，多加的点会被上一条边计算，也就不需要加了．那么一条边覆盖的点的个数为 gcd(𝑑𝑥,𝑑𝑦)gcd(dx,dy)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑑𝑥,𝑑𝑦dx,dy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为线段横向占的点数和纵向占的点数．如果 𝑑𝑥dx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑑𝑦dy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则覆盖的点数为 𝑑𝑦dy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **或** 𝑑𝑥dx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * Pick 定理：平面上以整点为顶点的简单多边形的面积 = 边上的点数/2 + 内部的点数 - 1．
  * 任意一个多边形的面积等于按顺序求相邻两个点与原点组成的向量的叉积之和的一半（这个也可以通过顺时针定积分求得）．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``` |  ```text #include <cmath> #include <iomanip> #include <iostream> using namespace std ; constexpr int MAXN = 110 ; struct node { int x , y ; } p [ MAXN ]; // 求最大公约数 int gcd ( int x , int y ) { return y == 0 ? x : gcd ( y , x % y ); } // 求区域 int area ( int a , int b ) { return p [ a ]. x * p [ b ]. y \- p [ a ]. y * p [ b ]. x ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int t , ncase = 1 ; cin >> t ; while ( t \-- ) { int n , dx , dy , x , y , num = 0 , sum = 0 ; cin >> n ; p [ 0 ]. x = 0 , p [ 0 ]. y = 0 ; for ( int i = 1 ; i <= n ; i ++ ) { cin >> x >> y ; p [ i ]. x = x \+ p [ i \- 1 ]. x , p [ i ]. y = y \+ p [ i \- 1 ]. y ; dx = x , dy = y ; if ( x < 0 ) dx = \- x ; if ( y < 0 ) dy = \- y ; num += gcd ( dx , dy ); sum += area ( i \- 1 , i ); } if ( sum < 0 ) sum = \- sum ; cout << fixed << setprecision ( 1 ); cout << "Scenario #" << ncase ++ << ": \n " ; cout << (( sum \- num \+ 2 ) >> 1 ) << ' ' << num << ' ' << sum * 0.5 << " \n\n " ; } return 0 ; } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/geometry/pick.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/geometry/pick.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [FFjet](https://github.com/FFjet), [ksyx](https://github.com/ksyx), [StudyingFather](https://github.com/StudyingFather), [yjl9903](https://github.com/yjl9903), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [kenlig](https://github.com/kenlig), [lhhxxxxx](https://github.com/lhhxxxxx), [ShaoChenHeng](https://github.com/ShaoChenHeng), [thredreams](https://github.com/thredreams), [Tiphereth-A](https://github.com/Tiphereth-A), [WalterSumbon](https://github.com/WalterSumbon), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
