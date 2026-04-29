# 伯努利数 - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/bernoulli/

# 伯努利数

伯努利数 𝐵𝑛Bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个与数论有密切关联的有理数序列．前几项被发现的伯努利数分别为：

𝐵0 =1,𝐵1 = −12,𝐵2 =16,𝐵3 =0,𝐵4 = −130,…B0=1,B1=−12,B2=16,B3=0,B4=−130,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 等幂求和

伯努利数是由雅各布·伯努利的名字命名的，他在研究 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次幂和的公式时发现了奇妙的关系．我们记

𝑆𝑚(𝑛)=𝑛−1∑𝑘=0𝑘𝑚=0𝑚+1𝑚+⋯+(𝑛−1)𝑚Sm(n)=∑k=0n−1km=0m+1m+⋯+(n−1)m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

伯努利观察了如下一列公式，勾画出一种模式：

𝑆0(𝑛)=𝑛𝑆1(𝑛)=12𝑛2−12𝑛𝑆2(𝑛)=13𝑛3−12𝑛2+16𝑛𝑆3(𝑛)=14𝑛4−12𝑛3+14𝑛2𝑆4(𝑛)=15𝑛5−12𝑛4+13𝑛3−130𝑛S0(n)=nS1(n)=12n2−12nS2(n)=13n3−12n2+16nS3(n)=14n4−12n3+14n2S4(n)=15n5−12n4+13n3−130n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以发现，在 𝑆𝑚(𝑛)Sm(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 𝑛𝑚+1nm+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数总是 1𝑚+11m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑛𝑚nm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数总是 −12−12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑛𝑚−1nm−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数总是 𝑚12m12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑛𝑚−3nm−3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数是 −𝑚(𝑚−1)(𝑚−2)720−m(m−1)(m−2)720![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑛𝑚−4nm−4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数总是零等．

而 𝑛𝑚−𝑘nm−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数总是某个常数乘以 𝑚𝑘――mk―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑚𝑘――mk―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示下降阶乘幂，即 𝑚!(𝑚−𝑘)!m!(m−k)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 递推公式

𝑆𝑚(𝑛)=1𝑚+1(𝐵0𝑛𝑚+1+(𝑚+11)𝐵1𝑛𝑚+⋯+(𝑚+1𝑚)𝐵𝑚𝑛)=1𝑚+1𝑚∑𝑘=0(𝑚+1𝑘)𝐵𝑘𝑛𝑚+1−𝑘Sm(n)=1m+1(B0nm+1+(m+11)B1nm+⋯+(m+1m)Bmn)=1m+1∑k=0m(m+1k)Bknm+1−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

伯努利数由隐含的递推关系定义：

𝑚∑𝑗=0(𝑚+1𝑗)𝐵𝑗=0,(𝑚>0)𝐵0=1∑j=0m(m+1j)Bj=0,(m>0)B0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

例如，(20)𝐵0 +(21)𝐵1 =0(20)B0+(21)B1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，前几个值显然是

𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 77![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| ……![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
---|---|---|---|---|---|---|---|---|---|---  
𝐵𝑛Bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| −12−12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1616![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| −130−130![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 142142![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| −130−130![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| ……![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
  
### 证明

#### 利用归纳法证明

这个证明方法来自 Concrete Mathematics 6.5 BERNOULLI NUMBER．

运用二项式系数的恒等变换和归纳法进行证明：

𝑆𝑚+1(𝑛)+𝑛𝑚+1=𝑛−1∑𝑘=0(𝑘+1)𝑚+1=𝑛−1∑𝑘=0𝑚+1∑𝑗=0(𝑚+1𝑗)𝑘𝑗=𝑚+1∑𝑗=0(𝑚+1𝑗)𝑆𝑗(𝑛)Sm+1(n)+nm+1=∑k=0n−1(k+1)m+1=∑k=0n−1∑j=0m+1(m+1j)kj=∑j=0m+1(m+1j)Sj(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令 ˆ𝑆𝑚(𝑛) =1𝑚+1∑𝑚𝑘=0(𝑚+1𝑘)𝐵𝑘𝑛𝑚+1−𝑘S^m(n)=1m+1∑k=0m(m+1k)Bknm+1−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们希望证明 𝑆𝑚(𝑛) =ˆ𝑆𝑚(𝑛)Sm(n)=S^m(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，假设对 𝑗 ∈[0,𝑚)j∈[0,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑆𝑗(𝑛) =ˆ𝑆𝑗(𝑛)Sj(n)=S^j(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

将原式中两边都减去 𝑆𝑚+1(𝑛)Sm+1(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后可以得到：

𝑆𝑚+1(𝑛)+𝑛𝑚+1=𝑚+1∑𝑗=0(𝑚+1𝑗)𝑆𝑗(𝑛)𝑛𝑚+1=𝑚∑𝑗=0(𝑚+1𝑗)𝑆𝑗(𝑛)=𝑚−1∑𝑗=0(𝑚+1𝑗)ˆ𝑆𝑗(𝑛)+(𝑚+1𝑚)𝑆𝑚(𝑛)Sm+1(n)+nm+1=∑j=0m+1(m+1j)Sj(n)nm+1=∑j=0m(m+1j)Sj(n)=∑j=0m−1(m+1j)S^j(n)+(m+1m)Sm(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

尝试在式子的右边加上 (𝑚+1𝑚)ˆ𝑆𝑚(𝑛) −(𝑚+1𝑚)ˆ𝑆𝑚(𝑛)(m+1m)S^m(n)−(m+1m)S^m(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 再进行化简，可以得到：

𝑛𝑚+1=𝑚∑𝑗=0(𝑚+1𝑗)ˆ𝑆𝑗(𝑛)+(𝑚+1)(𝑆𝑚(𝑛)−ˆ𝑆𝑚(𝑛))nm+1=∑j=0m(m+1j)S^j(n)+(m+1)(Sm(n)−S^m(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

不妨设 Δ =𝑆𝑚(𝑛) −ˆ𝑆𝑚(𝑛)Δ=Sm(n)−S^m(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且将 ˆ𝑆𝑗(𝑛)S^j(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 展开，那么有

𝑛𝑚+1=𝑚∑𝑗=0(𝑚+1𝑗)ˆ𝑆𝑗(𝑛)+(𝑚+1)Δ=𝑚∑𝑗=0(𝑚+1𝑗)1𝑗+1𝑗∑𝑘=0(𝑗+1𝑘)𝐵𝑘𝑛𝑗+1−𝑘+(𝑚+1)Δnm+1=∑j=0m(m+1j)S^j(n)+(m+1)Δ=∑j=0m(m+1j)1j+1∑k=0j(j+1k)Bknj+1−k+(m+1)Δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将第二个 ∑∑![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的求和顺序改为逆向，再将组合数的写法恒等变换可以得到：

𝑛𝑚+1=𝑚∑𝑗=0(𝑚+1𝑗)1𝑗+1𝑗∑𝑘=0(𝑗+1𝑗−𝑘)𝐵𝑗−𝑘𝑛𝑘+1+(𝑚+1)Δ=𝑚∑𝑗=0(𝑚+1𝑗)1𝑗+1𝑗∑𝑘=0(𝑗+1𝑘+1)𝐵𝑗−𝑘𝑛𝑘+1+(𝑚+1)Δ=𝑚∑𝑗=0(𝑚+1𝑗)1𝑗+1𝑗∑𝑘=0𝑗+1𝑘+1(𝑗𝑘)𝐵𝑗−𝑘𝑛𝑘+1+(𝑚+1)Δ=𝑚∑𝑗=0(𝑚+1𝑗)𝑗∑𝑘=0(𝑗𝑘)𝐵𝑗−𝑘𝑘+1𝑛𝑘+1+(𝑚+1)Δnm+1=∑j=0m(m+1j)1j+1∑k=0j(j+1j−k)Bj−knk+1+(m+1)Δ=∑j=0m(m+1j)1j+1∑k=0j(j+1k+1)Bj−knk+1+(m+1)Δ=∑j=0m(m+1j)1j+1∑k=0jj+1k+1(jk)Bj−knk+1+(m+1)Δ=∑j=0m(m+1j)∑k=0j(jk)Bj−kk+1nk+1+(m+1)Δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对两个求和符号进行交换，可以得到：

𝑛𝑚+1=𝑚∑𝑘=0𝑛𝑘+1𝑘+1𝑚∑𝑗=𝑘(𝑚+1𝑗)(𝑗𝑘)𝐵𝑗−𝑘+(𝑚+1)Δnm+1=∑k=0mnk+1k+1∑j=km(m+1j)(jk)Bj−k+(m+1)Δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对 (𝑚+1𝑗)(𝑗𝑘)(m+1j)(jk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行恒等变换：

(𝑚+1𝑗)(𝑗𝑘)＝(𝑚+1𝑘)(𝑚−𝑘+1𝑗−𝑘)(m+1j)(jk)＝(m+1k)(m−k+1j−k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么式子就变成了：

𝑛𝑚+1=𝑚∑𝑘=0𝑛𝑘+1𝑘+1𝑚∑𝑗=𝑘(𝑚+1𝑘)(𝑚−𝑘+1𝑗−𝑘)𝐵𝑗−𝑘+(𝑚+1)Δ=𝑚∑𝑘=0𝑛𝑘+1𝑘+1(𝑚+1𝑘)𝑚∑𝑗=𝑘(𝑚−𝑘+1𝑗−𝑘)𝐵𝑗−𝑘+(𝑚+1)Δnm+1=∑k=0mnk+1k+1∑j=km(m+1k)(m−k+1j−k)Bj−k+(m+1)Δ=∑k=0mnk+1k+1(m+1k)∑j=km(m−k+1j−k)Bj−k+(m+1)Δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将所有的 𝑗 −𝑘j−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 用 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代替，那么就可以得到：

𝑛𝑚+1=𝑚∑𝑘=0𝑛𝑘+1𝑘+1(𝑚+1𝑘)𝑚−𝑘∑𝑗=0(𝑚−𝑘+1𝑗)𝐵𝑗+(𝑚+1)Δnm+1=∑k=0mnk+1k+1(m+1k)∑j=0m−k(m−k+1j)Bj+(m+1)Δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

考虑我们前面提到过的递归关系

𝑚∑𝑗=0(𝑚+1𝑗)𝐵𝑗=0,(𝑚>0)𝐵0=1𝑚∑𝑗=0(𝑚+1𝑗)𝐵𝑗=[𝑚=0]∑j=0m(m+1j)Bj=0,(m>0)B0=1∑j=0m(m+1j)Bj=[m=0]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代入后可以得到：

𝑛𝑚+1=𝑚∑𝑘=0𝑛𝑘+1𝑘+1(𝑚+1𝑘)[𝑚−𝑘=0]+(𝑚+1)Δ=𝑛𝑚+1𝑚+1(𝑚+1𝑚)+(𝑚+1)Δ=𝑛𝑚+1+(𝑚+1)Δnm+1=∑k=0mnk+1k+1(m+1k)[m−k=0]+(m+1)Δ=nm+1m+1(m+1m)+(m+1)Δ=nm+1+(m+1)Δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是 Δ =0Δ=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且有 𝑆𝑚(𝑛) =ˆ𝑆𝑚(𝑛)Sm(n)=S^m(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 利用指数生成函数证明

对递推式 ∑𝑚𝑗=0(𝑚+1𝑗)𝐵𝑗 =[𝑚 =0]∑j=0m(m+1j)Bj=[m=0]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

两边都加上 𝐵𝑚+1Bm+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即得到：

𝑚+1∑𝑗=0(𝑚+1𝑗)𝐵𝑗=[𝑚=0]+𝐵𝑚+1𝑚∑𝑗=0(𝑚𝑗)𝐵𝑗=[𝑚=1]+𝐵𝑚𝑚∑𝑗=0𝐵𝑗𝑗!⋅1(𝑚−𝑗)!=[𝑚=1]+𝐵𝑚𝑚!∑j=0m+1(m+1j)Bj=[m=0]+Bm+1∑j=0m(mj)Bj=[m=1]+Bm∑j=0mBjj!⋅1(m−j)!=[m=1]+Bmm!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 𝐵(𝑧) =∑𝑖≥0𝐵𝑖𝑖!𝑧𝑖B(z)=∑i≥0Bii!zi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，注意到左边为卷积形式，故：

𝐵(𝑧)e𝑧=𝑧+𝐵(𝑧)𝐵(𝑧)=𝑧e𝑧−1B(z)ez=z+B(z)B(z)=zez−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 𝐹𝑛(𝑧) =∑𝑚≥0𝑆𝑚(𝑛)𝑚!𝑧𝑚Fn(z)=∑m≥0Sm(n)m!zm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则：

𝐹𝑛(𝑧)=∑𝑚≥0𝑆𝑚(𝑛)𝑚!𝑧𝑚=∑𝑚≥0𝑛−1∑𝑖=0𝑖𝑚𝑧𝑚𝑚!Fn(z)=∑m≥0Sm(n)m!zm=∑m≥0∑i=0n−1imzmm!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

调换求和顺序：

𝐹𝑛(𝑧)=𝑛−1∑𝑖=0∑𝑚≥0𝑖𝑚𝑧𝑚𝑚!=𝑛−1∑𝑖=0e𝑖𝑧=e𝑛𝑧−1e𝑧−1=𝑧e𝑧−1⋅e𝑛𝑧−1𝑧Fn(z)=∑i=0n−1∑m≥0imzmm!=∑i=0n−1eiz=enz−1ez−1=zez−1⋅enz−1z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代入 𝐵(𝑧) =𝑧e𝑧−1B(z)=zez−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝐹𝑛(𝑧)=𝐵(𝑧)⋅e𝑛𝑧−1𝑧=(∑𝑖≥0𝐵𝑖𝑖!)(∑𝑖≥1𝑛𝑖𝑧𝑖−1𝑖!)=(∑𝑖≥0𝐵𝑖𝑖!)(∑𝑖≥0𝑛𝑖+1𝑧𝑖(𝑖+1)!)Fn(z)=B(z)⋅enz−1z=(∑i≥0Bii!)(∑i≥1nizi−1i!)=(∑i≥0Bii!)(∑i≥0ni+1zi(i+1)!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于 𝐹𝑛(𝑧) =∑𝑚≥0𝑆𝑚(𝑛)𝑚!𝑧𝑚Fn(z)=∑m≥0Sm(n)m!zm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑆𝑚(𝑛) =𝑚![𝑧𝑚]𝐹𝑛(𝑧)Sm(n)=m![zm]Fn(z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑆×𝑚(𝑛)=𝑚![𝑧𝑚]𝐹𝑛(𝑧)=𝑚!𝑚∑𝑖=0𝐵×𝑖𝑖!⋅𝑛𝑚−𝑖+1(𝑚−𝑖+1)!=1𝑚+1𝑚∑𝑖=0(𝑚+1𝑖)𝐵𝑖𝑛𝑚−𝑖+1S×m(n)=m![zm]Fn(z)=m!∑i=0mB×ii!⋅nm−i+1(m−i+1)!=1m+1∑i=0m(m+1i)Binm−i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

故得证．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``` |  ```text using ll = long long ; constexpr int MAXN = 10000 ; constexpr int mod = 1e9 \+ 7 ; ll B [ MAXN ]; // 伯努利数 ll C [ MAXN ][ MAXN ]; // 组合数 ll inv [ MAXN ]; // 逆元（计算伯努利数） void init () { // 预处理组合数 for ( int i = 0 ; i < MAXN ; i ++ ) { C [ i ][ 0 ] = C [ i ][ i ] = 1 ; for ( int k = 1 ; k < i ; k ++ ) { C [ i ][ k ] = ( C [ i \- 1 ][ k ] % mod \+ C [ i \- 1 ][ k \- 1 ] % mod ) % mod ; } } // 预处理逆元 inv [ 1 ] = 1 ; for ( int i = 2 ; i < MAXN ; i ++ ) { inv [ i ] = ( mod \- mod / i ) * inv [ mod % i ] % mod ; } // 预处理伯努利数 B [ 0 ] = 1 ; for ( int i = 1 ; i < MAXN ; i ++ ) { ll ans = 0 ; if ( i == MAXN \- 1 ) break ; for ( int k = 0 ; k < i ; k ++ ) { ans += C [ i \+ 1 ][ k ] * B [ k ]; ans %= mod ; } ans = ( ans * ( \- inv [ i \+ 1 ]) % mod \+ mod ) % mod ; B [ i ] = ans ; } } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/4/25 19:18:16，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/bernoulli.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/bernoulli.md "edit.link.title")  
>  __本页面贡献者：[StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [ShaoChenHeng](https://github.com/ShaoChenHeng), [Aquistcev](https://github.com/Aquistcev), [c-forrest](https://github.com/c-forrest), [Great-designer](https://github.com/Great-designer), [Ir1d](https://github.com/Ir1d), [JiZiQian](https://github.com/JiZiQian), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [OkazakiYumemi](https://github.com/OkazakiYumemi), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
