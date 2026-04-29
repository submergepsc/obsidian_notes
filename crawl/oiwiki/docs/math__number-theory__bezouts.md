# 裴蜀定理 & 一次不定方程 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/bezouts/

# 裴蜀定理 & 一次不定方程

裴蜀定理揭示了最大公约数与整数线性组合之间的深刻联系，是数论中最基础也最重要的结论之一．基于此，本文进一步讨论了一次不定方程的求解方法．

## 裴蜀定理

**裴蜀定理** （Bézout's lemma），也译作贝祖定理，或称作贝祖等式（Bézout's identity），给出了一个整数能够表示为两个整数的整系数线性组合的充分必要条件．

裴蜀定理

设 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是不全为零的整数．那么，对于任意整数 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 gcd(𝑎,𝑏) ∣𝑎𝑥 +𝑏𝑦gcd(a,b)∣ax+by![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立；而且，存在整数 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑎𝑥 +𝑏𝑦 =gcd(𝑎,𝑏)ax+by=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．

证明

记 𝑑 =gcd(𝑎,𝑏)d=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为 𝑑 ∣𝑎,𝑏d∣a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，存在整数 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑎 =𝑑𝑢, 𝑏 =𝑑𝑣a=du, b=dv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．因此，总有

𝑎𝑥+𝑏𝑦=𝑑(𝑢𝑥+𝑣𝑦).ax+by=d(ux+vy).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就说明 𝑑 ∣𝑎𝑥 +𝑏𝑦d∣ax+by![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

反过来，需要说明存在 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得等式成立．如果 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之一是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不妨设 𝑏 =0b=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么它们的最大公约数为 𝑑 =𝑎d=a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，显然有 (𝑥,𝑦) =(1,0)(x,y)=(1,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得等式成立．接下来，考虑 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均不为零的情形．由于 gcd(𝑎,𝑏) =gcd( −𝑎,𝑏) =gcd(𝑎, −𝑏)gcd(a,b)=gcd(−a,b)=gcd(a,−b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以不妨设 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是正数．

考虑辗转相除法的过程，有

𝑎=𝑞1𝑏+𝑟1,0≤𝑟1<𝑏,𝑏=𝑞2𝑟1+𝑟2,0≤𝑟2<𝑟1,𝑟1=𝑞3𝑟2+𝑟3,0≤𝑟3<𝑟2,⋯𝑟𝑛−3=𝑞𝑛−1𝑟𝑛−2+𝑟𝑛−1,0≤𝑟𝑛−1<𝑟𝑛−2,𝑟𝑛−2=𝑞𝑛𝑟𝑛−1+𝑟𝑛,0≤𝑟𝑛<𝑟𝑛−1,𝑟𝑛−1=𝑞𝑛+1𝑟𝑛.a=q1b+r1,0≤r1<b,b=q2r1+r2,0≤r2<r1,r1=q3r2+r3,0≤r3<r2,⋯rn−3=qn−1rn−2+rn−1,0≤rn−1<rn−2,rn−2=qnrn−1+rn,0≤rn<rn−1,rn−1=qn+1rn.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于最大公约数是 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最后一步辗转相除时，一定有 𝑟𝑛 =𝑑rn=d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，倒数第二个等式可以写作

𝑑=𝑟𝑛=𝑟𝑛−2−𝑞𝑛𝑟𝑛−1.d=rn=rn−2−qnrn−1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

从倒数第三个等式中解出

𝑟𝑛−1=𝑟𝑛−3−𝑞𝑛−1𝑟𝑛−2rn−1=rn−3−qn−1rn−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再代入上式，就可以消去 𝑟𝑛−1rn−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑑=𝑟𝑛−2−𝑞𝑛(𝑟𝑛−3−𝑞𝑛−1𝑟𝑛−2)=(1+𝑞𝑛𝑞𝑛−1)𝑟𝑛−2−𝑞𝑛𝑟𝑛−3.d=rn−2−qn(rn−3−qn−1rn−2)=(1+qnqn−1)rn−2−qnrn−3.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

类似地，可以逐步地消去所有 𝑟𝑛−2,𝑟𝑛−3,⋯,𝑟2,𝑟1rn−2,rn−3,⋯,r2,r1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最终得到

𝑑=𝑥𝑎+𝑦𝑏.d=xa+yb.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就证明了存在 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑎𝑥 +𝑏𝑦 =𝑑ax+by=d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．由前文分析可知，这也证明了原命题．

此处，关于存在性的证明是构造性的，它同时给出了该系数的一种计算方法．这一计算方法就是 [扩展欧几里得算法](../gcd/#扩展欧几里得算法)．

考虑裴蜀定理在 gcd(𝑎,𝑏) =1gcd(a,b)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时的特殊情形，可以得到如下推论：

推论

整数 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素，当且仅当存在整数 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑎𝑥 +𝑏𝑦 =1ax+by=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．

### 多个整数的情形

裴蜀定理可以推广到多个整数的情形．

定理

设 𝑎1,𝑎2,⋯,𝑎𝑛a1,a2,⋯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是不全为零的整数．那么，对于任意整数 𝑥1,𝑥2,⋯,𝑥𝑛x1,x2,⋯,xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 gcd(𝑎1,𝑎2,⋯,𝑎𝑛) ∣𝑎1𝑥1 +𝑎2𝑥2 +⋯ +𝑎𝑛𝑥𝑛gcd(a1,a2,⋯,an)∣a1x1+a2x2+⋯+anxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立；而且，存在整数 𝑥1,𝑥2,⋯,𝑥𝑛x1,x2,⋯,xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 gcd(𝑎1,𝑎2,⋯,𝑎𝑛) =𝑎1𝑥1 +𝑎2𝑥2 +⋯ +𝑎𝑛𝑥𝑛gcd(a1,a2,⋯,an)=a1x1+a2x2+⋯+anxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．

证明

利用 gcd(𝑎1,𝑎2,⋯,𝑎𝑛) =gcd(gcd(𝑎1,𝑎2,⋯,𝑎𝑛−1),𝑎𝑛)gcd(a1,a2,⋯,an)=gcd(gcd(a1,a2,⋯,an−1),an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这一点，对 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行归纳即可．

### 例题

[Codeforces 510 D. Fox And Jumping](https://codeforces.com/problemset/problem/510/D)

给出 𝑛 ≤300n≤300![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 张卡片，分别有 𝑙𝑖li![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．在一条无限长的纸带上，你可以选择花 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的钱来购买卡片 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从此以后可以向左或向右跳 𝑙𝑖li![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个单位任意次．问你至少花多少元钱才能够跳到纸带上全部位置．若不行，输出 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解答

分析该问题，发现想要跳到每一个格子上，必须使得所选数 𝑙𝑖1,⋯,𝑙𝑖𝑘li1,⋯,lik![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 通过数次相加或相减得出的绝对值为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．也就是说，存在整数 𝑥1,⋯,𝑥𝑘x1,⋯,xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑙𝑖1𝑥1 +⋯ +𝑙𝑖𝑘𝑥𝑘 =1li1x1+⋯+likxk=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由多个整数的裴蜀定理，这相当于从数组 𝑙1,⋯,𝑙𝑛l1,⋯,ln![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中选择若干个数，满足它们的最大公约数为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，同时要求代价和最小．

**解法 1** ：将最小代价和看作是最短路径问题，可以用 Dijkstra 算法求解．图的顶点处存储了当前的最大公约数的取值．图的起点是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要到达的目标点是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．每走一步，就从当前顶点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发，沿着长度为 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边走到顶点 gcd(𝑥,𝑙𝑖)gcd(x,li)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这一算法的时间复杂度为 𝑂(𝑛2log⁡𝑛)O(n2log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**解法 2** ：从数组 𝑙1,⋯,𝑙𝑛l1,⋯,ln![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 选择若干个数，满足它们的最大公因数为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且代价和最小，由此可以想到 0-1 背包问题．

设 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示考虑前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数且最大公因数为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小代价，则有转移方程：

𝑓𝑖,𝑗=mingcd(𝑘,𝑙𝑖)=𝑗𝑓𝑖−1,𝑘+𝑐𝑖.fi,j=mingcd(k,li)=jfi−1,k+ci.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

DP 后最终的总代价即为 𝑓𝑛,1fn,1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

如同一般的 0-1 背包问题，可以用滚动数组优化，去掉第一维．而这里 300 个数可以组成的最大公约数 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是很稀疏的，可以用哈希表储存．

实际上，这里解法 1 建出的图便是解法 2 中动态规划的状态转移图，解法 2 相当于用动态规划求有向无环图的最短路，因此解法 1 和解法 2 是等价的．但解法 2 无需储存全图，同时 DP 的时间复杂度为 𝑂(𝑛 +𝑚)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，相比 Dijkstra 算法更低，因此解法 2 在时间和空间上更优．

## 一次不定方程

**一次不定方程** （linear Diophantine equation）是形如

𝑎1𝑥1+𝑎2𝑥2+⋯+𝑎𝑛𝑥𝑛=𝑏a1x1+a2x2+⋯+anxn=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的不定方程，其中，𝑎1,𝑎2,⋯,𝑎𝑛a1,a2,⋯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是整数．本节的目标是寻找它的全体整数解．

### 两个变量的情形

首先考虑二元一次不定方程：

𝑎1𝑥1+𝑎2𝑥2=𝑏.a1x1+a2x2=b.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

裴蜀定理指出，该方程有解，当且仅当

𝑑=gcd(𝑎1,𝑎2)∣𝑏.d=gcd(a1,a2)∣b.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

接下来，假设这一条件成立．利用扩展欧几里得算法可以求出方程 𝑎1𝑥1 +𝑎2𝑥2 =𝑑a1x1+a2x2=d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组整数解 (𝑥∗1,𝑥∗2)(x1∗,x2∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由此，可以得到原方程的一组特解

(𝑥∘1,𝑥∘2)=(𝑏𝑑𝑥∗1,𝑏𝑑𝑥∗2).(x1∘,x2∘)=(bdx1∗,bdx2∗).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

要得到全部解，可以考虑将原方程与恒等式 𝑎1𝑥∘1 +𝑎2𝑥∘2 =𝑏a1x1∘+a2x2∘=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相减，就有

𝑎1(𝑥1−𝑥∘1)+𝑎2(𝑥2−𝑥∘2)=0.a1(x1−x1∘)+a2(x2−x2∘)=0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是一个关于 (𝑥1 −𝑥∘1,𝑥2 −𝑥∘2)(x1−x1∘,x2−x2∘)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的齐次一次不定方程，它有通解

(𝑥1−𝑥∘1,𝑥2−𝑥∘2)=(𝑡𝑎2𝑑,−𝑡𝑎1𝑑).(𝑡∈𝐙)(x1−x1∘,x2−x2∘)=(ta2d,−ta1d).(t∈Z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，原方程的通解就是

(𝑥1,𝑥2)=(𝑥∘1+𝑡𝑎2𝑑,𝑥∘2−𝑡𝑎1𝑑).(𝑡∈𝐙)(x1,x2)=(x1∘+ta2d,x2∘−ta1d).(t∈Z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是直线 𝑎1𝑥1 +𝑎2𝑥2 =𝑏a1x1+a2x2=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上一系列等间隔分布的整点．

### 多个变量的情形

解决了二元的情形，多元的情形也就容易解决了．对于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元一次不定方程

𝑎1𝑥1+𝑎2𝑥2+⋯+𝑎𝑛𝑥𝑛=𝑏,(𝑛>3)a1x1+a2x2+⋯+anxn=b,(n>3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由裴蜀定理可知，方程有解当且仅当

gcd(𝑎1,𝑎2,⋯,𝑎𝑛)∣𝑏.gcd(a1,a2,⋯,an)∣b.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

和二元的情形类似，多元一次不定方程的通解同样可以写作

(𝑥∘1,𝑥∘2,⋯,𝑥∘𝑛)+𝑛−1∑𝑘=1𝑡𝑘(𝑥(𝑘)1,𝑥(𝑘)2,⋯,𝑥(𝑘)𝑛)(x1∘,x2∘,⋯,xn∘)+∑k=1n−1tk(x1(k),x2(k),⋯,xn(k))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的形式，其中，𝑥∘x∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为一个特解，𝑥(𝑘)x(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为相应的齐次方程的 (𝑛 −1)(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个解．

要求出通解的具体形式，可以通过将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元方程转化为 (𝑛 −1)(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元方程来完成．不妨设 𝑑1 =gcd(𝑎1,𝑎2)d1=gcd(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，根据裴蜀定理，𝑎1𝑥1 +𝑎2𝑥2a1x1+a2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全体恰为 𝑑1d1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有倍数．因此，可以首先求解 (𝑛 −1)(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元一次不定方程：

𝑑1𝑦1+𝑎3𝑥3+𝑎4𝑥4+⋯+𝑎𝑛𝑥𝑛=𝑏.d1y1+a3x3+a4x4+⋯+anxn=b.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设得到的它的通解为

𝑦1=𝑦∘1+𝑛−1∑𝑘=2𝑡𝑘𝑦(𝑘)1,𝑥𝑖=𝑥∘𝑖+𝑛−1∑𝑘=2𝑡𝑘𝑥(𝑘)𝑖,𝑖=3,⋯,𝑛.y1=y1∘+∑k=2n−1tky1(k),xi=xi∘+∑k=2n−1tkxi(k),i=3,⋯,n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 𝑎1𝑥1 +𝑎2𝑥2 =𝑑1a1x1+a2x2=d1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组特解为 (𝑥∗1,𝑥∗2)(x1∗,x2∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，根据前一节的讨论可知，关于 𝑥1,𝑥2x1,x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二元一次不定方程 𝑎1𝑥1 +𝑎2𝑥2 =𝑑1𝑦1a1x1+a2x2=d1y1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的通解就是

𝑥1=𝑥∗1𝑦1+𝑡1𝑎2𝑑1, 𝑥2=𝑥∗2𝑦1−𝑡1𝑎1𝑑1.x1=x1∗y1+t1a2d1, x2=x2∗y1−t1a1d1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代入 𝑦1y1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表达式，就得到原方程的通解

𝑥1=𝑥∗1𝑦∘1+𝑡1𝑎2𝑑1+𝑛−1∑𝑘=2𝑡𝑘𝑥∗1𝑦(𝑘)1,𝑥2=𝑥∗2𝑦∘1−𝑡1𝑎1𝑑1+𝑛−1∑𝑘=2𝑡𝑘𝑥∗2𝑦(𝑘)1,𝑥𝑖=𝑥∘𝑖+𝑛−1∑𝑘=2𝑡𝑘𝑥(𝑘)𝑖,𝑖=3,⋯,𝑛.x1=x1∗y1∘+t1a2d1+∑k=2n−1tkx1∗y1(k),x2=x2∗y1∘−t1a1d1+∑k=2n−1tkx2∗y1(k),xi=xi∘+∑k=2n−1tkxi(k),i=3,⋯,n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## Frobenius 硬币问题

裴蜀定理给出了一个整数可以由若干个整数线性表出的充分必要条件．与此紧密相关的是 **Frobenius 硬币问题** （Frobenius coin problem）：

  * 如果硬币共有 𝑎1,𝑎2,⋯,𝑎𝑛a1,a2,⋯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等若干种整数面值，且 gcd(𝑎1,𝑎2,⋯,𝑎𝑛) =1gcd(a1,a2,⋯,an)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，不能够由这些硬币组成的最大整数是多少？

同样是在考察整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 什么时候可以表示为 𝑎1𝑥1 +𝑎2𝑥2 +⋯ +𝑎𝑛𝑥𝑛a1x1+a2x2+⋯+anxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，裴蜀定理中 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以是任意整数，而 Frobenius 硬币问题中 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只能是自然数．

只有一种硬币的情形是平凡的，因为只能有 𝑎1 =1a1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所有自然数都可以由它表示．而 𝑛 >2n>2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形又太过复杂，所以，本节仅讨论 𝑛 =2n=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．

### Sylvester 定理

在 1882 年，Sylvester 完全解决了 𝑛 =2n=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时的 Frobenius 硬币问题：

定理（Sylvester）

对于互素的正整数 𝑎1,𝑎2a1,a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不能够写作 𝑎1𝑥1 +𝑎2𝑥2 (𝑥1,𝑥2 ∈𝐍)a1x1+a2x2 (x1,x2∈N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大整数是 𝐶 =𝑎1𝑎2 −𝑎1 −𝑎2C=a1a2−a1−a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而且，对于所有 𝑘 ∈𝐙k∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐶 −𝑘C−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中有且只有一个可以写作该形式．

为表述方便，称可以写作 𝑎1𝑥1 +𝑎2𝑥2 (𝑥1,𝑥2 ∈𝐍)a1x1+a2x2 (x1,x2∈N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 形式的整数为 **可表示的** ．

证明一

由于 𝑎1,𝑎2a1,a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素，对于任意整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，方程 𝑎1𝑥1 +𝑎2𝑥2 =𝑘a1x1+a2x2=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定有解，且通解为

(𝑥1,𝑥2)=(𝑥∘1+𝑡𝑎2,𝑥∘2−𝑡𝑎1).(𝑡∈𝐙)(x1,x2)=(x1∘+ta2,x2∘−ta1).(t∈Z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

取 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑥∘2x2∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作带余除法得到的商，那么，余数 𝑥2 =𝑥∘2 −𝑡𝑎1x2=x2∘−ta1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑎1 −1a1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间．考察此时得到的一组解 (𝑥1,𝑥2)(x1,x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为 𝑥2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是它能够取到的最小非负整数值，所以 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可表示当且仅当 𝑥1 ≥0x1≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**第一步** ：证明大于 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数都是可表示的．

当 𝑘 >𝐶k>C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有

𝑎1𝑥1=𝑘−𝑎2𝑥2>𝐶−𝑎2(𝑎1−1)=−𝑎1.a1x1=k−a2x2>C−a2(a1−1)=−a1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，𝑥1 > −1x1>−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说，𝑥1 ≥0x1≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这说明，(𝑥1,𝑥2)(x1,x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一组自然数解．此时，𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以写作所求形式．

**第二步** ：证明 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不可表示．进而，𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是最大的不可表示的整数，且 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐶 −𝑘C−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并非都可表示的．

反证法．假设 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以表示，即存在 𝑥1,𝑥2 ∈𝐍x1,x2∈N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑎1𝑥1 +𝑎2𝑥2 =𝐶a1x1+a2x2=C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．代入 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表达式，可知

𝑎1𝑎2=𝑎1(𝑥1+1)+𝑎2(𝑥2+1).a1a2=a1(x1+1)+a2(x2+1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，𝑎2 ∣(𝑥1 +1)a2∣(x1+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎1 ∣(𝑥2 +1)a1∣(x2+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．又因为 𝑥1 +1,𝑥2 +1x1+1,x2+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是正数，所以，有

𝑎1𝑎2≥𝑎1𝑎2+𝑎2𝑎1=2𝑎1𝑎2.a1a2≥a1a2+a2a1=2a1a2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

矛盾．这就说明 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不可表示．结合第一步，它也就是不可表示的最大整数．

如果 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐶 −𝑘C−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都可以表示，那么，将 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐶 −𝑘C−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表示中的系数相加就得到 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表示中的系数，这与 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不可表示矛盾，故而 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐶 −𝑘C−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至多只有一个可以表示．

**第三步** ：证明如果 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不可表示，那么 𝐶 −𝑘C−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定是可表示的．

设 (𝑥1,𝑥2)(x1,x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是前文所设的方程 𝑎1𝑥1 +𝑎2𝑥2 =𝑘a1x1+a2x2=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数解．那么，前文已经说明 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不可表示，就等价于 𝑥1 <0x1<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，有

𝐶−𝑘=𝑎1𝑎2−𝑎1−𝑎2−𝑎1𝑥1−𝑎2𝑥2=𝑎1(−1−𝑥1)+𝑎2(𝑎1−1−𝑥2).C−k=a1a2−a1−a2−a1x1−a2x2=a1(−1−x1)+a2(a1−1−x2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，−1 −𝑥1−1−x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑎1 −1 −𝑥2a1−1−x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是非负整数，所以，𝐶 −𝑘C−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以表示．

证明二

此处仅证明 𝐶 =𝑎1𝑎2 −𝑎1 −𝑎2C=a1a2−a1−a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是最大的不可表示的自然数，其余部分的证明类似证明一．

考虑模 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下，每个剩余系中最小的可表示的自然数．因为同一个剩余系中的不同自然数可以通过加减若干个 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互相转化，所以，在讨论最小可表示数时，只需要考虑加减 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的可能性就可以了．由于 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素，所以，每个剩余系中最小的可表示的自然数恰好就是 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数

0, 𝑎1, 2𝑎1, ⋯, (𝑎2−1)𝑎1.0, a1, 2a1, ⋯, (a2−1)a1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，最大的不可表示数为

max0≤𝑖<𝑎2𝑖𝑎1−𝑎2=(𝑎2−1)𝑎1−𝑎2=𝐶.max0≤i<a2ia1−a2=(a2−1)a1−a2=C.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 几何意义

将方程 𝑎1𝑥1 +𝑎2𝑥2 =𝑘a1x1+a2x2=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 看作是一条直线．那么，𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可表示，当且仅当这条直线在第一象限（包括坐标轴）内通过一个整点．当 𝑘 <𝑎𝑏k<ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，这条直线在第一象限至多只能通过一个整点．因此，对于 0 ≤𝑘 <𝑎𝑏0≤k<ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以表示，当且仅当 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在第一象限通过恰好一个整点．

因此，小于等于 𝑘 <𝑎𝑏k<ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且可以表示的自然数的数量，恰好等于第一象限内直线 𝑎1𝑥1 +𝑎2𝑥2 =𝑘a1x1+a2x2=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的整点个数（包含边界上的点）．这一数量就等于

⌊𝑘/𝑎1⌋∑𝑖=0⌊𝑘−𝑖𝑎1𝑎2⌋.∑i=0⌊k/a1⌋⌊k−ia1a2⌋.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是经典的直线下整点问题，可以用 [类欧几里得算法](../euclidean/#类欧几里得算法) 在 𝑂(log⁡min{𝑎1,𝑎2,𝑘})O(log⁡min{a1,a2,k})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间求解．

### 习题

  * [Luogu P3951 NOIP2017 提高组 小凯的疑惑/蓝桥杯 2013 省 买不到的数目](https://www.luogu.com.cn/problem/P3951)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/bezouts.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/bezouts.md "edit.link.title")  
>  __本页面贡献者：[Xeonacid](https://github.com/Xeonacid), [Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [greyqz](https://github.com/greyqz), [MegaOwIer](https://github.com/MegaOwIer), [sshwy](https://github.com/sshwy), [ylxmf2005](https://github.com/ylxmf2005), [buggg-hfc](https://github.com/buggg-hfc), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [ImpleLee](https://github.com/ImpleLee), [monkeysui](https://github.com/monkeysui), [ShizuhaAki](https://github.com/ShizuhaAki), [StudyingFather](https://github.com/StudyingFather), [Sunlight-zero](https://github.com/Sunlight-zero), [TianKong-y](https://github.com/TianKong-y)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
