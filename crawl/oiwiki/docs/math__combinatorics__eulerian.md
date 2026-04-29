# Eulerian Number - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/eulerian/

# Eulerian Number

注意

下文中的欧拉数特指 Eulerian number．注意与 Euler number，以及 Euler's number（指与欧拉相关的数学常数例如 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 ee![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）作区分．

在计算组合中，**欧拉数** （Eulerian Number）是从 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中正好满足 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素大于前一个元素（具有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个「上升」的排列）条件的排列 **个数** ．定义为：

𝐴(𝑛,𝑚)=⟨𝑛𝑚−1⟩A(n,m)=⟨nm−1⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

例如，从数字 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一共有 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种排列使得恰好有一个元素比前一个元素大：

排列| 满足条件的相邻元素| 个数  
---|---|---  
1 2 3| 1, 2 & 2, 3| 2  
1 3 2| 1, 3| 1  
2 1 3| 1, 3| 1  
2 3 1| 2, 3| 1  
3 1 2| 1, 2| 1  
3 2 1| | 0  
  
所以按照 𝐴(𝑛,𝑚)A(n,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 定义：如果 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等于 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，欧拉数值为 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示共有 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个有 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素大于前一个元素的排列．

对于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值比较小的欧拉数来说，我们可以直接得到结果：

𝐴(𝑛,𝑚)A(n,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 满足要求的排列| 个数  
---|---|---  
𝐴(1,0)A(1,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| (1)(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1  
𝐴(2,0)A(2,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| (2,1)(2,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1  
𝐴(2,1)A(2,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| (1,2)(1,2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1  
𝐴(3,0)A(3,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| (3,2,1)(3,2,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1  
𝐴(3,1)A(3,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| (1,3,2),(2,1,3),(2,3,1),(3,1,2)(1,3,2),(2,1,3),(2,3,1),(3,1,2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 4  
𝐴(3,2)A(3,2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| (1,2,3)(1,2,3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 1  
  
## 公式

可以通过递推或者递归的方法计算欧拉数．

首先，当 𝑚 ≥𝑛m≥n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑛 =0n=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，没有满足条件的排列，即此时欧拉数为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

其次，当 𝑚 =0m=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，只有降序的排列满足条件，即此时欧拉数为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最后，考虑在 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的排列的基础上插入 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 从而得到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的排列，由于插入 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至多使欧拉数增加 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝐴(𝑛,𝑚)A(n,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以仅从 𝐴(𝑛 −1,𝑚 −1)A(n−1,m−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处和 𝐴(𝑛 −1,𝑚)A(n−1,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处转移得到．

考虑 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 插入的位置：当 𝑝𝑖−1 <𝑝𝑖pi−1<pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，若将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 插到 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之前，即将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 插入到「上升」中，排列的欧拉数不变；此外，将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 插在排列之前，排列的欧拉数也不变；否则，若将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 插到其余位置，排列的欧拉数增加 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑从 𝐴(𝑛 −1,𝑚 −1)A(n−1,m−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转移到 𝐴(𝑛,𝑚)A(n,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时需要使欧拉数增加 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时不能将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 插在「上升」中或者排列开头，共有 𝑛 −(𝑚 −1) −1 =𝑛 −𝑚n−(m−1)−1=n−m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种方案．

考虑从 𝐴(𝑛 −1,𝑚)A(n−1,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转移到 𝐴(𝑛,𝑚)A(n,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时需要欧拉数保持不变，只能将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 插在「上升」中或者排列开头，共 𝑚 +1m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种方案．

综上所述，有

𝐴(𝑛,𝑚)=⎧{ {⎨{ {⎩0,𝑚>𝑛 or 𝑛=0,1,𝑚=0,(𝑛−𝑚)⋅𝐴(𝑛−1,𝑚−1)+(𝑚+1)⋅𝐴(𝑛−1,𝑚),otherwise.A(n,m)={0,m>n or n=0,1,m=0,(n−m)⋅A(n−1,m−1)+(m+1)⋅A(n−1,m),otherwise.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 实现

C++Python

```text 1 2 3 4 5 6 ``` |  ```text int eulerianNumber ( int n , int m ) { if ( m >= n || n == 0 ) return 0 ; if ( m == 0 ) return 1 ; return ((( n \- m ) * eulerianNumber ( n \- 1 , m \- 1 )) \+ (( m \+ 1 ) * eulerianNumber ( n \- 1 , m ))); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text def eulerianNumber ( n , m ): if m >= n or n == 0 : return 0 if m == 0 : return 1 return (( n \- m ) * eulerianNumber ( n \- 1 , m \- 1 )) \+ ( ( m \+ 1 ) * eulerianNumber ( n \- 1 , m ) ) ```   
---|---  
  
## 习题

  * [CF1349F1 Slime and Sequences (Easy Version)](https://codeforces.com/problemset/problem/1349/F1)
  * [CF1349F2 Slime and Sequences (Hard Version)](https://codeforces.com/problemset/problem/1349/F2)
  * [UOJ 593. 新年的军队](https://uoj.ac/problem/593)
  * [P7511 三到六](https://www.luogu.com.cn/problem/P7511)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/eulerian.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/eulerian.md "edit.link.title")  
>  __本页面贡献者：[ksyx](https://github.com/ksyx), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [isdanni](https://github.com/isdanni), [Xeonacid](https://github.com/Xeonacid), [Backl1ght](https://github.com/Backl1ght), [CCXXXI](https://github.com/CCXXXI), [ChungZH](https://github.com/ChungZH), [HeRaNO](https://github.com/HeRaNO), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [Konano](https://github.com/Konano), [Menci](https://github.com/Menci), [mgt](mailto:i@margatroid.xyz), [shawlleyw](https://github.com/shawlleyw), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [thredreams](https://github.com/thredreams), [XuYueming520](https://github.com/XuYueming520), [xyf007](https://github.com/xyf007)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
