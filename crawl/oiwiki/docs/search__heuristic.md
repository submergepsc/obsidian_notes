# 启发式搜索 - OI Wiki

- Source: https://oi-wiki.org/search/heuristic/

# 启发式搜索

本页面将简要介绍启发式搜索及其用法．

## 定义

启发式搜索（英文：heuristic search）是一种在普通搜索算法的基础上引入了启发式函数的搜索算法．

启发式函数的作用是基于已有的信息对搜索的每一个分支选择都做估价，进而选择分支．简单来说，启发式搜索就是对取和不取都做分析，从中选取更优解或删去无效解．

## 例题

由于概念过于抽象，这里使用例题讲解．

[「NOIP2005 普及组」采药](https://www.luogu.com.cn/problem/P1048)

题目大意：有 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种物品和一个容量为 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的背包，每种物品有重量 𝑤𝑖wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和价值 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两种属性，要求选若干个物品（每种物品只能选一次）放入背包，使背包中物品的总价值最大，且背包中物品的总重量不超过背包的容量．

解题思路

我们写一个估价函数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以剪掉所有无效的 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枝条（就是剪去大量无用不选枝条）．

估价函数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的运行过程如下：

我们在取的时候判断一下是不是超过了规定体积（可行性剪枝）；在不取的时候判断一下不取这个时，剩下的药所有的价值 + 现有的价值是否大于目前找到的最优解（最优性剪枝）．

示例代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 ``` |  ```text #include <algorithm> #include <iostream> using namespace std ; constexpr int N = 105 ; int n , m , ans ; struct Node { int a , b ; // a 代表时间，b 代表价值 double f ; } node [ N ]; bool operator < ( Node p , Node q ) { return p . f > q . f ; } int f ( int t , int v ) { // 计算在当前时间下，剩余物品的最大价值 int tot = 0 ; for ( int i = 1 ; t \+ i <= n ; i ++ ) if ( v >= node [ t \+ i ]. a ) { v -= node [ t \+ i ]. a ; tot += node [ t \+ i ]. b ; } else return ( int )( tot \+ v * node [ t \+ i ]. f ); return tot ; } void work ( int t , int p , int v ) { ans = max ( ans , v ); if ( t > n ) return ; // 边界条件：只有n种物品 if ( f ( t , p ) \+ v > ans ) work ( t \+ 1 , p , v ); // 最优性剪枝 if ( node [ t ]. a <= p ) work ( t \+ 1 , p \- node [ t ]. a , v \+ node [ t ]. b ); // 可行性剪枝 } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> m >> n ; for ( int i = 1 ; i <= n ; i ++ ) { cin >> node [ i ]. a >> node [ i ]. b ; node [ i ]. f = 1.0 * node [ i ]. b / node [ i ]. a ; // f为性价比 } sort ( node \+ 1 , node \+ n \+ 1 ); // 根据性价比排序 work ( 1 , m , 0 ); cout << ans << '\n' ; return 0 ; } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/search/heuristic.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/search/heuristic.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [ksyx](https://github.com/ksyx), [Henry-ZHR](https://github.com/Henry-ZHR), [Enter-tainer](https://github.com/Enter-tainer), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [leoleoasd](https://github.com/leoleoasd), [luoguyuntianming](https://github.com/luoguyuntianming), [NachtgeistW](https://github.com/NachtgeistW), [ouuan](https://github.com/ouuan), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
