# Kahan 求和 - OI Wiki

- Source: https://oi-wiki.org/misc/kahan-summation/

# Kahan 求和

## 引入

**Kahan 求和** 算法，又名补偿求和或进位求和算法，是一个用来 **降低有限精度浮点数序列累加值误差** 的算法．它主要通过保持一个单独变量用来累积误差（常用变量名为 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）来完成的．

该算法主要由 William Kahan 于 1960s 发现．因为 Ivo Babuška 也曾独立提出了一个类似的算法，Kahan 求和算法又名为 Kahan–Babuška 求和算法．

## 舍入误差

在计算机程序中，我们需要用有限位数对实数做近似表示，如今的大多数计算机都使用 [IEEE-754](https://en.wikipedia.org/wiki/IEEE_754) 规定的浮点数来作为这个近似表示．对于 1313![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由于我们不能在有限位数内对它进行精准表示，因此在使用 IEEE-754 表示法时，必须四舍五入一部分数值（truncate）．这种 **舍入误差** （Rounding off error）是浮点计算的一个特征．

在浮点加法计算中，交换律（commutativity）成立，但结合律（associativity）不成立．也就是说，𝑎 +𝑏 =𝑏 +𝑎a+b=b+a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 但 (𝑎 +𝑏) +𝑐 ≠𝑎 +(𝑏 +𝑐)(a+b)+c≠a+(b+c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此在浮点序列加法计算中，我们可以从左到右一个个累加，也可以在原有顺序上，将他们两两分成一对．第二种算法会相对较慢并需要更多内存，也常被一些语言的特定求和函数使用，但相对结果更准确．

为了得到更准确的浮点累加结果，我们需要使用 Kahan 求和算法．

在计算 𝑆𝑛𝑒𝑤 =𝑆𝑜𝑙𝑑 +𝑎Snew=Sold+a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为浮点序列的一个数值）时，定义实际计算加入 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值为 𝑎𝑒𝑓𝑓 =𝑆𝑛𝑒𝑤 −𝑆𝑜𝑙𝑑aeff=Snew−Sold![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 如果 𝑎𝑒𝑓𝑓aeff![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大，则证明有向上舍入误差；如果 𝑎𝑒𝑓𝑓aeff![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小，则证明有向下舍入误差．则舍入误差定义为 𝐸𝑟𝑜𝑢𝑛𝑑𝑜𝑓𝑓 =𝑎𝑒𝑓𝑓 −𝑎Eroundoff=aeff−a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么用来纠正这部分舍入误差的值就为 𝑎 −𝑎𝑒𝑓𝑓a−aeff![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 即 𝐸𝑟𝑜𝑢𝑛𝑑𝑜𝑓𝑓Eroundoff![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的负值．定义 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是对丢失的低位进行运算补偿的变量，就可以得到 𝑐𝑛𝑒𝑤 =𝑐𝑜𝑙𝑑 +(𝑎 −𝑎𝑒𝑓𝑓)cnew=cold+(a−aeff)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 过程

Kahan 求和算法主要通过一个单独变量用来累积误差．如下方参考代码所示，𝑠𝑢𝑚sum![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为最终返回的累加结果．𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是对丢失的低位进行运算补偿的变量（其被舍去的部分），也是 Kahan 求和算法中的必要变量．

因为 𝑠𝑢𝑚sum![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大，𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小，所以 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的低位数丢失．(𝑡 −𝑠𝑢𝑚)(t−sum)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 抵消了 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的高阶部分，减去 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则会恢复负值（𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的低价部分）．因此代数值中 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 始终为零．在下一轮迭代中，丢失的低位部分会被更新添加到 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 实现

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text float kahanSum ( vector < float > nums ) { float sum = 0.0f ; float c = 0.0f ; for ( auto num : nums ) { float y = num \- c ; float t = sum \+ y ; c = ( t \- sum ) \- y ; sum = t ; } return sum ; } ```   
---|---  
  
## 习题

在 OI 中，Kahan 求和主要作为辅助工具存在，为计算结果提供误差更小的值．

例题 [CodeForces Contest 800 Problem A. Voltage Keepsake](https://codeforces.com/contest/800/problem/A)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个同时使用的设备．第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个设备每秒使用 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单位的功率．这种用法是连续的．也就是说，在 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 秒内，设备将使用 𝜆 ×𝑎𝑖λ×ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单位的功率．第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个设备当前存储了 𝑏𝑖bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单位的电力．所有设备都可以存储任意数量的电量．有一个可以插入任何单个设备的充电器．充电器每秒会为设备增加 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个单位的电量．这种充电是连续的．也就是说，如果将设备插入 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 秒，它将获得 𝜆 ×𝑝λ×p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单位的功率．我们可以在任意时间单位内（包括实数）切换哪个设备正在充电（切换所需时间忽略不计）．求其中一个设备达到 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单位功率前，可以使用这些设备的最长时间．

例题 [CodeForces Contest 504 Problem B. Misha and Permutations Summation](https://codeforces.com/problemset/problem/504/B)

定义数字 0,1,⋯,(𝑛 −1)0,1,⋯,(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的两个排列 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的和为 𝑃𝑒𝑟𝑚((𝑂𝑟𝑑(𝑝) +𝑂𝑟𝑑(𝑞))mod𝑛!)Perm((Ord(p)+Ord(q))modn!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑃𝑒𝑟𝑚(𝑥)Perm(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是数字 0,1,⋯,(𝑛 −1)0,1,⋯,(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字典排列（从零开始计数），𝑂𝑟𝑑(𝑝)Ord(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是字典序排列 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数．例如，𝑃𝑒𝑟𝑚(0) =(0,1,⋯,𝑛 −2,𝑛 −1)Perm(0)=(0,1,⋯,n−2,n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑃𝑒𝑟𝑚(𝑛! −1) =(𝑛 −1,𝑛 −2,⋯,1,0))Perm(n!−1)=(n−1,n−2,⋯,1,0))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．Misha 有两个排列 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，找到它们的总和．

## 编程语言的求和

Python 的标准库指定了精确舍入求和的 [fsum](https://docs.python.org/3/library/math.html#math.fsum) 函数可用于返回可迭代对象中值的准确浮点总和，它通过使用 Shewchuk 算法跟踪多个中间部分和来避免精度损失．

Julia 语言中，[sum](https://docs.julialang.org/en/v1/base/collections/#Base.sum) 函数的默认实现是成对求和，以获得高精度和良好的性能．同时外部库函数 [sum_kbn](http://www.jlhub.com/julia/manual/en/function/sum_kbn) 为需要更高精度的情况提供了 Neumaier 变体的实现，具体可见 [KahanSummation.jl](https://github.com/JuliaMath/KahanSummation.jl)．

## 参考资料与注释

  1. [Kahan_summation_algorithm - Wikipedia](https://en.wikipedia.org/wiki/Kahan_summation_algorithm)
  2. [Kahan summation - Rosetta Code](https://rosettacode.org/wiki/Kahan_summation)
  3. [VK Cup Round 2 + Codeforces Round 409 Announcement](https://codeforces.com/blog/entry/51577)
  4. [Rounding off errors in Java - GeeksforGeeks](https://www.geeksforgeeks.org/rounding-off-errors-java/)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/kahan-summation.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/kahan-summation.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [iamtwz](https://github.com/iamtwz), [isdanni](https://github.com/isdanni), [StudyingFather](https://github.com/StudyingFather)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
