# 平衡三进制 - OI Wiki

- Source: https://oi-wiki.org/math/numeral-sys/balanced-ternary/

# 平衡三进制

## 定义

平衡三进制，也称为对称三进制．这是一个广义进位系统．

正规的三进制的数字都是由 `0`,`1`,`2` 构成的，而平衡三进制的数字是由 `-1`,`0`,`1` 构成的．它的基数也是 `3`（因为有三个可能的值）．由于将 `-1` 写成数字不方便，我们将使用字母 `Z` 来代替 `-1`．

## 解释

这里有几个例子：

十进制| 平衡三进制| 十进制| 平衡三进制  
---|---|---|---  
`0`| `0`| `5`| `1ZZ`  
`1`| `1`| `6`| `1Z0`  
`2`| `1Z`| `7`| `1Z1`  
`3`| `10`| `8`| `10Z`  
`4`| `11`| `9`| `100`  
  
该数字系统的负数表示起来很容易：只需要将正数的数字倒转即可（`Z` 变成 `1`,`1` 变成 `Z`）．

十进制| 平衡三进制  
---|---  
`-1`| `Z`  
`-2`| `Z1`  
`-3`| `Z0`  
`-4`| `ZZ`  
`-5`| `Z11`  
  
很容易就可以看到，负数最高位是 `Z`，正数最高位是 `1`．

## 过程

在平衡三进制的转转换法中，需要先写出一个给定的数 `x` 在标准三进制中的表示．当 `x` 是用标准三进制表示时，其数字的每一位都是 `0`、`1` 或 `2`．从最低的数字开始迭代，我们可以先跳过任何的 `0` 和 `1`，但是如果遇到 `2` 就应该先将其变成 `Z`，下一位数字再加上 `1`．而遇到数字 `3` 则应该转换为 `0` 下一位数字再加上 `1`．

### 应用一

把 `64` 转换成平衡三进制．

首先，我们用标准三进制数来重写这个数：

6410=0210136410=021013![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

让我们从对整个数影响最小的数字（最低位）进行处理：

  * `101` 被跳过（因为在平衡三进制中允许 `0` 和 `1`）；
  * `2` 变成了 `Z`，它左边的数字加 `1`，得到 `1Z101`；
  * `1` 被跳过，得到 `1Z101`．

最终的结果是 `1Z101`．

我们再把它转换回十进制：

𝟷𝚉𝟷𝟶𝟷=81×1+27×(−1)+9×1+3×0+1×1=64101Z101=81×1+27×(−1)+9×1+3×0+1×1=6410![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 应用二

把 `237` 转换成平衡三进制．

首先，我们用标准三进制数来重写这个数：

23710=22210323710=222103![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * `0` 和 `1` 被跳过（因为在平衡三进制中允许 `0` 和 `1`）；
  * `2` 变成 `Z`，左边的数字加 `1`，得到 `23Z10`；
  * `3` 变成 `0`，左边的数字加 `1`，得到 `30Z10`；
  * `3` 变成 `0`，左边的数字（默认是 `0`）加 `1`，得到 `100Z10`；
  * `1` 被跳过，得到 `100Z10`．

最终的结果是 `100Z10`．

我们再把它转换回十进制：

𝟷𝟶𝟶𝚉𝟷𝟶=243⋅1+81⋅0+27⋅0+9⋅(−1)+3⋅1+1⋅0=23710100Z10=243⋅1+81⋅0+27⋅0+9⋅(−1)+3⋅1+1⋅0=23710![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 性质

对于一个平衡三进制数 𝑋3X3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来说，其可以按照每一位 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 乘上对应的权值 3𝑖3i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来唯一得到一个十进制数 𝑌10Y10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

那对于一个十进制数 𝑌10Y10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，是否 **唯一对应一个平衡三进制数** 呢？

答案是肯定的，这种性质被叫做平衡三进制的唯一性．

证明

我们利用 **反证法** 来求证：

假设一个十进制数 𝑌10Y10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，存在两个 **不同的平衡三进制数** 𝐴3,𝐵3A3,B3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转化成十进制时等于 𝑌10Y10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即证 𝐴3 =𝐵3A3=B3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．分情况讨论：

  1. 当 𝑌10 =0Y10=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，显然 𝐴3 =𝐵3 =03A3=B3=03![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，与假设矛盾．
  2. 当 𝑌10 >0Y10>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

     * 将 𝐴3A3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵3B3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数位按低位到高位编号，记 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝐴3A3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位，𝑏𝑖bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位．在 𝐴3,𝐵3A3,B3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，必存在 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑎𝑖 ≠𝑏𝑖ai≠bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．可以发现第 𝑖 −1,𝑖 −2,…,0i−1,i−2,…,0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位均与证明无关．因此，将 𝐴3,𝐵3A3,B3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 按位右移 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位，得到 𝐴′3,𝐵′3A3′,B3′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，原问题等价于证明 𝐴′3 =𝐵′3A3′=B3′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
     * 对于 𝐴′3,𝐵′3A3′,B3′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 第 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位，𝑎0 ≠𝑏0a0≠b0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．假设 𝑏0 >𝑎0b0>a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑎0 >𝑏0a0>b0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时结果相同），易知 𝑏0 −𝑎0 ∈{1,2}b0−a0∈{1,2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝐴′3A3′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位 𝑖 =1,2,3,…i=1,2,3,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于 𝐴′3A3′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值的贡献为 𝑆1 =𝑎1 ×31 +𝑎2 ×32 +…S1=a1×31+a2×32+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵′3B3′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位 𝑖 =1,2,3,…i=1,2,3,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于 𝐵′3B3′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值的贡献为 𝑆2 =𝑏1 ×31 +𝑏2 ×32 +…S2=b1×31+b2×32+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于 𝐴′3 =𝐵′3A3′=B3′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得 𝑆1 −𝑆2 =𝑏0 −𝑎0S1−S2=b0−a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝑆1,𝑆2S1,S2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有公因子 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而 𝑏0 −𝑎0b0−a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不能被 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除，与假设矛盾，因此 𝐴′3 ≠𝐵′3A3′≠B3′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. 当 𝑌10 <0Y10<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，证法与 𝑌10 >0Y10>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相同．

故对于任意十进制 𝑌10Y10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，均有唯一对应的平衡三进制 𝑋3X3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 练习题

[Topcoder SRM 604 PowerOfThree](https://archive.topcoder.com/ProblemStatement/pm/12917)

**本页面部分内容译自博文[Троичная сбалансированная система счисления](http://e-maxx.ru/algo/balanced_ternary) 与其英文翻译版 [Balanced Ternary](https://cp-algorithms.com/algebra/balanced-ternary.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/1/30 14:50:40，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/numeral-sys/balanced-ternary.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/numeral-sys/balanced-ternary.md "edit.link.title")  
>  __本页面贡献者：[Yanjun-Zhao](https://github.com/Yanjun-Zhao), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [Falicitas](https://github.com/Falicitas), [HeRaNO](https://github.com/HeRaNO), [iamtwz](https://github.com/iamtwz), [ImpleLee](https://github.com/ImpleLee), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
