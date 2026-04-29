# 弧度制与坐标系 - OI Wiki

- Source: https://oi-wiki.org/math/coordinate/

# 弧度制与坐标系

## 角的定义

在小学或初中已经学习过角的 **静态定义** ：具有公共端点的两条射线组成的图形叫做角．

但是该定义将角度限制在了 [0,360∘][0,360∘]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这给深入研究带来了一定的困难，还有其他的问题无法解释清，比如：旋转 720∘720∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是什么意思？

在高中数学，讲了角的 **动态定义** ：平面内一条射线绕其端点从一个位置旋转到另一个位置形成的图形叫做角．

开始的位置称为 **始边** ，结束的位置称为 **终边** ．并规定：

  * 按 **逆时针** 方向旋转形成的角叫做 **正角** ，其角度为正；
  * 按 **顺时针** 方向旋转形成的角叫做 **负角** ，其角度为负；
  * 终边相对于始边没有做任何旋转的角叫做 **零角** ，其角度为 0∘0∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这样就把角的概念推向了 **任意角** ．

注意

零角始边和终边重合，但始边和终边重合的角并不都是零角，如以 360∘360∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为倍数的角．

## 弧度制

实际应用中经常有角度到各种参数的转换，而使用弧度制描述角可以减少系数的使用．所以接下来，介绍 **弧度制** ：

把长度等于半径长的弧所对的圆心角称为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 弧度的角，用符号 radrad![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示，读作：弧度．

根据前面的规定，正角的弧度为正，负角的弧度为负，零角的弧度为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果半径为 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的圆的圆心角 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所对弧长为 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则：

|𝛼|=𝑙𝑟|α|=lr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用这个公式还可以写出弧长和扇形面积公式，在此略过．

于是，360∘360∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 角的弧度为 2𝜋2π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样有了对应关系之后就可以进行角度值和弧度制的转化了：

𝑘rad=𝜋180∘𝑛∘krad=π180∘n∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

考虑一个角，将其终边再旋转一周，甚至多周，始边位置不动，那么终边位置永远是相同的，称这些角为终边位置相同的角．

与角 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 终边位置相同的角的集合很容易得出，为 {𝜑 ∣𝜑 =𝛼 +2𝑘𝜋,𝑘 ∈𝐙}{φ∣φ=α+2kπ,k∈Z}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

可以理解为：给这个角的边不停加转一圈，终边位置不变．

𝜋π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝜏τ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两个数学常数

目前西方数学界有一些观点认为，「真正的圆周率」应为 2𝜋2π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将这个值记为希腊字母 𝜏τ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．新圆周率的支持者们选择在 6 月 28 日庆祝「真正的」圆周率日．

比如，在弧度制下，一个周角是 2𝜋2π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，直接对 2𝜋2π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行等分可以得到周角的等分．又例如，在复变函数中频繁出现 2𝜋2π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的组合，等等．

为了迎合中国各地区约定俗成的习惯，在 **OI Wiki** ，采用参数 𝜋π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示圆周率．

编程中圆周率的习惯写法

在 C/C++ 语言中，一般取 𝜋π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 `acos(-1)`，只有这个值是最接近 𝜋π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的浮点数．使用 `acos(-1)` 或者 `4 * atan(1)` 写出来的 𝜋π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 3.141592653589793100003.14159265358979310000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

采用其他值，例如 `acos(-1.0/2.0)`，`acos(1.0/2.0)`，`asin(1.0/2.0)` 等等，写出来的 𝜋π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 3.141592653589793600003.14159265358979360000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这就不是最接近 𝜋π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的浮点数了．

如果你背得下来，也可以直接写 3.14159265358979323.1415926535897932![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 平面直角坐标系

在同一个平面上互相垂直且有公共原点的两条数轴构成平面直角坐标系（Rectangular Coordinates）．

通常，两条数轴分别置于水平位置与垂直位置，取向右与向上的方向分别为两条数轴的正方向．水平的数轴叫做 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴（x-axis）或横轴，垂直的数轴叫做 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴（y-axis）或纵轴，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴统称为坐标轴，它们的公共原点 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为平面直角坐标系的原点（origin），以点 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为原点的平面直角坐标系记作平面直角坐标系 𝑥𝑂𝑦xOy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴将坐标平面分成了四个象限（quadrant），右上方的部分叫做第一象限，其他三个部分按逆时针方向依次叫做第二象限、第三象限和第四象限．象限以数轴为界，横轴、纵轴上的点及原点不在任何一个象限内．一般情况下，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴取相同的单位长度，但在特殊的情况下，也可以取不同的单位长度．

### 平面直角坐标系下位置的描述

在平面直角坐标系中，对于平面上的任意一点，都有唯一的一个有序数对（即点的坐标（coordinates））与它对应；反过来，对于任意一个有序数对，都有平面上唯一的一点与它对应．

对于平面内任意一点 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，过点 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别向 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴、𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴作垂线，垂足在 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴、𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴上的对应点 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别叫做点 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的横坐标、纵坐标，有序数对（ordered pair）(𝑎,𝑏)(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 叫做点 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的直角坐标．一个点在不同的象限或坐标轴上，其坐标都不一样．

## 平面极坐标系

考虑实际情况，比如航海，说「点 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在点 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的北偏东 30∘30∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 方向上，距离为 100100![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 米」，而不是「以 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为原点建立平面直角坐标系，𝐵(50,50√3)B(50,503)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」．

这样：

  1. 在平面上选一定点 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称为 **极点** ；
  2. 自极点引出一条射线 𝑂𝑥Ox![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称为 **极轴** ；
  3. 选择一个单位长度（在数学问题中通常为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），一个角度单位（通常为弧度）及其正方向（通常为逆时针方向）；

就建立了 **极坐标系** ．

### 极坐标系下位置的描述

设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为平面上一点．

  * 极点 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的距离 |𝑂𝐴||OA|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 **极径** ，记为 𝜌ρ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 以极轴为始边，𝑂𝐴OA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为终边的角 ∠𝑥𝑂𝐴∠xOA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 **极角** ，记为 𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；

那么有序数对 (𝜌,𝜑)(ρ,φ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **极坐标** ．

由终边相同的角的定义可知，(𝜌,𝜑)(ρ,φ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 (𝜌,𝜑 +2𝑘𝜋) (𝑘 ∈𝐙)(ρ,φ+2kπ) (k∈Z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 其实表示的是一样的点．特别地，极点的极坐标为 (0,𝜑) (𝜑 ∈𝐑)(0,φ) (φ∈R)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，于是平面内的点的极坐标表示有无数多种．

如果规定 𝜌 ≥0,0 ≤𝜑 <2𝜋ρ≥0,0≤φ<2π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么除极点外，其他平面内的点可以用唯一有序数对 (𝜌,𝜑)(ρ,φ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示，而极坐标 (𝜌,𝜑)(ρ,φ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示的点是唯一确定的．

### 平面直角坐标系与极坐标系的相互转换

当然，有时候研究极坐标系下的图形有些不方便．要想转到直角坐标系下研究，有互化公式．点 𝐴(𝜌,𝜑)A(ρ,φ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的直角坐标 (𝑥,𝑦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以如下表示：

𝑥=𝜌cos⁡𝜑𝑦=𝜌sin⁡𝜑x=ρcos⁡φy=ρsin⁡φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

进而可知：

𝜌2=𝑥2+𝑦2tan⁡𝜑=𝑦𝑥 (𝑥≠0)ρ2=x2+y2tan⁡φ=yx (x≠0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是有 𝜌 =√𝑥2+𝑦2ρ=x2+y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

但具有相同 𝑦𝑥yx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 tan⁡𝜑tan⁡φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有两个可能的 𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，此时还需要根据 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值来确定方向．具体地，定义函数：

atan2⁡(𝑦,𝑥)=⎧{ { { { {⎨{ { { { {⎩arctan⁡(𝑦𝑥)if 𝑥>0arctan⁡(𝑦𝑥)+𝜋if 𝑦≥0,𝑥<0arctan⁡(𝑦𝑥)−𝜋if 𝑦<0,𝑥<0𝜋/2if 𝑦>0,𝑥=0−𝜋/2if 𝑦<0,𝑥=0anyif 𝑦=0,𝑥=0atan2⁡(y,x)={arctan⁡(yx)if x>0arctan⁡(yx)+πif y≥0,x<0arctan⁡(yx)−πif y<0,x<0π/2if y>0,x=0−π/2if y<0,x=0anyif y=0,x=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则 𝜑 =atan2⁡(𝑦,𝑥)φ=atan2⁡(y,x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．注意上述函数的值域为 ( −𝜋,𝜋](−π,π]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在 C/C++ 语言的 `<math.h>` 或 `<cmath>` 库里定义了 [该函数](https://zh.cppreference.com/w/cpp/numeric/math/atan2)，调用 `atan2(y, x)` 即可．

## 空间直角坐标系

使用如下方法建立空间直角坐标系：

  1. 在空间内选定一点 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 过点 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作三条互相垂直的数轴 ⟶𝑂𝑥,⟶𝑂𝑦,⟶𝑂𝑧Ox→,Oy→,Oz→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，分别称作 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴（横轴），𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴（纵轴），𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴（竖轴），统称为坐标轴；它们的正方向符合右手规则，即以右手握住 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴，当右手的四个手指 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴的正向以角度转向 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴正向时，大拇指的指向就是 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴的正向；
  3. 设定各轴上的长度单位，通常都设为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这样就构成了一个空间直角坐标系，称为空间直角坐标系 𝑂 −𝑥𝑦𝑧O−xyz![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．定点 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为该坐标系的原点．

任意两条坐标轴确定一个平面，这样可确定三个互相垂直的平面，统称为坐标面．其中 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴与 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴所确定的坐标面称为 𝑥𝑂𝑦xOy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 面，类似地有 𝑦𝑂𝑧yOz![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 面和 𝑧𝑂𝑥zOx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 面．三个坐标面把空间分成八个部分，每一部分称为一个卦限．

### 空间直角坐标系下位置的描述

取定空间直角坐标系 𝑂 −𝑥𝑦𝑧O−xyz![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，就可以建立空间的点与三元组之间的一一对应关系．

设点 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为空间的一点，过点 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别作垂直于 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴、𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴和 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴的平面．设三个平面与 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴、𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴和 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴的交点依次为 𝑃,𝑄,𝑅P,Q,R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，点 𝑃,𝑄,𝑅P,Q,R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别称为点 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴、𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴和 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴上的投影．又设点 𝑃,𝑄,𝑅P,Q,R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴、𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴和 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴上的坐标依次为 𝑥,𝑦,𝑧x,y,z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，于是点 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 确定了一个三元组 (𝑥,𝑦,𝑧)(x,y,z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

反之，如果给定一个三元组 (𝑥,𝑦,𝑧)(x,y,z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以在 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴上取坐标为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴上取坐标为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴上取坐标为 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后点 𝑃,𝑄,𝑅P,Q,R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别作垂直于 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴、𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴和 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴的三个平面，它们相交于空间的一点 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，点 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是由三元组 (𝑥,𝑦,𝑧)(x,y,z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所确定的点．

这样一来，空间的点 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与三元组 (𝑥,𝑦,𝑧)(x,y,z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间就建立了一一对应的关系．把三元组 (𝑥,𝑦,𝑧)(x,y,z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为点 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的坐标，记作 𝑀(𝑥,𝑦,𝑧)M(x,y,z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为横坐标、𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为纵坐标、𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为竖坐标．

## 空间柱坐标系

空间柱坐标系，将极坐标扩展为三维的方式：从应用于平面工作中的极坐标系开始，然后过极点 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 添加垂直于该平面的 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴，方向朝上．

为了找到由柱坐标 (𝜌,𝜑,𝑧)(ρ,φ,z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所描述的点，可以首先在极坐标系下处理 𝜌ρ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后根据 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 坐标沿着 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴「向上」或「向下」移动．

### 柱坐标系与空间直角坐标系的相互转换

两坐标系下 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值是相同的．

(𝑥,𝑦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 (𝜌,𝜑)(ρ,φ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的相互转换参见上文 平面直角坐标系与极坐标系的相互转换．

## 空间球坐标系

球坐标可以通过以下方法确定：

  1. 站在原点，面向水平极轴的方向；垂直轴的指向是从脚指向头部；
  2. 手臂向上，指向垂直极轴方向；
  3. 逆时针旋转角度 𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  4. 将手臂向下旋转角度 𝜗ϑ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，手臂指向 𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝜗ϑ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指定的方向；
  5. 沿着该方向从原点移位距离 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这样即可到达球坐标 (𝑟,𝜗,𝜑)(r,ϑ,φ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所描述的点．其中 𝜗ϑ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 **天顶角** ，𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 **方位角** ．

Warning

由于诸多原因，有的地方使用 𝜙ϕ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示天顶角，用 𝜃θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示方位角．阅读文章遇到球坐标系时请务必注意这一点．

同时，在写文章时，如果用到了球坐标系，建议提前声明清楚使用什么符号表示天顶角和方位角．

### 柱坐标系与球坐标系的相互转换

两坐标系下 𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值是相同的．

从柱坐标系到球坐标系：

𝑟=√𝜌2+𝑧2𝜗=⎧{ {⎨{ {⎩arctan⁡(𝜌𝑧)if 𝑧>0𝜋/2if 𝑧=0,𝜌≠0arctan⁡(𝜌𝑧)+𝜋if 𝑧<0r=ρ2+z2ϑ={arctan⁡(ρz)if z>0π/2if z=0,ρ≠0arctan⁡(ρz)+πif z<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意对于柱坐标系下的点 (0,0,0)(0,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其球坐标的 𝜗ϑ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不明确．

从球坐标系到柱坐标系：

𝜌=𝑟sin⁡𝜗𝑧=𝑟cos⁡𝜗ρ=rsin⁡ϑz=rcos⁡ϑ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 空间直角坐标系与球坐标系的相互转换

可以结合上文 平面直角坐标系与极坐标系的相互转换 和上文 柱坐标系与球坐标系的相互转换 一起使用，或直接使用下面的公式：

从空间直角坐标系到球坐标系：

𝑟=√𝑥2+𝑦2+𝑧2𝜗=arccos⁡(𝑧√𝑥2+𝑦2+𝑧2)𝜑=atan2⁡(𝑦,𝑥)r=x2+y2+z2ϑ=arccos⁡(zx2+y2+z2)φ=atan2⁡(y,x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 atan2atan2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义见 平面直角坐标系与极坐标系的相互转换．

注意对于空间直角坐标系下的点 (0,0,0)(0,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其球坐标的 𝜗ϑ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取值不明确．

从球坐标系到空间直角坐标系：

𝑥=𝑟sin⁡𝜗cos⁡𝜑𝑦=𝑟sin⁡𝜗sin⁡𝜑𝑧=𝑟cos⁡𝜗x=rsin⁡ϑcos⁡φy=rsin⁡ϑsin⁡φz=rcos⁡ϑ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/coordinate.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/coordinate.md "edit.link.title")  
>  __本页面贡献者：[mxdyzmx](https://github.com/mxdyzmx), [shuzhouliu](https://github.com/shuzhouliu), [Tiphereth-A](https://github.com/Tiphereth-A), [abc1763613206](https://github.com/abc1763613206), [aofall](https://github.com/aofall), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [chieh2lu2](https://github.com/chieh2lu2), [Chrogeek](https://github.com/Chrogeek), [CoelacanthusHex](https://github.com/CoelacanthusHex), [FinParker](https://github.com/FinParker), [Great-designer](https://github.com/Great-designer), [HeRaNO](https://github.com/HeRaNO), [Ir1d](https://github.com/Ir1d), [Marcythm](https://github.com/Marcythm), [megakite](https://github.com/megakite), [opsiff](https://github.com/opsiff), [Persdre](https://github.com/Persdre), [untitledunrevised](https://github.com/untitledunrevised), [yanboishere](https://github.com/yanboishere)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
