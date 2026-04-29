# 数值积分 - OI Wiki

- Source: https://oi-wiki.org/math/numerical/integral/

# 数值积分

## 定积分的定义

简单来说，函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的定积分 ∫𝑟𝑙𝑓(𝑥)d𝑥∫lrf(x)dx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指的是 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中与 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴围成的区域的面积（其中 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴上方的部分为正值，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴下方的部分为负值）．

很多情况下，我们需要高效，准确地求出一个积分的近似值．下面介绍的 **辛普森法** ，就是这样一种求数值积分的方法．

## 辛普森法

这个方法的思想是将被积区间分为若干小段，每段套用二次函数的积分公式进行计算．

二次函数积分公式（辛普森公式）

对于一个二次函数 𝑓(𝑥) =𝑎𝑥2 +𝑏𝑥 +𝑐f(x)=ax2+bx+c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有：

∫𝑟𝑙𝑓(𝑥)d𝑥=(𝑟−𝑙)(𝑓(𝑙)+𝑓(𝑟)+4𝑓(𝑙+𝑟2))6∫lrf(x)dx=(r−l)(f(l)+f(r)+4f(l+r2))6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

推导过程： 对于一个二次函数 𝑓(𝑥) =𝑎𝑥2 +𝑏𝑥 +𝑐f(x)=ax2+bx+c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)； 求积分可得 𝐹(𝑥) =∫𝑥0𝑓(𝑥)d𝑥 =𝑎3𝑥3 +𝑏2𝑥2 +𝑐𝑥 +𝐷F(x)=∫0xf(x)dx=a3x3+b2x2+cx+D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在这里 D 是一个常数，那么

∫𝑟𝑙𝑓(𝑥)d𝑥=𝐹(𝑟)−𝐹(𝑙)=𝑎3(𝑟3−𝑙3)+𝑏2(𝑟2−𝑙2)+𝑐(𝑟−𝑙)=(𝑟−𝑙)(𝑎3(𝑙2+𝑟2+𝑙𝑟)+𝑏2(𝑙+𝑟)+𝑐)=𝑟−𝑙6(2𝑎𝑙2+2𝑎𝑟2+2𝑎𝑙𝑟+3𝑏𝑙+3𝑏𝑟+6𝑐)=𝑟−𝑙6((𝑎𝑙2+𝑏𝑙+𝑐)+(𝑎𝑟2+𝑏𝑟+𝑐)+4(𝑎(𝑙+𝑟2)2+𝑏(𝑙+𝑟2)+𝑐))=𝑟−𝑙6(𝑓(𝑙)+𝑓(𝑟)+4𝑓(𝑙+𝑟2))∫lrf(x)dx=F(r)−F(l)=a3(r3−l3)+b2(r2−l2)+c(r−l)=(r−l)(a3(l2+r2+lr)+b2(l+r)+c)=r−l6(2al2+2ar2+2alr+3bl+3br+6c)=r−l6((al2+bl+c)+(ar2+br+c)+4(a(l+r2)2+b(l+r2)+c))=r−l6(f(l)+f(r)+4f(l+r2))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据这个辛普森公式，我们先介绍一种普通的辛普森积分法．

### 普通辛普森法

1743 年，这种方法发表于托马斯·辛普森的一篇论文中．

#### 描述

给定一个自然数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分成 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个等长的区间 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

𝑥𝑖 =𝑙 +𝑖ℎ, 𝑖 =0…2𝑛,xi=l+ih, i=0…2n,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ℎ =𝑟−𝑙2𝑛.h=r−l2n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们就可以计算每个小区间 [𝑥2𝑖−2,𝑥2𝑖][x2i−2,x2i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑖 =1…𝑛i=1…n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的积分值，将所有区间的积分值相加即为总积分．

对于 [𝑥2𝑖−2,𝑥2𝑖][x2i−2,x2i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑖 =1…𝑛i=1…n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个区间，选其中的三个点 (𝑥2𝑖−2,𝑥2𝑖−1,𝑥2𝑖)(x2i−2,x2i−1,x2i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就可以构成一条抛物线从而得到一个函数 𝑃(𝑥)P(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这个函数存在且唯一．计算原函数在该区间的积分值就变成了计算新的二次函数 𝑃(𝑥)P(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在该段区间的积分值．这样我们就可以利用辛普森公式来近似计算它．

∫𝑥2𝑖𝑥2𝑖−2𝑓(𝑥) 𝑑𝑥 ≈∫𝑥2𝑖𝑥2𝑖−2𝑃(𝑥) 𝑑𝑥 =(𝑓(𝑥2𝑖−2)+4𝑓(𝑥2𝑖−1)+(𝑓(𝑥2𝑖))ℎ3∫x2i−2x2if(x) dx≈∫x2i−2x2iP(x) dx=(f(x2i−2)+4f(x2i−1)+(f(x2i))h3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将其分段求和即可得到如下结论：

∫𝑟𝑙𝑓(𝑥)𝑑𝑥 ≈(𝑓(𝑥0)+4𝑓(𝑥1)+2𝑓(𝑥2)+4𝑓(𝑥3)+2𝑓(𝑥4)+…+4𝑓(𝑥2𝑁−1)+𝑓(𝑥2𝑁))ℎ3∫lrf(x)dx≈(f(x0)+4f(x1)+2f(x2)+4f(x3)+2f(x4)+…+4f(x2N−1)+f(x2N))h3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

#### 误差

我们直接给出结论，普通辛普森法的误差为：

−190(𝑟−𝑙2)5𝑓(4)(𝜉)−190(r−l2)5f(4)(ξ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝜉ξ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是位于区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的某个值．

#### 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text constexpr int N = 1000 * 1000 ; double simpson_integration ( double a , double b ) { double h = ( b \- a ) / N ; double s = f ( a ) \+ f ( b ); for ( int i = 1 ; i <= N \- 1 ; ++ i ) { double x = a \+ h * i ; s += f ( x ) * (( i & 1 ) ? 4 : 2 ); } s *= h / 3 ; return s ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text N = 1000 * 1000 def simpson_integration ( a , b ): h = ( b \- a ) / N s = f ( a ) \+ f ( b ) for i in range ( 1 , N ): x = a \+ h * i if i & 1 : s = s \+ f ( x ) * 4 else : s = s \+ f ( x ) * 2 s = s * ( h / 3 ) return s ```   
---|---  
  
### 自适应辛普森法

普通的方法为保证精度在时间方面无疑会受到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的限制，我们应该找一种更加合适的方法．

现在唯一的问题就是如何进行分段．如果段数少了计算误差就大，段数多了时间效率又会低．我们需要找到一个准确度和效率的平衡点．

我们这样考虑：假如有一段图像已经很接近二次函数的话，直接带入公式求积分，得到的值精度就很高了，不需要再继续分割这一段了．

于是我们有了这样一种分割方法：每次判断当前段和二次函数的相似程度，如果足够相似的话就直接代入公式计算，否则将当前段分割成左右两段递归求解．

现在就剩下一个问题了：如果判断每一段和二次函数是否相似？

我们把当前段直接代入公式求积分，再将当前段从中点分割成两段，把这两段再直接代入公式求积分．如果当前段的积分和分割成两段后的积分之和相差很小的话，就可以认为当前段和二次函数很相似了，不用再递归分割了．

上面就是自适应辛普森法的思想．在分治判断的时候，除了判断精度是否正确，一般还要强制执行最少的迭代次数．

参考代码如下：

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text double simpson ( double l , double r ) { double mid = ( l \+ r ) / 2 ; return ( r \- l ) * ( f ( l ) \+ 4 * f ( mid ) \+ f ( r )) / 6 ; // 辛普森公式 } double asr ( double l , double r , double eps , double ans , int step ) { double mid = ( l \+ r ) / 2 ; double fl = simpson ( l , mid ), fr = simpson ( mid , r ); if ( abs ( fl \+ fr \- ans ) <= 15 * eps && step < 0 ) return fl \+ fr \+ ( fl \+ fr \- ans ) / 15 ; // 足够相似的话就直接返回 return asr ( l , mid , eps / 2 , fl , step \- 1 ) \+ asr ( mid , r , eps / 2 , fr , step \- 1 ); // 否则分割成两段递归求解 } double calc ( double l , double r , double eps ) { return asr ( l , r , eps , simpson ( l , r ), 12 ); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text def simpson ( l , r ): mid = ( l \+ r ) / 2 return ( r \- l ) * ( f ( l ) \+ 4 * f ( mid ) \+ f ( r )) / 6 # 辛普森公式 def asr ( l , r , eps , ans , step ): mid = ( l \+ r ) / 2 fl = simpson ( l , mid ) fr = simpson ( mid , r ) if abs ( fl \+ fr \- ans ) <= 15 * eps and step < 0 : return fl \+ fr \+ ( fl \+ fr \- ans ) / 15 # 足够相似的话就直接返回 return asr ( l , mid , eps / 2 , fl , step \- 1 ) \+ asr ( mid , r , eps / 2 , fr , step \- 1 ) # 否则分割成两段递归求解 def calc ( l , r , eps ): return asr ( l , r , eps , simpson ( l , r ), 12 ) ```   
---|---  
  
## 习题

  * [Luogu4525【模板】自适应辛普森法 1](https://www.luogu.com.cn/problem/P4525)
  * [HDU1724 Ellipse](https://acm.hdu.edu.cn/showproblem.php?pid=1724)
  * [NOI2005 月下柠檬树](https://www.luogu.com.cn/problem/P4207)

## 参考资料

<https://doi.org/10.1145/321526.321537>：该文章讨论了自适应 Simpson 法的改进方案，其中详细论述了上文代码中的常数 `15` 的由来与优势．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/numerical/integral.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/numerical/integral.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [H-J-Granger](https://github.com/H-J-Granger), [StudyingFather](https://github.com/StudyingFather), [Enter-tainer](https://github.com/Enter-tainer), [Tiphereth-A](https://github.com/Tiphereth-A), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [ksyx](https://github.com/ksyx), [ShaoChenHeng](https://github.com/ShaoChenHeng), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [Chrogeek](https://github.com/Chrogeek), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mao1t](https://github.com/mao1t), [Menci](https://github.com/Menci), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [Nanarikom](https://github.com/Nanarikom), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [SukkaW](https://github.com/SukkaW), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [alphagocc](https://github.com/alphagocc), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Peanut-Tang](https://github.com/Peanut-Tang), [shawlleyw](https://github.com/shawlleyw), [Xeonacid](https://github.com/Xeonacid), [Yanjun-Zhao](https://github.com/Yanjun-Zhao), [zyj-111](https://github.com/zyj-111)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
