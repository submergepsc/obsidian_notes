# 公平组合游戏 - OI Wiki

- Source: https://oi-wiki.org/math/game-theory/impartial-game/

# 公平组合游戏

前置知识：[博弈论简介](../intro/)

本文讨论 [公平组合游戏](../intro/#公平组合博弈)．

公平组合游戏中，最基础也最重要的是正常 Nim 游戏．Sprague–Grundy 定理指出，所有正常规则的公平组合游戏都等价于一个单堆 Nim 游戏．由此，可以发展出 Sprague–Grundy 函数和 Nim 数的概念，它们完全地刻画了一个正常规则的公平组合游戏．因此，本文首先建立了正常 Nim 游戏的结论和 Sprague–Grundy 理论．随后，本文讨论了算法竞赛中常见的一些公平组合游戏．

最后，本文简单地讨论了反常 Nim 游戏．反常游戏相对于正常游戏来说要复杂得多，也很少在算法竞赛中出现．本文提到的游戏，如果没有特别说明，均默认为正常的公平组合游戏．

「状态」、「局面」与「游戏」

本文会交替地使用这三个词语．在博弈论中，游戏的状态（state）通常包括到游戏的某一时刻为止，所有可能与游戏有关的信息．在一般的情形下，游戏的状态通常包括双方玩家过往的行动、已经实现的随机变量值、双方已知信息的内容等．游戏的局面（position）相对来说并非博弈论的标准术语，通常指在游戏的某一时刻，双方玩家面对的局势，例如棋类游戏中各棋子的位置等．仅对于公平组合游戏（或更一般的零和、确定、完美信息游戏）而言，由于游戏不涉及随机性，且玩家未来的行动集合与收益函数均与到达当前局面的历史路径（即之前双方的行为）无关，所以，游戏的状态（state）和局面（position）没有区别，且都可以看作博弈图上的一个结点（node）．由于一个游戏（game）总是可以由它的初始局面描述，所以有时也会直接使用「局面」一词代指游戏本身．

## Nim 游戏

Nim 游戏的规则很简单：

Nim 游戏

共有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆有 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚石子．两名玩家轮流取走任意一堆中的任意多枚石子，但不能不取．取走最后一枚石子的玩家获胜．

容易验证，Nim 游戏是正常规则的公平组合游戏．

例子

举个例子．当前，有 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子，石子的数量分别为 2,5,42,5,4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，可以取走第 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆中的 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品，局面就变成了 0,5,40,5,4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；也可以取走第 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆的 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品，局面就变成了 2,1,42,1,4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果某一时刻的局面变为了 0,0,50,0,5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，甲取走了第 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆的 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品，也就是取走了最后一个物品，此时甲获胜．

### 博弈图和状态

Nim 游戏中，局面可能的变化可以用博弈图来描述．

将每一个可能的状态都看作是图中的一个结点，并将状态向它的后继状态（即通过一次操作可以达到的状态）连边，就得到一个有向无环图，这就是博弈图．图是无环的，因为 Nim 游戏中，每次操作，石子的总数量都是严格减少的．

例子

例如，对于初始局面有 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子，且每堆石子的数量分别为 1,1,21,1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Nim 游戏，可以绘制如下的博弈图：

![博弈图的例子](./images/nim.svg)

马上就会提到，图中的红色结点表示必胜状态，黑色结点表示必败状态．

由于 Nim 游戏是公平组合游戏，每个玩家是否有必胜策略，只取决当前游戏所处的状态，而与玩家的身份无关．因此，所有状态可以分为（先手）**必胜状态** 和（先手）**必败状态** ，分别记为 NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 态和 PP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 态1．这个定义适用于所有公平组合游戏．

通过下述引理，可以归纳地将所有状态标记为必胜状态和必败状态：

引理

正常规则的公平组合游戏中，

  1. 没有后继状态的状态是必败状态 PP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  2. 一个状态是必胜状态 NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当存在至少一个它的后继状态为必败状态 PP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  3. 一个状态是必败状态 PP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当它的所有后继状态均为必胜状态 NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

对于第一条，如果玩家当前已经没有可选的行动，那么玩家已经输掉了游戏．

对于第二条，如果该状态至少有一个后继状态为必败状态，那么玩家可以操作到该必败状态；此时，对手面临了先手必败状态，玩家自己就获得了胜利．

对于第三条，如果不存在一个后继状态为必败状态，那么无论如何，玩家只能操作到必胜状态；此时，对手面临了先手必胜状态，玩家自己就输掉了游戏．

所有公平组合游戏中，博弈图都是有向无环图．所以，通过这三条性质，可以在绘制出博弈图后，在 𝑂(|𝑉| +|𝐸|)O(|V|+|E|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内，计算出每个状态是必胜状态还是必败状态．其中，|𝑉||V|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为博弈图的状态数目，|𝐸||E|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为边数，即所有状态可以采取的行动的数量的总和．

这一引理可以推广到反常游戏和有向图可能有环的情形．相关讨论详见 有向图游戏 一节．

### Nim 和

继续考察 Nim 游戏．

通过绘制博弈图，可以在 Ω(∏𝑛𝑖=1𝑎𝑖)Ω(∏i=1nai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内求出某一局面是否是先手必胜．但是，这样做的复杂度过高，无法实际应用．实际上，可以发现 Nim 游戏的状态是否先手必胜，只与当前局面的石子数目的 Nim 和有关．

Nim 和

自然数 𝑎1,𝑎2,⋯,𝑎𝑛a1,a2,⋯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **Nim 和** （Nim sum）定义为 𝑎1 ⊕𝑎2 ⊕⋯ ⊕𝑎𝑛a1⊕a2⊕⋯⊕an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

所谓 Nim 和，就是 [异或运算](../../bit/#位运算)．

定理

Nim 游戏中，状态 (𝑎1,𝑎2,⋯,𝑎𝑛)(a1,a2,⋯,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是必败状态 PP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当 Nim 和

𝑎1⊕𝑎2⊕⋯⊕𝑎𝑛=0.a1⊕a2⊕⋯⊕an=0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

对所有可能的状态应用归纳法：

  1. 如果 𝑎𝑖 =0ai=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对所有 𝑖 =1,⋯,𝑛i=1,⋯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立，该状态没有后继状态，且 Nim 和等于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，命题成立．
  2. 如果 𝑘 =𝑎1 ⊕𝑎2 ⊕⋯ ⊕𝑎𝑛 ≠0k=a1⊕a2⊕⋯⊕an≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，需要证明该状态是必胜状态．也就是说，需要构造一个合法移动，使得后继状态为必败状态；由归纳假设，只需要证明后继状态满足 𝑎′1 ⊕𝑎′2 ⊕⋯ ⊕𝑎′𝑛 =0a1′⊕a2′⊕⋯⊕an′=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．利用 Nim 和（即异或）的性质，这等价于说，存在一堆石子，将 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 拿走若干颗石子，可以得到 𝑎𝑖 ⊕𝑘ai⊕k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即 𝑎𝑖 >𝑎𝑖 ⊕𝑘ai>ai⊕k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

实际上，设 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制表示中，最高位的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是第 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位．那么，一定存在某个 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得它的二进制第 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于相应的石子堆，就一定有 𝑎𝑖 >𝑎𝑖 ⊕𝑘ai>ai⊕k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为 𝑎𝑖 ⊕𝑘ai⊕k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中第 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，更高位和 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一样．

  3. 如果 𝑎1 ⊕𝑎2 ⊕⋯ ⊕𝑎𝑛 =0a1⊕a2⊕⋯⊕an=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，需要证明该状态是必败状态．由归纳假设可知，只要证明它的所有后继状态的 Nim 和都不是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这是必然的，任何合法移动将 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变为 𝑎′𝑖 ≠𝑎𝑖ai′≠ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就必然会使得 Nim 和变为 𝑎′𝑖 ⊕𝑎𝑖 ≠0ai′⊕ai≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由此，可以在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内判断 Nim 游戏的一个状态是否为先手必胜状态．

## Sprague–Grundy 理论

Sprague–Grundy 理论指出，所有公平组合游戏都等价于单堆 Nim 游戏．这一结论主要应用的场景，就是游戏由多个相互独立的子游戏组成的情形．此时，游戏的状态判定可以通过计算子游戏的 SG 函数值的 Nim 和来完成．如果游戏本身没有这样的结构，那么，判定必胜状态和必败状态只需要应用前文博弈图一节的 引理．

### 游戏的记法

前文已经说明，所有公平组合游戏都可以通过绘制博弈图来描述．由于博弈图中，每个状态的性质只由它的后继状态决定，所以，可以将博弈图中的一个状态 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 用它的后继状态的集合来表示．

例子（续）

以上文的博弈图为例，可以得到如下状态表示：

𝑆0,0,0={},𝑆0,1,0={𝑆0,0,0}={{}},𝑆0,0,1={𝑆0,0,0}={{}},𝑆0,0,2={𝑆0,0,0,𝑆0,0,1}={{},{{}}},𝑆0,1,1={𝑆0,0,0,𝑆0,1,0,𝑆0,0,1}={{},{{}}},𝑆0,1,2={𝑆0,0,2,𝑆0,1,0,𝑆0,1,1}={{{}},{{},{{}}}}.S0,0,0={},S0,1,0={S0,0,0}={{}},S0,0,1={S0,0,0}={{}},S0,0,2={S0,0,0,S0,0,1}={{},{{}}},S0,1,1={S0,0,0,S0,1,0,S0,0,1}={{},{{}}},S0,1,2={S0,0,2,S0,1,0,S0,1,1}={{{}},{{},{{}}}}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑆0,1,0 =𝑆0,0,1S0,1,0=S0,0,1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑆0,0,2 =𝑆0,1,1S0,0,2=S0,1,1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

一个游戏可以用它的初始状态表示．

尽管公平游戏的表示可能相当复杂，单堆 Nim 游戏相对来说简单很多．只有一堆石子，石子数量为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，它可以表示为

∗0={}, ∗𝑛={∗𝑚:𝑚<𝑛, 𝑚∈𝐍}={∗0,∗1,⋯,∗(𝑛−1)}.∗0={}, ∗n={∗m:m<n, m∈N}={∗0,∗1,⋯,∗(n−1)}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，记号 ∗𝑛∗n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示石子数量为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时的单堆 Nim 游戏（的初始状态）．

例子（续）

利用这一记号，上面的例子中的状态可以简单地表示为

𝑆0,0,0=∗0, 𝑆0,1,0=𝑆0,0,1=∗1, 𝑆0,0,2=𝑆0,1,1=∗2, 𝑆0,1,2={∗1,∗2}.S0,0,0=∗0, S0,1,0=S0,0,1=∗1, S0,0,2=S0,1,1=∗2, S0,1,2={∗1,∗2}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在随后的讨论中，记号 𝑇 ∈𝑆T∈S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 应当理解为状态 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是状态 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的后继状态．

### 游戏的和与等价

游戏的等价关系，依赖于游戏的和2的概念．

游戏的和

游戏 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **和** （sum），或称 **游戏组合** （combined game），记作 𝐺 +𝐻G+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，是指游戏

𝐺+𝐻={𝑔+𝐻:𝑔∈𝐺}∪{𝐺+ℎ:ℎ∈𝐻}.G+H={g+H:g∈G}∪{G+h:h∈H}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

游戏的和，可以理解为由两个同时进行且互不干扰的子游戏组成的游戏，玩家在每一步能且只能选择其中一个子游戏移动一步，且游戏在两个子游戏都无法移动时结束．游戏的和的概念，可以推广到任意多个游戏的情形，且满足结合律和交换律——也就是说，多个游戏组合的结果，和组合进行的次序以及游戏的顺序都无关．Nim 游戏就是多个单堆 Nim 游戏的和．

一个观察是，尽管单堆 Nim 游戏中，除了没有石子的情形，都是先手必胜状态，但是这些不同的单堆 Nim 游戏在和其他的单堆 Nim 游戏组合起来时，得到的游戏并不相同．比如，游戏 ∗𝑛∗n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只有在和另一个 ∗𝑛∗n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组合时，才能得到一个必败游戏；和所有其他的游戏 ∗𝑛′ ≠ ∗𝑛∗n′≠∗n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组合，得到的游戏都是必胜游戏．

这个观察带来的启示是，可以通过考察与其他游戏的和来研究某个游戏的性质．这就引出了游戏的等价的概念．

游戏的等价关系

如果对于所有游戏 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，游戏 𝐺1 +𝐻G1+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐺2 +𝐻G2+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都同处于必败状态或必胜状态，那么，称游戏 𝐺1G1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐺2G2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **等价** （equivalent），记作 𝐺1 ≈𝐺2G1≈G2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

容易验证，这样定义的 ≈≈![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 确实是全体公平游戏上的 [等价关系](../../order-theory/#二元关系)．

### Sprague–Grundy 函数

对 Nim 游戏的分析说明，不同的单堆 Nim 游戏互不等价．但是，所有的公平游戏都等价于某个单堆 Nim 游戏．由此，可以给每个公平游戏都分配一个数字，这就是 Sprague–Grundy 函数．

为了证明这些结论，首先需要建立关于游戏等价关系的两个引理．第一，将必败游戏和任何游戏组合到一起，都和原来的游戏等价．

引理 1

对于游戏 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和任何必败游戏 𝐴 ∈PA∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝐺 ≈𝐺 +𝐴G≈G+A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

按照定义，只需要证明对于任何游戏 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 𝐺 +𝐻 ≈𝐺 +𝐴 +𝐻G+H≈G+A+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．

如果游戏 𝐺 +𝐻G+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有必胜策略，那么，游戏 𝐺 +𝐴 +𝐻G+A+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也有必胜策略．如果对手在子游戏 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中进行了移动，就进行移动，将它恢复至必败状态；否则，按照游戏 𝐺 +𝐻G+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的必胜策略移动．这样一定能保证最终的胜利．

如果游戏 𝐺 +𝐻G+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是必败游戏，那么，游戏 𝐺 +𝐴 +𝐻G+A+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也同样是必败游戏．因为无论这一回合进行的是子游戏 𝐺 +𝐻G+H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和子游戏 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的移动，对手都可以在下一回合将相应子游戏恢复至必败状态．最终，先手玩家一定无法获胜．

第二，两个游戏等价，当且仅当它们的和是必败游戏．这一引理提供了证明两个游戏等价的方法．

引理 2

游戏 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等价，当且仅当 𝐺 +𝐺′ ∈PG+G′∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是必败游戏．

证明

如果游戏 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等价，那么，𝐺 +𝐺′G+G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝐺 +𝐺G+G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同时必胜或同时必败，而游戏 𝐺 +𝐺G+G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是必败游戏．这是因为，对于先手玩家的任何操作，后手玩家都可以在另一个子游戏中采取相同的行动，最后一定是先手玩家无法移动．

反过来，如果 𝐺 +𝐺′G+G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是必败游戏，那么，由引理 1 可知，𝐺 ≈𝐺 +(𝐺 +𝐺′) =(𝐺 +𝐺) +𝐺′ ≈𝐺′G≈G+(G+G′)=(G+G)+G′≈G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

利用这些引理，可以得到如下定理：

定理（Sprague–Grundy）

对于任何一个（有限）公平游戏 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都存在 𝑛 ∈𝐍n∈N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝐺 ≈ ∗𝑛G≈∗n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．

证明

要证明定理的结论，可以应用数学归纳法．设游戏 𝐺 ={𝐺1,𝐺2,⋯,𝐺𝑘}G={G1,G2,⋯,Gk}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据归纳假设可知，存在 𝑛1,𝑛2,⋯,𝑛𝑘n1,n2,⋯,nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝐺𝑖 ≈ ∗𝑛𝑖Gi≈∗ni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，可以考察游戏

𝐺′={∗𝑛1,∗𝑛2,⋯,∗𝑛𝑘}.G′={∗n1,∗n2,⋯,∗nk}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将要证明的是，𝐺′ ≈ ∗𝑚G′≈∗m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑚 =mex⁡{𝑛1,𝑛2,⋯,𝑛𝑘}m=mex⁡{n1,n2,⋯,nk}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是没有出现在集合中的最小自然数．

第一步，需要说明 𝐺 ≈𝐺′G≈G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据 引理 2，只需要证明游戏 𝐺 +𝐺′G+G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是必败游戏．不妨假设 𝐺 ≠ ∗0G≠∗0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果先手玩家选择 𝐺𝑖Gi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么后手玩家就可以选择 ∗𝑛𝑖∗ni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；反过来，如果先手玩家选择了 ∗𝑛𝑖∗ni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，后手玩家就可以选择 𝐺𝑖Gi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．总之，在这两步操作后，游戏变为 𝐺𝑖 + ∗𝑛𝑖Gi+∗ni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，根据引理 2 和 𝐺𝑖 ≈ ∗𝑛𝑖Gi≈∗ni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这是必败游戏．这就证明了 𝐺 ≈𝐺′G≈G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

第二步，需要说明 𝐺′ ≈ ∗𝑚G′≈∗m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据 引理 2，只需要证明 𝐺′ + ∗𝑚G′+∗m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是必败游戏．不妨假设 𝐺′ ≠ ∗0G′≠∗0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果先手玩家选择了 ∗𝑛𝑖 ∈ ∗𝑚∗ni∈∗m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么根据 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义，后手玩家就可以选择 ∗𝑛𝑖 ∈𝐺′∗ni∈G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将游戏局面变为 ∗𝑛𝑖 + ∗𝑛𝑖 ∈P∗ni+∗ni∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，先手必败．如果先手玩家选择了 ∗𝑛𝑖 ∈𝐺′∗ni∈G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑛𝑖 <𝑚ni<m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，后手玩家可以选择 ∗𝑛𝑖 ∈ ∗𝑚∗ni∈∗m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，游戏局面同样变为 ∗𝑛𝑖 + ∗𝑛𝑖 ∈P∗ni+∗ni∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，先手必败．最后，如果先手玩家选择了 ∗𝑛𝑖 ∈𝐺′∗ni∈G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑛𝑖 >𝑚ni>m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，后手玩家可以选择 ∗𝑚 ∈ ∗𝑛𝑖∗m∈∗ni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，游戏局面变为 ∗𝑚 + ∗𝑚 ∈P∗m+∗m∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，先手必败．这就证明了 𝐺′ ≈ ∗𝑚G′≈∗m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由等价关系的传递性可知，𝐺 ≈ ∗𝑚G≈∗m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就完成了归纳，证明所有游戏 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都等价于一个单堆 Nim 游戏．

这一结论说明，可以为每一个公平游戏 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都分配一个自然数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝐺 ≈ ∗𝑛G≈∗n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

Nim 数

一个公平游戏 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的 **Nim 数** （nimber）就是使得 𝐺 ≈ ∗𝑛G≈∗n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立的唯一自然数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这个将公平游戏映射到 Nim 数的函数称为 **Sprague–Grundy 函数** （Sprague–Grundy function），简称 **SG 函数** ，记作 SG⁡( ⋅)SG⁡(⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于每个公平游戏的状态都是另一个公平游戏，所以，对于公平游戏的每一个状态都可以计算相应的 Nim 数，也称为相应的 SG 函数值．

根据本节定理的证明过程可知，Sprague–Grundy 函数可以递归地计算如下：

推论

公平游戏 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的一个状态 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的 Sprague–Grundy 函数值 SG⁡(𝑥)SG⁡(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足

SG⁡(𝑥)=mex⁡{SG⁡(𝑥′):𝑥′∈𝑥}.SG⁡(x)=mex⁡{SG⁡(x′):x′∈x}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，mex⁡(𝐴) :=min{𝑛 ∈𝐍 :𝑛 ∉𝐴}mex⁡(A):=min{n∈N:n∉A}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是没有出现在集合 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的最小自然数．

也就是说，一个状态的 SG 函数值，等于它的所有后继状态的 SG 函数值的 mexmex![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值．

利用 SG 函数值（即 Nim 数），可以判断一个状态是否为先手必胜状态．

推论

公平游戏 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的一个状态 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是先手必胜状态，当且仅当 SG⁡(𝑥) ≠0SG⁡(x)≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最后，游戏的和的 SG 函数值，就是子游戏的 SG 函数值的 Nim 和（即异或）．

定理（Sprague–Grundy）

对于公平游戏 𝐺1,𝐺2,⋯,𝐺𝑛G1,G2,⋯,Gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

SG⁡(𝐺1+𝐺2+⋯+𝐺𝑛)=SG⁡(𝐺1)⊕SG⁡(𝐺2)⊕⋯⊕SG⁡(𝐺𝑛).SG⁡(G1+G2+⋯+Gn)=SG⁡(G1)⊕SG⁡(G2)⊕⋯⊕SG⁡(Gn).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

因为 ∗𝑎1 + ∗𝑎2 +⋯ + ∗𝑎𝑛∗a1+∗a2+⋯+∗an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是石子数量为 (𝑎1,𝑎2,⋯,𝑎𝑛)(a1,a2,⋯,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Nim 游戏，所以，根据 Nim 游戏的结论可知，游戏

∗𝑎1+∗𝑎2+⋯+∗𝑎𝑛+∗(𝑎1⊕𝑎2⊕⋯⊕𝑎𝑛)∗a1+∗a2+⋯+∗an+∗(a1⊕a2⊕⋯⊕an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

是先手必败的．根据 引理 2，有

∗𝑎1+∗𝑎2+⋯+∗𝑎𝑛≈∗(𝑎1⊕𝑎2⊕⋯⊕𝑎𝑛).∗a1+∗a2+⋯+∗an≈∗(a1⊕a2⊕⋯⊕an).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，有

SG⁡(∗𝑎1+∗𝑎2+⋯+∗𝑎𝑛)=𝑎1⊕𝑎2⊕⋯⊕𝑎𝑛.SG⁡(∗a1+∗a2+⋯+∗an)=a1⊕a2⊕⋯⊕an.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 𝑎𝑖 =SG⁡(𝐺𝑖)ai=SG⁡(Gi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有 𝐺𝑖 ≈ ∗𝑎𝑖Gi≈∗ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，利用 ≈≈![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的代数性质，有

(𝐺1+𝐺2+⋯+𝐺𝑛)+(∗𝑎1+∗𝑎2+⋯+∗𝑎𝑛)=𝑛∑𝑖=1(𝐺𝑖+∗𝑎𝑖)∈P.(G1+G2+⋯+Gn)+(∗a1+∗a2+⋯+∗an)=∑i=1n(Gi+∗ai)∈P.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，就有

SG⁡(𝐺1+𝐺2+⋯+𝐺𝑛)=SG⁡(∗𝑎1+∗𝑎2+⋯+∗𝑎𝑛)=𝑎1⊕𝑎2⊕⋯⊕𝑎𝑛=SG⁡(𝐺1)⊕SG⁡(𝐺2)⊕⋯⊕SG⁡(𝐺𝑛).SG⁡(G1+G2+⋯+Gn)=SG⁡(∗a1+∗a2+⋯+∗an)=a1⊕a2⊕⋯⊕an=SG⁡(G1)⊕SG⁡(G2)⊕⋯⊕SG⁡(Gn).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用这一定理，在计算游戏的和的 SG 函数值时，可以大幅简化计算．

由此，可以总结出 SG 函数值的计算方法：

  * 对于多个独立的游戏，可以分别计算它们的 SG 函数值，再求 Nim 和；
  * 对于单个游戏，每个状态的 SG 函数值都是它的所有后继状态的 SG 函数值的 mexmex![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值；
  * 特别地，终止状态（即没有后继状态的状态）的 SG 函数值为 mex⁡∅ =0mex⁡∅=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### Nim 数

所有的公平游戏都唯一对应一个 Nim 数．（有限）Nim 数的集合就是自然数集 𝐍N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，它的代数性质和自然数集不同．具体来说，Nim 数上可以定义 Nim 和 ⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、Nim 乘积 ⊗⊗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两种运算：

Nim 数的运算

对于 Nim 数 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以定义：

  * Nim 和 𝑎 ⊕𝑏 =mex⁡({𝑎′ ⊕𝑏 :𝑎′ <𝑎, 𝑎′ ∈𝐍} ∪{𝑎 ⊕𝑏′ :𝑏′ <𝑏, 𝑏′ ∈𝐍})a⊕b=mex⁡({a′⊕b:a′<a, a′∈N}∪{a⊕b′:b′<b, b′∈N})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * Nim 积 𝑎 ⊗𝑏 =mex⁡({(𝑎′ ⊗𝑏) ⊕(𝑎 ⊗𝑏′) ⊕(𝑎′ ⊗𝑏′) :𝑎′ <𝑎, 𝑏′ <𝑏, 𝑎′,𝑏′ ∈𝐍})a⊗b=mex⁡({(a′⊗b)⊕(a⊗b′)⊕(a′⊗b′):a′<a, b′<b, a′,b′∈N})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

全体 Nim 数在运算 ⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ⊗⊗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下构成一个特征为 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [域](../../algebra/basic/#域)．而且，这些运算以及它们的逆运算，对于前 22𝑛22n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 Nim 数是封闭的；这就得到一系列大小为 22𝑛22n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [有限域](../../algebra/field-theory/#有限域) 𝐅22𝑛F22n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 常见的公平游戏

尽管 Sprague–Grundy 理论完全解决了公平游戏的问题，但是，处理实际的公平游戏时，直接应用 Sprague–Grundy 定理计算效率仍然不高．比如，Nim 游戏中，暴力计算 Sprague–Grundy 值的复杂度是指数级的．因此，往往需要通过打表的方式猜测具体的公平游戏的结论．

本节列举了一些常见的公平游戏及其结论．叙述结论时，本节只给出了必胜和必败状态的判断法则．至于必胜策略，就是进行恰当的操作，使得留给对手的局面恰好为必败状态．由于算法竞赛中经常出现这些游戏的变体，所以，掌握每个游戏的结论的证明过程也很重要．

本节结论的证明方法

本节结论的证明都是验证性的．对于一个游戏，结论中会描述它的先手必败状态和先手必胜状态．证明中，只需要验证从一个先手必败状态出发，只能得到先手必胜状态；而从先手必胜状态出发，总能得到至少一个先手必败状态．要将这些证明改写为严格的证明，需要建立博弈图，然后对博弈图上的状态应用数学归纳法，而这些验证的步骤就是其中的归纳部分．

### Bachet 游戏

相较于单堆 Nim 游戏，Bachet 游戏限制了每次可以取走的石子的数量．

Bachet 游戏

有一堆石子，共计 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚．两名玩家轮流取走至少 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚、至多 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚石子．取走最后一枚石子的玩家获胜．

对此，有如下结论：

定理

游戏先手必败，当且仅当 𝑛 ≡0(mod𝑘 +1)n≡0(modk+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明一

当 𝑛 ≢0(mod𝑘 +1)n≢0(modk+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，只要取走 𝑛mod(𝑘+1) ∈[1,𝑘]nmod(k+1)∈[1,k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚石子，就能保证对手处于必败状态．因此，此时是先手必胜状态．

反过来，当 𝑛 ≡0(mod𝑘 +1)n≡0(modk+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，那么，要么已经没有选择，要么自己取走 𝑘′k′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚石子后，对手紧接着可以取走 𝑘 +1 −𝑘′k+1−k′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚石子，让自己回到必败状态．

证明二

作为 Sprague–Grundy 定理的应用，可以计算 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为只剩下 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚石子时，对应局面的 SG 函数值．

对于 𝑛 ≤𝑘n≤k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以归纳地证明 𝑓(𝑛) =𝑛f(n)=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这与单堆 Nim 游戏相同，因为取走石子数目的限制没有发挥作用．对于 𝑛 >𝑘n>k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，可以证明 𝑓(𝑛) =𝑛mod(𝑘+1)f(n)=nmod(k+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，有

𝑓(𝑛)=mex⁡{𝑓(𝑛−𝑘),𝑓(𝑛−𝑘+1),⋯,𝑓(𝑛−1)}.f(n)=mex⁡{f(n−k),f(n−k+1),⋯,f(n−1)}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这遍历了模 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全体余数，除了 𝑛mod(𝑘+1)nmod(k+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，就有 𝑓(𝑛) =𝑛mod(𝑘+1)f(n)=nmod(k+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### Moore's Nim-k 游戏

相较于 Nim 游戏，Moore's Nim-𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 游戏允许一次性从 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个石子堆中取石子．

Moore's Nim-𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 游戏

共有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆有 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚石子．两名玩家轮流取走至少 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆、至多 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆中的任意多枚石子，但不能不取．取走最后一枚石子的玩家获胜．

对此，有如下结论：

定理

将每一堆石子的数目都表示为二进制数，并对每个数位 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都统计有多少堆石子数目的第 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并计算这个数目对于 (𝑘 +1)(k+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的余数．如果对于每个数位，这个余数都等于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么先手必败；否则，先手必胜．

证明

仿照 Nim 游戏的结论的证明，很容易证明本结论．设 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为余数不为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最高二进制位，且对应的余数为 𝑘′ ≤𝑘k′≤k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，必胜策略为，在石子数目二进制第 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的石子堆中，选择 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆，并选择移走的石子数目恰好使得对手局面中，每个数位的余数都是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．唯一需要说明的是，最后取走石子数量的选择总是可行的．

实际上，只要选定 𝑘′k′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子，每堆都取走 2𝑑2d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚石子，就能使得结果中，第 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位余数变为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于更低的数位的余数，将这些余数随意摊派给某一个堆即可．

### 阶梯 Nim 游戏

阶梯 Nim 游戏稍微复杂一些，它允许石子在相邻的堆之间移动．

阶梯 Nim 游戏

共有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆有 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚石子．两名玩家轮流操作，每次操作中，要么取走第 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子中的任意多枚，要么将第 𝑖 >1i>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子中的任意多枚移动到第 𝑖 −1i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆，但不能不做任何操作．取走最后一枚石子的玩家取胜．

对此，有如下结论：

定理

游戏先手必败，当且仅当奇数堆石子数量的 Nim 和 𝑎1 ⊕𝑎3 ⊕⋯ ⊕𝑎𝑛−1+(𝑛mod2) =0a1⊕a3⊕⋯⊕an−1+(nmod2)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

任何玩家将偶数堆的石子移动到奇数堆时，对手都可以将这些石子继续移动到下一个偶数堆（或移走），因此，这样的移动不会影响奇数堆的局面．此时，每一个奇数堆向下移动到相邻的偶数堆（或移走）都可以看作独立的单堆 Nim 游戏．根据 Sprague–Grundy 定理关于游戏的和的结论，阶梯 Nim 游戏的 SG 函数值，是这些子游戏的 SG 函数值的 Nim 和．这就得到上述结论．

### Fibonacci Nim 游戏

Fibonacci Nim 游戏类似 Bachet 游戏，只有一堆石子，且限制了每次取走的数量．与 Bachet 游戏不同，Fibonacci Nim 游戏中，每次取走的数量的限制是动态的．

Fibonacci Nim 游戏

有一堆石子，共计 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚．两名玩家轮流取石子．第一个行动的玩家不限制取走的石子数目，但是不能取完石子；随后，每次取走的石子数目不得超过上次（指对手回合）取走的石子数目的二倍．每次取走的石子的数目不得为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．取走最后一枚石子的玩家获胜．

对此，有如下结论：

定理

游戏开始时，先手必败，当且仅当石子数目 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 [Fibonacci 数](../../combinatorics/fibonacci/)．

证明

设 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为当前局面可移走石子数量的限额（quota）．那么，第一回合中，𝑞 =𝑛 −1q=n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；而之后的回合中，𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是上次（对手）移走的石子数目的二倍．考察剩余石子数目 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [Fibonacci 编码](../../combinatorics/fibonacci/#斐波那契编码)，也就是将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 唯一地分解为一系列不相邻的、正的 Fibonacci 数的和．需要证明的是，当前状态是必胜状态，当且仅当 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大于等于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的分解中的最小 Fibonacci 数．

必胜策略是：如果可以，移走所有剩余石子；否则，移走分解中最小的 Fibonacci 数．由于分解中，次小的 Fibonacci 数一定严格大于最小的 Fibonacci 数的两倍，所以，只要处于必胜状态的当前回合取不走所有石子，对手在下一回合也取不走次小的 Fibonacci 数（也就是下一回合最小的 Fibonacci 数），对手一定处于必败状态．

反过来，如果当前处于必败状态，那么，设当前取走的数目为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它一定严格小于当前分解中的最小 Fibonacci 数 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．假设下一回合最小的 Fibonacci 数是 𝐹′F′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它一定也是 𝐹 −𝑘F−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的分解中最小的 Fibonacci 数．设 𝐹′ =𝐹″ +𝐹‴F′=F″+F‴![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝐹″ >𝐹‴F″>F‴![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说，𝐹‴,𝐹″,𝐹′F‴,F″,F′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 Fibonacci 数列中相邻三项．如果 𝑘 <𝐹″k<F″![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，利用 Fibonacci 编码计算 𝑘 +(𝐹 −𝑘)k+(F−k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，不需要进位，自然得不到 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，一定有 𝑘 ≥𝐹″k≥F″![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就说明，下一回合的限额 2𝑘 >𝐹″ +𝐹‴ =𝐹′2k>F″+F‴=F′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，是必胜状态．

### Wythoff 游戏

Wythoff 游戏允许同时从多堆石子中移除，但是要求每堆移除相同数量的石子．

Wythoff 游戏

有两堆石子，分别有 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚石子．两名玩家轮流从其中一堆或两堆中取石子，不能不取，但要求从两堆都取石子时，取走的石子数量必须相同．取走最后一枚石子的玩家获胜．

对此，有如下结论：

定理

不妨设 𝑎1 ≤𝑎2a1≤a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，先手必败，当且仅当 𝑎1 =⌊(𝑎2 −𝑎1)𝜙⌋a1=⌊(a2−a1)ϕ⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝜙 =(√5 +1)/2ϕ=(5+1)/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是黄金分割比．

为了证明这一结论，需要用到如下引理：

Beatty 序列

设 𝑟 >1r>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为无理数．它生成的 Beatty 序列是 B𝑟 ={⌊𝑘𝑟⌋ :𝑘 ∈𝐍+}Br={⌊kr⌋:k∈N+}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

Rayleigh 定理

设 𝑟,𝑠 >1r,s>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是两个无理数，且 1𝑟 +1𝑠 =11r+1s=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，序列 B𝑟Br![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 B𝑠Bs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成正整数集 𝐍+N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个分划．此时，它们也称为互补的 Beatty 序列．

证明

设 A𝑟 ={𝑘𝑟 :𝑘 ∈𝐍+}Ar={kr:k∈N+}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．考虑将集合 A =A𝑟 ∪AℓA=Ar∪Aℓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 里的元素排序得到序列 {𝑎𝑖}𝑖∈𝐍+{ai}i∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．需要证明的是，𝑖 =⌊𝑎𝑖⌋i=⌊ai⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对所有 𝑖 ∈𝐍+i∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立，就能得到 B𝑟 ∪B𝑠Br∪Bs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是正整数集 𝐍+N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个分划．

首先，证明序列里没有重复的元素．假设不然，存在 𝑘,ℓ ∈𝐍+k,ℓ∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑘𝑟 =ℓ𝑠kr=ℓs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．那么，有

ℓ𝑘=𝑟𝑠=𝑟−1.ℓk=rs=r−1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

但是，等式左侧是有理数，等式右侧是无理数，矛盾．因此，序列的数字各不相同．

然后，证明集合 AA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中小于等于 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数恰有 ⌊𝑎𝑖⌋⌊ai⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．不妨设 𝑎𝑖 ∈A𝑟ai∈Ar![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑎𝑖 =𝑘𝑟ai=kr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，对集合 A𝑟Ar![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 AℓAℓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素分别计数，就得到小于等于 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正整数恰有

𝑘+⌊𝑘𝑟𝑠⌋=𝑘+⌊𝑘(𝑟−1)⌋=⌊𝑘𝑟⌋=⌊𝑎𝑖⌋k+⌊krs⌋=k+⌊k(r−1)⌋=⌊kr⌋=⌊ai⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

个．进而，由于序列 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是严格递增的，小于等于 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数恰有 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．这就得到 𝑖 =⌊𝑎𝑖⌋i=⌊ai⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由此，可以得到前述结论的证明．

Wythoff 游戏结论的证明

对于所有 𝑎1 <𝑎2a1<a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且先手必败的状态 (𝑎1,𝑎2)(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，令 𝑘 =𝑎2 −𝑎1 ∈𝐍+k=a2−a1∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑎1 =⌊𝑘𝜙⌋a1=⌊kϕ⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎2 =⌊𝑘(𝜙 +1)⌋a2=⌊k(ϕ+1)⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于 𝜙ϕ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是黄金分割比，所以 1𝜙 +1𝜙+1 =11ϕ+1ϕ+1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由 Rayleigh 定理可知，序列 {⌊𝑘𝜙⌋}{⌊kϕ⌋}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ⌊𝑘(𝜙 +1)⌋⌊k(ϕ+1)⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成正整数集 𝐍+N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个分划．这其实说明，所有 𝑎1 <𝑎2a1<a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且先手必败的状态 (𝑎1,𝑎2)(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，分量 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 恰取遍全体正整数一次，且它们的差 𝑎2 −𝑎1a2−a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也恰取遍全体正整数一次．

由于 Wythoff 游戏中，一次合法的操作要么保持分量之一不变，要么保持分量之差不变，所以，从一个先手必败状态开始，确实无法由一次合法的操作中得到另一个先手必败状态．反过来，对于任何先手必胜状态 (𝑎1,𝑎2)(a1,a2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不妨设 𝑎1 ≤𝑎2a1≤a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并令 𝑘 =𝑎2 −𝑎1k=a2−a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果 𝑎1 >⌊𝑘𝜙⌋a1>⌊kϕ⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，先手玩家可以从两堆石子各取 (𝑎1 −⌊𝑘𝜙⌋)(a1−⌊kϕ⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚，将局面变为必败状态．反过来，由前一段的结论，对于这个 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然存在唯一一个必败状态 (𝑎1,𝑎′2)(a1,a2′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．进而，如果 𝑎1 >𝑎′2a1>a2′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，显然有 𝑎′2 <𝑎2a2′<a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；否则，如果 𝑎1 <𝑎′2a1<a2′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，可以取 𝑘′ =𝑎′2 −𝑎1k′=a2′−a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑎1 =⌊𝑘′𝜙⌋a1=⌊k′ϕ⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，又有 𝑎1 <⌊𝑘𝜙⌋a1<⌊kϕ⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故而 𝑘′ <𝑘k′<k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此 𝑎′2 =𝑎1 +𝑘′ <𝑎1 +𝑘 =𝑎2a2′=a1+k′<a1+k=a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，只要 𝑎1 <⌊𝑘𝜙⌋a1<⌊kϕ⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就一定有 𝑎′2 <𝑎2a2′<a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，先手玩家只需要从第二堆石子中取走 (𝑎2 −𝑎′2)(a2−a2′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚石子就可以使得局面变为必败状态．

### 翻硬币游戏

翻硬币游戏也是一类常见的公平组合游戏．

翻硬币游戏

设 (𝑆, ⪯)(S,⪯)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 [良基偏序集](../../order-theory/)，映射 𝑓 :𝑆 →PP𝑆f:S→PPS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足对于所有 𝑠 ∈𝑆s∈S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 集合都有 𝑓(𝑠)f(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 非空，对于 𝑇 ∈𝑓(𝑠)T∈f(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 𝑠 ∈𝑇s∈T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而且对于所有 𝑡 ∈𝑇t∈T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑡 ⪯𝑠t⪯s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的每个元素处都有一枚硬币，可能正面朝上也可能背面朝上．玩家轮流行动，选择一枚正面朝上的硬币 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和集合 𝑇 ∈𝑓(𝑠)T∈f(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并将集合 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有硬币翻转．将所有硬币都翻转到背面朝上的玩家获胜．

翻硬币游戏其实是一大类游戏．取决于具体的偏序集 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和映射 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的选择，翻硬币游戏的具体形式也有所不同．游戏描述中，映射 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要满足的条件是在说，每次玩家选择翻转硬币的集合 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，一定存在一枚正面朝上的硬币 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得集合 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有元素都排在 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 前面．这保证了游戏可以在若干步后终止．

例子

  1. 设 𝑆 ={1,2,⋯,𝑛}S={1,2,⋯,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓(𝑠) ={{𝑡,𝑠} :𝑡 ≤𝑠}f(s)={{t,s}:t≤s}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这相当于说，有一排 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚硬币，每次翻转一枚正面朝上的硬币，并且可以选择一枚它左侧的硬币翻转．
  2. 设 𝑆 ={1,2,⋯,𝑛}S={1,2,⋯,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓(𝑠) ={[𝑡,𝑠] :𝑡 ≤𝑠}f(s)={[t,s]:t≤s}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这相当于说，有一排 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚硬币，每次翻转一段连续的硬币，但是必须保证这些硬币中最右侧的那枚硬币在翻转前是正面朝上的．
  3. 设 𝑆 ={1,2,⋯,𝑛}2S={1,2,⋯,n}2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓(𝑠) ={{𝑠}}f(s)={{s}}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这相当于说，有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列硬币，每次只能翻转一枚正面朝上的硬币．
  4. 设 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一棵有根树的结点集合，且 𝑓(𝑠)f(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是顶点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到树根的路径经过的结点集合的子集中，所有包含 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 自身的子集的集合．这相当于说，有一棵有根树，每个结点处放置一枚硬币，每次翻转一枚正面朝上的硬币，并且可以选择它的若干个祖先结点处的硬币翻转．

尽管翻硬币游戏种类繁多，但是它们的求解思路是一致的．对于翻硬币游戏 (𝑆,𝑓)(S,f)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设 𝐺𝑠Gs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为只有元素 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的硬币正面朝上的局面．这些局面称为基础局面．那么，任意一个局面 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都可以看做是这些基础局面对应的游戏的和．也就是说，以下结论成立：

定理

对于翻硬币游戏 (𝑆,𝑓)(S,f)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和局面 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设其中正面朝上的硬币所处位置的集合为 𝐻(𝐺) ⊆𝑆H(G)⊆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，局面 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 SG 函数值就是

SG⁡(𝐺)=⨁𝑠∈𝐻(𝐺)SG⁡(𝐺𝑠).SG⁡(G)=⨁s∈H(G)SG⁡(Gs).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

考虑一个相关的游戏：一个局面 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的每个元素处都放置有若干枚石子；玩家每次行动时，都可以取走 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的一枚石子，并选取集合 𝑇 ∈𝑓(𝑠)T∈f(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再在集合 𝑇 ∖{𝑠}T∖{s}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的各个元素处均放置一枚石子．对于这类游戏，仍然可以定义基础局面 𝐺′𝑠Gs′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即仅在位置 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处放置有一枚石子的局面．这类游戏中，每个局面均为其所有石子对应基础局面的和．这是因为只要放置新石子时将它对应到取走的石子上，就可以将游戏过程中出现的每枚石子都对应到初始局面中的各个石子上，进而对应初始局面不同石子的子游戏进程互不干扰，整个游戏就可以看作是这些子游戏的和．由于相同位置石子对应基础局面的 SG 值是一样的，所以利用异或值的特性可知，局面 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 SG 值仅由各堆石子数量的奇偶性决定，而与具体数量无关．因此，对于游戏局面 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果记其石子数量为奇数的位置集合为 𝐻(𝐺′)H(G′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，本段的分析可以总结为公式：

SG⁡(𝐺′)=⨁𝑠∈𝐻(𝐺′)SG⁡(𝐺′𝑠).SG⁡(G′)=⨁s∈H(G′)SG⁡(Gs′).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由此，下文只需要建立游戏 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与游戏 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的等价性就可以证明定理中的公式．

需要说明的是，对于新游戏的局面 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与翻硬币游戏的局面 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只要 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中石子数量为奇数的位置与 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中硬币正面朝上的位置处相同，就有 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等价．根据 Sprague–Grundy 定理的引理 2，这等价于证明局面 𝐺 +𝐺′G+G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是必败状态．后手玩家的胜利策略很简单：如果先手玩家选择取走 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的石子且该处不止一枚石子，那么后手玩家直接模仿先手玩家的行为；否则，后手玩家选择和先手玩家同样的 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇 ∈𝑓(𝑠)T∈f(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是选择和先手玩家不同的子游戏，即先手取石子后手就取硬币，先手取硬币后手就翻石子．由于先手玩家无论任何操作，后手玩家就可以继续操作，并保证残余局面中石子数量为奇数的位置与硬币正面朝上的位置相同．这样，游戏必然结束在先手玩家没有合法操作时，因此，先手必败．定理由此得证．

利用这一结论，判断某一局面是否必胜，只需要计算其中所有正面朝上的硬币对应的基础局面的 SG 函数值，再求 Nim 和即可．这些基础局面的 SG 函数值也不难计算，因为它们的后继局面已经由映射 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 给出，且后继局面的 SG 值可以归纳地计算：

SG⁡(𝐺𝑠)=mex𝑇∈𝑓(𝑠)⁡⨁𝑡∈𝑇∖{𝑠}SG⁡(𝐺𝑡).SG⁡(Gs)=mexT∈f(s)⁡⨁t∈T∖{s}SG⁡(Gt).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这相当于提供了一个基础局面 SG 函数值的递推公式．

### 二分图博弈

前置知识：[二分图最大匹配](../../../graph/graph-matching/bigraph-match/)

本节的最后，讨论二分图博弈．尽管这个游戏常称作二分图博弈，但是它的描述和结论的证明都与二分图的结构无关，所以，它的结论实际上对于一般的无向图都成立．但是，一般图的最大匹配较为复杂，所以这一结论常出现在二分图的题目中．

二分图博弈

两个玩家轮流行动．每个玩家面临的局面都由一个无向图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和它的一个顶点 𝑣 ∈𝑉v∈V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成．在一名玩家的回合中，若当前局面为 (𝐺,𝑣)(G,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则该玩家必须选择一个与 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相邻的顶点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．随后，将顶点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 及其所有关联边从图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中删除，得到残余图 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．新的局面即为 (𝐺′,𝑢)(G′,u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，交由下一位玩家．若某位玩家在其回合开始时，当前顶点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在图中没有相邻顶点（即不存在合法选择），则该玩家无法行动，并因此输掉游戏．

对此，有如下结论：

定理

游戏先手必胜，当且仅当顶点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大匹配关键点，也就是说，在图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有最大匹配中，顶点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是匹配点．

证明

首先，顶点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大匹配关键点．设 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个最大匹配为 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时，先手可以将局面移动到在 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中与顶点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 匹配的顶点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于顶点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出现在所有图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大匹配中，所以，残余图 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大匹配的大小至多是 |𝑀| −1|M|−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；而且将 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 去掉边 (𝑣,𝑣)(v,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就能得到图 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个大小为 |𝑀| −1|M|−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的匹配 𝑀′M′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：结合这两点就知道，𝑀′M′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是图 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个最大匹配．但是，后手玩家所处的局面中，顶点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并不是匹配 𝑀′M′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个匹配点．因此，后手玩家必然处于一个必败状态．

反过来，假设存在最大匹配 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是未匹配点．由于 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是最大匹配，与顶点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相邻的顶点一定是匹配点；否则，就可以将它们之间的连边添加到 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，得到一个更大的匹配．因此，无论先手怎么选择，后手都处于一个必胜状态．

求出二分图最大匹配关键点的算法详见 [二分图最大匹配页面](../../../graph/graph-matching/bigraph-match/#最大匹配关键点)．

另外，二分图博弈还有一个变体：

二分图博弈的变体

设 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个无向图，且图的每个顶点上都放置了一枚石子．两名玩家轮流行动取走石子．游戏开始时，先手玩家可以取走任何一枚石子；后续的回合中，每名玩家取走石子的顶点必须与上一回合中对方取走石子的顶点相邻．最先无法取走石子的玩家输掉游戏．

显然，这个变体相当于在前文所述二分图博弈中，让先手玩家选择初始局面，然后从后手玩家开始二分图博弈．因此，这个变体中，先手玩家必败，当且仅当每个顶点都是最大匹配关键点，亦即图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在 [完美匹配](../../../graph/graph-matching/graph-match/#定义)．

## 反常 Nim 游戏

本节讨论反常 Nim 游戏的求解．

Nim 游戏

共有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆有 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚石子．两名玩家轮流取走任意一堆中的任意多枚石子，但不能不取．取走最后一枚石子的玩家失败．

对此，有如下结论：

定理

反常 Nim 游戏中，状态 (𝑎1,𝑎2,⋯,𝑎𝑛)(a1,a2,⋯,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是必败状态 PP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当

  1. 存在 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑎𝑖 >1ai>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 Nim 和 𝑎1 ⊕𝑎2 ⊕⋯ ⊕𝑎𝑛 =0a1⊕a2⊕⋯⊕an=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，或者
  2. 对于所有 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 𝑎𝑖 ≤1ai≤1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且剩余的非空石子堆数是奇数．

证明

由于无法操作是先手必胜态 NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，可以归纳地证明，如果每堆石子都只有一枚，那么石子堆数是奇数就对应着先手必败态 NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，石子堆数是偶数就对应着先手必胜态 NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

接下来，考察有些堆石子的数量严格大于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况．

情形 A：如果只有一堆石子的数量严格大于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，此时 Nim 和一定不为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而且，由于先手玩家可以选择转移到全部堆的石子数量均不超过 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的局面，而且可以控制剩余的非空石子堆的奇偶性．因此，此时为先手必胜态 NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

情形 B：现在，有不止一堆石子的数量严格大于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，无论怎么操作，下一个局面中，都至少有一堆石子的数量严格大于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据归纳假设，下一局面中，先手必败对应着 Nim 和为零，先手必胜对应着 Nim 和不为零．这与正常 Nim 游戏的归纳假设完全相同．因此，重复 Nim 游戏的论证，就能知道，当前局面同样符合 Nim 和为零对应先手必败状态的结论．

## 有向图游戏

本文讨论的公平组合游戏，要求同一局面不能出现两次，也不存在平局的可能性．因此，对应的博弈图总是有向无环图．本节放宽了这一限制，讨论如何在一般的有向图上判定各个状态是先手必胜、先手必败或平局．

有向图游戏的规则和其他的公平组合游戏大体一致：从起始状态出发，轮流沿着有向图的边移动一步，直到无路可走．根据游戏是正常规则还是反常规则，最后一个不能移动的玩家分别是败者和胜者．在这样的游戏里，每个状态的胜负情况共有三种可能性：先手必胜、先手必败、平局．平局中游戏永远不会终止．尽管稍微复杂一些，但是关于必败状态和必胜状态的 引理 依然成立，而剩下的状态就是平局状态：

  * 一个状态有后继状态先手必胜，当且仅当后继状态之一是必败状态；
  * 如果一个状态有后继状态，那么它先手必败，当且仅当所有后继状态都是必胜状态；
  * 如果一个状态无法分类为必胜状态和必败状态，那么它就是平局状态．

要将所有状态分类为这三种状态，只需要采用类似 [拓扑排序](../../../graph/topo/) 的思路：

  1. 初始化时，记录所有状态的出度，将所有出度为零的状态压入队列，并根据游戏是正常规则或是反常规则分别设为必败状态或必胜状态．
  2. 弹出队首状态．如果是必败状态，则设前驱状态为必胜状态；否则，当前状态是必胜状态，将它的所有前驱状态的出度减一，并将出度为零的前驱状态设为必败状态．将可以判断是必胜或必败状态的前驱状态压入队列．
  3. 算法在队列为空时终止．尚未判断为必胜或必败状态的状态均为平局状态．

这一算法可以在 𝑂(|𝑉| +|𝐸|)O(|V|+|E|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内将所有状态分类．

## 例题

本节讨论一些典型的例题．

[Luogu P2148 [SDOI2009] E&D](https://www.luogu.com.cn/problem/P2148)

有 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子．对于 𝑘 =1,2,⋯,𝑛k=1,2,⋯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，石子堆 2𝑘 −12k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 2𝑘2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分为一组．两名玩家轮流操作，每次选择一组石子堆，将其中一堆移走，并将另一堆分为非空的两堆，放到该组石子堆所在的两个位置．如果所有石子堆都只有一枚石子，当前玩家就没有合法操作，输掉游戏．给定每堆石子的数量 {𝑎𝑖}2𝑛𝑖=1{ai}i=12n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，问是否为先手必胜状态．

解答

显然，不同组石子堆的游戏相互独立，所以，只要计算每组游戏的 SG 函数值，就能计算出整个游戏的 SG 值，进而判断是否为必胜状态．关键在于如何计算每组石子堆的 SG 函数值．这并不容易．解决这类博弈论问题的常见思路是打表．设一组石子堆中石子数量分别为 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，SG 值为 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，写一个暴力打表的程序，就得到如下结果：

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text 0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 4 1 1 2 2 1 1 3 3 1 1 2 2 1 1 4 4 0 2 0 2 0 3 0 3 0 2 0 2 0 4 0 4 2 2 2 2 3 3 3 3 2 2 2 2 4 4 4 4 0 1 0 3 0 1 0 3 0 1 0 4 0 1 0 4 1 1 3 3 1 1 3 3 1 1 4 4 1 1 4 4 0 3 0 3 0 3 0 3 0 4 0 4 0 4 0 4 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 0 1 0 2 0 1 0 4 0 1 0 2 0 1 0 4 1 1 2 2 1 1 4 4 1 1 2 2 1 1 4 4 0 2 0 2 0 4 0 4 0 2 0 2 0 4 0 4 2 2 2 2 4 4 4 4 2 2 2 2 4 4 4 4 0 1 0 4 0 1 0 4 0 1 0 4 0 1 0 4 1 1 4 4 1 1 4 4 1 1 4 4 1 1 4 4 0 4 0 4 0 4 0 4 0 4 0 4 0 4 0 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 ```   
---|---  
  
这个表很具有规律性．有一个简单的观察：表格分成若干个 2 ×22×2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵，且左上角处总是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而其余三个值总是一样的．于是，不妨将这个表格压缩，将每个 2 ×22×2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵都压缩为除了左上角之外那个共同的数值：

```text 1 2 3 4 5 6 7 8 ``` |  ```text 1 2 1 3 1 2 1 4 2 2 3 3 2 2 4 4 1 3 1 3 1 4 1 4 3 3 3 3 4 4 4 4 1 2 1 4 1 2 1 4 2 2 4 4 2 2 4 4 1 4 1 4 1 4 1 4 4 4 4 4 4 4 4 4 ```   
---|---  
  
可以发现，这个压缩的表格是前面完整表格相同位置的值加一．其实问题已经解决了．设下标从 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始，那么表格中 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的值 𝑔(𝑖,𝑗)g(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以由如下递推公式给出：

𝑔(𝑖,𝑗)={0,if 2∣𝑖 and 2∣𝑗,𝑔(⌊𝑖/2⌋,⌊𝑗/2⌋)+1,otherwise.g(i,j)={0,if 2∣i and 2∣j,g(⌊i/2⌋,⌊j/2⌋)+1,otherwise.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

要求的 SG 函数 𝑓(𝑖,𝑗) =𝑔(𝑖 −1,𝑗 −1)f(i,j)=g(i−1,j−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．利用这一递推公式，算法可以在 𝑂(log⁡min{𝑖,𝑗})O(log⁡min{i,j})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内求出 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值．

当然，可以通过简单的归纳法得到 𝑔(𝑖,𝑗)g(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 其实就是将 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 反复同时除以 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到两个偶数的最少次数．换句话说，它就是 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的按位或中末尾 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数．由此，也可以直接利用 `__builtin_ctz(~(i | j))` 算出该值．

这类题目中，只要通过打表观察的方法得到 SG 函数表达式，它都很容易通过归纳法证明，因而解题的关键在于以某种形式获得这些结论而非推导．例如，已知结论后，本题中的递推关系可以归纳证明如下．设 𝑆𝑘Sk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为将 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚石子分成非空的两堆能得到的局面的 SG 值集合，那么，𝑓(𝑖,𝑗) =mex⁡(𝑆𝑖 ∪𝑆𝑗)f(i,j)=mex⁡(Si∪Sj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．故而，𝑆𝑘Sk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有递推关系：

𝑆𝑘={mex⁡(𝑆𝑖∪𝑆𝑗):𝑖+𝑗=𝑘, 𝑖,𝑗∈𝐍+}.Sk={mex⁡(Si∪Sj):i+j=k, i,j∈N+}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

需要证明的是，𝑑 ∈𝑆𝑘d∈Sk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当 (𝑘 −1)(k−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制表示中第 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位（最低位是第 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位）是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

利用数学归纳法．归纳起点 𝑆1 =∅S1=∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 显然成立．假设命题对小于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正整数都成立．那么，𝑑 ∈𝑆𝑘d∈Sk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当存在 𝑖,𝑗 ∈𝐍+i,j∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑖 +𝑗 =𝑘i+j=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 (𝑖 −1)(i−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑗 −1)(j−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两个数的第 𝑑′ <𝑑d′<d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位至少有一个为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且第 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位均为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．显然，存在这样一种拆分，当且仅当只考虑第 0 ∼𝑑0∼d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的部分，即模 2𝑑+12d+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，(𝑘 −1) =(𝑖 −1) +(𝑗 −1) +1(k−1)=(i−1)+(j−1)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值范围为 [2𝑑,2𝑑+1 −1)[2d,2d+1−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间．这一条件就等价于 (𝑘 −1)(k−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由此，归纳步骤成立．原命题得证．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` |  ```text #include <iostream> #include <vector> int g ( int i , int j ) { return i % 2 == 0 && j % 2 == 0 ? 0 : g ( i / 2 , j / 2 ) \+ 1 ; } int f ( int i , int j ) { return g ( i \- 1 , j \- 1 ); } int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { int n ; std :: cin >> n ; int v = 0 ; for ( int i = 0 ; i < n / 2 ; ++ i ) { int x , y ; std :: cin >> x >> y ; v ^= f ( x , y ); } std :: cout << ( v ? "YES" : "NO" ) << '\n' ; } return 0 ; } ```   
---|---  
  
[Luogu P5675 [GZOI2017] 取石子游戏](https://www.luogu.com.cn/problem/P5675)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆有 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚．两人玩 Nim 游戏．现在，可以任意指定若干堆石子作为初始局面，并指定其中一堆石子要求先手玩家首轮必须从中取走石子，但不能指定取走石子的数目．问有多少种指定方式，使得先手无法获得胜利．数据满足 𝑛,𝑎𝑖 ≤200n,ai≤200![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解答

对于这类问题，需要利用常见游戏的结论，并结合其他部分知识来进行解答．假设指定先手必须取走第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子，且指定的所有石子堆数量 Nim 和为 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，先手无法获得胜利，当且仅当 𝑎𝑖 ≤𝑎𝑖 ⊕𝑣ai≤ai⊕v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子数量 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不超过除第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆外剩余石子堆数量 Nim 和 𝑎𝑖 ⊕𝑣ai⊕v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于数据范围很小，直接枚举指定首轮取石子的堆；枚举到第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆时，剩余每个堆选或不选，可以得到不同 Nim 和的方案数可以通过 DP 计算出来，将最后得到的方案数中大于等于 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的部分加总起来即可．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``` |  ```text #include <array> #include <iostream> #include <vector> int main () { constexpr int M = 1e9 \+ 7 ; constexpr int L = 256 ; int n ; std :: cin >> n ; std :: vector < int > a ( n ); for ( auto & x : a ) std :: cin >> x ; int res = 0 ; for ( int i = 0 ; i < n ; ++ i ) { std :: array < int , L > dp = {}; dp [ 0 ] = 1 ; for ( int j = 0 ; j < n ; ++ j ) { if ( j == i ) continue ; std :: array < int , L > _dp = {}; for ( int v = 0 ; v < L ; ++ v ) { _dp [ v ] = ( dp [ v ] \+ dp [ v ^ a [ j ]]) % M ; } dp = std :: move ( _dp ); } for ( int v = a [ i ]; v < L ; ++ v ) { res = ( res \+ dp [ v ]) % M ; } } std :: cout << res << std :: endl ; return 0 ; } ```   
---|---  
  
[Luogu P2599 [ZJOI2009] 取石子游戏](https://www.luogu.com.cn/problem/P2599)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆有 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚．两人轮流取走石子，每次都只能从最左或最右的两堆中选择一堆取走任意枚石子，但不能不取．取走最后一枚石子的玩家胜利．问先手是否必胜．

解答

由于本题中并不存在相互独立的子游戏，所有这道题目原则上只用到 判断必败和必胜状态的引理．从最简单的情形开始分析．当 𝑛 ≤2n≤2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，就是 Nim 游戏．当 𝑛 ≥3n≥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，问题变得复杂．但是，由于可操作的石子堆只能是两端的石子堆，不妨设它们中石子数量分别为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．进一步地，设 𝑓(𝑥,𝑦)f(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为先手必胜状态的指示函数，即先手必胜时 𝑓(𝑥,𝑦) =1f(x,y)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，否则 𝑓(𝑥,𝑦) =0f(x,y)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．容易发现，𝑓(𝑥,𝑦)f(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值满足递推关系：𝑓(𝑥,𝑦) =0f(x,y)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当对于所有 𝑠 <𝑥s<x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑡 <𝑦t<y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 𝑓(𝑥,𝑡) =𝑓(𝑠,𝑦) =1f(x,t)=f(s,y)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．递推起点在 𝑥 =0x=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑦 =0y=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，此时，游戏已经不足 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子，需要进一步考虑中间石子堆的数量．因此，不妨暂时假设 𝑓(𝑥,0)f(x,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓(0,𝑦)f(0,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是已知的，考虑如何从它们的取值推出所有 𝑓(𝑥,𝑦)f(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值．这并不困难．考虑下标集合为 𝐍 ×𝐍N×N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的无穷大矩阵，求 𝑓(𝑥,𝑦)f(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相当于向里面填 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，需要满足的条件是，每行和每列都至多一个 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且如果同行或同列中之前的位置都没有出现过 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，该位置一定是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．每行中 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置实际上定义了一个从行号 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到列号 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的函数．简单尝试几个例子（即打表）之后就可以发现，如果设使得 𝑓(𝑥,0) =0f(x,0)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的唯一的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑓(0,𝑦) =0f(0,y)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的唯一的 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑦0y0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，对于任何 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑓(𝑥,𝑦) =0f(x,y)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立的

𝑦=⎧{ { {⎨{ { {⎩0,𝑥=𝑥0,𝑥−1,𝑥0<𝑥<𝑦0,𝑥+1,𝑦0<𝑥<𝑥0,𝑥,otherwise.y={0,x=x0,x−1,x0<x<y0,x+1,y0<x<x0,x,otherwise.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，只要知道 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦0y0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以在 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内计算出任意 𝑓(𝑥,𝑦)f(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，判断当前状态是否为先手必胜状态．而 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦0y0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以递归计算．例如，𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是使得 𝑓(𝑥,0) =0f(x,0)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的唯一解，但同时，𝑓(𝑥,0)f(x,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值可以通过移除最右侧石子堆后，只考虑剩下的 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子来计算；也就是说，只考虑前 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆石子，同样可以计算一个 𝑓1,𝑛−1(𝑥,𝑦)f1,n−1(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，显然有 𝑓(𝑥,0) =𝑓1,𝑛−1(𝑥,𝑎𝑛−1)f(x,0)=f1,n−1(x,an−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；类似地，移除最左侧石子堆并计算得出 𝑓2,𝑛(𝑥,𝑦)f2,n(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，就得到 𝑓(0,𝑦) =𝑓2,𝑛(𝑎1,𝑦)f(0,y)=f2,n(a1,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．当然，内层的函数 𝑓1,𝑛−1(𝑥,𝑦)f1,n−1(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓2,𝑛(𝑥,𝑦)f2,n(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算依赖于更内层的函数．这是典型的 [区间 DP](../../../dp/interval/)．每层只需要维护相应函数的 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦0y0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 ``` |  ```text #include <array> #include <iostream> #include <vector> int main () { // Transition helper as explained above. auto calc = []( int x0 , int y0 , int x ) -> int { return x == x0 ? 0 : (( x < x0 && x < y0 ) || ( x > x0 && x > y0 ) ? x : ( x0 < y0 ? x \- 1 : x \+ 1 )); }; int t ; std :: cin >> t ; for (; t ; \-- t ) { int n ; std :: cin >> n ; std :: vector < int > a ( n ); for ( auto & x : a ) std :: cin >> x ; // dp[i][j][0] = the unique value x such that // f_{i-1,j}(x, a_j) = 0 // i.e. the interval game [i, j] is in a P-position // when a pile of size x is attached to the LEFT. // // dp[i][j][1] = the unique value y such that // f_{i,j+1}(a_i, y) = 0 // i.e. the interval game [i, j] is in a P-position // when a pile of size y is attached to the RIGHT. std :: vector < std :: vector < std :: array < int , 2 >>> dp ( n , std :: vector < std :: array < int , 2 >> ( n )); // Base case: single-element interval [i, i]. // The "left" and "right" pile values both equal a[i]. for ( int i = 0 ; i < n ; ++ i ) dp [ i ][ i ][ 0 ] = dp [ i ][ i ][ 1 ] = a [ i ]; // Build up intervals of increasing length d. for ( int d = 1 ; d < n ; ++ d ) { for ( int i = 0 ; i \+ d < n ; ++ i ) { dp [ i ][ i \+ d ][ 0 ] = calc ( dp [ i ][ i \+ d \- 1 ][ 1 ], dp [ i ][ i \+ d \- 1 ][ 0 ], a [ i \+ d ]); dp [ i ][ i \+ d ][ 1 ] = calc ( dp [ i \+ 1 ][ i \+ d ][ 0 ], dp [ i \+ 1 ][ i \+ d ][ 1 ], a [ i ]); } } // The original game corresponds to attaching nothing on the left. // It is a P-position if and only if the unique value y satisfying // f_{-1, n-1}(0, y) = 0 // is y = 0. std :: cout << ( dp [ 0 ][ n \- 1 ][ 0 ] != 0 ) << '\n' ; } return 0 ; } ```   
---|---  
  
## 习题

首先是一些模板题．它们是对本页面的结论的简单应用：

  * [Luogu P2197【模板】Nim 游戏](https://www.luogu.com.cn/problem/P2197)
  * [Luogu P2252 [SHOI2002] 取石子游戏](https://www.luogu.com.cn/problem/P2252)
  * [Luogu P2594 [ZJOI2009] 染色游戏](https://www.luogu.com.cn/problem/P2594)
  * [Luogu P3185 [HNOI2007] 分裂游戏](https://www.luogu.com.cn/problem/P3185)
  * [Luogu P3480 [POI 2009] KAM-Pebbles](https://www.luogu.com.cn/problem/P3480)
  * [Luogu P4101 [HEOI2014] 人人尽说江南好](https://www.luogu.com.cn/problem/P4101)
  * [Luogu P4279 [SHOI2008] 小约翰的游戏](https://www.luogu.com.cn/problem/P4279)
  * [Luogu P6487 [COCI 2010/2011 #4] HRPA](https://www.luogu.com.cn/problem/P6487)
  * [Luogu P6560 [SBCOI2020] 时光的流逝](https://www.luogu.com.cn/problem/P6560)
  * [Luogu P7589 黑白棋（2021 CoE-II B）](https://www.luogu.com.cn/problem/P7589)
  * [AtCoder Regular Contest 168 B - Arbitrary Nim](https://atcoder.jp/contests/arc168/tasks/arc168_b)

然后是一些思维性更强或更为综合的题目：

  * [Luogu P2490 [SDOI2011] 黑白棋](https://www.luogu.com.cn/problem/P2490)
  * [Luogu P3179 [HAOI2015] 数组游戏](https://www.luogu.com.cn/problem/P3179)
  * [Luogu P5363 [SDOI2019] 移动金币](https://www.luogu.com.cn/problem/P5363)
  * [Luogu P5970 [POI 2016] Nim z utrudnieniem](https://www.luogu.com.cn/problem/P5970)
  * [Luogu P6791 [SNOI2020] 取石子](https://www.luogu.com.cn/problem/P6791)
  * [Luogu P7864「EVOI-RD1」摘叶子](https://www.luogu.com.cn/problem/P7864)
  * [Luogu P8347「Wdoi-6」另一侧的月](https://www.luogu.com.cn/problem/P8347)
  * [AtCoder Grand Contest 002 E - Candy Piles](https://atcoder.jp/contests/agc002/tasks/agc002_e)
  * [AtCoder Grand Contest 010 F - Tree Game](https://atcoder.jp/contests/agc010/tasks/agc010_f)
  * [AtCoder Grand Contest 017 D - Game on Tree](https://atcoder.jp/contests/agc017/tasks/agc017_d)
  * [AtCoder Beginner Contest 278 G - Generalized Subtraction Game](https://atcoder.jp/contests/abc278/tasks/abc278_g)
  * [SPOJ COT3 - Combat on a tree](https://www.spoj.com/problems/COT3/)
  * [Codeforces 494 E. Sharti](https://codeforces.com/problemset/problem/494/E)
  * [Codeforces 1149 E. Election Promises](https://www.luogu.com.cn/problem/CF1149E)
  * [Codeforces 1451 F. Nullify The Matrix](https://codeforces.com/problemset/problem/1451/F)
  * [Codeforces 1704 F. Colouring Game](https://codeforces.com/problemset/problem/1704/F)

最后是一些二分图博弈的题目．由于需要用到一些二分图匹配的算法，故将它们单独列出：

  * [Luogu P4136 谁能赢呢？](https://www.luogu.com.cn/problem/P4136)
  * [Luogu P4617 [COCI 2017/2018 #5] Planinarenje](https://www.luogu.com.cn/problem/P4617)
  * [Luogu P4055 [JSOI2009] 游戏](https://www.luogu.com.cn/problem/P4055)
  * [Luogu P1971 [NOI2011] 兔兔与蛋蛋游戏](https://www.luogu.com.cn/problem/P1971)
  * [Codeforces 1147 F. Zigzag Game](https://codeforces.com/problemset/problem/1147/F)

## 参考资料与注释

  * [（转载）Nim 游戏博弈（收集完全版）by exponent - 博客园](http://www.cnblogs.com/exponent/articles/2141477.html)
  * [[组合游戏与博弈论]【学习笔记】by Candy? - 博客园](https://www.cnblogs.com/candy99/p/6548836.html)
  * [Nim - Wikipedia](https://en.wikipedia.org/wiki/Nim)
  * [Sprague–Grundy theorem - Wikipedia](https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem)
  * [Nimber - Wikipedia](https://en.wikipedia.org/wiki/Nimber)
  * [Beatty Sequence - Wikipedia](https://en.wikipedia.org/wiki/Beatty_sequence)
  * [Games on arbitrary graphs - CP Algorithms](https://cp-algorithms.com/game_theory/games_on_graphs.html)
  * [算法学习笔记（74): 二分图博弈 by Pecco - 知乎](https://zhuanlan.zhihu.com/p/359334008)
  * Conway, John H. On numbers and games. AK Peters/CRC Press, 2000.
  * Berlekamp, Elwyn R., John H. Conway, and Richard K. Guy. Winning ways for your mathematical plays, volume 1-4. AK Peters/CRC Press, 2001-2004.

* * *

  1. 「NN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 态」和「PP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 态」这两个名称分别表示「下一名玩家胜利」（Next player wins）和「前一名玩家胜利」（Previous player wins）． ↩

  2. 本文讨论的「和」都是 **长规则** （long rule）下的 **析取和** （disjunctive sum）．这也是最常见的一种游戏组合方式．除此之外，还有其他可能的游戏组合方式．关于它们的详细讨论，可以参考 Conway, John H. On numbers and games. AK Peters/CRC Press, 2000. 一书的第 14 章． ↩

* * *

>  __本页面最近更新： 2026/1/27 12:26:08，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/game-theory/impartial-game.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/game-theory/impartial-game.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [countercurrent-time](https://github.com/countercurrent-time), [H-J-Granger](https://github.com/H-J-Granger), [NachtgeistW](https://github.com/NachtgeistW), [Backl1ght](https://github.com/Backl1ght), [CCXXXI](https://github.com/CCXXXI), [MegaOwIer](https://github.com/MegaOwIer), [ouuan](https://github.com/ouuan), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [woruo27](https://github.com/woruo27), [AngelKitty](https://github.com/AngelKitty), [chu-yuehan](https://github.com/chu-yuehan), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [Marcythm](https://github.com/Marcythm), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [tinjyu](https://github.com/tinjyu), [weiyong1024](https://github.com/weiyong1024), [2008verser](https://github.com/2008verser), [billchenchina](https://github.com/billchenchina), [ChungZH](https://github.com/ChungZH), [cutekibry](mailto:cutekibry@yahoo.com), [cutekibry](https://github.com/cutekibry), [FFjet](https://github.com/FFjet), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [hhc0001](https://github.com/hhc0001), [isdanni](https://github.com/isdanni), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Molmin](https://github.com/Molmin), [orzAtalod](https://github.com/orzAtalod), [Peanut-Tang](https://github.com/Peanut-Tang), [SaMiiKaaaa](https://github.com/SaMiiKaaaa), [ShizuhaAki](https://github.com/ShizuhaAki), [SukkaW](https://github.com/SukkaW), [TOMWT-qwq](https://github.com/TOMWT-qwq)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
