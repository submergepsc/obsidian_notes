# Meissel–Lehmer 算法 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/meissel-lehmer/

# Meissel–Lehmer 算法

「Meissel–Lehmer 算法」是一种能在亚线性时间复杂度内求出 1 ∼𝑛1∼n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内质数个数的一种算法．

## 记号规定

[𝑥][x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示对 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下取整得到的结果．  
𝑝𝑘pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个质数，𝑝1 =2p1=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．  
𝜋(𝑥)π(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 1 ∼𝑥1∼x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 范围内素数的个数．  
𝜇(𝑥)μ(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示莫比乌斯函数．  
对于集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，#𝑆#S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小．  
𝛿(𝑥)δ(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小的质因子．  
𝑃+(𝑥)P+(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最大的质因子．

## Meissel–Lehmer 算法求 π(x)

定义 𝜙(𝑥,𝑎)ϕ(x,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为所有小于 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正整数中满足其所有质因子都大于 𝑝𝑎pa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数的个数，即：

𝜙(𝑥,𝑎)=#{𝑛≤𝑥∣𝑛mod𝑝=0⟹𝑝>𝑝𝑎}(1)(1)ϕ(x,a)=#{n≤x∣nmodp=0⟹p>pa}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再定义 𝑃𝑘(𝑥,𝑎)Pk(x,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示为所有小于 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正整数中满足可重质因子恰好有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个且所有质因子都大于 𝑝𝑎pa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数的个数，即：

𝑃𝑘(𝑥,𝑎)=#{𝑛≤𝑥∣𝑛=𝑞1𝑞2⋯𝑞𝑘⟹∀𝑖,𝑞𝑖>𝑝𝑎}(2)(2)Pk(x,a)=#{n≤x∣n=q1q2⋯qk⟹∀i,qi>pa}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

特殊的，我们定义：𝑃0(𝑥,𝑎) =1P0(x,a)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如此便有：

𝜙(𝑥,𝑎)=𝑃0(𝑥,𝑎)+𝑃1(𝑥,𝑎)+⋯+𝑃𝑘(𝑥,𝑎)+⋯ϕ(x,a)=P0(x,a)+P1(x,a)+⋯+Pk(x,a)+⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这个无限和式实际上是可以表示为有限和式的，因为在 𝑝𝑘𝑎 >𝑥pak>x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有 𝑃𝑘(𝑥,𝑎) =0Pk(x,a)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

设 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为满足 𝑥1/3 ≤𝑦 ≤𝑥1/2x1/3≤y≤x1/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数，再记 𝑎 =𝜋(𝑦)a=π(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在 𝑘 ≥3k≥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有 𝑃1(𝑥,𝑎) =𝜋(𝑥) −𝑎P1(x,a)=π(x)−a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑃𝑘(𝑥,𝑎) =0Pk(x,a)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由此我们可以推出：

𝜋(𝑥)=𝜙(𝑥,𝑎)+𝑎−1−𝑃2(𝑥,𝑎)(3)(3)π(x)=ϕ(x,a)+a−1−P2(x,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这样，计算 𝜋(𝑥)π(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 便可以转化为计算 𝜙(𝑥,𝑎)ϕ(x,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑃2(𝑥,𝑎)P2(x,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 计算 P₂(x,a)

由等式 (2)(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 我们可以得出 𝑃2(𝑥,𝑎)P2(x,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等于满足 𝑦 <𝑝 ≤𝑞y<p≤q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑝𝑞 ≤𝑥pq≤x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的质数对 (𝑝,𝑞)(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数．

首先我们注意到 𝑝 ∈[𝑦+1,√𝑥]p∈[y+1,x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此外，对于每个 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们都有 𝑞 ∈[𝑝,𝑥/𝑝]q∈[p,x/p]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此：

𝑃2(𝑥,𝑎)=∑𝑦<𝑝≤√𝑥(𝜋(𝑥𝑝)−𝜋(𝑝)+1)(4)(4)P2(x,a)=∑y<p≤x(π(xp)−π(p)+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当 𝑝 ∈[𝑦+1,√𝑥]p∈[y+1,x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，我们有 𝑥𝑝 ∈[1,𝑥𝑦]xp∈[1,xy]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，我们可以筛区间 [1,𝑥𝑦][1,xy]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后对于所有的质数 𝑝 ∈[𝑦+1,√𝑥]p∈[y+1,x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算 𝜋(𝑥𝑝) −𝜋(𝑝) +1π(xp)−π(p)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．为了减少上述算法的空间复杂度，我们可以考虑分块，块长为 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．若块长 𝐿 =𝑦L=y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则我们可以在 𝑂(𝑥𝑦log⁡log⁡𝑥)O(xylog⁡log⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度，𝑂(𝑦)O(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的空间复杂度内计算 𝑃2(𝑥,𝑎)P2(x,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 计算 ϕ(x,a)

对于 𝑏 ≤𝑎b≤a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，考虑所有不超过 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正整数，满足它的所有质因子都大于 𝑝𝑏−1pb−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这些数可以被分为两类：

  1. 可以被 𝑝𝑏pb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除的；
  2. 不可以被 𝑝𝑏pb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除的．

属于第 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类的数有 𝜙(𝑥𝑝𝑏,𝑏−1)ϕ(xpb,b−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，属于第二类的数有 𝜙(𝑥,𝑏)ϕ(x,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．

因此我们得出结论：

> **定理 5.15.1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：** 函数 𝜙ϕ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足下列性质
> 
> 𝜙(𝑢,0)=[𝑢](5)(5)ϕ(u,0)=[u]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝜙(𝑥,𝑏)=𝜙(𝑥,𝑏−1)−𝜙(𝑥𝑝𝑏,𝑏−1)(6)(6)ϕ(x,b)=ϕ(x,b−1)−ϕ(xpb,b−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

计算 𝜙(𝑥,𝑎)ϕ(x,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的简单方法可以从这个定理推导出来：我们重复使用等式 (7)(7)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，知道最后得到 𝜙(𝑢,0)ϕ(u,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这个过程可以看作从根节点 𝜙(𝑥,𝑎)ϕ(x,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始创建有根二叉树，图 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 画出了这一过程．通过这种方法，我们得到如下公式：

𝜙(𝑥,𝑎)=∑1≤𝑛≤𝑥𝑃+(𝑛)≤𝑦𝜇(𝑛)[𝑥/𝑛]ϕ(x,a)=∑1≤n≤xP+(n)≤yμ(n)[x/n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝜙(𝑥,𝑎)↙↘𝜙(𝑥,𝑎−1)−𝜙(𝑥𝑝𝑎,𝑎−1)↙↓↓↘𝜙(𝑥,𝑎−2)𝜙(𝑥𝑝𝑎−1,𝑎−2)−𝜙(𝑥𝑝𝑎,𝑎−2)𝜙(𝑥𝑝𝑎𝑝𝑎−1,𝑎−2)⋮ϕ(x,a)↙↘ϕ(x,a−1)−ϕ(xpa,a−1)↙↓↓↘ϕ(x,a−2)ϕ(xpa−1,a−2)−ϕ(xpa,a−2)ϕ(xpapa−1,a−2)⋮![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

上图表示计算 𝜙(𝑥,𝑎)ϕ(x,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 过程的二叉树：叶子节点权值之和就是 𝜙(𝑥,𝑎)ϕ(x,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

但是，这样需要计算太多东西．因为 𝑦 ≥𝑥1/3y≥x1/3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，仅仅计算为 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 不超过 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 质数的乘积的数，如果按照这个方法计算，会有至少 𝑥log3⁡𝑥xlog3⁡x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个项，没有办法我们对复杂度的需求．

为了限制这个二叉树的「生长」，我们要改变原来的终止条件．这是原来的终止条件．

> **终止条件 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：** 如果 𝑏 =0b=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则不要再对节点 𝜇(𝑛)𝜙(𝑥𝑛,𝑏)μ(n)ϕ(xn,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 调用等式 (6)(6)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们把它改成更强的终止条件：

> **终止条件 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：** 如果满足下面 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个条件中的一个，不要再对节点 𝜇(𝑛)𝜙(𝑥𝑛,𝑏)μ(n)ϕ(xn,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 调用等式 (6)(6)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7):
> 
>   1. 𝑏 =0b=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑛 ≤𝑦n≤y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
>   2. 𝑛 >𝑦n>y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
> 

我们根据 **终止条件 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)** 将原二叉树上的叶子分成两种：

  1. 如果叶子节点 𝜇(𝑛)𝜙(𝑥𝑛,𝑏)μ(n)ϕ(xn,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑛 ≤𝑦n≤y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称这种叶子节点为 **普通叶子** ；
  2. 如果叶子节点 𝜇(𝑛)𝜙(𝑥𝑛,𝑏)μ(n)ϕ(xn,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑛 >𝑦n>y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑛 =𝑚𝑝𝑏(𝑚≤𝑦)n=mpb(m≤y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称这种节点为 **特殊叶子** ．

由此我们得出：

> **定理 5.25.2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：** 我们有：
> 
> 𝜙(𝑥,𝑎)=𝑆0+𝑆(7)(7)ϕ(x,a)=S0+S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
> 
> 其中 𝑆0S0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 **普通叶子** 的贡献：
> 
> 𝑆0=∑𝑛≤𝑦𝜇(𝑛)[𝑥𝑛](8)(8)S0=∑n≤yμ(n)[xn]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
> 
> 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 **特殊叶子** 的贡献：
> 
> 𝑆=∑𝑛/𝛿(𝑛)≤𝑦≤𝑛𝜇(𝑛)𝜙(𝑥𝑛,𝜋(𝛿(𝑛))−1)(9)(9)S=∑n/δ(n)≤y≤nμ(n)ϕ(xn,π(δ(n))−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

计算 𝑆0S0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 显然是可以在 𝑂(𝑦log⁡log⁡𝑥)O(ylog⁡log⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度内解决的，现在我们要考虑如何计算 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 计算 S

我们有：

𝑆=−∑𝑝≤𝑦 ∑𝛿(𝑚)>𝑝𝑚≤𝑦<𝑚𝑝𝜇(𝑚)𝜙(𝑥𝑚𝑝,𝜋(𝑝)−1)(10)(10)S=−∑p≤y ∑δ(m)>pm≤y<mpμ(m)ϕ(xmp,π(p)−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们将这个等式改写为：

𝑆=𝑆1+𝑆2+𝑆3S=S1+S2+S3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中：

𝑆1=−∑𝑥1/3<𝑝≤𝑦 ∑𝛿(𝑚)>𝑝𝑚≤𝑦<𝑚𝑝𝜇(𝑚)𝜙(𝑥𝑚𝑝,𝜋(𝑝)−1)S1=−∑x1/3<p≤y ∑δ(m)>pm≤y<mpμ(m)ϕ(xmp,π(p)−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑆2=−∑𝑥1/4<𝑝≤𝑥1/3 ∑𝛿(𝑚)>𝑝𝑚≤𝑦<𝑚𝑝𝜇(𝑚)𝜙(𝑥𝑚𝑝,𝜋(𝑝)−1)S2=−∑x1/4<p≤x1/3 ∑δ(m)>pm≤y<mpμ(m)ϕ(xmp,π(p)−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑆3=−∑𝑝≤𝑥1/4 ∑𝛿(𝑚)>𝑝𝑚≤𝑦<𝑚𝑝𝜇(𝑚)𝜙(𝑥𝑚𝑝,𝜋(𝑝)−1)S3=−∑p≤x1/4 ∑δ(m)>pm≤y<mpμ(m)ϕ(xmp,π(p)−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到计算 𝑆1,𝑆2S1,S2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的和式中涉及到的 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是质数，证明如下：

> 如果不是这样，因为有 𝛿(𝑚) >𝑝 >𝑥1/4δ(m)>p>x1/4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以有 𝑚 >𝑝2 >√𝑥m>p2>x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这与 𝑚 ≤𝑦m≤y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矛盾，所以原命题成立．

更多的，当 𝑚𝑝 >𝑥1/2 ≥𝑦mp>x1/2≥y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有 𝑦 ≤𝑚𝑝y≤mp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此我们有：

𝑆1=∑𝑥1/3<𝑝≤𝑦 ∑𝑝<𝑞≤𝑦𝜙(𝑥𝑝𝑞,𝜋(𝑝)−1)S1=∑x1/3<p≤y ∑p<q≤yϕ(xpq,π(p)−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑆2=∑𝑥1/4<𝑝≤𝑥1/3 ∑𝑝<𝑞≤𝑦𝜙(𝑥𝑝𝑞,𝜋(𝑝)−1)S2=∑x1/4<p≤x1/3 ∑p<q≤yϕ(xpq,π(p)−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 计算 S₁

因为：

𝑥𝑝𝑞<𝑥1/3<𝑝xpq<x1/3<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以：

𝜙(𝑥𝑝𝑞,𝜋(𝑝)−1)=1ϕ(xpq,π(p)−1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以计算 𝑆1S1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的和式中的项都是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以我们实际上要计算质数对 (𝑝,𝑞)(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数，满足：𝑥1/3 <𝑝 <𝑞 ≤𝑦x1/3<p<q≤y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因此：

𝑆1=(𝜋(𝑦)−𝜋(𝑥1/3))(𝜋(𝑦)−𝜋(𝑥1/3)−1)2S1=(π(y)−π(x1/3))(π(y)−π(x1/3)−1)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

有了这个等式我们便可以在 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内计算 𝑆1S1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 计算 S₂

我们有：

𝑆2=∑𝑥1/4<𝑝≤𝑥1/3 ∑𝑝<𝑞≤𝑦𝜙(𝑥𝑝𝑞,𝜋(𝑝)−1)S2=∑x1/4<p≤x1/3 ∑p<q≤yϕ(xpq,π(p)−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们将 𝑆2S2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分成 𝑞 >𝑥𝑝2q>xp2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑞 ≤𝑥𝑝2q≤xp2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两部分：

𝑆2=𝑈+𝑉S2=U+V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中：

𝑈=∑𝑥1/4<𝑝≤𝑥1/3 ∑𝑝<𝑞<𝑦𝑞>𝑥/𝑝2𝜙(𝑥𝑝𝑞,𝜋(𝑝)−1)U=∑x1/4<p≤x1/3 ∑p<q<yq>x/p2ϕ(xpq,π(p)−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑉=∑𝑥1/4<𝑝≤𝑥1/3 ∑𝑝<𝑞<𝑦𝑞≤𝑥/𝑝2𝜙(𝑥𝑝𝑞,𝜋(𝑝)−1)V=∑x1/4<p≤x1/3 ∑p<q<yq≤x/p2ϕ(xpq,π(p)−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 计算 U

由 𝑞 >𝑥𝑝2q>xp2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可得 𝑝2 >𝑥𝑞 ≤𝑥𝑦,𝑝 >√𝑥𝑦p2>xq≤xy,p>xy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此：

𝑈=∑√𝑥/𝑦<𝑝≤𝑥1/3 ∑𝑝<𝑞≤𝑦𝑞>𝑥/𝑝2𝜙(𝑥𝑝𝑞,𝜋(𝑝)−1)U=∑x/y<p≤x1/3 ∑p<q≤yq>x/p2ϕ(xpq,π(p)−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此：

𝑈=∑√𝑥/𝑦<𝑝≤𝑥1/3#{𝑞∣𝑥𝑝2<𝑞≤𝑦}U=∑x/y<p≤x1/3#{q∣xp2<q≤y}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此：

𝑈=∑√𝑥/𝑦<𝑝≤𝑥1/3(𝜋(𝑦)−𝜋(𝑥𝑝2))U=∑x/y<p≤x1/3(π(y)−π(xp2))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为有 𝑥𝑝2 <𝑦xp2<y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以我们可以预处理出所有的 𝜋(𝑡)(𝑡≤𝑦)π(t)(t≤y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样我们就可以在 𝑂(𝑦)O(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度内计算出 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 计算 V

对于计算 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的和式中的每一项，我们都有 𝑝 ≤𝑥𝑝𝑞 <𝑥1/2 <𝑝2p≤xpq<x1/2<p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此：

𝜙(𝑥𝑝𝑞,𝜋(𝑝)−1)=1+𝜋(𝑥𝑝𝑞)−(𝜋(𝑝)−1)=2−𝜋(𝑝)+𝜋(𝑥𝑝𝑞)ϕ(xpq,π(p)−1)=1+π(xpq)−(π(p)−1)=2−π(p)+π(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以被表示为：

𝑉=𝑉1+𝑉2V=V1+V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中：

𝑉1=∑𝑥1/4<𝑝≤𝑥1/3 ∑𝑝<𝑞≤min(𝑥/𝑝2,𝑦)(2−𝜋(𝑝))V1=∑x1/4<p≤x1/3 ∑p<q≤min(x/p2,y)(2−π(p))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑉2=∑𝑥1/4<𝑝≤𝑥1/3 ∑𝑝<𝑞≤min(𝑥/𝑝2,𝑦)𝜋(𝑥𝑝𝑞)V2=∑x1/4<p≤x1/3 ∑p<q≤min(x/p2,y)π(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

预处理出 𝜋(𝑡)(𝑡≤𝑦)π(t)(t≤y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 我们就可以在 𝑂(𝑥1/3)O(x1/3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度内计算出 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑我们如何加速计算 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的过程．我们可以把 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的贡献拆分成若干个 𝜋(𝑥𝑝𝑞)π(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为定值的区间上，这样就只需要计算出每一个区间的长度和从一个区间到下一个区间的 𝜋(𝑥𝑝𝑞)π(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的改变量．

更准确的说，我们首先将 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分成两个部分，将 𝑞 ≤min(𝑥𝑝2,𝑦)q≤min(xp2,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这个复杂的条件简化：

𝑉2=∑𝑥1/4<𝑝≤√𝑥/𝑦 ∑𝑝<𝑞≤𝑦𝜋(𝑥𝑝𝑞)+∑√𝑥/𝑦<𝑝≤𝑥1/3 ∑𝑝<𝑞≤𝑥/𝑝2𝜋(𝑥𝑝𝑞)V2=∑x1/4<p≤x/y ∑p<q≤yπ(xpq)+∑x/y<p≤x1/3 ∑p<q≤x/p2π(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

接着我们把这个式子改写为：

𝑉2=𝑊1+𝑊2+𝑊3+𝑊4+𝑊5V2=W1+W2+W3+W4+W5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中：

𝑊1=∑𝑥1/4<𝑝≤𝑥/𝑦2 ∑𝑝<𝑞≤𝑦𝜋(𝑥𝑝𝑞)W1=∑x1/4<p≤x/y2 ∑p<q≤yπ(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑊2=∑𝑥/𝑦2<𝑝≤√𝑥/𝑦 ∑𝑝<𝑞≤√𝑥/𝑝𝜋(𝑥𝑝𝑞)W2=∑x/y2<p≤x/y ∑p<q≤x/pπ(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑊3=∑𝑥/𝑦2<𝑝≤√𝑥/𝑦 ∑√𝑥/𝑝<𝑞≤𝑦𝜋(𝑥𝑝𝑞)W3=∑x/y2<p≤x/y ∑x/p<q≤yπ(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑊4=∑√𝑥/𝑦<𝑝≤𝑥1/3 ∑𝑝<𝑞≤√𝑥/𝑝𝜋(𝑥𝑝𝑞)W4=∑x/y<p≤x1/3 ∑p<q≤x/pπ(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑊5=∑√𝑥/𝑦<𝑝≤𝑥1/3 ∑√𝑥/𝑝<𝑞≤𝑥/𝑝2𝜋(𝑥𝑝𝑞)W5=∑x/y<p≤x1/3 ∑x/p<q≤x/p2π(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

#### 计算 W₁ 与 W₂

计算这两个值需要计算满足 𝑦 <𝑥𝑝𝑞 <𝑥1/2y<xpq<x1/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝜋(𝑥𝑝𝑞)π(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．可以在区间 [1,√𝑥][1,x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分块筛出．在每个块中我们对于所有满足条件的 (𝑝,𝑞)(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都累加 𝜋(𝑥𝑝𝑞)π(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 计算 W₃

对于每个 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们把 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分成若干个区间，每个区间都满足它们的 𝜋(𝑥𝑝𝑞)π(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是定值，每个区间我们都可以 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算它的贡献．当我们获得一个新的 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，我们用 𝜋(𝑡)π(t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑡 ≤𝑦t≤y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）的值表计算 𝜋(𝑥𝑝𝑞)π(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以内的质数表可以给出使得 𝜋(𝑡) <𝜋(𝑡 +1) =𝜋(𝑥𝑝𝑞)π(t)<π(t+1)=π(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立的 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．以此类推使得 𝜋(𝑥𝑝𝑞)π(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变化的下一个 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

#### 计算 W₄

相比于 𝑊3W3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑊4W4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更小，所以 𝜋(𝑥𝑝𝑞)π(xpq)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 改变得更快．这时候再按照计算 𝑊3W3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方法计算 𝑊4W4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就显得没有任何优势．于是我们直接暴力枚举数对 (𝑝,𝑞)(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来计算 𝑊4W4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 计算 W₅

我们像计算 𝑊3W3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那样来计算 𝑊5W5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 计算 S₃

我们使用所有小于 𝑥1/4x1/4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素数一次筛出区间 [1,𝑥𝑦][1,xy]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．当我们的筛法进行到 𝑝𝑘pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时候，我们算出了所有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足没有平方因子并且 𝛿(𝑚) >𝑝𝑘δ(m)>pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 −𝜇(𝑚)𝜙(𝑥𝑚𝑝𝑘,𝑘−1)−μ(m)ϕ(xmpk,k−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值．这个筛法是分块进行的，我们在筛选间隔中维护一个二叉树，以实时维护所有素数筛选到给定素数后的中间结果．这样我们就可以只用 𝑂(log⁡𝑥)O(log⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度求出在筛法进行到某一个值的时候没有被筛到的数的数量．

## 算法的时空复杂度

时空复杂度被如下 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个过程影响：

  1. 计算 𝑃2(𝑥,𝑎)P2(x,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 计算 𝑊1,𝑊2,𝑊3,𝑊4,𝑊5W1,W2,W3,W4,W5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  3. 计算 𝑆3S3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 计算 P₂(x,y) 的复杂度

我们已经知道了这个过程的时间复杂度为 𝑂(𝑥𝑦log⁡log⁡𝑥)O(xylog⁡log⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，空间复杂度为 𝑂(𝑦)O(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 计算 W₁,W₂,W₃,W₄,W₅ 的复杂度

计算 𝑊1,𝑊2W1,W2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所进行的块长度为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的筛的时间按复杂度为 𝑂(√𝑥log⁡log⁡𝑥)O(xlog⁡log⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，空间复杂度为 𝑂(𝑦)O(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

计算 𝑊1W1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所需的时间复杂度为：

𝜋(𝑥𝑦2)𝜋(𝑦)=𝑂(𝑥𝑦log2⁡𝑥)π(xy2)π(y)=O(xylog2⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

计算 𝑊2W2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度为：

𝑂⎛⎜ ⎜ ⎜⎝∑𝑥/𝑦2<𝑝≤√𝑥/𝑦𝜋(√𝑥𝑝)⎞⎟ ⎟ ⎟⎠=𝑂(𝑥3/4𝑦1/4log2⁡𝑥)O(∑x/y2<p≤x/yπ(xp))=O(x3/4y1/4log2⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，计算 𝑊3W3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度为：

𝑂⎛⎜ ⎜ ⎜⎝∑𝑥/𝑦2<𝑝≤√𝑥/𝑦𝜋(√𝑥𝑝)⎞⎟ ⎟ ⎟⎠=𝑂(𝑥3/4𝑦1/4log2⁡𝑥)O(∑x/y2<p≤x/yπ(xp))=O(x3/4y1/4log2⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

计算 𝑊4W4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度为：

𝑂⎛⎜ ⎜ ⎜⎝∑√𝑥/𝑦<𝑝≤𝑥1/3𝜋(√𝑥𝑝)⎞⎟ ⎟ ⎟⎠=𝑂(𝑥2/3log2⁡𝑥)O(∑x/y<p≤x1/3π(xp))=O(x2/3log2⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

计算 𝑊5W5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度为：

𝑂⎛⎜ ⎜ ⎜⎝∑√𝑥/𝑦<𝑝≤𝑥1/3𝜋(√𝑥𝑝)⎞⎟ ⎟ ⎟⎠=𝑂(𝑥2/3log2⁡𝑥)O(∑x/y<p≤x1/3π(xp))=O(x2/3log2⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 计算 S₃ 的复杂度

对于预处理：由于要快速查询 𝜙(𝑢,𝑏)ϕ(u,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，我们没办法用普通的筛法 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求出，而是要维护一个数据结构使得每次查询的时间复杂度是 𝑂(log⁡𝑥)O(log⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此时间复杂度为 𝑂(𝑥𝑦log⁡𝑥log⁡log⁡𝑥)O(xylog⁡xlog⁡log⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于求和：对于计算 𝑆3S3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和式中的每一项，我们查询上述数据结构，一共 𝑂(log⁡𝑥)O(log⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次查询．我们还需要计算和式的项数，即二叉树中叶子的个数．所有叶子的形式均为 ±𝜙(𝑥𝑚𝑝𝑏,𝑏−1)±ϕ(xmpb,b−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑚 ≤𝑦,𝑏 <𝜋(𝑥1/4)m≤y,b<π(x1/4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，叶子的数目是 𝑂(𝑦𝜋(𝑥1/4))O(yπ(x1/4))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别的．所以计算 𝑆3S3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的总时间复杂度为：

𝑂(𝑥𝑦log⁡𝑥log⁡log⁡𝑥+𝑦𝑥1/4)O(xylog⁡xlog⁡log⁡x+yx1/4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 总复杂度

这个算法的空间复杂度为 𝑂(𝑦)O(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，时间复杂度为：

𝑂(𝑥𝑦log⁡log⁡𝑥+𝑥𝑦log⁡𝑥log⁡log⁡𝑥+𝑥1/4𝑦+𝑥2/3log2⁡𝑥)O(xylog⁡log⁡x+xylog⁡xlog⁡log⁡x+x1/4y+x2/3log2⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们取 𝑦 =𝑥1/3log3⁡𝑥log⁡log⁡𝑥y=x1/3log3⁡xlog⁡log⁡x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有最优时间复杂度为 𝑂(𝑥2/3log2⁡𝑥)O(x2/3log2⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，空间复杂度为 𝑂(𝑥1/3log3⁡𝑥log⁡log⁡𝑥)O(x1/3log3⁡xlog⁡log⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 一些改进

我们在这里给出改进方法，以减少算法的常数，提高它的实际效率．

  * 在 **终止条件 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)** 中，我们可以用一个 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来代替 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑧 >𝑦z>y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们可以证明这样子计算 𝑆3S3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度可以优化到：

𝑂(𝑥𝑧log⁡𝑥log⁡log⁡𝑥+𝑦𝑥1/4log⁡𝑥+𝑧3/2)O(xzlog⁡xlog⁡log⁡x+yx1/4log⁡x+z3/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这也为通过改变 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值来检查计算提供了一个很好的方法．

  * 为了清楚起见，我们在阐述算法的时候选择在 𝑥1/4x1/4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处拆分来计算总和 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但实际上我们只需要有 𝑝 ≤𝑥𝑝𝑞 <𝑝2p≤xpq<p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就可以计算．我们可以利用这一点，渐近复杂性保持不变．

  * 用前几个素数 2,3,52,3,5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 预处理计算可以节省更多的时间．

## 参考资料与拓展阅读

本文翻译自：[Computing 𝜋(𝑥)π(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7): the Meissel, Lehmer, Lagarias, Miller, Odlyzko method](https://dl.acm.org/doi/abs/10.1090/s0025-5718-96-00674-6)

* * *

>  __本页面最近更新： 2026/4/23 03:45:48，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/meissel-lehmer.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/meissel-lehmer.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [Peanut-Tang](https://github.com/Peanut-Tang), [1196131597](https://github.com/1196131597), [Alpacabla](https://github.com/Alpacabla), [alphagocc](https://github.com/alphagocc), [CCXXXI](https://github.com/CCXXXI), [GHLinZhengyu](https://github.com/GHLinZhengyu), [Great-designer](https://github.com/Great-designer), [lailai0916](https://github.com/lailai0916), [ljy2009](https://github.com/ljy2009), [megakite](https://github.com/megakite), [Menci](https://github.com/Menci), [r-value](https://github.com/r-value), [StudyingFather](https://github.com/StudyingFather), [Vxlimo](https://github.com/Vxlimo), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
