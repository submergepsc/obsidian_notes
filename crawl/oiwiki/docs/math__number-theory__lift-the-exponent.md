# 升幂引理 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/lift-the-exponent/

# 升幂引理

## 内容

升幂（Lift the Exponent，LTE）引理是初等数论中比较常用的一个定理．

定义 𝜈𝑝(𝑛)νp(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的标准分解中素因子 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次，即 𝜈𝑝(𝑛)νp(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑝𝜈𝑝(𝑛) ∣𝑛pνp(n)∣n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑝𝜈𝑝(𝑛)+1 ∤𝑛pνp(n)+1∤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

由于升幂引理内容较长，我们将其分为三部分介绍：

以下内容设 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为素数，𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为满足 𝑝 ∤𝑥p∤x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑝 ∤𝑦p∤y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为正整数．

### 第一部分

对所有的素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和满足 (𝑛,𝑝) =1(n,p)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，

  1. 若 𝑝 ∣𝑥 −𝑦p∣x−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则：

𝜈𝑝(𝑥𝑛−𝑦𝑛)=𝜈𝑝(𝑥−𝑦)νp(xn−yn)=νp(x−y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 若 𝑝 ∣𝑥 +𝑦p∣x+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则对奇数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有：

𝜈𝑝(𝑥𝑛+𝑦𝑛)=𝜈𝑝(𝑥+𝑦)νp(xn+yn)=νp(x+y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证明

若 𝑝 ∣𝑥 −𝑦p∣x−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则不难发现 𝑝 ∣𝑥 −𝑦 ⟺ 𝑥 ≡𝑦(mod𝑝)p∣x−y⟺x≡y(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则显然有：

𝑛−1∑𝑖=0𝑥𝑖𝑦𝑛−1−𝑖≡𝑛𝑥𝑛−1≢0(mod𝑝)∑i=0n−1xiyn−1−i≡nxn−1≢0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

进而由 𝑥𝑛 −𝑦𝑛 =(𝑥 −𝑦)∑𝑛−1𝑖=0𝑥𝑖𝑦𝑛−1−𝑖xn−yn=(x−y)∑i=0n−1xiyn−1−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可知命题得证．

对 𝑝 ∣𝑥 +𝑦p∣x+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况证明方法类似．

### 第二部分

若 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇素数，

  1. 若 𝑝 ∣𝑥 −𝑦p∣x−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则：

𝜈𝑝(𝑥𝑛−𝑦𝑛)=𝜈𝑝(𝑥−𝑦)+𝜈𝑝(𝑛)νp(xn−yn)=νp(x−y)+νp(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 若 𝑝 ∣𝑥 +𝑦p∣x+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则对奇数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有：

𝜈𝑝(𝑥𝑛+𝑦𝑛)=𝜈𝑝(𝑥+𝑦)+𝜈𝑝(𝑛)νp(xn+yn)=νp(x+y)+νp(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证明

若 𝑝 ∣𝑥 −𝑦p∣x−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，令 𝑦 =𝑥 +𝑘𝑝y=x+kp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们只需证明 𝑝 ∣𝑛p∣n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况．

  * 若 𝑛 =𝑝n=p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则由二项式定理：

𝑝−1∑𝑖=0𝑥𝑝−1−𝑖𝑦𝑖=𝑝−1∑𝑖=0𝑥𝑝−1−𝑖𝑖∑𝑗=0(𝑖𝑗)𝑥𝑗(𝑘𝑝)𝑖−𝑗≡𝑝𝑥𝑝−1(mod𝑝2)∑i=0p−1xp−1−iyi=∑i=0p−1xp−1−i∑j=0i(ij)xj(kp)i−j≡pxp−1(modp2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

从而

𝜈𝑝(𝑥𝑛−𝑦𝑛)=𝜈𝑝(𝑥−𝑦)+1νp(xn−yn)=νp(x−y)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 若 𝑛 =𝑝𝑎n=pa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则由数学归纳法可得

𝜈𝑝(𝑥𝑛−𝑦𝑛)=𝜈𝑝(𝑥−𝑦)+𝑎νp(xn−yn)=νp(x−y)+a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此命题得证．

对 𝑝 ∣𝑥 +𝑦p∣x+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况证明方法类似．

### 第三部分

若 𝑝 =2p=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑝 ∣𝑥 −𝑦p∣x−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，

  1. 对奇数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有（与第一部分的 1 相同）：

𝜈𝑝(𝑥𝑛−𝑦𝑛)=𝜈𝑝(𝑥−𝑦)νp(xn−yn)=νp(x−y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 对偶数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有：

𝜈𝑝(𝑥𝑛−𝑦𝑛)=𝜈𝑝(𝑥−𝑦)+𝜈𝑝(𝑥+𝑦)+𝜈𝑝(𝑛)−1νp(xn−yn)=νp(x−y)+νp(x+y)+νp(n)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

另外对上述的 𝑥,𝑦,𝑛x,y,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们有：

若 4 ∣𝑥 −𝑦4∣x−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则：

  * 𝜈2(𝑥 +𝑦) =1ν2(x+y)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝜈2(𝑥𝑛−𝑦𝑛) =𝜈2(𝑥 −𝑦) +𝜈2(𝑛)ν2(xn−yn)=ν2(x−y)+ν2(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证明

我们只需证明 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为偶数的情况．由于此时 𝑝 ∤(𝑝2)p∤(p2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故我们不能用第二部分的方法证明．

令 𝑛 =2𝑎𝑏n=2ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑎 =𝜈𝑝(𝑛)a=νp(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，2 ∤𝑏2∤b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而

𝜈𝑝(𝑥𝑛−𝑦𝑛)=𝜈𝑝(𝑥2𝑎−𝑦2𝑎)=𝜈𝑝((𝑥−𝑦)(𝑥+𝑦)𝑎−1∏𝑖=1(𝑥2𝑖+𝑦2𝑖))νp(xn−yn)=νp(x2a−y2a)=νp((x−y)(x+y)∏i=1a−1(x2i+y2i))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到 2 ∣𝑥 −𝑦 ⟹ 4 ∣𝑥2 −𝑦22∣x−y⟹4∣x2−y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而 (∀𝑖 ≥1), 𝑥2𝑖 +𝑦2𝑖 ≡2(mod4)(∀i≥1), x2i+y2i≡2(mod4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进而上式可变为：

𝜈𝑝(𝑥𝑛−𝑦𝑛)=𝜈𝑝(𝑥−𝑦)+𝜈𝑝(𝑥+𝑦)+𝜈𝑝(𝑛)−1νp(xn−yn)=νp(x−y)+νp(x+y)+νp(n)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此命题得证．

## 参考资料

  1. [Lifting-the-exponent lemma - Wikipedia](https://en.wikipedia.org/wiki/Lifting-the-exponent_lemma)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/lift-the-exponent.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/lift-the-exponent.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
