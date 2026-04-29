# Sqrt Tree - OI Wiki

- Source: https://oi-wiki.org/ds/sqrt-tree/

# Sqrt Tree

## 引入

给你一个长度为 n 的序列 ⟨𝑎𝑖⟩𝑛𝑖=1⟨ai⟩i=1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再给你一个满足结合律的运算 ∘∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（比如 gcd,min,max, +,and,or,xorgcd,min,max,+,and,or,xor![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均满足结合律），然后对于每一次区间询问 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们需要计算 𝑎𝑙 ∘𝑎𝑙+1 ∘⋯ ∘𝑎𝑟al∘al+1∘⋯∘ar![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

Sqrt Tree 可以在 𝑂(𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内预处理，并在 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内回答询问．

## 解释

### 序列分块

首先我们把整个序列分成 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个块，每一块的大小为 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于每个块，我们计算：

  1. 𝑃𝑖Pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 块内的前缀区间询问
  2. 𝑆𝑖Si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 块内的后缀区间询问
  3. 维护一个额外的数组 ⟨𝐵𝑖,𝑗⟩⟨Bi,j⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个块到第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个块的区间答案．

举个例子，假设 ∘∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代表加法运算 ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，序列为 {1,2,3,4,5,6,7,8,9}{1,2,3,4,5,6,7,8,9}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

首先我们将序列分成三块，变成了 {1,2,3},{4,5,6},{7,8,9}{1,2,3},{4,5,6},{7,8,9}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

那么每一块的前缀区间答案和后缀区间答案分别为

𝑃1={1,3,6},𝑆1={6,5,3}𝑃2={4,9,15},𝑆2={15,11,6}𝑃3={7,15,24},𝑆3={24,17,9}P1={1,3,6},S1={6,5,3}P2={4,9,15},S2={15,11,6}P3={7,15,24},S3={24,17,9}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组为：

𝐵=⎡⎢ ⎢⎣62145015390024⎤⎥ ⎥⎦B=[62145015390024]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

（对于 𝑖 >𝑗i>j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的不合法的情况我们假设答案为 0）

显然我们可以在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内预处理这些值，空间复杂度同样是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．处理好之后，我们可以利用它们在 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内回答一些跨块的询问．但对于那些整个区间都在一个块内的询问我们仍不能处理，因此我们还需要处理一些东西．

### 构建一棵树

容易想到我们在每个块内递归地构造上述结构以支持块内的查询．对于大小为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的块我们可以 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 地回答询问．这样我们就建出了一棵树，每一个结点代表序列的一个区间．叶子结点的区间长度为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．一个大小为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的结点有 𝑂(√𝑘)O(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个子节点，于是整棵树的高度是 𝑂(log⁡log⁡𝑛)O(log⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，每一层的区间总长是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，因此我们构建这棵树的复杂度是 𝑂(𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

树高度的证明

根据定义，设「控制」𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的结点的子树高度为 𝑇(𝑛)T(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以写出递归式：

𝑇(𝑛)=𝑇(√𝑛)+1T(n)=T(n)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

作换元 𝑛 =2𝑚n=2m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得

𝑇(2𝑚)=𝑇(2𝑚2)+1T(2m)=T(2m2)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再定义 𝑆(𝑚) =𝑇(2𝑚)S(m)=T(2m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，代入有

𝑆(𝑚)=𝑆(𝑚2)+1S(m)=S(m2)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据主定理，可知 𝑆(𝑚) =𝑂(log⁡𝑚)S(m)=O(log⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此 𝑇(𝑛) =𝑆(log⁡𝑛) =𝑂(log⁡log⁡𝑛)T(n)=S(log⁡n)=O(log⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

现在我们可以在 𝑂(log⁡log⁡𝑛)O(log⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内回答询问．对于询问 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们只需要快速找到一个区间长度最小的结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能包含 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的分块区间中一定是跨块的，就可以 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 地计算答案了．查询一次的总体复杂度是 𝑂(log⁡log⁡𝑛)O(log⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为树高是 𝑂(log⁡log⁡𝑛)O(log⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．不过我们仍可以优化这个过程．

### 优化询问复杂度

容易想到二分高度，然后可以 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 判断是否合法．这样复杂度就变成了 𝑂(log⁡log⁡log⁡𝑛)O(log⁡log⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．不过我们仍可以进一步加速这一过程．

我们假设

  1. 每一块的大小都是 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数幂次；
  2. 每一层上的块大小是相同的．

为此我们需要在序列的末位补充一些 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元素，使得它的长度变成 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数次幂．尽管有些块可能会变成原来的两倍大小，但这样仍是 𝑂(√𝑘)O(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，于是预处理分块的复杂度仍是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

现在我们可以轻松地确定一个询问区间是否被整个地包含在一个块中．对于区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（以 0 为起点），我们把端点写为二进制形式．举一个例子，对于 𝑘 =4,𝑙 =39,𝑟 =46k=4,l=39,r=46![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，二进制表示为

𝑙=3910=1001112,𝑟=4610=1011102l=3910=1001112,r=4610=1011102![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们知道每一层的区间长度是相同的，而分块的大小也是相同的（在上述示例中 2𝑘 =24 =162k=24=16![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．这些块完全覆盖了整个序列，因此第一块代表的元素为 [0,15][0,15]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（二进制表示为 [0000002,0011112][0000002,0011112]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），第二个块代表的元素区间为 [16,31][16,31]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（二进制表示为 [0100002,0111112][0100002,0111112]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），以此类推．我们发现这些在同一个块内的元素的位置在二进制上只有后 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位不同（上述示例中 𝑘 =4k=4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．而示例的 𝑙,𝑟l,r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也只有后 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位不同，因此他们在同一个块中．

因此我们需要检查区间两个端点是否只有后 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位不同，即 𝑙 ⊕𝑟 ≤2𝑘 −1l⊕r≤2k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此我们可以快速找到答案区间所在的层：

  1. 对于每个 𝑖 ∈[1,𝑛]i∈[1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们找到 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最高位上的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 现在对于一个询问 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们计算 𝑙 ⊕𝑟l⊕r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最高位，这样就可以快速确定答案区间所在的层．

这样我们就可以在 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内回答询问啦．

## 更新元素的过程

我们可以在 Sqrt Tree 上更新元素，单点修改和区间修改都是支持的．

### 单点修改

考虑一次单点赋值操作 𝑎𝑥 =𝑣𝑎𝑙ax=val![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们希望高效更新这个操作的信息．

#### 朴素实现

首先我们来看看在做了一次单点修改后 Sqrt Tree 会变成什么样子．

考虑一个长度为 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的结点以及对应的序列：⟨𝑃𝑖⟩,⟨𝑆𝑖⟩,⟨𝐵𝑖,𝑗⟩⟨Pi⟩,⟨Si⟩,⟨Bi,j⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．容易发现在 ⟨𝑃𝑖⟩⟨Pi⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ⟨𝑆𝑖⟩⟨Si⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中都只有 𝑂(√𝑙)O(l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素改变．而在 ⟨𝐵𝑖,𝑗⟩⟨Bi,j⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中则有 𝑂(𝑙)O(l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素被改变．因此有 𝑂(𝑙)O(l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素在树上被更新．因此在 Sqrt Tree 上单点修改的复杂度是 𝑂(𝑛 +√𝑛 +√√𝑛 +⋯) =𝑂(𝑛)O(n+n+n+⋯)=O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 使用 Sqrt Tree 替代 B 数组

注意到单点更新的瓶颈在于更新根结点的 ⟨𝐵𝑖,𝑗⟩⟨Bi,j⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此我们尝试用另一个 Sqrt Tree 代替根结点的 ⟨𝐵𝑖,𝑗⟩⟨Bi,j⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称其为 𝑖𝑛𝑑𝑒𝑥index![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．它的作用和原来的二维数组一样，维护整段询问的答案．其他非根结点仍然使用 ⟨𝐵𝑖,𝑗⟩⟨Bi,j⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维护．注意，如果一个 Sqrt Tree 根结点有 𝑖𝑛𝑑𝑒𝑥index![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结构，称其 Sqrt Tree 是 **含有索引** 的；如果一个 Sqrt Tree 的根结点有 ⟨𝐵𝑖,𝑗⟩⟨Bi,j⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结构，称其是 **没有索引** 的．而 𝑖𝑛𝑑𝑒𝑥index![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这棵树本身是没有索引的．

因此我们可以这样更新 𝑖𝑛𝑑𝑒𝑥index![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 树：

  1. 在 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内更新 ⟨𝑃𝑖⟩⟨Pi⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ⟨𝑆𝑖⟩⟨Si⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 更新 𝑖𝑛𝑑𝑒𝑥index![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的长度是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，但我们只需要更新其中的一个元素（这个元素代表了被改变的块），这一步的时间复杂度是 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的（使用朴素实现的算法）．
  3. 进入产生变化的子节点并使用朴素实现的算法在 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内更新信息．

注意，查询的复杂度仍是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，因为我们最多使用 𝑖𝑛𝑑𝑒𝑥index![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 树一次．于是单点修改的复杂度就是 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

### 更新一个区间

Sqrt Tree 也支持区间覆盖操作 Update⁡(𝑙,𝑟,𝑥)Update⁡(l,r,x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即把区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数全部变成 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对此我们有两种实现方式，其中一种会花费 𝑂(√𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度更新信息，𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间查询；另一种则是 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更新信息，但查询的时间会增加到 𝑂(log⁡log⁡𝑛)O(log⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们可以像线段树一样在 Sqrt Tree 上打懒标记．但是在 Sqrt Tree 上有一点不同．因为下传一个结点的懒标记，复杂度可能达到 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此我们不是在询问的时侯下传标记，而是看父节点是否有标记，如果有标记就把它下传．

#### 第一种实现

在第一种实现中，我们只会给第 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的结点（结点区间长度为 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）打懒标记，在下传标记的时侯直接更新整个子树，复杂度为 𝑂(√𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．操作过程如下：

  1. 考虑第 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层上的结点，对于那些被修改区间完全包含的结点，给他们打一个懒标记；

  2. 有两个块只有部分区间被覆盖，我们直接在 𝑂(√𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内 **重建** 这两个块．如果它本身带有之前修改的懒标记，就在重建的时侯顺便下传标记；

  3. 更新根结点的 ⟨𝑃𝑖⟩⟨Pi⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ⟨𝑆𝑖⟩⟨Si⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，时间复杂度 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；

  4. 重建 𝑖𝑛𝑑𝑒𝑥index![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 树，时间复杂度 𝑂(√𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

现在我们可以高效完成区间修改了．那么如何利用懒标记回答询问？操作如下：

  1. 如果我们的询问被包含在一个有懒标记的块内，可以利用懒标记计算答案；

  2. 如果我们的询问包含多个块，那么我们只需要关心最左边和最右边不完整块的答案．中间的块的答案可以在 𝑖𝑛𝑑𝑒𝑥index![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 树中查询（因为 𝑖𝑛𝑑𝑒𝑥index![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 树在每次修改完后会重建），复杂度是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因此询问的复杂度仍为 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 第二种实现

在这种实现中，每一个结点都可以被打上懒标记．因此在处理一个询问的时侯，我们需要考虑祖先中的懒标记，那么查询的复杂度将变成 𝑂(log⁡log⁡𝑛)O(log⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．不过更新信息的复杂度就会变得更快．操作如下：

  1. 被修改区间完全包含的块，我们把懒标记添加到这些块上，复杂度 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 被修改区间部分覆盖的块，更新 ⟨𝑃𝑖⟩⟨Pi⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ⟨𝑆𝑖⟩⟨Si⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，复杂度 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（因为只有两个被修改的块）；
  3. 更新 𝑖𝑛𝑑𝑒𝑥index![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 树，复杂度 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（使用同样的更新算法）；
  4. 对于没有索引的子树更新他们的 ⟨𝐵𝑖,𝑗⟩⟨Bi,j⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  5. 递归地更新两个没有被完全覆盖的区间．

时间复杂度是 𝑂(√𝑛 +√√𝑛 +⋯) =𝑂(√𝑛)O(n+n+⋯)=O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 实现

下面的实现在 𝑂(𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内建树，在 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内回答询问，在 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内单点修改．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 ``` |  ```text SqrtTreeItem op ( const SqrtTreeItem & a , const SqrtTreeItem & b ); int log2Up ( int n ) { int res = 0 ; while (( 1 << res ) < n ) { res ++ ; } return res ; } class SqrtTree { private : int n , lg , indexSz ; vector < SqrtTreeItem > v ; vector < int > clz , layers , onLayer ; vector < vector < SqrtTreeItem >> pref , suf , between ; void buildBlock ( int layer , int l , int r ) { pref [ layer ][ l ] = v [ l ]; for ( int i = l \+ 1 ; i < r ; i ++ ) { pref [ layer ][ i ] = op ( pref [ layer ][ i \- 1 ], v [ i ]); } suf [ layer ][ r \- 1 ] = v [ r \- 1 ]; for ( int i = r \- 2 ; i >= l ; i \-- ) { suf [ layer ][ i ] = op ( v [ i ], suf [ layer ][ i \+ 1 ]); } } void buildBetween ( int layer , int lBound , int rBound , int betweenOffs ) { int bSzLog = ( layers [ layer ] \+ 1 ) >> 1 ; int bCntLog = layers [ layer ] >> 1 ; int bSz = 1 << bSzLog ; int bCnt = ( rBound \- lBound \+ bSz \- 1 ) >> bSzLog ; for ( int i = 0 ; i < bCnt ; i ++ ) { SqrtTreeItem ans ; for ( int j = i ; j < bCnt ; j ++ ) { SqrtTreeItem add = suf [ layer ][ lBound \+ ( j << bSzLog )]; ans = ( i == j ) ? add : op ( ans , add ); between [ layer \- 1 ][ betweenOffs \+ lBound \+ ( i << bCntLog ) \+ j ] = ans ; } } } void buildBetweenZero () { int bSzLog = ( lg \+ 1 ) >> 1 ; for ( int i = 0 ; i < indexSz ; i ++ ) { v [ n \+ i ] = suf [ 0 ][ i << bSzLog ]; } build ( 1 , n , n \+ indexSz , ( 1 << lg ) \- n ); } void updateBetweenZero ( int bid ) { int bSzLog = ( lg \+ 1 ) >> 1 ; v [ n \+ bid ] = suf [ 0 ][ bid << bSzLog ]; update ( 1 , n , n \+ indexSz , ( 1 << lg ) \- n , n \+ bid ); } void build ( int layer , int lBound , int rBound , int betweenOffs ) { if ( layer >= ( int ) layers . size ()) { return ; } int bSz = 1 << (( layers [ layer ] \+ 1 ) >> 1 ); for ( int l = lBound ; l < rBound ; l += bSz ) { int r = min ( l \+ bSz , rBound ); buildBlock ( layer , l , r ); build ( layer \+ 1 , l , r , betweenOffs ); } if ( layer == 0 ) { buildBetweenZero (); } else { buildBetween ( layer , lBound , rBound , betweenOffs ); } } void update ( int layer , int lBound , int rBound , int betweenOffs , int x ) { if ( layer >= ( int ) layers . size ()) { return ; } int bSzLog = ( layers [ layer ] \+ 1 ) >> 1 ; int bSz = 1 << bSzLog ; int blockIdx = ( x \- lBound ) >> bSzLog ; int l = lBound \+ ( blockIdx << bSzLog ); int r = min ( l \+ bSz , rBound ); buildBlock ( layer , l , r ); if ( layer == 0 ) { updateBetweenZero ( blockIdx ); } else { buildBetween ( layer , lBound , rBound , betweenOffs ); } update ( layer \+ 1 , l , r , betweenOffs , x ); } SqrtTreeItem query ( int l , int r , int betweenOffs , int base ) { if ( l == r ) { return v [ l ]; } if ( l \+ 1 == r ) { return op ( v [ l ], v [ r ]); } int layer = onLayer [ clz [( l \- base ) ^ ( r \- base )]]; int bSzLog = ( layers [ layer ] \+ 1 ) >> 1 ; int bCntLog = layers [ layer ] >> 1 ; int lBound = ((( l \- base ) >> layers [ layer ]) << layers [ layer ]) \+ base ; int lBlock = (( l \- lBound ) >> bSzLog ) \+ 1 ; int rBlock = (( r \- lBound ) >> bSzLog ) \- 1 ; SqrtTreeItem ans = suf [ layer ][ l ]; if ( lBlock <= rBlock ) { SqrtTreeItem add = ( layer == 0 ) ? ( query ( n \+ lBlock , n \+ rBlock , ( 1 << lg ) \- n , n )) : ( between [ layer \- 1 ][ betweenOffs \+ lBound \+ ( lBlock << bCntLog ) \+ rBlock ]); ans = op ( ans , add ); } ans = op ( ans , pref [ layer ][ r ]); return ans ; } public : SqrtTreeItem query ( int l , int r ) { return query ( l , r , 0 , 0 ); } void update ( int x , const SqrtTreeItem & item ) { v [ x ] = item ; update ( 0 , 0 , n , 0 , x ); } SqrtTree ( const vector < SqrtTreeItem > & a ) : n (( int ) a . size ()), lg ( log2Up ( n )), v ( a ), clz ( 1 << lg ), onLayer ( lg \+ 1 ) { clz [ 0 ] = 0 ; for ( int i = 1 ; i < ( int ) clz . size (); i ++ ) { clz [ i ] = clz [ i >> 1 ] \+ 1 ; } int tlg = lg ; while ( tlg > 1 ) { onLayer [ tlg ] = ( int ) layers . size (); layers . push_back ( tlg ); tlg = ( tlg \+ 1 ) >> 1 ; } for ( int i = lg \- 1 ; i >= 0 ; i \-- ) { onLayer [ i ] = max ( onLayer [ i ], onLayer [ i \+ 1 ]); } int betweenLayers = max ( 0 , ( int ) layers . size () \- 1 ); int bSzLog = ( lg \+ 1 ) >> 1 ; int bSz = 1 << bSzLog ; indexSz = ( n \+ bSz \- 1 ) >> bSzLog ; v . resize ( n \+ indexSz ); pref . assign ( layers . size (), vector < SqrtTreeItem > ( n \+ indexSz )); suf . assign ( layers . size (), vector < SqrtTreeItem > ( n \+ indexSz )); between . assign ( betweenLayers , vector < SqrtTreeItem > (( 1 << lg ) \+ bSz )); build ( 0 , 0 , n , 0 ); } }; ```   
---|---  
  
## 习题

[CodeChef - SEGPROD](https://www.codechef.com/NOV17/problems/SEGPROD)

**本页面主要译自[Sqrt Tree - Algorithms for Competitive Programming](https://cp-algorithms.com/data_structures/sqrt-tree.html)，版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/sqrt-tree.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/sqrt-tree.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [sshwy](https://github.com/sshwy), [mgt](mailto:i@margatroid.xyz), [Enter-tainer](https://github.com/Enter-tainer), [ouuan](https://github.com/ouuan), [Chrogeek](https://github.com/Chrogeek), [ChungZH](https://github.com/ChungZH), [iamtwz](https://github.com/iamtwz), [PerfectPan](https://github.com/PerfectPan), [qwqAutomaton](https://github.com/qwqAutomaton), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
