# 快速沃尔什变换 - OI Wiki

- Source: https://oi-wiki.org/math/poly/fwt/

# 快速沃尔什变换

## 简介

沃尔什转换（Walsh Transform）1是在频谱分析上作为离散傅立叶变换的替代方案的一种方法，在信号处理中应用很广泛．FFT 是 double 类型的，但是 Walsh 把信号在不同震荡频率方波下拆解，因此所有的系数都是绝对值大小相同的整数，这使得不需要作浮点数的乘法运算，提高了运算速度．

所以，FWT 和 FFT 的核心思想应该是相同的，都是对数组的变换．我们记对数组 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行快速沃尔什变换后得到的结果为 𝐹𝑊𝑇[𝐴]FWT[A]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

那么 FWT 核心思想就是：

我们需要一个新序列 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由序列 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和序列 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 经过某运算规则得到，即 𝐶 =𝐴 ⋅𝐵C=A⋅B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；

我们先正向得到序列 𝐹𝑊𝑇[𝐴],𝐹𝑊𝑇[𝐵]FWT[A],FWT[B]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再根据 𝐹𝑊𝑇[𝐶] =𝐹𝑊𝑇[𝐴] ⋅𝐹𝑊𝑇[𝐵]FWT[C]=FWT[A]⋅FWT[B]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度内求出 𝐹𝑊𝑇[𝐶]FWT[C]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 ⋅⋅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是序列对应位置相乘；

然后逆向运算得到原序列 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．时间复杂度为 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在算法竞赛中，FWT 是用于解决对下标进行位运算卷积问题的方法．

公式：𝐶𝑖 =∑𝑖=𝑗⊕𝑘𝐴𝑗𝐵𝑘Ci=∑i=j⊕kAjBk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

（其中 ⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是二元位运算中的某一种）

下面我们举 ∪∪![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（按位或）、∩∩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（按位与）和 ⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（按位异或）为例．

## FWT 的运算

### 或运算

如果有 𝑘 =𝑖 ∪𝑗k=i∪j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制位为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置和 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制位为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置肯定是 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制位为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置的子集．

现在要得到 𝐹𝑊𝑇[𝐶] =𝐹𝑊𝑇[𝐴] ⋅𝐹𝑊𝑇[𝐵]FWT[C]=FWT[A]⋅FWT[B]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们就要构造这个 FWT 的规则．

我们按照定义，显然可以构造 𝐹𝑊𝑇[𝐴]𝑖 =𝐴′𝑖 =∑𝑖=𝑖∪𝑗𝐴𝑗FWT[A]i=Ai′=∑i=i∪jAj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，来表示 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足二进制中 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集．

那么有：

𝐹𝑊𝑇[𝐴]𝑖⋅𝐹𝑊𝑇[𝐵]𝑖=(∑𝑖∪𝑗=𝑖𝐴𝑗)(∑𝑖∪𝑘=𝑖𝐵𝑘)=∑𝑖∪𝑗=𝑖∑𝑖∪𝑘=𝑖𝐴𝑗𝐵𝑘=∑𝑖∪(𝑗∪𝑘)=𝑖𝐴𝑗𝐵𝑘=𝐹𝑊𝑇[𝐶]𝑖FWT[A]i⋅FWT[B]i=(∑i∪j=iAj)(∑i∪k=iBk)=∑i∪j=i∑i∪k=iAjBk=∑i∪(j∪k)=iAjBk=FWT[C]i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么我们接下来看 𝐹𝑊𝑇[𝐴]FWT[A]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 怎么求．

首先肯定不能枚举了，复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．既然不能整体枚举，我们就考虑分治．

我们把整个区间二分，其实二分区间之后，下标写成二进制形式是有规律可循的．

我们令 𝐴0A0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前一半，𝐴1A1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示区间的后一半，那么 𝐴0A0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是 A 下标最大值的最高位为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，他的子集就是他本身的子集（因为最高位为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 了），但是 𝐴1A1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最高位是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，他满足条件的子集不仅仅是他本身，还包最高位为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集，即

𝐹𝑊𝑇[𝐴]=𝑚𝑒𝑟𝑔𝑒(𝐹𝑊𝑇[𝐴0],𝐹𝑊𝑇[𝐴0]+𝐹𝑊𝑇[𝐴1])FWT[A]=merge(FWT[A0],FWT[A0]+FWT[A1])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 merge 表示像字符串拼接一样把两个数组拼起来，++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是普通加法，表示对应二进制位相加．

这样我们就通过二分能在 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度内完成拼接，每次拼接的时候要完成一次运算，也就是说在 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度得到了 𝐹𝑊𝑇[𝐴]FWT[A]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

接下来就是反演了，其实反演是很简单的，既然知道了 𝐴0A0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的本身的子集是他自己（𝐴0 =𝐹𝑊𝑇[𝐴0]A0=FWT[A0]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），𝐴1A1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集是 𝐹𝑊𝑇[𝐴0] +𝐹𝑊𝑇[𝐴1]FWT[A0]+FWT[A1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那就很简单的得出反演的递推式了：

𝑈𝐹𝑊𝑇[𝐴′]=𝑚𝑒𝑟𝑔𝑒(𝑈𝐹𝑊𝑇[𝐴′0],𝑈𝐹𝑊𝑇[𝐴′1]−𝑈𝐹𝑊𝑇[𝐴′0])UFWT[A′]=merge(UFWT[A0′],UFWT[A1′]−UFWT[A0′])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

下面我们给出代码实现．容易发现顺变换和逆变换可以合并为一个函数，顺变换时 type =1type=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，逆变换时 type = −1type=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

实现

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text void Or ( ll * a , ll type ) { // 迭代实现，常数更小 for ( ll x = 2 ; x <= n ; x <<= 1 ) { ll k = x >> 1 ; for ( ll i = 0 ; i < n ; i += x ) { for ( ll j = 0 ; j < k ; j ++ ) { ( a [ i \+ j \+ k ] += a [ i \+ j ] * type ) %= P ; } } } } ```   
---|---  
  
### 与运算

与运算类比或运算可以得到类似结论

𝐹𝑊𝑇[𝐴]=𝑚𝑒𝑟𝑔𝑒(𝐹𝑊𝑇[𝐴0]+𝐹𝑊𝑇[𝐴1],𝐹𝑊𝑇[𝐴1])FWT[A]=merge(FWT[A0]+FWT[A1],FWT[A1])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑈𝐹𝑊𝑇[𝐴′]=𝑚𝑒𝑟𝑔𝑒(𝑈𝐹𝑊𝑇[𝐴′0]−𝑈𝐹𝑊𝑇[𝐴′1],𝑈𝐹𝑊𝑇[𝐴′1])UFWT[A′]=merge(UFWT[A0′]−UFWT[A1′],UFWT[A1′])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

下面我们给出代码实现．顺变换时 type =1type=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，逆变换时 type = −1type=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

实现

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text void And ( ll * a , ll type ) { for ( ll x = 2 ; x <= n ; x <<= 1 ) { ll k = x >> 1 ; for ( ll i = 0 ; i < n ; i += x ) { for ( ll j = 0 ; j < k ; j ++ ) { ( a [ i \+ j ] += a [ i \+ j \+ k ] * type ) %= P ; } } } } ```   
---|---  
  
### 异或运算

异或的卷积是基于如下原理：

若我们令 𝑥 ∘𝑦x∘y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑥 ∩𝑦x∩y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数量的奇偶性，即 𝑥 ∘𝑦 =popcnt(𝑥 ∩𝑦)mod2x∘y=popcnt(x∩y)mod2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么容易有 (𝑥 ∘𝑦) ⊕(𝑥 ∘𝑧) =𝑥 ∘(𝑦 ⊕𝑧)(x∘y)⊕(x∘z)=x∘(y⊕z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于 𝐹𝑊𝑇[𝐴]FWT[A]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的运算其实也很好得到．

设 𝐹𝑊𝑇[𝐴]𝑖 =∑𝑖∘𝑗=0𝐴𝑗 −∑𝑖∘𝑗=1𝐴𝑗FWT[A]i=∑i∘j=0Aj−∑i∘j=1Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们来证一下 𝐹𝑊𝑇[𝐶] =𝐹𝑊𝑇[𝐴] ⋅𝐹𝑊𝑇[𝐵]FWT[C]=FWT[A]⋅FWT[B]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正确性：

𝐹𝑊𝑇[𝐴]𝑖𝐹𝑊𝑇[𝐵]𝑖=(∑𝑖∘𝑗=0𝐴𝑗−∑𝑖∘𝑗=1𝐴𝑗)(∑𝑖∘𝑘=0𝐵𝑘−∑𝑖∘𝑘=1𝐵𝑘)=(∑𝑖∘𝑗=0𝐴𝑗∑𝑖∘𝑘=0𝐵𝑘+∑𝑖∘𝑗=1𝐴𝑗∑𝑖∘𝑘=1𝐵𝑘)−(∑𝑖∘𝑗=0𝐴𝑗∑𝑖∘𝑘=1𝐵𝑘+∑𝑖∘𝑗=1𝐴𝑗∑𝑖∘𝑘=0𝐵𝑘)=∑(𝑗⊕𝑘)∘𝑖=0𝐴𝑗𝐵𝑘−∑(𝑗⊕𝑘)∘𝑖=1𝐴𝑗𝐵𝑘=𝐹𝑊𝑇[𝐶]𝑖FWT[A]iFWT[B]i=(∑i∘j=0Aj−∑i∘j=1Aj)(∑i∘k=0Bk−∑i∘k=1Bk)=(∑i∘j=0Aj∑i∘k=0Bk+∑i∘j=1Aj∑i∘k=1Bk)−(∑i∘j=0Aj∑i∘k=1Bk+∑i∘j=1Aj∑i∘k=0Bk)=∑(j⊕k)∘i=0AjBk−∑(j⊕k)∘i=1AjBk=FWT[C]i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

来看看怎么快速计算 𝐴,𝐵A,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，依旧是分治：

对于 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在当前位为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子数列 𝐹𝑊𝑇[𝐴0]FWT[A0]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进行 ∘∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 运算时发现它和 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算或和 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算结果都不会变（因为 0 ∩0 =0,0 ∩1 =00∩0=0,0∩1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），所以 𝐹𝑊𝑇[𝐴] =∑𝑖∘𝑗=0𝐴𝑗 −∑𝑖∘𝑗=1𝐴𝑗FWT[A]=∑i∘j=0Aj−∑i∘j=1Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 ∑𝑖∘𝑗=1𝐴𝑗 =0∑i∘j=1Aj=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在当前位为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子数列 𝐴1A1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进行 ∘∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 运算时发现它和 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算结果是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，和 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算结果是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（因为 1 ∩0 =0,1 ∩1 =11∩0=0,1∩1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

综上，有：

𝐹𝑊𝑇[𝐴]=𝑚𝑒𝑟𝑔𝑒((𝐹𝑊𝑇[𝐴0]+𝐹𝑊𝑇[𝐴1])−0,𝐹𝑊𝑇[𝐴0]−𝐹𝑊𝑇[𝐴1])FWT[A]=merge((FWT[A0]+FWT[A1])−0,FWT[A0]−FWT[A1])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是：

𝐹𝑊𝑇[𝐴]=𝑚𝑒𝑟𝑔𝑒(𝐹𝑊𝑇[𝐴0]+𝐹𝑊𝑇[𝐴1],𝐹𝑊𝑇[𝐴0]−𝐹𝑊𝑇[𝐴1])FWT[A]=merge(FWT[A0]+FWT[A1],FWT[A0]−FWT[A1])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

逆变换易得：

𝑈𝐹𝑊𝑇[𝐴′]=𝑚𝑒𝑟𝑔𝑒(𝑈𝐹𝑊𝑇[𝐴′0]+𝑈𝐹𝑊𝑇[𝐴′1]2,𝑈𝐹𝑊𝑇[𝐴′0]−𝑈𝐹𝑊𝑇[𝐴′1]2)UFWT[A′]=merge(UFWT[A0′]+UFWT[A1′]2,UFWT[A0′]−UFWT[A1′]2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

给出代码，顺变换时 type =1type=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，逆变换时 type =12type=12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text void Xor ( ll * a , ll type ) { for ( ll x = 2 ; x <= n ; x <<= 1 ) { ll k = x >> 1 ; for ( ll i = 0 ; i < n ; i += x ) { for ( ll j = 0 ; j < k ; j ++ ) { ( a [ i \+ j ] += a [ i \+ j \+ k ]) %= P ; ( a [ i \+ j \+ k ] = a [ i \+ j ] \- a [ i \+ j \+ k ] * 2 ) %= P ; ( a [ i \+ j ] *= type ) %= P ; ( a [ i \+ j \+ k ] *= type ) %= P ; } } } } ```   
---|---  
  
### 同或运算

类比异或运算给出公式：

𝐹𝑊𝑇[𝐴]𝑖 =∑𝐶1𝐴𝑗 −∑𝐶2𝐴𝑗FWT[A]i=∑C1Aj−∑C2Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝐶1C1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 popcnt(𝑥 ∪𝑦)mod2popcnt(x∪y)mod2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐶2C2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 popcnt(𝑥 ∪𝑦)mod2popcnt(x∪y)mod2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

𝐹𝑊𝑇[𝐴]=𝑚𝑒𝑟𝑔𝑒(𝐹𝑊𝑇[𝐴1]−𝐹𝑊𝑇[𝐴0],𝐹𝑊𝑇[𝐴1]+𝐹𝑊𝑇[𝐴0])FWT[A]=merge(FWT[A1]−FWT[A0],FWT[A1]+FWT[A0])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑈𝐹𝑊𝑇[𝐴′]=𝑚𝑒𝑟𝑔𝑒(𝑈𝐹𝑊𝑇[𝐴′1]−𝑈𝐹𝑊𝑇[𝐴′0]2,𝑈𝐹𝑊𝑇[𝐴′1]+𝑈𝐹𝑊𝑇[𝐴′0]2)UFWT[A′]=merge(UFWT[A1′]−UFWT[A0′]2,UFWT[A1′]+UFWT[A0′]2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 另一个角度的 FWT

我们设 𝑐(𝑖,𝑗)c(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝐴𝑗Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对 𝐹𝑊𝑇[𝐴]𝑖FWT[A]i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的贡献系数．我们可以重新描述 FWT 变换的过程：

𝐹𝑊𝑇[𝐴]𝑖=𝑛−1∑𝑗=0𝑐(𝑖,𝑗)𝐴𝑗FWT[A]i=∑j=0n−1c(i,j)Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为有：

𝐹𝑊𝑇[𝐴]𝑖⋅𝐹𝑊𝑇[𝐵]𝑖=𝐹𝑊𝑇[𝐶]𝑖FWT[A]i⋅FWT[B]i=FWT[C]i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以我们可以通过简单的证明得到：𝑐(𝑖,𝑗)𝑐(𝑖,𝑘) =𝑐(𝑖,𝑗 ⊙𝑘)c(i,j)c(i,k)=c(i,j⊙k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．其中 ⊙⊙![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是任意一种位运算．

同时，𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 函数还有一个重要的性质，它可以按位处理．

举个例子，我们变换的时候：

𝐹𝑊𝑇[𝐴]𝑖=𝑛−1∑𝑗=0𝑐(𝑖,𝑗)𝐴𝑗FWT[A]i=∑j=0n−1c(i,j)Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这么做是比较劣的，我们将其拆分：

𝐹𝑊𝑇[𝐴]𝑖=𝑛/2−1∑𝑗=0𝑐(𝑖,𝑗)𝐴𝑗+𝑛−1∑𝑗=𝑛/2𝑐(𝑖,𝑗)𝐴𝑗FWT[A]i=∑j=0n/2−1c(i,j)Aj+∑j=n/2n−1c(i,j)Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

考虑前面的式子和后面的式子 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的区别，发现只有最高位不同．

所以我们将 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 去除最高位的值为 𝑖′,𝑗′i′,j′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并记 𝑖0i0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最高位．有：

𝐹𝑊𝑇[𝐴]𝑖=𝑐(𝑖0,0)𝑛/2−1∑𝑗=0𝑐(𝑖′,𝑗′)𝐴𝑗+𝑐(𝑖0,1)𝑛−1∑𝑗=𝑛/2𝑐(𝑖′,𝑗′)𝐴𝑗FWT[A]i=c(i0,0)∑j=0n/2−1c(i′,j′)Aj+c(i0,1)∑j=n/2n−1c(i′,j′)Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果 𝑖0 =0i0=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有：

𝐹𝑊𝑇[𝐴]𝑖=𝑐(0,0)𝑛/2−1∑𝑗=0𝑐(𝑖′,𝑗′)𝐴𝑗+𝑐(0,1)𝑛−1∑𝑗=𝑛/2𝑐(𝑖′,𝑗′)𝐴𝑗FWT[A]i=c(0,0)∑j=0n/2−1c(i′,j′)Aj+c(0,1)∑j=n/2n−1c(i′,j′)Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝑖0 =1i0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则有：

𝐹𝑊𝑇[𝐴]𝑖=𝑐(1,0)𝑛/2−1∑𝑗=0𝑐(𝑖′,𝑗′)𝐴𝑗+𝑐(1,1)𝑛−1∑𝑗=𝑛/2𝑐(𝑖′,𝑗′)𝐴𝑗FWT[A]i=c(1,0)∑j=0n/2−1c(i′,j′)Aj+c(1,1)∑j=n/2n−1c(i′,j′)Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，我们只需要：

[𝑐(0,0)𝑐(0,1)𝑐(1,0)𝑐(1,1)][c(0,0)c(0,1)c(1,0)c(1,1)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

四个数就可以完成变换了．我们称这个矩阵为位矩阵．

如果我们要进行逆变换，则需要上面的位矩阵的逆矩阵．

若逆矩阵为 𝑐−1c−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以通过类似操作得到原数：

𝐴𝑖=𝑛∑𝑗=0𝑐−1(𝑖,𝑗)𝐹𝑊𝑇[𝐴]𝑗Ai=∑j=0nc−1(i,j)FWT[A]j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

逆矩阵不一定存在，比如如果有一排 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或者一列 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么这个矩阵就没有逆，我们在构造时需要格外小心．

### 按位或

我们可以构造：

[1011][1011]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这样满足 𝑐(𝑖,𝑗)𝑐(𝑖,𝑘) =𝑐(𝑖,𝑗 ∪𝑘)c(i,j)c(i,k)=c(i,j∪k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们发现，这和我们前面推出的 𝐹𝑊𝑇[𝐴] =merge(𝐹𝑊𝑇[𝐴0],𝐹𝑊𝑇[𝐴0] +𝐹𝑊𝑇[𝐴1])FWT[A]=merge(FWT[A0],FWT[A0]+FWT[A1])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一模一样！同理，下面也是一个满足这个条件的矩阵，但我们一般使用上面这个：

[1110][1110]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

虽然下面这个矩阵也满足 𝑐(𝑖,𝑗)𝑐(𝑖,𝑘) =𝑐(𝑖,𝑗 ∪𝑘)c(i,j)c(i,k)=c(i,j∪k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但这个矩阵存在一排 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不存在逆，所以不合法：

[0011][0011]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果我们要进行逆变换，则需要对矩阵求逆，以 **最上面** 这个矩阵为例，得：

[10−11][10−11]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

然后按照顺变换的方法，把逆变换矩阵代入即可．

### 按位与

我们可以构造：

[1101][1101]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这样满足 𝑐(𝑖,𝑗)𝑐(𝑖,𝑘) =𝑐(𝑖,𝑗 ∩𝑘)c(i,j)c(i,k)=c(i,j∩k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

逆矩阵：

[1−101][1−101]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 按位异或

我们可以构造：

[111−1][111−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这样满足 𝑐(𝑖,𝑗)𝑐(𝑖,𝑘) =𝑐(𝑖,𝑗 ⊕𝑘)c(i,j)c(i,k)=c(i,j⊕k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

逆矩阵：

[0.50.50.5−0.5][0.50.50.5−0.5]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## FWT 是线性变换

FWT 是线性变换．也就是说，它满足：

𝐹𝑊𝑇[𝐴+𝐵]=𝐹𝑊𝑇[𝐴]+𝐹𝑊𝑇[𝐵]FWT[A+B]=FWT[A]+FWT[B]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

以及：

𝐹𝑊𝑇[𝑐⋅𝐴]=𝑐⋅𝐹𝑊𝑇[𝐴]FWT[c⋅A]=c⋅FWT[A]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## K 维 FWT

其实位运算的本质是对一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维 {0,1}{0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向量的运算．或运算就是每一维取 maxmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．且运算就是每一维取 minmin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．异或运算则是每一维对应相加再 mod2mod2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

位运算有个特点：向量的每一位都是独立的．

我们把 {0,1}{0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 扩展到 [0,𝐾) ∩𝐙[0,K)∩Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也就是扩展到 𝐾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制，看看会得到什么？

### max 运算

我们将 ∪∪![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 运算拓展到 𝐾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制，定义 𝑖 ∪𝑗i∪j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示按位取 maxmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有：

𝑐(𝑖,𝑗)𝑐(𝑖,𝑘)=𝑐(𝑖,𝑗∪𝑘)c(i,j)c(i,k)=c(i,j∪k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若 𝑗 =𝑘j=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么上式又是：

𝑐(𝑖,𝑗)𝑐(𝑖,𝑗)=𝑐(𝑖,𝑗)c(i,j)c(i,j)=c(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，每一行的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必定只能在 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前面，如果在后面则不合法了．手玩一下可以发现一组合法构造：

⎡⎢ ⎢ ⎢ ⎢⎣1000110011101111⎤⎥ ⎥ ⎥ ⎥⎦[1000110011101111]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

求逆可得：

⎡⎢ ⎢ ⎢ ⎢⎣1000−11000−11000−11⎤⎥ ⎥ ⎥ ⎥⎦[1000−11000−11000−11]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### min 运算

我们将 ∩∩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 运算拓展到 𝐾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制，定义 𝑖 ∩𝑗i∩j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示按位取 minmin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有：

𝑐(𝑖,𝑗)𝑐(𝑖,𝑘)=𝑐(𝑖,𝑗∩𝑘)c(i,j)c(i,k)=c(i,j∩k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若 𝑗 =𝑘j=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么上式又是：

𝑐(𝑖,𝑗)𝑐(𝑖,𝑗)=𝑐(𝑖,𝑗)c(i,j)c(i,j)=c(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，每一行的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必定只能在 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的后面，如果在前面则不合法了．手玩一下可以发现一组合法构造：

⎡⎢ ⎢ ⎢ ⎢⎣1111011100110001⎤⎥ ⎥ ⎥ ⎥⎦[1111011100110001]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

求逆可得：

⎡⎢ ⎢ ⎢ ⎢⎣1−10001−10001−10001⎤⎥ ⎥ ⎥ ⎥⎦[1−10001−10001−10001]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

前两者用得比较少，用得比较多的是：

### 不进位加法

我们将 ⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 运算拓展到 𝐾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制，定义 𝑖 ⊕𝑗i⊕j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示按位相加再 mod𝐾modK![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有：

𝑐(𝑖,𝑗)𝑐(𝑖,𝑘)=𝑐(𝑖,𝑗⊕𝑘)c(i,j)c(i,k)=c(i,j⊕k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们构造 𝑐(𝑖,𝑗) =𝜔𝑗𝐾c(i,j)=ωKj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以满足要求了：

𝜔𝑗𝐾𝜔𝑘𝐾=𝜔𝑗⊕𝑘𝐾ωKjωKk=ωKj⊕k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

但是每一行都一样矩阵也没有逆，所以我们可以构造 𝑐(𝑖,𝑗) =𝜔(𝑖−1)𝑗𝐾c(i,j)=ωK(i−1)j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

有下面这个矩阵：

⎡⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢⎣111⋯11𝜔1𝐾𝜔2𝐾⋯𝜔𝑘−1𝐾1𝜔2𝐾𝜔4𝐾⋯𝜔2(𝑘−1)𝐾1𝜔3𝐾𝜔6𝐾⋯𝜔3(𝑘−1)𝐾⋮⋮⋮⋱⋮1𝜔𝑘−1𝐾𝜔2(𝑘−1)𝐾⋯𝜔(𝑘−1)(𝑘−1)𝐾⎤⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥⎦[111⋯11ωK1ωK2⋯ωKk−11ωK2ωK4⋯ωK2(k−1)1ωK3ωK6⋯ωK3(k−1)⋮⋮⋮⋱⋮1ωKk−1ωK2(k−1)⋯ωK(k−1)(k−1)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

此即为 [范德蒙德矩阵](https://en.wikipedia.org/wiki/Vandermonde_matrix)，求逆可得：

1𝐾⎡⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢⎣111⋯11𝜔−1𝐾𝜔−2𝐾⋯𝜔−(𝑘−1)𝐾1𝜔−2𝐾𝜔−4𝐾⋯𝜔−2(𝑘−1)𝐾1𝜔−3𝐾𝜔−6𝐾⋯𝜔−3(𝑘−1)𝐾⋮⋮⋮⋱⋮1𝜔−(𝑘−1)𝐾𝜔−2(𝑘−1)𝐾⋯𝜔−(𝑘−1)(𝑘−1)𝐾⎤⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥⎦1K[111⋯11ωK−1ωK−2⋯ωK−(k−1)1ωK−2ωK−4⋯ωK−2(k−1)1ωK−3ωK−6⋯ωK−3(k−1)⋮⋮⋮⋱⋮1ωK−(k−1)ωK−2(k−1)⋯ωK−(k−1)(k−1)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果我们题目给出的模数是存在单位根的，我们就可以简单实现．

但是 **单位根在模意义下可能不存在** ，所以我们考虑扩域，就是人为地定义一个 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足 𝑥𝐾 =1xK=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后直接把 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代入计算，这样每个数都是一个关于 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑘 −1k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次多项式．我们只需要在 mod𝑥𝐾−1modxK−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下计算即可．那么矩阵可以这么表示：

⎡⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢⎣111⋯11𝑥1𝑥2⋯𝑥𝑘−11𝑥2𝑥4⋯𝑥2(𝑘−1)1𝑥3𝑥6⋯𝑥3(𝑘−1)⋮⋮⋮⋱⋮1𝑥𝑘−1𝑥2(𝑘−1)⋯𝑥(𝑘−1)(𝑘−1)⎤⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥⎦[111⋯11x1x2⋯xk−11x2x4⋯x2(k−1)1x3x6⋯x3(k−1)⋮⋮⋮⋱⋮1xk−1x2(k−1)⋯x(k−1)(k−1)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

但是这么做可能会存在零因子，也就是 **一个数有多种表示方法** ，我们无法确定一个数的真实值．

我们考虑不 mod𝑥𝐾−1modxK−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 了，我们 modmod![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分圆多项式 Φ𝐾(𝑥)ΦK(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，他满足 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且在 ℚQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上不可约．所以我们定义上面的计算是在 modΦ𝐾(𝑥)modΦK(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下进行即可．

还有一个问题是，modΦ𝐾(𝑥)modΦK(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 常数大（因为 ΦΦ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 本身就是一个多项式）．但是因为 Φ𝐾(𝑥) ∣𝑥𝑘 −1ΦK(x)∣xk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们只需要在计算时 mod𝑥𝑘 −1modxk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最后再 modΦ𝐾(𝑥)modΦK(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

## 例题

[「CF 1103E」Radix sum](https://www.luogu.com.cn/problem/CF1103E)

给定一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列 𝑎1,𝑎2,...,𝑎𝑛a1,a2,...,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，对于每一个 𝑝 ∈[0,𝑛 −1]p∈[0,n−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求满足下列条件的整数序列 𝑖1,𝑖2,...,𝑖𝑛i1,i2,...,in![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方案数，对 258258![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模：

  * ∀𝑗 ∈[1,𝑛],𝑖𝑗 ∈[1,𝑛]∀j∈[1,n],ij∈[1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 𝑛∑𝑗=1𝑎𝑖𝑗 =𝑝∑j=1naij=p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这里的加法定义为十进制不进位加法．

𝑛 ≤105,𝑎𝑖 ≤105n≤105,ai≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

题解

我们可以想到 dp：设计状态 𝑓𝑖,𝑠fi,s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示考虑到第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数，当前加法状态为 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为 FWT 变换是线性的，可以先变换为 FWT 点值表示法，然后变成自己的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次幂，最后再变换回来．

上面是平凡的，但是题目给出了模数 258258![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．发现没有单位根，所以考虑扩域．

这里的分圆多项式 Φ10(𝑥) =𝑥4 −𝑥3 +𝑥2 −𝑥 +1Φ10(x)=x4−x3+x2−x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

然而我们发现 UFWT 时，需要除去进制 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然而我们发现 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 258258![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下没有逆元．实际上我们发现 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 258258![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下是有逆元的：5764607523034234957646075230342349![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们只需要再除去一个 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就可以了．设已经除以了 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的答案为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，真正的答案为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是 25𝑦 ≡𝑥(mod264)25y≡x(mod264)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，显然，我们有 𝑦 ≡𝑥25(mod264−5)y≡x25(mod264−5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是 𝑦 ≡𝑥25(mod259)y≡x25(mod259)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以直接将最后的答案除以 2525![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．虽然出题人不知道为什么要模 258258![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但再取下模即可．

[【CF103329F】【XXII Opencup, Grand Prix of XiAn】The Struggle](https://codeforces.com/gym/103329/problem/F)

给出一个椭圆 𝐸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中所有整点的坐标均在 [1,4 ⋅106][1,4⋅106]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间．求 ∑(𝑥,𝑦)∈𝐸(𝑥 ⊕𝑦)33𝑥−2𝑦−1mod 109 +7∑(x,y)∈E(x⊕y)33x−2y−1mod109+7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

题解

这是一道比较不裸的题，出题人提供了详细的英文题解，具体请见 [此链接](https://codeforces.com/blog/entry/96518)．

## 参考资料

  * [桃酱的算法笔记](https://zhuanlan.zhihu.com/p/41867199)
  * [ZnPdCo 的博客](https://znpdco.github.io/%E7%AE%97%E6%B3%95/2024/05/07/FWT.html)

* * *

  1. [维基百科](https://zh.wikipedia.org/zh-cn/%E6%B2%83%E7%88%BE%E4%BB%80%E8%BD%89%E6%8F%9B) ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/fwt.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/fwt.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [ZnPdCo](https://github.com/ZnPdCo), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [Xeonacid](https://github.com/Xeonacid), [BinDir0](https://github.com/BinDir0), [HeRaNO](https://github.com/HeRaNO), [lxlonlyn](https://github.com/lxlonlyn), [nocriz](https://github.com/nocriz), [nocrizwang](https://github.com/nocrizwang), [qkhm](https://github.com/qkhm), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [xyf007](https://github.com/xyf007)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
