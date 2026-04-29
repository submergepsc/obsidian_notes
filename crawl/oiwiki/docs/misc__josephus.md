# 约瑟夫问题 - OI Wiki

- Source: https://oi-wiki.org/misc/josephus/

# 约瑟夫问题

约瑟夫问题由来已久，而这个问题的解法也在不断改进，只是目前仍没有一个极其高效的算法（log 以内）解决这个问题．

## 问题描述

> n 个人标号 0,1,⋯,𝑛 −10,1,⋯,n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．逆时针站一圈，从 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号开始，每一次从当前的人逆时针数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，然后让这个人出局．问最后剩下的人是谁．

这个经典的问题由约瑟夫于公元 1 世纪提出，尽管他当时只考虑了 𝑘 =2k=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况．现在我们可以用许多高效的算法解决这个问题．

## 过程

### 朴素算法

最朴素的算法莫过于直接枚举．用一个环形链表枚举删除的过程，重复 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次得到答案．复杂度 Θ(𝑛2)Θ(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 简单优化

寻找下一个人的过程可以用线段树优化．具体地，开一个 0,1,⋯,𝑛 −10,1,⋯,n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线段树，然后记录区间内剩下的人的个数．寻找当前的人的位置以及之后的第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人可以在线段树上二分做．

### 线性算法

设 𝐽𝑛,𝑘Jn,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示规模分别为 𝑛,𝑘n,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约瑟夫问题的答案．我们有如下递归式

𝐽𝑛,𝑘=(𝐽𝑛−1,𝑘+𝑘)mod𝑛Jn,k=(Jn−1,k+k)modn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这个也很好推．你从 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，让第 𝑘 −1k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人出局后剩下 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人，你计算出在 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人中选的答案后，再加一个相对位移 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到真正的答案．这个算法的复杂度显然是 Θ(𝑛)Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

实现

```text 1 2 3 4 5 ``` |  ```text int josephus ( int n , int k ) { int res = 0 ; for ( int i = 1 ; i <= n ; ++ i ) res = ( res \+ k ) % i ; return res ; } ```   
---|---  
  
### 对数算法

对于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 较小 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 较大的情况，本题还有一种复杂度为 Θ(𝑘log⁡𝑛)Θ(klog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的算法．

考虑到我们每次走 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个删一个，那么在一圈以内我们可以删掉 ⌊𝑛𝑘⌋⌊nk⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，然后剩下了 𝑛 −⌊𝑛𝑘⌋n−⌊nk⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人．这时我们在第 ⌊𝑛𝑘⌋ ⋅𝑘⌊nk⌋⋅k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人的位置上．而你发现它等于 𝑛 −𝑛mod𝑘n−nmodk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．于是我们继续递归处理，算完后还原它的相对位置．还原相对位置的依据是：每次做一次删除都会把数到的第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人删除，他们的编号被之后的人逐个继承，也即用 𝑛 −⌊𝑛𝑘⌋n−⌊nk⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 人环算时每 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人即有 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人的位置失算，因此在得数小于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，用还没有被删去 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 倍数编号的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 人环的 的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求模，在得数大于等于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，即可以直接乘 𝑘𝑘−1kk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 于是得到如下的算法：

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text int josephus ( int n , int k ) { if ( n == 1 ) return 0 ; if ( k == 1 ) return n \- 1 ; if ( k > n ) return ( josephus ( n \- 1 , k ) \+ k ) % n ; // 线性算法 int res = josephus ( n \- n / k , k ); res -= n % k ; if ( res < 0 ) res += n ; // mod n else res += res / ( k \- 1 ); // 还原位置 return res ; } ```   
---|---  
  
可以证明这个算法的复杂度是 Θ(𝑘log⁡𝑛)Θ(klog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．我们设这个过程的递归次数是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么每一次问题规模会大致变成 𝑛(1−1𝑘)n(1−1k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，于是得到

𝑛(1−1𝑘)𝑥=1n(1−1k)x=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

解这个方程得到

𝑥=−ln⁡𝑛ln⁡(1−1𝑘)x=−ln⁡nln⁡(1−1k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

下面我们证明该算法的复杂度是 Θ(𝑘log⁡𝑛)Θ(klog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

证明

考虑 lim𝑘→∞𝑘log⁡(1−1𝑘)limk→∞klog⁡(1−1k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们有

lim𝑘→∞𝑘log⁡(1−1𝑘)=lim𝑘→∞log⁡(1−1𝑘)1/𝑘=lim𝑘→∞dd𝑘log⁡(1−1𝑘)dd𝑘(1𝑘)=lim𝑘→∞1𝑘2(1−1𝑘)−1𝑘2=lim𝑘→∞−𝑘𝑘−1=−lim𝑘→∞11−1𝑘=−1limk→∞klog⁡(1−1k)=limk→∞log⁡(1−1k)1/k=limk→∞ddklog⁡(1−1k)ddk(1k)=limk→∞1k2(1−1k)−1k2=limk→∞−kk−1=−limk→∞11−1k=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以 𝑥 ∼𝑘ln⁡𝑛,𝑘 →∞x∼kln⁡n,k→∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 −ln⁡𝑛ln⁡(1−1𝑘) =Θ(𝑘log⁡𝑛)−ln⁡nln⁡(1−1k)=Θ(klog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**本页面主要译自博文[Задача Иосифа](https://e-maxx.ru/algo/joseph_problem) 与其英文翻译版 [Josephus Problem](https://cp-algorithms.com/others/josephus_problem.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/josephus.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/josephus.md "edit.link.title")  
>  __本页面贡献者：[Enter-tainer](https://github.com/Enter-tainer), [sshwy](https://github.com/sshwy), [F1shAndCat](https://github.com/F1shAndCat), [FFjet](https://github.com/FFjet), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
