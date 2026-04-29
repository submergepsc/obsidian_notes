# 主元素问题 - OI Wiki

- Source: https://oi-wiki.org/misc/main-element/

# 主元素问题

## 问题介绍

给一个有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的序列，保证有一个元素 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出现的次数 **严格大于** 𝑛/2n/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求这个元素．

## 做法

### 离线算法

若一开始就可以知道整个序列，一个自然的思路是统计序列中各元素的出现次数，出现次数大于 𝑛/2n/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的就是主元素．可以创建一个桶来统计每种元素的出现次数，输出出现次数大于 𝑛/2n/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素即可．

但上述方案引入了桶进行统计，空间效率并不优．显然，若序列存在主元素，那么在排序后，序列的第 ⌊𝑛/2⌋ +1⌊n/2⌋+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素一定是主元素，利用 [`nth_element`](https://en.cppreference.com/w/cpp/algorithm/nth_element.html) 就可以找到这个元素．这样我们就在不引入额外空间的情况下，以线性时间复杂度求得主元素了．

### 在线算法

在一些情况下，我们需要在线处理流式数据，此时我们需要一种不需要预知全体数据，而是只利用当前给出的数据逐步求得答案的算法．**多数投票算法** 1就是一种可以在线解决主元素问题的算法．

由于主元素的出现的次数超过 𝑛/2n/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么对于一个完整的序列，在不断消掉一个主元素和一个与主元素不同的元素之后，最后一定剩下主元素．借助这个观察，我们可以设计一个在线算法进行这样的消除操作．设 `val` 和 `cnt` 两个变量分别代表当前的主元素候选和目前如果进行了这样的消除操作后主元素候选会剩多少个．初始时 `cnt` 置为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．每次从数据流中取出一个元素，如果当前 `cnt` 为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则代表主元素候选已经被消除完了，当前记录的 `val` 一定不是主元素，因此设置当前元素为主元素候补．之后检查当前元素是否是主元素候补，如果是，则 `cnt` 增加 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果不是，则该元素应与一个主元素候补一起消除，`cnt` 减少 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．重复上述操作直到数据流读取完成，`val` 即为主元素．

注意

当原数据中不存在主元素时，此算法给出的结果是错误的．如要判断序列中是否存在主元素，需要再次读入数据流，统计 `val` 出现次数，判断其是否超过 𝑛/2n/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

为了再次读入数据流，可以选择重置输入位置指示器，可利用 [`std::basic_istream<CharT,Traits>::seekg`](https://en.cppreference.com/w/cpp/io/basic_istream/seekg)（流式输入）或 [`rewind`](https://en.cppreference.com/w/c/io/rewind)、[`fseek`](https://en.cppreference.com/w/c/io/fseek)（C 风格输入）等库函数．

## 例题

[洛谷 P2397 yyy loves Maths VI (mode)](https://www.luogu.com.cn/problem/P2397)

求给定序列的主元素．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text #include <cstdio> int main () { int n ; scanf ( "%d" , & n ); int val , cnt = 0 ; while ( n \-- ) { int x ; scanf ( "%d" , & x ); if ( ! cnt ) val = x ; ( val == x ) ? ++ cnt : \-- cnt ; } printf ( "%d \n " , val ); return 0 ; } ```   
---|---  
  
[LeetCode 229. 多数元素 II](https://leetcode.cn/problems/majority-element-ii)

给定一个大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数数组，找出其中所有出现超过 ⌊𝑛/3⌋⌊n/3⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次的元素．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` |  ```text class Solution { public : vector < int > majorityElement ( vector < int >& nums ) { // 将多数投票算法的「抵消2个不同元素」变为「抵消3个两两不同的元素」 int maj1 , maj2 ; int cnt1 = 0 , cnt2 = 0 ; for ( int num : nums ) { if ( num == maj1 ) { ++ cnt1 ; } else if ( num == maj2 ) { ++ cnt2 ; } else if ( cnt1 == 0 ) { maj1 = num ; ++ cnt1 ; } else if ( cnt2 == 0 ) { maj2 = num ; ++ cnt2 ; } else { \-- cnt1 ; \-- cnt2 ; } } // 由于题目没有保证存在2个超过 ⌊ n/3 ⌋ 次的元素，故需检验 vector < int > ans ; cnt1 = 0 , cnt2 = 0 ; for ( int num : nums ) { if ( num == maj1 ) ++ cnt1 ; else if ( num == maj2 ) ++ cnt2 ; } int n = nums . size (); if ( cnt1 > n / 3 ) ans . push_back ( maj1 ); if ( cnt2 > n / 3 ) ans . push_back ( maj2 ); return ans ; } }; ```   
---|---  
  
## 参考资料

* * *

  1. [多数投票算法 - 维基百科](https://zh.wikipedia.org/zh-cn/%E5%A4%9A%E6%95%B0%E6%8A%95%E7%A5%A8%E7%AE%97%E6%B3%95) ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/main-element.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/main-element.md "edit.link.title")  
>  __本页面贡献者：[Enter-tainer](https://github.com/Enter-tainer), [Early0v0](https://github.com/Early0v0), [Ethkuil](https://github.com/Ethkuil), [HeRaNO](https://github.com/HeRaNO), [Tiphereth-A](https://github.com/Tiphereth-A), [Ir1d](https://github.com/Ir1d), [ksyx](https://github.com/ksyx), [SDLTF](https://github.com/SDLTF)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
