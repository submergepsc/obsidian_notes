# 数位 DP - OI Wiki

- Source: https://oi-wiki.org/dp/number/

# 数位 DP

本页面将简要介绍数位 DP．

## 引入

数位是指把一个数字按照个、十、百、千等等一位一位地拆开，关注它每一位上的数字．如果拆的是十进制数，那么每一位数字都是 0~9，其他进制可类比十进制．

数位 DP：用来解决一类特定问题，这种问题比较好辨认，一般具有这几个特征：

  1. 要求统计满足一定条件的数的数量（即，最终目的为计数）；

  2. 这些条件经过转化后可以使用「数位」的思想去理解和判断；

  3. 输入会提供一个数字区间（有时也只提供上界）来作为统计的限制；

  4. 上界很大（比如 10181018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），暴力枚举验证会超时．

数位 DP 的基本原理：

考虑人类计数的方式，最朴素的计数就是从小到大开始依次加一．但我们发现对于位数比较多的数，这样的过程中有许多重复的部分．例如，从 7000 数到 7999、从 8000 数到 8999、和从 9000 数到 9999 的过程非常相似，它们都是后三位从 000 变到 999，不一样的地方只有千位这一位，所以我们可以把这些过程归并起来，将这些过程中产生的计数答案也都存在一个通用的数组里．此数组根据题目具体要求设置状态，用递推或 DP 的方式进行状态转移．

数位 DP 中通常会利用常规计数问题技巧，比如把一个区间内的答案拆成两部分相减（即 ans[𝑙,𝑟] =ans[0,𝑟] −ans[0,𝑙−1]ans[l,r]=ans[0,r]−ans[0,l−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

那么有了通用答案数组，接下来就是统计答案．统计答案可以选择记忆化搜索，也可以选择循环迭代递推．为了不重不漏地统计所有不超过上限的答案，要从高到低枚举每一位，再考虑每一位都可以填哪些数字，最后利用通用答案数组统计答案．

接下来我们具体看几道题目．

## 例题一

例 1 [Luogu P2602 数字计数](https://www.luogu.com.cn/problem/P2602)

题目大意：给定两个正整数 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求在 [𝑎,𝑏][a,b]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的所有整数中，每个数码（digit）各出现了多少次．

### 方法一

#### 解释

发现对于满 ii![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的数，所有数字出现的次数都是相同的，故设数组 dp𝑖dpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为满 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的数中每个数字出现的次数，此时暂时不处理前导零．则有 dp𝑖 =10 ×dp𝑖−1 +10𝑖−1dpi=10×dpi−1+10i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这两部分前一个是来自前 𝑖 −1i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位数字的贡献，后一个是来自第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的数字的贡献．

有了 dpdp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组，我们来考虑如何统计答案．将上界按位分开，从高到低枚举，不贴着上界时，后面可以随便取值．贴着上界时，后面就只能取 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到上界，分两部分分别计算贡献．最后考虑下前导零，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位为前导 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，此时 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 i−1i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位也都是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是多算了将 𝑖 −1i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位填满的答案，需要额外减去．

#### 实现

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` |  ```text #include <cstdio> using namespace std ; constexpr int N = 15 ; using ll = long long ; ll l , r , dp [ N ], mi [ N ]; ll ans1 [ N ], ans2 [ N ]; int a [ N ]; void solve ( ll n , ll * ans ) { ll tmp = n ; int len = 0 ; while ( n ) a [ ++ len ] = n % 10 , n /= 10 ; for ( int i = len ; i >= 1 ; \-- i ) { for ( int j = 0 ; j < 10 ; j ++ ) ans [ j ] += dp [ i \- 1 ] * a [ i ]; for ( int j = 0 ; j < a [ i ]; j ++ ) ans [ j ] += mi [ i \- 1 ]; tmp -= mi [ i \- 1 ] * a [ i ], ans [ a [ i ]] += tmp \+ 1 ; ans [ 0 ] -= mi [ i \- 1 ]; } } int main () { scanf ( "%lld%lld" , & l , & r ); mi [ 0 ] = 1l l ; for ( int i = 1 ; i <= 13 ; ++ i ) { dp [ i ] = dp [ i \- 1 ] * 10 \+ mi [ i \- 1 ]; mi [ i ] = 10l l * mi [ i \- 1 ]; } solve ( r , ans1 ), solve ( l \- 1 , ans2 ); for ( int i = 0 ; i < 10 ; ++ i ) printf ( "%lld " , ans1 [ i ] \- ans2 [ i ]); return 0 ; } ```   
---|---  
  
### 方法二

#### 解释

此题也可以使用记忆化搜索．dp𝑖dpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示不贴上限、无前导零时，位数为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的答案．

详见代码注释

#### 过程

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 ``` |  ```text #include <cstdio> #include <cstring> #include <iostream> using namespace std ; using ll = long long ; constexpr int N = 50005 ; ll a , b ; ll f [ 15 ], ksm [ 15 ], p [ 15 ], now [ 15 ]; ll dfs ( int u , int x , bool f0 , bool lim ) { // u 表示位数，f0 是否有前导零，lim 是否都贴在上限上 if ( ! u ) { if ( f0 ) f0 = false ; return 0 ; } if ( ! lim && ! f0 && ( ~ f [ u ])) return f [ u ]; ll cnt = 0 ; int lst = lim ? p [ u ] : 9 ; for ( int i = 0 ; i <= lst ; i ++ ) { // 枚举这位要填的数字 if ( f0 && i == 0 ) cnt += dfs ( u \- 1 , x , 1 , lim && i == lst ); // 处理前导零 else if ( i == x && lim && i == lst ) cnt += now [ u \- 1 ] \+ 1 \+ dfs ( u \- 1 , x , 0 , lim && i == lst ); // 此时枚举的前几位都贴在给定的上限上． else if ( i == x ) cnt += ksm [ u \- 1 ] \+ dfs ( u \- 1 , x , 0 , lim && i == lst ); else cnt += dfs ( u \- 1 , x , 0 , lim && i == lst ); } if (( ! lim ) && ( ! f0 )) f [ u ] = cnt ; // 只有不贴着上限和没有前导零才能记忆 return cnt ; } ll gans ( ll d , int dig ) { int len = 0 ; memset ( f , -1 , sizeof ( f )); while ( d ) { p [ ++ len ] = d % 10 ; d /= 10 ; now [ len ] = now [ len \- 1 ] \+ p [ len ] * ksm [ len \- 1 ]; } return dfs ( len , dig , 1 , 1 ); } int main () { scanf ( "%lld%lld" , & a , & b ); ksm [ 0 ] = 1 ; for ( int i = 1 ; i <= 12 ; i ++ ) ksm [ i ] = ksm [ i \- 1 ] * 10l l ; for ( int i = 0 ; i < 9 ; i ++ ) printf ( "%lld " , gans ( b , i ) \- gans ( a \- 1 , i )); printf ( "%lld \n " , gans ( b , 9 ) \- gans ( a \- 1 , 9 )); return 0 ; } ```   
---|---  
  
## 例题二

例 2 [HDU 2089 不要 62](https://acm.hdu.edu.cn/showproblem.php?pid=2089)

题面大意：统计一个区间内数位上不能有 4 也不能有连续的 62 的数有多少．

### 解释

没有 4 的话在枚举的时候判断一下，不枚举 4 就可以保证状态合法了，所以这个约束没有记忆化的必要，而对于 62 的话，涉及到两位，当前一位是 6 或者不是 6 这两种不同情况计数是不相同的，所以要用状态来记录不同的方案数．dppos,stadppos,sta![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示当前第 pospos![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位，前一位是否是 6 的状态，这里 stasta![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只需要取 0 和 1 两种状态就可以了，不是 6 的情况可视为同种，不会影响计数．

### 实现

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ``` |  ```text #include <cstdio> #include <cstring> #include <iostream> using namespace std ; int x , y , dp [ 15 ][ 3 ], p [ 50 ]; void pre () { memset ( dp , 0 , sizeof ( dp )); dp [ 0 ][ 0 ] = 1 ; for ( int i = 1 ; i <= 10 ; i ++ ) { dp [ i ][ 0 ] = dp [ i \- 1 ][ 0 ] * 9 \- dp [ i \- 1 ][ 1 ]; dp [ i ][ 1 ] = dp [ i \- 1 ][ 0 ]; dp [ i ][ 2 ] = dp [ i \- 1 ][ 2 ] * 10 \+ dp [ i \- 1 ][ 1 ] \+ dp [ i \- 1 ][ 0 ]; } } int cal ( int x ) { int cnt = 0 , ans = 0 , tmp = x ; while ( x ) { p [ ++ cnt ] = x % 10 ; x /= 10 ; } bool flag = false ; p [ cnt \+ 1 ] = 0 ; for ( int i = cnt ; i ; i \-- ) { // 从高到低枚举数位 ans += p [ i ] * dp [ i \- 1 ][ 2 ]; if ( flag ) ans += p [ i ] * dp [ i \- 1 ][ 0 ]; else { if ( p [ i ] > 4 ) ans += dp [ i \- 1 ][ 0 ]; if ( p [ i ] > 6 ) ans += dp [ i \- 1 ][ 1 ]; if ( p [ i ] > 2 && p [ i \+ 1 ] == 6 ) ans += dp [ i ][ 1 ]; if ( p [ i ] == 4 || ( p [ i ] == 2 && p [ i \+ 1 ] == 6 )) flag = true ; } } return tmp \- ans ; } int main () { pre (); while ( ~ scanf ( "%d%d" , & x , & y )) { if ( ! x && ! y ) break ; if ( x > y ) swap ( x , y ); printf ( "%d \n " , cal ( y \+ 1 ) \- cal ( x )); } return 0 ; } ```   
---|---  
  
## 例题三

例 3 [SCOI2009 windy 数](https://loj.ac/problem/10165)

题目大意：给定一个区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求其中满足条件 **不含前导 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且相邻两个数字相差至少为 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)** 的数字个数．

### 解释

首先我们将问题转化成更加简单的形式．设 ans𝑖ansi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示在区间 [1,𝑖][1,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中满足条件的数的数量，那么所求的答案就是 ans𝑟 −ans𝑙−1ansr−ansl−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于一个小于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数，它从高到低肯定出现某一位，使得这一位上的数值小于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这一位上对应的数值．而之前的所有位都和 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的位相等．

有了这个性质，我们可以定义 𝑓(𝑖,𝑠𝑡,𝑜𝑝)f(i,st,op)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示当前将要考虑的是从高到低的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位，当前该前缀的状态为 𝑠𝑡st![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且前缀和当前求解的数字的大小关系是 𝑜𝑝op![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑜𝑝 =1op=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示等于，𝑜𝑝 =0op=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示小于）时的数字个数．在本题中，这个前缀的状态就是上一位的值，因为当前将要确定的位不能取哪些数只和上一位有关．在其他题目中，这个值可以是：前缀的数字和，前缀所有数字的 gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，该前缀取模某个数的余数，也有两种或多种合用的情况．

写出 **状态转移方程** ：𝑓(𝑖,𝑠𝑡,𝑜𝑝) =∑maxx𝑘=1𝑓(𝑖 +1,𝑘,𝑜𝑝 =1 and⁡ 𝑘 =maxx) (|st −𝑘| ≥2)f(i,st,op)=∑k=1maxxf(i+1,k,op=1 and⁡ k=maxx)(|st−k|≥2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是当前枚举的下一位的值，而 maxxmaxx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是当前能取到的最高位．因为如果 op =1op=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么你在这一位上取的值一定不能大于求解的数字上该位的值，否则则没有限制．

我们发现，尽管前缀所选择的状态不同，而 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的三个参数相同，答案就是一样的．为了防止这个答案被计算多次，可以使用 [记忆化搜索](../memo/) 的方式实现．

### 实现

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` |  ```text int dfs ( int x , int st , int op ) // op=1 =; op=0 < { if ( ! x ) return 1 ; if ( ! op && ~ f [ x ][ st ]) return f [ x ][ st ]; int maxx = op ? dim [ x ] : 9 , ret = 0 ; for ( int i = 0 ; i <= maxx ; i ++ ) { if ( abs ( st \- i ) < 2 ) continue ; if ( st == 11 && i == 0 ) ret += dfs ( x \- 1 , 11 , op & ( i == maxx )); else ret += dfs ( x \- 1 , i , op & ( i == maxx )); } if ( ! op ) f [ x ][ st ] = ret ; return ret ; } int solve ( int x ) { memset ( f , -1 , sizeof f ); dim . clear (); dim . push_back ( -1 ); int t = x ; while ( x ) { dim . push_back ( x % 10 ); x /= 10 ; } return dfs ( dim . size () \- 1 , 11 , 1 ); } ```   
---|---  
  
## 例题四

例 4.[SPOJMYQ10](https://www.spoj.com/problems/MYQ10/en/)

题面大意：假如手写下 [𝑛,𝑚][n,m]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间所有整数，会有多少数看起来和在镜子里看起来一模一样？（𝑛,𝑚 <1044,𝑇 <105n,m<1044,T<105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

### 解释

注：由于这里考虑到的镜像，只有 0,1,80,1,8![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的镜像是自己本身．所以，这里的「一模一样」并不是传统意义上的回文串，而是只含有 0,1,80,1,8![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的回文串．

首先，在数位 DP 过程中，显然只有 0,1,80,1,8![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能被选中．

其次，由于数值超过 long long 范围，所以 [𝑛,𝑚] =[1,𝑚] −[1,𝑛 −1][n,m]=[1,m]−[1,n−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不再适用（高精度比较繁琐），而是需要对 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否合法进行判断，得出：[𝑛,𝑚] =[1,𝑚] −[1,𝑛] +check(𝑛)[n,m]=[1,m]−[1,n]+check(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

镜像解决了，如何判断回文？

我们需要用一个小数组记录一下之前的值．在未超过一半的长度时，只要不超上限就行；在超过一半的长度时，还需要判断是否和与之「镜面对称」的位相等．

需要额外注意的是，这道题的记忆化部分，不能用 `memset`，否则会导致超时．

### 实现

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``` |  ```text int check ( char cc []) { // n 的特判 int strc = strlen ( cc ); for ( int i = 0 ; i < strc ; ++ i ) { if ( ! ( cc [ i ] == cc [ strc \- i \- 1 ] && ( cc [ i ] == '1' || cc [ i ] == '8' || cc [ i ] == '0' ))) return 0l l ; } return 1l l ; } // now: 当前位, eff: 有效位, fulc: 是否全顶格, ful0: 是否全0 int dfs ( int now , int eff , bool ful0 , bool fulc ) { if ( now == 0 ) return 1l l ; if ( ! fulc && f [ now ][ eff ][ ful0 ] != -1 ) // 记忆化 return f [ now ][ eff ][ ful0 ]; int res = 0 , maxk = fulc ? dig [ now ] : 9 ; for ( int i = 0 ; i <= maxk ; ++ i ) { if ( i != 0 && i != 1 && i != 8 ) continue ; b [ now ] = i ; if ( ful0 && i == 0 ) // 全前导 0 res += dfs ( now \- 1 , eff \- 1 , 1 , 0 ); else if ( now > eff / 2 ) // 未过半程 res += dfs ( now \- 1 , eff , 0 , fulc && ( dig [ now ] == i )); // 已过半程 else if ( b [ now ] == b [ eff \- now \+ 1 ]) res += dfs ( now \- 1 , eff , 0 , fulc && ( dig [ now ] == i )); } if ( ! fulc ) f [ now ][ eff ][ ful0 ] = res ; return res ; } char cc1 [ 100 ], cc2 [ 100 ]; int strc , ansm , ansn ; int get ( char cc []) { // 处理封装 strc = strlen ( cc ); for ( int i = 0 ; i < strc ; ++ i ) dig [ strc \- i ] = cc [ i ] \- '0' ; return dfs ( strc , strc , 1 , 1 ); } scanf ( "%s%s" , cc1 , cc2 ); printf ( "%lld \n " , get ( cc2 ) \- get ( cc1 ) \+ check ( cc1 )); ```   
---|---  
  
## 例题五

例 5.[P3311 数数](https://www.luogu.com.cn/problem/P3311)

题面：我们称一个正整数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是幸运数，当且仅当它的十进制表示中不包含数字串集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中任意一个元素作为其子串．例如当 𝑆 ={22,333,0233}S={22,333,0233}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，233233233233![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是幸运数，2333233323332333![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、20233202332023320233![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、3223322332233223![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是幸运数．给定 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，计算不大于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幸运数个数．答案对 109 +7109+7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模．

1 ≤𝑛 <101201，1 ≤𝑚 ≤100，1 ≤∑𝑚𝑖=1|𝑠𝑖| ≤1500，min𝑚𝑖=1|𝑠𝑖| ≥11≤n<101201，1≤m≤100，1≤∑i=1m|si|≤1500，mini=1m|si|≥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 |𝑠𝑖||si|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示字符串 𝑠𝑖si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的长度．𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有前导 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是 𝑠𝑖si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能有前导 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 解释

阅读题面发现，如果将数字看成字符串，那么这就是需要完成一个多模匹配，自然而然就想到 AC 自动机．普通数位 DP 中，先从高到低枚举数位，再枚举每一位都填什么，在这道题中，我们也就自然地转化为枚举已经填好的位数，再枚举此时停在 AC 自动机上的哪个节点，然后从当前节点转移到它在 AC 自动机上的子节点．

设 𝑓(𝑖,𝑗,0/1)f(i,j,0/1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示当前从高到低已经填了 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位（即在 AC 自动机上走过了 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边），此时停在标号为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的节点上，当前是否正好贴着上界．

至于题目中的「不包含」条件，只需在 AC 自动机上给每个模式串的结尾节点都打上标记，DP 过程中一旦遇上这些结尾节点就跳过即可．

转移很好想，详见代码主函数部分．

### 实现

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 ``` |  ```text #include <cstdio> #include <cstring> #include <queue> using namespace std ; using ll = long long ; constexpr int N = 1505 ; constexpr int mod = 1000000007 ; int n , m ; char s [ N ], c [ N ]; int ch [ N ][ 10 ], fail [ N ], ed [ N ], tot , len ; void insert () { int now = 0 ; int L = strlen ( s ); for ( int i = 0 ; i < L ; ++ i ) { if ( ! ch [ now ][ s [ i ] \- '0' ]) ch [ now ][ s [ i ] \- '0' ] = ++ tot ; now = ch [ now ][ s [ i ] \- '0' ]; } ed [ now ] = 1 ; } queue < int > q ; void build () { for ( int i = 0 ; i < 10 ; ++ i ) if ( ch [ 0 ][ i ]) q . push ( ch [ 0 ][ i ]); while ( ! q . empty ()) { int u = q . front (); q . pop (); for ( int i = 0 ; i < 10 ; ++ i ) { if ( ch [ u ][ i ]) { fail [ ch [ u ][ i ]] = ch [ fail [ u ]][ i ], q . push ( ch [ u ][ i ]), ed [ ch [ u ][ i ]] |= ed [ fail [ ch [ u ][ i ]]]; } else ch [ u ][ i ] = ch [ fail [ u ]][ i ]; } } ch [ 0 ][ 0 ] = 0 ; } ll f [ N ][ N ][ 2 ], ans ; void add ( ll & x , ll y ) { x = ( x \+ y ) % mod ; } int main () { scanf ( "%s" , c ); n = strlen ( c ); scanf ( "%d" , & m ); for ( int i = 1 ; i <= m ; ++ i ) scanf ( "%s" , s ), insert (); build (); f [ 0 ][ 0 ][ 1 ] = 1 ; for ( int i = 0 ; i < n ; ++ i ) { for ( int j = 0 ; j <= tot ; ++ j ) { if ( ed [ j ]) continue ; for ( int k = 0 ; k < 10 ; ++ k ) { if ( ed [ ch [ j ][ k ]]) continue ; add ( f [ i \+ 1 ][ ch [ j ][ k ]][ 0 ], f [ i ][ j ][ 0 ]); if ( k < c [ i ] \- '0' ) add ( f [ i \+ 1 ][ ch [ j ][ k ]][ 0 ], f [ i ][ j ][ 1 ]); if ( k == c [ i ] \- '0' ) add ( f [ i \+ 1 ][ ch [ j ][ k ]][ 1 ], f [ i ][ j ][ 1 ]); } } } for ( int j = 0 ; j <= tot ; ++ j ) { if ( ed [ j ]) continue ; add ( ans , f [ n ][ j ][ 0 ]); add ( ans , f [ n ][ j ][ 1 ]); } printf ( "%lld \n " , ans \- 1 ); return 0 ; } ```   
---|---  
  
此题可以很好地帮助理解数位 DP 的原理．

## 习题

[Ahoi2009 self 同类分布](https://www.luogu.com.cn/problem/P4127)

[洛谷 P3413 SAC#1 - 萌数](https://www.luogu.com.cn/problem/P3413)

[HDU 6148 Valley Number](https://acm.hdu.edu.cn/showproblem.php?pid=6148)

[CF55D Beautiful numbers](http://codeforces.com/problemset/problem/55/D)

[CF628D Magic Numbers](http://codeforces.com/problemset/problem/628/D)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/dp/number.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/dp/number.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [greyqz](https://github.com/greyqz), [hsfzLZH1](https://github.com/hsfzLZH1), [c-forrest](https://github.com/c-forrest), [Early0v0](https://github.com/Early0v0), [Henry-ZHR](https://github.com/Henry-ZHR), [ksyx](https://github.com/ksyx), [Marcythm](https://github.com/Marcythm), [ouuan](https://github.com/ouuan), [StudyingFather](https://github.com/StudyingFather), [Xeonacid](https://github.com/Xeonacid), [alphagocc](https://github.com/alphagocc), [Alphnia](https://github.com/Alphnia), [billchenchina](https://github.com/billchenchina), [ChungZH](https://github.com/ChungZH), [Enter-tainer](https://github.com/Enter-tainer), [GavinZhengOI](https://github.com/GavinZhengOI), [H-J-Granger](https://github.com/H-J-Granger), [iamtwz](https://github.com/iamtwz), [isdanni](https://github.com/isdanni), [NachtgeistW](https://github.com/NachtgeistW), [Promise2679](https://github.com/Promise2679), [r-value](https://github.com/r-value), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [thredreams](https://github.com/thredreams)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
