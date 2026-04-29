# 布尔代数 - OI Wiki

- Source: https://oi-wiki.org/math/boolean-algebra/

# 布尔代数

在数理逻辑中，布尔代数（boolean algebra）是代数的一个分支．初等代数中变量的值是数字，其研究的主要运算符有加法、乘法、乘方以及这三种运算的逆运算．而布尔代数中变量的值仅为 **真** 和 **假** 两种（通常记作 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），其研究的主要运算符有合取（与，∧∧![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）、析取（或，∨∨![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）、否定（非，¬¬![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．就像初等代数是描述数字运算的一种形式一样，布尔代数是描述逻辑运算的一种形式．

## 布尔函数

定义

**布尔函数** （boolean function）指的是形如 𝑓 :𝐁𝑘 →𝐁f:Bk→B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的函数，其中 𝐁 ={0,1}B={0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **布尔域** （boolean domain），非负整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为该布尔函数的 **元数** （arity）．𝑘 =1k=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的布尔函数为一元函数，以此类推．𝑘 =0k=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，我们认为函数退化为 𝐁B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的常量．

我们一般只研究一元和二元的布尔函数．如无特殊说明，下文的布尔函数仅限于一元和二元的情况．

除了函数的一般表达方式外，我们还可以用 **真值表** （truth table）、**逻辑门** （logic gate）、[Venn 图](https://en.wikipedia.org/wiki/Venn_diagram) 来表示布尔函数．

真值表

对一个布尔函数，我们枚举其输入的所有情况，并将输入和对应的输出列成一张表，这个表就叫做真值表．

𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元布尔函数也可以用含 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个变量的 **命题公式** （propositional formula）表示，命题公式 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **逻辑等价** （logically equivalent）当且仅当其描述的是同一个布尔函数，记作 𝑝 ⟺ 𝑞p⟺q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

以下是一些常见布尔函数，我们也会把这些布尔函数统称为 **逻辑运算符** （logical connective）或 **逻辑算子** （logical operator）：

名称（数理逻辑）| 其他名称| 记号  
---|---|---  
恒真（truth、tautology）| | ⊤⊤![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
恒假（falsity、contradiction）| | ⊥⊥![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
命题| 自身| 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
否定（negation）| 非（NOT）| ¬𝐴¬A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
合取（conjunction）| 与（AND）| 𝐴 ∧𝐵A∧B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
析取（disjunction）| 或（OR）| 𝐴 ∨𝐵A∨B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
非合取（non-conjunction）| 与非（NAND）、Sheffer 竖线| 𝐴 ¯∧𝐵A∧¯B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝐴 ↑𝐵A↑B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
非析取（non-disjunction）| 或非（NOR）| 𝐴 ¯∨𝐵A∨¯B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝐴 ↓𝐵A↓B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
| 异或（Exclusive-OR，XOR）| 𝐴 ⊕𝐵A⊕B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
| 同或（Exclusive-NOR）| 𝐴 ⊙𝐵A⊙B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
实质蕴含（material implication）2| | 𝐴 →𝐵A→B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
实质非蕴含（material nonimplication）2| | 𝐴 ↛𝐵A↛B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
反蕴涵（converse implication）2| | 𝐴 ←𝐵A←B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
非反蕴涵（converse nonimplication）2| | 𝐴 ↚𝐵A↚B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
双条件（biconditional）、等价（equivalence）23| | 𝐴 ↔𝐵A↔B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
非等价（non-equivalence）24| | 𝐴 ↮𝐵A↮B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
  
对应的真值表（From [Wikipedia](https://commons.wikimedia.org/wiki/File:Logical_connectives_table.svg)）：

![](./images/logical-connectives-table.svg)

对应的 Venn 图和 [Hasse 图](../order-theory/#偏序集的可视化表示hasse-图)（以集合的包含关系 ⊆⊆![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为偏序，From [Wikipedia](https://en.wikipedia.org/wiki/File:Logical_connectives_Hasse_diagram.svg)）：

![](./images/logical-connectives-hasse-diagram.svg)

由于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元布尔函数的输入有 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种，所以 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元布尔函数有 2 ↑(2 ↑𝑛)2↑(2↑n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种，其中 ↑↑![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 Knuth 箭头．

我们把逻辑算子的组合称为 **逻辑表达式** （logical expression）．

如果我们把 𝐁B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 视作模 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个 [剩余类](../number-theory/basic/#同余类与剩余系)，此时异或等价于模 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加法，与等价于模 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 乘法，所以有时我们也用 𝐙2Z2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示布尔域．

### 优先级

一元逻辑算子优先级高于二元逻辑算子，即 ¬¬![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的优先级高于 ∧∧![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、∨∨![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等的优先级．

二元逻辑算子之间的优先级有多种规定，有的资料认为 ∧∧![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、∨∨![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的优先级比 →→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、←←![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、↔↔![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更高，而有的资料持相反观点．所以在使用时推荐多加括号来明确顺序．

C++ 中的规定参见 [C++ 运算符优先级总表](../../lang/op/#c-运算符优先级总表)．

### 自足算子与完备算子集

实际上，我们只用与非或者或非即可表达其余的逻辑算子，CPU 也是基于这一点构建的．但是，由于 **与、或、非、异或** 这四种逻辑算子的性质更好，所以我们在研究布尔代数时一般只使用这四种函数．

如何分别用与非、或非表示其余的逻辑算子

我们有

  * ¬𝑝 =𝑝 ¯∧𝑝 =𝑝 ¯∨𝑝¬p=p∧¯p=p∨¯p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 𝑝 ∧𝑞 =(𝑝 ¯∧𝑞) ¯∧(𝑝 ¯∧𝑞) =(𝑝 ¯∨𝑝) ¯∨(𝑞 ¯∨𝑞)p∧q=(p∧¯q)∧¯(p∧¯q)=(p∨¯p)∨¯(q∨¯q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 𝑝 ∨𝑞 =(𝑝 ¯∧𝑝) ¯∧(𝑞 ¯∧𝑞) =(𝑝 ¯∨𝑞) ¯∨(𝑝 ¯∨𝑞)p∨q=(p∧¯p)∧¯(q∧¯q)=(p∨¯q)∨¯(p∨¯q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 𝑝 →𝑞 =𝑝 ¯∧(𝑞 ¯∧𝑞) =((𝑝 ¯∨𝑝) ¯∨𝑞) ¯∨((𝑝 ¯∨𝑝) ¯∨𝑞)p→q=p∧¯(q∧¯q)=((p∨¯p)∨¯q)∨¯((p∨¯p)∨¯q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

另外

  * 𝑝 =¬¬𝑝p=¬¬p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 𝑝 ↮𝑞 =𝑝 ⊕𝑞 =(𝑝 ∨𝑞) ∧¬(𝑝 ∧𝑞)p↮q=p⊕q=(p∨q)∧¬(p∧q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 𝑝 ↔𝑞 =𝑝 ⊙𝑞 =¬(𝑝 ⊕𝑞)p↔q=p⊙q=¬(p⊕q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 𝑝 ↛𝑞 =¬(𝑝 →𝑞)p↛q=¬(p→q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 𝑝 ←𝑞 =𝑞 →𝑝p←q=q→p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 𝑝 ↚𝑞 =¬(𝑝 ←𝑞)p↚q=¬(p←q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们能不能用指定的若干逻辑算子描述所有的逻辑算子？这便引出了完备算子集的定义．

定义

对一个给定的逻辑算子集，如果能只用这个集合里的函数描述所有的逻辑算子，则称该集合为 **完备算子集** （functionally complete operator set）．特别地，如果只用一个逻辑算子即可描述所有的逻辑算子，则称该算子为 **自足算子** （sole sufficient operator）或 **Sheffer 函数** （Sheffer function）．

如果在一个完备算子集中删去任意一个元素，其都不能描述所有的逻辑算子，则称该集合为 **极小完备算子集** （minimal functionally complete operator set）．

可以证明逻辑算子中只有 ¯∧∧¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、¯∨∨¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是自足算子．

以下为常见的极小完备算子集1：

  * { ¯∧}{∧¯}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ¯∨}{∨¯}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * { ∧,¬}{∧,¬}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ∨,¬}{∨,¬}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ←,¬}{←,¬}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ →,¬}{→,¬}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ↚,¬}{↚,¬}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ↛,¬}{↛,¬}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * { ←,⊥}{←,⊥}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ →,⊥}{→,⊥}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ↚,⊤}{↚,⊤}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ↛,⊤}{↛,⊤}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * { ←, ↚}{←,↚}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ →, ↚}{→,↚}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ←, ↛}{←,↛}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ →, ↛}{→,↛}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * { ←, ↮}{←,↮}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ →, ↮}{→,↮}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ↚, ↔}{↚,↔}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ↛, ↔}{↛,↔}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * { ∨, ↔,⊥}{∨,↔,⊥}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ∨, ↔, ↮}{∨,↔,↮}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ∨, ↮,⊤}{∨,↮,⊤}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * { ∧, ↔,⊥}{∧,↔,⊥}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ∧, ↔, ↮}{∧,↔,↮}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{ ∧, ↮,⊤}{∧,↮,⊤}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 性质

首先是代数结构的相关性质：

  * 与、或均关于 𝐁B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成 [交换幺半群](../algebra/basic/#群)．即与运算和或运算均具有交换律、结合律和幺元（𝑥 ∧1 =𝑥 ∨0 =𝑥x∧1=x∨0=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．
  * 异或、同或均关于 𝐁B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成 [群](../algebra/basic/#群)．即异或运算和同或运算均具有交换律、结合律、幺元（𝑥 ⊕0 =𝑥 ⊙1 =𝑥x⊕0=x⊙1=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）和逆元（𝑥 ⊕𝑥 =0x⊕x=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑥 ⊙𝑥 =1x⊙x=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．
  * 与非、或非均不具有结合律，所以不构成半群．

对于 ∧∧![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、∨∨![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们有

  * 分配律：
    * 𝑎 ∧(𝑏 ⋄𝑐) =(𝑎 ∧𝑏) ⋄(𝑎 ∧𝑐)a∧(b⋄c)=(a∧b)⋄(a∧c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 ⋄⋄![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以为 ∧∧![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、∨∨![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
    * 𝑎 ∨(𝑏 ⋄𝑐) =(𝑎 ∨𝑏) ⋄(𝑎 ∨𝑐)a∨(b⋄c)=(a∨b)⋄(a∨c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 ⋄⋄![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以为 ∧∧![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、∨∨![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、⊙⊙![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * **幂等** （idempotence）律：𝑥 ∧𝑥 =𝑥x∧x=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝑥 ∨𝑥 =𝑥x∨x=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 单调性：𝑎 →𝑏 ⟺ (𝑎 ∧𝑐) →(𝑏 ∧𝑐)a→b⟺(a∧c)→(b∧c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝑎 →𝑏 ⟺ (𝑎 ∨𝑐) →(𝑏 ∨𝑐)a→b⟺(a∨c)→(b∨c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * **吸收** （absorption）律：𝑥 ∧(𝑥 ∨𝑦) =𝑥 ∨(𝑥 ∧𝑦) =𝑥x∧(x∨y)=x∨(x∧y)=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 与「→→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」的关系：
    * 𝑎 ∨𝑏 ⟺ (¬𝑎 →𝑏) ∧(¬𝑏 →𝑎)a∨b⟺(¬a→b)∧(¬b→a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
    * 𝑎 ∧𝑏 ⟺ ¬((𝑎 →¬𝑏) ∨(𝑏 →¬𝑎))a∧b⟺¬((a→¬b)∨(b→¬a))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

布尔函数的单调性

对一个布尔函数 𝑓(𝑥1,…,𝑥𝑛)f(x1,…,xn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐁𝑛Bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的两个元素 (𝑎1,…,𝑎𝑛),(𝑏1,…,𝑏𝑛)(a1,…,an),(b1,…,bn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若当 𝑎𝑖 ≤𝑏𝑖, ∀𝑖 =1,…,𝑛ai≤bi, ∀i=1,…,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时恒有 𝑓(𝑎1,…,𝑎𝑛) ≤𝑓(𝑏1,…,𝑏𝑛)f(a1,…,an)≤f(b1,…,bn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称该布尔函数是单调的．

我们还有如下性质：

  * **排中律** （law of excluded middle）：𝑝 ∨¬𝑝p∨¬p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 恒真．
  * ¬𝑝 ⟺ 𝑝 →⊥¬p⟺p→⊥![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 双重否定/¬¬![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **对合** （involution）律：¬¬𝑥 =𝑥¬¬x=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * ⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、⊙⊙![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的对合律：𝑥 ⊕𝑦 ⊕𝑦 =𝑥x⊕y⊕y=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝑥 ⊙𝑦 ⊙𝑦 =𝑥x⊙y⊙y=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * De Morgan 律：¬(𝑝 ∧𝑞) =¬𝑝 ∨¬𝑞¬(p∧q)=¬p∨¬q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、¬(𝑝 ∨𝑞) =¬𝑝 ∧¬𝑞¬(p∨q)=¬p∧¬q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 逻辑表达式的标准化

根据上述性质，我们可以对逻辑表达式进行一定的等价变换，使其符合特定的范式，这一点可用于自动定理证明中．常见的标准化范式有 **合取范式** （conjunctive normal form，CNF）、**析取范式** （disjunctive normal form，DNF）和 **代数范式** （algebraic normal form，ANF）．

合取范式与析取范式

我们做如下递归式的定义：

  1. **文字** （literal）：对变量 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ¬𝑥¬x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是文字．
  2. 子式：
     * 文字是子式，
     * 若 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是文字、𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是子式，则 𝐴 ∨𝐵A∨B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是子式．
  3. 合取范式：
     * 若 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是子式，则 (𝐴)(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是合取范式，
     * 若 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是子式、𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是合取范式，则 (𝐴) ∧𝐵(A)∧B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是合取范式．

类似地，交换上面定义中的 ∧∧![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 ∨∨![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可得到析取范式的定义．

例如以下逻辑表达式均为析取范式：

  * (𝐴 ∧¬𝐵) ∨(𝐶 ∧𝐷 ∧¬𝐸)(A∧¬B)∨(C∧D∧¬E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * (𝐴 ∧𝐵) ∨(𝐶)(A∧B)∨(C)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * (𝐴 ∧𝐵)(A∧B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * (𝐴)(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

以下逻辑表达式均为合取范式：

  * (¬𝐴 ∨¬𝐵 ∨𝐶) ∧( ∨𝐷 ∨¬𝐸)(¬A∨¬B∨C)∧(∨D∨¬E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * (𝐴 ∨𝐵) ∧(𝐶)(A∨B)∧(C)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * (𝐴 ∨𝐵)(A∨B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * (𝐴)(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

以下逻辑表达式既不为合取范式也不为析取范式：

  * ¬(𝐴 ∧𝐵)¬(A∧B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 𝐴 ∧(𝐵 ∨(𝐶 ∧𝐷))A∧(B∨(C∧D))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们可以通过如下的步骤将任意一个只含有 ¬¬![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、∧∧![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、∨∨![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 运算的逻辑表达式变形为 DNF：

¬¬𝑥↦𝑥,¬(𝑥∨𝑦)↦¬𝑥∧¬𝑦,¬(𝑥∧𝑦)↦¬𝑥∨¬𝑦,𝑥∧(𝑦∨𝑧)↦(𝑥∧𝑦)∨(𝑥∧𝑧),(𝑥∨𝑦)∧𝑧↦(𝑥∧𝑧)∨(𝑦∧𝑧).¬¬x↦x,¬(x∨y)↦¬x∧¬y,¬(x∧y)↦¬x∨¬y,x∧(y∨z)↦(x∧y)∨(x∧z),(x∨y)∧z↦(x∧z)∨(y∧z).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

要得到表达式 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 CNF，只需得到 ¬𝑋¬X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 DNF 后取反并应用 De Morgan 律即可．

代数范式

首先，我们用如下递归式的定义来定义子式：

  * 变量 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是子式，
  * 若 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是子式，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是变量，则 𝑥 ∧𝐴x∧A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是子式．

则满足如下三种形式之一的逻辑表达式为代数范式：

  1. 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  2. 若干不等价子式的异或，如 𝑎 ⊕𝑏 ⊕(𝑎 ∧𝑏) ⊕(𝑎 ∧𝑏 ∧𝑐)a⊕b⊕(a∧b)⊕(a∧b∧c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  3. 若干不等价子式与唯一的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的异或，如 1 ⊕𝑎 ⊕𝑏 ⊕(𝑎 ∧𝑏) ⊕(𝑎 ∧𝑏 ∧𝑐)1⊕a⊕b⊕(a∧b)⊕(a∧b∧c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注意到代数范式和 𝐙2Z2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的多项式一一对应，所以代数范式也被称为 **Zhegalkin 多项式** （Zhegalkin polynomial）．

我们可以通过如下的步骤将任意一个只含有 ¬¬![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、∧∧![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、∨∨![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 运算的逻辑表达式变形为 ANF：

  1. ⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：直接展开，如 (1 ⊕𝑥) ⊕(1 ⊕𝑥 ⊕𝑦) =1 ⊕𝑥 ⊕1 ⊕𝑥 ⊕𝑦 =𝑦(1⊕x)⊕(1⊕x⊕y)=1⊕x⊕1⊕x⊕y=y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  2. ∧∧![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：用分配律展开，如 𝑥 ∧(1 ⊕𝑥 ⊕𝑦) =(𝑥 ∧1) ⊕(𝑥 ∧𝑥) ⊕(𝑥 ∧𝑦) =𝑥 ⊕(𝑥 ∧𝑦)x∧(1⊕x⊕y)=(x∧1)⊕(x∧x)⊕(x∧y)=x⊕(x∧y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  3. ¬¬![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：将 ¬𝑥¬x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 用 1 ⊕𝑥1⊕x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代替，如 ¬(1 ⊕𝑥 ⊕𝑦) =1 ⊕1 ⊕𝑥 ⊕𝑦 =𝑥 ⊕𝑦¬(1⊕x⊕y)=1⊕1⊕x⊕y=x⊕y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  4. ∨∨![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：将 𝑥 ∨𝑦x∨y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 用 1 ⊕((1 ⊕𝑥) ∧(1 ⊕𝑦))1⊕((1⊕x)∧(1⊕y))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑥 ⊕𝑦 ⊕(𝑥 ∧𝑦)x⊕y⊕(x∧y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代替，如 (1 ⊕𝑥) ∨(1 ⊕𝑥 ⊕𝑦) =1 ⊕((1 ⊕1 ⊕𝑥) ∧(1 ⊕1 ⊕𝑥 ⊕𝑦)) =1 ⊕𝑥 ⊕(𝑥 ∧𝑦)(1⊕x)∨(1⊕x⊕y)=1⊕((1⊕1⊕x)∧(1⊕1⊕x⊕y))=1⊕x⊕(x∧y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 参考资料与注释

  1. [Boolean algebra - Wikipedia](https://en.wikipedia.org/wiki/Boolean_algebra)
  2. [Boolean function - Wikipedia](https://en.wikipedia.org/wiki/Boolean_function)
  3. [Logical connective - Wikipedia](https://en.wikipedia.org/wiki/Logical_connective)
  4. [Disjunctive normal form - Wikipedia](https://en.wikipedia.org/wiki/Disjunctive_normal_form)
  5. [Zhegalkin polynomial - Wikipedia](https://en.wikipedia.org/wiki/Zhegalkin_polynomial)

* * *

  1. Vaughan, H. E. (1942). Complete sets of logical functions._Transactions of the American Mathematical Society 51_ : 117–32. ↩

  2. 用于命题推导时应使用双横长箭头，如 𝐴 ⟹ 𝐵A⟹B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝐴 ⟸ 𝐵A⟸B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝐴 ⟺ 𝐵A⟺B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等． ↩↩↩↩↩↩

  3. 等价于同或． ↩

  4. 等价于异或． ↩

* * *

>  __本页面最近更新： 2026/1/27 12:26:08，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/boolean-algebra.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/boolean-algebra.md "edit.link.title")  
>  __本页面贡献者：[c-forrest](https://github.com/c-forrest), [hhc0001](https://github.com/hhc0001), [Tiphereth-A](https://github.com/Tiphereth-A), [TOMWT-qwq](https://github.com/TOMWT-qwq)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
