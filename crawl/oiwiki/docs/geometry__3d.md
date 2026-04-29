# 三维计算几何基础 - OI Wiki

- Source: https://oi-wiki.org/geometry/3d/

# 三维计算几何基础

三维几何的很多概念与 [二维几何](../2d/) 是相通的，我们可以用与解决二维几何问题相同的方法来解决三维几何问题．

## 基本概念

点，向量，直线这些概念和二维几何是相似的，这里不再展开．

### 平面

我们可以用平面上的一点 𝑃0(𝑥0,𝑦0,𝑧0)P0(x0,y0,z0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和该平面的法向量（即垂直于该平面的向量）𝒏n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来表示一个平面．

因为 𝒏n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 垂直于平面，所以 𝒏n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 垂直于该平面内的所有直线．换句话说，设 𝒏 =(𝐴,𝐵,𝐶)n=(A,B,C)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则该平面上的点 𝑃(𝑥,𝑦,𝑧)P(x,y,z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都满足 𝒏 ⋅←←←←←→𝑃𝑃0 =0n⋅PP0→=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

根据向量点积的定义，上式等价于：

𝐴(𝑥−𝑥0)+𝐵(𝑦−𝑦0)+𝐶(𝑧−𝑧0)=0A(x−x0)+B(y−y0)+C(z−z0)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

整理后得到：

𝐴𝑥+𝐵𝑦+𝐶𝑧−(𝐴𝑥0+𝐵𝑦0+𝐶𝑧0)=0Ax+By+Cz−(Ax0+By0+Cz0)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令 𝐷 = −(𝐴𝑥0 +𝐵𝑦0 +𝐶𝑧0)D=−(Ax0+By0+Cz0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则上式变成 𝐴𝑥 +𝐵𝑦 +𝐶𝑧 +𝐷 =0Ax+By+Cz+D=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们称这个式子为平面的 **一般式** ．

## 基本操作

### 直线、平面之间的夹角

运用空间向量的知识，空间中直线、平面之间的夹角可以很快求出．

对于两条异面直线 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，过空间中一点 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，作 𝑎′ ∥𝑎a′∥a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏′ ∥𝑏′b′∥b′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑎′a′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑏′b′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所成的锐角或直角被称为 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两条 **异面直线所成的角** ．

对于直线 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和平面 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相交于 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，过 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上一点 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 引平面 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的垂线交 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 于 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑃𝑂PO![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所成角的余角被称为 **直线与平面所成的角** ．特别地，若 𝑎 ∥𝛼a∥α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑎 ⊂𝛼a⊂α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则它们之间的夹角为 0∘0∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于两个平面 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它们的夹角被定义为与两条平面的交线 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 垂直的两条直线 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（其中 𝑎 ⊂𝛼a⊂α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏 ⊂𝛽b⊂β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）所成的角．

#### 两直线夹角定义与关系充要条件

  * 两直线的方向向量的夹角，叫做两直线的夹角．

有了这个命题，我们就可以得出以下结论：已知两条直线 𝑙1,𝑙2l1,l2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它们的方向向量分别是 𝑠1(𝑚1,𝑛1,𝑝1)s1(m1,n1,p1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑠2(𝑚2,𝑛2,𝑝2)s2(m2,n2,p2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设 𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为两直线夹角，我们可以得到 cos⁡𝜑 =|𝑚1𝑚2+𝑛1𝑛2+𝑝1𝑝2|√𝑚21+𝑛21+𝑝21√𝑚22+𝑛22+𝑝22cos⁡φ=|m1m2+n1n2+p1p2|m12+n12+p12m22+n22+p22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

  * 𝑙1 ⟂𝑙2 ⟺ 𝑚1𝑚2 +𝑛1𝑛2 +𝑝1𝑝2 =0l1⟂l2⟺m1m2+n1n2+p1p2=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 𝑙1 ∥𝑙2 ⟺ 𝑚1𝑚2 =𝑛1𝑛2 =𝑝1𝑝2l1∥l2⟺m1m2=n1n2=p1p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

### 三维向量与平面的夹角

当直线与平面不垂直时，直线和它在平面上的投影直线的夹角 𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝜑 ∈[0,𝜋2]φ∈[0,π2]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）称为直线与平面的夹角．

设直线向量 𝑠(𝑚,𝑛,𝑝)s(m,n,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，平面法线向量 𝑓(𝑎,𝑏,𝑐)f(a,b,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么以下命题成立：

  * 角度的正弦值：sin⁡𝜑 =|𝑎𝑚+𝑏𝑛+𝑐𝑝|√𝑎2+𝑏2+𝑐2√𝑚2+𝑛2+𝑝2sin⁡φ=|am+bn+cp|a2+b2+c2m2+n2+p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 直线与平面平行  ⟺ 𝑎𝑚 +𝑏𝑛 +𝑐𝑝 =0⟺am+bn+cp=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 直线与平面垂直  ⟺ 𝑎𝑚 =𝑏𝑛 =𝑐𝑝⟺am=bn=cp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 点到平面的距离

### 直线与平面的交点

直接联立直线方程和平面方程即可．

## 立体几何定理

### 三正弦定理

设二面角 𝑀－𝐴𝐵－𝑁M－AB－N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的度数为 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在平面 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上有一条射线 𝐴𝐶AC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它和棱 𝐴𝐵AB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所成角为 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，和平面 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所成的角为 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 sin⁡𝛾 =sin⁡𝛼 ⋅sin⁡𝛽sin⁡γ=sin⁡α⋅sin⁡β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 三余弦定理

设 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为平面上一点，过平面外一点 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的直线 𝐵𝑂BO![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在面上的射影为 𝐴𝑂AO![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑂𝐶OC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为面上的一条直线，那么 ∠𝐶𝑂𝐵，∠𝐴𝑂𝐶，∠𝐴𝑂𝐵∠COB，∠AOC，∠AOB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 三角的余弦关系为：cos⁡∠𝐵𝑂𝐶 =cos⁡∠𝐴𝑂𝐵 ⋅cos⁡∠𝐴𝑂𝐶cos⁡∠BOC=cos⁡∠AOB⋅cos⁡∠AOC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（∠𝐴𝑂𝐶∠AOC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，∠𝐴𝑂𝐵∠AOB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只能是锐角）．

## 参考资料

  * [3D 空间基础概念之一：点、向量（矢量）和齐次坐标](https://www.cnblogs.com/CodeBlove/articles/1319563.html)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/geometry/3d.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/geometry/3d.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [shuzhouliu](https://github.com/shuzhouliu), [Enter-tainer](https://github.com/Enter-tainer), [billchenchina](https://github.com/billchenchina), [Great-designer](https://github.com/Great-designer), [ouuan](https://github.com/ouuan), [Qaaxaap](https://github.com/Qaaxaap), [StudyingFather](https://github.com/StudyingFather), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
