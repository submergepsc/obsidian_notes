# 复杂度简介 - OI Wiki

- Source: https://oi-wiki.org/basic/complexity/

# 复杂度简介

时间复杂度和空间复杂度是衡量一个算法效率的重要标准．

## 基本操作数

同一个算法在不同的计算机上运行的速度会有一定的差别，并且实际运行速度难以在理论上进行计算，实际去测量又比较麻烦，所以我们通常考虑的不是算法运行的实际用时，而是算法运行所需要进行的基本操作的数量．

在普通的计算机上，加减乘除、访问变量（基本数据类型的变量，下同）、给变量赋值等都可以看作基本操作．

对基本操作的计数或是估测可以作为评判算法用时的指标．

## 时间复杂度

### 定义

衡量一个算法的快慢，一定要考虑数据规模的大小．所谓数据规模，一般指输入的数字个数、输入中给出的图的点数与边数等等．一般来说，数据规模越大，算法的用时就越长．而在算法竞赛中，我们衡量一个算法的效率时，最重要的不是看它在某个数据规模下的用时，而是看它的用时随数据规模而增长的趋势，即 **时间复杂度** ．

### 引入

考虑用时随数据规模变化的趋势的主要原因有以下几点：

  1. 现代计算机每秒可以处理数亿乃至更多次基本运算，因此我们处理的数据规模通常很大．如果算法 A 在规模为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数据上用时为 100𝑛100n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而算法 B 在规模为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数据上用时为 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在数据规模小于 100100![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时算法 B 用时更短，但在一秒钟内算法 A 可以处理数百万规模的数据，而算法 B 只能处理数万规模的数据．在允许算法执行时间更久时，时间复杂度对可处理数据规模的影响就会更加明显，远大于同一数据规模下用时的影响．
  2. 我们采用基本操作数来表示算法的用时，而不同的基本操作实际用时是不同的，例如加减法的用时远小于除法的用时．计算时间复杂度而忽略不同基本操作之间的区别以及一次基本操作与十次基本操作之间的区别，可以消除基本操作间用时不同的影响．

当然，算法的运行用时并非完全由输入规模决定，而是也与输入的内容相关．所以，时间复杂度又分为几种，例如：

  1. 最坏时间复杂度，即每个输入规模下用时最长的输入对应的时间复杂度．在算法竞赛中，由于输入可以在给定的数据范围内任意给定，我们为保证算法能够通过某个数据范围内的任何数据，一般考虑最坏时间复杂度．
  2. 平均（期望）时间复杂度，即每个输入规模下所有可能输入对应用时的平均值的复杂度（随机输入下期望用时的复杂度）．

所谓「用时随数据规模而增长的趋势」是一个模糊的概念，我们需要借助下文所介绍的 **渐近符号** 来形式化地表示时间复杂度．

## 渐近符号的定义

渐近符号是函数的阶的规范描述．简单来说，渐近符号忽略了一个函数中增长较慢的部分以及各项的系数（在时间复杂度相关分析中，系数一般被称作「常数」），而保留了可以用来表明该函数增长趋势的重要部分．

一个简单的记忆方法是，含等于（非严格）用大写，不含等于（严格）用小写，相等是 ΘΘ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，小于是 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，大于是 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．大 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和小 𝑜o![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 原本是希腊字母 Omicron，由于字形相同，也可以理解为拉丁字母的大 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和小 𝑜o![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在英文中，词根「-micro-」和「-mega-」常用于表示 10 的负六次方（百万分之一）和六次方（百万），也表示「小」和「大」．小和大也是希腊字母 Omicron 和 Omega 常表示的含义．

### 大 Θ 符号

对于函数 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑓(𝑛) =Θ(𝑔(𝑛))f(n)=Θ(g(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当 ∃𝑐1,𝑐2,𝑛0 >0∃c1,c2,n0>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 ∀𝑛 ≥𝑛0,0 ≤𝑐1 ⋅𝑔(𝑛) ≤𝑓(𝑛) ≤𝑐2 ⋅𝑔(𝑛)∀n≥n0,0≤c1⋅g(n)≤f(n)≤c2⋅g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

也就是说，如果函数 𝑓(𝑛) =Θ(𝑔(𝑛))f(n)=Θ(g(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么我们能找到两个正数 𝑐1,𝑐2c1,c2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被 𝑐1 ⋅𝑔(𝑛)c1⋅g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑐2 ⋅𝑔(𝑛)c2⋅g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 夹在中间．

例如，3𝑛2 +5𝑛 −3 =Θ(𝑛2)3n2+5n−3=Θ(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 这里的 𝑐1,𝑐2,𝑛0c1,c2,n0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以分别是 2,4,1002,4,100![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝑛√𝑛 +𝑛log5⁡𝑛 +𝑚log⁡𝑚 +𝑛𝑚 =Θ(𝑛√𝑛 +𝑚log⁡𝑚 +𝑛𝑚)nn+nlog5⁡n+mlog⁡m+nm=Θ(nn+mlog⁡m+nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这里的 𝑐1,𝑐2,𝑛0c1,c2,n0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以分别是 1,2,1001,2,100![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 大 O 符号

ΘΘ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 符号同时给了我们一个函数的上下界，如果只知道一个函数的渐近上界而不知道其渐近下界，可以使用 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 符号．𝑓(𝑛) =𝑂(𝑔(𝑛))f(n)=O(g(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当 ∃𝑐,𝑛0∃c,n0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 ∀𝑛 ≥𝑛0,0 ≤𝑓(𝑛) ≤𝑐 ⋅𝑔(𝑛)∀n≥n0,0≤f(n)≤c⋅g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

研究时间复杂度时通常会使用 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 符号，因为我们关注的通常是程序用时的上界，而不关心其用时的下界．

需要注意的是，这里的「上界」和「下界」是对于函数的变化趋势而言的，而不是对算法而言的．算法用时的上界对应的是「最坏时间复杂度」而非大 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记号．所以，使用 ΘΘ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记号表示最坏时间复杂度是完全可行的，甚至可以说 ΘΘ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更加精确，而使用 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记号的主要原因，一是我们有时只能证明时间复杂度的上界而无法证明其下界（这种情况一般出现在较为复杂的算法以及复杂度分析），二是 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在电脑上输入更方便一些．

### 大 Ω 符号

同样的，我们使用 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 符号来描述一个函数的渐近下界．𝑓(𝑛) =Ω(𝑔(𝑛))f(n)=Ω(g(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当 ∃𝑐,𝑛0∃c,n0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 ∀𝑛 ≥𝑛0,0 ≤𝑐 ⋅𝑔(𝑛) ≤𝑓(𝑛)∀n≥n0,0≤c⋅g(n)≤f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 小 o 符号

如果说 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 符号相当于小于等于号，那么 𝑜o![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 符号就相当于小于号．

小 𝑜o![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 符号大量应用于数学分析中，函数在某点处的泰勒展开式拥有皮亚诺余项，使用小 𝑜o![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 符号表示严格小于，从而进行等价无穷小的渐近分析．

𝑓(𝑛) =𝑜(𝑔(𝑛))f(n)=o(g(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当对于任意给定的正数 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，∃𝑛0∃n0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 ∀𝑛 ≥𝑛0,0 ≤𝑓(𝑛) <𝑐 ⋅𝑔(𝑛)∀n≥n0,0≤f(n)<c⋅g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 小 ω 符号

如果说 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 符号相当于大于等于号，那么 𝜔ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 符号就相当于大于号．

𝑓(𝑛) =𝜔(𝑔(𝑛))f(n)=ω(g(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当对于任意给定的正数 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，∃𝑛0∃n0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 ∀𝑛 ≥𝑛0,0 ≤𝑐 ⋅𝑔(𝑛) <𝑓(𝑛)∀n≥n0,0≤c⋅g(n)<f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

![](./images/order.png)

### 常见性质

  * 𝑓(𝑛) =Θ(𝑔(𝑛)) ⟺ 𝑓(𝑛) =𝑂(𝑔(𝑛)) ∧𝑓(𝑛) =Ω(𝑔(𝑛))f(n)=Θ(g(n))⟺f(n)=O(g(n))∧f(n)=Ω(g(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑓1(𝑛) +𝑓2(𝑛) =𝑂(max(𝑓1(𝑛),𝑓2(𝑛)))f1(n)+f2(n)=O(max(f1(n),f2(n)))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑓1(𝑛) ×𝑓2(𝑛) =𝑂(𝑓1(𝑛) ×𝑓2(𝑛))f1(n)×f2(n)=O(f1(n)×f2(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * ∀𝑎 ≠1,log𝑎⁡𝑛 =𝑂(log2⁡𝑛)∀a≠1,loga⁡n=O(log2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由换底公式可以得知，任何对数函数无论底数为何，都具有相同的增长率，因此渐近时间复杂度中对数的底数一般省略不写．

## 简单的时间复杂度计算的例子

### `for` 循环

C++PythonJava

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text int n , m ; std :: cin >> n >> m ; for ( int i = 0 ; i < n ; ++ i ) { for ( int j = 0 ; j < n ; ++ j ) { for ( int k = 0 ; k < m ; ++ k ) { std :: cout << "hello world \n " ; } } } ```   
---|---  
  
```text 1 2 3 4 5 6 ``` |  ```text n = int ( input ()) m = int ( input ()) for i in range ( 0 , n ): for j in range ( 0 , n ): for k in range ( 0 , m ): print ( "hello world" ) ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text int n , m ; n = input . nextInt (); m = input . nextInt (); for ( int i = 0 ; i < n ; ++ i ) { for ( int j = 0 ; j < n ; ++ j ) { for ( int k = 0 ; k < m ; ++ k ) { System . out . println ( "hello world" ); } } } ```   
---|---  
  
如果以输入的数值 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小作为数据规模，则上面这段代码的时间复杂度为 Θ(𝑛2𝑚)Θ(n2m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### DFS

在对一张 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边的图进行 [DFS](../../graph/dfs/) 时，由于每个节点和每条边都只会被访问常数次，复杂度为 Θ(𝑛 +𝑚)Θ(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 哪些量是常量？

当我们要进行若干次操作时，如何判断这若干次操作是否影响时间复杂度呢？例如：

C++PythonJava

```text 1 2 3 4 ``` |  ```text constexpr int N = 100000 ; for ( int i = 0 ; i < N ; ++ i ) { std :: cout << "hello world \n " ; } ```   
---|---  
  
```text 1 2 3 ``` |  ```text N = 100000 for i in range ( 0 , N ): print ( "hello world" ) ```   
---|---  
  
```text 1 2 3 4 ``` |  ```text final int N = 100000 ; for ( int i = 0 ; i < N ; ++ i ) { System . out . println ( "hello world" ); } ```   
---|---  
  
如果 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小不被看作输入规模，那么这段代码的时间复杂度就是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

进行时间复杂度计算时，哪些变量被视作输入规模是很重要的，而所有和输入规模无关的量都被视作常量，计算复杂度时可当作 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来处理．

需要注意的是，在进行时间复杂度相关的理论性讨论时，「算法能够解决任何规模的问题」是一个基本假设（当然，在实际中，由于时间和存储空间有限，无法解决规模过大的问题）．因此，能在常量时间内解决数据规模有限的问题（例如，对于数据范围内的每个可能输入预先计算出答案）并不能使一个算法的时间复杂度变为 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 主定理 (Master Theorem)

我们可以使用 Master Theorem 来快速求得关于递归算法的复杂度． Master Theorem 递推关系式如下

𝑇(𝑛)=𝑎𝑇(𝑛𝑏)+𝑓(𝑛)∀𝑛>𝑏T(n)=aT(nb)+f(n)∀n>b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么

𝑇(𝑛)=⎧{ {⎨{ {⎩Θ(𝑛log𝑏⁡𝑎)𝑓(𝑛)=𝑂(𝑛log𝑏⁡(𝑎)−𝜖),𝜖>0Θ(𝑓(𝑛))𝑓(𝑛)=Ω(𝑛log𝑏⁡(𝑎)+𝜖),𝜖≥0Θ(𝑛log𝑏⁡𝑎log𝑘+1⁡𝑛)𝑓(𝑛)=Θ(𝑛log𝑏⁡𝑎log𝑘⁡𝑛),𝑘≥0T(n)={Θ(nlogb⁡a)f(n)=O(nlogb⁡(a)−ϵ),ϵ>0Θ(f(n))f(n)=Ω(nlogb⁡(a)+ϵ),ϵ≥0Θ(nlogb⁡alogk+1⁡n)f(n)=Θ(nlogb⁡alogk⁡n),k≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

需要注意的是，这里的第二种情况还需要满足 regularity condition, 即 𝑎𝑓(𝑛/𝑏) ≤𝑐𝑓(𝑛)af(n/b)≤cf(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，for some constant 𝑐 <1c<1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) and sufficiently large 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明思路是是将规模为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的问题，分解为 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个规模为 (𝑛𝑏)(nb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的问题，然后依次合并，直到合并到最高层．每一次合并子问题，都需要花费 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间．

证明

依据上文提到的证明思路，具体证明过程如下

对于第 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层（最高层），合并子问题需要花费 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间

对于第 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层（第一次划分出来的子问题），共有 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个子问题，每个子问题合并需要花费 𝑓(𝑛𝑏)f(nb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间，所以合并总共要花费 𝑎𝑓(𝑛𝑏)af(nb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间．

层层递推，我们可以写出类推树如下：![](./images/master-theorem-proof.svg)

这棵树的高度为 log𝑏⁡𝑛logb⁡n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，共有 𝑛log𝑏⁡𝑎nlogb⁡a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个叶子，从而 𝑇(𝑛) =Θ(𝑛log𝑏⁡𝑎) +𝑔(𝑛)T(n)=Θ(nlogb⁡a)+g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑔(𝑛) =∑log𝑏⁡𝑛−1𝑗=0𝑎𝑗𝑓(𝑛/𝑏𝑗)g(n)=∑j=0logb⁡n−1ajf(n/bj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

针对于第一种情况：𝑓(𝑛) =𝑂(𝑛log𝑏⁡𝑎−𝜖)f(n)=O(nlogb⁡a−ϵ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此 𝑔(𝑛) =𝑂(𝑛log𝑏⁡𝑎)g(n)=O(nlogb⁡a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于第二种情况而言：首先 𝑔(𝑛) =Ω(𝑓(𝑛))g(n)=Ω(f(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，又因为 𝑎𝑓(𝑛𝑏) ≤𝑐𝑓(𝑛)af(nb)≤cf(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只要 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值是一个足够小的正数，且 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值足够大，因此可以推导出：𝑔(𝑛) =𝑂(𝑓(𝑛)g(n)=O(f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7))．两侧夹逼可以得出，𝑔(𝑛) =Θ(𝑓(𝑛))g(n)=Θ(f(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

而对于第三种情况：𝑓(𝑛) =Θ(𝑛log𝑏⁡𝑎)f(n)=Θ(nlogb⁡a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此 𝑔(𝑛) =𝑂(𝑛log𝑏⁡𝑎log⁡𝑛)g(n)=O(nlogb⁡alog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝑇(𝑛)T(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的结果可在 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得出后显然得到．

下面举几个例子来说明主定理如何使用．

  1. 𝑇(𝑛) =2𝑇(𝑛2) +1T(n)=2T(n2)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑎 =2,𝑏 =2,log2⁡2 =1a=2,b=2,log2⁡2=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝜖ϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以取值在 (0,1](0,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间，从而满足第一种情况，所以 𝑇(𝑛) =Θ(𝑛)T(n)=Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  2. 𝑇(𝑛) =𝑇(𝑛2) +𝑛T(n)=T(n2)+n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑎 =1,𝑏 =2,log2⁡1 =0a=1,b=2,log2⁡1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝜖ϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以取值在 (0,1](0,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间，从而满足第二种情况，所以 𝑇(𝑛) =Θ(𝑛)T(n)=Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  3. 𝑇(𝑛) =𝑇(𝑛2) +log⁡𝑛T(n)=T(n2)+log⁡n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑎 =1,𝑏 =2,log2⁡1 =0a=1,b=2,log2⁡1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以取值为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而满足第三种情况，所以 𝑇(𝑛) =Θ(log2⁡𝑛)T(n)=Θ(log2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  4. 𝑇(𝑛) =𝑇(𝑛2) +1T(n)=T(n2)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑎 =1,𝑏 =2,log2⁡1 =0a=1,b=2,log2⁡1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以取值为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而满足第三种情况，所以 𝑇(𝑛) =Θ(log⁡𝑛)T(n)=Θ(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 均摊复杂度

详情可见 [均摊复杂度](../amortized-analysis/)．

## 空间复杂度

类似地，算法所使用的空间随输入规模变化的趋势可以用 **空间复杂度** 来衡量．

## 计算复杂性

本文主要从算法分析的角度对复杂度进行了介绍，如果有兴趣的话可以在 [计算复杂性](../../misc/cc-basic/) 进行更深入的了解．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/basic/complexity.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/basic/complexity.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [ouuan](https://github.com/ouuan), [Enter-tainer](https://github.com/Enter-tainer), [GuanghaoYe](https://github.com/GuanghaoYe), [Persdre](https://github.com/Persdre), [Tiphereth-A](https://github.com/Tiphereth-A), [CCXXXI](https://github.com/CCXXXI), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [linehk](https://github.com/linehk), [shuzhouliu](https://github.com/shuzhouliu), [sshwy](https://github.com/sshwy), [abc1763613206](https://github.com/abc1763613206), [aquastripe](https://github.com/aquastripe), [Backl1ght](https://github.com/Backl1ght), [blackwhitetony](https://github.com/blackwhitetony), [c-forrest](https://github.com/c-forrest), [chinggg](https://github.com/chinggg), [ChungZH](https://github.com/ChungZH), [Enonya](https://github.com/Enonya), [GreyTigerOIer](https://github.com/GreyTigerOIer), [he-zhiyuan](https://github.com/he-zhiyuan), [isdanni](https://github.com/isdanni), [Konano](https://github.com/Konano), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [mgt](mailto:i@margatroid.xyz), [nullnan](https://github.com/nullnan), [onelittlechildawa](https://github.com/onelittlechildawa), [partychicken](https://github.com/partychicken), [persdre](https://github.com/persdre), [shawlleyw](https://github.com/shawlleyw), [TianyiQ](https://github.com/TianyiQ), [wr786](https://github.com/wr786), [Xeonacid](https://github.com/Xeonacid), [YHN-ice](https://github.com/YHN-ice), [yyyu-star](https://github.com/yyyu-star)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
