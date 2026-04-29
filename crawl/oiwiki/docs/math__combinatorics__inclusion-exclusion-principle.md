# 容斥原理 - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/inclusion-exclusion-principle/

# 容斥原理

## 引入

入门例题

假设班里有 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个学生喜欢数学，1515![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个学生喜欢语文，2121![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个学生喜欢编程，班里至少喜欢一门学科的有多少个学生呢？

是 10 +15 +21 =4610+15+21=46![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个吗？不是的，因为有些学生可能同时喜欢数学和语文，或者语文和编程，甚至还有可能三者都喜欢．

为了叙述方便，我们把喜欢语文、数学、编程的学生集合分别用 𝐴,𝐵,𝐶A,B,C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示，则学生总数等于 |𝐴 ∪𝐵 ∪𝐶||A∪B∪C|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．刚才已经讲过，如果把这三个集合的元素个数 |𝐴|,|𝐵|,|𝐶||A|,|B|,|C|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 直接加起来，会有一些元素重复统计了，因此需要扣掉 |𝐴 ∩𝐵|,|𝐵 ∩𝐶|,|𝐶 ∩𝐴||A∩B|,|B∩C|,|C∩A|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但这样一来，又有一小部分多扣了，需要加回来，即 |𝐴 ∩𝐵 ∩𝐶||A∩B∩C|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．即

|𝐴∪𝐵∪𝐶|=|𝐴|+|𝐵|+|𝐶|−|𝐴∩𝐵|−|𝐵∩𝐶|−|𝐶∩𝐴|+|𝐴∩𝐵∩𝐶||A∪B∪C|=|A|+|B|+|C|−|A∩B|−|B∩C|−|C∩A|+|A∩B∩C|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

![容斥原理 - venn 图示例](./images/incexcp.png)

把上述问题推广到一般情况，就是我们熟知的容斥原理．

## 定义

设 U 中元素有 n 种不同的属性，而第 i 种属性称为 𝑃𝑖Pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，拥有属性 𝑃𝑖Pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素构成集合 𝑆𝑖Si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么

∣𝑛⋃𝑖=1𝑆𝑖∣=∑𝑖|𝑆𝑖|−∑𝑖<𝑗|𝑆𝑖∩𝑆𝑗|+∑𝑖<𝑗<𝑘|𝑆𝑖∩𝑆𝑗∩𝑆𝑘|−⋯+(−1)𝑚−1∑𝑎𝑖<𝑎𝑖+1∣𝑚⋂𝑖=1𝑆𝑎𝑖∣+⋯+(−1)𝑛−1|𝑆1∩⋯∩𝑆𝑛||⋃i=1nSi|=∑i|Si|−∑i<j|Si∩Sj|+∑i<j<k|Si∩Sj∩Sk|−⋯+(−1)m−1∑ai<ai+1|⋂i=1mSai|+⋯+(−1)n−1|S1∩⋯∩Sn|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即

∣𝑛⋃𝑖=1𝑆𝑖∣=𝑛∑𝑚=1(−1)𝑚−1∑𝑎𝑖<𝑎𝑖+1∣𝑚⋂𝑖=1𝑆𝑎𝑖∣|⋃i=1nSi|=∑m=1n(−1)m−1∑ai<ai+1|⋂i=1mSai|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 证明

对于每个元素使用二项式定理计算其出现的次数．对于元素 x，假设它出现在 𝑇1,𝑇2,⋯,𝑇𝑚T1,T2,⋯,Tm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的集合中，那么它的出现次数为

𝐶𝑛𝑡=|{𝑇𝑖}|−|{𝑇𝑖∩𝑇𝑗|𝑖<𝑗}|+⋯+(−1)𝑘−1∣{𝑘⋂𝑖=1𝑇𝑎𝑖|𝑎𝑖<𝑎𝑖+1}∣+⋯+(−1)𝑚−1|{𝑇1∩⋯∩𝑇𝑚}|=(𝑚1)−(𝑚2)+⋯+(−1)𝑚−1(𝑚𝑚)=(𝑚0)−𝑚∑𝑖=0(−1)𝑖(𝑚𝑖)=1−(1−1)𝑚=1Cnt=|{Ti}|−|{Ti∩Tj|i<j}|+⋯+(−1)k−1|{⋂i=1kTai|ai<ai+1}|+⋯+(−1)m−1|{T1∩⋯∩Tm}|=(m1)−(m2)+⋯+(−1)m−1(mm)=(m0)−∑i=0m(−1)i(mi)=1−(1−1)m=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是每个元素出现的次数为 1，那么合并起来就是并集．证毕．

### 补集

对于全集 U 下的 **集合的并** 可以使用容斥原理计算，而集合的交则用全集减去 **补集的并集** 求得：

∣𝑛⋂𝑖=1𝑆𝑖∣=|𝑈|−∣𝑛⋃𝑖=1――𝑆𝑖∣|⋂i=1nSi|=|U|−|⋃i=1nSi―|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

右边使用容斥即可．

可能接触过容斥的读者都清楚上述内容，而更关心的是容斥的应用．

那么接下来我们给出 3 个层次不同的例题来为大家展示容斥原理的应用．

## 不定方程非负整数解计数

不定方程非负整数解计数

给出不定方程 ∑𝑛𝑖=1𝑥𝑖 =𝑚∑i=1nxi=m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个限制条件 𝑥𝑖 ≤𝑏𝑖xi≤bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑚,𝑏𝑖 ∈ℕm,bi∈N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 求方程的非负整数解的个数．

### 没有限制时

如果没有 𝑥𝑖 ≤𝑏𝑖xi≤bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的限制，那么不定方程 ∑𝑛𝑖=1𝑥𝑖 =𝑚∑i=1nxi=m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非负整数解的数目为 (𝑚+𝑛−1𝑛−1)(m+n−1n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

略证：插板法．

相当于你有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个球要分给 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个盒子，允许某个盒子是空的．这个问题不能直接用组合数解决．

于是我们再加入 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个球，于是问题就变成了在一个长度为 𝑚 +𝑛 −1m+n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的球序列中选择 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个球，然后这个 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个球把这个序列隔成了 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 份，恰好可以一一对应放到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个盒子中．那么在 𝑚 +𝑛 −1m+n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个球中选择 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个球的方案数就是 (𝑚+𝑛−1𝑛−1)(m+n−1n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 容斥模型

接着我们尝试抽象出容斥原理的模型：

  1. 全集 U：不定方程 ∑𝑛𝑖=1𝑥𝑖 =𝑚∑i=1nxi=m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非负整数解
  2. 元素：变量 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).
  3. 属性：𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的属性即 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足的条件，即 𝑥𝑖 ≤𝑏𝑖xi≤bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的条件

目标：所有变量满足对应属性时集合的大小，即 |⋂𝑛𝑖=1𝑆𝑖||⋂i=1nSi|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

这个东西可以用 |⋂𝑛𝑖=1𝑆𝑖| =|𝑈| −∣⋃𝑛𝑖=1――𝑆𝑖∣|⋂i=1nSi|=|U|−|⋃i=1nSi―|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求解．|𝑈||U|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以用组合数计算，后半部分自然使用容斥原理展开．

那么问题变成，对于一些 ―――𝑆𝑎𝑖Sai―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的交集求大小．考虑 ―――𝑆𝑎𝑖Sai―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的含义，表示 𝑥𝑎𝑖 ≥𝑏𝑎𝑖 +1xai≥bai+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解的数目．而交集表示同时满足这些条件．因此这个交集对应的不定方程中，有些变量有 **下界限制** ，而有些则没有限制．

能否消除这些下界限制呢？既然要求的是非负整数解，而有些变量的下界又大于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么我们直接 **把这个下界减掉** ，就可以使得这些变量的下界变成 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即没有下界啦．因此对于

∣1≤𝑖≤𝑘⋂𝑎𝑖<𝑎𝑖+1𝑆𝑎𝑖∣|⋂ai<ai+11≤i≤kSai|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的不定方程形式为

𝑛∑𝑖=1𝑥𝑖=𝑚−𝑘∑𝑖=1(𝑏𝑎𝑖+1)∑i=1nxi=m−∑i=1k(bai+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是这个也可以组合数计算啦．这个长度为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组相当于在枚举子集．

## HAOI2008 硬币购物

HAOI2008 硬币购物

4 种面值的硬币，第 i 种的面值是 𝐶𝑖Ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次询问，每次询问给出每种硬币的数量 𝐷𝑖Di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和一个价格 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，问付款方式．

𝑛 ≤103,𝑆 ≤105n≤103,S≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

如果用背包做的话复杂度是 𝑂(4𝑛𝑆)O(4nS)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，无法承受．这道题最明显的特点就是硬币一共只有四种．抽象模型，其实就是让我们求方程 ∑4𝑖=1𝐶𝑖𝑥𝑖 =𝑆,𝑥𝑖 ≤𝐷𝑖∑i=14Cixi=S,xi≤Di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非负整数解的个数．

采用同样的容斥方式，𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的属性为 𝑥𝑖 ≤𝐷𝑖xi≤Di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 套用容斥原理的公式，最后我们要求解

4∑𝑖=1𝐶𝑖𝑥𝑖=𝑆−𝑘∑𝑖=1𝐶𝑎𝑖(𝐷𝑎𝑖+1)∑i=14Cixi=S−∑i=1kCai(Dai+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是无限背包问题．这个问题可以预处理，算上询问，总复杂度 𝑂(4𝑆 +24𝑛)O(4S+24n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

代码实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` |  ```text #include <iostream> using namespace std ; constexpr long long S = 1e5 \+ 5 ; long long c [ 5 ], d [ 5 ], n , s ; long long f [ S ]; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> c [ 1 ] >> c [ 2 ] >> c [ 3 ] >> c [ 4 ] >> n ; f [ 0 ] = 1 ; for ( long long j = 1 ; j <= 4 ; j ++ ) for ( long long i = 1 ; i < S ; i ++ ) if ( i >= c [ j ]) f [ i ] += f [ i \- c [ j ]]; // f[i]：价格为i时的硬币组成方法数 for ( long long k = 1 ; k <= n ; k ++ ) { cin >> d [ 1 ] >> d [ 2 ] >> d [ 3 ] >> d [ 4 ] >> s ; long long ans = 0 ; for ( long long i = 1 ; i < 16 ; i ++ ) { // 容斥，因为物品一共有4种，所以从1到2^4-1=15循环 long long m = s , bit = 0 ; for ( long long j = 1 ; j <= 4 ; j ++ ) { if (( i >> ( j \- 1 )) % 2 == 1 ) { m -= ( d [ j ] \+ 1 ) * c [ j ]; bit ++ ; } } if ( m >= 0 ) ans += ( bit % 2 * 2 \- 1 ) * f [ m ]; } cout << f [ s ] \- ans << '\n' ; } return 0 ; } ```   
---|---  
  
## 完全图子图染色问题

前面的三道题都是容斥原理的正向运用，这道题则需要用到容斥原理逆向分析．

完全图子图染色问题

A 和 B 喜欢对图（不一定连通）进行染色，而他们的规则是，相邻的结点必须染同一种颜色．今天 A 和 B 玩游戏，对于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶 **完全图** 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．他们定义一个估价函数 𝐹(𝑆)F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 S 是边集，𝑆 ⊆𝐸S⊆E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).𝐹(𝑆)F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值是对图 𝐺′ =(𝑉,𝑆)G′=(V,S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 用 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种颜色染色的总方案数．他们的另一个规则是，如果 |𝑆||S|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇数，那么 A 的得分增加 𝐹(𝑆)F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，否则 B 的得分增加 𝐹(𝑆)F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 问 A 和 B 的得分差值．

### 数学形式

一看这道题的算法趋向并不明显，因此对于棘手的题目首先抽象出数学形式．得分差即为奇偶对称差，可以用 -1 的幂次来作为系数．我们求的是

𝐴𝑛𝑠=∑𝑆⊆𝐸(−1)|𝑆|−1𝐹(𝑆)Ans=∑S⊆E(−1)|S|−1F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 容斥模型

相邻结点染同一种颜色，我们把它当作属性．在这里我们先不遵守染色的规则，假定我们用 m 种颜色直接对图染色．对于图 𝐺′ =(𝑉,𝑆)G′=(V,S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们把它当作 **元素** ．**属性** 𝑥𝑖 =𝑥𝑗xi=xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的含义是结点 i,j 染同色（注意，并未要求 i,j 之间有连边）．

而属性 𝑥𝑖 =𝑥𝑗xi=xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的 **集合** 定义为 𝑄𝑖,𝑗Qi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其含义是所有满足该属性的图 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的染色方案，集合的大小就是满足该属性的染色方案数，集合内的元素相当于所有满足该属性的图 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的染色图．

回到题目，「相邻的结点必须染同一种颜色」，可以理解为若干个 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 集合的交集．因此可以写出

𝐹(𝑆)=∣⋂(𝑖,𝑗)∈𝑆𝑄𝑖,𝑗∣F(S)=|⋂(i,j)∈SQi,j|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

上述式子右边的含义就是说对于 S 内的每一条边 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都满足 𝑥𝑖 =𝑥𝑗xi=xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的染色方案数，也就是 𝐹(𝑆)F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

是不是很有容斥的味道了？由于容斥原理本身没有二元组的形式，因此我们把 **所有** 的边 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 映射到 𝑇 =𝑛(𝑛+1)2T=n(n+1)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数上，假设将 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 映射为 𝑘,1 ≤𝑘 ≤𝑇k,1≤k≤T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，同时 𝑄𝑖,𝑗Qi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 映射为 𝑄𝑘Qk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 那么属性 𝑥𝑖 =𝑥𝑗xi=xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则定义为 𝑃𝑘Pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

同时 S 可以表示为若干个 k 组成的集合，即 𝑆 ⟺ 𝐾 ={𝑘1,𝑘2,⋯,𝑘𝑚}S⟺K={k1,k2,⋯,km}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).（也就是说我们在边集与数集间建立了等价关系）．

而 E 对应集合 𝑀 ={1,2,⋯,𝑛(𝑛+1)2}M={1,2,⋯,n(n+1)2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 于是乎

𝐹(𝑆)⟺𝐹({𝑘𝑖})=∣⋂𝑘𝑖𝑄𝑘𝑖∣F(S)⟺F({ki})=|⋂kiQki|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 逆向分析

那么要求的式子展开

𝐴𝑛𝑠=∑𝐾⊆𝑀(−1)|𝐾|−1∣⋂𝑘𝑖∈𝐾𝑄𝑘𝑖∣=∑𝑖|𝑄𝑖|−∑𝑖<𝑗|𝑄𝑖∩𝑄𝑗|+∑𝑖<𝑗<𝑘|𝑄𝑖∩𝑄𝑗∩𝑄𝑘|−⋯+(−1)𝑇−1∣𝑇⋂𝑖=1𝑄𝑖∣Ans=∑K⊆M(−1)|K|−1|⋂ki∈KQki|=∑i|Qi|−∑i<j|Qi∩Qj|+∑i<j<k|Qi∩Qj∩Qk|−⋯+(−1)T−1|⋂i=1TQi|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是就出现了容斥原理的展开形式，因此对这个式子逆向推导

𝐴𝑛𝑠=∣𝑇⋃𝑖=1𝑄𝑖∣Ans=|⋃i=1TQi|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再考虑等式右边的含义，只要满足 1 ∼𝑇1∼T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 任一条件即可，也就是存在两个点同色（不一定相邻）的染色方案数！而我们知道染色方案的全集是 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，显然 |𝑈| =𝑚𝑛|U|=mn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 而转化为补集，就是求两两异色的染色方案数，即 𝐴𝑛𝑚 =𝑚!(𝑚−𝑛)!Amn=m!(m−n)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 因此

𝐴𝑛𝑠=𝑚𝑛−𝐴𝑛𝑚Ans=mn−Amn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

解决这道题，我们首先抽象出题目数学形式，然后从题目中信息量最大的条件，𝐹(𝑆)F(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 函数的定义入手，将其转化为集合的交并补．然后将式子转化为容斥原理的形式，并 **逆向推导** 出最终的结果．这道题体现的正是容斥原理的逆用．

## 数论中的容斥

使用容斥原理能够巧妙地求解一些数论问题．

### 容斥原理求最大公约数为 k 的数对个数

考虑下面的问题：

求最大公约数为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数对个数

设 1 ≤𝑥,𝑦 ≤𝑁1≤x,y≤N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑓(𝑘)f(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示最大公约数为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有序数对 (𝑥,𝑦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数，求 𝑓(1)f(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑓(𝑁)f(N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

这道题固然可以用欧拉函数或莫比乌斯反演的方法来做，但是都不如用容斥原理来的简单．

由容斥原理可以得知，先找到所有以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **公约数** 的数对，再从中剔除所有以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数为 **公约数** 的数对，余下的数对就是以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **最大公约数** 的数对．即 𝑓(𝑘) =f(k)=![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **公约数** 的数对个数 −−![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数为 **公约数** 的数对个数．

进一步可发现，以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数为 **公约数** 的数对个数等于所有以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数为 **最大公约数** 的数对个数之和．于是，可以写出如下表达式：

𝑓(𝑘)=⌊(𝑁/𝑘)⌋2−𝑖∗𝑘≤𝑁∑𝑖=2𝑓(𝑖∗𝑘)f(k)=⌊(N/k)⌋2−∑i=2i∗k≤Nf(i∗k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于当 𝑘 >𝑁/2k>N/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，我们可以直接算出 𝑓(𝑘) =⌊(𝑁/𝑘)⌋2f(k)=⌊(N/k)⌋2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此我们可以倒过来，从 𝑓(𝑁)f(N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 算到 𝑓(1)f(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就可以了．于是，我们使用容斥原理完成了本题．

```text 1 2 3 4 ``` |  ```text for ( long long k = N ; k >= 1 ; k \-- ) { f [ k ] = ( N / k ) * ( N / k ); for ( long long i = k \+ k ; i <= N ; i += k ) f [ k ] -= f [ i ]; } ```   
---|---  
  
上述方法的时间复杂度为 𝑂(∑𝑁𝑖=1𝑁/𝑖) =𝑂(𝑁∑𝑁𝑖=11/𝑖) =𝑂(𝑁log⁡𝑁)O(∑i=1NN/i)=O(N∑i=1N1/i)=O(Nlog⁡N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

附赠三倍经验供大家练手．

  * [Luogu P2398 GCD SUM](https://www.luogu.com.cn/problem/P2398)
  * [Luogu P2158[SDOI2008] 仪仗队](https://www.luogu.com.cn/problem/P2158)
  * [Luogu P1447[NOI2010] 能量采集](https://www.luogu.com.cn/problem/P1447)

### 容斥原理推导欧拉函数

考虑下面的问题：

欧拉函数公式

求欧拉函数 𝜑(𝑛)φ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．其中 𝜑(𝑛) =|{1 ≤𝑥 ≤𝑛|gcd(𝑥,𝑛) =1}|φ(n)=|{1≤x≤n|gcd(x,n)=1}|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

直接计算是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，用线性筛是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，杜教筛是 𝑂(𝑛23)O(n23)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的（话说一道数论入门题用容斥做为什么还要扯到杜教筛上），接下来考虑用容斥推出欧拉函数的公式

判断两个数是否互质，首先分解质因数

𝑛=𝑘∏𝑖=1𝑝𝑖𝑐𝑖n=∏i=1kpici![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么就要求对于任意 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都不是 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数，即 𝑝𝑖 ∤𝑥pi∤x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 把它当作属性，对应的集合为 𝑆𝑖Si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此有

𝜑(𝑛)=∣𝑘⋂𝑖=1𝑆𝑖∣=|𝑈|−∣𝑘⋃𝑖=1――𝑆𝑖∣φ(n)=|⋂i=1kSi|=|U|−|⋃i=1kSi―|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

全集大小 |𝑈| =𝑛|U|=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而 ――𝑆𝑖Si―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示的是 𝑝𝑖 ∣𝑥pi∣x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成的集合，显然 |――𝑆𝑖| =𝑛𝑝𝑖|Si―|=npi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并由此推出

∣⋂𝑎𝑖<𝑎𝑖+1𝑆𝑎𝑖∣=𝑛∏𝑝𝑎𝑖|⋂ai<ai+1Sai|=n∏pai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此可得

𝜑(𝑛)=𝑛−∑𝑖𝑛𝑝𝑖+∑𝑖<𝑗𝑛𝑝𝑖𝑝𝑗−⋯+(−1)𝑘𝑛𝑝1𝑝2⋯𝑝𝑘=𝑛(1−1𝑝1)(1−1𝑝2)⋯(1−1𝑝𝑘)=𝑛𝑘∏𝑖=1(1−1𝑝𝑖)φ(n)=n−∑inpi+∑i<jnpipj−⋯+(−1)knp1p2⋯pk=n(1−1p1)(1−1p2)⋯(1−1pk)=n∏i=1k(1−1pi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就是欧拉函数的数学表示啦

## 容斥原理一般化

容斥原理常用于集合的计数问题，而对于两个集合的函数 𝑓(𝑆),𝑔(𝑆)f(S),g(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若

𝑓(𝑆)=∑𝑇⊆𝑆𝑔(𝑇)f(S)=∑T⊆Sg(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么就有

𝑔(𝑆)=∑𝑇⊆𝑆(−1)|𝑆|−|𝑇|𝑓(𝑇)g(S)=∑T⊆S(−1)|S|−|T|f(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 证明

接下来我们简单证明一下．我们从等式的右边开始推：

∑𝑇⊆𝑆(−1)|𝑆|−|𝑇|𝑓(𝑇)=∑𝑇⊆𝑆(−1)|𝑆|−|𝑇|∑𝑄⊆𝑇𝑔(𝑄)=∑𝑄𝑔(𝑄)∑𝑄⊆𝑇⊆𝑆(−1)|𝑆|−|𝑇|∑T⊆S(−1)|S|−|T|f(T)=∑T⊆S(−1)|S|−|T|∑Q⊆Tg(Q)=∑Qg(Q)∑Q⊆T⊆S(−1)|S|−|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们发现后半部分的求和与 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 无关，因此把后半部分的 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 剔除：

=∑𝑄𝑔(𝑄)∑𝑇⊆(𝑆∖𝑄)(−1)|𝑆∖𝑄|−|𝑇|=∑Qg(Q)∑T⊆(S∖Q)(−1)|S∖Q|−|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

记关于集合 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的函数 𝐹(𝑃) =∑𝑇⊆𝑃( −1)|𝑃|−|𝑇|F(P)=∑T⊆P(−1)|P|−|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并化简这个函数：

𝐹(𝑃)=∑𝑇⊆𝑃(−1)|𝑃|−|𝑇|=|𝑃|∑𝑖=0(|𝑃|𝑖)(−1)|𝑃|−𝑖=|𝑃|∑𝑖=0(|𝑃|𝑖)1𝑖(−1)|𝑃|−𝑖=(1−1)|𝑃|=0|𝑃|F(P)=∑T⊆P(−1)|P|−|T|=∑i=0|P|(|P|i)(−1)|P|−i=∑i=0|P|(|P|i)1i(−1)|P|−i=(1−1)|P|=0|P|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此原来的式子的值是

∑𝑄𝑔(𝑄)∑𝑇⊆(𝑆∖𝑄)(−1)|𝑆∖𝑄|−|𝑇|=∑𝑄𝑔(𝑄)𝐹(𝑆∖𝑄)=∑𝑄𝑔(𝑄)⋅0|𝑆∖𝑄|∑Qg(Q)∑T⊆(S∖Q)(−1)|S∖Q|−|T|=∑Qg(Q)F(S∖Q)=∑Qg(Q)⋅0|S∖Q|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

分析发现，仅当 |𝑆 ∖𝑄| =0|S∖Q|=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时有 00 =100=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这时 𝑄 =𝑆Q=S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，对答案的贡献就是 𝑔(𝑆)g(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其他时侯 0|𝑆∖𝑄| =00|S∖Q|=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则对答案无贡献．于是得到

∑𝑄𝑔(𝑄)⋅0|𝑆∖𝑄|=𝑔(𝑆)∑Qg(Q)⋅0|S∖Q|=g(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

综上所述，得证．

### 推论

该形式还有这样一个推论．在全集 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下，对于函数 𝑓(𝑆),𝑔(𝑆)f(S),g(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果

𝑓(𝑆)=∑𝑆⊆𝑇𝑔(𝑇)f(S)=∑S⊆Tg(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么

𝑔(𝑆)=∑𝑆⊆𝑇(−1)|𝑇|−|𝑆|𝑓(𝑇)g(S)=∑S⊆T(−1)|T|−|S|f(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这个推论其实就是补集形式，证法类似．

## DAG 计数

DAG 计数

对 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点带标号的有向无环图进行计数，对 109 +7109+7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模．𝑛 ≤5 ×103n≤5×103![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 直接 DP

考虑 DP，定义 𝑓[𝑖,𝑗]f[i,j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点的 DAG，有 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点个入度为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的图的个数．假设去掉这 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点后，有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点入度为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么在去掉前这 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点至少与这 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点中的某几个有连边，即 2𝑗 −12j−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种情况；而这 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点除了与 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点连边，还可以与剩下的点任意连边，有 2𝑖−𝑗−𝑘2i−j−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种情况．因此方程如下：

𝑓[𝑖,𝑗]=(𝑖𝑗)𝑖−𝑗∑𝑘=1(2𝑗−1)𝑘2(𝑖−𝑗−𝑘)𝑗𝑓[𝑖−𝑗,𝑘]f[i,j]=(ij)∑k=1i−j(2j−1)k2(i−j−k)jf[i−j,k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

计算上式的复杂度是 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

### 放宽限制

上述 DP 的定义是恰好 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点入度为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 太过于严格，可以放宽为至少 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点入度为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．直接定义 𝑓[𝑖]f[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点的 DAG 个数．可以直接容斥．考虑选出的 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点，这 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点可以和剩下的 𝑖 −𝑗i−j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点有任意的连边，即 (2𝑖−𝑗)𝑗 =2(𝑖−𝑗)𝑗(2i−j)j=2(i−j)j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种情况：

𝑓[𝑖]=𝑖∑𝑗=1(−1)𝑗−1(𝑖𝑗)2(𝑖−𝑗)𝑗𝑓[𝑖−𝑗]f[i]=∑j=1i(−1)j−1(ij)2(i−j)jf[i−j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

计算上式的复杂度是 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

## Min-max 容斥

对于满足 [全序](../../order-theory/#偏序集) 关系并且其中元素满足可加减性的序列 {𝑥𝑖}{xi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设其长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并设 𝑆 ={1,2,3,⋯,𝑛}S={1,2,3,⋯,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有：

max𝑖∈𝑆𝑥𝑖=∑𝑇⊆𝑆(−1)|𝑇|−1min𝑗∈𝑇𝑥𝑗maxi∈Sxi=∑T⊆S(−1)|T|−1minj∈Txj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)min𝑖∈𝑆𝑥𝑖=∑𝑇⊆𝑆(−1)|𝑇|−1max𝑗∈𝑇𝑥𝑗mini∈Sxi=∑T⊆S(−1)|T|−1maxj∈Txj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**证明：** 考虑做一个到一般容斥原理的映射．对于 𝑥 ∈𝑆x∈S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，假设 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小的元素．那么我们定义一个映射 𝑓 :𝑥 ↦{1,2,⋯,𝑘}f:x↦{1,2,⋯,k}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．显然这是一个双射．

那么容易发现，对于 𝑥,𝑦 ∈𝑆x,y∈S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑓(min(𝑥,𝑦)) =𝑓(𝑥) ∩𝑓(𝑦)f(min(x,y))=f(x)∩f(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑓(max(𝑥,𝑦)) =𝑓(𝑥) ∪𝑓(𝑦)f(max(x,y))=f(x)∪f(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此我们得到：

∣𝑓(max𝑖∈𝑆𝑥𝑖)∣=∣⋃𝑖∈𝑆𝑓(𝑥𝑖)∣=∑𝑇⊆𝑆(−1)|𝑇|−1∣⋂𝑗∈𝑇𝑓(𝑥𝑗)∣=∑𝑇⊆𝑆(−1)|𝑇|−1∣𝑓(min𝑗∈𝑇𝑥𝑗)∣|f(maxi∈Sxi)|=|⋃i∈Sf(xi)|=∑T⊆S(−1)|T|−1|⋂j∈Tf(xj)|=∑T⊆S(−1)|T|−1|f(minj∈Txj)|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

然后再把 |𝑓(max𝑖∈𝑆𝑥𝑖)||f(maxi∈Sxi)|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 映射回 max𝑖∈𝑆𝑥𝑖maxi∈Sxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而 minmin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是类似的．

证毕．

但是你可能觉得这个式子非常蠢，最大值明明可以直接求．之所以 min-max 容斥这么重要，是因为它在期望上也是成立的，即：

𝐸(max𝑖∈𝑆𝑥𝑖)=∑𝑇⊆𝑆(−1)|𝑇|−1𝐸(min𝑗∈𝑇𝑥𝑗)E(maxi∈Sxi)=∑T⊆S(−1)|T|−1E(minj∈Txj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝐸(min𝑖∈𝑆𝑥𝑖)=∑𝑇⊆𝑆(−1)|𝑇|−1𝐸(max𝑗∈𝑇𝑥𝑗)E(mini∈Sxi)=∑T⊆S(−1)|T|−1E(maxj∈Txj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**证明：** 我们考虑计算期望的一种方法：

𝐸(max𝑖∈𝑆𝑥𝑖)=∑𝑦𝑃(𝑦=𝑥)max𝑗∈𝑆𝑦𝑗E(maxi∈Sxi)=∑yP(y=x)maxj∈Syj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列．

我们对后面的 maxmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使用之前的式子：

𝐸(max𝑖∈𝑆𝑥𝑖)=∑𝑦𝑃(𝑦=𝑥)max𝑗∈𝑆𝑦𝑗=∑𝑦𝑃(𝑦=𝑥)∑𝑇⊆𝑆(−1)|𝑇|−1min𝑗∈𝑇𝑦𝑗E(maxi∈Sxi)=∑yP(y=x)maxj∈Syj=∑yP(y=x)∑T⊆S(−1)|T|−1minj∈Tyj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

调换求和顺序：

𝐸(max𝑖∈𝑆𝑥𝑖)=∑𝑦𝑃(𝑦=𝑥)∑𝑇⊆𝑆(−1)|𝑇|−1min𝑗∈𝑇𝑦𝑗=∑𝑇⊆𝑆(−1)|𝑇|−1∑𝑦𝑃(𝑦=𝑥)min𝑗∈𝑇𝑦𝑗=∑𝑇⊆𝑆(−1)|𝑇|−1𝐸(min𝑗∈𝑇𝑦𝑗)E(maxi∈Sxi)=∑yP(y=x)∑T⊆S(−1)|T|−1minj∈Tyj=∑T⊆S(−1)|T|−1∑yP(y=x)minj∈Tyj=∑T⊆S(−1)|T|−1E(minj∈Tyj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

minmin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是类似的．

证毕．

还有更强的：

kthmax⁡𝑥𝑖𝑖∈𝑆=∑𝑇⊆𝑆(−1)|𝑇|−𝑘(|𝑇|−1𝑘−1)min𝑗∈𝑇𝑥𝑗kthmax⁡xii∈S=∑T⊆S(−1)|T|−k(|T|−1k−1)minj∈Txj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)kthmin⁡𝑥𝑖𝑖∈𝑆=∑𝑇⊆𝑆(−1)|𝑇|−𝑘(|𝑇|−1𝑘−1)max𝑗∈𝑇𝑥𝑗kthmin⁡xii∈S=∑T⊆S(−1)|T|−k(|T|−1k−1)maxj∈Txj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝐸(kthmax⁡𝑥𝑖𝑖∈𝑆)=∑𝑇⊆𝑆(−1)|𝑇|−𝑘(|𝑇|−1𝑘−1)𝐸(min𝑗∈𝑇𝑥𝑗)E(kthmax⁡xii∈S)=∑T⊆S(−1)|T|−k(|T|−1k−1)E(minj∈Txj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝐸(kthmin⁡𝑥𝑖𝑖∈𝑆)=∑𝑇⊆𝑆(−1)|𝑇|−𝑘(|𝑇|−1𝑘−1)𝐸(max𝑗∈𝑇𝑥𝑗)E(kthmin⁡xii∈S)=∑T⊆S(−1)|T|−k(|T|−1k−1)E(maxj∈Txj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

规定若 𝑛 <𝑚n<m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 (𝑛𝑚) =0(nm)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**证明：** 不妨设 ∀1 ≤𝑖 <𝑛,𝑥𝑖 ≤𝑥𝑖+1∀1≤i<n,xi≤xi+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．则有：

∑𝑇⊆𝑆(−1)|𝑇|−𝑘(|𝑇|−1𝑘−1)min𝑗∈𝑇𝑥𝑗=∑𝑖∈𝑆𝑥𝑖∑𝑇⊆𝑆(−1)|𝑇|−𝑘(|𝑇|−1𝑘−1)[𝑥𝑖=min𝑗∈𝑇𝑥𝑗]=∑𝑖∈𝑆𝑥𝑖𝑛∑𝑗=𝑘(𝑛−𝑖𝑗−1)(𝑗−1𝑘−1)(−1)𝑗−𝑘∑T⊆S(−1)|T|−k(|T|−1k−1)minj∈Txj=∑i∈Sxi∑T⊆S(−1)|T|−k(|T|−1k−1)[xi=minj∈Txj]=∑i∈Sxi∑j=kn(n−ij−1)(j−1k−1)(−1)j−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

又因为有组合恒等式：(𝑎𝑏)(𝑏𝑐) =(𝑎𝑐)(𝑎−𝑐𝑏−𝑐)(ab)(bc)=(ac)(a−cb−c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以有：

∑𝑇⊆𝑆(−1)|𝑇|−𝑘(|𝑇|−1𝑘−1)min𝑗∈𝑇𝑥𝑗=∑𝑖∈𝑆𝑥𝑖𝑛∑𝑗=𝑘(𝑛−𝑖𝑗−1)(𝑗−1𝑘−1)(−1)𝑗−𝑘=∑𝑖∈𝑆𝑥𝑖𝑛∑𝑗=𝑘(𝑛−𝑖𝑘−1)(𝑛−𝑖−𝑘+1𝑗−𝑘)(−1)𝑗−𝑘=∑𝑖∈𝑆(𝑛−𝑖𝑘−1)𝑥𝑖𝑛∑𝑗=𝑘(𝑛−𝑖−𝑘+1𝑗−𝑘)(−1)𝑗−𝑘=∑𝑖∈𝑆(𝑛−𝑖𝑘−1)𝑥𝑖𝑛−𝑖−𝑘+1∑𝑗=0(𝑛−𝑖−𝑘+1𝑗)(−1)𝑗∑T⊆S(−1)|T|−k(|T|−1k−1)minj∈Txj=∑i∈Sxi∑j=kn(n−ij−1)(j−1k−1)(−1)j−k=∑i∈Sxi∑j=kn(n−ik−1)(n−i−k+1j−k)(−1)j−k=∑i∈S(n−ik−1)xi∑j=kn(n−i−k+1j−k)(−1)j−k=∑i∈S(n−ik−1)xi∑j=0n−i−k+1(n−i−k+1j)(−1)j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当 𝑖 =𝑛 −𝑘 +1i=n−k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时：

(𝑛−𝑖𝑘−1)𝑛−𝑖−𝑘+1∑𝑗=0(𝑛−𝑖−𝑘+1𝑗)(−1)𝑗=1(n−ik−1)∑j=0n−i−k+1(n−i−k+1j)(−1)j=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

否则：

(𝑛−𝑖𝑘−1)𝑛−𝑖−𝑘+1∑𝑗=0(𝑛−𝑖−𝑘+1𝑗)(−1)𝑗=0(n−ik−1)∑j=0n−i−k+1(n−i−k+1j)(−1)j=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以：

∑𝑖∈𝑆(𝑛−𝑖𝑘−1)𝑥𝑖𝑛−𝑖−𝑘+1∑𝑗=0(𝑛−𝑖−𝑘+1𝑗)(−1)𝑗=kthmax𝑖∈𝑆𝑥𝑖∑i∈S(n−ik−1)xi∑j=0n−i−k+1(n−i−k+1j)(−1)j=kthmaxi∈Sxi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

剩下三个是类似的．

证毕．

根据 min-max 容斥，我们还可以得到下面的式子：

lcm𝑖∈𝑆𝑥𝑖=∏𝑇⊆𝑆(gcd𝑗∈𝑇𝑥𝑗)(−1)|𝑇|−1lcmi∈Sxi=∏T⊆S(gcdj∈Txj)(−1)|T|−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 lcm,gcd,𝑎1,𝑎−1lcm,gcd,a1,a−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别相当于 max,min, +, −max,min,+,−![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就是说相当于对于指数做了一个 min-max 容斥，自然就是对的了

## PKUWC2018 随机游走

[PKUWC2018 随机游走](https://loj.ac/problem/2542)

给定一棵 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点的树，你从 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发，每次等概率随机选择一条与所在点相邻的边走过去．

有 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次询问．每次询问给出一个集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求如果从 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发一直随机游走，直到点集 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的点都至少经过一次的话，期望游走几步．

特别地，点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即起点）视为一开始就被经过了一次．

对 998244353998244353![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模．

1 ≤𝑛 ≤18,1 ≤𝑄 ≤5000,1 ≤|𝑆| ≤𝑛1≤n≤18,1≤Q≤5000,1≤|S|≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

期望游走的步数也就是游走的时间．那么设随机变量 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示第一次走到结点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间．那么我们要求的就是

𝐸(max𝑖∈𝑆𝑥𝑖)E(maxi∈Sxi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

使用 min-max 容斥可以得到

𝐸(max𝑖∈𝑆𝑥𝑖)=𝐸(∑𝑇⊆𝑆(−1)|𝑇|−1min𝑖∈𝑇𝑥𝑖)=∑𝑇⊆𝑆(−1)|𝑇|−1𝐸(min𝑖∈𝑇𝑥𝑖)E(maxi∈Sxi)=E(∑T⊆S(−1)|T|−1mini∈Txi)=∑T⊆S(−1)|T|−1E(mini∈Txi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于一个集合 𝑇 ∈[𝑛]T∈[n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，考虑求出 𝐹(𝑇) =𝐸(min𝑖∈𝑇𝑥𝑖)F(T)=E(mini∈Txi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑 𝐸(min𝑖∈𝑇𝑥𝑖)E(mini∈Txi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的含义，是第一次走到 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中某一个点的期望时间．不妨设 𝑓(𝑖)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示从结点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发，第一次走到 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中某个结点的期望时间．

  * 对于 𝑖 ∈𝑇i∈T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑓(𝑖) =0f(i)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 对于 𝑖 ∉𝑇i∉T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑓(𝑖) =1 +1deg(𝑖)∑(𝑖,𝑗)∈𝐸𝑓(𝑗)f(i)=1+1deg(i)∑(i,j)∈Ef(j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

如果直接高斯消元，复杂度 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么我们对每个 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都计算 𝐹(𝑇)F(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的总复杂度就是 𝑂(2𝑛𝑛3)O(2nn3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不能接受．我们使用树上消元的技巧．

不妨设根结点是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的父亲是 𝑝𝑢pu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于叶子结点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑓(𝑖)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只会和 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的父亲有关（也可能 𝑓(𝑖) =0f(i)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那样更好）．因此我们可以把 𝑓(𝑖)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示成 𝑓(𝑖) =𝐴𝑖 +𝐵𝑖𝑓(𝑝𝑖)f(i)=Ai+Bif(pi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，其中 𝐴𝑖,𝐵𝑖Ai,Bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以快速计算．

对于非叶结点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，考虑它的儿子序列 𝑗1,⋯,𝑗𝑘j1,⋯,jk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于 𝑓(𝑗𝑒) =𝐴𝑗𝑒 +𝐵𝑗𝑒𝑓(𝑖)f(je)=Aje+Bjef(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此可以得到

𝑓(𝑖)=1+1deg⁡(𝑖)𝑘∑𝑒=1(𝐴𝑗𝑒+𝐵𝑗𝑒𝑓(𝑖))+𝑓(𝑝𝑖)deg⁡(𝑖)f(i)=1+1deg⁡(i)∑e=1k(Aje+Bjef(i))+f(pi)deg⁡(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么变换一下可以得到

𝑓(𝑖)=deg⁡(𝑖)+∑𝑘𝑒=1𝐴𝑗𝑒deg⁡(𝑖)−∑𝑘𝑒=1𝐵𝑗𝑒+𝑓(𝑝𝑖)deg⁡(𝑖)−∑𝑘𝑒=1𝐵𝑗𝑒f(i)=deg⁡(i)+∑e=1kAjedeg⁡(i)−∑e=1kBje+f(pi)deg⁡(i)−∑e=1kBje![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是我们把 𝑓(𝑖)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也写成了 𝐴𝑖 +𝐵𝑖𝑓(𝑝𝑖)Ai+Bif(pi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式．这样可以一直倒推到根结点．而根结点没有父亲．也就是说

𝑓(1)=deg⁡(1)+∑𝑘𝑒=1𝐴𝑗𝑒deg⁡(1)−∑𝑘𝑒=1𝐵𝑗𝑒f(1)=deg⁡(1)+∑e=1kAjedeg⁡(1)−∑e=1kBje![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

解一下这个方程我们就得到了 𝑓(1)f(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再从上往下推一次就得到了每个点的 𝑓(𝑖)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么 𝐹(𝑇) =𝑓(𝑥)F(T)=f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．时间复杂度 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这样，我们可以对于每一个 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算出 𝐹(𝑇)F(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，时间复杂度 𝑂(2𝑛𝑛)O(2nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

回到容斥的部分，我们知道 𝐸(max𝑖∈𝑆𝑥𝑖) =∑𝑇⊆𝑆( −1)|𝑇|−1𝐹(𝑇)E(maxi∈Sxi)=∑T⊆S(−1)|T|−1F(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

不妨设 𝐹′(𝑇) =( −1)|𝑇|−1𝐹(𝑇)F′(T)=(−1)|T|−1F(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么进一步得到 𝐸(max𝑖∈𝑆𝑥𝑖) =∑𝑇⊆𝑆𝐹′(𝑇)E(maxi∈Sxi)=∑T⊆SF′(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此可以使用 FMT（也叫子集前缀和，或者 FWT 或变换）在 𝑂(2𝑛𝑛)O(2nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内对每个 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算出 𝐸(max𝑖∈𝑆𝑥𝑖)E(maxi∈Sxi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样就可以 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 回答询问了．

### 习题

  * [ABC331- G - Collect Them All](https://atcoder.jp/contests/abc331/tasks/abc331_g)
  * [洛谷 P4707 重返现世](https://www.luogu.com.cn/problem/P4707)

## 参考文献

[浅探容斥原理 - 王迪](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2013%E8%AE%BA%E6%96%87%E9%9B%86.pdf)，2013 年信息学奥林匹克中国国家队候选队员论文集

[有标号的 DAG 计数系列问题 - Cyhlnj](https://www.cnblogs.com/cjoieryl/p/10078167.html)

[全序关系 - Wikipedia](https://en.wikipedia.org/wiki/Total_order)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/inclusion-exclusion-principle.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/inclusion-exclusion-principle.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [sshwy](https://github.com/sshwy), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [MegaOwIer](https://github.com/MegaOwIer), [Peanut-Tang](https://github.com/Peanut-Tang), [HeRaNO](https://github.com/HeRaNO), [Xeonacid](https://github.com/Xeonacid), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [Chrogeek](https://github.com/Chrogeek), [ComeIntoCalm](https://github.com/ComeIntoCalm), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [Jerrycyx](https://github.com/Jerrycyx), [Jiangkangping](https://github.com/Jiangkangping), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [Lumos-exe](https://github.com/Lumos-exe), [lychees](https://github.com/lychees), [megakite](https://github.com/megakite), [ouuan](https://github.com/ouuan), [sbofgayschool](https://github.com/sbofgayschool), [ShizuhaAki](https://github.com/ShizuhaAki), [StableAgOH](https://github.com/StableAgOH), [StudyingFather](https://github.com/StudyingFather), [tder6](https://github.com/tder6), [untitledunrevised](https://github.com/untitledunrevised), [UserUnauthorized](https://github.com/UserUnauthorized), [ZYStream](https://github.com/ZYStream)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
