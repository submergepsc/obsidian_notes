# 杜教筛 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/du/

# 杜教筛

杜教筛被用于处理一类数论函数的前缀和问题．对于数论函数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，杜教筛可以在低于线性时间的复杂度内计算 𝑆(𝑛) =∑𝑛𝑖=1𝑓(𝑖)S(n)=∑i=1nf(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 算法思想

我们想办法构造一个 𝑆(𝑛)S(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 关于 𝑆(⌊𝑛𝑖⌋)S(⌊ni⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的递推式．

对于任意一个数论函数 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，必满足：

𝑛∑𝑖=1(𝑓∗𝑔)(𝑖)=𝑛∑𝑖=1∑𝑑∣𝑖𝑔(𝑑)𝑓(𝑖𝑑)=𝑛∑𝑖=1𝑔(𝑖)𝑆(⌊𝑛𝑖⌋)∑i=1n(f∗g)(i)=∑i=1n∑d∣ig(d)f(id)=∑i=1ng(i)S(⌊ni⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑓 ∗𝑔f∗g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为数论函数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [狄利克雷卷积](../dirichlet/#dirichlet-卷积)．

略证

𝑔(𝑑)𝑓(𝑖𝑑)g(d)f(id)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是对所有 𝑖 ≤𝑛i≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的做贡献，因此变换枚举顺序，枚举 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑖𝑑id![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（分别对应新的 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

𝑛∑𝑖=1∑𝑑∣𝑖𝑔(𝑑)𝑓(𝑖𝑑)=𝑛∑𝑖=1⌊𝑛/𝑖⌋∑𝑗=1𝑔(𝑖)𝑓(𝑗)=𝑛∑𝑖=1𝑔(𝑖)⌊𝑛/𝑖⌋∑𝑗=1𝑓(𝑗)=𝑛∑𝑖=1𝑔(𝑖)𝑆(⌊𝑛𝑖⌋)∑i=1n∑d∣ig(d)f(id)=∑i=1n∑j=1⌊n/i⌋g(i)f(j)=∑i=1ng(i)∑j=1⌊n/i⌋f(j)=∑i=1ng(i)S(⌊ni⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么可以得到递推式：

𝑔(1)𝑆(𝑛)=𝑛∑𝑖=1𝑔(𝑖)𝑆(⌊𝑛𝑖⌋)−𝑛∑𝑖=2𝑔(𝑖)𝑆(⌊𝑛𝑖⌋)=𝑛∑𝑖=1(𝑓∗𝑔)(𝑖)−𝑛∑𝑖=2𝑔(𝑖)𝑆(⌊𝑛𝑖⌋)g(1)S(n)=∑i=1ng(i)S(⌊ni⌋)−∑i=2ng(i)S(⌊ni⌋)=∑i=1n(f∗g)(i)−∑i=2ng(i)S(⌊ni⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

假如我们可以构造恰当的数论函数 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得：

  1. 可以快速计算 ∑𝑛𝑖=1(𝑓 ∗𝑔)(𝑖)∑i=1n(f∗g)(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 可以快速计算 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀和，以用数论分块求解 ∑𝑛𝑖=2𝑔(𝑖)𝑆(⌊𝑛𝑖⌋)∑i=2ng(i)S(⌊ni⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

则我们可以在较短时间内求得 𝑔(1)𝑆(𝑛)g(1)S(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注意

无论数论函数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否为积性函数，只要可以构造出恰当的数论函数 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 便都可以考虑用杜教筛求 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀和．

如考虑 𝑓(𝑛) =i𝜑(𝑛)f(n)=iφ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 显然 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是积性函数，但可取 𝑔(𝑛) =1g(n)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 从而：

𝑛∑𝑘=1(𝑓∗𝑔)(𝑘)=i𝑛(𝑛+1)2∑k=1n(f∗g)(k)=in(n+1)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

计算 ∑𝑘≤𝑚(𝑓 ∗𝑔)(𝑘)∑k≤m(f∗g)(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ∑𝑘≤𝑚𝑔(𝑘)∑k≤mg(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度均为 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 故可以考虑使用杜教筛．

## 时间复杂度

令 𝑅(𝑛) ={⌊𝑛𝑘⌋:𝑘=2,3,…,𝑛}R(n)={⌊nk⌋:k=2,3,…,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．利用数论分块的 [性质](../sqrt-decomposition/#性质) 可知，对任意的 𝑚 ∈𝑅(𝑛)m∈R(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑅(𝑚) ⊆𝑅(𝑛)R(m)⊆R(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．也就是说，使用记忆化之后，只需要对所有 𝑘 ∈𝑅(𝑛)k∈R(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算一次 𝑆(𝑘)S(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就可以得到 𝑅(𝑛)R(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．而这些点的数目 |𝑅(𝑛)| =𝑂(√𝑛)|R(n)|=O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

设计算 ∑𝑛𝑖=1(𝑓 ∗𝑔)(𝑖)∑i=1n(f∗g)(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ∑𝑛𝑖=1𝑔(𝑖)∑i=1ng(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度均为 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 设计算 𝑆(𝑛)S(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度为 𝑇(𝑛)T(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则：

𝑇(𝑛)=∑𝑘∈𝑅(𝑛)𝑇(𝑘)=Θ(√𝑛)+⌊√𝑛⌋∑𝑘=1𝑂(√𝑘)+⌊√𝑛⌋∑𝑘=2𝑂(√𝑛𝑘)=𝑂(∫√𝑛0(√𝑥+√𝑛𝑥)d𝑥)=𝑂(𝑛3/4).T(n)=∑k∈R(n)T(k)=Θ(n)+∑k=1⌊n⌋O(k)+∑k=2⌊n⌋O(nk)=O(∫0n(x+nx)dx)=O(n3/4).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若我们可以预处理出一部分 𝑆(𝑘)S(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 其中 𝑘 =1,2,…,𝑚k=1,2,…,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑚 ≥⌊√𝑛⌋m≥⌊n⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设预处理的时间复杂度为 𝑇0(𝑚)T0(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则此时的 𝑇(𝑛)T(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为：

𝑇(𝑛)=𝑇0(𝑚)+∑𝑘∈𝑅(𝑛);𝑘>𝑚𝑇(𝑘)=𝑇0(𝑚)+⌊𝑛/𝑚⌋∑𝑘=1𝑂(√𝑛𝑘)=𝑂(𝑇0(𝑚)+∫𝑛/𝑚0√𝑛𝑥d𝑥)=𝑂(𝑇0(𝑚)+𝑛√𝑚).T(n)=T0(m)+∑k∈R(n);k>mT(k)=T0(m)+∑k=1⌊n/m⌋O(nk)=O(T0(m)+∫0n/mnxdx)=O(T0(m)+nm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若 𝑇0(𝑚) =𝑂(𝑚)T0(m)=O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（如线性筛），由均值不等式可知：当 𝑚 =Θ(𝑛2/3)m=Θ(n2/3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝑇(𝑛)T(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取得最小值 𝑂(𝑛2/3)O(n2/3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

伪证一例

设计算 𝑆(𝑛)S(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度为 𝑇(𝑛)T(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则有：

𝑇(𝑛)=Θ(√𝑛)+𝑂⎛⎜ ⎜⎝⌊√𝑛⌋∑𝑖=2𝑇(⌊𝑛𝑖⌋)⎞⎟ ⎟⎠T(n)=Θ(n)+O(∑i=2⌊n⌋T(⌊ni⌋))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 𝑇(⌊𝑛𝑖⌋)=Θ(√𝑛𝑖)+𝑂⎛⎜ ⎜ ⎜⎝⌊√𝑛/𝑖⌋∑𝑗=2𝑇(⌊𝑛𝑖𝑗⌋)⎞⎟ ⎟ ⎟⎠=𝑂(√𝑛𝑖)T(⌊ni⌋)=Θ(ni)+O(∑j=2⌊n/i⌋T(⌊nij⌋))=O(ni)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑂(∑⌊√𝑛/𝑖⌋𝑗=2𝑇(⌊𝑛𝑖𝑗⌋))O(∑j=2⌊n/i⌋T(⌊nij⌋))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 视作高阶无穷小，从而可以舍去．故：

𝑇(𝑛)=Θ(√𝑛)+𝑂⎛⎜ ⎜⎝⌊√𝑛⌋∑𝑖=2√𝑛𝑖⎞⎟ ⎟⎠=𝑂⎛⎜ ⎜⎝⌊√𝑛⌋∑𝑖=1√𝑛𝑖⎞⎟ ⎟⎠=𝑂(∫√𝑛0√𝑛𝑥d𝑥)=𝑂(𝑛3/4)T(n)=Θ(n)+O(∑i=2⌊n⌋ni)=O(∑i=1⌊n⌋ni)=O(∫0nnxdx)=O(n3/4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) Bug

问题在于「视作高阶无穷小，从而可以舍去」这一处．我们将 𝑇(⌊𝑛𝑖⌋)T(⌊ni⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代入 𝑇(𝑛)T(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的式子里，有：

𝑇(𝑛)=Θ(√𝑛)+𝑂⎛⎜ ⎜⎝⌊√𝑛⌋∑𝑖=2√𝑛𝑖⎞⎟ ⎟⎠+𝑂⎛⎜ ⎜ ⎜⎝⌊√𝑛⌋∑𝑖=2⌊√𝑛/𝑖⌋∑𝑗=2𝑇(⌊𝑛𝑖𝑗⌋)⎞⎟ ⎟ ⎟⎠=𝑂(√𝑛+∫√𝑛0√𝑛𝑥d𝑥)+𝑂⎛⎜ ⎜ ⎜⎝⌊√𝑛⌋∑𝑖=2⌊√𝑛/𝑖⌋∑𝑗=2𝑇(⌊𝑛𝑖𝑗⌋)⎞⎟ ⎟ ⎟⎠=𝑂(𝑛3/4)+𝑂⎛⎜ ⎜ ⎜⎝⌊√𝑛⌋∑𝑖=2⌊√𝑛/𝑖⌋∑𝑗=2𝑇(⌊𝑛𝑖𝑗⌋)⎞⎟ ⎟ ⎟⎠T(n)=Θ(n)+O(∑i=2⌊n⌋ni)+O(∑i=2⌊n⌋∑j=2⌊n/i⌋T(⌊nij⌋))=O(n+∫0nnxdx)+O(∑i=2⌊n⌋∑j=2⌊n/i⌋T(⌊nij⌋))=O(n3/4)+O(∑i=2⌊n⌋∑j=2⌊n/i⌋T(⌊nij⌋))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们考虑 ⌊√𝑛⌋∑𝑖=2⌊√𝑛/𝑖⌋∑𝑗=2𝑇(⌊𝑛𝑖𝑗⌋)∑i=2⌊n⌋∑j=2⌊n/i⌋T(⌊nij⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这部分，不难发现：

⌊√𝑛⌋∑𝑖=2⌊√𝑛/𝑖⌋∑𝑗=2𝑇(⌊𝑛𝑖𝑗⌋)=Ω⎛⎜ ⎜⎝⌊√𝑛⌋∑𝑖=2𝑇⎛⎜ ⎜⎝⎢ ⎢ ⎢⎣𝑛𝑖⋅⌊√𝑛𝑖⌋−1⎥ ⎥ ⎥⎦⎞⎟ ⎟⎠⎞⎟ ⎟⎠=Ω⎛⎜ ⎜⎝⌊√𝑛⌋∑𝑖=2𝑇(⌊√𝑛𝑖⌋)⎞⎟ ⎟⎠∑i=2⌊n⌋∑j=2⌊n/i⌋T(⌊nij⌋)=Ω(∑i=2⌊n⌋T(⌊ni⋅⌊ni⌋−1⌋))=Ω(∑i=2⌊n⌋T(⌊ni⌋))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于没有引入记忆化，因此上式中的 𝑇(⌊√𝑛𝑖⌋)T(⌊ni⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仍然是 Ω((𝑛𝑖)1/4)Ω((ni)1/4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，进而所谓的「高阶无穷小」部分是不可以舍去的．

实际上杜教筛的亚线性时间复杂度是由记忆化保证的．只有使用了记忆化之后才能保证不会出现那个多重求和的项．

## 例题

### 问题一

[P4213【模板】杜教筛（Sum）](https://www.luogu.com.cn/problem/P4213)

求 𝑆1(𝑛) =∑𝑛𝑖=1𝜇(𝑖)S1(n)=∑i=1nμ(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑆2(𝑛) =∑𝑛𝑖=1𝜑(𝑖)S2(n)=∑i=1nφ(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，1 ≤𝑛 <2311≤n<231![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

莫比乌斯函数前缀和欧拉函数前缀和

我们知道：

𝜖=[𝑛=1]=𝜇∗1=∑𝑑∣𝑛𝜇(𝑑)ϵ=[n=1]=μ∗1=∑d∣nμ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑆1(𝑛)=𝑛∑𝑖=1𝜖(𝑖)−𝑛∑𝑖=2𝑆1(⌊𝑛𝑖⌋)=1−𝑛∑𝑖=2𝑆1(⌊𝑛𝑖⌋)S1(n)=∑i=1nϵ(i)−∑i=2nS1(⌊ni⌋)=1−∑i=2nS1(⌊ni⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

时间复杂度的推导见 时间复杂度 一节．

对于较大的值，需要用 `map`/`unordered_map` 存下其对应的值，方便以后使用时直接使用之前计算的结果．

当然也可以用杜教筛求出 𝜑(𝑥)φ(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀和，但是更好的方法是应用莫比乌斯反演．

莫比乌斯反演杜教筛

𝑛∑𝑖=1𝑛∑𝑗=1[gcd(𝑖,𝑗)=1]=𝑛∑𝑖=1𝑛∑𝑗=1∑𝑑∣𝑖,𝑑∣𝑗𝜇(𝑑)=𝑛∑𝑑=1𝜇(𝑑)⌊𝑛𝑑⌋2∑i=1n∑j=1n[gcd(i,j)=1]=∑i=1n∑j=1n∑d∣i,d∣jμ(d)=∑d=1nμ(d)⌊nd⌋2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于题目所求的是 ∑𝑛𝑖=1∑𝑖𝑗=1[gcd(𝑖,𝑗) =1]∑i=1n∑j=1i[gcd(i,j)=1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 所以我们排除掉 𝑖 =1,𝑗 =1i=1,j=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况，并将结果除以 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

观察到，只需求出莫比乌斯函数的前缀和，就可以快速计算出欧拉函数的前缀和了．时间复杂度 𝑂(𝑛23)O(n23)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

求 𝑆(𝑛) =∑𝑛𝑖=1𝜑(𝑖)S(n)=∑i=1nφ(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

同样的，𝜑 ∗1 =idφ∗1=id![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 从而：

𝑆(𝑛)=𝑛∑𝑖=1𝑖−𝑛∑𝑖=2𝑆(⌊𝑛𝑖⌋)=12𝑛(𝑛+1)−𝑛∑𝑖=2𝑆(⌊𝑛𝑖⌋)S(n)=∑i=1ni−∑i=2nS(⌊ni⌋)=12n(n+1)−∑i=2nS(⌊ni⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代码实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 ``` |  ```text #include <cstring> #include <iostream> #include <map> using namespace std ; constexpr int MAXN = 2000010 ; long long T , n , pri [ MAXN ], cur , mu [ MAXN ], sum_mu [ MAXN ]; bool vis [ MAXN ]; map < long long , long long > mp_mu ; long long S_mu ( long long x ) { // 求mu的前缀和 if ( x < MAXN ) return sum_mu [ x ]; if ( mp_mu [ x ]) return mp_mu [ x ]; // 如果map中已有该大小的mu值，则可直接返回 long long ret = ( long long ) 1 ; for ( long long i = 2 , j ; i <= x ; i = j \+ 1 ) { j = x / ( x / i ); ret -= S_mu ( x / i ) * ( j \- i \+ 1 ); } return mp_mu [ x ] = ret ; // 路径压缩，方便下次计算 } long long S_phi ( long long x ) { // 求phi的前缀和 long long ret = ( long long ) 0 ; long long j ; for ( long long i = 1 ; i <= x ; i = j \+ 1 ) { j = x / ( x / i ); ret += ( S_mu ( j ) \- S_mu ( i \- 1 )) * ( x / i ) * ( x / i ); } return ( ret \- 1 ) / 2 \+ 1 ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> T ; mu [ 1 ] = 1 ; for ( int i = 2 ; i < MAXN ; i ++ ) { // 线性筛预处理mu数组 if ( ! vis [ i ]) { pri [ ++ cur ] = i ; mu [ i ] = -1 ; } for ( int j = 1 ; j <= cur && i * pri [ j ] < MAXN ; j ++ ) { vis [ i * pri [ j ]] = true ; if ( i % pri [ j ]) mu [ i * pri [ j ]] = \- mu [ i ]; else { mu [ i * pri [ j ]] = 0 ; break ; } } } for ( int i = 1 ; i < MAXN ; i ++ ) sum_mu [ i ] = sum_mu [ i \- 1 ] \+ mu [ i ]; // 求mu数组前缀和 while ( T \-- ) { cin >> n ; cout << S_phi ( n ) << ' ' << S_mu ( n ) << '\n' ; } return 0 ; } ```   
---|---  
  
### 问题二

[「LuoguP3768」简单的数学题](https://www.luogu.com.cn/problem/P3768)

大意：求

𝑛∑𝑖=1𝑛∑𝑗=1𝑖⋅𝑗⋅gcd(𝑖,𝑗)(mod𝑝)∑i=1n∑j=1ni⋅j⋅gcd(i,j)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑛 ≤1010,5 ×108 ≤𝑝 ≤1.1 ×109n≤1010,5×108≤p≤1.1×109![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是质数．

利用 𝜑 ∗1 =idφ∗1=id![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 做莫比乌斯反演化为：

𝑛∑𝑑=1𝐹2(⌊𝑛𝑑⌋)⋅𝑑2𝜑(𝑑)∑d=1nF2(⌊nd⌋)⋅d2φ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝐹(𝑛) =12𝑛(𝑛 +1)F(n)=12n(n+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对 ∑𝑛𝑑=1𝐹(⌊𝑛𝑑⌋)2∑d=1nF(⌊nd⌋)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 做数论分块，𝑑2𝜑(𝑑)d2φ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀和用杜教筛处理：

𝑓(𝑛)=𝑛2𝜑(𝑛)=(id2⁡𝜑)(𝑛)f(n)=n2φ(n)=(id2⁡φ)(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑆(𝑛)=𝑛∑𝑖=1𝑓(𝑖)=𝑛∑𝑖=1(id2⁡𝜑)(𝑖)S(n)=∑i=1nf(i)=∑i=1n(id2⁡φ)(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

需要构造积性函数 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑓 ×𝑔f×g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能快速求和．

单纯的 𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀和可以用 𝜑 ∗1φ∗1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的杜教筛处理，但是这里的 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 多了一个 id2id2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么我们就卷一个 id2id2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上去，让它变成常数：

𝑆(𝑛)=𝑛∑𝑖=1((id2⁡𝜑)∗id2)(𝑖)−𝑛∑𝑖=2id2⁡(𝑖)𝑆(⌊𝑛𝑖⌋)S(n)=∑i=1n((id2⁡φ)∗id2)(i)−∑i=2nid2⁡(i)S(⌊ni⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

化一下卷积：

((id2⁡𝜑)∗id2)(𝑖)=∑𝑑∣𝑖(id2⁡𝜑)(𝑑)id2⁡(𝑖𝑑)=∑𝑑∣𝑖𝑑2𝜑(𝑑)(𝑖𝑑)2=∑𝑑∣𝑖𝑖2𝜑(𝑑)=𝑖2∑𝑑∣𝑖𝜑(𝑑)=𝑖2(𝜑∗1)(𝑖)=𝑖3((id2⁡φ)∗id2)(i)=∑d∣i(id2⁡φ)(d)id2⁡(id)=∑d∣id2φ(d)(id)2=∑d∣ii2φ(d)=i2∑d∣iφ(d)=i2(φ∗1)(i)=i3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再化一下 𝑆(𝑛)S(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7):

𝑆(𝑛)=𝑛∑𝑖=1((id2⁡𝜑)∗id2)(𝑖)−𝑛∑𝑖=2id2⁡(𝑖)𝑆(⌊𝑛𝑖⌋)=𝑛∑𝑖=1𝑖3−𝑛∑𝑖=2𝑖2𝑆(⌊𝑛𝑖⌋)=(12𝑛(𝑛+1))2−𝑛∑𝑖=2𝑖2𝑆(⌊𝑛𝑖⌋)S(n)=∑i=1n((id2⁡φ)∗id2)(i)−∑i=2nid2⁡(i)S(⌊ni⌋)=∑i=1ni3−∑i=2ni2S(⌊ni⌋)=(12n(n+1))2−∑i=2ni2S(⌊ni⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

分块求解即可．

代码实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 ``` |  ```text // 不要为了省什么内存把数组开小,会卡80 #include <cmath> #include <iostream> #include <map> using namespace std ; constexpr int N = 5e6 , NP = 5e6 , SZ = N ; long long n , P , inv2 , inv6 , s [ N ]; int phi [ N ], p [ NP ], cnt , pn ; bool bp [ N ]; map < long long , long long > s_map ; long long ksm ( long long a , long long m ) { // 求逆元用 long long res = 1 ; while ( m ) { if ( m & 1 ) res = res * a % P ; a = a * a % P , m >>= 1 ; } return res ; } void prime_work ( int k ) { // 线性筛phi，s bp [ 0 ] = bp [ 1 ] = true , phi [ 1 ] = 1 ; for ( int i = 2 ; i <= k ; i ++ ) { if ( ! bp [ i ]) p [ ++ cnt ] = i , phi [ i ] = i \- 1 ; for ( int j = 1 ; j <= cnt && i * p [ j ] <= k ; j ++ ) { bp [ i * p [ j ]] = true ; if ( i % p [ j ] == 0 ) { phi [ i * p [ j ]] = phi [ i ] * p [ j ]; break ; } else phi [ i * p [ j ]] = phi [ i ] * phi [ p [ j ]]; } } for ( int i = 1 ; i <= k ; i ++ ) s [ i ] = ( 1l l * i * i % P * phi [ i ] % P \+ s [ i \- 1 ]) % P ; } long long s3 ( long long k ) { // 立方和 return k %= P , ( k * ( k \+ 1 ) / 2 ) % P * (( k * ( k \+ 1 ) / 2 ) % P ) % P ; } long long s2 ( long long k ) { // 平方和 return k %= P , k * ( k \+ 1 ) % P * ( k * 2 \+ 1 ) % P * inv6 % P ; } long long calc ( long long k ) { // 计算S(k) if ( k <= pn ) return s [ k ]; if ( s_map [ k ]) return s_map [ k ]; // 对于超过pn的用map离散存储 long long res = s3 ( k ), pre = 1 , cur ; for ( long long i = 2 , j ; i <= k ; i = j \+ 1 ) j = k / ( k / i ), cur = s2 ( j ), res = ( res \- calc ( k / i ) * ( cur \- pre ) % P ) % P , pre = cur ; return s_map [ k ] = ( res \+ P ) % P ; } long long solve () { long long res = 0 , pre = 0 , cur ; for ( long long i = 1 , j ; i <= n ; i = j \+ 1 ) { j = n / ( n / i ); cur = calc ( j ); res = ( res \+ ( s3 ( n / i ) * ( cur \- pre )) % P ) % P ; pre = cur ; } return ( res \+ P ) % P ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> P >> n ; inv2 = ksm ( 2 , P \- 2 ), inv6 = ksm ( 6 , P \- 2 ); pn = ( long long ) pow ( n , 0.666667 ); // n^(2/3) prime_work ( pn ); cout << solve (); return 0 ; } ```   
---|---  
  
### 参考资料

  1. 任之洲，2016，《积性函数求和的几种方法》，2016 年信息学奥林匹克中国国家队候选队员论文
  2. [杜教筛的时空复杂度分析 - riteme.site](https://riteme.site/blog/2018-9-11/time-space-complexity-dyh-algo.html)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/du.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/du.md "edit.link.title")  
>  __本页面贡献者：[StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [hsfzLZH1](https://github.com/hsfzLZH1), [Ir1d](https://github.com/Ir1d), [Enter-tainer](https://github.com/Enter-tainer), [sshwy](https://github.com/sshwy), [c-forrest](https://github.com/c-forrest), [Marcythm](https://github.com/Marcythm), [MegaOwIer](https://github.com/MegaOwIer), [Henry-ZHR](https://github.com/Henry-ZHR), [Xeonacid](https://github.com/Xeonacid), [Backl1ght](https://github.com/Backl1ght), [Great-designer](https://github.com/Great-designer), [huayucaiji](https://github.com/huayucaiji), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [Menci](https://github.com/Menci), [Nanarikom](https://github.com/Nanarikom), [nanmenyangde](https://github.com/nanmenyangde), [ouuan](https://github.com/ouuan), [purple-vine](https://github.com/purple-vine), [shawlleyw](https://github.com/shawlleyw), [Sshwy](mailto:hwy1272918035@outlook.com)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
