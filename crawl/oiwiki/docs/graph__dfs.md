# DFS（图论） - OI Wiki

- Source: https://oi-wiki.org/graph/dfs/

# DFS（图论）

## 引入

DFS 全称是 [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search)，中文名是深度优先搜索，是一种用于遍历或搜索树或图的算法．所谓深度优先，就是说每次都尝试向更深的节点走．

该算法讲解时常常与 BFS 并列，但两者除了都能遍历图的连通块以外，用途完全不同，很少有能混用两种算法的情况．

DFS 常常用来指代用递归函数实现的搜索，但实际上两者并不一样．有关该类搜索思想请参阅 [DFS（搜索）](../../search/dfs/).

## 过程

DFS 最显著的特征在于其 **递归调用自身** ．同时与 BFS 类似，DFS 会对其访问过的点打上访问标记，在遍历图时跳过已打过标记的点，以确保 **每个点仅访问一次** ．符合以上两条规则的函数，便是广义上的 DFS．

具体地说，DFS 大致结构如下：

```text 1 2 3 4 5 6 7 8 ``` |  ```text DFS(v) // v 可以是图中的一个顶点，也可以是抽象的概念，如 dp 状态等． 在 v 上打访问标记 for u in v 的相邻节点 if u 没有打过访问标记 then DFS(u) end end end ```   
---|---  
  
以上代码只包含了 DFS 必需的主要结构．实际的 DFS 会在以上代码基础上加入一些代码，利用 DFS 性质进行其他操作．

## 性质

该算法通常的时间复杂度为 𝑂(𝑛 +𝑚)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，空间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示点数，𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示边数．注意空间复杂度包含了栈空间，栈空间的空间复杂度是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．在平均 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍历一条边的条件下才能达到此时间复杂度，例如用前向星或邻接表存储图；如果用邻接矩阵则不一定能达到此复杂度．

> 备注：目前大部分算法竞赛（包括 NOIP、大部分省选以及 CCF 举办的各项赛事）都支持 **无限栈空间** ，即：栈空间不单独限制，但总内存空间仍然受题面限制．但大部分操作系统会对栈空间做额外的限制，因此在本地调试时需要一些方式来取消栈空间限制．
> 
>   * 在 Windows 上，通常的方法是在 **编译选项** 中加入 `-Wl,--stack=1000000000`，表示将栈空间限制设置为 1000000000 字节．
>   * 在 Linux 上，通常的方法是在运行程序前 **在终端内** 执行 `ulimit -s unlimited`，表示栈空间无限．每个终端只需执行一次，对之后每次程序运行都有效．
> 

## 实现

### 栈实现

DFS 可以使用 [栈（Stack）](../../ds/stack/) 为遍历中节点的暂存容器来实现；这与用 [队列（Queue）](../../ds/queue/) 实现的 BFS 形成高度对应．

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` |  ```text vector < vector < int >> adj ; // 邻接表 vector < bool > vis ; // 记录节点是否已经遍历 void dfs ( int s ) { stack < int > st ; st . push ( s ); vis [ s ] = true ; while ( ! st . empty ()) { int u = st . top (); st . pop (); for ( int v : adj [ u ]) { if ( ! vis [ v ]) { vis [ v ] = true ; // 确保栈里没有重复元素 st . push ( v ); } } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text # adj : List[List[int]] 邻接表 # vis : List[bool] 记录节点是否已经遍历 def dfs ( s : int ) -> None : stack = [ s ] # 用列表来模拟栈，把起点加入栈中 vis [ s ] = True # 起点被遍历 while stack : # 当栈非空时继续执行 u = ( stack . pop () ) # 拿取并丢弃掉最后一个元素（栈顶的元素），可以理解为走到u这个元素 for v in adj [ u ]: # 对于与u相邻的每个元素v if not vis [ v ]: # 如果v在此前没有走过 vis [ v ] = True # 确保栈里没有重复元素 stack . append ( v ) # 把v加入栈中 ```   
---|---  
  
### 递归实现

函数在递归调用时的求值如同对栈的添加和删除元素的顺序，故函数调用所占据的虚拟地址被称为函数调用栈（Call Stack），DFS 可用递归的方式实现．

以 [邻接表（Adjacency List）](../save/#邻接表) 作为图的存储方式：

C++Python

```text 1 2 3 4 5 6 7 8 ``` |  ```text vector < vector < int >> adj ; // 邻接表 vector < bool > vis ; // 记录节点是否已经遍历 void dfs ( const int u ) { vis [ u ] = true ; for ( int v : adj [ u ]) if ( ! vis [ v ]) dfs ( v ) } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 ``` |  ```text # adj : List[List[int]] 邻接表 # vis : List[bool] 记录节点是否已经遍历 def dfs ( u : int ) -> None : vis [ u ] = True for v in adj [ u ]: if not vis [ v ]: dfs ( v ) ```   
---|---  
  
以 [链式前向星](../save/#链式前向星) 为例：

C++JavaPython

```text 1 2 3 4 5 6 7 8 ``` |  ```text void dfs ( int u ) { vis [ u ] = 1 ; for ( int i = head [ u ]; i ; i = e [ i ]. x ) { if ( ! vis [ e [ i ]. t ]) { dfs ( v ); } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text public void dfs ( int u ) { vis [ u ] = true ; for ( int i = head [ u ] ; i != 0 ; i = e [ i ] . x ) { if ( ! vis [ e [ i ] . t ] ) { dfs ( v ); } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text def dfs ( u ): vis [ u ] = True i = head [ u ] while i : if vis [ e [ i ] . t ] == False : dfs ( v ) i = e [ i ] . x ```   
---|---  
  
### DFS 序列

DFS 序列是指 DFS 调用过程中访问的节点编号的序列．

我们发现，每个子树都对应 DFS 序列中的连续一段（一段区间）．

### 括号序列

DFS 进入某个节点的时候记录一个左括号 `(`，退出某个节点的时候记录一个右括号 `)`．

每个节点会出现两次．相邻两个节点的深度相差 1．

### 一般图上 DFS

对于非连通图，只能访问到起点所在的连通分量．

对于连通图，DFS 序列通常不唯一．

注：树的 DFS 序列也是不唯一的．

在 DFS 过程中，通过记录每个节点从哪个点访问而来，可以建立一个树结构，称为 DFS 树．DFS 树是原图的一个生成树．

[DFS 树](../scc/#dfs-生成树) 有很多性质，比如可以用来求 [强连通分量](../scc/)．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/dfs.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/dfs.md "edit.link.title")  
>  __本页面贡献者：[Enter-tainer](https://github.com/Enter-tainer), [ouuan](https://github.com/ouuan), [Tiphereth-A](https://github.com/Tiphereth-A), [Craneplayz](https://github.com/Craneplayz), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [shenshuaijie](https://github.com/shenshuaijie), [sshwy](https://github.com/sshwy), [vincent-163](https://github.com/vincent-163), [Acfboy](https://github.com/Acfboy), [billchenchina](https://github.com/billchenchina), [ChungZH](https://github.com/ChungZH), [greyqz](https://github.com/greyqz), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [HeRaNO](https://github.com/HeRaNO), [ksyx](https://github.com/ksyx), [LLLgoyour](https://github.com/LLLgoyour), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [partychicken](https://github.com/partychicken), [qq1010903229](https://github.com/qq1010903229), [shawlleyw](https://github.com/shawlleyw), [StudyingFather](https://github.com/StudyingFather), [Xeonacid](https://github.com/Xeonacid), [yjl9903](https://github.com/yjl9903), [zychen20](https://github.com/zychen20)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
