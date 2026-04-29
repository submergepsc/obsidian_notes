# Min_25 筛 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/min-25/

# Min_25 筛

## 定义

从此种筛法的思想方法来说，其又被称为「Extended Eratosthenes Sieve」．

由于其由 [Min_25](http://min-25.hatenablog.com/) 发明并最早开始使用，故称「Min_25 筛」．

## 性质

其可以在 𝑂(𝑛34log⁡𝑛)O(n34log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 Θ(𝑛1−𝜖)Θ(n1−ϵ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度下解决一类 **积性函数** 的前缀和问题．

要求：𝑓(𝑝)f(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个关于 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以快速求值的完全积性函数之和（例如多项式）；𝑓(𝑝𝑐)f(pc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以快速求值．

## 记号

  * **如无特别说明，本节中所有记为 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的变量的取值集合均为全体质数．**
  * 𝑥/𝑦 :=⌊𝑥𝑦⌋x/y:=⌊xy⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * isprime⁡(𝑛) :=[|{𝑑 :𝑑 ∣𝑛}| =2]isprime⁡(n):=[|{d:d∣n}|=2]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为质数时其值为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，否则为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝑝𝑘pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：全体质数中第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小的质数（如：𝑝1 =2,𝑝2 =3p1=2,p2=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．特别地，令 𝑝0 =1p0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * lpf⁡(𝑛) :=[1 <𝑛]min{𝑝 :𝑝 ∣𝑛} +[1 =𝑛]lpf⁡(n):=[1<n]min{p:p∣n}+[1=n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小质因数．特别地，𝑛 =1n=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，其值为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝐹prime(𝑛) :=∑2≤𝑝≤𝑛𝑓(𝑝)Fprime(n):=∑2≤p≤nf(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝐹𝑘(𝑛) :=∑𝑛𝑖=2[𝑝𝑘 ≤lpf⁡(𝑖)]𝑓(𝑖)Fk(n):=∑i=2n[pk≤lpf⁡(i)]f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 解释

观察 𝐹𝑘(𝑛)Fk(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义，可以发现答案即为 𝐹1(𝑛) +𝑓(1) =𝐹1(𝑛) +1F1(n)+f(1)=F1(n)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑如何求出 𝐹𝑘(𝑛)Fk(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．通过枚举每个 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小质因子及其次数可以得到递推式：

𝐹𝑘(𝑛)=𝑛∑𝑖=2[𝑝𝑘≤lpf⁡(𝑖)]𝑓(𝑖)=∑𝑘≤𝑖𝑝2𝑖≤𝑛∑𝑐≥1𝑝𝑐𝑖≤𝑛𝑓(𝑝𝑐𝑖)([𝑐>1]+𝐹𝑖+1(𝑛/𝑝𝑐𝑖))+∑𝑘≤𝑖𝑝𝑖≤𝑛𝑓(𝑝𝑖)=∑𝑘≤𝑖𝑝2𝑖≤𝑛∑𝑐≥1𝑝𝑐𝑖≤𝑛𝑓(𝑝𝑐𝑖)([𝑐>1]+𝐹𝑖+1(𝑛/𝑝𝑐𝑖))+𝐹prime(𝑛)−𝐹prime(𝑝𝑘−1)=∑𝑘≤𝑖𝑝2𝑖≤𝑛∑𝑐≥1𝑝𝑐+1𝑖≤𝑛(𝑓(𝑝𝑐𝑖)𝐹𝑖+1(𝑛/𝑝𝑐𝑖)+𝑓(𝑝𝑐+1𝑖))+𝐹prime(𝑛)−𝐹prime(𝑝𝑘−1)Fk(n)=∑i=2n[pk≤lpf⁡(i)]f(i)=∑k≤ipi2≤n∑c≥1pic≤nf(pic)([c>1]+Fi+1(n/pic))+∑k≤ipi≤nf(pi)=∑k≤ipi2≤n∑c≥1pic≤nf(pic)([c>1]+Fi+1(n/pic))+Fprime(n)−Fprime(pk−1)=∑k≤ipi2≤n∑c≥1pic+1≤n(f(pic)Fi+1(n/pic)+f(pic+1))+Fprime(n)−Fprime(pk−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

最后一步推导基于这样一个事实：对于满足 𝑝𝑐𝑖 ≤𝑛 <𝑝𝑐+1𝑖pic≤n<pic+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑝𝑐+1𝑖 >𝑛 ⟺ 𝑛/𝑝𝑐𝑖 <𝑝𝑖 <𝑝𝑖+1pic+1>n⟺n/pic<pi<pi+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故 𝐹𝑖+1(𝑛/𝑝𝑐𝑖) =0Fi+1(n/pic)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．  
其边界值即为 𝐹𝑘(𝑛) =0(𝑝𝑘 >𝑛)Fk(n)=0(pk>n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

假设现在已经求出了所有的 𝐹prime(𝑛)Fprime(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么有两种方式可以求出所有的 𝐹𝑘(𝑛)Fk(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

  1. 直接按照递推式计算．
  2. 从大到小枚举 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转移，仅当 𝑝2 <𝑛p2<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时转移增加值不为零，故按照递推式后缀和优化即可．

现在考虑如何计算 𝐹prime(𝑛)Fprime(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．  
观察求 𝐹𝑘(𝑛)Fk(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的过程，容易发现 𝐹primeFprime![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有且仅有 1,2,…,⌊√𝑛⌋,𝑛/√𝑛,…,𝑛/2,𝑛1,2,…,⌊n⌋,n/n,…,n/2,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的点值是有用的．  
一般情况下，𝑓(𝑝)f(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个关于 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的低次多项式，可以表示为 𝑓(𝑝) =∑𝑎𝑖𝑝𝑐𝑖f(p)=∑aipci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．  
那么对于每个 𝑝𝑐𝑖pci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其对 𝐹prime(𝑛)Fprime(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的贡献即为 𝑎𝑖∑2≤𝑝≤𝑛𝑝𝑐𝑖ai∑2≤p≤npci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．  
分开考虑每个 𝑝𝑐𝑖pci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的贡献，问题就转变为了：给定 𝑛,𝑠,𝑔(𝑝) =𝑝𝑠n,s,g(p)=ps![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，对所有的 𝑚 =𝑛/𝑖m=n/i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求 ∑𝑝≤𝑚𝑔(𝑝)∑p≤mg(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注意

𝑔(𝑝) =𝑝𝑠g(p)=ps![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全积性函数！

于是设 𝐺𝑘(𝑛) :=∑𝑛𝑖=2[𝑝𝑘<lpf⁡(𝑖)∨isprime⁡(𝑖)]𝑔(𝑖)Gk(n):=∑i=2n[pk<lpf⁡(i)∨isprime⁡(i)]g(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即埃筛第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轮筛完后剩下的数的 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值之和．  
对于一个合数 𝑥 ≤𝑛x≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，必定有 lpf⁡(𝑥) ≤√𝑥 ≤√𝑛lpf⁡(x)≤x≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设 𝑝ℓ(𝑛)pℓ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为不大于 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大质数，则 ∑2≤𝑝≤𝑛𝑔(𝑝) =𝐺ℓ(𝑛)(𝑛)∑2≤p≤ng(p)=Gℓ(n)(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即在埃筛进行 ℓℓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轮之后剩下的均为质数． 考虑 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边界值，显然为 𝐺0(𝑛) =∑𝑛𝑖=2𝑔(𝑖)G0(n)=∑i=2ng(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．（还记得吗？特别约定了 𝑝0 =1p0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）  
对于转移，考虑埃筛的过程，分开讨论每部分的贡献，有：

  1. 对于 𝑛 <𝑝2𝑘n<pk2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的部分，𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值不变，即 𝐺𝑘(𝑛) =𝐺𝑘−1(𝑛)Gk(n)=Gk−1(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 对于 𝑝2𝑘 ≤𝑛pk2≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的部分，被筛掉的数必有质因子 𝑝𝑘pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 −𝑔(𝑝𝑘)𝐺𝑘−1(𝑛/𝑝𝑘)−g(pk)Gk−1(n/pk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. 对于第二部分，由于 𝑝2𝑘 ≤𝑛 ⟺ 𝑝𝑘 ≤𝑛/𝑝𝑘pk2≤n⟺pk≤n/pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足 lpf⁡(𝑖) <𝑝𝑘lpf⁡(i)<pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 会被额外减去．这部分应当加回来，即 𝑔(𝑝𝑘)𝐺𝑘−1(𝑝𝑘−1)g(pk)Gk−1(pk−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

则有：

𝐺𝑘(𝑛)=𝐺𝑘−1(𝑛)−[𝑝2𝑘≤𝑛]𝑔(𝑝𝑘)(𝐺𝑘−1(𝑛/𝑝𝑘)−𝐺𝑘−1(𝑝𝑘−1))Gk(n)=Gk−1(n)−[pk2≤n]g(pk)(Gk−1(n/pk)−Gk−1(pk−1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 复杂度分析

对于 𝐹𝑘(𝑛)Fk(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算，其第一种方法的时间复杂度被证明为 𝑂(𝑛1−𝜖)O(n1−ϵ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（见朱震霆集训队论文 [《一些特殊的数论函数求和问题》](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2018%E8%AE%BA%E6%96%87%E9%9B%86.pdf) 2.3）；  
对于第二种方法，其本质即为洲阁筛的第二部分，在任之洲论文 [《积性函数求和的几种方法》](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2016%E8%AE%BA%E6%96%87%E9%9B%86.pdf) 中也有提及（6.5.4），其时间复杂度被证明为 𝑂(𝑛34log⁡𝑛)O(n34log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于 𝐹prime(𝑛)Fprime(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算，事实上，其实现与洲阁筛第一部分是相同的．  
考虑对于每个 𝑚 =𝑛/𝑖m=n/i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只有在枚举满足 𝑝2𝑘 ≤𝑚pk2≤m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑝𝑘pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转移时会对时间复杂度产生贡献，则时间复杂度可估计为：

𝑇(𝑛)=∑𝑖2≤𝑛𝑂(𝜋(√𝑖))+∑𝑖2≤𝑛𝑂(𝜋(√𝑛𝑖))=∑𝑖2≤𝑛𝑂(√𝑖ln⁡√𝑖)+∑𝑖2≤𝑛𝑂(√𝑛𝑖ln⁡√𝑛𝑖)=𝑂(∫√𝑛1√𝑛𝑥log⁡√𝑛𝑥d𝑥)=𝑂(𝑛34log⁡𝑛)T(n)=∑i2≤nO(π(i))+∑i2≤nO(π(ni))=∑i2≤nO(iln⁡i)+∑i2≤nO(niln⁡ni)=O(∫1nnxlog⁡nxdx)=O(n34log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于空间复杂度，可以发现不论是 𝐹𝑘Fk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还是 𝐹primeFprime![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其均只在 𝑛/𝑖n/i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处取有效点值，共 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，仅记录有效值即可将空间复杂度优化至 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

首先，通过一次数论分块可以得到所有的有效值，用一个大小为 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数组 lislis![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记录．对于有效值 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，记 id(𝑣)id(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 lislis![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的下标，易得：对于所有有效值 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，id(𝑣) ≤√𝑛id(v)≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

然后分开考虑小于等于 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有效值和大于 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有效值：对于小于等于 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有效值 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，用一个数组 lele![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记录其 id(𝑣)id(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 le𝑣 =id(𝑣)lev=id(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；对于大于 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有效值 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，用一个数组 gege![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记录 id(𝑣)id(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由于 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 过大所以借助 𝑣′ =𝑛/𝑣 <√𝑛v′=n/v<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记录 id(𝑣)id(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 ge𝑣′ =id(𝑣)gev′=id(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这样，就可以使用两个大小为 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数组记录所有有效值的 idid![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 查询．在计算 𝐹𝑘Fk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝐹primeFprime![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，使用有效值的 idid![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代替有效值作为下标，即可将空间复杂度优化至 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 过程

对于 𝐹𝑘(𝑛)Fk(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算，我们实现时一般选择实现难度较低的第一种方法，其在数据规模较小时往往比第二种方法的表现要好；

对于 𝐹prime(𝑛)Fprime(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算，直接按递推式实现即可．

对于 𝑝2𝑘 ≤𝑛pk2≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以用线性筛预处理出 𝑠𝑘 :=𝐹prime(𝑝𝑘)sk:=Fprime(pk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来替代 𝐹𝑘Fk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递推式中的 𝐹prime(𝑝𝑘−1)Fprime(pk−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．  
相应地，𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递推式中的 𝐺𝑘−1(𝑝𝑘−1) =∑𝑘−1𝑖=1𝑔(𝑝𝑖)Gk−1(pk−1)=∑i=1k−1g(pi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也可以用此方法预处理．

用 Extended Eratosthenes Sieve 求 **积性函数** 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀和时，应当明确以下几点：

  * 如何快速（一般是线性时间复杂度）筛出前 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值；
  * 𝑓(𝑝)f(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的多项式表示；
  * 如何快速求出 𝑓(𝑝𝑐)f(pc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

明确上述几点之后按顺序实现以下几部分即可：

  1. 筛出 [1,√𝑛][1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的质数与前 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值；
  2. 对 𝑓(𝑝)f(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 多项式表示中的每一项筛出对应的 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，合并得到 𝐹primeFprime![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个有用点值；
  3. 按照 𝐹𝑘Fk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的递推式实现递归，求出 𝐹1(𝑛)F1(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 例题

[Luogu P4213【模板】杜教筛](https://www.luogu.com.cn/problem/P4213)

求 𝑛∑𝑖=1𝜑(𝑖)∑i=1nφ(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛∑𝑖=1𝜇(𝑖)∑i=1nμ(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解答

对于求 𝜑(𝑖)φ(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀和，首先易知 𝑓(𝑝) =𝑝 −1f(p)=p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于 𝑓(𝑝)f(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一次项 (𝑝)(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑔(𝑝) =𝑝,𝐺0(𝑛) =∑𝑛𝑖=2𝑔(𝑖) =(𝑛+2)(𝑛−1)2g(p)=p,G0(n)=∑i=2ng(i)=(n+2)(n−1)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；对于 𝑓(𝑝)f(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的常数项 ( −1)(−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑔(𝑝) = −1,𝐺0(𝑛) =∑𝑛𝑖=2𝑔(𝑖) = −𝑛 +1g(p)=−1,G0(n)=∑i=2ng(i)=−n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．筛两次加起来即可得到 𝐹primeFprime![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个所需点值．

对于求 𝜇(𝑖)μ(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀和，易知 𝑓(𝑝) = −1f(p)=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．则 𝑔(𝑝) = −1,𝐺0(𝑛) =∑𝑛𝑖=2𝑔(𝑖) = −𝑛 +1g(p)=−1,G0(n)=∑i=2ng(i)=−n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．直接筛即可得到 𝐹primeFprime![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个所需点值．

[LOJ 6053 简单的函数](https://loj.ac/p/6053)

给定 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑓(𝑛)=⎧{ {⎨{ {⎩1𝑛=1𝑝xor⁡𝑐𝑛=𝑝𝑐𝑓(𝑎)𝑓(𝑏)𝑛=𝑎𝑏∧𝑎⟂𝑏f(n)={1n=1pxor⁡cn=pcf(a)f(b)n=ab∧a⟂b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

求 𝑛∑𝑖=1𝑓(𝑖)∑i=1nf(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解答

易知 𝑓(𝑝) =𝑝 −1 +2[𝑝 =2]f(p)=p−1+2[p=2]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．则按照筛 𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方法筛，对 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 讨论一下即可．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 ``` |  ```text /* 「LOJ #6053」简单的函数 */ #include <cmath> #include <iostream> constexpr int MAXS = 200000 ; // 2sqrt(n) constexpr int mod = 1000000007 ; template < typename x_t , typename y_t > void inc ( x_t & x , const y_t & y ) { x += y ; ( mod <= x ) && ( x -= mod ); } template < typename x_t , typename y_t > void dec ( x_t & x , const y_t & y ) { x -= y ; ( x < 0 ) && ( x += mod ); } template < typename x_t , typename y_t > int sum ( const x_t & x , const y_t & y ) { return x \+ y < mod ? x \+ y : ( x \+ y \- mod ); } template < typename x_t , typename y_t > int sub ( const x_t & x , const y_t & y ) { return x < y ? x \- y \+ mod : ( x \- y ); } template < typename _Tp > int div2 ( const _Tp & x ) { return (( x & 1 ) ? x \+ mod : x ) >> 1 ; } // 以上目的均为防负数和取模 template < typename _Tp > long long sqrll ( const _Tp & x ) { // 平方函数 return ( long long ) x * x ; } int pri [ MAXS / 7 ], lpf [ MAXS \+ 1 ], spri [ MAXS \+ 1 ], pcnt ; void sieve ( const int & n ) { for ( int i = 2 ; i <= n ; ++ i ) { if ( lpf [ i ] == 0 ) { // 记录质数 lpf [ i ] = ++ pcnt ; pri [ lpf [ i ]] = i ; spri [ pcnt ] = sum ( spri [ pcnt \- 1 ], i ); // 前缀和 } for ( int j = 1 , v ; j <= lpf [ i ] && ( v = i * pri [ j ]) <= n ; ++ j ) lpf [ v ] = j ; } } long long global_n ; int lim ; int le [ MAXS \+ 1 ], // x <= \sqrt{n} ge [ MAXS \+ 1 ]; // x > \sqrt{n} #define idx(v) (v <= lim ? le[v] : ge[global_n / v]) int G [ MAXS \+ 1 ][ 2 ], Fprime [ MAXS \+ 1 ]; long long lis [ MAXS \+ 1 ]; int cnt ; void init ( const long long & n ) { for ( long long i = 1 , j , v ; i <= n ; i = n / j \+ 1 ) { j = n / i ; v = j % mod ; lis [ ++ cnt ] = j ; ( j <= lim ? le [ j ] : ge [ global_n / j ]) = cnt ; G [ cnt ][ 0 ] = sub ( v , 1l l ); G [ cnt ][ 1 ] = div2 (( long long )( v \+ 2l l ) * ( v \- 1l l ) % mod ); } } void calcFprime () { for ( int k = 1 ; k <= pcnt ; ++ k ) { const int p = pri [ k ]; const long long sqrp = sqrll ( p ); for ( int i = 1 ; lis [ i ] >= sqrp ; ++ i ) { const long long v = lis [ i ] / p ; const int id = idx ( v ); dec ( G [ i ][ 0 ], sub ( G [ id ][ 0 ], k \- 1 )); dec ( G [ i ][ 1 ], ( long long ) p * sub ( G [ id ][ 1 ], spri [ k \- 1 ]) % mod ); } } /* F_prime = G_1 - G_0 */ for ( int i = 1 ; i <= cnt ; ++ i ) Fprime [ i ] = sub ( G [ i ][ 1 ], G [ i ][ 0 ]); } int f_p ( const int & p , const int & c ) { /* f(p^{c}) = p xor c */ return p ^ c ; } int F ( const int & k , const long long & n ) { if ( n < pri [ k ] || n <= 1 ) return 0 ; const int id = idx ( n ); long long ans = Fprime [ id ] \- ( spri [ k \- 1 ] \- ( k \- 1 )); if ( k == 1 ) ans += 2 ; for ( int i = k ; i <= pcnt && sqrll ( pri [ i ]) <= n ; ++ i ) { long long pw = pri [ i ], pw2 = sqrll ( pw ); for ( int c = 1 ; pw2 <= n ; ++ c , pw = pw2 , pw2 *= pri [ i ]) ans += (( long long ) f_p ( pri [ i ], c ) * F ( i \+ 1 , n / pw ) \+ f_p ( pri [ i ], c \+ 1 )) % mod ; } return ans % mod ; } using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> global_n ; lim = sqrt ( global_n ); // 上限 sieve ( lim \+ 1000 ); // 预处理 init ( global_n ); calcFprime (); cout << ( F ( 1 , global_n ) \+ 1l l \+ mod ) % mod << '\n' ; return 0 ; } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/2/8 14:42:40，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/min-25.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/min-25.md "edit.link.title")  
>  __本页面贡献者：[Marcythm](https://github.com/Marcythm), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [MegaOwIer](https://github.com/MegaOwIer), [StudyingFather](https://github.com/StudyingFather), [CSPNOIP](https://github.com/CSPNOIP), [Enter-tainer](https://github.com/Enter-tainer), [HeRaNO](https://github.com/HeRaNO), [aofall](https://github.com/aofall), [Backl1ght](https://github.com/Backl1ght), [c-forrest](https://github.com/c-forrest), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Enoch-xm](https://github.com/Enoch-xm), [Great-designer](https://github.com/Great-designer), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [kenlig](https://github.com/kenlig), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [Persdre](https://github.com/Persdre), [Revltalize](https://github.com/Revltalize), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [shuzhouliu](https://github.com/shuzhouliu), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
