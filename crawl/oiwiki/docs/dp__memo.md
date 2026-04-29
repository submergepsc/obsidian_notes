# 记忆化搜索 - OI Wiki

- Source: https://oi-wiki.org/dp/memo/

# 记忆化搜索

## 定义

记忆化搜索是一种通过记录已经遍历过的状态的信息，从而避免对同一状态重复遍历的搜索实现方式．

因为记忆化搜索确保了每个状态只访问一次，它也是一种常见的动态规划实现方式．

## 引入

[[NOIP2005] 采药](https://www.luogu.com.cn/problem/P1048)

山洞里有 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 株不同的草药，采每一株都需要一些时间 𝑡𝑖ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每一株也有它自身的价值 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．给你一段时间 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在这段时间里，你可以采到一些草药．让采到的草药的总价值最大．

1 ≤𝑇 ≤1031≤T≤103![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，1 ≤𝑡𝑖,𝑣𝑖,𝑀 ≤1001≤ti,vi,M≤100![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 朴素的 [DFS](../../search/dfs/) 做法

很容易实现这样一个朴素的搜索做法：在搜索时记录下当前准备选第几个物品、剩余的时间是多少、已经获得的价值是多少这三个参数，然后枚举当前物品是否被选，转移到相应的状态．

实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text int n , t ; int tcost [ 103 ], mget [ 103 ]; int ans = 0 ; void dfs ( int pos , int tleft , int tans ) { if ( tleft < 0 ) return ; if ( pos == n \+ 1 ) { ans = max ( ans , tans ); return ; } dfs ( pos \+ 1 , tleft , tans ); dfs ( pos \+ 1 , tleft \- tcost [ pos ], tans \+ mget [ pos ]); } int main () { cin >> t >> n ; for ( int i = 1 ; i <= n ; i ++ ) cin >> tcost [ i ] >> mget [ i ]; dfs ( 1 , t , 0 ); cout << ans << endl ; return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text tcost = [ 0 ] * 103 mget = [ 0 ] * 103 ans = 0 def dfs ( pos , tleft , tans ): global ans if tleft < 0 : return if pos == n \+ 1 : ans = max ( ans , tans ) return dfs ( pos \+ 1 , tleft , tans ) dfs ( pos \+ 1 , tleft \- tcost [ pos ], tans \+ mget [ pos ]) t , n = map ( lambda x : int ( x ), input () . split ()) for i in range ( 1 , n \+ 1 ): tcost [ i ], mget [ i ] = map ( lambda x : int ( x ), input () . split ()) dfs ( 1 , t , 0 ) print ( ans ) ```   
---|---  
  
这种做法的时间复杂度是指数级别的，并不能通过本题．

### 优化

上面的做法为什么效率低下呢？因为同一个状态会被访问多次．

如果我们每查询完一个状态后将该状态的信息存储下来，再次需要访问这个状态就可以直接使用之前计算得到的信息，从而避免重复计算．这充分利用了动态规划中很多问题具有大量重叠子问题的特点，属于用空间换时间的「记忆化」思想．

具体到本题上，我们在朴素的 DFS 的基础上，增加一个数组 `mem` 来记录每个 `dfs(pos,tleft)` 的返回值．刚开始把 `mem` 中每个值都设成 `-1`（代表没求解过）．每次需要访问一个状态时，如果相应状态的值在 `mem` 中为 `-1`，则递归访问该状态．否则我们直接使用 `mem` 中已经存储过的值即可．

通过这样的处理，我们确保了每个状态只会被访问一次，因此该算法的时间复杂度为 𝑂(𝑇𝑀)O(TM)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text int n , t ; int tcost [ 103 ], mget [ 103 ]; int mem [ 103 ][ 1003 ]; int dfs ( int pos , int tleft ) { if ( mem [ pos ][ tleft ] != -1 ) return mem [ pos ][ tleft ]; // 已经访问过的状态，直接返回之前记录的值 if ( pos == n \+ 1 ) return mem [ pos ][ tleft ] = 0 ; int dfs1 , dfs2 = \- INF ; dfs1 = dfs ( pos \+ 1 , tleft ); if ( tleft >= tcost [ pos ]) dfs2 = dfs ( pos \+ 1 , tleft \- tcost [ pos ]) \+ mget [ pos ]; // 状态转移 return mem [ pos ][ tleft ] = max ( dfs1 , dfs2 ); // 最后将当前状态的值存下来 } int main () { memset ( mem , -1 , sizeof ( mem )); cin >> t >> n ; for ( int i = 1 ; i <= n ; i ++ ) cin >> tcost [ i ] >> mget [ i ]; cout << dfs ( 1 , t ) << endl ; return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text tcost = [ 0 ] * 103 mget = [ 0 ] * 103 mem = [[ \- 1 for i in range ( 1003 )] for j in range ( 103 )] def dfs ( pos , tleft ): if mem [ pos ][ tleft ] != \- 1 : return mem [ pos ][ tleft ] if pos == n \+ 1 : mem [ pos ][ tleft ] = 0 return mem [ pos ][ tleft ] dfs1 = dfs2 = \- INF dfs1 = dfs ( pos \+ 1 , tleft ) if tleft >= tcost [ pos ]: dfs2 = dfs ( pos \+ 1 , tleft \- tcost [ pos ]) \+ mget [ pos ] mem [ pos ][ tleft ] = max ( dfs1 , dfs2 ) return mem [ pos ][ tleft ] t , n = map ( lambda x : int ( x ), input () . split ()) for i in range ( 1 , n \+ 1 ): tcost [ i ], mget [ i ] = map ( lambda x : int ( x ), input () . split ()) print ( dfs ( 1 , t )) ```   
---|---  
  
## 与递推的联系与区别

在求解动态规划的问题时，记忆化搜索与递推的代码，在形式上是高度类似的．这是由于它们使用了相同的状态表示方式和类似的状态转移．也正因为如此，一般来说两种实现的时间复杂度是一样的．

下面给出的是递推实现的代码（为了方便对比，没有添加滚动数组优化），通过对比可以发现二者在形式上的类似性．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text int n , t , w [ 105 ], v [ 105 ], f [ 105 ][ 1005 ]; int main () { cin >> n >> t ; for ( int i = 1 ; i <= n ; i ++ ) cin >> w [ i ] >> v [ i ]; for ( int i = 1 ; i <= n ; i ++ ) for ( int j = 0 ; j <= t ; j ++ ) { f [ i ][ j ] = f [ i \- 1 ][ j ]; if ( j >= w [ i ]) f [ i ][ j ] = max ( f [ i ][ j ], f [ i \- 1 ][ j \- w [ i ]] \+ v [ i ]); // 状态转移方程 } cout << f [ n ][ t ]; return 0 ; } ```   
---|---  
  
在求解动态规划的问题时，记忆化搜索和递推，都确保了同一状态至多只被求解一次．而它们实现这一点的方式则略有不同：递推通过设置明确的访问顺序来避免重复访问，记忆化搜索虽然没有明确规定访问顺序，但通过给已经访问过的状态打标记的方式，也达到了同样的目的．

与递推相比，记忆化搜索因为不用明确规定访问顺序，在实现难度上有时低于递推，且能比较方便地处理边界情况，这是记忆化搜索的一大优势．但与此同时，记忆化搜索难以使用滚动数组等优化，且由于存在递归，运行效率会低于递推．因此应该视题目选择更适合的实现方式．

## 如何写记忆化搜索

### 方法一

  1. 把这道题的 dp 状态和方程写出来
  2. 根据它们写出 dfs 函数
  3. 添加记忆化数组

举例：

𝑑𝑝𝑖 =max{𝑑𝑝𝑗 +1} (1 ≤𝑗 <𝑖 ∧𝑎𝑗 <𝑎𝑖)dpi=max{dpj+1}(1≤j<i∧aj<ai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（最长上升子序列）

转为

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text int dfs ( int i ) { if ( mem [ i ] != -1 ) return mem [ i ]; int ret = 1 ; for ( int j = 1 ; j < i ; j ++ ) if ( a [ j ] < a [ i ]) ret = max ( ret , dfs ( j ) \+ 1 ); return mem [ i ] = ret ; } int main () { memset ( mem , -1 , sizeof ( mem )); // 读入部分略去 int ret = 0 ; for ( int j = 1 ; j <= n ; j ++ ) { ret = max ( ret , dfs ( j )); } cout << ret << endl ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 ``` |  ```text def dfs ( i ): if mem [ i ] != \- 1 : return mem [ i ] ret = 1 for j in range ( 1 , i ): if a [ j ] < a [ i ]: ret = max ( ret , dfs ( j ) \+ 1 ) mem [ i ] = ret return mem [ i ] ```   
---|---  
  
### 方法二

  1. 写出这道题的暴搜程序（最好是 [dfs](../../search/dfs/)）
  2. 将这个 dfs 改成「无需外部变量」的 dfs
  3. 添加记忆化数组

举例：本文中「采药」的例子

* * *

>  __本页面最近更新： 2026/4/23 03:45:48，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/dp/memo.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/dp/memo.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [interestingLSY](https://github.com/interestingLSY), [Enter-tainer](https://github.com/Enter-tainer), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [Tiphereth-A](https://github.com/Tiphereth-A), [Marcythm](https://github.com/Marcythm), [ouuan](https://github.com/ouuan), [Xeonacid](https://github.com/Xeonacid), [cbw2007](https://github.com/cbw2007), [Chrogeek](https://github.com/Chrogeek), [H-J-Granger](https://github.com/H-J-Granger), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [ImpleLee](https://github.com/ImpleLee), [lailai0916](https://github.com/lailai0916), [luklapse](https://github.com/luklapse), [Menci](https://github.com/Menci), [NachtgeistW](https://github.com/NachtgeistW), [shawlleyw](https://github.com/shawlleyw), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [Wahacer](https://github.com/Wahacer)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
