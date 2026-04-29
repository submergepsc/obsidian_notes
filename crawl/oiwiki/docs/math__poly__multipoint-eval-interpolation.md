# 多项式多点求值|快速插值 - OI Wiki

- Source: https://oi-wiki.org/math/poly/multipoint-eval-interpolation/

# 多项式多点求值|快速插值

## 多项式的多点求值

### 描述

给出一个多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点 𝑥1,𝑥2,…,𝑥𝑛x1,x2,…,xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求

𝑓(𝑥1),𝑓(𝑥2),…,𝑓(𝑥𝑛)f(x1),f(x2),…,f(xn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 解法

考虑使用分治来将问题规模减半．

将给定的点分为两部分：

𝑋0={𝑥1,𝑥2,…,𝑥⌊𝑛2⌋}𝑋1={𝑥⌊𝑛2⌋+1,𝑥⌊𝑛2⌋+2,…,𝑥𝑛}X0={x1,x2,…,x⌊n2⌋}X1={x⌊n2⌋+1,x⌊n2⌋+2,…,xn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

构造多项式

𝑔0(𝑥)=∏𝑥𝑖∈𝑋0(𝑥−𝑥𝑖)g0(x)=∏xi∈X0(x−xi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则有 ∀𝑥 ∈𝑋0 :𝑔0(𝑥) =0∀x∈X0:g0(x)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑将 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示为 𝑔0(𝑥)𝑄(𝑥) +𝑓0(𝑥)g0(x)Q(x)+f0(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，即：

𝑓0(𝑥)≡𝑓(𝑥)(mod𝑔0(𝑥))f0(x)≡f(x)(modg0(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则有 ∀𝑥 ∈𝑋0 :𝑓(𝑥) =𝑔0(𝑥)𝑄(𝑥) +𝑓0(𝑥) =𝑓0(𝑥)∀x∈X0:f(x)=g0(x)Q(x)+f0(x)=f0(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑋1X1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同理．

至此，问题的规模被减半，可以使用分治 + 多项式取模解决．

时间复杂度

𝑇(𝑛)=2𝑇(𝑛2)+𝑂(𝑛log⁡𝑛)=𝑂(𝑛log2⁡𝑛)T(n)=2T(n2)+O(nlog⁡n)=O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 多项式的快速插值

### 描述

给出一个 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点的集合

𝑋={(𝑥0,𝑦0),(𝑥1,𝑦1),…,(𝑥𝑛,𝑦𝑛)}X={(x0,y0),(x1,y1),…,(xn,yn)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

求一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得其满足 ∀(𝑥,𝑦) ∈𝑋 :𝑓(𝑥) =𝑦∀(x,y)∈X:f(x)=y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 解法

考虑拉格朗日插值公式

𝑓(𝑥)=𝑛∑𝑖=1∏𝑗≠𝑖𝑥−𝑥𝑗𝑥𝑖−𝑥𝑗𝑦𝑖f(x)=∑i=1n∏j≠ix−xjxi−xjyi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

记多项式 𝑀(𝑥) =∏𝑛𝑖=1(𝑥 −𝑥𝑖)M(x)=∏i=1n(x−xi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由洛必达法则可知

∏𝑗≠𝑖(𝑥𝑖−𝑥𝑗)=lim𝑥→𝑥𝑖∏𝑛𝑗=1(𝑥−𝑥𝑗)𝑥−𝑥𝑖=𝑀′(𝑥𝑖)∏j≠i(xi−xj)=limx→xi∏j=1n(x−xj)x−xi=M′(xi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此多项式被表示为

𝑓(𝑥)=𝑛∑𝑖=1𝑦𝑖𝑀′(𝑥𝑖)∏𝑗≠𝑖(𝑥−𝑥𝑗)f(x)=∑i=1nyiM′(xi)∏j≠i(x−xj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们首先通过分治计算出 𝑀(𝑥)M(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数表示，接着可以通过多点求值在 𝑂(𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内计算出所有的 𝑀′(𝑥𝑖)M′(xi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们令 𝑣𝑖 =𝑦𝑖𝑀′(𝑥𝑖)vi=yiM′(xi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，接下来考虑计算出 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于 𝑛 =1n=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况，有 𝑓(𝑥) =𝑣1,𝑀(𝑥) =𝑥 −𝑥1f(x)=v1,M(x)=x−x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．否则令

𝑓0(𝑥)=⌊𝑛2⌋∑𝑖=1𝑣𝑖∏𝑗≠𝑖∧𝑗≤⌊𝑛2⌋(𝑥−𝑥𝑗)𝑀0(𝑥)=⌊𝑛2⌋∏𝑖=1(𝑥−𝑥𝑖)𝑓1(𝑥)=𝑛∑𝑖=⌊𝑛2⌋+1𝑣𝑖∏𝑗≠𝑖∧⌊𝑛2⌋<𝑗≤𝑛(𝑥−𝑥𝑗)𝑀1(𝑥)=𝑛∏𝑖=⌊𝑛2⌋+1(𝑥−𝑥𝑖)f0(x)=∑i=1⌊n2⌋vi∏j≠i∧j≤⌊n2⌋(x−xj)M0(x)=∏i=1⌊n2⌋(x−xi)f1(x)=∑i=⌊n2⌋+1nvi∏j≠i∧⌊n2⌋<j≤n(x−xj)M1(x)=∏i=⌊n2⌋+1n(x−xi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可得 𝑓(𝑥) =𝑓0(𝑥)𝑀1(𝑥) +𝑓1(𝑥)𝑀0(𝑥),𝑀(𝑥) =𝑀0(𝑥)𝑀1(𝑥)f(x)=f0(x)M1(x)+f1(x)M0(x),M(x)=M0(x)M1(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此可以分治计算，这一部分的复杂度同样是 𝑂(𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/multipoint-eval-interpolation.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/multipoint-eval-interpolation.md "edit.link.title")  
>  __本页面贡献者：[fps5283](https://github.com/fps5283), [Tiphereth-A](https://github.com/Tiphereth-A), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [Enter-tainer](https://github.com/Enter-tainer), [EntropyIncreaser](https://github.com/EntropyIncreaser), [H-J-Granger](https://github.com/H-J-Granger), [ImpleLee](https://github.com/ImpleLee), [Ir1d](https://github.com/Ir1d), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
