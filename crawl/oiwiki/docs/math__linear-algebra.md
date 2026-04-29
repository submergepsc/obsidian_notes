# 线性代数简介 - OI Wiki

- Source: https://oi-wiki.org/math/linear-algebra/

# 线性代数简介

提示

本篇与「线性代数」分类下的其他篇目关联不大．但笔者认为，讲讲线性代数的本质，追溯概念的根源与联系，让读者对于线性代数有一个初步但是成体系的认识，确实有其必要性．

早在几千年前，就有古人应用线性方程组解决问题，而如今，线性代数仍然应用广泛．

线性代数源于人们的观察．人们发现，很多对象都拥有相似的性质，比如：

  * 力可以被分解、合成．

  * 对于任意的 𝑘,𝑥0k,x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑘sin⁡(𝑥−𝑥0)ksin⁡(x−x0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以分解成 𝑘1sin⁡𝑥 +𝑘2cos⁡𝑥k1sin⁡x+k2cos⁡x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这些性质与所描述对象的 **缩放** 、**分解** 、**叠加** 等有关．线性代数把这些性质从具体对象中抽象出来，作为一个独立的学科来研究．在 OI 中，线性代数的知识可以直接用来解决问题，也可以用于优化算法、数据结构等．例如：

  * 用树剖维护线性基求链上最大异或和

  * 利用矩阵树定理把图的生成树计数问题转化为求矩阵的行列式

  * 用矩阵快速幂优化递推

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/linear-algebra/index.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/linear-algebra/index.md "edit.link.title")  
>  __本页面贡献者：[codewasp942](https://github.com/codewasp942), [ChungZH](https://github.com/ChungZH), [Great-designer](https://github.com/Great-designer), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
