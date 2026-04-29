# 常系数齐次线性递推 - OI Wiki

- Source: https://oi-wiki.org/math/poly/linear-recurrence/

# 常系数齐次线性递推

## 简介

常系数齐次线性递推数列（又称为 C-finite 或 C-recursive 数列）是常见的一类基础的递推数列．

对于数列 (𝑎𝑗)𝑗≥0(aj)j≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和其递推式

𝑎𝑛=𝑑∑𝑗=1𝑐𝑗𝑎𝑛−𝑗,(𝑛≥𝑑)an=∑j=1dcjan−j,(n≥d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑐𝑗cj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不全为零，我们的目标是在给出初值 𝑎0,…,𝑎𝑑−1a0,…,ad−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和递推式中的 𝑐1,…,𝑐𝑑c1,…,cd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后求出 𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果 𝑘 ≫𝑑k≫d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们想要更快速的算法．

这里 (𝑎𝑗)𝑗≥0(aj)j≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被称为 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶的常系数齐次线性递推数列．

### Fiduccia 算法

Fiduccia 算法使用多项式取模和快速幂来计算 𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，时间为 𝑂(𝖬(𝑑)log⁡𝑘)O(M(d)log⁡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑂(𝖬(𝑑))O(M(d))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示两个次数为 𝑂(𝑑)O(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的多项式相乘的时间．

**算法** ：构造多项式 Γ(𝑥) :=𝑥𝑑 −∑𝑑−1𝑗=0𝑐𝑑−𝑗𝑥𝑗Γ(x):=xd−∑j=0d−1cd−jxj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐴(𝑥) :=∑𝑑−1𝑗=0𝑎𝑗𝑥𝑗A(x):=∑j=0d−1ajxj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么

𝑎𝑘=⟨𝑥𝑘modΓ(𝑥),𝐴(𝑥)⟩ak=⟨xkmodΓ(x),A(x)⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中定义 ⟨(∑𝑛−1𝑗=0𝑓𝑗𝑥𝑗),(∑𝑛−1𝑗=0𝑔𝑗𝑥𝑗)⟩ :=∑𝑛−1𝑗=0𝑓𝑗𝑔𝑗⟨(∑j=0n−1fjxj),(∑j=0n−1gjxj)⟩:=∑j=0n−1fjgj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为内积．

**证明** ：我们定义 Γ(𝑥)Γ(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的友矩阵为

𝐶Γ:=⎡⎢ ⎢ ⎢ ⎢⎣𝑐𝑑1𝑐𝑑−1⋱⋮1𝑐1⎤⎥ ⎥ ⎥ ⎥⎦CΓ:=[cd1cd−1⋱⋮1c1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们定义多项式 𝑏(𝑥) :=∑𝑑−1𝑗=0𝑏𝑗𝑥𝑗b(x):=∑j=0d−1bjxj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和

𝐵𝑏:=[𝑏0𝑏1⋯𝑏𝑑−1]⊺Bb:=[b0b1⋯bd−1]⊺![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

观察到

⎡⎢ ⎢ ⎢ ⎢⎣𝑐𝑑1𝑐𝑑−1⋱⋮1𝑐1⎤⎥ ⎥ ⎥ ⎥⎦⏟___⏟___⏟𝐶Γ⎡⎢ ⎢ ⎢ ⎢⎣𝑏0𝑏1⋮𝑏𝑑−1⎤⎥ ⎥ ⎥ ⎥⎦⏟𝐵𝑏=⎡⎢ ⎢ ⎢ ⎢⎣𝑐𝑑𝑏𝑑−1𝑏0+𝑐𝑑−1𝑏𝑑−1⋮𝑏𝑑−2+𝑐1𝑏𝑑−1⎤⎥ ⎥ ⎥ ⎥⎦⏟___⏟___⏟𝐵𝑥𝑏modΓ[cd1cd−1⋱⋮1c1]⏟CΓ[b0b1⋮bd−1]⏟Bb=[cdbd−1b0+cd−1bd−1⋮bd−2+c1bd−1]⏟BxbmodΓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

且

𝐶Γ=[𝐵𝑥modΓ𝐵𝑥2modΓ⋯𝐵𝑥𝑑modΓ],(𝐶Γ)2=[𝐵𝑥2modΓ𝐵𝑥3modΓ⋯𝐵𝑥𝑑+1modΓ],⋯(𝐶Γ)𝑘=[𝐵𝑥𝑘modΓ𝐵𝑥𝑘+1modΓ⋯𝐵𝑥𝑘+𝑑modΓ]CΓ=[BxmodΓBx2modΓ⋯BxdmodΓ],(CΓ)2=[Bx2modΓBx3modΓ⋯Bxd+1modΓ],⋯(CΓ)k=[BxkmodΓBxk+1modΓ⋯Bxk+dmodΓ]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们将这个递推用矩阵表示有

⎡⎢ ⎢ ⎢ ⎢⎣𝑎𝑘𝑎𝑘+1⋮𝑎𝑘+𝑑−1⎤⎥ ⎥ ⎥ ⎥⎦=⎡⎢ ⎢ ⎢ ⎢⎣1⋱1𝑐𝑑𝑐𝑑−1⋯𝑐1⎤⎥ ⎥ ⎥ ⎥⎦𝑘⏟____⏟____⏟((𝐶Γ)⊺)𝑘=((𝐶Γ)𝑘)⊺⎡⎢ ⎢ ⎢ ⎢⎣𝑎0𝑎1⋮𝑎𝑑−1⎤⎥ ⎥ ⎥ ⎥⎦[akak+1⋮ak+d−1]=[1⋱1cdcd−1⋯c1]k⏟((CΓ)⊺)k=((CΓ)k)⊺[a0a1⋮ad−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可知 ((𝐶Γ)𝑘)⊺((CΓ)k)⊺![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第一行为 𝐵𝑥𝑘modΓBxkmodΓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，根据矩阵乘法的定义得证．

### 表示为有理函数

对于上述数列 (𝑎𝑗)𝑗≥0(aj)j≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定存在有理函数

𝑃(𝑥)𝑄(𝑥)=∑𝑗≥0𝑎𝑗𝑥𝑗P(x)Q(x)=∑j≥0ajxj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

且 𝑄(𝑥) =𝑥𝑑Γ(𝑥−1)Q(x)=xdΓ(x−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，deg⁡𝑃 <𝑑deg⁡P<d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们称其为「**有理函数** 」是因为 𝑃(𝑥),𝑄(𝑥)P(x),Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是「**多项式** 」．

**证明** ：对于 𝑃(𝑥) =∑𝑑−1𝑗=0𝑝𝑗𝑥𝑗P(x)=∑j=0d−1pjxj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑄(𝑥) :=∑𝑑𝑗=0𝑞𝑗𝑥𝑗Q(x):=∑j=0dqjxj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 考虑 𝑃(𝑥)𝑄(𝑥) =∑𝑗≥0˜𝑞𝑗𝑥𝑗P(x)Q(x)=∑j≥0q~jxj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数定义，这几乎就是形式幂级数「**除法** 」的定义，

˜𝑞𝑁=⎧{ { {⎨{ { {⎩𝑝0𝑞−10, if 𝑁=0,(𝑝𝑁−∑𝑁𝑗=1𝑞𝑗˜𝑞𝑁−𝑗)⋅𝑞−10, else if 𝑁<𝑑,−𝑞−10∑𝑑𝑗=1𝑞𝑗˜𝑞𝑁−𝑗, otherwise.q~N={p0q0−1, if N=0,(pN−∑j=1Nqjq~N−j)⋅q0−1, else if N<d,−q0−1∑j=1dqjq~N−j, otherwise.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们只需要令

𝑃(𝑥)=((∑𝑗≥0𝑎𝑗𝑥𝑗)⋅𝑥𝑑Γ(𝑥−1))mod𝑥𝑑P(x)=((∑j≥0ajxj)⋅xdΓ(x−1))modxd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么根据 ˜𝑞𝑁q~N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义，必然有 𝑃(𝑥)𝑄(𝑥) =∑𝑗≥0𝑎𝑗𝑥𝑗P(x)Q(x)=∑j≥0ajxj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### Bostan–Mori 算法

#### 计算单项

我们的目标仍然是给出上述多项式 𝑃(𝑥),𝑄(𝑥)P(x),Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求算 [𝑥𝑘]𝑃(𝑥)𝑄(𝑥)[xk]P(x)Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

Bostan–Mori 算法基于 Graeffe 迭代，对于上述多项式 𝑃(𝑥),𝑄(𝑥)P(x),Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有

𝑃(𝑥)𝑄(𝑥)=𝑃(𝑥)𝑄(−𝑥)𝑄(𝑥)𝑄(−𝑥)=𝑈0(𝑥2)+𝑥𝑈1(𝑥2)𝑉(𝑥2)P(x)Q(x)=P(x)Q(−x)Q(x)Q(−x)=U0(x2)+xU1(x2)V(x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为分母 𝑉(𝑥2)V(x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是偶函数，所以子问题只需考虑其中的一侧

[𝑥𝑘]𝑃(𝑥)𝑄(𝑥)=[𝑥⌊𝑘/2⌋]𝑈𝑘mod2(𝑥)𝑉(𝑥)[xk]P(x)Q(x)=[x⌊k/2⌋]Ukmod2(x)V(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们付出两次多项式乘法的代价使得问题至少减少为原先的一半，而当 𝑘 =0k=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时显然有 [𝑥0]𝑃(𝑥)𝑄(𝑥) =𝑃(0)𝑄(0)[x0]P(x)Q(x)=P(0)Q(0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，时间复杂度同上．

#### 计算连续若干项

目标是给出上述多项式 𝑃(𝑥),𝑄(𝑥)P(x),Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求算 [𝑥[𝐿,𝑅)]𝑃(𝑥)𝑄(𝑥)[x[L,R)]P(x)Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．下面的计算中我们只需考虑对答案「**有影响** 」的系数，这是 Bostan–Mori 算法的关键．

我们不妨假设 deg⁡𝑃 <deg⁡𝑄deg⁡P<deg⁡Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，否则我们也可以通过一次带余除法使问题回到这种情况．

我们先考虑更简单的问题：

[𝑥[𝐿,𝑅)]1𝑄(𝑥)=[𝑥[𝐿,𝑅)]1𝑄(𝑥)𝑄(−𝑥)⋅𝑄(−𝑥)[x[L,R)]1Q(x)=[x[L,R)]1Q(x)Q(−x)⋅Q(−x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们需要求出 [𝑥[𝐿−deg⁡𝑄,𝑅)]1𝑄(𝑥)𝑄(−𝑥)[x[L−deg⁡Q,R)]1Q(x)Q(−x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 然后作一次乘法并取出 𝑥𝐿,…,𝑥𝑅−1xL,…,xR−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数．令 𝑉(𝑥2) =𝑄(𝑥)𝑄( −𝑥)V(x2)=Q(x)Q(−x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么我们只需求出

[𝑥[⌈𝐿−deg⁡𝑄2⌉,⌈𝑅2⌉)]1𝑉(𝑥)[x[⌈L−deg⁡Q2⌉,⌈R2⌉)]1V(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

就可以还原出 [𝑥[𝐿−deg⁡𝑄,𝑅)]1𝑄(𝑥)𝑄(−𝑥)[x[L−deg⁡Q,R)]1Q(x)Q(−x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．进而我们只需求出 [𝑥[𝐿−deg⁡𝑃,𝑅)]1𝑄(𝑥)[x[L−deg⁡P,R)]1Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 再和 𝑃(𝑥)P(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作一次乘法即可求出 [𝑥[𝐿,𝑅)]𝑃(𝑥)𝑄(𝑥)[x[L,R)]P(x)Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

上面的算法虽然已经可以工作，但是每一次的递归的时间复杂度与 𝑅 −𝐿R−L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相关，我们希望能至少在递归求算时摆脱 𝑅 −𝐿R−L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，更具体的，我们先考虑求算 [𝑥[𝐿,𝐿+deg⁡𝑄+1)]1𝑄(𝑥)[x[L,L+deg⁡Q+1)]1Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，考虑

[𝑥[𝐿,𝐿+deg⁡𝑄+1)]1𝑄(𝑥)=[𝑥[𝐿,𝐿+deg⁡𝑄+1)]1𝑄(𝑥)𝑄(−𝑥)⋅𝑄(−𝑥)[x[L,L+deg⁡Q+1)]1Q(x)=[x[L,L+deg⁡Q+1)]1Q(x)Q(−x)⋅Q(−x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们需要求出

[𝑥[𝐿−deg⁡𝑄,𝐿+deg⁡𝑄+1)]1𝑄(𝑥)𝑄(−𝑥)[x[L−deg⁡Q,L+deg⁡Q+1)]1Q(x)Q(−x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么对于 𝑉(𝑥2) =𝑄(𝑥)𝑄( −𝑥)V(x2)=Q(x)Q(−x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而言，我们只需求出

[𝑥[⌈(𝐿−deg⁡𝑄)/2⌉,⌈(𝐿+deg⁡𝑄+1)/2⌉)]1𝑉(𝑥)[x[⌈(L−deg⁡Q)/2⌉,⌈(L+deg⁡Q+1)/2⌉)]1V(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是因为

[𝑥𝑘]1𝑄(𝑥)𝑄(−𝑥)=⎧{ {⎨{ {⎩[𝑥𝑘/2]1𝑉(𝑥),if 𝑘≡0(mod2),0,otherwise.[xk]1Q(x)Q(−x)={[xk/2]1V(x),if k≡0(mod2),0,otherwise.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们知道 𝐿 +deg⁡𝑄L+deg⁡Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐿 −deg⁡𝑄L−deg⁡Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的奇偶性是一样的，所以

⌈𝐿+deg⁡𝑄+12⌉−⌈𝐿−deg⁡𝑄2⌉={deg⁡𝑄+1,if 𝐿+deg⁡𝑄≡0(mod2),deg⁡𝑄,otherwise.⌈L+deg⁡Q+12⌉−⌈L−deg⁡Q2⌉={deg⁡Q+1,if L+deg⁡Q≡0(mod2),deg⁡Q,otherwise.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这样我们可以写出伪代码

𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦 Slice-Coefficients⁡(𝑄,𝐿):𝐈𝐧𝐩𝐮𝐭: 𝑄(𝑥)∈ℂ[𝑥],𝐿∈ℤ.𝐎𝐮𝐭𝐩𝐮𝐭: [𝑥[𝐿,𝐿+deg⁡𝑄+1)]𝑄(𝑥)−1.1𝐢𝐟 𝐿≤1 𝐭𝐡𝐞𝐧 𝐫𝐞𝐭𝐮𝐫𝐧 [𝑥[𝐿,𝐿+deg⁡𝑄+1)]𝑄(𝑥)−1Use other algorithm to compute 𝑄(𝑥)−12𝑉(𝑥2)←𝑄(𝑥)𝑄(−𝑥)3𝑘←⌈𝐿−deg⁡𝑄2⌉4(𝑡𝑘,…,𝑡𝑘+deg⁡𝑄)←Slice-Coefficients⁡(𝑉,𝑘)5𝑇(𝑥)←𝑥(𝐿−deg⁡𝑄)mod2∑deg⁡𝑄𝑗=0𝑡𝑗+𝑘𝑥2𝑗6𝐫𝐞𝐭𝐮𝐫𝐧 [𝑥[deg⁡𝑄,2deg⁡𝑄+1)]𝑇(𝑥)𝑄(−𝑥)Algorithm Slice-Coefficients⁡(Q,L):Input: Q(x)∈C[x],L∈Z.Output: [x[L,L+deg⁡Q+1)]Q(x)−1.1if L≤1 then return [x[L,L+deg⁡Q+1)]Q(x)−1Use other algorithm to compute Q(x)−12V(x2)←Q(x)Q(−x)3k←⌈L−deg⁡Q2⌉4(tk,…,tk+deg⁡Q)←Slice-Coefficients⁡(V,k)5T(x)←x(L−deg⁡Q)mod2∑j=0deg⁡Qtj+kx2j6return [x[deg⁡Q,2deg⁡Q+1)]T(x)Q(−x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

但是只有这个算法还不够，我们需要重新找到一个有理函数并求算更多系数．

#### 找到新的有理函数表示

我们知道 𝑄(𝑥)Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 本身和 𝑄(𝑥)−1Q(x)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一部分连续的系数比如 [𝑥[𝐿,𝐿+deg⁡𝑄)]𝑄(𝑥)−1[x[L,L+deg⁡Q)]Q(x)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐿 ≥0L≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们希望求出 [𝑥[𝐿+deg⁡𝑄,𝐿+2deg⁡𝑄)]𝑄(𝑥)−1[x[L+deg⁡Q,L+2deg⁡Q)]Q(x)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这等价于我们要求某个 𝑃(𝑥)P(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 deg⁡𝑃 <deg⁡𝑄deg⁡P<deg⁡Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑃(𝑥)𝑄(𝑥)P(x)Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前 deg⁡𝑄deg⁡Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项与 [𝑥[𝐿,𝐿+deg⁡𝑄)]𝑄(𝑥)−1[x[L,L+deg⁡Q)]Q(x)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相同．简单来说：递推关系（有理函数的分母）是不变的，我们所做的只是更换初值（有理函数的分子）．

具体的，考虑

𝑃(𝑥)𝑄(𝑥)=∑𝑗≥0𝑎𝑗𝑥𝑗P(x)Q(x)=∑j≥0ajxj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们现在希望将递推前进 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项，那么就是

∑𝑗≥𝑛𝑎𝑗𝑥𝑗−𝑛=𝑃(𝑥)𝑄(𝑥)𝑥𝑛−𝑄(𝑥)∑𝑛−1𝑗=0𝑎𝑗𝑥𝑗𝑄(𝑥)𝑥𝑛∑j≥najxj−n=P(x)Q(x)xn−Q(x)∑j=0n−1ajxjQ(x)xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们先用一次 Slice-Coefficients⁡(𝑄,𝐿 −deg⁡𝑃)Slice-Coefficients⁡(Q,L−deg⁡P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算出 [𝑥[𝐿−deg⁡𝑃,𝐿−deg⁡𝑃+deg⁡𝑄+1)]𝑄(𝑥)−1[x[L−deg⁡P,L−deg⁡P+deg⁡Q+1)]Q(x)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后我们扩展合并出 [𝑥[𝐿−deg⁡𝑃,𝐿+deg⁡𝑄)]𝑄(𝑥)−1[x[L−deg⁡P,L+deg⁡Q)]Q(x)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再重新计算一个分子使得

̃𝑃(𝑥)𝑄(𝑥)=∑𝑗≥0([𝑥𝐿+𝑗]𝑃(𝑥)𝑄(𝑥))𝑥𝑗P~(x)Q(x)=∑j≥0([xL+j]P(x)Q(x))xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

最后我们使用形式幂级数的除法计算出 [𝑥[0,𝑅−𝐿)]̃𝑃(𝑥)𝑄(𝑥)[x[0,R−L)]P~(x)Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，时间为 𝑂(𝖬(𝑑)log⁡𝐿 +𝖬(𝑅 −𝐿))O(M(d)log⁡L+M(R−L))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 参考文献

  1. Alin Bostan, Ryuhei Mori.[A Simple and Fast Algorithm for Computing the 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)-th Term of a Linearly Recurrent Sequence](https://arxiv.org/abs/2008.08822).

* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/linear-recurrence.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/linear-recurrence.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [hly1204](https://github.com/hly1204), [QAQAutoMaton](https://github.com/QAQAutoMaton), [Marcythm](https://github.com/Marcythm), [97littleleaf11](https://github.com/97littleleaf11), [ksyx](https://github.com/ksyx), [shuzhouliu](https://github.com/shuzhouliu), [abc1763613206](https://github.com/abc1763613206), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [Early0v0](https://github.com/Early0v0), [EndlessCheng](https://github.com/EndlessCheng), [fps5283](https://github.com/fps5283), [Great-designer](https://github.com/Great-designer), [H-J-Granger](https://github.com/H-J-Granger), [hsfzLZH1](https://github.com/hsfzLZH1), [huayucaiji](https://github.com/huayucaiji), [Ir1d](https://github.com/Ir1d), [kenlig](https://github.com/kenlig), [ouuan](mailto:1609483441@qq.com), [ouuan](https://github.com/ouuan), [qz-cqy](https://github.com/qz-cqy), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [test12345-pupil](https://github.com/test12345-pupil), [thredreams](https://github.com/thredreams), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [untitledunrevised](https://github.com/untitledunrevised), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
