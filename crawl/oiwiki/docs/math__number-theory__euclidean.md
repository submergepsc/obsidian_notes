# 类欧几里德算法 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/euclidean/

# 类欧几里德算法

## 引入

类欧几里德算法是洪华敦在 2016 年冬令营营员交流中提出的内容．它常用于解决形如

⌊𝑎𝑖+𝑏𝑐⌋⌊ai+bc⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

结构的数列（下标为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）的求和问题．它的主要想法是，利用分数自身的递归结构，将问题转化为更小规模的问题，递归求解．因为分数的递归结构和 [欧几里得算法](../gcd/#欧几里得算法) 存在直接的 [联系](../continued-fraction/#连分数表示的求法)，因此，这一求和方法也称为类欧几里得算法．

因为 [连分数](../continued-fraction/) 和 [Stern–Brocot 树](../stern-brocot/) 等方法同样刻画了分数的递归结构，所以利用类欧几里得算法可以解决的问题，通常也可以用这些方法解决．与这些方法相比，类欧几里得算法通常更容易理解，它的实现也更为简明．

## 类欧几里得算法

最简单的例子，就是求和问题：

𝑓(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=0⌊𝑎𝑖+𝑏𝑐⌋,f(a,b,c,n)=∑i=0n⌊ai+bc⌋,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑎,𝑏,𝑐,𝑛a,b,c,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是正整数．

### 代数解法

首先，将 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模，可以简化问题，将问题转化为 0 ≤𝑎,𝑏 <𝑐0≤a,b<c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形：

𝑓(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=0⌊𝑎𝑖+𝑏𝑐⌋=𝑛∑𝑖=0⌊(⌊𝑎𝑐⌋𝑐+(𝑎mod𝑐))𝑖+(⌊𝑏𝑐⌋𝑐+(𝑏mod𝑐))𝑐⌋=𝑛∑𝑖=0(⌊𝑎𝑐⌋𝑖+⌊𝑏𝑐⌋+⌊(𝑎mod𝑐)𝑖+(𝑏mod𝑐)𝑐⌋)=𝑛(𝑛+1)2⌊𝑎𝑐⌋+(𝑛+1)⌊𝑏𝑐⌋+𝑓(𝑎mod𝑐,𝑏mod𝑐,𝑐,𝑛).f(a,b,c,n)=∑i=0n⌊ai+bc⌋=∑i=0n⌊(⌊ac⌋c+(amodc))i+(⌊bc⌋c+(bmodc))c⌋=∑i=0n(⌊ac⌋i+⌊bc⌋+⌊(amodc)i+(bmodc)c⌋)=n(n+1)2⌊ac⌋+(n+1)⌊bc⌋+f(amodc,bmodc,c,n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

现在，考虑转化后的问题．令

𝑚=⌊𝑎𝑛+𝑏𝑐⌋.m=⌊an+bc⌋.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么，原问题可以写作二次求和式：

𝑛∑𝑖=0⌊𝑎𝑖+𝑏𝑐⌋=𝑛∑𝑖=0𝑚−1∑𝑗=0[𝑗<⌊𝑎𝑖+𝑏𝑐⌋].∑i=0n⌊ai+bc⌋=∑i=0n∑j=0m−1[j<⌊ai+bc⌋].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

交换求和次序，这需要对于每个 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算满足条件的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的范围．为此，将条件变形：

𝑗<⌊𝑎𝑖+𝑏𝑐⌋=⌈𝑎𝑖+𝑏+1𝑐⌉−1⟺𝑗+1<⌈𝑎𝑖+𝑏+1𝑐⌉⟺𝑗+1<𝑎𝑖+𝑏+1𝑐⟺𝑐𝑗+𝑐−𝑏−1𝑎<𝑖⟺⌊𝑐𝑗+𝑐−𝑏−1𝑎⌋<𝑖.j<⌊ai+bc⌋=⌈ai+b+1c⌉−1⟺j+1<⌈ai+b+1c⌉⟺j+1<ai+b+1c⟺cj+c−b−1a<i⟺⌊cj+c−b−1a⌋<i.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

变形过程中多次利用了 [取整函数](../basic/#取整函数) 的性质．代入变形后的条件，原式可以写作：

𝑓(𝑎,𝑏,𝑐,𝑛)=𝑚−1∑𝑗=0𝑛∑𝑖=0[𝑖>⌊𝑐𝑗+𝑐−𝑏−1𝑎⌋]=𝑚−1∑𝑗=0(𝑛−⌊𝑐𝑗+𝑐−𝑏−1𝑎⌋)=𝑛𝑚−𝑓(𝑐,𝑐−𝑏−1,𝑎,𝑚−1).f(a,b,c,n)=∑j=0m−1∑i=0n[i>⌊cj+c−b−1a⌋]=∑j=0m−1(n−⌊cj+c−b−1a⌋)=nm−f(c,c−b−1,a,m−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令 (𝑎′,𝑏′,𝑐′,𝑛′) =(𝑐,𝑐 −𝑏 −1,𝑎,𝑚 −1)(a′,b′,c′,n′)=(c,c−b−1,a,m−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这就又回到了前面讨论过的 𝑎′ >𝑐′a′>c′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．

将这两步转化结合在一起，可以发现在过程中，(𝑎,𝑐)(a,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不断地取模后交换位置，直到 𝑎 =0a=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就类似于对 (𝑎,𝑐)(a,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行辗转相除，这也是类欧几里德算法的得名．它的时间复杂度是 𝑂(log⁡min{𝑎,𝑐})O(log⁡min{a,c})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

在计算过程中，可能会出现 𝑚 =0m=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，此时内层递归会出现 𝑛 = −1n=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这并不影响最终的结果．但是，如果要求出现 𝑚 =0m=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，直接终止算法，那么算法的时间复杂度可以改良为 𝑂(log⁡min{𝑎,𝑐,𝑛})O(log⁡min{a,c,n})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

对复杂度的解释

利用该算法和欧几里得算法的相似性，很容易说明它的时间复杂度是 𝑂(log⁡min{𝑎,𝑐})O(log⁡min{a,c})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．因此，只需要说明，如果在 𝑚 =0m=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时终止算法，那么它的时间复杂度也是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

令 𝑚 =⌊(𝑎𝑛 +𝑏)/𝑐⌋m=⌊(an+b)/c⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并记 𝑆 =𝑚𝑛S=mn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑘 =𝑚/𝑛k=m/n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它们分别相当于几何直观（见下一节）中点阵图的面积和直线的斜率．对于充分大的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，近似有 𝑘 ≐𝑎/𝑐k≐a/c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考察 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在算法过程中的变化．第一步取模时，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 保持不变，𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 近似由 𝑎/𝑐a/c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变为 (𝑎mod𝑐)/𝑐(amodc)/c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，相当于斜率由 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变为 𝑘 −⌊𝑘⌋k−⌊k⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也近似变为原来的 (𝑘 −⌊𝑘⌋)(k−⌊k⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 倍．第二步交换横纵坐标时，𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 近似保持不变，𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则变为它的倒数．因此，若设两步操作后，二元组 (𝑘,𝑆)(k,S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变为 (𝑘′,𝑆′)(k′,S′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有 𝑘′ =(𝑘 −⌊𝑘⌋)−1k′=(k−⌊k⌋)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑆′ =(𝑘 −⌊𝑘⌋)𝑆S′=(k−⌊k⌋)S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因为 1 ≤⌊𝑘′⌋ ≤𝑘′ <⌊𝑘′⌋ +11≤⌊k′⌋≤k′<⌊k′⌋+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，递归计算两轮后，乘积缩小的倍数最少为

(𝑘′−⌊𝑘′⌋)(𝑘−⌊𝑘⌋)=1−⌊𝑘′⌋𝑘′<1−⌊𝑘′⌋⌊𝑘′⌋+1=1⌊𝑘′⌋+1≤12.(k′−⌊k′⌋)(k−⌊k⌋)=1−⌊k′⌋k′<1−⌊k′⌋⌊k′⌋+1=1⌊k′⌋+1≤12.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，至多 𝑂(log⁡𝑆)O(log⁡S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轮，算法必然终止．因为从第二轮开始，每轮开始时的 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是不超过上一轮取模结束后的 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而后者大致为 𝑘𝑛2kn2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑘 <1k<1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因而 𝑂(log⁡𝑆) ⊆𝑂(log⁡𝑛)O(log⁡S)⊆O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就得到了上述结论．

模板题的参考实现如下：

模板题实现（[Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text #include <iostream> long long solve ( long long a , long long b , long long c , long long n ) { long long n2 = n * ( n \+ 1 ) / 2 ; if ( a >= c || b >= c ) return solve ( a % c , b % c , c , n ) \+ ( a / c ) * n2 \+ ( b / c ) * ( n \+ 1 ); long long m = ( a * n \+ b ) / c ; if ( ! m ) return 0 ; return m * n \- solve ( c , c \- b \- 1 , a , m \- 1 ); } int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int a , b , c , n ; std :: cin >> n >> c >> a >> b ; std :: cout << solve ( a , b , c , n \- 1 ) << '\n' ; } return 0 ; } ```   
---|---  
  
### 几何直观

这个算法还可以从几何的角度理解．类欧几里得算法可以解决的问题主要是直线下整点计数问题．

如下图最左部分所示，该求和式相当于求直线

𝑦=𝑎𝑥+𝑏𝑐y=ax+bc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

下方，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴上方（不包括 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴），且横坐标位于 [0,𝑛][0,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的格点数目．

![](./images/euclidean-1.svg)

首先，移除斜率和截距中的整数部分．这一步相当于将上图中间部分的蓝点数量单独计算出来．当斜率和截距都是整数时，蓝点一定构成一个梯形阵列，也就是说，不同纵列的格点形成等差数列，因而这些点的数量是容易计算的．将这些点移除后，剩余的格点和上图最右部分的红点数量一致．问题就转化成了斜率和截距都小于一的情形．因为梯形的高为 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且两个底边长度分别为 ⌊𝑏/𝑐⌋⌊b/c⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (⌊𝑎/𝑐⌋𝑛 +⌊𝑏/𝑐⌋)(⌊a/c⌋n+⌊b/c⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，利用梯形面积公式，这一步骤可以归纳为算式

𝑓(𝑎,𝑏,𝑐,𝑛)=𝑓(𝑎mod𝑐,𝑏mod𝑐,𝑐,𝑛)+12(𝑛+1)(⌊𝑏𝑐⌋+(⌊𝑎𝑐⌋𝑛+⌊𝑏𝑐⌋)).f(a,b,c,n)=f(amodc,bmodc,c,n)+12(n+1)(⌊bc⌋+(⌊ac⌋n+⌊bc⌋)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

然后，翻转横纵坐标轴．如下图最左部分所示，图中的红点和蓝点构成了一个横向长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、纵向长度为 𝑚 =⌊(𝑎𝑛 +𝑏)/𝑐⌋m=⌊(an+b)/c⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩形点阵．要计算红点的数量，只需要计算蓝点的数量，再用矩形点阵的数量减去蓝点的数量即可．翻转后，上图左半部分中的蓝点点阵就变成了某条直线下的红色点阵．而且，翻转后，斜率大于一，就又回到了上文已经处理过的情形．

![](./images/euclidean-2.svg)

关键在于如何计算新的红色点阵上方的直线的方程．将上图最左部分的横纵坐标轴翻转，就得到上图中间部分．翻转后的红色点阵上方的直线（中间部分的实线），并非对应翻转前的直线（最左部分的实线），而是翻转前的直线向左上平移一点点的结果（最左部分的虚线）．这是因为，如果直接将直线（最左部分的实线）翻转，将得到中间部分的虚线，但是按照定义，它下方的格点包括恰好落在直线上的格点，这就会导致直线上的格点重复计数．为了避免这一点，需要将翻转直线 𝑦 =(𝑎𝑥 +𝑏)/𝑐y=(ax+b)/c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后得到的直线 𝑦 =(𝑐𝑥 −𝑏)/𝑎y=(cx−b)/a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向下平移一点点，得到直线 𝑦 =(𝑐𝑥 −𝑏 −1)/𝑎y=(cx−b−1)/a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样它下方的点阵才恰为翻转前的蓝色点阵．

还有另一处细节需要处理．上图中间部分的直线的截距是负数，这意味着还没有回到之前的初始情形．要让截距恢复为非负数，只需要将直线（中间部分的实线）向左平移一个单位．这样做不会漏掉任何格点，因为翻转前的蓝色点阵中没有纵坐标为零的点，翻转后也就不存在横坐标为零的点．最后，直线方程就变为 𝑦 =(𝑐𝑥 +𝑐 −𝑏 −1)/𝑎y=(cx+c−b−1)/a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；同时，点阵的横坐标的上界也从 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变成了 𝑚 −1m−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这一步骤可以归纳为算式

𝑓(𝑎,𝑏,𝑐,𝑛)=𝑚𝑛−𝑓(𝑐,𝑐−𝑏−1,𝑎,𝑚−1).f(a,b,c,n)=mn−f(c,c−b−1,a,m−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这种递归的算法行得通，主要有两个原因：

  * 第一，直线的斜率不断地先取小数部分再取倒数，这等价于计算直线斜率 𝑘 =𝑎/𝑐k=a/c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [连分数展开](../continued-fraction/#连分数表示的求法)．因为有理分数的连分数展开的长度是 𝑂(log⁡min{𝑎,𝑐})O(log⁡min{a,c})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，所以这一过程一定在 𝑂(log⁡min{𝑎,𝑐})O(log⁡min{a,c})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步后终止；
  * 第二，因为每次翻转坐标轴的时候，直线斜率都是小于一的，因此，直觉上应该有 𝑚 <𝑛m<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说，经过这样一轮迭代后，横坐标的范围一直是在缩小的．前文的复杂度计算中通过严格的分析说明，每两轮迭代后，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至多为原来的一半，故而这一过程一定在 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步后终止．

这也是斜率为有理数时的类欧几里得算法的复杂度是 𝑂(log⁡min{𝑎,𝑐,𝑛})O(log⁡min{a,c,n})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原因．

利用类似的几何直观，可以将类欧几里得算法推广到斜率为无理数的情形，具体分析请参考后文的例题．

### 例题

[【模板】类欧几里得算法](https://www.luogu.com.cn/problem/P5170)

多组询问．给定正整数 𝑎,𝑏,𝑐,𝑛a,b,c,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求

𝑓(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=0⌊𝑎𝑖+𝑏𝑐⌋,𝑔(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=0𝑖⌊𝑎𝑖+𝑏𝑐⌋,ℎ(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=0⌊𝑎𝑖+𝑏𝑐⌋2.f(a,b,c,n)=∑i=0n⌊ai+bc⌋,g(a,b,c,n)=∑i=0ni⌊ai+bc⌋,h(a,b,c,n)=∑i=0n⌊ai+bc⌋2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)解答一

类似于 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的推导，可以得到 𝑔,ℎg,h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的递归表达式．

首先，利用取模，将问题转化为 0 ≤𝑎,𝑏 <𝑐0≤a,b<c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形：

𝑔(𝑎,𝑏,𝑐,𝑛)=𝑔(𝑎mod𝑐,𝑏mod𝑐,𝑐,𝑛)+⌊𝑎𝑐⌋𝑛(𝑛+1)(2𝑛+1)6+⌊𝑏𝑐⌋𝑛(𝑛+1)2,ℎ(𝑎,𝑏,𝑐,𝑛)=ℎ(𝑎mod𝑐,𝑏mod𝑐,𝑐,𝑛)+2⌊𝑏𝑐⌋𝑓(𝑎mod𝑐,𝑏mod𝑐,𝑐,𝑛)+2⌊𝑎𝑐⌋𝑔(𝑎mod𝑐,𝑏mod𝑐,𝑐,𝑛)+⌊𝑎𝑐⌋2𝑛(𝑛+1)(2𝑛+1)6+⌊𝑏𝑐⌋2(𝑛+1)+⌊𝑎𝑐⌋⌊𝑏𝑐⌋𝑛(𝑛+1).g(a,b,c,n)=g(amodc,bmodc,c,n)+⌊ac⌋n(n+1)(2n+1)6+⌊bc⌋n(n+1)2,h(a,b,c,n)=h(amodc,bmodc,c,n)+2⌊bc⌋f(amodc,bmodc,c,n)+2⌊ac⌋g(amodc,bmodc,c,n)+⌊ac⌋2n(n+1)(2n+1)6+⌊bc⌋2(n+1)+⌊ac⌋⌊bc⌋n(n+1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

然后，利用交换求和次序，可以进一步转化．同样地，令

𝑚=⌊𝑎𝑛+𝑏𝑐⌋.m=⌊an+bc⌋.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么，对于和式 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

𝑔(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=0𝑖⌊𝑎𝑖+𝑏𝑐⌋=𝑛∑𝑖=0𝑚−1∑𝑗=0𝑖[𝑗<⌊𝑎𝑖+𝑏𝑐⌋]=𝑚−1∑𝑗=0𝑛∑𝑖=0𝑖[𝑖>⌊𝑐𝑗+𝑐−𝑏−1𝑎⌋]=𝑚−1∑𝑗=012(⌊𝑐𝑗+𝑐−𝑏−1𝑎⌋+𝑛+1)(𝑛−⌊𝑐𝑗+𝑐−𝑏−1𝑎⌋)=12𝑚𝑛(𝑛+1)−12𝑚−1∑𝑗=0⌊𝑐𝑗+𝑐−𝑏−1𝑎⌋−12𝑚−1∑𝑗=0⌊𝑐𝑗+𝑐−𝑏−1𝑎⌋2=12𝑚𝑛(𝑛+1)−12𝑓(𝑐,𝑐−𝑏−1,𝑎,𝑚−1)−12ℎ(𝑐,𝑐−𝑏−1,𝑎,𝑚−1).g(a,b,c,n)=∑i=0ni⌊ai+bc⌋=∑i=0n∑j=0m−1i[j<⌊ai+bc⌋]=∑j=0m−1∑i=0ni[i>⌊cj+c−b−1a⌋]=∑j=0m−112(⌊cj+c−b−1a⌋+n+1)(n−⌊cj+c−b−1a⌋)=12mn(n+1)−12∑j=0m−1⌊cj+c−b−1a⌋−12∑j=0m−1⌊cj+c−b−1a⌋2=12mn(n+1)−12f(c,c−b−1,a,m−1)−12h(c,c−b−1,a,m−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于和式 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

ℎ(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=0⌊𝑎𝑖+𝑏𝑐⌋2=𝑛∑𝑖=0𝑚−1∑𝑗=0(2𝑗+1)[𝑗<⌊𝑎𝑖+𝑏𝑐⌋]=𝑚−1∑𝑗=0𝑛∑𝑖=0(2𝑗+1)[𝑖>⌊𝑐𝑗+𝑐−𝑏−1𝑎⌋]=𝑚−1∑𝑗=0(2𝑗+1)(𝑛−⌊𝑐𝑗+𝑐−𝑏−1𝑎⌋)=𝑛𝑚2−𝑚−1∑𝑗=0⌊𝑐𝑗+𝑐−𝑏−1𝑎⌋−2𝑚−1∑𝑗=0𝑗⌊𝑐𝑗+𝑐−𝑏−1𝑎⌋=𝑛𝑚2−𝑓(𝑐,𝑐−𝑏−1,𝑎,𝑚−1)−2𝑔(𝑐,𝑐−𝑏−1,𝑎,𝑚−1).h(a,b,c,n)=∑i=0n⌊ai+bc⌋2=∑i=0n∑j=0m−1(2j+1)[j<⌊ai+bc⌋]=∑j=0m−1∑i=0n(2j+1)[i>⌊cj+c−b−1a⌋]=∑j=0m−1(2j+1)(n−⌊cj+c−b−1a⌋)=nm2−∑j=0m−1⌊cj+c−b−1a⌋−2∑j=0m−1j⌊cj+c−b−1a⌋=nm2−f(c,c−b−1,a,m−1)−2g(c,c−b−1,a,m−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

从几何直观的角度看，这些非线性的求和式相当于给区域中的每个点 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都赋予了相应的权重 𝑤(𝑖,𝑗)w(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．除了这些权重之外，其余部分的计算过程是完全一致的．对于权重的选择，一般地，有

𝑛∑𝑖=0𝑖𝑟⌊𝑎𝑖+𝑏𝑐⌋𝑠=𝑛∑𝑖=0𝑚−1∑𝑗=0𝑖𝑟((𝑗+1)𝑠−𝑗𝑠)[𝑗<⌊𝑎𝑖+𝑏𝑐⌋].∑i=0nir⌊ai+bc⌋s=∑i=0n∑j=0m−1ir((j+1)s−js)[j<⌊ai+bc⌋].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

本题的另一个特点是，𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在递归计算时，会相互交错．因此，需要将 (𝑓,𝑔,ℎ)(f,g,h)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为三元组同时递归．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ``` |  ```text #include <iostream> struct Data { int f , g , h ; }; Data solve ( long long a , long long b , long long c , long long n ) { constexpr long long M = 998244353 ; constexpr long long i2 = ( M \+ 1 ) / 2 ; constexpr long long i6 = ( M \+ 1 ) / 6 ; long long n2 = ( n \+ 1 ) * n % M * i2 % M ; long long n3 = ( 2 * n \+ 1 ) * ( n \+ 1 ) % M * n % M * i6 % M ; Data res = { 0 , 0 , 0 }; if ( a >= c || b >= c ) { auto tmp = solve ( a % c , b % c , c , n ); long long aa = a / c , bb = b / c ; res . f = ( tmp . f \+ aa * n2 \+ bb * ( n \+ 1 )) % M ; res . g = ( tmp . g \+ aa * n3 \+ bb * n2 ) % M ; res . h = ( tmp . h \+ 2 * bb * tmp . f % M \+ 2 * aa * tmp . g % M \+ aa * aa % M * n3 % M \+ bb * bb % M * ( n \+ 1 ) % M \+ 2 * aa * bb % M * n2 % M ) % M ; return res ; } long long m = ( a * n \+ b ) / c ; if ( ! m ) return res ; auto tmp = solve ( c , c \- b \- 1 , a , m \- 1 ); res . f = ( m * n \- tmp . f \+ M ) % M ; res . g = ( m * n2 \+ ( M \- tmp . f ) * i2 \+ ( M \- tmp . h ) * i2 ) % M ; res . h = ( n * m % M * m \- tmp . f \- tmp . g * 2 \+ 3 * M ) % M ; return res ; } int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int n , a , b , c ; std :: cin >> n >> a >> b >> c ; auto res = solve ( a , b , c , n ); std :: cout << res . f << ' ' << res . h << ' ' << res . g << '\n' ; } return 0 ; } ```   
---|---  
  
[[清华集训 2014] Sum](https://www.luogu.com.cn/problem/P5172)

多组询问．给定正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求

𝑛∑𝑑=1(−1)⌊𝑑√𝑟⌋.∑d=1n(−1)⌊dr⌋.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)解答一

如果 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全平方数，那么当 √𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为偶数时，和式为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；否则，和式依据 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 奇偶性不同，在 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间交替变化．下面考虑 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是完全平方数的情形．

为了应用类欧几里得算法，首先将求和式转化为熟悉的形式：

𝑛∑𝑑=1(−1)⌊𝑑√𝑟⌋=𝑛∑𝑑=1(1−2(⌊𝑑√𝑟⌋mod2))=𝑛−2𝑛∑𝑑=1(⌊𝑑√𝑟⌋−2⌊⌊𝑑√𝑟⌋2⌋)=𝑛−2𝑛∑𝑑=1⌊𝑑√𝑟⌋+4𝑛∑𝑑=1⌊𝑑√𝑟2⌋=𝑛−2𝑓(𝑛,1,0,1)+4𝑓(𝑛,1,0,2)∑d=1n(−1)⌊dr⌋=∑d=1n(1−2(⌊dr⌋mod2))=n−2∑d=1n(⌊dr⌋−2⌊⌊dr⌋2⌋)=n−2∑d=1n⌊dr⌋+4∑d=1n⌊dr2⌋=n−2f(n,1,0,1)+4f(n,1,0,2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中的函数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 具有形式

𝑓(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=1⌊𝑎√𝑟+𝑏𝑐𝑖⌋.f(a,b,c,n)=∑i=1n⌊ar+bci⌋.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

与正文中的算法不同的是，此处的斜率不再是有理数．设斜率

𝑘=𝑎√𝑟+𝑏𝑐.k=ar+bc.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

同样分为两种情形讨论．如果 𝑘 ≥1k≥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么

𝑓(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=1⌊𝑘𝑖⌋=𝑛∑𝑖=1⌊(𝑘−⌊𝑘⌋)𝑖⌋+⌊𝑘⌋𝑛∑𝑖=1𝑖=⌊𝑘⌋𝑛(𝑛+1)2+𝑓(𝑎,𝑏−𝑐⌊𝑘⌋,𝑐,𝑛).f(a,b,c,n)=∑i=1n⌊ki⌋=∑i=1n⌊(k−⌊k⌋)i⌋+⌊k⌋∑i=1ni=⌊k⌋n(n+1)2+f(a,b−c⌊k⌋,c,n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

问题转化为斜率小于一的情形．如果 𝑘 <1k<1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么设 𝑚 =⌊𝑛𝑘⌋m=⌊nk⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

𝑓(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=1⌊𝑘𝑖⌋=𝑛∑𝑖=1𝑚∑𝑗=1[𝑗≤⌊𝑘𝑖⌋]=𝑚∑𝑗=1𝑛∑𝑖=1[𝑖>⌊𝑘−1𝑗⌋]=𝑛𝑚−𝑚∑𝑗=1𝑛∑𝑖=1[𝑖≤⌊𝑘−1𝑗⌋].f(a,b,c,n)=∑i=1n⌊ki⌋=∑i=1n∑j=1m[j≤⌊ki⌋]=∑j=1m∑i=1n[i>⌊k−1j⌋]=nm−∑j=1m∑i=1n[i≤⌊k−1j⌋].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

此处的推导中，交换 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的条件比正文中的情形更为简单，是因为直线 𝑦 =𝑘𝑥y=kx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上没有除了原点之外的格点．关键在于交换后的求和式写成 𝑓(𝑎,𝑏,𝑐,𝑛)f(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，这相当于要求 𝑎′,𝑏′,𝑐′a′,b′,c′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足

𝑘−1=𝑎′√𝑟+𝑏′𝑐′.k−1=a′r+b′c′.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这并不困难，只需要将分母有理化，就能得到

𝑘−1=𝑐𝑎√𝑟+𝑏=𝑐𝑎√𝑟−𝑐𝑏𝑎2𝑟−𝑏2.k−1=car+b=car−cba2r−b2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，有

𝑎′=𝑐𝑎, 𝑏′=−𝑐𝑏, 𝑐′=𝑎2𝑟−𝑏2.a′=ca, b′=−cb, c′=a2r−b2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这说明

𝑓(𝑎,𝑏,𝑐,𝑛)=𝑛𝑚−𝑓(𝑐𝑎,−𝑐𝑏,𝑎2𝑟−𝑏2,𝑚).f(a,b,c,n)=nm−f(ca,−cb,a2r−b2,m).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为了避免整数溢出，需要每次都将 𝑎,𝑏,𝑐a,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同除以它们的最大公约数．因为这个计算过程和计算 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连分数的过程完全一致，所以根据 [连分数理论](../continued-fraction/#二次无理数)，只要保证 gcd(𝑎,𝑏,𝑐) =1gcd(a,b,c)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它们在计算过程中必然在整型范围内．另外，尽管 (𝑎,𝑏,𝑐,𝑛)(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不会溢出，但是在该题数据范围下，𝑓(𝑎,𝑏,𝑐,𝑛)f(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能会超过 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位整数的范围，自然溢出即可，无需额外处理，最后结果一定在 [ −𝑛,𝑛][−n,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间．

尽管斜率不会变为零，算法的复杂度仍然是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，这一点从前文关于算法复杂度的论证容易看出．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``` |  ```text #include <cmath> #include <iostream> long long r ; long double sqrt_r ; long long gcd ( long long a , long long b ) { return b ? gcd ( b , a % b ) : a ; } unsigned long long f ( long long a , long long b , long long c , long long n ) { if ( ! n ) return 0 ; auto d = gcd ( a , gcd ( b , c )); a /= d ; b /= d ; c /= d ; unsigned long long k = ( a * sqrt_r \+ b ) / c ; if ( k ) { return n * ( n \+ 1 ) / 2 * k \+ f ( a , b \- c * k , c , n ); } else { unsigned long long m = n * ( a * sqrt_r \+ b ) / c ; return n * m \- f ( c * a , \- c * b , a * a * r \- b * b , m ); } } unsigned long long solve ( long long n , long long r ) { long long sqr = sqrt_r = sqrtl ( r ); if ( r == sqr * sqr ) return r % 2 ? ( n % 2 ? -1 : 0 ) : n ; return n \- 2 * f ( 1 , 0 , 1 , n ) \+ 4 * f ( 1 , 0 , 2 , n ); } int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int n ; std :: cin >> n >> r ; long long res = solve ( n , r ); std :: cout << res << '\n' ; } return 0 ; } ```   
---|---  
  
[Fraction](https://www.luogu.com.cn/problem/P5179)

给定正整数 𝑎,𝑏,𝑐,𝑑a,b,c,d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求所有满足 𝑎/𝑏 <𝑝/𝑞 <𝑐/𝑑a/b<p/q<c/d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最简分数 𝑝/𝑞p/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 (𝑞,𝑝)(q,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字典序最小的那个．

解答

这道题目也是 [Stern–Brocot 树](../stern-brocot/) 的经典应用，相关题解可以在 [此处](../continued-fraction/#连分数的树) 找到．因为它只依赖于分数的递归结构，所以它同样可以利用类似欧几里得算法的方法求解，故而也可以视作类欧几里得算法的一个应用．

如果 𝑎/𝑏a/b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑐/𝑑c/d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间（不含端点）存在至少一个自然数，可以直接取 (𝑞,𝑝) =(1,⌊𝑎/𝑏⌋ +1)(q,p)=(1,⌊a/b⌋+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．否则，必然有

⌊𝑎𝑏⌋≤𝑎𝑏<𝑝𝑞<𝑐𝑑≤⌊𝑎𝑏⌋+1.⌊ab⌋≤ab<pq<cd≤⌊ab⌋+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

从这个不等式中可以看出，𝑝/𝑞p/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数部分可以确定为 ⌊𝑎/𝑏⌋⌊a/b⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，直接消去该整数部分，然后整体取倒数，用于确定它的小数部分．这正是确定 𝑝/𝑞p/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连分数的 [基本方法](../continued-fraction/#连分数表示的求法)．若最终的答案是 𝑝/𝑞p/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么算法的时间复杂度为 𝑂(log⁡min{𝑝,𝑞})O(log⁡min{p,q})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

此处，有一个细节问题，即取倒数之后得到的字典序最小的分数，是否是取倒数之前的字典序最小的分数．换句话说，满足 𝑎/𝑏 <𝑝/𝑞 <𝑐/𝑑a/b<p/q<c/d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的分数 𝑝/𝑞p/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，字典序 (𝑞,𝑝)(q,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小的，是否也是字典序 (𝑝,𝑞)(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小的．假设不然，设 𝑝/𝑞p/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是字典序 (𝑞,𝑝)(q,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小的，但是 𝑟/𝑠 ≠𝑝/𝑞r/s≠p/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是字典序 (𝑟,𝑠)(r,s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小的．这必然有 𝑟 <𝑝r<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑞 <𝑠q<s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，这说明

𝑎𝑏<𝑟𝑠<𝑟𝑞<𝑝𝑞<𝑐𝑑.ab<rs<rq<pq<cd.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，𝑟/𝑞r/q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 无论按照哪个字典序怎样都是严格更小于当前解的．这与所设条件矛盾．因此，上述算法是正确的．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` |  ```text #include <iostream> void solve ( int a , int b , int & p , int & q , int c , int d ) { if (( a / b \+ 1 ) * d < c ) { p = a / b \+ 1 ; q = 1 ; } else { solve ( d , c \- d * ( a / b ), q , p , b , a % b ); p += q * ( a / b ); } } int main () { int a , b , c , d , p , q ; while ( std :: cin >> a >> b >> c >> d ) { solve ( a , b , p , q , c , d ); std :: cout << p << '/' << q << '\n' ; } return 0 ; } ```   
---|---  
  
## 万能欧几里得算法

上一节讨论的类欧几里得算法推导通常较为繁琐，而且能够解决的和式主要是可以转化为直线下（带权）整点计数问题的和式．本节讨论一种更为一般的方法，它进一步抽象了上述过程，从而可以解决更多的问题．因此，这一方法也称为万能欧几里得算法．它同样利用了分数的递归结构求解问题，但是与类欧几里得算法约化问题的思路稍有不同．

仍然考虑最经典的求和问题：

𝑓(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=1⌊𝑎𝑖+𝑏𝑐⌋,f(a,b,c,n)=∑i=1n⌊ai+bc⌋,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑎,𝑏,𝑐,𝑛a,b,c,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是正整数．

### 问题转化

设参数为 (𝑎,𝑏,𝑐,𝑛)(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线段为

𝑦=𝑎𝑥+𝑏𝑐, 0<𝑥≤𝑛.y=ax+bc, 0<x≤n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于这条线段，可以按照如下方法定义一个由 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组成的字符串 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也称为 **操作序列** ：

  * 字符串恰有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚 =⌊(𝑎𝑛 +𝑏)/𝑐⌋m=⌊(an+b)/c⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组成；
  * 第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 前方的 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量恰等于 ⌊(𝑎𝑖 +𝑏)/𝑐⌋⌊(ai+b)/c⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑖 =1,⋯,𝑛i=1,⋯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

从几何直观上看，这大致相当于从原点开始，每向右穿过一次竖向的网格线，就写下一个 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每向上穿过一次横向的网格线，就写下一个 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如下图所示：

![](./images/euclidean-universal.svg)

当然，这样的定义还需要考量一系列特殊情形：

  * 经过整点（即同时上穿和右穿）时，需要先写 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 再写 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 字符串开始时，除了在 (0,1](0,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 区间内上穿网格线的次数外，还需要格外补充 ⌊𝑏/𝑐⌋⌊b/c⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 字符串结束时，不能有格外的 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

如果对于几何直观的描述有任何不明晰的地方，可以参考上述代数方法的定义辅助理解．几何直观的描述，有助于理解下文的算法过程．

万能欧几里得算法的基本思路，就是将操作序列中的 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都视作某个 [幺半群](../../algebra/basic/#群) 内的元素，将整个操作序列视为幺半群内元素的乘积，而问题最终的答案与这个乘积有关．

比如，本题中，可以定义状态向量 𝑣 =(1,𝑦,∑𝑦)v=(1,y,∑y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示自原点开始，经历了若干次上穿和右穿网格线后，当前的状态．其中，第一个分量是常数，第二个分量是纵坐标 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，第三个分量是要求的和式．起始时，有 𝑣 =(1,0,0)v=(1,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．每向上穿过一次网格线，纵坐标就累加一，即相当于将状态向量右乘以矩阵

𝑈=⎛⎜ ⎜ ⎜⎝110010001⎞⎟ ⎟ ⎟⎠.U=(110010001).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

每向右穿过一次网格线，和式就累加一次纵坐标，即相当于将状态向量右乘以矩阵

𝑅=⎛⎜ ⎜ ⎜⎝100011001⎞⎟ ⎟ ⎟⎠.R=(100011001).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，最终的状态就是乘积 (1,0,0)𝑆(1,0,0)S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 理解为上述矩阵的乘积．所求的答案，就是最终状态的第三个分量．

除了将幺半群中的元素定义为矩阵以外，还可以将它们定义为一段操作序列对于最终结果的贡献，然后将操作的乘积定义为两段操作序列的贡献的合并．

本题中，可以定义每段操作序列的贡献为 (𝑥,𝑦,∑𝑦)(x,y,∑y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．为了严谨地解释这些记号，可以将这些分量都看作是操作序列的函数，也就是说，对于操作序列 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的贡献可以写作 (𝑥(𝑆),𝑦(𝑆),(∑𝑦)(𝑆))(x(S),y(S),(∑y)(S))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．其中，𝑥(𝑆)x(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦(𝑆)y(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别对应着操作序列 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量，也就是该线段右穿和上穿网格线的次数．最后一项中的求和符号，一般地，有如下定义：对于操作序列上的函数 𝑓(𝑆)f(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以定义 (∑𝑓)(𝑆)(∑f)(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，或记作 ∑𝑆𝑓∑Sf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，为下面的表达式：

∑𝑆𝑓:=∑{𝑓(𝑆[1,𝑟]):𝑆𝑟=𝑅}.∑Sf:=∑{f(S[1,r]):Sr=R}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑆𝑟Sr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的第 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字符，𝑆[1,𝑟]S[1,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中前 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字符组成的前缀．也就是说，这个求和记号，可以看作是对于操作序列 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有以 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结尾的前缀进行的求和．比如说，有

∑𝑆1=𝑥, ∑𝑆𝑥=12𝑥(𝑥+1).∑S1=x, ∑Sx=12x(x+1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再比如说，∑𝑦∑y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是操作序列中，每次右穿网格线时，之前上穿网格线的次数的累加．对于整段操作序列来说，𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在所有以 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结尾的前缀处的值，就是在 𝑖 =1,⋯,𝑛i=1,⋯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的所有 ⌊(𝑎𝑖 +𝑏)/𝑐⌋⌊(ai+b)/c⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．因此，对于整段操作序列计算的 ∑𝑦∑y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就是本题最终要求的量．

初始时，有 𝑈 =(0,1,0)U=(0,1,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑅 =(1,0,0)R=(1,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．进一步，可以将两个元素 (𝑥1,𝑦1,𝑠1)(x1,y1,s1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑥2,𝑦2,𝑠2)(x2,y2,s2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘积定义为

(𝑥1,𝑦1,𝑠1)⋅(𝑥2,𝑦2,𝑠2)=(𝑥1+𝑥2,𝑦1+𝑦2,𝑠1+𝑠2+𝑥2𝑦1).(x1,y1,s1)⋅(x2,y2,s2)=(x1+x2,y1+y2,s1+s2+x2y1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，最后一项贡献合并的结果可以通过如下计算得到：

∑𝑆1+𝑆2𝑦=∑𝑆1𝑦+∑𝑆2(𝑦+𝑦1)=∑𝑆1𝑦+∑𝑆2𝑦+𝑦1∑𝑆21=𝑠1+𝑠2+𝑥2𝑦1.∑S1+S2y=∑S1y+∑S2(y+y1)=∑S1y+∑S2y+y1∑S21=s1+s2+x2y1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

容易验证，这个乘法运算满足结合律，且幺元为 (0,0,0)(0,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以这些元素在该乘法运算下构成幺半群．所求的答案，就是乘积的第三个分量．

这两种方法都可以得到正确的结果．但是，因为保留了较多的冗余信息，矩阵运算的常数较大，所以第二种方法在处理实际问题时更为实用．

### 算法过程

与类欧几里得算法整体约化不同，万能欧几里得算法约化问题的手段是将这些操作分批次地合并．记字符串对应的操作的乘积为

𝐹(𝑎,𝑏,𝑐,𝑛,𝑈,𝑅).F(a,b,c,n,U,R).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

约化过程具体如下：

  * 当 𝑏 ≥𝑐b≥c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，操作序列的开始有 ⌊𝑏/𝑐⌋⌊b/c⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，直接计算它们的乘积，并将这些 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 从操作序列中移除．此时，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 前方的 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量等于

⌊𝑎𝑖+𝑏𝑐⌋−⌊𝑏𝑐⌋=⌊𝑎𝑖+(𝑏mod𝑐)𝑐⌋.⌊ai+bc⌋−⌊bc⌋=⌊ai+(bmodc)c⌋.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，这相当于将线段参数由 (𝑎,𝑏,𝑐,𝑛)(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变为 (𝑎,𝑏mod𝑐,𝑐,𝑛)(a,bmodc,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，对于这种情形，有

𝐹(𝑎,𝑏,𝑐,𝑛,𝑈,𝑅)=𝑈⌊𝑏/𝑐⌋𝐹(𝑎,𝑏mod𝑐,𝑐,𝑛,𝑈,𝑅).F(a,b,c,n,U,R)=U⌊b/c⌋F(a,bmodc,c,n,U,R).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 当 𝑎 ≥𝑐a≥c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，操作序列中每个 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前方都至少有 ⌊𝑎/𝑐⌋⌊a/c⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以将它们合并到 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上．也就是说，可以用 𝑈⌊𝑎/𝑐⌋𝑅U⌊a/c⌋R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 替代 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．合并后的字符串中，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 前方的 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量等于

⌊𝑎𝑖+𝑏𝑐⌋−⌊𝑎𝑐⌋𝑖=⌊(𝑎mod𝑐)𝑖+𝑏𝑐⌋.⌊ai+bc⌋−⌊ac⌋i=⌊(amodc)i+bc⌋.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，这相当于将线段参数由 (𝑎,𝑏,𝑐,𝑛)(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变为 (𝑎mod𝑐,𝑏,𝑐,𝑛)(amodc,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，对于这种情形，有

𝐹(𝑎,𝑏,𝑐,𝑛,𝑈,𝑅)=𝐹(𝑎mod𝑐,𝑏,𝑐,𝑛,𝑈,𝑈⌊𝑎/𝑐⌋𝑅).F(a,b,c,n,U,R)=F(amodc,b,c,n,U,U⌊a/c⌋R).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 对于剩下的情形，需要翻转横纵坐标，这基本是在交换 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只是翻转后线段的参数需要仔细计算．结合操作序列的定义可知，需要确定系数 (𝑎′,𝑏′,𝑐′,𝑛′)(a′,b′,c′,n′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得变换前的操作序列中，第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 前方的 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量恰为 ⌊(𝑎′𝑗 +𝑏′)/𝑐′⌋⌊(a′j+b′)/c′⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且总共有 𝑛′n′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据定义可知，

𝑛′=⌊𝑎𝑛+𝑏𝑐⌋=𝑚,n′=⌊an+bc⌋=m,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 前方的 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量，就等于最大的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

⌊𝑎𝑖+𝑏𝑐⌋<𝑗⟺𝑎𝑖+𝑏𝑐<𝑗⟺𝑖<𝑐𝑗−𝑏𝑎⟺𝑖<⌈𝑐𝑗−𝑏𝑎⌉=⌊𝑐𝑗−𝑏−1𝑎⌋+1.⌊ai+bc⌋<j⟺ai+bc<j⟺i<cj−ba⟺i<⌈cj−ba⌉=⌊cj−b−1a⌋+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，𝑖 =⌊(𝑐𝑗 −𝑏 −1)/𝑎⌋i=⌊(cj−b−1)/a⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这一推导过程与前文类欧几里得算法的推导类似，同样利用了上下取整函数的性质．

有两处细节需要处理：

    * 截距项 −(𝑏 +1)/𝑎−(b+1)/a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为负数．注意到，如果将线段向左平移一个单位，就可以让截距项恢复为非负数，因为总有 (𝑐 −𝑏 −1)/𝑎 ≥0(c−b−1)/a≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，可以将交换前的第一段 𝑅⌊(𝑐−𝑏−1)/𝑎⌋𝑈R⌊(c−b−1)/a⌋U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 提取出来，只交换剩余操作序列中的 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
    * 交换 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，结尾存在多余的 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，交换 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之前，需要首先将最后一段 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 提取出来，只交换剩余操作序列中的 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这一段 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量为 𝑛 −⌊(𝑐𝑚 −𝑏 −1)/𝑎⌋n−⌊(cm−b−1)/a⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

去掉头尾若干个字符后，第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 前方的 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量变为：

⌊𝑐(𝑗+1)−𝑏−1𝑎⌋−⌊𝑐−𝑏−1𝑎⌋=⌊𝑐𝑗+(𝑐−𝑏−1)mod𝑎𝑎⌋.⌊c(j+1)−b−1a⌋−⌊c−b−1a⌋=⌊cj+(c−b−1)modaa⌋.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

回忆起，交换前的序列中 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量为 𝑚 =⌊(𝑎𝑛 +𝑏)/𝑐⌋m=⌊(an+b)/c⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而上述左移一个单位的操作，要求保证交换前至少存在一个 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是 𝑚 >0m>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．利用这一条件，可以分为两种情形：

    * 对于 𝑚 >0m>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，处理了上面的两点后，交换完 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的操作序列就是对应着参数为 (𝑐,(𝑐 −𝑏 −1)mod𝑎,𝑎,𝑚 −1)(c,(c−b−1)moda,a,m−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线段的合法序列．所以，有

𝐹(𝑎,𝑏,𝑐,𝑛,𝑈,𝑅)=𝑅⌊(𝑐−𝑏−1)/𝑎⌋𝑈𝐹(𝑐,(𝑐−𝑏−1)mod𝑎,𝑎,𝑚−1,𝑅,𝑈)𝑅𝑛−⌊(𝑐𝑚−𝑏−1)/𝑎⌋.F(a,b,c,n,U,R)=R⌊(c−b−1)/a⌋UF(c,(c−b−1)moda,a,m−1,R,U)Rn−⌊(cm−b−1)/a⌋.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
    * 特别地，对于 𝑚 =0m=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，交换前的操作序列中只包含 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，无需交换，可以直接返回：

𝐹(𝑎,𝑏,𝑐,𝑛,𝑈,𝑅)=𝑅𝑛.F(a,b,c,n,U,R)=Rn.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

与类欧几里得算法不同，万能欧几里得算法的这一特殊情形需要单独处理，否则会因涉及负幂次而无法正确计算．

利用这些讨论，就可以将问题递归地解决．

假设幺半群内元素单次相乘的时间复杂度是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．那么，如果计算过程中这些元素的幂次计算都使用 [快速幂](../../binary-exponentiation/) 进行，最终的算法复杂度就是 𝑂(log⁡max{𝑎,𝑐} +log⁡(𝑏/𝑐))O(log⁡max{a,c}+log⁡(b/c))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的1．

对复杂度的解释

对比（类）欧几里得算法，万能欧几里得算法只是多了求快速幂的步骤．其余的计算过程的复杂度和类欧几里得算法相仿，已经说明是 𝑂(log⁡min{𝑎,𝑐,𝑛})O(log⁡min{a,c,n})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．现在，需要计算这些快速幂的总复杂度．

除了第一轮迭代，都有 𝑏 <𝑐b<c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此这些迭代每轮都涉及三次快速幂的计算，总的复杂度是：

𝑂(log⁡⌊𝑎𝑐⌋+log⁡⌊𝑐−𝑏1−1𝑎1⌋+log⁡(𝑛−⌊𝑐𝑚−𝑏1−1𝑎1⌋)),O(log⁡⌊ac⌋+log⁡⌊c−b1−1a1⌋+log⁡(n−⌊cm−b1−1a1⌋)),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑎1 =𝑎mod𝑐a1=amodc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏1 =𝑏mod𝑐b1=bmodc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑚 =⌊(𝑎1𝑛 +𝑏1)/𝑐⌋m=⌊(a1n+b1)/c⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．后面两项，分别有估计：

𝑐−𝑏1−1𝑎1≤𝑐𝑎1,𝑛−⌊𝑐𝑚−𝑏1−1𝑎1⌋≤𝑛−𝑐𝑚−𝑏1−1𝑎1+1≤𝑛−𝑐((𝑎1𝑛+𝑏1)/𝑐−1)−𝑏1−1𝑎1+1=𝑐+1𝑎1+1.c−b1−1a1≤ca1,n−⌊cm−b1−1a1⌋≤n−cm−b1−1a1+1≤n−c((a1n+b1)/c−1)−b1−1a1+1=c+1a1+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，这两项的复杂度都是 𝑂(log⁡(𝑐/𝑎1))O(log⁡(c/a1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

每一轮迭代中，线段的参数都由 (𝑎, ⋅,𝑐, ⋅)(a,⋅,c,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变换为 (𝑐, ⋅,𝑎mod𝑐, ⋅)(c,⋅,amodc,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且该轮总的时间复杂度为

𝑂(log⁡𝑎𝑐+log⁡𝑐𝑎mod𝑐).O(log⁡ac+log⁡camodc).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于全部递归的轮次，这些项可以裂项相消，因此，最后总和复杂度就是 𝑂(log⁡𝑎 +log⁡𝑐) =𝑂(log⁡max{𝑎,𝑐})O(log⁡a+log⁡c)=O(log⁡max{a,c})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

最后，再加上第一轮迭代中快速幂 𝑈⌊𝑏/𝑐⌋U⌊b/c⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度 𝑂(log⁡(𝑏/𝑐))O(log⁡(b/c))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就得到总的复杂度为 𝑂(log⁡max{𝑎,𝑐} +log⁡(𝑏/𝑐))O(log⁡max{a,c}+log⁡(b/c))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

万能欧几里得算法的流程可以写成统一的模板，处理具体问题时只需要更改模板类型 `T` 的实现即可．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text // Class T implements the monoid. // Assume that it provides a multiplication operator // and a default constructor returning the unity in the monoid. // Binary exponentiation. template < typename T > T pow ( T a , int b ) { T res ; for (; b ; b >>= 1 ) { if ( b & 1 ) res = res * a ; a = a * a ; } return res ; } // Universal Euclidean algorithm. template < typename T > T euclid ( int a , int b , int c , int n , T U , T R ) { if ( b >= c ) return pow ( U , b / c ) * euclid ( a , b % c , c , n , U , R ); if ( a >= c ) return euclid ( a % c , b , c , n , U , pow ( U , a / c ) * R ); auto m = (( long long ) a * n \+ b ) / c ; if ( ! m ) return pow ( R , n ); return pow ( R , ( c \- b \- 1 ) / a ) * U * euclid ( c , ( c \- b \- 1 ) % a , a , m \- 1 , R , U ) * pow ( R , n \- ( c * m \- b \- 1 ) / a ); } ```   
---|---  
  
利用万能欧几里得算法可以得到模板题的实现如下：

模板题实现（[Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 ``` |  ```text #include <array> #include <iostream> // Switch between matrix and info merging approaches. #define MATRIX 1 // Class T implements the monoid. // Assume that it provides a multiplication operator // and a default constructor returning the unity in the monoid. // Binary exponentiation. template < typename T > T pow ( T a , int b ) { T res ; for (; b ; b >>= 1 ) { if ( b & 1 ) res = res * a ; a = a * a ; } return res ; } // Universal Euclidean algorithm. template < typename T > T euclid ( int a , int b , int c , int n , T U , T R ) { if ( b >= c ) return pow ( U , b / c ) * euclid ( a , b % c , c , n , U , R ); if ( a >= c ) return euclid ( a % c , b , c , n , U , pow ( U , a / c ) * R ); auto m = (( long long ) a * n \+ b ) / c ; if ( ! m ) return pow ( R , n ); return pow ( R , ( c \- b \- 1 ) / a ) * U * euclid ( c , ( c \- b \- 1 ) % a , a , m \- 1 , R , U ) * pow ( R , n \- ( c * m \- b \- 1 ) / a ); } #if MATRIX template < size_t N > struct Matrix { std :: array < long long , N * N > mat ; auto loc ( size_t i , size_t j ) const { return mat [ i * N \+ j ]; } auto & loc ( size_t i , size_t j ) { return mat [ i * N \+ j ]; } Matrix () : mat {} { for ( size_t i = 0 ; i != N ; ++ i ) { loc ( i , i ) = 1 ; } } Matrix operator * ( const Matrix & rhs ) const { Matrix res ; res . mat . fill ( 0 ); for ( size_t i = 0 ; i != N ; ++ i ) { for ( size_t k = 0 ; k != N ; ++ k ) { for ( size_t j = 0 ; j != N ; ++ j ) { res . loc ( i , j ) += loc ( i , k ) * rhs . loc ( k , j ); } } } return res ; } }; long long solve ( int a , int b , int c , int n ) { if ( ! n ) return 0 ; Matrix < 3 > U , R ; U . loc ( 0 , 1 ) = R . loc ( 1 , 2 ) = 1 ; auto res = euclid ( a , b , c , n , U , R ); return res . loc ( 0 , 2 ); } #else struct Info { long long x , y , s ; Info () : x ( 0 ), y ( 0 ), s ( 0 ) {} Info operator * ( const Info & rhs ) const { Info res ; res . x = x \+ rhs . x ; res . y = y \+ rhs . y ; res . s = s \+ rhs . s \+ rhs . x * y ; return res ; } }; long long solve ( int a , int b , int c , int n ) { if ( ! n ) return 0 ; Info U , R ; U . y = 1 ; R . x = 1 ; auto res = euclid ( a , b , c , n , U , R ); return res . s ; } #endif int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int a , b , c , n ; std :: cin >> n >> c >> a >> b ; std :: cout << solve ( a , b , c , n \- 1 ) << '\n' ; } return 0 ; } ```   
---|---  
  
### 例题

[【模板】类欧几里得算法](https://www.luogu.com.cn/problem/P5170)

多组询问．给定正整数 𝑎,𝑏,𝑐,𝑛a,b,c,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求

𝑓(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=0⌊𝑎𝑖+𝑏𝑐⌋,𝑔(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=0𝑖⌊𝑎𝑖+𝑏𝑐⌋,ℎ(𝑎,𝑏,𝑐,𝑛)=𝑛∑𝑖=0⌊𝑎𝑖+𝑏𝑐⌋2.f(a,b,c,n)=∑i=0n⌊ai+bc⌋,g(a,b,c,n)=∑i=0ni⌊ai+bc⌋,h(a,b,c,n)=∑i=0n⌊ai+bc⌋2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)解答二

为了应用万能欧几里得算法的模板，首先将 𝑖 =0i=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的项提出来，单独考虑．对于剩下的部分，可以看作是对参数为 (𝑎,𝑏,𝑐,𝑛)(a,b,c,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线段分别计算 ∑𝑦,∑𝑥𝑦,∑𝑦2∑y,∑xy,∑y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如正文所言，有两种将操作序列转换为幺半群元素的方式．

**矩阵运算** ：状态向量定义为 (1,𝑥,𝑦,𝑥𝑦,𝑦2,∑𝑦,∑𝑥𝑦,∑𝑦2)(1,x,y,xy,y2,∑y,∑xy,∑y2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．初始状态为 (1,0,0,0,0,0,0,0)(1,0,0,0,0,0,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，两个操作分别为

𝑈=⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝1010100001010000001020000001000000001000000001000000001000000001⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠, 𝑅=⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝1100000001000000001101100001001000001001000001000000001000000001⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠.U=(1010100001010000001020000001000000001000000001000000001000000001), R=(1100000001000000001101100001001000001001000001000000001000000001).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

最终答案为初始状态右乘这些操作矩阵的乘积得到的向量末尾三个分量．

这个做法的常数巨大，并不能通过本题，这里给出细节仅仅是为了辅助理解．

**贡献合并** ：一段操作序列的贡献定义为 (𝑥,𝑦,∑𝑦,∑𝑥𝑦,∑𝑦2)(x,y,∑y,∑xy,∑y2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．两个操作分别为

𝑈=(0,1,0,0,0), 𝑅=(1,0,0,0,0).U=(0,1,0,0,0), R=(1,0,0,0,0).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

贡献合并时，有

∑𝑆1+𝑆2𝑦=∑𝑆1𝑦+∑𝑆2(𝑦+𝑦1)=∑𝑆1𝑦+∑𝑆2𝑦+𝑥2𝑦1,∑𝑆1+𝑆2𝑥𝑦=∑𝑆1𝑥𝑦+∑𝑆2(𝑥+𝑥1)(𝑦+𝑦1)=∑𝑆1𝑥𝑦+∑𝑆2𝑥𝑦+𝑥1∑𝑆2𝑦+𝑦1∑𝑆2𝑥+𝑥1𝑦1∑𝑆21=∑𝑆1𝑥𝑦+∑𝑆2𝑥𝑦+𝑥1∑𝑆2𝑦+12𝑥2(𝑥2+1)𝑦1+𝑥1𝑥2𝑦1,∑𝑆1+𝑆2𝑦2=∑𝑆1𝑦2+∑𝑆2(𝑦+𝑦1)2=∑𝑆1𝑦2+∑𝑆2𝑦2+2𝑦1∑𝑆2𝑦+𝑦21∑𝑆21=∑𝑆1𝑦2+∑𝑆2𝑦2+2𝑦1∑𝑆2𝑦+𝑥2𝑦21.∑S1+S2y=∑S1y+∑S2(y+y1)=∑S1y+∑S2y+x2y1,∑S1+S2xy=∑S1xy+∑S2(x+x1)(y+y1)=∑S1xy+∑S2xy+x1∑S2y+y1∑S2x+x1y1∑S21=∑S1xy+∑S2xy+x1∑S2y+12x2(x2+1)y1+x1x2y1,∑S1+S2y2=∑S1y2+∑S2(y+y1)2=∑S1y2+∑S2y2+2y1∑S2y+y12∑S21=∑S1y2+∑S2y2+2y1∑S2y+x2y12.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这说明，应该将操作的乘法定义为

(𝑥1,𝑦1,𝑠1,𝑡1,𝑢1)⋅(𝑥2,𝑦2,𝑠2,𝑡2,𝑢2)=(𝑥1+𝑥2,𝑦1+𝑦2,𝑠1+𝑠2+𝑥2𝑦1,𝑡1+𝑡2+𝑥1𝑠2+(1/2)𝑥2(𝑥2+1)𝑦1+𝑥1𝑥2𝑦1,𝑢1+𝑢2+2𝑦1𝑠2+𝑥2𝑦21).(x1,y1,s1,t1,u1)⋅(x2,y2,s2,t2,u2)=(x1+x2,y1+y2,s1+s2+x2y1,t1+t2+x1s2+(1/2)x2(x2+1)y1+x1x2y1,u1+u2+2y1s2+x2y12).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

虽然直接验证较为繁琐，但是上述定义的贡献向量在该乘法下的确构成幺半群，单位元为 (0,0,0,0,0)(0,0,0,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于一般的情形，有

∑𝑆1+𝑆2𝑥𝑟𝑦𝑠=∑𝑆1𝑥𝑟𝑦𝑠+∑𝑆2(𝑥+𝑥1)𝑟(𝑦+𝑦1)𝑠=∑𝑆1𝑥𝑟𝑦𝑠+𝑟∑𝑖=0𝑠∑𝑗=0(𝑟𝑖)(𝑠𝑗)𝑥𝑟−𝑖1𝑦𝑠−𝑗1∑𝑆2𝑥𝑖𝑦𝑗.∑S1+S2xrys=∑S1xrys+∑S2(x+x1)r(y+y1)s=∑S1xrys+∑i=0r∑j=0s(ri)(sj)x1r−iy1s−j∑S2xiyj.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

只要维护好所有更低幂次的贡献，就可以计算一般情形的和式．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 ``` |  ```text #include <iostream> template < typename T > T pow ( T a , int b ) { T res ; for (; b ; b >>= 1 ) { if ( b & 1 ) res = res * a ; a = a * a ; } return res ; } template < typename T > T euclid ( int a , int b , int c , int n , T U , T R ) { if ( b >= c ) return pow ( U , b / c ) * euclid ( a , b % c , c , n , U , R ); if ( a >= c ) return euclid ( a % c , b , c , n , U , pow ( U , a / c ) * R ); auto m = (( long long ) a * n \+ b ) / c ; if ( ! m ) return pow ( R , n ); return pow ( R , ( c \- b \- 1 ) / a ) * U * euclid ( c , ( c \- b \- 1 ) % a , a , m \- 1 , R , U ) * pow ( R , n \- ( c * m \- b \- 1 ) / a ); } constexpr int M = 998244353 ; struct Info { long long x , y , s , t , u ; Info () : x ( 0 ), y ( 0 ), s ( 0 ), t ( 0 ), u ( 0 ) {} Info operator * ( const Info & rhs ) const { Info res ; res . x = ( x \+ rhs . x ) % M ; res . y = ( y \+ rhs . y ) % M ; res . s = ( s \+ rhs . s \+ rhs . x * y ) % M ; auto tmp = ( rhs . x * ( rhs . x \+ 1 ) / 2 \+ x * rhs . x ) % M ; res . t = ( t \+ rhs . t \+ x * rhs . s \+ tmp * y ) % M ; res . u = ( u \+ rhs . u \+ 2 * y * rhs . s \+ rhs . x * y % M * y ) % M ; return res ; } }; void solve ( int a , int b , int c , int n ) { Info U , R ; U . y = 1 ; R . x = 1 ; auto res = euclid ( a , b , c , n , U , R ); auto f = ( res . s \+ b / c ) % M ; auto g = res . t ; auto h = ( res . u \+ ( long long )( b / c ) * ( b / c )) % M ; std :: cout << f << ' ' << h << ' ' << g << '\n' ; } int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int a , b , c , n ; std :: cin >> n >> a >> b >> c ; solve ( a , b , c , n ); } return 0 ; } ```   
---|---  
  
[[清华集训 2014] Sum](https://www.luogu.com.cn/problem/P5172)

多组询问．给定正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求

𝑛∑𝑑=1(−1)⌊𝑑√𝑟⌋.∑d=1n(−1)⌊dr⌋.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)解答二

首先，单独处理 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为完全平方数的情形，与前文完全一致，从略．此处，仅考虑 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是完全平方数的情形．

本题应用万能欧几里得算法的方式有很多．比如说，可以为每个操作定义一个线性变换：

𝑈(𝑥)=−𝑥, 𝑅(𝑥)=𝑥+1.U(x)=−x, R(x)=x+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

操作的乘法定义为线性变换的复合．那么，最终的答案就是操作序列对应的变换的复合得到的函数在 𝑥 =0x=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的值．

还可以为每段操作序列定义它的贡献．贡献可以定义为 (( −1)𝑦,∑( −1)𝑦)((−1)y,∑(−1)y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，两个操作分别取

𝑈=(0,−1), 𝑅=(1,1).U=(0,−1), R=(1,1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

贡献的合并定义为

(𝑢1,𝑣1)⋅(𝑢2,𝑣2)=(𝑢1𝑢2,𝑣1+𝑢1𝑣2).(u1,v1)⋅(u2,v2)=(u1u2,v1+u1v2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

容易验证，在该乘法下，所有操作构成了幺半群，且单位元为 (0,1)(0,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．最终的答案就是所有元素乘积的第二个分量．

这两种方法是一致的，因为如果将线性变换写作 𝑓(𝑥) =𝑢 +𝑣𝑥f(x)=u+vx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么线性变换的复合对应的系数的变化，恰恰就是上述操作的乘法．也就是说，这两个幺半群是同构的．

本题中，线段的参数为 (𝑘,𝑛)(k,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑘 ∈𝐑k∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为直线的斜率．设操作序列对应的乘积为 𝐹(𝑘,𝑛,𝑈,𝑅)F(k,n,U,R)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，有如下递归算法：

  * 如果 𝑘 ≥1k≥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么操作序列中每个 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 前方都有至少 ⌊𝑘⌋⌊k⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，有

𝐹(𝑘,𝑛,𝑈,𝑅)=𝐹(𝑘−⌊𝑘⌋,𝑛,𝑈,𝑈⌊𝑘⌋𝑅).F(k,n,U,R)=F(k−⌊k⌋,n,U,U⌊k⌋R).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 如果 𝑘 <1k<1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么交换操作序列中的 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并舍去末尾的 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即交换前的 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），所以，有

𝐹(𝑘,𝑛,𝑈,𝑅)=𝐹(𝑘−1,𝑚,𝑅,𝑈)𝑅𝑛−⌊𝑘−1𝑚⌋.F(k,n,U,R)=F(k−1,m,R,U)Rn−⌊k−1m⌋.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

算法中，𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的迭代过程其实就是在求 √𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连分数展开．为此，可以应用 [PQa 算法](../pell-equation/#pqa-算法)．求连分数的过程和万能欧几里得算法迭代的过程可以同时进行．

和类欧几里得算法的情形一致，算法的复杂度仍然是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 ``` |  ```text #include <algorithm> #include <cmath> #include <iostream> template < typename T > T pow ( T a , int b ) { T res ; for (; b ; b >>= 1 ) { if ( b & 1 ) res = res * a ; a = a * a ; } return res ; } struct LinearTransform { int u , v ; LinearTransform () : u ( 0 ), v ( 1 ) {} LinearTransform operator * ( const LinearTransform & rhs ) const { LinearTransform res ; res . u = u \+ v * rhs . u ; res . v = v * rhs . v ; return res ; } int eval ( int x ) const { return u \+ v * x ; } }; int solve ( int n , int r ) { long double sqrt_r = sqrtl ( r ); int sqr = sqrt_r ; if ( r == sqr * sqr ) return sqr % 2 ? ( n % 2 ? -1 : 0 ) : n ; int P = 0 , Q = 1 , D = r , val = 0 ; LinearTransform U , R ; U . v = -1 ; R . u = 1 ; while ( n ) { int a = ( P \+ sqr ) / Q ; R = pow ( U , a ) * R ; int m = (( P \+ sqrt_r ) / Q \- a ) * n ; P = a * Q \- P ; Q = ( D \- P * P ) / Q ; int rem = n \- ( int )( m * ( P \+ sqrt_r ) / Q ); val = pow ( R , rem ). eval ( val ); std :: swap ( U , R ); n = m ; } return val ; } int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int n , r ; std :: cin >> n >> r ; std :: cout << solve ( n , r ) << '\n' ; } return 0 ; } ```   
---|---  
  
## 习题

模板题：

  * [Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)
  * [Luogu P5170【模板】类欧几里得算法](https://www.luogu.com.cn/problem/P5170)
  * [Luogu P5171 Earthquake](https://www.luogu.com.cn/problem/P5171)
  * [Luogu P5172 [清华集训 2014] Sum](https://www.luogu.com.cn/problem/P5172)
  * [Luogu P4132 [BJOI2012] 算不出的等式](https://www.luogu.com.cn/problem/P4132)
  * [LOJ 138. 类欧几里得算法](https://loj.ac/p/138)
  * [LOJ 6440. 万能欧几里得](https://loj.ac/p/6440)
  * [Luogu P5179 Fraction](https://www.luogu.com.cn/problem/P5179)
  * [Codeforces 1182 F. Maximum Sine](https://codeforces.com/problemset/problem/1182/F)

应用题：

  * [Luogu P4433 [COCI 2009/2010 #1] ALADIN](https://www.luogu.com.cn/problem/P4433)
  * [AtCoder Beginner Contest 372 G - Ax + By < C](https://atcoder.jp/contests/abc372/tasks/abc372_g)
  * [AtCoder Beginner Contest 313 G - Redistribution of Piles](https://atcoder.jp/contests/abc313/tasks/abc313_g)
  * [AtCoder Beginner Contest 283 Ex - Popcount Sum](https://atcoder.jp/contests/abc283/tasks/abc283_h)
  * [Codeforces 1098 E. Fedya the Potter](https://codeforces.com/problemset/problem/1098/E)
  * [Codeforces 868 G. El Toll Caves](https://codeforces.com/problemset/problem/868/G)

## 参考资料与注释

* * *

  1. 通常考虑的问题中，𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都与 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同阶，𝑂(log⁡(𝑏/𝑐))O(log⁡(b/c))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这一项可以忽略．而且，如果在调用万能欧几里得算法前，首先进行了一轮类欧几里得算法的取模，消除 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的影响，这一项的快速幂的复杂度是可以规避的．这其实是因为通常的问题中，𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的初始形式较为特殊，它的幂次有着更简单的形式，不需要通过快速幂计算．比如正文的例子中，𝑈⌊𝑏/𝑎⌋U⌊b/a⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的结果，就是将 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中不在对角线上的那个 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 替换成 ⌊𝑏/𝑎⌋⌊b/a⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而无需用快速幂计算． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/euclidean.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/euclidean.md "edit.link.title")  
>  __本页面贡献者：[sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [Enter-tainer](https://github.com/Enter-tainer), [Tiphereth-A](https://github.com/Tiphereth-A), [H-J-Granger](https://github.com/H-J-Granger), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [c-forrest](https://github.com/c-forrest), [Early0v0](https://github.com/Early0v0), [Ir1d](https://github.com/Ir1d), [MegaOwIer](https://github.com/MegaOwIer), [Xeonacid](https://github.com/Xeonacid), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [FFjet](https://github.com/FFjet), [GekkaSaori](https://github.com/GekkaSaori), [Henry-ZHR](https://github.com/Henry-ZHR), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [qz-cqy](https://github.com/qz-cqy), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [alphagocc](https://github.com/alphagocc), [cxm1024](https://github.com/cxm1024), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [megakite](https://github.com/megakite), [Peanut-Tang](https://github.com/Peanut-Tang), [r-value](https://github.com/r-value), [SukkaW](https://github.com/SukkaW), [TonyYin0418](https://github.com/TonyYin0418)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
