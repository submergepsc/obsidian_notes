# Stoer–Wagner 算法 - OI Wiki

- Source: https://oi-wiki.org/graph/stoer-wagner/

# Stoer–Wagner 算法

## 定义

由于取消了 **源汇点** 的定义，我们需要对 **割** 的概念进行重定义．

（其实是网络流部分有关割的定义与维基百科不符，只是由于一般接触到的割都是「有源汇的最小割问题」，因此这个概念也就约定俗成了．）

### 割

去掉其中所有边能使一张网络流图不再连通（即分成两个子图）的边集称为图的割．

即：在无向图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，设 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中一些弧的集合，若从 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中删去 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的所有弧能使图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是连通图，称 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个割．

### 有源汇点的最小割问题

同 [最小割](../flow/min-cut/) 中的定义．

### 无源汇点的最小割问题

包含的弧的权和最小的割．也称为全局最小割．

显然，直接跑网络流的复杂度是行不通的．

* * *

## Stoer–Wagner 算法

### 引入

Stoer–Wagner 算法在 1995 年由 _Mechthild Stoer_ 与 _Frank Wagner_ 提出，是一种通过 **递归** 的方式来解决 **无向正权图** 上的全局最小割问题的算法．

### 性质

算法复杂度 𝑂(|𝑉||𝐸| +|𝑉|2log⁡|𝑉|)O(|V||E|+|V|2log⁡|V|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一般可近似看作 𝑂(|𝑉|3)O(|V|3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

它的实现基于以下基本事实：设图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中有任意两点 𝑆,𝑇S,T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么任意一个图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的割 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，或者有 𝑆,𝑇S,T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在同一连通块中，或者有 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 𝑆−𝑇S−T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 割．

### 过程

  1. 在图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中任意指定两点 𝑠,𝑡s,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且以这两点作为源汇点求出图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑆 −𝑇S−T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小割（定义为 _cut of phase_ ），更新当前答案．
  2. 「合并」点 𝑠,𝑡s,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 |𝑉||V|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则回到第一步．
  3. 输出所有 _cut of phase_ 的最小值．

合并两点 𝑠,𝑡s,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：删除 𝑠,𝑡s,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的连边 (𝑠,𝑡)(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，对于 𝐺 ∖{𝑠,𝑡}G∖{s,t}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中任意一点 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，删除 (𝑡,𝑘)(t,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并将其边权 𝑑(𝑡,𝑘)d(t,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加到 𝑑(𝑠,𝑘)d(s,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上

解释：如果 𝑠,𝑡s,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在同一连通块，对于 𝐺 ∖{𝑠,𝑡}G∖{s,t}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的一点 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，假如 (𝑘,𝑠) ∈𝐶min(k,s)∈Cmin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 (𝑘,𝑡) ∈𝐶min(k,t)∈Cmin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也一定成立，否则因为 𝑠,𝑡s,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连通，𝑘,𝑡k,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连通，导致 𝑠,𝑘s,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在同一连通块，此时 𝐶 =𝐶min ∖{(𝑡,𝑘)}C=Cmin∖{(t,k)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将比 𝐶minCmin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更优．反之亦然．所以 𝑠,𝑡s,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以看作同一点．

步骤 1 考虑了 𝑠,𝑡s,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不在同一连通块的情形，步骤 2 考虑了剩余的情况．由于每次执行步骤 2 都会使 |𝑉||V|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 减小 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此算法将在进行 |𝑉| −1|V|−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后结束．

### S-T 最小割的求法

（显然不是网络流．）

假设进行若干次合并以后，当前图 𝐺′ =(𝑉′,𝐸′)G′=(V′,E′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，执行步骤 1．

我们构造一个集合 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，初始时令 𝐴 =∅A=∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们每次将 𝑉′V′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有点中，满足 𝑖 ∉𝐴i∉A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且权值函数 𝑤(𝐴,𝑖)w(A,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最大的节点加入集合 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，直到 |𝐴| =|𝑉′||A|=|V′|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

其中权值函数的定义：

𝑤(𝐴,𝑖) =∑𝑗∈𝐴𝑑(𝑖,𝑗)w(A,i)=∑j∈Ad(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

（若 (𝑖,𝑗) ∉𝐸′(i,j)∉E′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑑(𝑖,𝑗) =0d(i,j)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

容易知道所有点加入 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的顺序是固定的，令 ord⁡(𝑖)ord⁡(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个加入 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点，𝑡 =ord⁡(|𝑉′|)t=ord⁡(|V′|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；pos⁡(𝑣)pos⁡(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被加入 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后 |𝐴||A|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小，即 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被加入的顺序．

则对任意点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，一个 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的割即为 𝑤(𝑡)w(t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 证明

定义一个点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被激活，当且仅当 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在加入 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中时，发现在 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 此时最后一个点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 早于 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加入集合，并且在图 𝐺″ =(𝑉′,𝐸′/𝐶)G″=(V′,E′/C)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不在同一连通块．

![Stoer-Wagner1](./images/Stoer-Wagner1.png)

如图，蓝色区域和黄色区域为两个不同的连通块，方括号中的数字为加入 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的顺序．灰色节点为活跃节点，白色节点则不是活跃节点．

定义 𝐴𝑣 ={𝑢 ∣pos⁡(𝑢) <pos⁡(𝑣)}Av={u∣pos⁡(u)<pos⁡(v)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是严格早于 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加入 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点，令 𝐸𝑣Ev![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝐸′E′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的诱导子图（点集为 𝐴𝑣 ∪{𝑣}Av∪{v}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）的边集．（注意包含点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．）

定义诱导割 𝐶𝑣Cv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝐶 ∩𝐸𝑣C∩Ev![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝑤(𝐶𝑣) =∑(𝑖,𝑗)∈𝐶𝑣𝑑(𝑖,𝑗)w(Cv)=∑(i,j)∈Cvd(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

Lemma 1

对于任何被激活的点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑤(𝐴𝑣,𝑣) ≤𝑤(𝐶𝑣)w(Av,v)≤w(Cv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明：使用数学归纳法．

对于第一个被激活的点 𝑣0v0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由定义可知 𝑤(𝐴𝑣0,𝑣0) =𝑤(𝐶𝑣0)w(Av0,v0)=w(Cv0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于之后两个被激活的点 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，假设 pos⁡(𝑣) <pos⁡(𝑢)pos⁡(v)<pos⁡(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有：

𝑤(𝐴𝑢,𝑢) =𝑤(𝐴𝑣,𝑢) +𝑤(𝐴𝑢 −𝐴𝑣,𝑢)w(Au,u)=w(Av,u)+w(Au−Av,u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

又，已知：

𝑤(𝐴𝑣,𝑢) ≤𝑤(𝐴𝑣,𝑣)w(Av,u)≤w(Av,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并且 𝑤(𝐴𝑣,𝑣) ≤𝑤(𝐶𝑣)w(Av,v)≤w(Cv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 联立可得：

𝑤(𝐴𝑢,𝑢) ≤𝑤(𝐶𝑣) +𝑤(𝐴𝑢 −𝐴𝑣,𝑢)w(Au,u)≤w(Cv)+w(Au−Av,u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于 𝑤(𝐴𝑢 −𝐴𝑣,𝑢)w(Au−Av,u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对 𝑤(𝐶𝑢)w(Cu)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有贡献而对 𝑤(𝐶𝑣)w(Cv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有贡献，在所有边均为正权的情况下，可导出：

𝑤(𝐴𝑢,𝑢) ≤𝑤(𝐶𝑢)w(Au,u)≤w(Cu)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由归纳法得证．

由于 pos⁡(𝑠) <pos⁡(𝑡)pos⁡(s)<pos⁡(t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且 𝑠,𝑡s,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不在同一连通块，因此 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 会被激活，由此可以得出 𝑤(𝐴𝑡,𝑡) ≤𝑤(𝐶𝑡) =𝑤(𝐶)w(At,t)≤w(Ct)=w(C)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

[P5632【模板】Stoer–Wagner 算法](https://www.luogu.com.cn/problem/P5632)

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 ``` |  ```text #include <cstring> #include <iostream> using namespace std ; constexpr int N = 601 ; int fa [ N ], siz [ N ], edge [ N ][ N ]; int find ( int x ) { return fa [ x ] == x ? x : fa [ x ] = find ( fa [ x ]); } int dist [ N ], vis [ N ], bin [ N ]; int n , m ; int contract ( int & s , int & t ) { // Find s,t memset ( dist , 0 , sizeof ( dist )); memset ( vis , false , sizeof ( vis )); int i , j , k , mincut , maxc ; for ( i = 1 ; i <= n ; i ++ ) { k = -1 ; maxc = -1 ; for ( j = 1 ; j <= n ; j ++ ) if ( ! bin [ j ] && ! vis [ j ] && dist [ j ] > maxc ) { k = j ; maxc = dist [ j ]; } if ( k == -1 ) return mincut ; s = t ; t = k ; mincut = maxc ; vis [ k ] = true ; for ( j = 1 ; j <= n ; j ++ ) if ( ! bin [ j ] && ! vis [ j ]) dist [ j ] += edge [ k ][ j ]; } return mincut ; } constexpr int inf = 0x3f3f3f3f ; int Stoer_Wagner () { int mincut , i , j , s , t , ans ; for ( mincut = inf , i = 1 ; i < n ; i ++ ) { ans = contract ( s , t ); bin [ t ] = true ; if ( mincut > ans ) mincut = ans ; if ( mincut == 0 ) return 0 ; for ( j = 1 ; j <= n ; j ++ ) if ( ! bin [ j ]) edge [ s ][ j ] = ( edge [ j ][ s ] += edge [ j ][ t ]); } return mincut ; } int main () { ios :: sync_with_stdio ( false ), cin . tie ( nullptr ); cin >> n >> m ; if ( m < n \- 1 ) { cout << 0 ; return 0 ; } for ( int i = 1 ; i <= n ; ++ i ) fa [ i ] = i , siz [ i ] = 1 ; for ( int i = 1 , u , v , w ; i <= m ; ++ i ) { cin >> u >> v >> w ; int fu = find ( u ), fv = find ( v ); if ( fu != fv ) { if ( siz [ fu ] > siz [ fv ]) swap ( fu , fv ); fa [ fu ] = fv , siz [ fv ] += siz [ fu ]; } edge [ u ][ v ] += w , edge [ v ][ u ] += w ; } int fr = find ( 1 ); if ( siz [ fr ] != n ) { cout << 0 ; return 0 ; } cout << Stoer_Wagner (); return 0 ; } ```   
---|---  
  
* * *

### 复杂度分析与优化

 _contract_ 操作的复杂度为 𝑂(|𝐸| +|𝑉|log⁡|𝑉|)O(|E|+|V|log⁡|V|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

一共进行 𝑂(|𝑉|)O(|V|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次 _contract_ ，总复杂度为 𝑂(|𝐸||𝑉| +|𝑉|2log⁡|𝑉|)O(|E||V|+|V|2log⁡|V|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

根据 [最短路](../shortest-path/) 的经验，算法瓶颈在于找到权值最大的点．

在一次 _contract_ 中需要找 |𝑉||V|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次堆顶，并递增地修改 |𝐸||E|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次权值．

斐波那契堆 可以胜任 𝑂(log⁡|𝑉|)O(log⁡|V|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 查找堆顶和 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递增修改权值的工作，理论复杂度可以达到 𝑂(|𝐸| +|𝑉|log⁡|𝑉|)O(|E|+|V|log⁡|V|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是由于斐波那契堆常数过大，码量高，实际应用价值偏低．

（实际测试中开 O2 还要卡评测波动才能过．）

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/stoer-wagner.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/stoer-wagner.md "edit.link.title")  
>  __本页面贡献者：[Enter-tainer](https://github.com/Enter-tainer), [Tiphereth-A](https://github.com/Tiphereth-A), [DanJoshua](https://github.com/DanJoshua), [opsiff](https://github.com/opsiff), [yingqi-z20](https://github.com/yingqi-z20), [aberter0x3f](https://github.com/aberter0x3f), [CroMarmot](https://github.com/CroMarmot), [EntropyIncreaser](https://github.com/EntropyIncreaser), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [ImpleLee](https://github.com/ImpleLee), [kenlig](https://github.com/kenlig), [Konano](https://github.com/Konano), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [ouuan](https://github.com/ouuan), [sldpzshdwz](https://github.com/sldpzshdwz), [yzy-1](https://github.com/yzy-1)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
