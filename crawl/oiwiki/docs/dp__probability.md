# 概率 DP - OI Wiki

- Source: https://oi-wiki.org/dp/probability/

# 概率 DP

## 引入

概率 DP 用于解决概率问题与期望问题，建议先对 [概率 & 期望](../../math/probability/exp-var/) 的内容有一定了解．一般情况下，解决概率问题需要顺序循环，而解决期望问题使用逆序循环．如果定义的状态转移方程存在后效性问题，还需要用到 [高斯消元](../../math/numerical/gauss/) 来优化．概率 DP 也会结合其他知识进行考察，例如 [状态压缩](../state/)、树上进行 DP 转移等．

## 概率 DP

这类题目采用顺推，也就是从初始状态推向结果．同一般的 DP 类似，难点依然是对状态转移方程的刻画，只是这类题目经过了概率论知识的包装．

### 例题

[Codeforces 148D Bag of mice](https://codeforces.com/problemset/problem/148/D)

袋子里有 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只白鼠和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只黑鼠，公主和龙轮流从袋子里抓老鼠．谁先抓到白色老鼠谁就赢，如果袋子里没有老鼠了并且没有谁抓到白色老鼠，那么算龙赢．公主每次抓一只老鼠，龙每次抓完一只老鼠之后会有一只老鼠跑出来．每次抓的老鼠和跑出来的老鼠都是随机的．公主先抓．问公主赢的概率．

解答

设 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为轮到公主时袋子里有 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只白鼠，𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只黑鼠，公主赢的概率．初始化边界，𝑓0,𝑗 =0f0,j=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 因为没有白鼠了算龙赢，𝑓𝑖,0 =1fi,0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 因为抓一只就是白鼠，公主赢． 考虑 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的转移：

  * 公主抓到一只白鼠，公主赢了．概率为 𝑖𝑖+𝑗ii+j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 公主抓到一只黑鼠，龙抓到一只白鼠，龙赢了．概率为 𝑗𝑖+𝑗 ⋅𝑖𝑖+𝑗−1ji+j⋅ii+j−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 公主抓到一只黑鼠，龙抓到一只黑鼠，跑出来一只黑鼠，转移到 𝑓𝑖,𝑗−3fi,j−3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．概率为 𝑗𝑖+𝑗 ⋅𝑗−1𝑖+𝑗−1 ⋅𝑗−2𝑖+𝑗−2ji+j⋅j−1i+j−1⋅j−2i+j−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 公主抓到一只黑鼠，龙抓到一只黑鼠，跑出来一只白鼠，转移到 𝑓𝑖−1,𝑗−2fi−1,j−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．概率为 𝑗𝑖+𝑗 ⋅𝑗−1𝑖+𝑗−1 ⋅𝑖𝑖+𝑗−2ji+j⋅j−1i+j−1⋅ii+j−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑公主赢的概率，第二种情况不参与计算．并且要保证后两种情况合法，所以还要判断 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小，满足第三种情况至少要有 3 只黑鼠，满足第四种情况要有 1 只白鼠和 2 只黑鼠．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` |  ```text #include <cstring> #include <iomanip> #include <iostream> using namespace std ; using ll = long long ; int w , b ; double dp [ 1010 ][ 1010 ]; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> w >> b ; memset ( dp , 0 , sizeof ( dp )); for ( int i = 1 ; i <= w ; i ++ ) dp [ i ][ 0 ] = 1 ; // 初始化 for ( int i = 1 ; i <= b ; i ++ ) dp [ 0 ][ i ] = 0 ; for ( int i = 1 ; i <= w ; i ++ ) { for ( int j = 1 ; j <= b ; j ++ ) { // 以下为题面概率转移 dp [ i ][ j ] += ( double ) i / ( i \+ j ); if ( j >= 3 ) { dp [ i ][ j ] += ( double ) j / ( i \+ j ) * ( j \- 1 ) / ( i \+ j \- 1 ) * ( j \- 2 ) / ( i \+ j \- 2 ) * dp [ i ][ j \- 3 ]; } if ( i >= 1 && j >= 2 ) { dp [ i ][ j ] += ( double ) j / ( i \+ j ) * ( j \- 1 ) / ( i \+ j \- 1 ) * i / ( i \+ j \- 2 ) * dp [ i \- 1 ][ j \- 2 ]; } } } cout << fixed << setprecision ( 9 ) << dp [ w ][ b ] << '\n' ; return 0 ; } ```   
---|---  
  
### 习题

  * [POJ3071 Football](http://poj.org/problem?id=3071)
  * [CodeForces 768D Jon and Orbs](https://codeforces.com/problemset/problem/768/D)

## 期望 DP

### 例题

[POJ2096 Collecting Bugs](http://poj.org/problem?id=2096)

一个软件有 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个子系统，会产生 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种 bug．某人一天发现一个 bug，这个 bug 属于某种 bug 分类，也属于某个子系统．每个 bug 属于某个子系统的概率是 1𝑠1s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，属于某种 bug 分类的概率是 1𝑛1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．求发现 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种 bug，且 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个子系统都找到 bug 的期望天数．

解答

令 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为已经找到 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种 bug 分类，𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个子系统的 bug，达到目标状态的期望天数．这里的目标状态是找到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种 bug 分类，𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个子系统的 bug．那么就有 𝑓𝑛,𝑠 =0fn,s=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为已经达到了目标状态，不需要用更多的天数去发现 bug 了，于是就以目标状态为起点开始递推，答案是 𝑓0,0f0,0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的状态转移：

  * 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，发现一个 bug 属于已经发现的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种 bug 分类，𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个子系统，概率为 𝑝1 =𝑖𝑛 ⋅𝑗𝑠p1=in⋅js![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝑓𝑖,𝑗+1fi,j+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，发现一个 bug 属于已经发现的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种 bug 分类，不属于已经发现的子系统，概率为 𝑝2 =𝑖𝑛 ⋅(1 −𝑗𝑠)p2=in⋅(1−js)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝑓𝑖+1,𝑗fi+1,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，发现一个 bug 不属于已经发现 bug 分类，属于 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个子系统，概率为 𝑝3 =(1 −𝑖𝑛) ⋅𝑗𝑠p3=(1−in)⋅js![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝑓𝑖+1,𝑗+1fi+1,j+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，发现一个 bug 不属于已经发现 bug 分类，不属于已经发现的子系统，概率为 𝑝4 =(1 −𝑖𝑛) ⋅(1 −𝑗𝑠)p4=(1−in)⋅(1−js)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

再根据期望的线性性质，就可以得到状态转移方程：

𝑓𝑖,𝑗=𝑝1⋅𝑓𝑖,𝑗+𝑝2⋅𝑓𝑖,𝑗+1+𝑝3⋅𝑓𝑖+1,𝑗+𝑝4⋅𝑓𝑖+1,𝑗+1+1=𝑝2⋅𝑓𝑖,𝑗+1+𝑝3⋅𝑓𝑖+1,𝑗+𝑝4⋅𝑓𝑖+1,𝑗+1+11−𝑝1fi,j=p1⋅fi,j+p2⋅fi,j+1+p3⋅fi+1,j+p4⋅fi+1,j+1+1=p2⋅fi,j+1+p3⋅fi+1,j+p4⋅fi+1,j+1+11−p1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text #include <iomanip> #include <iostream> using namespace std ; int n , s ; double dp [ 1010 ][ 1010 ]; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> s ; dp [ n ][ s ] = 0 ; for ( int i = n ; i >= 0 ; i \-- ) { for ( int j = s ; j >= 0 ; j \-- ) { if ( i == n && s == j ) continue ; dp [ i ][ j ] = ( dp [ i ][ j \+ 1 ] * i * ( s \- j ) \+ dp [ i \+ 1 ][ j ] * ( n \- i ) * j \+ dp [ i \+ 1 ][ j \+ 1 ] * ( n \- i ) * ( s \- j ) \+ n * s ) / ( n * s \- i * j ); // 概率转移 } } cout << fixed << setprecision ( 4 ) << dp [ 0 ][ 0 ] << '\n' ; return 0 ; } ```   
---|---  
  
[「NOIP2016」换教室](http://uoj.ac/problem/262)

牛牛要上 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个时间段的课，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个时间段在 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号教室，可以申请换到 𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号教室，申请成功的概率为 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，至多可以申请 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 节课进行交换．第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个时间段的课上完后要走到第 𝑖 +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个时间段的教室，给出一张图 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个教室 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条路，移动会消耗体力，申请哪几门课程可以使他因在教室间移动耗费的体力值的总和的期望值最小，也就是求出最小的期望路程和．

解答

对于这个无向连通图，先用 Floyd 求出最短路，为后续的状态转移带来便利．以移动一步为一个阶段（从第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个时间段到达第 𝑖 +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个时间段就是移动了一步），那么每一步就有 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率到 𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不过在所有的 𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中只能选 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，有 1 −𝑝𝑖1−pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率到 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求出在 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个阶段走完后的最小期望路程和．

定义 𝑓𝑖,𝑗,0/1fi,j,0/1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为在第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个时间段，连同这一个时间段已经用了 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次换教室的机会，在这个时间段换（1）或者不换（0）教室的最小期望路程和，那么答案就是 min{𝑓𝑛,𝑖,0,𝑓𝑛,𝑖,1},𝑖 ∈[0,𝑚]min{fn,i,0,fn,i,1},i∈[0,m]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．注意边界 𝑓1,0,0 =𝑓1,1,1 =0f1,0,0=f1,1,1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑 𝑓𝑖,𝑗,0/1fi,j,0/1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的状态转移：

  * 如果这一阶段不换，即 𝑓𝑖,𝑗,0fi,j,0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．可能是由上一次不换的状态转移来的，那么就是 𝑓𝑖−1,𝑗,0 +𝑤𝑐𝑖−1,𝑐𝑖fi−1,j,0+wci−1,ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 也有可能是由上一次交换的状态转移来的，这里结合条件概率和全概率的知识分析可以得到 𝑓𝑖−1,𝑗,1 +𝑤𝑑𝑖−1,𝑐𝑖 ⋅𝑝𝑖−1 +𝑤𝑐𝑖−1,𝑐𝑖 ⋅(1 −𝑝𝑖−1)fi−1,j,1+wdi−1,ci⋅pi−1+wci−1,ci⋅(1−pi−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，状态转移方程就有：

𝑓𝑖,𝑗,0=𝑚𝑖𝑛(𝑓𝑖−1,𝑗,0+𝑤𝑐𝑖−1,𝑐𝑖,𝑓𝑖−1,𝑗,1+𝑤𝑑𝑖−1,𝑐𝑖⋅𝑝𝑖−1+𝑤𝑐𝑖−1,𝑐𝑖⋅(1−𝑝𝑖−1))fi,j,0=min(fi−1,j,0+wci−1,ci,fi−1,j,1+wdi−1,ci⋅pi−1+wci−1,ci⋅(1−pi−1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 如果这一阶段交换，即 𝑓𝑖,𝑗,1fi,j,1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．类似地，可能由上一次不换的状态转移来，也可能由上一次交换的状态转移来．那么遇到不换的就乘上 (1 −𝑝𝑖)(1−pi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，遇到交换的就乘上 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将所有会出现的情况都枚举一遍出进行计算就好了．这里不再赘述各种转移情况，相信通过上一种阶段例子，这里的状态转移应该能够很容易写出来．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 ``` |  ```text #include <algorithm> #include <iomanip> #include <iostream> using namespace std ; constexpr int MAXN = 2010 ; int n , m , v , e ; int f [ MAXN ][ MAXN ], c [ MAXN ], d [ MAXN ]; double dp [ MAXN ][ MAXN ][ 2 ], p [ MAXN ]; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> m >> v >> e ; for ( int i = 1 ; i <= n ; i ++ ) cin >> c [ i ]; for ( int i = 1 ; i <= n ; i ++ ) cin >> d [ i ]; for ( int i = 1 ; i <= n ; i ++ ) cin >> p [ i ]; for ( int i = 1 ; i <= v ; i ++ ) for ( int j = 1 ; j < i ; j ++ ) f [ i ][ j ] = f [ j ][ i ] = 1e9 ; int u , V , w ; for ( int i = 1 ; i <= e ; i ++ ) { cin >> u >> V >> w ; f [ u ][ V ] = f [ V ][ u ] = min ( w , f [ u ][ V ]); } for ( int k = 1 ; k <= v ; k ++ ) for ( int i = 1 ; i <= v ; i ++ ) // 前面的，按照前面的题解进行一个状态转移 for ( int j = 1 ; j < i ; j ++ ) if ( f [ i ][ k ] \+ f [ k ][ j ] < f [ i ][ j ]) f [ i ][ j ] = f [ j ][ i ] = f [ i ][ k ] \+ f [ k ][ j ]; for ( int i = 1 ; i <= n ; i ++ ) for ( int j = 0 ; j <= m ; j ++ ) dp [ i ][ j ][ 0 ] = dp [ i ][ j ][ 1 ] = 1e9 ; dp [ 1 ][ 0 ][ 0 ] = dp [ 1 ][ 1 ][ 1 ] = 0 ; for ( int i = 2 ; i <= n ; i ++ ) // 有后效性方程 for ( int j = 0 ; j <= min ( i , m ); j ++ ) { dp [ i ][ j ][ 0 ] = min ( dp [ i \- 1 ][ j ][ 0 ] \+ f [ c [ i \- 1 ]][ c [ i ]], dp [ i \- 1 ][ j ][ 1 ] \+ f [ c [ i \- 1 ]][ c [ i ]] * ( 1 \- p [ i \- 1 ]) \+ f [ d [ i \- 1 ]][ c [ i ]] * p [ i \- 1 ]); if ( j != 0 ) { dp [ i ][ j ][ 1 ] = min ( dp [ i \- 1 ][ j \- 1 ][ 0 ] \+ f [ c [ i \- 1 ]][ d [ i ]] * p [ i ] \+ f [ c [ i \- 1 ]][ c [ i ]] * ( 1 \- p [ i ]), dp [ i \- 1 ][ j \- 1 ][ 1 ] \+ f [ c [ i \- 1 ]][ c [ i ]] * ( 1 \- p [ i \- 1 ]) * ( 1 \- p [ i ]) \+ f [ c [ i \- 1 ]][ d [ i ]] * ( 1 \- p [ i \- 1 ]) * p [ i ] \+ f [ d [ i \- 1 ]][ c [ i ]] * ( 1 \- p [ i ]) * p [ i \- 1 ] \+ f [ d [ i \- 1 ]][ d [ i ]] * p [ i \- 1 ] * p [ i ]); } } double ans = 1e9 ; for ( int i = 0 ; i <= m ; i ++ ) ans = min ( dp [ n ][ i ][ 0 ], min ( dp [ n ][ i ][ 1 ], ans )); cout << fixed << setprecision ( 2 ) << ans ; return 0 ; } ```   
---|---  
  
比较这两个问题可以发现，DP 求期望题目在对具体是求一个值或是最优化问题上会对方程得到转移方式有一些影响，但无论是 DP 求概率还是 DP 求期望，总是离不开概率知识和列出、化简计算公式的步骤，在写状态转移方程时需要思考的细节也类似．

### 习题

  * [HDU3853 LOOPS](https://acm.hdu.edu.cn/showproblem.php?pid=3853)
  * [HDU4035 Maze](https://acm.hdu.edu.cn/showproblem.php?pid=4035)
  * [「SCOI2008」奖励关](https://www.luogu.com.cn/problem/P2473)

## 有后效性 DP

### 例题

[CodeForces 24D Broken robot](https://codeforces.com/problemset/problem/24/D)

给出一个 𝑛 ×𝑚n×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵区域．一个机器人初始在第 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行第 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列，每一步机器人会等概率地选择停在原地、左移一步、右移一步、下移一步．如果机器人在边界则不会往区域外移动，问机器人到达最后一行的期望步数．

解答

在 𝑚 =1m=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时每次有 1212![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率不动，有 1212![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率向下移动一格，答案为 2 ⋅(𝑛 −𝑥)2⋅(n−x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)． 设 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为机器人机器人从第 i 行第 j 列出发到达第 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行的期望步数，最终状态为 𝑓𝑛,𝑗 =0fn,j=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)． 由于机器人会等概率地选择停在原地，左移一步，右移一步，下移一步，考虑 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的状态转移：

  * 𝑓𝑖,1 =13 ⋅(𝑓𝑖+1,1 +𝑓𝑖,2 +𝑓𝑖,1) +1fi,1=13⋅(fi+1,1+fi,2+fi,1)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑓𝑖,𝑗 =14 ⋅(𝑓𝑖,𝑗 +𝑓𝑖,𝑗−1 +𝑓𝑖,𝑗+1 +𝑓𝑖+1,𝑗) +1fi,j=14⋅(fi,j+fi,j−1+fi,j+1+fi+1,j)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑓𝑖,𝑚 =13 ⋅(𝑓𝑖,𝑚 +𝑓𝑖,𝑚−1 +𝑓𝑖+1,𝑚) +1fi,m=13⋅(fi,m+fi,m−1+fi+1,m)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在行之间由于只能向下移动，是满足无后效性的．在列之间可以左右移动，在移动过程中可能产生环，不满足无后效性． 将方程变换后可以得到：

  * 2𝑓𝑖,1 −𝑓𝑖,2 =3 +𝑓𝑖+1,12fi,1−fi,2=3+fi+1,1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 3𝑓𝑖,𝑗 −𝑓𝑖,𝑗−1 −𝑓𝑖,𝑗+1 =4 +𝑓𝑖+1,𝑗3fi,j−fi,j−1−fi,j+1=4+fi+1,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 2𝑓𝑖,𝑚 −𝑓𝑖,𝑚−1 =3 +𝑓𝑖+1,𝑚2fi,m−fi,m−1=3+fi+1,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于是逆序的递推，所以每一个 𝑓𝑖+1,𝑗fi+1,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是已知的． 由于有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列，所以右边相当于是一个 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行的列向量，那么左边就是 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列的矩阵．使用增广矩阵，就变成了 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行 𝑚 +1m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列的矩阵，然后进行 [高斯消元](../../math/numerical/gauss/) 即可解出答案．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 ``` |  ```text #include <cstdio> #include <cstring> using namespace std ; constexpr int MAXN = 1e3 \+ 10 ; double a [ MAXN ][ MAXN ], f [ MAXN ]; int n , m ; void solve ( int x ) { for ( int i = 1 ; i <= m ; i ++ ) { if ( i == 1 ) { a [ i ][ i ] = 2 ; a [ i ][ i \+ 1 ] = -1 ; a [ i ][ m \+ 1 ] = 3 \+ f [ i ]; continue ; } else if ( i == m ) { a [ i ][ i ] = 2 ; a [ i ][ i \- 1 ] = -1 ; a [ i ][ m \+ 1 ] = 3 \+ f [ i ]; continue ; } a [ i ][ i ] = 3 ; a [ i ][ i \+ 1 ] = -1 ; a [ i ][ i \- 1 ] = -1 ; a [ i ][ m \+ 1 ] = 4 \+ f [ i ]; } for ( int i = 1 ; i < m ; i ++ ) { double p = a [ i \+ 1 ][ i ] / a [ i ][ i ]; a [ i \+ 1 ][ i ] = 0 ; a [ i \+ 1 ][ i \+ 1 ] -= a [ i ][ i \+ 1 ] * p ; a [ i \+ 1 ][ m \+ 1 ] -= a [ i ][ m \+ 1 ] * p ; } f [ m ] = a [ m ][ m \+ 1 ] / a [ m ][ m ]; for ( int i = m \- 1 ; i >= 1 ; i \-- ) f [ i ] = ( a [ i ][ m \+ 1 ] \- f [ i \+ 1 ] * a [ i ][ i \+ 1 ]) / a [ i ][ i ]; } int main () { scanf ( "%d %d" , & n , & m ); int st , ed ; scanf ( "%d %d" , & st , & ed ); if ( m == 1 ) { printf ( "%.10f \n " , 2.0 * ( n \- st )); return 0 ; } for ( int i = n \- 1 ; i >= st ; i \-- ) { solve ( i ); } printf ( "%.10f \n " , f [ ed ]); return 0 ; } ```   
---|---  
  
### 习题

  * [HDU 4418 Time Travel](https://acm.hdu.edu.cn/showproblem.php?pid=4418)
  * [「HNOI2013」游走](https://loj.ac/problem/2383)

## 参考文献

[kuangbin 概率 DP 总结](https://www.cnblogs.com/kuangbin/archive/2012/10/02/2710606.html)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/dp/probability.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/dp/probability.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [ShaoChenHeng](https://github.com/ShaoChenHeng), [Enter-tainer](https://github.com/Enter-tainer), [ksyx](https://github.com/ksyx), [c-forrest](https://github.com/c-forrest), [StudyingFather](https://github.com/StudyingFather), [H-J-Granger](https://github.com/H-J-Granger), [iamtwz](https://github.com/iamtwz), [imp2002](https://github.com/imp2002), [Ir1d](https://github.com/Ir1d), [kenlig](https://github.com/kenlig), [LeBronGod](https://github.com/LeBronGod), [Marcythm](https://github.com/Marcythm), [MegaOwIer](https://github.com/MegaOwIer), [NachtgeistW](https://github.com/NachtgeistW), [ouuan](https://github.com/ouuan), [Patchouliys](https://github.com/Patchouliys), [Soohti](https://github.com/Soohti), [sun2snow](https://github.com/sun2snow), [TianKong-y](https://github.com/TianKong-y)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
