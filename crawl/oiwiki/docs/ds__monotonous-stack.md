# 单调栈 - OI Wiki

- Source: https://oi-wiki.org/ds/monotonous-stack/

# 单调栈

## 引入

何为单调栈？顾名思义，单调栈即满足单调性的栈结构．与单调队列相比，其只在一端进行进出．

为了描述方便，以下举例及伪代码以维护一个整数的单调递增栈为例．

## 过程

### 插入

将一个元素插入单调栈时，为了维护栈的单调性，需要在保证将该元素插入到栈顶后整个栈满足单调性的前提下弹出最少的元素．

例如，栈中自顶向下的元素为 {0,11,45,81}{0,11,45,81}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

![](./images/monotonous-stack-before.svg)

插入元素 1414![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时为了保证单调性需要依次弹出元素 0,110,11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，操作后栈变为 {14,45,81}{14,45,81}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

![](./images/monotonous-stack-after.svg)

用伪代码描述如下：

实现

```text 1 2 3 4 ``` |  ```text insert x while !sta.empty() && sta.top()<x sta.pop() sta.push(x) ```   
---|---  
  
### 使用

自然就是从栈顶读出来一个元素，该元素满足单调性的某一端．

例如举例中取出的即栈中的最小值．

## 应用

[POJ3250 Bad Hair Day](http://poj.org/problem?id=3250)

有 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 头牛从左到右排成一排，每头牛有一个高度 ℎ𝑖hi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设左数第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 头牛与「它右边第一头高度 ≥ℎ𝑖≥hi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」的牛之间有 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 头牛，试求 ∑𝑁𝑖=1𝑐𝑖∑i=1Nci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

比较基础的应用有这一题，就是个单调栈的简单应用，记录每头牛被弹出的位置，如果没有被弹出过则为最远端，稍微处理一下即可计算出题目所需结果．

另外，单调栈也可以用于离线解决 RMQ 问题．

我们可以把所有询问按右端点排序，然后每次在序列上从左往右扫描到当前询问的右端点处，并把扫描到的元素插入到单调栈中．这样，每次回答询问时，单调栈中存储的值都是位置 ≤𝑟≤r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的、可能成为答案的决策点，并且这些元素满足单调性质．此时，单调栈上第一个位置 ≥𝑙≥l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素就是当前询问的答案，这个过程可以用二分查找实现．使用单调栈解决 RMQ 问题的时间复杂度为 𝑂(𝑞log⁡𝑞 +𝑞log⁡𝑛)O(qlog⁡q+qlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，空间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 习题

  * [洛谷 P5788【模板】单调栈](https://www.luogu.com.cn/problem/P5788)
  * [洛谷 P1901 发射站](https://www.luogu.com.cn/problem/P1901)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/monotonous-stack.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/monotonous-stack.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Enter-tainer](https://github.com/Enter-tainer), [ksyx](https://github.com/ksyx), [Xeonacid](https://github.com/Xeonacid), [ChungZH](https://github.com/ChungZH), [countercurrent-time](https://github.com/countercurrent-time), [iamtwz](https://github.com/iamtwz), [mcendu](https://github.com/mcendu), [Planet6174](https://github.com/Planet6174), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
