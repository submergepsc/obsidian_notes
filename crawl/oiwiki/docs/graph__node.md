# 拆点 - OI Wiki

- Source: https://oi-wiki.org/graph/node/

# 拆点

拆点是一种图论建模思想，常用于 [网络流](../flow/)，用来处理 **点权或者点的流量限制** 的问题，也常用于 **分层图** ．

## 结点有流量限制的最大流

如果把结点转化成边，那么这个问题就可以套板子解决了．

我们考虑把有流量限制的结点转化成这样一种形式：由两个结点 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和一条边 ⟨𝑢,𝑣⟩⟨u,v⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组成的部分．其中，结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 承接所有从原图上其他点的出发到原图上该点的边，结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 引出所有从原图上该点出发到达原图上其他点的边．边 ⟨𝑢,𝑣⟩⟨u,v⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的流量限制为原图该点的流量限制，再套板子就可以解决本题．这就是拆点的基本思想．

如果原图是这样：

![](./images/node.svg)

拆点之后的图是这个样子：

![](./images/node-split.svg)

## 分层图最短路

分层图最短路，如：有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次零代价通过一条路径，求总的最小花费．对于这种题目，我们可以采用 DP 相关的思想，设 dis𝑖,𝑗disi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示当前从起点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号结点，使用了 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次免费通行权限后的最短路径．显然，disdis![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组可以这么转移：

dis𝑖,𝑗 =min{min{dis𝑓𝑟𝑜𝑚,𝑗−1},min{dis𝑓𝑟𝑜𝑚,𝑗 +𝑤}}disi,j=min{min{disfrom,j−1},min{disfrom,j+w}}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑓𝑟𝑜𝑚from![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的父亲节点，𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示当前所走的边的边权．当 𝑗 −1 ≥𝑘j−1≥k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，dis𝑓𝑟𝑜𝑚,𝑗disfrom,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)=∞∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

事实上，这个 DP 就相当于把每个结点拆分成了 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个结点，每个新结点代表使用不同多次免费通行后到达的原图结点．换句话说，就是每个结点 𝑢𝑖ui![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示使用 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次免费通行权限后到达 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结点．

[「JLOI2011」飞行路线](https://www.luogu.com.cn/problem/P4568)

题意：有一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边的无向图，你可以选择 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条道路以零代价通行，求 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小花费．

参考核心代码：

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 ``` |  ```text struct State { // 优先队列的结点结构体 int v , w , cnt ; // cnt 表示已经使用多少次免费通行权限 State () {} State ( int v , int w , int cnt ) : v ( v ), w ( w ), cnt ( cnt ) {} bool operator < ( const State & rhs ) const { return w > rhs . w ; } }; void dijkstra () { memset ( dis , 0x3f , sizeof dis ); dis [ s ][ 0 ] = 0 ; pq . push ( State ( s , 0 , 0 )); // 到起点不需要使用免费通行权，距离为零 while ( ! pq . empty ()) { const State top = pq . top (); pq . pop (); int u = top . v , nowCnt = top . cnt ; if ( done [ u ][ nowCnt ]) continue ; done [ u ][ nowCnt ] = true ; for ( int i = head [ u ]; i ; i = edge [ i ]. next ) { int v = edge [ i ]. v , w = edge [ i ]. w ; if ( nowCnt < k && dis [ v ][ nowCnt \+ 1 ] > dis [ u ][ nowCnt ]) { // 可以免费通行 dis [ v ][ nowCnt \+ 1 ] = dis [ u ][ nowCnt ]; pq . push ( State ( v , dis [ v ][ nowCnt \+ 1 ], nowCnt \+ 1 )); } if ( dis [ v ][ nowCnt ] > dis [ u ][ nowCnt ] \+ w ) { // 不可以免费通行 dis [ v ][ nowCnt ] = dis [ u ][ nowCnt ] \+ w ; pq . push ( State ( v , dis [ v ][ nowCnt ], nowCnt )); } } } } int main () { n = read (), m = read (), k = read (); // 笔者习惯从 1 到 n 编号，而这道题是从 0 到 n - 1，所以要处理一下 s = read () \+ 1 , t = read () \+ 1 ; while ( m \-- ) { int u = read () \+ 1 , v = read () \+ 1 , w = read (); add ( u , v , w ), add ( v , u , w ); // 这道题是双向边 } dijkstra (); int ans = std :: numeric_limits < int >:: max (); // ans 取 int 最大值为初值 for ( int i = 0 ; i <= k ; ++ i ) ans = std :: min ( ans , dis [ t ][ i ]); // 对到达终点的所有情况取最优值 println ( ans ); } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/node.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/node.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [mcendu](https://github.com/mcendu), [ouuan](https://github.com/ouuan), [Anguei](https://github.com/Anguei), [Chrogeek](https://github.com/Chrogeek), [Enter-tainer](https://github.com/Enter-tainer), [Henry-ZHR](https://github.com/Henry-ZHR), [hsfzLZH1](https://github.com/hsfzLZH1), [ksyx](https://github.com/ksyx), [MonkeyOliver](https://github.com/MonkeyOliver), [sshwy](https://github.com/sshwy), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
