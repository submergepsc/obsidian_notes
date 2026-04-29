# 牛顿迭代法 - OI Wiki

- Source: https://oi-wiki.org/math/numerical/newton/

# 牛顿迭代法

## 引入

本文介绍如何用牛顿迭代法（Newton's method for finding roots）求方程的近似解，该方法于 17 世纪由牛顿提出．

具体的任务是，对于在 [𝑎,𝑏][a,b]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上连续且单调的函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求方程 𝑓(𝑥) =0f(x)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的近似解．

## 解释

初始时我们从给定的 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和一个近似解 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始（初值的问题与 Newton 分形有关，可参考 3Blue1Brown 的 [牛顿分形](https://www.bilibili.com/video/BV1HQ4y1q78v)）．

假设我们目前的近似解是 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们画出与 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 切于点 (𝑥𝑖,𝑓(𝑥𝑖))(xi,f(xi))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的直线 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴的交点横坐标记为 𝑥𝑖+1xi+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么这就是一个更优的近似解．重复这个迭代的过程． 根据导数的几何意义，可以得到如下关系：

𝑓′(𝑥𝑖)=𝑓(𝑥𝑖)𝑥𝑖−𝑥𝑖+1f′(xi)=f(xi)xi−xi+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

整理后得到如下递推式：

𝑥𝑖+1=𝑥𝑖−𝑓(𝑥𝑖)𝑓′(𝑥𝑖)xi+1=xi−f(xi)f′(xi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

直观地说，如果 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比较平滑，那么随着迭代次数的增加，𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 会越来越逼近方程的解．

牛顿迭代法的收敛率是平方级别的，这意味着每次迭代后近似解的精确数位会翻倍． 关于牛顿迭代法的收敛性证明可参考 [citizendium - Newton method Convergence analysis](http://en.citizendium.org/wiki/Newton%27s_method#Convergence_analysis)

当然牛顿迭代法也同样存在着缺陷，详情参考 [Xiaolin Wu - Roots of Equations 第 18 - 20 页分析](https://www.ece.mcmaster.ca/~xwu/part2.pdf)

## 求解平方根

我们尝试用牛顿迭代法求解平方根．设 𝑓(𝑥) =𝑥2 −𝑛f(x)=x2−n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这个方程的近似解就是 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的近似值．于是我们得到

𝑥𝑖+1=𝑥𝑖−𝑥2𝑖−𝑛2𝑥𝑖=𝑥𝑖+𝑛𝑥𝑖2xi+1=xi−xi2−n2xi=xi+nxi2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在实现的时候注意设置合适的精度．代码如下

### 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text double sqrt_newton ( double n ) { constexpr static double eps = 1E-15 ; double x = 1 ; while ( true ) { double nx = ( x \+ n / x ) / 2 ; if ( abs ( x \- nx ) < eps ) break ; x = nx ; } return x ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 ``` |  ```text def sqrt_newton ( n ): eps = 1e-15 x = 1 while True : nx = ( x \+ n / x ) / 2 if abs ( x \- nx ) < eps : break x = nx return x ```   
---|---  
  
## 求解整数平方根

尽管我们可以调用 `sqrt()` 函数来获取平方根的值，但这里还是讲一下牛顿迭代法的变种算法，用于求不等式 𝑥2 ≤𝑛x2≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大整数解．我们仍然考虑一个类似于牛顿迭代的过程，但需要在边界条件上稍作修改．如果 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在迭代的过程中上一次迭代值得近似解变小，而这一次迭代使得近似解变大，那么我们就不进行这次迭代，退出循环．

### 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text int isqrt_newton ( int n ) { int x = 1 ; bool decreased = false ; for (;;) { int nx = ( x \+ n / x ) >> 1 ; if ( x == nx || ( nx > x && decreased )) break ; decreased = nx < x ; x = nx ; } return x ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text def isqrt_newton ( n ): x = 1 decreased = False while True : nx = ( x \+ n // x ) // 2 if x == nx or ( nx > x and decreased ): break decreased = nx < x x = nx return x ```   
---|---  
  
## 高精度平方根

最后考虑高精度的牛顿迭代法．迭代的方法是不变的，但这次我们需要关注初始时近似解的设置，即 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．由于需要应用高精度的数一般都非常大，因此不同的初始值对于算法效率的影响也很大．一个自然的想法就是考虑 𝑥0 =2⌊12log2⁡𝑛⌋x0=2⌊12log2⁡n⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样既可以快速计算出 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，又可以较为接近平方根的近似解．

### 实现

给出 Java 代码的实现：

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text public static BigInteger isqrtNewton ( BigInteger n ) { BigInteger a = BigInteger . ONE . shiftLeft ( n . bitLength () / 2 ); boolean p_dec = false ; for (;;) { BigInteger b = n . divide ( a ). add ( a ). shiftRight ( 1 ); if ( a . compareTo ( b ) == 0 || a . compareTo ( b ) < 0 && p_dec ) break ; p_dec = a . compareTo ( b ) > 0 ; a = b ; } return a ; } ```   
---|---  
  
实践效果：在 𝑛 =101000n=101000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时候该算法的运行时间是 60 ms，如果我们不优化 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，直接从 𝑥0 =1x0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始迭代，那么运行时间将增加到 120 ms．

## 习题

  * [UVa 10428 - The Roots](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=16&page=show_problem&problem=1369)
  * [LeetCode 69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)

**本页面主要译自博文[Метод Ньютона (касательных) для поиска корней](http://e-maxx.ru/algo/roots_newton) 与其英文翻译版 [Newton's method for finding roots](https://cp-algorithms.com/num_methods/roots_newton.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/numerical/newton.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/numerical/newton.md "edit.link.title")  
>  __本页面贡献者：[H-J-Granger](https://github.com/H-J-Granger), [countercurrent-time](https://github.com/countercurrent-time), [Marcythm](https://github.com/Marcythm), [NachtgeistW](https://github.com/NachtgeistW), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [Ir1d](https://github.com/Ir1d), [sshwy](https://github.com/sshwy), [Xeonacid](https://github.com/Xeonacid), [iamtwz](https://github.com/iamtwz), [nutshellfool](https://github.com/nutshellfool), [allenanswerzq](https://github.com/allenanswerzq), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [hly1204](https://github.com/hly1204), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [Menci](https://github.com/Menci), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [SukkaW](https://github.com/SukkaW), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Peanut-Tang](https://github.com/Peanut-Tang), [shawlleyw](https://github.com/shawlleyw)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
