# 欧拉图 - OI Wiki

- Source: https://oi-wiki.org/graph/euler/

# 欧拉图

本页面将简要介绍欧拉图的概念、实现和应用．

## 定义

本文中仅讨论有限图．

在图论中，**欧拉路径（Eulerian path）** 是经过图中每条边恰好一次的路径，**欧拉回路（Eulerian circuit）** 是经过图中每条边恰好一次的回路． 如果一个图中存在欧拉回路，则这个图被称为**欧拉图（Eulerian graph）** ；如果一个图中不存在欧拉回路但是存在欧拉路径，则这个图被称为**半欧拉图（semi-Eulerian graph）** ．

Warning

此处定义中虽然使用「路径」一词，但严格说来此处使用的概念应该是「迹（trail）」．欧拉路径与欧拉回路仅能使用每条边恰好一次，但并没有对经过顶点的情况进行限制．

## 性质

以下我们假设所讨论的图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中不存在孤立顶点．该假设不失一般性，因为对于存在孤立顶点的图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以下性质对从 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中删除孤立顶点后得到的图 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仍然成立．

对于连通图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以下三个性质是互相等价的：

  1. 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是欧拉图；
  2. 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有顶点的度数都是偶数（对于有向图，每个顶点的入度等于出度）；
  3. 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可被分解为若干条不共边回路的并．

以下我们对等价性进行证明．

若一个图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是欧拉图，那么 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有顶点的度数都是偶数：考虑从任意顶点开始沿着欧拉回路走一圈，则每个点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的度数等于离开点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的次数加到达点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的次数．又由于行动的轨迹是一个回路，则对于每个点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，离开该点的次数等于到达该点的次数．这也就是说，每个点的度数都形如 2𝑘2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即偶数． 特别地，对于有向图，根据相同的证明过程，每个顶点的入度等于出度．

若一个图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有顶点的度数都是偶数（或入度与出度相等），则它可被分解为若干条不共边回路的不交并：考虑从任意顶点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始，选择任意出边 (𝑢,𝑣)(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，走向对应的相邻顶点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并删除 (𝑢,𝑣)(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，直到返回最初开始的顶点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．可以证明该过程必定会最终回到 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：每当到达一个新的顶点 𝑣 ≠𝑢v≠u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，根据上一条性质，该顶点剩余的度数为奇数，也就是说必定存在一条出边，该过程不会在点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 终止．（换句话说，该过程会且仅会在回到点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时停止．）又因图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的边数是有限的，该过程必定会在有限步内停止，则最终必然可以返回 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并得到一条回路．注意到在前述证明中我们仅使用了点度数均为偶数的性质，且在找到并删除一条回路后剩下部分的图仍然满足该性质，我们可以不断重复该过程直到剩下的图为空图，从而将 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 拆分为若干条不共边的回路． 更进一步地，每条回路都可以被从其多次经过的顶点处分解成若干简单环的不交并，所以上述性质中的简单回路亦可被替换为简单环．

若一个连通图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可被分解为若干条不共边回路的不交并，则 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是欧拉图：对于一组不共边回路，每次从中选出两条有共同顶点的回路并将其合并为一条，重复该过程直到不存在有共同顶点的两条回路． 可以证明该过程结束时剩下的回路唯一．对于任意两条不共边回路 𝑃1,𝑃2P1,P2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 𝑃1P1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑃2P2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共点，则可以在共点处直接进行合并；否则，任取 𝑃1P1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的点 𝑣1v1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑃2P2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的点 𝑣2v2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，根据 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连通性，存在连接 𝑣1v1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑣2v2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径 𝑒1,𝑒2,…,𝑒𝑘e1,e2,…,ek![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中的每条边 𝑒𝑖ei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都被一个回路 𝐶𝑖Ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 包含，且 𝑃1P1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝐶1C1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐶𝑖Ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝐶𝑖+1Ci+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐶𝑘Ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑃2P2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均存在共点（或者 𝐶𝑖 =𝐶𝑖+1Ci=Ci+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此情况不影响证明）．此情况下，𝑃1P1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑃2P2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以通过 𝐶1,…,𝐶𝑘C1,…,Ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行合并．也就是说，任意两条回路都可以进行合并，最后剩下的回路必定唯一，且组成该回路的边集是所有不共边回路的并即 𝐸(𝐺)E(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，该回路为 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的欧拉回路，𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为欧拉图．

以上的性质同时也构成了欧拉图的判断条件．具体地说，一个图是欧拉图当且仅当非零度顶点互相（强）连通，且顶点的度数都是偶数（或入度与出度相等）．

对于半欧拉图，其性质与欧拉图相似：一个半欧拉图具有恰好两个奇度数的顶点，且这两个顶点就是欧拉路径的两个端点．通过将这两个点连接起来，可以将半欧拉图转化为欧拉图．通过删除欧拉图中的任意一条边，可以得到一个半欧拉图． 由此可以导出半欧拉图的判别法：一个图是半欧拉图当且仅当非零度顶点互相（强）连通，且奇度数顶点恰好有两个．对于有向图，第二个条件为恰存在两个顶点 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 deg+⁡(𝑢) −deg−⁡(𝑢) =1,deg+⁡(𝑣) −deg−⁡(𝑣) = −1deg+⁡(u)−deg−⁡(u)=1,deg+⁡(v)−deg−⁡(v)=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且其余顶点的入度等于出度．

## 欧拉回路/欧拉路径的构造

此处我们介绍最常用的 Hierholzer 算法，该算法的核心思想为利用上述欧拉图性质中的第三点，即欧拉图可以被拆解为若干条不共边回路的并． 可以注意到，在上述证明中其实已经提到了完整可行的将不共边回路合并为欧拉回路的操作，且在使用合适的数据结构储存时（如使用类链表的结构储存环）实现并不困难．

算法的具体流程为先从图中找到一条回路作为当前回路，每次从当前回路中选取剩余度数不为零的点，从该点出发找到一条新的简单回路，并将该简单回路与当前回路合并，重复该过程直到当前回路中的所有点均无剩余度数，此时的当前回路即为欧拉回路．

该算法同样适用于有向图．对于半欧拉图，可以从图中找到一条连接两个奇度数点的路径作为当前路径，每次选取度数非零的点寻找简单回路并将其与当前路径合并，最后得到欧拉路径．

### 实现

Hierholzer 算法的伪代码如下：

1𝐈𝐧𝐩𝐮𝐭. The edges of the graph 𝑒, where each element in 𝑒 is (𝑢,𝑣)2𝐎𝐮𝐭𝐩𝐮𝐭. The vertex of the Euler Road of the input graph.3𝐌𝐞𝐭𝐡𝐨𝐝. 4𝐅𝐮𝐧𝐜𝐭𝐢𝐨𝐧 Hierholzer (𝑣)5𝑐𝑖𝑟𝑐𝑙𝑒←Find a Circle in 𝑒 Begin with 𝑣6𝐢𝐟 𝑐𝑖𝑟𝑐𝑙𝑒=∅7𝐫𝐞𝐭𝐮𝐫𝐧 𝑣8𝑒←𝑒−𝑐𝑖𝑟𝑐𝑙𝑒9𝐟𝐨𝐫 each 𝑣∈𝑐𝑖𝑟𝑐𝑙𝑒10𝑣←Hierholzer(𝑣)11𝐫𝐞𝐭𝐮𝐫𝐧 𝑐𝑖𝑟𝑐𝑙𝑒12𝐄𝐧𝐝𝐟𝐮𝐧𝐜𝐭𝐢𝐨𝐧13𝐫𝐞𝐭𝐮𝐫𝐧 Hierholzer(any vertex)1Input. The edges of the graph e, where each element in e is (u,v)2Output. The vertex of the Euler Road of the input graph.3Method. 4Function Hierholzer (v)5circle←Find a Circle in e Begin with v6if circle=∅7return v8e←e−circle9for each v∈circle10v←Hierholzer(v)11return circle12Endfunction13return Hierholzer(any vertex)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 时间复杂度分析

Hierholzer 算法的时间复杂度为 𝑂(|𝐸| +|𝑉|)O(|E|+|V|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注意到在前述正确性分析中，在欧拉图或半欧拉图上寻找简单回路（或半欧拉图的初始路径）的过程是 **无需回溯** 的，只要沿着剩下的边一直走就必定可以发现所求的回路或路径，且 **每条边仅会被访问一次** ． 为了利用这一性质，在实现上应采取类链表的方式储存图中的边，如邻接表或链式前向星，以便每条边在被访问过后即刻删除之．如果采用朴素的邻接矩阵进行储存，则每次寻边耗时 𝑂(|𝑉|)O(|V|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，总复杂度为 𝑂(|𝑉||𝐸|)O(|V||E|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

Note

事实上，该算法的准确复杂度应为 𝑂(|𝐸|)O(|E|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而非 𝑂(|𝑉| +|𝐸|)O(|V|+|E|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这是因为该算法的实现方式可以采取依赖于边而不依赖于点的方法，通过维护剩余边的总链表来进行下一步回路的寻找．

如果需要输出字典序最小的欧拉路或欧拉回路，则需要将边排序，时间复杂度为 Θ(|𝐸|log⁡|𝐸|)Θ(|E|log⁡|E|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 Θ(|𝐸|)Θ(|E|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（使用计数排序或者基数排序）．

### 应用

有向欧拉图可用于计算机译码．

设有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字母，希望构造一个有 𝑚𝑛mn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个扇形的圆盘，每个圆盘上放一个字母，使得圆盘上每连续 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位对应长为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的符号串．转动一周（𝑚𝑛mn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次）后得到由 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字母产生的长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑚𝑛mn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个各不相同的符号串．

![](./images/euler1.svg)

构造如下有向欧拉图：

设 𝑆 ={𝑎1,𝑎2,⋯,𝑎𝑚}S={a1,a2,⋯,am}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，构造 𝐷 =⟨𝑉,𝐸⟩D=⟨V,E⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如下：

𝑉 ={𝑎𝑖1𝑎𝑖2⋯𝑎𝑖𝑛−1|𝑎𝑖 ∈𝑆,1 ≤𝑖 ≤𝑛 −1}V={ai1ai2⋯ain−1|ai∈S,1≤i≤n−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝐸 ={𝑎𝑗1𝑎𝑗2⋯𝑎𝑗𝑛−1|𝑎𝑗 ∈𝑆,1 ≤𝑗 ≤𝑛}E={aj1aj2⋯ajn−1|aj∈S,1≤j≤n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

规定 𝐷D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中顶点与边的关联关系如下：

顶点 𝑎𝑖1𝑎𝑖2⋯𝑎𝑖𝑛−1ai1ai2⋯ain−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 引出 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边：𝑎𝑖1𝑎𝑖2⋯𝑎𝑖𝑛−1𝑎𝑟,𝑟 =1,2,⋯,𝑚ai1ai2⋯ain−1ar,r=1,2,⋯,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

边 𝑎𝑗1𝑎𝑗2⋯𝑎𝑗𝑛−1aj1aj2⋯ajn−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 引入顶点 𝑎𝑗2𝑎𝑗3⋯𝑎𝑗𝑛aj2aj3⋯ajn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

![](./images/euler2.svg)

这样的 𝐷D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是连通的，且每个顶点入度等于出度（均等于 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），所以 𝐷D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是有向欧拉图．

任求 𝐷D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中一条欧拉回路 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，取 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中各边的最后一个字母，按各边在 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的顺序排成圆形放在圆盘上即可．

## 例题

[洛谷 P2731 骑马修栅栏](https://www.luogu.com.cn/problem/P2731)

给定一张有 500 个顶点的无向图，求这张图的一条欧拉路或欧拉回路．如果有多组解，输出最小的那一组．

在本题中，欧拉路或欧拉回路不需要经过所有顶点．

边的数量 m 满足 1 ≤𝑚 ≤10241≤m≤1024![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解题思路

本题为 Hierholzer 算法的直接应用．

保存答案可以使用 `std::stack<int>`，因为如果找的不是回路的话必须将那一部分放在最后．

注意，不能使用邻接矩阵存图，否则时间复杂度会退化为 Θ(𝑛𝑚)Θ(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于需要将边排序，建议使用前向星或者 `std::vector` 存图．示例代码使用 `std::vector`．

示例代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 ``` |  ```text #include <algorithm> #include <iostream> #include <stack> #include <vector> using namespace std ; struct edge { int to ; bool exists ; int revref ; bool operator < ( const edge & b ) const { return to < b . to ; } }; vector < edge > beg [ 505 ]; int cnt [ 505 ]; constexpr int dn = 500 ; stack < int > ans ; void Hierholzer ( int x ) { // 关键函数 for ( int & i = cnt [ x ]; i < ( int ) beg [ x ]. size ();) { if ( beg [ x ][ i ]. exists ) { edge e = beg [ x ][ i ]; beg [ x ][ i ]. exists = beg [ e . to ][ e . revref ]. exists = false ; ++ i ; Hierholzer ( e . to ); } else { ++ i ; } } ans . push ( x ); } int deg [ 505 ]; int reftop [ 505 ]; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); for ( int i = 1 ; i <= dn ; ++ i ) { beg [ i ]. reserve ( 1050 ); // vector 用 reserve 避免动态分配空间，加快速度 } int m ; cin >> m ; for ( int i = 1 ; i <= m ; ++ i ) { int a , b ; cin >> a >> b ; beg [ a ]. push_back ( edge { b , true , 0 }); beg [ b ]. push_back ( edge { a , true , 0 }); ++ deg [ a ]; ++ deg [ b ]; } for ( int i = 1 ; i <= dn ; ++ i ) { if ( ! beg [ i ]. empty ()) { sort ( beg [ i ]. begin (), beg [ i ]. end ()); // 为了要按字典序贪心，必须排序 } } for ( int i = 1 ; i <= dn ; ++ i ) { for ( int j = 0 ; j < ( int ) beg [ i ]. size (); ++ j ) { beg [ i ][ j ]. revref = reftop [ beg [ i ][ j ]. to ] ++ ; } } int bv = 0 ; for ( int i = 1 ; i <= dn ; ++ i ) { if ( ! deg [ bv ] && deg [ i ]) { bv = i ; } else if ( ! ( deg [ bv ] & 1 ) && ( deg [ i ] & 1 )) { bv = i ; } } Hierholzer ( bv ); while ( ! ans . empty ()) { cout << ans . top () << '\n' ; ans . pop (); } } ```   
---|---  
  
## 习题

  * [SGU 101 Domino](https://codeforces.com/problemsets/acmsguru/problem/99999/101)

  * [POJ 1780 Code](http://poj.org/problem?id=1780)

  * [洛谷 P1127 词链](https://www.luogu.com.cn/problem/P1127)

  * [洛谷 P1333 瑞瑞的木棍](https://www.luogu.com.cn/problem/P1333)

  * [洛谷 P1341 无序字母对](https://www.luogu.com.cn/problem/P1341)

  * [洛谷 P6066 [USACO05JAN]Watchcow S](https://www.luogu.com.cn/problem/P6066)

  * [洛谷 P6628 [省选联考 2020 B 卷] 丁香之路](https://www.luogu.com.cn/problem/P6628)

  * [洛谷 P3520 [POI 2011] SMI-Garbage](https://www.luogu.com.cn/problem/P3520)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/euler.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/euler.md "edit.link.title")  
>  __本页面贡献者：[orzAtalod](https://github.com/orzAtalod), [Ir1d](https://github.com/Ir1d), [NachtgeistW](https://github.com/NachtgeistW), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [H-J-Granger](https://github.com/H-J-Granger), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [CCXXXI](https://github.com/CCXXXI), [Early0v0](https://github.com/Early0v0), [mgt](mailto:i@margatroid.xyz), [AngelKitty](https://github.com/AngelKitty), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [Konano](https://github.com/Konano), [leoleoasd](https://github.com/leoleoasd), [LovelyBuggies](https://github.com/LovelyBuggies), [lychees](https://github.com/lychees), [Makkiy](https://github.com/Makkiy), [Marcythm](https://github.com/Marcythm), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [aofall](https://github.com/aofall), [c-forrest](https://github.com/c-forrest), [Chrogeek](https://github.com/Chrogeek), [CoelacanthusHex](https://github.com/CoelacanthusHex), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Great-designer](https://github.com/Great-designer), [Henry-ZHR](https://github.com/Henry-ZHR), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [kxccc](https://github.com/kxccc), [lowtune](https://github.com/lowtune), [mcendu](https://github.com/mcendu), [Menci](https://github.com/Menci), [Peanut-Tang](https://github.com/Peanut-Tang), [Persdre](https://github.com/Persdre), [PsephurusGladius](https://github.com/PsephurusGladius), [shuzhouliu](https://github.com/shuzhouliu), [SukkaW](https://github.com/SukkaW), [zhu-yifang](https://github.com/zhu-yifang), [zryi2003](https://github.com/zryi2003)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
