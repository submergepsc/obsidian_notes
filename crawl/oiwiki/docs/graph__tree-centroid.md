# 树的重心 - OI Wiki

- Source: https://oi-wiki.org/graph/tree-centroid/

# 树的重心

本文介绍树的重心的概念和基本性质．

## 定义

如果在树 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中删去某个结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，得到的图 𝑇 ∖{𝑣}T∖{v}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中每个连通分量的大小均不超过原树结点数的一半，就称这个结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为整棵树的 **重心** （centroid）．删去某一结点后得到的最大连通分量的大小也称为该结点的 **重量** （weight）．利用这一概念，重心的定义可以叙述为重量不超过树结点数的一半的结点．

「子树」

本文可能同时涉及无根树、有根树，以及将有根树换根到非根结点得到的树．为了避免混淆，本文将用 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示无根树，用 𝑇(𝑣)T(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示以结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的有根树．本文中提到的「子树」均是指 **有根树** 中，一个结点及其所有子孙结点构成的树．有根树 𝑇(𝑣)T(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应子树记为 𝑇(𝑣)𝑢Tu(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这样定义的子树当然包括整棵树本身．如果要明确不包括整棵树本身，将称呼它为「真子树」．

无根树中的「子树」通常指它的一个连通子图．在讨论重心时，部分作者会用「子树」一词特指不包含某结点的极大连通子图，或者特指将某条边删去后得到的两个连通分量之一．容易验证，这两种方式定义得到的「子树」集合是一致的，且不包括整棵树自身．由于它和有根树的子树集合并不一致，本文将避免对无根树使用「子树」概念．

在实际求解重心或处理某些问题时，通常存在一个默认的树根．此时，将非根结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 删掉得到的连通分量中，除了该结点的子结点对应子树外，还有一棵「向上」的子树．此时，设结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的父结点为 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这棵「向上」的子树就是 𝑇(𝑣)𝑢Tu(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．本文在提及这类子图时，会显式地称呼它为「向上」的子树．若无特殊说明，本文提及的子树均不包括这类「向上」的子树．

注意到，得到的这些连通分量同样是无根树．通过删去树的重心，一棵树将变为若干棵至多原树一半大小的树．重心的这一特性使得在树上应用分治思想解决问题成为可能．这就是 [点分治](../tree-divide/#点分治)，也称为树的重心分解．

## 性质

本节讨论重心的性质．首先，树的重心有如下等价定义：

等价定义

树 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是它的重心，当且仅当以下任意一条成立：

无根树版本有根树版本

  1. 在树中删去结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，得到的图 𝑇 ∖{𝑣}T∖{v}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中每个连通分量的大小均不超过原树结点数的一半．
  2. 在所有删去某个结点后得到的最大连通分量大小中，删去结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时所得到的值最小．
  3. 树中所有结点到某个结点的距离和中，到结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的距离和最小．

  1. 当树以结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根时，任一真子树的大小均不超过原树结点数的一半．
  2. 在所有以某个结点为根时的最大真子树大小中，以结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根时所得到的值最小．
  3. 在所有以某个结点为根时所有结点的深度和中，以结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根时深度和最小．

证明

首先，引入一些记号．有根树和无根树两个版本的表述显然是等价的．定义 𝑊(𝑥) =max𝑢∼𝑥|𝑇(𝑥)𝑢|W(x)=maxu∼x|Tu(x)|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑢 ∼𝑥u∼x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相邻．定义 𝑆(𝑥) =∑𝑢∈𝑇𝑑(𝑢,𝑥)S(x)=∑u∈Td(u,x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑑(𝑢,𝑥)d(u,x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的距离．那么，定义 1 相当于要求 𝑊(𝑣) ≤|𝑇|/2W(v)≤|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义 2 相当于要求 𝑣 ∈arg⁡min𝑥∈𝑇𝑊(𝑥)v∈arg⁡minx∈TW(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义 3 相当于要求 𝑣 ∈arg⁡min𝑥∈𝑇𝑆(𝑥)v∈arg⁡minx∈TS(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．需要证明的是，这三个条件是等价的．

将 𝑆(𝑥)S(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 理解为以 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根时的结点深度和，考虑它在树根从结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 换为相邻结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时发生的变化．注意到，在树中删去边 (𝑣,𝑢)(v,u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，得到的两个连通分量分别是子树 𝑇(𝑢)𝑣Tv(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇(𝑣)𝑢Tu(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．在换根前后，子树 𝑇(𝑢)𝑣Tv(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中每个结点深度都增加 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，子树 𝑇(𝑣)𝑢Tu(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中每个结点深度都减少 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，深度和的变化为

Δ𝑆𝑣→𝑢=𝑆(𝑢)−𝑆(𝑣)=|𝑇(𝑢)𝑣|−|𝑇(𝑣)𝑢|=|𝑇|−2|𝑇(𝑣)𝑢|.ΔSv→u=S(u)−S(v)=|Tv(u)|−|Tu(v)|=|T|−2|Tu(v)|.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，定义 1 的条件相当于要求 Δ𝑆𝑣→𝑢 ≤0ΔSv→u≤0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有相邻结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立，也就是说，𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑆(𝑥)S(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的极小值点．

转而设 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑆(𝑥)S(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的（一个）最小值点（即定义 3），它必然存在，且一定是极小值点．考虑以 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的有根树 𝑇(𝑣)T(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设 𝑢 ≠𝑣u≠v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个非根结点，且从 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有向路径上，结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的后一个结点为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（可能就是 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前一个结点为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（可能就是 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．那么，因为 𝑇(𝑥)𝑢 ⊆𝑇(𝑣)𝑦Tu(x)⊆Ty(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以有

2|𝑇(𝑢)𝑥|=2|𝑇|−2|𝑇(𝑥)𝑢|≥2|𝑇|−2|𝑇(𝑣)𝑦|≥|𝑇|.2|Tx(u)|=2|T|−2|Tu(x)|≥2|T|−2|Ty(v)|≥|T|.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，最后一步用到 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑆(𝑥)S(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的极小值点这一事实．此时，有两种情形：

  * 存在结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 2|𝑇(𝑢)𝑥| =|𝑇|2|Tx(u)|=|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．此时，根据上述不等式，必然有 (𝑥,𝑢) =(𝑣,𝑦)(x,u)=(v,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 |𝑇(𝑢)𝑣| =|𝑇(𝑣)𝑢| =|𝑇|/2|Tv(u)|=|Tu(v)|=|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．也就是说，使得等式成立的结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只能有一个，且它必然与 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相邻．此时，对于所有其他结点 𝑢′ ≠𝑢,𝑣u′≠u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，必然存在 𝑥′ ∼𝑢′x′∼u′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 |𝑇(𝑢′)𝑥′| >|𝑇|/2|Tx′(u′)|>|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．满足条件 1 的结点集合为 {𝑣,𝑢}{v,u}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注意到，删去任何结点时，得到的连通分量大小之和总是 |𝑇| −1|T|−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，只要有一个连通分量大小不小于 |𝑇|/2|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它就必然是最大连通分量．因此，对于这种情形，𝑊(𝑣) =𝑊(𝑢) =|𝑇|/2W(v)=W(u)=|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且对于所有 𝑢′ ≠𝑢,𝑣u′≠u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 𝑊(𝑢′) >|𝑇|/2W(u′)>|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，满足条件 2 的结点集合为 arg⁡min𝑊(𝑥) ={𝑣,𝑢}arg⁡minW(x)={v,u}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

又因为 Δ𝑆𝑣→𝑢 =0ΔSv→u=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑆(𝑣) =𝑆(𝑢)S(v)=S(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是最小值点，𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也一定是最小值点．而对于 𝑢′ ≠𝑢,𝑣u′≠u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都存在 𝑥′ ∼𝑢′x′∼u′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 |𝑇(𝑢′)𝑥′| >|𝑇|/2|Tx′(u′)|>|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这违反了极小值点需要满足的条件，所以，𝑢′u′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定也不是最小值点．因此，满足条件 3 的结点集合为 arg⁡min𝑆(𝑥) ={𝑣,𝑢}arg⁡minS(x)={v,u}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 不存在结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 2|𝑇(𝑢)𝑥| =|𝑇|2|Tx(u)|=|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．此时，对于所有结点 𝑢 ≠𝑣u≠v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都存在结点 𝑥 ∼𝑢x∼u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 |𝑇(𝑢)𝑥| >|𝑇|/2|Tx(u)|>|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．重复前文分析可知，对于所有结点 𝑢 ≠𝑣u≠v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑊(𝑢) >|𝑇|/2W(u)>|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是 𝑆(𝑥)S(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的极小值点．因此，满足条件 1 的结点只有 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 arg⁡min𝑊(𝑥) =arg⁡min𝑆(𝑥) ={𝑣}arg⁡minW(x)=arg⁡minS(x)={v}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

无论在哪一情形中，满足三个条件的集合都是相同的．这就证明了三个定义是等价的．

除了这些等价定义外，树的重心还有如下常见性质：

性质

  1. 树的重心如果不唯一，则恰有两个．这两个重心相邻．而且，删去它们的连边后，树将变为两个大小相同的连通分量．
  2. 在一棵树上添加或删除一个叶子，那么它的重心最多只移动一条边的距离．
  3. 把两棵树通过一条边相连得到一棵新的树，那么新树的重心在连接原来两棵树的重心的路径上．
  4. 一棵有根树的重心一定在根结点所在的重链上．一棵树的重心一定是该树根结点重子结点对应子树的重心的祖先．

证明

性质 1 可以从对重心等价定义的证明中得到．

性质 2 只需要考虑添加一个叶子结点的情形．这进一步分为两种情形：

  * 树 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只有一个重心 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为新添加的叶子结点，且在新树中删去结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到的图 𝑇 ∪{𝑥} ∖{𝑣}T∪{x}∖{v}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在连通分量为 𝐵 ∪{𝑥}B∪{x}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是树 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的唯一重心，所以 2|𝐵| <|𝑇|2|B|<|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是 2|𝐵| +1 ≤|𝑇|2|B|+1≤|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．进而，有

2|𝐵∪{𝑥}|=2(|𝐵|+1)≤|𝑇|+1=|𝑇∪{𝑥}|.2|B∪{x}|=2(|B|+1)≤|T|+1=|T∪{x}|.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仍然是新树 𝑇 ∪{𝑥}T∪{x}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的重心．即使新树的重心不唯一，它也必然是 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的相邻结点．因此，重心至多移动一条边．

  * 树 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有两个重心 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时，删去 (𝑢,𝑣)(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到的两个连通分量 𝑇(𝑣)𝑢Tu(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇(𝑢)𝑣Tv(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大小相等，均为 |𝑇|/2|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．不妨设新添加的叶子结点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连接在 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在的连通分量 𝑇(𝑢)𝑣Tv(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上．那么，因为

|𝑇(𝑢)𝑣∪{𝑥}|=|𝑇|/2+1>(|𝑇|+1)/2=|𝑇∪{𝑥}|/2,|Tv(u)∪{x}|=|T|/2+1>(|T|+1)/2=|T∪{x}|/2,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不再是新树的重心．反过来，因为删去 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，仍然有大小为 |𝑇|/2|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连通分量 𝑇(𝑣)𝑢Tu(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而其他连通分量的大小之和为

|𝑇∪{𝑥}|−1−|𝑇(𝑣)𝑢|=|𝑇|/2≤|𝑇(𝑣)𝑢|,|T∪{x}|−1−|Tu(v)|=|T|/2≤|Tu(v)|,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仍然是新树的重心．因为新树的结点数是奇数，重心必然唯一．所以，重心也至多移动一条边．

总结两种情形的分析可以发现，新树的重心一定在旧树的重心与新添加的叶子结点的路径上．

性质 3 可以通过归纳法说明．设 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇′T′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连接时，新添加的边为 (𝑥,𝑦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑥 ∈𝑇,𝑦 ∈𝑇′x∈T,y∈T′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．不妨设新树的（一个）重心在 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中．考虑从树 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始，将树 𝑇′T′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中结点逐一添加为其叶子结点的过程．可以归纳地证明，树的（一个）重心始终在连接树 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的重心与结点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径上．归纳起点显然．假设直到某一时刻为止，命题仍然成立．设此时重心为 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由性质 2 的分析可知，新树的重心必然在连接新添加结点和当前重心 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径上，又因为它不会移动到树 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 外，所以，只需要考虑路径与树 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的公共部分，即连接当前重心 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和结点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径上．根据归纳假设，𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就在连接树 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的重心和结点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径上，所以，新树重心也必然在连接当前重心 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和结点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径上．由归纳法可知，命题成立．

性质 4 只需要结合 [重链剖分性质](../hld/#重链剖分的性质) 即可说明．设树 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的（一个）重心为 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是根结点时，命题显然成立．下面设 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是非根结点，𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是它的父结点．因为 |𝑇(𝑣)𝑢| ≤|𝑇|/2|Tu(v)|≤|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在子树大小至少是 |𝑇|/2|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，只要它到根结点的路径上经过一次轻边，它所在子树大小将严格小于 |𝑇|/2|T|/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，矛盾．所以，它必然在根结点所在重链上．进而，根据重链的定义，根结点重子结点对应子树中根结点所在重链就是原树中根结点所在重链的一部分；而且，根据性质 3，在重子结点对应子树上添加重子结点及其所有轻子结点对应子树后，重心位置将沿着当前重心和根结点路径移动，所以新重心必然是旧重心的祖先．

## 求法

根据重心的等价定义，有两种方法可以在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内求出树的所有重心，其中，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为树的大小．

### DFS 统计子树大小

通过 DFS 计算每个子树的大小．对每个结点，记录它的所有子结点对应子树的大小，并利用总结点数减去当前子树大小得到「向上」的子树的大小，然后就可以依据定义找到重心了．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text const int MAXN = 50005 ; int n ; // 这份代码默认节点编号从 1 开始，即 i ∈ [1,n] int siz [ MAXN ], // 这个节点的「大小」（所有子树上节点数 + 该节点） weight [ MAXN ]; // 这个节点的「重量」，即所有子树「大小」的最大值 vector < int > centroids ; // 用于记录树的重心（存的是节点编号） vector < int > g [ MAXN ]; void dfs ( int cur , int fa ) { // cur 表示当前节点 (current) siz [ cur ] = 1 ; weight [ cur ] = 0 ; for ( int v : g [ cur ]) { if ( v != fa ) { // v 表示这条有向边所通向的节点 dfs ( v , cur ); siz [ cur ] += siz [ v ]; weight [ cur ] = max ( weight [ cur ], siz [ v ]); } } weight [ cur ] = max ( weight [ cur ], n \- siz [ cur ]); if ( weight [ cur ] <= n / 2 ) { // 依照树的重心的定义统计 centroids . push_back ( cur ); } } void get_centroids () { dfs ( 1 , 0 ); } ```   
---|---  
  
### 换根 DP 统计深度和

还可以通过换根 DP 计算出以不同结点为根时，所有结点的深度和（即到当前根结点的距离和）．根据定义，只需要找到使得这一深度和最小的结点即可．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``` |  ```text const int N = 50005 ; int n , siz [ N ]; long long dp [ N ], ans [ N ]; vector < int > g [ N ], centroids ; // 求 1 号节点到所有其他节点的距离和 void dfs1 ( int u , int fa ) { siz [ u ] = 1 ; dp [ u ] = 0 ; for ( int v : g [ u ]) { if ( v == fa ) continue ; dfs1 ( v , u ); siz [ u ] += siz [ v ]; dp [ u ] += dp [ v ] \+ siz [ v ]; // 子树节点到 u 的距离和 } } // 通过换根 DP 求所有节点为树根时对应的距离和 void dfs2 ( int u , int fa ) { for ( int v : g [ u ]) { if ( v == fa ) continue ; ans [ v ] = ans [ u ] \- siz [ v ] \+ ( n \- siz [ v ]); dfs2 ( v , u ); } } // 求树的重心 void get_centroids () { dfs1 ( 1 , 0 ); ans [ 1 ] = dp [ 1 ]; dfs2 ( 1 , 0 ); long long mini = std :: numeric_limits < long long >:: max (); for ( int i = 1 ; i <= n ; i ++ ) { if ( ans [ i ] < mini ) { mini = ans [ i ]; centroids = { i }; } else if ( ans [ i ] == mini ) centroids . push_back ( i ); } } ```   
---|---  
  
## 例题

[Codeforces Round 359 (Div. 1) B. Kay and Snowflake](https://codeforces.com/problemset/problem/685/B)

给定一棵有根树，求出每一棵子树的重心．

解题思路

根据性质 3，对于一棵以点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树，其重心一定在所有以 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的直接子结点为根的子树的重心到点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径上．

类似于上文提到的 DFS 求重心方法，对于每棵以结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树，先求出所有以其直接子结点为根的子树的重心（叶子结点的重心是其本身），然后向上判断路径上的结点是不是重心即可．

在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内可以求出所有子树的重心．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ``` |  ```text #include <iostream> #include <vector> using namespace std ; constexpr int N = 3e5 \+ 5 ; int n , q ; // 点数，询问数 int fa [ N ]; vector < int > son [ N ]; int siz [ N ], // 子树大小 ans [ N ], // 以节点 u 为根的子树重心是 ans[u] weight [ N ]; // 节点重量（不包括向上的子树） void dfs ( int u ) { siz [ u ] = 1 , ans [ u ] = u ; for ( int v : son [ u ]) { dfs ( v ); siz [ u ] += siz [ v ]; weight [ u ] = max ( weight [ u ], siz [ v ]); } for ( int v : son [ u ]) { int p = ans [ v ]; while ( p != u ) { if ( max ( weight [ p ], siz [ u ] \- siz [ p ]) <= siz [ u ] / 2 ) { ans [ u ] = p ; break ; } else p = fa [ p ]; } } } int main () { ios :: sync_with_stdio ( false ); cin >> n >> q ; for ( int v = 2 ; v <= n ; v ++ ) cin >> fa [ v ], son [ fa [ v ]]. push_back ( v ); dfs ( 1 ); while ( q \-- ) { int u ; cin >> u ; cout << ans [ u ] << '\n' ; } return 0 ; } ```   
---|---  
  
## 习题

  * [Gym 101649G Godfather](https://codeforces.com/gym/101649/problem/G)
  * [POJ 1655 Balancing Art](http://poj.org/problem?id=1655)
  * [洛谷 P1364 医院设置](https://www.luogu.com.cn/problem/P1364)
  * [Codeforces 1406C Link Cut Centroids](https://codeforces.com/contest/1406/problem/C)
  * [Codeforces 708C Centroids](https://codeforces.com/problemset/problem/708/C)

## 参考资料

  * [树的 "重心" 的一些性质及动态维护 - fanhq666](https://web.archive.org/web/20181122041458/http://fanhq666.blog.163.com/blog/static/81943426201172472943638)（[博客园转载](https://www.cnblogs.com/qlky/p/5781081.html)）
  * [树的直径、树的重心与树的点分治 - cyendra](https://www.cnblogs.com/zinthos/p/3899075.html)
  * [树的重心的性质及其证明 - suxxsfe](https://www.cnblogs.com/suxxsfe/p/13543253.html)
  * 《信息学奥林匹克辞典》2.4.7.11 章 1. 树的重心

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/tree-centroid.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/tree-centroid.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [CornWorld](https://github.com/CornWorld), [Enter-tainer](https://github.com/Enter-tainer), [H-J-Granger](https://github.com/H-J-Granger), [Ir1d](https://github.com/Ir1d), [ttzc](https://github.com/ttzc), [Anguei](https://github.com/Anguei), [BackSlashDelta](mailto:64258212+backslashdelta@users.noreply.github.com), [CCXXXI](https://github.com/CCXXXI), [ChungZH](https://github.com/ChungZH), [HeRaNO](https://github.com/HeRaNO), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [LucienShui](https://github.com/LucienShui), [Marcythm](https://github.com/Marcythm), [ouuan](https://github.com/ouuan), [StudyingFather](https://github.com/StudyingFather), [wu-zeee](https://github.com/wu-zeee), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
