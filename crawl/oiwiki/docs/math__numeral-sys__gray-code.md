# 格雷码 - OI Wiki

- Source: https://oi-wiki.org/math/numeral-sys/gray-code/

# 格雷码

格雷码是一个二进制数字系统，其中两个相邻数的二进制位只有一位不同．举个例子，33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位二进制数的格雷码序列为

000,001,011,010,110,111,101,100000,001,011,010,110,111,101,100![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意序列的下标我们以 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为起点，也就是说 𝐺(0) =000,𝐺(4) =110G(0)=000,G(4)=110![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

格雷码由贝尔实验室的 Frank Gray 于 1940 年代提出，并于 1953 年获得专利．

## 构造格雷码（变换）

格雷码的构造方法很多．我们首先介绍手动构造方法，然后会给出构造的代码以及正确性证明．

### 手动构造

𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的格雷码可以通过以下方法构造．我们从全 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 格雷码开始，按照下面策略：

  1. 翻转最低位得到下一个格雷码，（例如 000 →001000→001![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）；
  2. 把最右边的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左边的位翻转得到下一个格雷码，（例如 001 →011001→011![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）；

交替按照上述策略生成 2𝑘−12k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，可得到 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的格雷码序列．

### 镜像构造

𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的格雷码可以从 𝑘 −1k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的格雷码以上下镜射后加上新位的方式快速得到，如下图：

𝑘=101→0110→𝑘=200011110→0001111010110100→𝑘=3000001011010110111101100k=101→0110→k=200011110→0001111010110100→k=3000001011010110111101100![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 计算方法

我们观察一下 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制和 𝐺(𝑛)G(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．可以发现，如果 𝐺(𝑛)G(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，仅当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，第 𝑖 +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或者第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，第 𝑖 +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．于是我们可以当成一个异或的运算，即

𝐺(𝑛)=𝑛⊕⌊𝑛2⌋G(n)=n⊕⌊n2⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

```text 1 ``` |  ```text int g ( int n ) { return n ^ ( n >> 1 ); } ```   
---|---  
  
### 正确性证明

接下来我们证明一下，按照上述公式生成的格雷码序列，相邻两个格雷码的二进制位有且仅有一位不同．

我们考虑 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的区别．把 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，相当于把 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制下末位的连续的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 全部变成取反，然后把最低位的 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变成 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们这样表示 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制位：

(𝑛)2=⋯011⋯11⏟𝑘个(𝑛+1)2=⋯100⋯00⏟𝑘个(n)2=⋯011⋯11⏟k个(n+1)2=⋯100⋯00⏟k个![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是我们在计算 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔(𝑛 +1)g(n+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时侯，后 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位都会变成 100⋯00⏟𝑘个100⋯00⏟k个![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，而第 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位是不同的，因为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 除了后 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位，其他位都是相同的．因此第 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位要么同时异或 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要么同时异或 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．两种情况，第 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位都是不同的．而除了后 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位以外的二进制位也是做相同的异或运算，结果是相同的．

证毕．

## 通过格雷码构造原数（逆变换）

接下来我们考虑格雷码的逆变换，即给你一个格雷码 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要求你找到原数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们考虑从二进制最高位遍历到最低位（最低位下标为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即个位；最高位下标为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．则 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位与 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位 𝑔𝑖gi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的关系如下：

𝑛𝑘=𝑔𝑘𝑛𝑘−1=𝑔𝑘−1⊕𝑛𝑘=𝑔𝑘⊕𝑔𝑘−1𝑛𝑘−2=𝑔𝑘−2⊕𝑛𝑘−1=𝑔𝑘⊕𝑔𝑘−1⊕𝑔𝑘−2𝑛𝑘−3=𝑔𝑘−3⊕𝑛𝑘−2=𝑔𝑘⊕𝑔𝑘−1⊕𝑔𝑘−2⊕𝑔𝑘−3⋮𝑛𝑘−𝑖=𝑖⨁𝑗=0𝑔𝑘−𝑗nk=gknk−1=gk−1⊕nk=gk⊕gk−1nk−2=gk−2⊕nk−1=gk⊕gk−1⊕gk−2nk−3=gk−3⊕nk−2=gk⊕gk−1⊕gk−2⊕gk−3⋮nk−i=⨁j=0igk−j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

```text 1 2 3 4 5 ``` |  ```text int rev_g ( int g ) { int n = 0 ; for (; g ; g >>= 1 ) n ^= g ; return n ; } ```   
---|---  
  
## 实际应用

格雷码有一些十分有用的应用，有些应用让人意想不到：

  * 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位二进制数的格雷码序列可以当作 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维空间中的一个超立方体（二维里的正方形，一维里的单位向量）顶点的哈密尔顿回路，其中格雷码的每一位代表一个维度的坐标．

  * 格雷码被用于最小化数字模拟转换器（比如传感器）的信号传输中出现的错误，因为它每次只改变一个位．

  * 格雷码可以用来解决汉诺塔的问题．

设盘的数量为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位全 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的格雷码 𝐺(0)G(0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始，依次移向下一个格雷码（𝐺(𝑖)G(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 移向 𝐺(𝑖 +1)G(i+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．当前格雷码的二进制第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位表示从小到大第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个盘子．

由于每一次只有一个二进制位会改变，因此当第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位改变时，我们移动第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个盘子．在移动盘子的过程中，除了最小的盘子，其他任意一个盘子在移动的时侯，只能有一个放置选择．在移动第一个盘子的时侯，我们总是有两个放置选择．于是我们的策略如下：

如果 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个奇数，那么盘子的移动路径为 𝑓 →𝑡 →𝑟 →𝑓 →𝑡 →𝑟 →⋯f→t→r→f→t→r→⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是最开始的柱子，𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是最终我们把所有盘子放到的柱子，𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是中间的柱子．

如果 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是偶数：𝑓 →𝑟 →𝑡 →𝑓 →𝑟 →𝑡 →⋯f→r→t→f→r→t→⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 格雷码也在遗传算法理论中得到应用．

## 习题

  * [CSP S2 2019 D1T1](https://www.luogu.com.cn/problem/P5657) Difficulty: easy

  * [SGU #249 Matrix](http://codeforces.com/problemsets/acmsguru/problem/99999/249) Difficulty: medium

> 本页面部分内容译自博文 [Код Грея](http://e-maxx.ru/algo/gray_code) 与其英文翻译版 [Gray code](https://cp-algorithms.com/algebra/gray-code.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．

* * *

>  __本页面最近更新： 2026/1/30 14:50:40，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/numeral-sys/gray-code.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/numeral-sys/gray-code.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [frank-xjh](https://github.com/frank-xjh), [Ir1d](https://github.com/Ir1d), [ouuan](https://github.com/ouuan), [StudyingFather](https://github.com/StudyingFather), [CCXXXI](https://github.com/CCXXXI), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [Henry-ZHR](https://github.com/Henry-ZHR), [mingyEx](https://github.com/mingyEx), [sshwy](https://github.com/sshwy), [Yanjun-Zhao](https://github.com/Yanjun-Zhao), [danni](mailto:lidanni.0606@bytedance.com), [danni](https://github.com/danni), [IgnotaYun](https://github.com/IgnotaYun), [infiWang](https://github.com/infiWang)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
