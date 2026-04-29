# Lagrange 反演 - OI Wiki

- Source: https://oi-wiki.org/math/poly/lagrange-inversion/

# Lagrange 反演

## 形式 Laurent 级数

我们已经知道形式幂级数环 ℂ[[𝑥]]C[[x]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 了，定义形式 Laurent 级数环：

ℂ((𝑥)):={∑𝑘≥𝑁𝑎𝑘𝑥𝑘:𝑁∈ℤ,𝑎𝑘∈ℂ}C((x)):={∑k≥Nakxk:N∈Z,ak∈C}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们可以仿照形式幂级数的乘法逆元定义来定义 ℂ((𝑥))C((x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上元素的乘法逆元：

若对于 𝑓 :=∑𝑘≥𝑁𝑓𝑘𝑥𝑘f:=∑k≥Nfkxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓𝑁 ≠0fN≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在 𝑔 =∑𝑘≥−𝑁𝑔𝑘𝑥𝑘g=∑k≥−Ngkxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑓𝑔 =1fg=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么

𝑔𝑘:={𝑓−1𝑁, if 𝑘=−𝑁,−𝑓−1𝑁∑𝑖>𝑁𝑓𝑖𝑔𝑘−𝑖, otherwisegk:={fN−1, if k=−N,−fN−1∑i>Nfigk−i, otherwise![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

与形式幂级数类似的，我们也对非零的 𝑓(𝑥) =∑𝑘≥𝑁𝑓𝑘𝑥𝑘f(x)=∑k≥Nfkxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 定义：

ord⁡𝑓:=min{𝑘:𝑓𝑘≠0}ord⁡f:=min{k:fk≠0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

显然对于 𝑔 ≠0g≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有

ord⁡(𝑓𝑔)=ord⁡(𝑓)+ord⁡(𝑔)ord⁡(fg)=ord⁡(f)+ord⁡(g)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 形式留数

形式留数是形式 Laurent 级数中 𝑥−1x−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项的系数．记 res⁡𝑓 :=[𝑥−1]𝑓res⁡f:=[x−1]f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**引理** ：对于任何形式 Laurent 级数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 res⁡𝑓′ =0res⁡f′=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**证明** ：考虑形式导数的定义 (𝑥𝑘)′ =𝑘𝑥𝑘−1(xk)′=kxk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**引理** ：对于任何形式 Laurent 级数 𝑓,𝑔f,g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 res⁡(𝑓′𝑔) = −res⁡(𝑓𝑔′)res⁡(f′g)=−res⁡(fg′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**证明** ：考虑乘法法则 (𝑓𝑔)′ =𝑓′𝑔 +𝑓𝑔′(fg)′=f′g+fg′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所以 0 =res⁡((𝑓𝑔)′) =res⁡(𝑓′𝑔) +res⁡(𝑓𝑔′)0=res⁡((fg)′)=res⁡(f′g)+res⁡(fg′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**引理** ：对于形式 Laurent 级数 𝑓(𝑥) ≠0f(x)≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 res⁡(𝑓′/𝑓) =ord⁡𝑓res⁡(f′/f)=ord⁡f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**证明** ：设 ord⁡𝑓 =𝑘ord⁡f=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么

res⁡(𝑓′𝑓)=res⁡(𝑘𝑓𝑘𝑥𝑘−1+⋯𝑓𝑘𝑥𝑘+𝑓𝑘+1𝑥𝑘+1+⋯)=res⁡(𝑘𝑓𝑘𝑥−1+⋯𝑓𝑘+𝑓𝑘+1𝑥+⋯)=𝑘res⁡(f′f)=res⁡(kfkxk−1+⋯fkxk+fk+1xk+1+⋯)=res⁡(kfkx−1+⋯fk+fk+1x+⋯)=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**引理** ：对于形式 Laurent 级数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和形式幂级数 𝑔 ≠0g≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 res⁡(𝑓)ord⁡(𝑔) =res⁡(𝑓(𝑔)𝑔′)res⁡(f)ord⁡(g)=res⁡(f(g)g′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**证明** ：考虑线性性，我们只需证明 𝑓 =𝑥𝑘f=xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 其中 𝑘 ∈ℤk∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况即可，若 𝑘 ≠ −1k≠−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么

res⁡𝑥𝑘=0res⁡(𝑔𝑘𝑔′)=res⁡(1𝑘+1(𝑔𝑘+1)′)=1𝑘+1res⁡((𝑔𝑘+1)′)=0res⁡xk=0res⁡(gkg′)=res⁡(1k+1(gk+1)′)=1k+1res⁡((gk+1)′)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若 𝑘 = −1k=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么

res⁡𝑓=res⁡(𝑥−1)=1res⁡(𝑓(𝑔)𝑔′)=res⁡(𝑔′/𝑔)=ord⁡(𝑔)=res⁡(𝑓)ord⁡(𝑔)res⁡f=res⁡(x−1)=1res⁡(f(g)g′)=res⁡(g′/g)=ord⁡(g)=res⁡(f)ord⁡(g)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 复合逆

记 𝐴(𝑥) ∘𝐵(𝑥) :=𝐴(𝐵(𝑥))A(x)∘B(x):=A(B(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**命题** ：𝑓(𝑥) :=∑𝑘≥1𝑓𝑘𝑥𝑘f(x):=∑k≥1fkxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在复合逆 𝑓⟨−1⟩(𝑥)f⟨−1⟩(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当 𝑓(0) =0 ≠𝑓′(0)f(0)=0≠f′(0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时 𝑓⟨−1⟩(𝑥)f⟨−1⟩(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是唯一的．进一步说：若 𝑔(𝑥) =∑𝑘≥1𝑔𝑘𝑥𝑘g(x)=∑k≥1gkxk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑓(𝑔(𝑥)) =𝑥f(g(x))=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑔(𝑓(𝑥)) =𝑥g(f(x))=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么 𝑔(𝑥) =𝑓⟨−1⟩(𝑥)g(x)=f⟨−1⟩(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**证明** ：考虑

𝑔(𝑓(𝑥))=𝑔1(𝑓1𝑥+𝑓2𝑥2+𝑓3𝑥3+⋯)+𝑔2(𝑓1𝑥+𝑓2𝑥2+⋯)2+𝑔3(𝑓1𝑥+⋯)3+⋯=𝑔1𝑓1𝑥+(𝑔1𝑓2+𝑔2𝑓21)𝑥2+(𝑔1𝑓3+2𝑔2𝑓1𝑓2+𝑔3𝑓31)𝑥3+⋯g(f(x))=g1(f1x+f2x2+f3x3+⋯)+g2(f1x+f2x2+⋯)2+g3(f1x+⋯)3+⋯=g1f1x+(g1f2+g2f12)x2+(g1f3+2g2f1f2+g3f13)x3+⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 𝑔(𝑓(𝑥)) =𝑥g(f(x))=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所以有下面的方程组

⎧{ { {⎨{ { {⎩𝑔1𝑓1=1𝑔1𝑓2+𝑔2𝑓21=0𝑔1𝑓3+2𝑔2𝑓1𝑓2+𝑔3𝑓31=0⋮{g1f1=1g1f2+g2f12=0g1f3+2g2f1f2+g3f13=0⋮![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们只能在 𝑓1 ≠0f1≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时才能解出第一个等式，然后依次可以解出 𝑔2,…g2,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

特别的，考虑 𝑓(ℎ(𝑥)) =𝑥f(h(x))=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么 𝑔(𝑓(ℎ(𝑥))) =𝑔(𝑥)g(f(h(x)))=g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进而 𝑔(𝑥) =𝑔 ∘𝑓 ∘ℎ(𝑥) =𝑥 ∘ℎ(𝑥) =ℎ(𝑥)g(x)=g∘f∘h(x)=x∘h(x)=h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## Lagrange 反演公式

令 𝑓(𝑥),𝑔(𝑥) ∈ℂ[[𝑥]]f(x),g(x)∈C[[x]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑓(𝑔(𝑥)) =𝑔(𝑓(𝑥)) =𝑥f(g(x))=g(f(x))=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．取 Φ(𝑥) ∈ℂ[[𝑥]]Φ(x)∈C[[x]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（或 Φ(𝑥) ∈ℂ((𝑥))Φ(x)∈C((x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），那么

[𝑥𝑛]Φ(𝑓(𝑥))=[𝑥𝑛−1]Φ(𝑥)𝑔′(𝑥)𝑔(𝑥)(𝑥𝑔(𝑥))𝑛=[𝑥−1]Φ(𝑥)𝑔′(𝑥)𝑔(𝑥)𝑛+1[xn]Φ(f(x))=[xn−1]Φ(x)g′(x)g(x)(xg(x))n=[x−1]Φ(x)g′(x)g(x)n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**证明** ：

[𝑥𝑛]Φ(𝑓(𝑥))=res⁡(Φ(𝑓(𝑥))𝑥𝑛+1)=res⁡(Φ(𝑓(𝑔(𝑥)))𝑔′(𝑥)𝑔(𝑥)𝑛+1)⋅(ord⁡(𝑔(𝑥)))−1=res⁡(Φ(𝑥)𝑔′(𝑥)𝑔(𝑥)𝑛+1)[xn]Φ(f(x))=res⁡(Φ(f(x))xn+1)=res⁡(Φ(f(g(x)))g′(x)g(x)n+1)⋅(ord⁡(g(x)))−1=res⁡(Φ(x)g′(x)g(x)n+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

一些读者可能会更加熟悉下面的版本：对于 𝑘 ∈ℤ≥0,𝑛 ∈ℤ>0k∈Z≥0,n∈Z>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有

[𝑥𝑛]𝑓(𝑥)𝑘=𝑘𝑛[𝑥𝑛−𝑘](𝑥𝑔(𝑥))𝑛[xn]f(x)k=kn[xn−k](xg(x))n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

或者

[𝑥𝑛]Φ(𝑓(𝑥))=1𝑛[𝑥𝑛−1]Φ′(𝑥)(𝑥𝑔(𝑥))𝑛=1𝑛[𝑥−1]Φ′(𝑥)𝑔(𝑥)𝑛[xn]Φ(f(x))=1n[xn−1]Φ′(x)(xg(x))n=1n[x−1]Φ′(x)g(x)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

发现

res⁡(Φ′(𝑥)𝑔(𝑥)𝑛−𝑛Φ(𝑥)𝑔′(𝑥)𝑔(𝑥)𝑛+1)=res⁡((Φ(𝑥)𝑔(𝑥)𝑛)′)=0res⁡(Φ′(x)g(x)n−nΦ(x)g′(x)g(x)n+1)=res⁡((Φ(x)g(x)n)′)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以通过我们已经证明的部分导出．

## 参考文献

  1. Richard P. Stanley and Sergey P. Fomin. Enumerative Combinatorics Volume 2 (Edition 1).
  2. Ira M. Gessel. Lagrange Inversion.

* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/lagrange-inversion.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/lagrange-inversion.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [hly1204](https://github.com/hly1204)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
