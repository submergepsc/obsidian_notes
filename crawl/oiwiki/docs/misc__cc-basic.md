# 计算理论基础 - OI Wiki

- Source: https://oi-wiki.org/misc/cc-basic/

# 计算理论基础

本部分将介绍基础的计算理论的知识．这部分内容在 OI 中作用不大（但还是略有作用：如果你遇到了一个 NP-hard 问题，你可以认为它是不存在多项式复杂度的解法的），可以作为兴趣了解，或者为以后的学习做准备．

本文中许多结论都是不加证明的，如果有兴趣的话可以自行查阅相关证明．

前置知识：[时间复杂度](../../basic/complexity/)．

## 问题

### 语言

一个 **字母表（alphabet）** 是一个非空有限集合，该集合中的元素称为 **符号/字符（symbol）** ．

令 Σ∗Σ∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示非负整数个 ΣΣ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的字符连接而成的串，字母表 ΣΣ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的一个 **语言（language）** 是 Σ∗Σ∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个子集．

需要注意的是，这里的「语言」是一个抽象的概念，通常意义上的字符串是语言，所有的有向无环图也可以是一个语言（01 串与有向图之间可以建立双射，具体方式无需了解）．

由于任何语言都可以转化成 01 串的形式，所以在下文中不加说明时 Σ ={0,1}Σ={0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 判定问题

判定问题就是只能用 YES/NO 回答的问题，本质上是判定一个串是否属于一个语言，即：𝑓 :Σ∗ →{0,1},𝑓(𝑥) =1 ⟺ 𝑥 ∈𝐿f:Σ∗→{0,1},f(x)=1⟺x∈L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个关于字母表 ΣΣ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和语言 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的判定问题．如，「判定一张图是不是一个有向无环图」就是一个判定问题．

判定问题由于其简洁性而常常被作为计算理论研究的对象．本文中不加说明时，「问题」都指「判定问题」，当然，有时一些命题也能简单地推广到其它问题上．

一个语言也可以代指「判定一个串是否属于这个语言」这个判定问题，因此，「语言」和「问题」可以视作同义词．

### 功能性问题

功能性问题的回答不止 YES/NO，可以是一个数或是其它．如，「求两个数的和」就是一个功能性问题．

任何功能性问题都可以转化为一个判定问题，如，「求两个数的和」可以转化为「判定两个数的和是否等于第三个数」．

判定问题也可以转化为一个功能性问题：求这个判定问题的指示函数，即上文中判定问题定义里的 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 图灵机

### 确定性图灵机

不加说明时，「图灵机」往往指「确定性图灵机」，本文中也是如此．

图灵机有很多不同的定义，这里选取其中一种，其它定义下的图灵机往往与下面这种定义的图灵机计算能力等价．

图灵机是一个在一条可双向无限延伸且被划分为若干格子的纸带上进行操作的机器，其有内部状态，还有一个可以在纸带上进行修改与移动的磁针．

正式地说，图灵机是一个七元组 𝑀 =⟨𝑄,Γ,𝑏,Σ,𝛿,𝑞0,𝐹⟩M=⟨Q,Γ,b,Σ,δ,q0,F⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中：

  * 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个有限非空的 **状态集合** ；
  * ΓΓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个有限非空的 **磁带字母表** ；
  * 𝑏 ∈Γb∈Γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 **空字符** ，它是唯一一个在计算过程中可以在磁带上无限频繁地出现的字符；
  * Σ ⊆(Γ ∖{𝑏})Σ⊆(Γ∖{b})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 **输入符号集** ，是可以出现在初始磁带（即输入）上的字符；
  * 𝑞0 ∈𝑄q0∈Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 **初始状态** ；
  * 𝐹 ⊆𝑄F⊆Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 **接受状态** ，如果一个图灵机在某个接受状态停机，则称初始磁带上的内容被这个图灵机 **接受** ．
  * 𝛿 :(𝑄 ∖𝐹) ×Γ ↛𝑄 ×Γ ×{𝐿,𝑅}δ:(Q∖F)×Γ↛Q×Γ×{L,R}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个被称作 **转移函数** 的 partial function（即只对定义域的一个子集有定义的函数）．如果 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在当前状态下没有定义，则图灵机停机．

图灵机从初始状态与纸带起点起，每次根据当前的内部状态 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和当前磁针指向的纸带上的单元格中的字符 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行操作：若 𝛿(𝑥,𝑦)δ(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有定义则停机，否则若 𝛿(𝑥,𝑦) =(𝑎,𝑏,𝑐)δ(x,y)=(a,b,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则将内部状态修改为 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将磁针指向的格子中的字符修改为 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则向左移动一格，为 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则向右移动一格．

其实，知道图灵机的工作细节是不必要的，只需建立直观理解即可．

图灵机 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在输入 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的输出记作 𝑀(𝑥)M(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑀(𝑥) =1M(x)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 接受 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑀(𝑥) =0M(x)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在输入 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下在有限步骤内停机且 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不接受 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），也可以在括号内包含多个参数，用逗号隔开，具体实现时可以向字母表中添加一个元素表示逗号来隔开各个参数．

图灵机与冯·诺依曼计算机解决问题的时间复杂度差别在多项式级别内，所以研究复杂度类时可以使用图灵机作为计算模型．

### 非确定性图灵机

非确定型图灵机是图灵机的一种，它与确定型图灵机的不同在于：确定型图灵机的每一步只能转移到一个状态，而非确定型图灵机可以「同时」转移到多个状态，从而在多个「分支」并行计算，一旦这些「分支」中有一个在接受状态停机，则此非确定性图灵机接受这个输入．

事实上，任何确定型图灵机都可以用类似于迭代加深搜索的方式在指数级时间内模拟一台非确定型图灵机多项式时间内的行为．

在现实生活中，确定型图灵机相当于单核处理器，只支持串行处理；而非确定型图灵机相当于理想的多核处理器，支持无限大小的并行处理．

### 多带图灵机

标准的图灵机只能在一条纸带上进行操作，但为了方便，本文中研究多带图灵机．对于一个 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 带图灵机，其中一条纸带是只读的输入带，而剩下的 𝑘 −1k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条纸带可以进行读写，并且这 𝑘 −1k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条纸带中还有一条纸带用作输出．

多带图灵机的纸带数必须是有限的．

对于一个多带图灵机，它使用的空间是磁头在除输入带外的其它纸带上所访问过的单元格数目．

### 图灵机的编码

图灵机可以被自然数编码，即存在满射函数 𝑓 :ℕ →𝕄f:N→M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得每个自然数都对应一个图灵机，而每个图灵机都有无数个编码．因此，由若干图灵机构成的集合可以是一个语言．

记由自然数 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 编码的图灵机为 𝑀𝛼Mα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 通用图灵机

存在一台图灵机 UU![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足：

  1. 若 𝑀𝛼Mα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在输入 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下在有限时间内停机，则 U(𝑥,𝛼) =𝑀𝛼(𝑥)U(x,α)=Mα(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，否则 U(𝑥,𝛼)U(x,α)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不会在有限时间内停机；
  2. 如果对于任意 𝑥 ∈{0,1}∗x∈{0,1}∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑀𝛼Mα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在输入 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下在 𝑇(|𝑥|)T(|x|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内停机，则对于任意 𝑥 ∈{0,1}∗x∈{0,1}∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，U(𝑥,𝛼)U(x,α)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑂(𝑇(|𝑥|)log⁡𝑇(|𝑥|))O(T(|x|)log⁡T(|x|))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内停机．

即：存在一台通用图灵机，它能模拟任何一台图灵机，且花费的时间只会比这台被模拟的图灵机慢其运行时间的对数．

## 可计算性

### 不可计算问题

对于一个判定问题，若存在一个总是在有限步内停机且能够正确进行判定的图灵机，则这个问题是一个 **图灵可计算** 的问题，否则这个问题是一个 **图灵不可计算** 的问题．

由于图灵机可以被自然数编码，所以图灵机的个数是可数无穷，而语言（即二进制串的集合）的个数是不可数无穷，而每个图灵机最多判定一个语言，所以一定存在图灵不可计算的问题．

### 停机问题

停机问题是一个经典的图灵不可计算问题：给定 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，判定 𝑀𝛼Mα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在输入为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时是否会在有限步内停机．

停机问题是图灵不可计算的证明

定义函数 𝖴𝖢 :{0,1}∗ →{0,1}UC:{0,1}∗→{0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为：

𝖴𝖢(𝛼)={0𝑀𝛼(𝛼)=11otherwiseUC(α)={0Mα(α)=11otherwise![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们先证明 𝖴𝖢UC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 函数是图灵不可计算的：

假设存在一台图灵机 𝑀𝛽Mβ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能够计算 𝖴𝖢UC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么根据 𝖴𝖢UC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义可以得到 𝖴𝖢(𝛽) =1 ⟺ 𝑀𝛽(𝛽) ≠1UC(β)=1⟺Mβ(β)≠1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而根据 𝑀𝛽Mβ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能够计算 𝖴𝖢UC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以得到 𝑀𝛽(𝛽) =𝖴𝖢(𝛽)Mβ(β)=UC(β)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，产生了矛盾，所以假设不成立，不存在可以计算 𝖴𝖢UC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的图灵机．

令 𝑀𝖧𝖠𝖫𝖳MHALT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个可以解决停机问题的图灵机，𝑀𝖧𝖠𝖫𝖳(𝑥,𝛼)MHALT(x,α)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值是判定问题 𝑀𝛼Mα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在输入为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时是否会在有限步内停机的解，那么我们可以构造出一台能够计算 𝖴𝖢UC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 函数的图灵机 𝑀𝖴𝖢MUC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑀𝖴𝖢MUC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 首先调用 𝑀𝖧𝖠𝖫𝖳(𝛼,𝛼)MHALT(α,α)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 如果它输出 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则 𝑀𝖴𝖢(𝛼) =1MUC(α)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；否则，𝑀𝖴𝖢MUC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使用通用图灵机模拟计算得到答案．

由于 𝖴𝖢UC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 函数是图灵不可计算的，所以 𝑀𝖧𝖠𝖫𝖳MHALT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不存在，也就是说停机问题是图灵不可计算的．

## 丘奇 - 图灵论题

丘奇 - 图灵论题称，若一类问题有一个有效的方法解决，则这类问题可以被某个图灵机解决．

其中，「有效的方法」需要满足：

  1. 包含有限条清晰的指令；
  2. 当用其解决这类问题的其中一个时，这个方法需要在有限步骤内结束，且得到正确的答案．

这个论题没有被证明，但其是计算理论的一条基本公理．

## 复杂度类

复杂度类有很多，本文只会介绍其中较为常见的一小部分．

### R 和 RE

对于语言 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和图灵机 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在任何输入下都能在有限步骤内停机，且 𝑀(𝑥) =1 ⟺ 𝑥 ∈𝐿M(x)=1⟺x∈L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能够 **判定** 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于语言 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和图灵机 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若对于任何属于 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的输入，𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都在有限步骤内停机，且 𝑀(𝑥) =1 ⟺ 𝑥 ∈𝐿M(x)=1⟺x∈L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能够 **识别** 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

复杂度类 𝖱R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示那些可以被某台图灵机判定的语言的集合，即所有图灵可计算的语言．

复杂度类 𝖱𝖤RE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示那些可以被某台图灵机识别的语言的集合．𝖱𝖤RE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也被称作递归可枚举语言．

由定义可以得到 𝖱 ⊆𝖱𝖤R⊆RE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### DTIME

如果存在一台确定性图灵机能够判定一个语言，且对于任何输入 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这台图灵机可以在 𝑂(𝑓(|𝑥|))O(f(|x|))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内停机，那么这个语言属于 𝖣𝖳𝖨𝖬𝖤(𝑓(𝑛))DTIME(f(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类．

### P

复杂度类 𝖯P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示可以由确定性图灵机在多项式时间内解决的判定问题，即：

𝖯=⋃𝑘∈ℕ𝖣𝖳𝖨𝖬𝖤(𝑛𝑘)P=⋃k∈NDTIME(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

线性规划、计算最大公约数、求图的最大匹配的判定版本都是 𝖯P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题．

### EXPTIME

复杂度类 𝖤𝖷𝖯𝖳𝖨𝖬𝖤EXPTIME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示可以由确定性图灵机在指数级时间内解决的判定问题，即：

𝖤𝖷𝖯𝖳𝖨𝖬𝖤=⋃𝑘∈ℕ𝖣𝖳𝖨𝖬𝖤(2𝑛𝑘)EXPTIME=⋃k∈NDTIME(2nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

停机问题的弱化版——给定一个图灵机的编码以及一个正整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，判定这个图灵机是否在 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步内停机，是一个 𝖤𝖷𝖯𝖳𝖨𝖬𝖤EXPTIME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类的问题．因为这个问题的解法需要 𝑂(𝑘)O(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间，而数字 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以被编码为长度为 𝑂(log⁡𝑘)O(log⁡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制串．

### NTIME

如果存在一台非确定性图灵机能够判定一个语言，且对于任何输入 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这台图灵机可以在 𝑂(𝑓(|𝑥|))O(f(|x|))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内停机，那么这个语言属于 𝖭𝖳𝖨𝖬𝖤(𝑓(𝑛))NTIME(f(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类．

### NP

复杂度类 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示可以由非确定性图灵机在多项式时间内解决的判定问题，即：

𝖭𝖯=⋃𝑘∈ℕ𝖭𝖳𝖨𝖬𝖤(𝑛𝑘)NP=⋃k∈NNTIME(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所有 𝖯P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题都是 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题．更多 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题请参见下文中的 NPC 问题以及 NP-intermediate 问题．

#### NP-hard

如果所有 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题都可以在多项式时间内规约到问题 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么问题 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 NP-hard 的．

换句话说，如果可以在一单位的时间内解决 NP-hard 的问题 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么所有 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题都可以在多项式单位的时间内解决．

#### NP-complete

如果一个问题既是 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题又是 NP-hard 的，那么这个问题是 NP 完全 (NP-complete) 的，或者说这是一个 NPC 问题．

一些经典的 NPC 问题：旅行商问题的判定版本、最大独立集问题的判定版本、最小点覆盖问题的判定版本、最长路问题的判定版本、0-1 整数规划问题的判定版本、集合覆盖问题、图着色问题、背包问题、三维匹配问题、最大割问题的判定版本．

NPC 问题的功能性版本往往是 NP-hard 的，例如：「判定一张图中是否存在大小为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的团」既是一个 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题又是 NP-hard 的，从而它是一个 NPC 问题，而它的功能性版本「求一张图的最大团」不是 NPC 问题，但这个功能性版本依然是 NP-hard 的．

类似地，其它复杂度类也会有「XX-complete」，如所有 𝖤𝖷𝖯𝖳𝖨𝖬𝖤EXPTIME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类的问题都能在多项式时间内规约到 EXPTIME-complete 的问题．

#### co-NP

一个问题是 𝖼𝗈−𝖭𝖯co−NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题，当且仅当它的补集是 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题．如果将「问题」理解为「语言」，而「语言」是 Σ∗Σ∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集，就能理解「补集」了．

例如：「给定 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个子集，判断是否能够从中选取 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，覆盖整个集合」是一个 NPC 问题，而其补集「给定 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个子集，判断是否从中任取 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个都不能覆盖整个集合」是一个 𝖼𝗈−𝖭𝖯co−NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题．如果第一个问题的答案是「是」，那么相当于找到了第二个问题的一组反例，从而第二个问题的答案是「否」．

#### NP-intermediate

如果一个问题是 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题，但它既不是 𝖯P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题也不是 NPC 问题，则称其为 NP-intermediate 问题．

就人们目前的了解，图同构问题、离散对数问题和因数分解问题可能是 NP-intermediate 的．

Ladner 定理指出，如果 𝖯 ≠𝖭𝖯P≠NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则一定存在问题是 NP-intermediate 的．

### NEXPTIME

复杂度类 𝖭𝖤𝖷𝖯𝖳𝖨𝖬𝖤NEXPTIME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示可以由非确定性图灵机在指数级时间内解决的判定问题，即：

𝖭𝖤𝖷𝖯𝖳𝖨𝖬𝖤=⋃𝑘∈ℕ𝖭𝖳𝖨𝖬𝖤(2𝑛𝑘)NEXPTIME=⋃k∈NNTIME(2nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### #P

#𝖯#P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题不是判定问题，而是关于 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题的计数问题：数一个 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类问题的解的个数是一个 #𝖯#P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类的问题．换句话说，数一个串在一个总是在多项式时间内停机的非确定性图灵机的多少个分支处被接受是一个 #𝖯#P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类的问题．

求一张普通图或二分图的匹配或完美匹配个数都是 #P 完全的，对应的判定问题为「判定一张图是否存在（完美）匹配」．

### DSPACE

如果存在一台确定性图灵机能够在输入为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时在 𝑂(𝑓(|𝑥|))O(f(|x|))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的空间内判定一个语言，那么这个语言属于 𝖣𝖲𝖯𝖠𝖢𝖤(𝑓(𝑛))DSPACE(f(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类．

  * 𝖱𝖤𝖦 =𝖣𝖲𝖯𝖠𝖢𝖤(𝑂(1))REG=DSPACE(O(1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即正则语言，也就是自动机能够判定的语言．

  * 𝖫 =𝖣𝖲𝖯𝖠𝖢𝖤(𝑂(log⁡𝑛))L=DSPACE(O(log⁡n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，需要注意的是图灵机使用的空间不包括输入占用的空间．

  * 𝖯𝖲𝖯𝖠𝖢𝖤 =⋃𝑘∈ℕ𝖣𝖲𝖯𝖠𝖢𝖤(𝑛𝑘)PSPACE=⋃k∈NDSPACE(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 𝖤𝖷𝖯𝖲𝖯𝖠𝖢𝖤 =⋃𝑘∈ℕ𝖣𝖲𝖯𝖠𝖢𝖤(2𝑛𝑘)EXPSPACE=⋃k∈NDSPACE(2nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### NSPACE

如果存在一台非确定性图灵机能够在输入为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时在 𝑂(𝑓(|𝑥|))O(f(|x|))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的空间内判定一个语言，那么这个语言属于 𝖭𝖲𝖯𝖠𝖢𝖤(𝑓(𝑛))NSPACE(f(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类．

  * 𝖱𝖤𝖦 =𝖣𝖲𝖯𝖠𝖢𝖤(𝑂(1)) =𝖭𝖲𝖯𝖠𝖢𝖤(𝑂(1))REG=DSPACE(O(1))=NSPACE(O(1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 𝖭𝖫 =𝖭𝖲𝖯𝖠𝖢𝖤(𝑂(log⁡𝑛))NL=NSPACE(O(log⁡n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 𝖢𝖲𝖫 =𝖭𝖲𝖯𝖠𝖢𝖤(𝑂(𝑛))CSL=NSPACE(O(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即上下文相关语言．

  * 𝖯𝖲𝖯𝖠𝖢𝖤 =𝖭𝖯𝖲𝖯𝖠𝖢𝖤 =⋃𝑘∈ℕ𝖭𝖲𝖯𝖠𝖢𝖤(𝑛𝑘)PSPACE=NPSPACE=⋃k∈NNSPACE(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 𝖤𝖷𝖯𝖲𝖯𝖠𝖢𝖤 =𝖭𝖤𝖷𝖯𝖲𝖯𝖠𝖢𝖤 =⋃𝑘∈ℕ𝖭𝖲𝖯𝖠𝖢𝖤(2𝑛𝑘)EXPSPACE=NEXPSPACE=⋃k∈NNSPACE(2nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 多项式时间

简单来说，如果存在正数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得一个算法的时间复杂度为 𝑂(𝑛𝑘)O(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（注意，不是 Θ(𝑛𝑘)Θ(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），其中 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为问题规模（输入的长度），则称这个算法是 **多项式时间** 的．如果一个问题有（确定性图灵机上的）多项式时间的算法来解决，则这个问题属于复杂度类 𝖯P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

多项式时间可分为强多项式时间和弱多项式时间，除此之外还有伪多项式时间．

### Strongly polynomial time 强多项式时间

我们先定义一个计算模型，称作算术模型．在算术模型中，数字之间的算术运算（加减乘除、比较大小）可以在单位时间内完成（即 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内完成，与数字大小无关）．

如果一个算法在算术模型下的操作数是输入中的数字个数的多项式，并且空间复杂度是输入规模（而非数字个数）的多项式，则这个算法是 **强多项式时间** 的．由于算术操作在一般的计算模型下可以在输入规模（即数字大小的对数）的多项式时间内完成，强多项式时间的算法一定是多项式时间的．

一般来说，强多项式时间的算法的时间复杂度与值域无关．

### Weakly polynomial time 弱多项式时间

如果一个算法是多项式时间的但不是强多项式时间的，则它是 **弱多项式时间** 的．

例如，计算最大公约数的欧几里得算法，时间复杂度为 𝑂(log⁡𝑎 +log⁡𝑏)O(log⁡a+log⁡b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为输入的数的大小），是弱多项式时间的．

### Pseudo-polynomial time 伪多项式时间

如果一个算法的用时是值域的多项式，则称它是 **伪多项式时间** 的．伪多项式时间的算法可能是多项式时间的也可能不是，可能不是多项式时间是因为表示一个大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正整数一般只需要 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个二进制位，所以关于值域多项式时间的算法往往关于输入长度是指数级时间的．虽然从定义上来说伪多项式时间也可能是多项式时间，但当我们说一个算法是伪多项式时间的，一般都是说这个算法不是多项式时间的．

例如，背包问题是 NP-hard 问题，但它有基于动态规划的伪多项式时间的解法．

如果一个 NPC/NP-hard 问题有伪多项式时间的解法，则称这个问题是 **弱 NPC** /**弱 NP-hard** 问题．如果一个 NPC/NP-hard 问题在 𝖯 ≠𝖭𝖯P≠NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前提下没有伪多项式时间的解法，则称这个问题是 **强 NPC** /**强 NP-hard** 问题．

## 可构造函数

### 时间可构造函数

有时，我们想让图灵机知道自己用了多长的时间，例如，强制图灵机在进行 𝑇(𝑛)T(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步计算后停机．但如果计算 𝑇(𝑛)T(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的用时就超过了 𝑇(𝑛)T(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这便是不可做到的．为此，定义了时间可构造函数，来避免这样的麻烦．

如果存在图灵机 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得输入为 1𝑛1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 1) 时 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能在 𝑂(𝑓(𝑛))O(f(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内停机并且输出 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制表示（注意，这里的图灵机的输出不是接受/不接受，而是一个串，输出可以在纸带上进行），则 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 **时间可构造函数** ．

由于读入需要 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间，𝑜(𝑛)o(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非常值函数都不是时间可构造函数．

### 空间可构造函数

类似地可以定义空间可构造函数．

如果存在图灵机 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得输入为 1𝑛1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 1) 时 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能在 𝑂(𝑓(𝑛))O(f(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的空间内停机并且输出 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制表示，则 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 **空间可构造函数** ．

## 复杂度类之间的关系

### 时间谱系定理

#### 确定性时间谱系定理

若 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个时间可构造函数，则：

𝖣𝖳𝖨𝖬𝖤(𝑜(𝑓(𝑛)log⁡𝑓(𝑛)))⊊𝖣𝖳𝖨𝖬𝖤(𝑓(𝑛))DTIME(o(f(n)log⁡f(n)))⊊DTIME(f(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由确定性时间谱系定理可以得到 𝖯 ⊊𝖤𝖷𝖯𝖳𝖨𝖬𝖤P⊊EXPTIME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

确定性时间谱系定理的证明

定义语言 𝐿 ={(𝑥,𝑦)|U((𝑥,𝑦),𝑥) 在 𝑓(|𝑥| +|𝑦|) 时间内停机并拒绝}L={(x,y)|U((x,y),x) 在 f(|x|+|y|) 时间内停机并拒绝}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由于 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个时间可构造函数，可以根据定义进行计算来判定 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，用时为 𝑂(𝑓(|𝑥| +|𝑦|))O(f(|x|+|y|))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝐿 ∈𝖣𝖳𝖨𝖬𝖤(𝑓(𝑛))L∈DTIME(f(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

现在假设 𝐿 ∈𝖣𝖳𝖨𝖬𝖤(𝑜(𝑓(𝑛)log⁡𝑓(𝑛)))L∈DTIME(o(f(n)log⁡f(n)))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设 𝑀𝑧Mz![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是那台在 𝑜(𝑓(𝑛)log⁡𝑓(𝑛))o(f(n)log⁡f(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内判定 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的图灵机．

令通用图灵机 U(𝑥,𝑧)U(x,z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 关于 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的用时为 𝑔(|𝑥|)g(|x|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由上文关于通用图灵机的介绍可以得到 𝑔(𝑛) =𝑜(𝑓(𝑛))g(n)=o(f(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，当 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 足够大时，𝑔(|𝑧| +|𝑦|) <𝑓(|𝑧| +|𝑦|)g(|z|+|y|)<f(|z|+|y|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

令 𝑦′y′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个足够大的 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 U((𝑧,𝑦′),𝑧)U((z,y′),z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定能在 𝑓(|𝑧| +|𝑦′|)f(|z|+|y′|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内停机，从而 𝑀𝑧(𝑧,𝑦′) ≠𝑀𝑧(𝑧,𝑦′)Mz(z,y′)≠Mz(z,y′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，产生矛盾，所以假设不成立，确定性时间谱系定理证毕．

#### 非确定性时间谱系定理

若 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个时间可构造函数，并且 𝑓(𝑛 +1) =𝑜(𝑔(𝑛))f(n+1)=o(g(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝖭𝖳𝖨𝖬𝖤(𝑓(𝑛)) ⊊𝖭𝖳𝖨𝖬𝖤(𝑔(𝑛))NTIME(f(n))⊊NTIME(g(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由非确定性时间谱系定理可以得到 𝖭𝖯 ⊊𝖭𝖤𝖷𝖯𝖳𝖨𝖬𝖤NP⊊NEXPTIME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 空间谱系定理

若 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个空间可构造函数且 𝑓(𝑛) =Ω(log⁡𝑛)f(n)=Ω(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝖲𝖯𝖠𝖢𝖤(𝑜(𝑓(𝑛))) ⊊𝖲𝖯𝖠𝖢𝖤(𝑓(𝑛))SPACE(o(f(n)))⊊SPACE(f(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

其中 𝖲𝖯𝖠𝖢𝖤SPACE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以代指 𝖣𝖲𝖯𝖠𝖢𝖤DSPACE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝖭𝖲𝖯𝖠𝖢𝖤NSPACE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由空间谱系定理可以得到 𝖯𝖲𝖯𝖠𝖢𝖤 ⊊𝖤𝖷𝖯𝖲𝖯𝖠𝖢𝖤PSPACE⊊EXPSPACE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 萨维奇定理

一台确定性图灵机可以在一台非确定性图灵机所消耗空间的平方内模拟它（尽管消耗的时间可能多很多），即：

若 𝑓(𝑛) =Ω(log⁡𝑛)f(n)=Ω(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则：

𝖭𝖲𝖯𝖠𝖢𝖤(𝑓(𝑛))⊆𝖣𝖲𝖯𝖠𝖢𝖤((𝑓(𝑛))2)NSPACE(f(n))⊆DSPACE((f(n))2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

推论：𝖯𝖲𝖯𝖠𝖢𝖤 =𝖭𝖯𝖲𝖯𝖠𝖢𝖤PSPACE=NPSPACE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝖤𝖷𝖯𝖲𝖯𝖠𝖢𝖤 =𝖭𝖤𝖷𝖯𝖲𝖯𝖠𝖢𝖤EXPSPACE=NEXPSPACE![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### P?=NP

复杂度类 𝖯P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否相等是计算复杂度理论中一个著名的尚未解决的问题．

若 𝖯 =𝖭𝖯P=NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以得到 𝖭𝖯 =𝖼𝗈−𝖭𝖯NP=co−NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但反之不行（目前没有基于 𝖭𝖯 =𝖼𝗈−𝖭𝖯NP=co−NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 证明 𝖯 =𝖭𝖯P=NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方法）．

为什么 NP?=co-NP 不是显然的？

由于 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 问题和与其对应的 𝖼𝗈−𝖭𝖯co−NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 问题答案相反，很容易有这种想法：对于一个 𝖼𝗈−𝖭𝖯co−NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 问题，我只要将解决其补集的非确定性图灵机的输出反过来，就解决了该 𝖼𝗈−𝖭𝖯co−NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 问题，所以 𝖭𝖯 =𝖼𝗈−𝖭𝖯NP=co−NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

实际上，上面所说的这种方法确实能够解决该 𝖼𝗈−𝖭𝖯co−NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 问题，但并没有找到一个非确定性图灵机来解决它：如果一个图灵机所做的事情是将一个非确定性图灵机的输出反过来，该图灵机并不是一个非确定性图灵机．因为，非确定性图灵机接受是在某个分支处接受，而拒绝是在所有分支处拒绝；而将其输出反过来，就变成了接受是在所有分支处，而拒绝是在一个分支处，而这样就不符合非确定性图灵机的定义了，所以能用该图灵机解决这个 𝖼𝗈−𝖭𝖯co−NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 问题并不能使这个 𝖼𝗈−𝖭𝖯co−NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 问题变成一个 𝖭𝖯NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 问题．

若 𝖯 =𝖭𝖯P=NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，还可以得到 𝖤𝖷𝖯𝖳𝖨𝖬𝖤 =𝖭𝖤𝖷𝖯𝖳𝖨𝖬𝖤EXPTIME=NEXPTIME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

若 𝖯 ≠𝖭𝖯P≠NP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以得到 NP-intermediate 不为空．

## 参考资料

  1. [计算复杂性（1）Warming Up: 自动机模型](https://lingeros-tot.github.io/2019/03/05/Warming-Up-自动机模型/)；

  2. [计算复杂性（2）图灵机计算模型](https://lingeros-tot.github.io/2019/03/05/图灵机模型与可计算性/)；

  3. [Wikipedia](https://en.wikipedia.org/) 的相关词条以及这些词条的参考资料．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/cc-basic.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/cc-basic.md "edit.link.title")  
>  __本页面贡献者：[ouuan](https://github.com/ouuan), [Enter-tainer](https://github.com/Enter-tainer), [GreyTigerOIer](https://github.com/GreyTigerOIer), [mgt](mailto:i@margatroid.xyz), [Tiphereth-A](https://github.com/Tiphereth-A), [Backl1ght](https://github.com/Backl1ght), [CCXXXI](https://github.com/CCXXXI), [Chrogeek](https://github.com/Chrogeek), [Great-designer](https://github.com/Great-designer), [Ir1d](https://github.com/Ir1d), [pw384](mailto:pw384@pku.edu.cn)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
